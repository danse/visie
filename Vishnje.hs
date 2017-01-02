module Vishnje (
  vishnje,
  vishnjeStandard,
  Style,
  Logic
  ) where

import WebOutput (multiToTheBrowser)
import Paths_vishnje (getDataFileName)

newtype Style = Style String
newtype Logic = Logic String

getDataFileContent fileNameGetter path = do
  fileName <- fileNameGetter path
  readFile fileName

getVishnjeFile = getDataFileContent getDataFileName

getStyleAndLogicData fileNameGetter = do
  style <- getDataFileContent fileNameGetter "data/style.css"
  logic <- getDataFileContent fileNameGetter "data/logic.js"
  return (Style style, Logic logic)

getCommonResources4 = do
  index <- getVishnjeFile "data/index.html"
  d3 <- getVishnjeFile "data/d3.v4.js"
  pure [("index.html", index), ("d3.v4.js", d3)]

-- Uses D3 version 2
getCommonResources2 = do
  index <- getVishnjeFile "data/index.v2.html"
  d3 <- getVishnjeFile "data/d3.v2.js"
  pure [("index.html", index), ("d3.v2.js", d3)]

vishnjeVersion :: IO [(FilePath, String)] -> (a -> String) -> Style -> Logic -> a -> IO ()
vishnjeVersion resourceGetter transform (Style style) (Logic logic) d = do
  common <- resourceGetter
  multiToTheBrowser (common ++ custom)
  return ()
    where custom = [styleRes, logicRes, dRes]
          styleRes = ("style.css", style)
          logicRes = ("logic.js", logic)
          dRes = ("data.js", (pad . transform) d)
          pad s = "vishnje(" ++ s ++ ")"

-- the default Vishnje call uses D3 version 4
vishnje = vishnjeVersion getCommonResources4
vishnje2 = vishnjeVersion getCommonResources2

vishnjeStandard :: (FilePath -> IO FilePath) -> (a -> String) -> a -> IO ()
vishnjeStandard fileNameGetter transform d = do
  (style, logic) <- getStyleAndLogicData fileNameGetter
  vishnje transform style logic d

vishnjeStandard2 fileNameGetter transform d = do
  (style, logic) <- getStyleAndLogicData fileNameGetter
  vishnje2 transform style logic d
