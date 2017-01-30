{-# LANGUAGE OverloadedStrings #-}
module Visie where

import WebOutput
import Paths_visie (getDataFileName)
import qualified Data.Text as T
import qualified Data.Text.IO as T
import Visie.Index

data D3Version = Version2 | Version3 | Version4 deriving Eq

-- resource description specified by the user, to be fetched from the
-- `data/` directory in the user package and transformed into a
-- Resource to be served
data ResourceDesc =  ResourceDesc {
  fetch :: FilePath,
  serve :: String
}

data Options = Options {
  d3Version :: D3Version,
  indexType :: IndexType,
  scriptDesc :: ResourceDesc,
  styleDesc :: ResourceDesc,
  additionalScripts :: [ResourceDesc]
}

defaultOptions = Options {
  d3Version = Version4,
  indexType = SVG,
  scriptDesc = ResourceDesc "data/script.js" "script.js",
  styleDesc = ResourceDesc "data/style.css" "style.css",
  additionalScripts = []
  }

getResource fileNameGetter (ResourceDesc { fetch = f, serve = s}) = do
  fileName <- fileNameGetter f
  content <- T.readFile fileName
  return Resource { location = s, content = content }

-- common resources are included in the Visie package and can use the
-- local getter
getCommonResource = getResource getDataFileName

d3FileNameFromOptions o
  | v == Version2 = "d3.v2.js"
  | v == Version3 = "d3.v3.js"
  | v == Version4 = "d3.v4.js"
  where v = d3Version o
                                                      
getCommonResources options = do
  d3 <- getCommonResource d3ResourceDesc
  pure [index, d3]
    where d3FileName = d3FileNameFromOptions options
          scriptsToAdd = (map serve . additionalScripts) options
          index = Resource {
            location = "index.html",
            content = makeIndex d3FileName (indexType options) scriptsToAdd
            }
          d3ResourceDesc = ResourceDesc {
            fetch = "data/" ++ d3FileName,
            serve = d3FileName
            }

customVisie :: Options -> (FilePath -> IO FilePath) -> (a -> T.Text) -> a -> IO ()
customVisie options fileNameGetter transform d = do
  common <- getCommonResources options
  user <- sequence (map (getResource fileNameGetter) userDescriptors)
  manyToTheBrowser (common ++ user ++ [dRes])
  return ()
    where userDescriptors = [style, script] ++ additional
          additional = additionalScripts options
          style = styleDesc options
          script = scriptDesc options
          dRes = Resource {
            location = "data.js",
            content = (pad . transform) d
            }
          pad s = T.concat ["visie(", s, ")"]

visie = customVisie defaultOptions
