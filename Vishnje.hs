module Vishnje (
  vishnje,
  vishnjeFiles,
  Style,
  Logic,
  Options,
  D3Version,
  IndexType
  ) where

import WebOutput (multiToTheBrowser)
import Paths_vishnje (getDataFileName)

newtype Style = Style String
newtype Logic = Logic String

data D3Version = Version2 | Version4 deriving Eq
data IndexType = SVG | ChartDiv deriving Eq

data Options = Options {
  d3Version :: D3Version,
  indexType :: IndexType
}

defaultOptions = Options Version4 SVG

getDataFileContent fileNameGetter path = do
  fileName <- fileNameGetter path
  readFile fileName

getVishnjeFile = getDataFileContent getDataFileName

getStyleAndLogicData fileNameGetter = do
  style <- getDataFileContent fileNameGetter "data/style.css"
  logic <- getDataFileContent fileNameGetter "data/logic.js"
  return (Style style, Logic logic)

d3FileNameFromOptions (Options d3Version indexType)
  | d3Version == Version2 = "d3.v2.js"
  | d3Version == Version4 = "d3.v4.js"
                                                      

makeIndex options = concat [start, d3, content, end]
  where start = "<!DOCTYPE html> <meta charset=\"utf-8\"> <link rel=\"stylesheet\" href=\"style.css\">"
        d3 = "<script type=\"text/javascript\" src=\"" ++ d3FileNameFromOptions options ++ "\"></script>"
        content = (if indexType options == SVG then "<svg width=\"900\" height=\"500\"></svg>" else "<div class=\"chart\"></div>")
        end = "<script type=\"text/javascript\" src=\"logic.js\"></script> <script type=\"text/javascript\" src=\"data.js\"></script>"

getCommonResources options = do
  d3 <- getVishnjeFile ("data/" ++ d3FileName)
  pure [("index.html", makeIndex options), (d3FileName, d3)]
    where d3FileName = d3FileNameFromOptions options

customVishnje :: Options -> (a -> String) -> Style -> Logic -> a -> IO ()
customVishnje options transform (Style style) (Logic logic) d = do
  common <- getCommonResources options
  multiToTheBrowser (common ++ custom)
  return ()
    where custom = [styleRes, logicRes, dRes]
          styleRes = ("style.css", style)
          logicRes = ("logic.js", logic)
          dRes = ("data.js", (pad . transform) d)
          pad s = "vishnje(" ++ s ++ ")"

vishnje = customVishnje defaultOptions

customVishnjeFiles :: Options -> (FilePath -> IO FilePath) -> (a -> String) -> a -> IO ()
customVishnjeFiles options fileNameGetter transform d = do
  (style, logic) <- getStyleAndLogicData fileNameGetter
  customVishnje options transform style logic d

vishnjeFiles = customVishnjeFiles defaultOptions
