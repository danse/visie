{-# LANGUAGE OverloadedStrings #-}
module Visie.Index where

import qualified Data.Text as T

data IndexType = SVG | ChartDiv deriving Eq

scriptElement loc = T.concat ["<script type=\"text/javascript\" src=\"", T.pack loc, "\"></script>"]

makeIndex d3FileName indexType additionalScripts = T.concat [start, content, scripts]
  where start = "<!DOCTYPE html> <meta charset=\"utf-8\"> <link rel=\"stylesheet\" href=\"style.css\">"
        content = (if indexType == SVG then "<svg width=\"900\" height=\"500\"></svg>" else "<div class=\"chart\"></div>")
        d3 = scriptElement d3FileName
        mainScript = scriptElement "script.js"
        dataScript = scriptElement "data.js"
        scripts = T.concat (d3 : map scriptElement additionalScripts ++ [mainScript, dataScript])
