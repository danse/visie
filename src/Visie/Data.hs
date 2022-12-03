{-# LANGUAGE OverloadedStrings #-}
module Visie.Data where

import Visie.ToTimeSeries

import Data.List (sortOn)
import Data.Scientific (fromFloatDigits)
import Data.Time (UTCTime)
import Data.Time.Format (formatTime, defaultTimeLocale)

import qualified Data.Aeson as A
import qualified Data.Aeson.KeyMap as KeyMap
import qualified Data.Text as T
import qualified Data.Text.Lazy as TextLazy
import qualified Data.Text.Lazy.Encoding as TextLazy
import qualified Data.Vector as V

data TextFloat = TextFloat { getText :: T.Text, getFloat :: Float }

squashOrConcat a b
  | a == "" = b
  | b == "" = a
  | a == b = a
  | otherwise = T.concat [a, ", ", b]

instance Semigroup TextFloat where
  (<>) (TextFloat t1 f1) (TextFloat t2 f2) =
    TextFloat (squashOrConcat t1 t2) (f1 + f2)

instance Monoid TextFloat where
  mempty = TextFloat "" 0

toTimestampedTextFloat :: (T.Text, Float, UTCTime) -> Timestamped TextFloat
toTimestampedTextFloat (te, fl, ti) = Timestamped (TextFloat te fl) ti

dateFormat :: UTCTime -> T.Text
dateFormat = T.pack . formatTime defaultTimeLocale "%D"

toText :: [Timestamped TextFloat] -> T.Text
toText =
  let single (Timestamped (TextFloat te fl) ti) =
        A.Object
        (KeyMap.fromList
         [("key",   A.String te),
          ("value", (A.Number . fromFloatDigits) fl),
          ("date",  (A.String . dateFormat) ti)])
  in TextLazy.toStrict . TextLazy.decodeUtf8 . A.encode . A.toJSON . A.Array . V.fromList . map single . sortOn getTime
