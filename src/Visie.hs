{-# LANGUAGE OverloadedStrings #-}
module Visie where

import WebOutput (multiToTheBrowser)
import Paths_visie (getDataFileName)
import qualified Data.Text as T
import qualified Data.Text.IO as T
import Visie.Index

newtype Style = Style T.Text
newtype Logic = Logic T.Text

data D3Version = Version2 | Version3 | Version4 deriving Eq

data Options = Options {
  d3Version :: D3Version,
  indexType :: IndexType,
  additionalResources :: [(String, T.Text)]
}

defaultOptions = Options Version4 SVG []

getDataFileContent fileNameGetter path = do
  fileName <- fileNameGetter path
  T.readFile fileName

getVisieFile = getDataFileContent getDataFileName

getStyleAndLogicData fileNameGetter = do
  style <- getDataFileContent fileNameGetter "data/style.css"
  logic <- getDataFileContent fileNameGetter "data/logic.js"
  return (Style style, Logic logic)

d3FileNameFromOptions o
  | v == Version2 = "d3.v2.js"
  | v == Version3 = "d3.v3.js"
  | v == Version4 = "d3.v4.js"
  where v = d3Version o
                                                      
getCommonResources options = do
  d3 <- getVisieFile ("data/" ++ d3FileName)
  pure [("index.html", makeIndex d3FileName (indexType options)), (d3FileName, d3)]
    where d3FileName = d3FileNameFromOptions options

customVisie :: Options -> (a -> T.Text) -> Style -> Logic -> a -> IO ()
customVisie options transform (Style style) (Logic logic) d = do
  common <- getCommonResources options
  multiToTheBrowser (common ++ custom ++ additional)
  return ()
    where custom = [styleRes, logicRes, dRes]
          styleRes = ("style.css", style)
          logicRes = ("logic.js", logic)
          dRes = ("data.js", (pad . transform) d)
          pad s = T.concat ["visie(", s, ")"]
          additional = additionalResources options

visie = customVisie defaultOptions

customVisieFiles :: Options -> (FilePath -> IO FilePath) -> (a -> T.Text) -> a -> IO ()
customVisieFiles options fileNameGetter transform d = do
  (style, logic) <- getStyleAndLogicData fileNameGetter
  customVisie options transform style logic d

visieFiles = customVisieFiles defaultOptions
