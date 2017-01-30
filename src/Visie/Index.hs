{-# LANGUAGE OverloadedStrings #-}
module Visie.Index where

import qualified Data.Text as T

data IndexType = SVG | ChartDiv deriving Eq

makeIndex d3FileName indexType = T.concat [start, d3, content, end]
  where start = "<!DOCTYPE html> <meta charset=\"utf-8\"> <link rel=\"stylesheet\" href=\"style.css\">"
        d3 = T.concat ["<script type=\"text/javascript\" src=\"", T.pack d3FileName, "\"></script>"]
        content = (if indexType == SVG then "<svg width=\"900\" height=\"500\"></svg>" else "<div class=\"chart\"></div>")
        end = "<script type=\"text/javascript\" src=\"script.js\"></script> <script type=\"text/javascript\" src=\"data.js\"></script>"
