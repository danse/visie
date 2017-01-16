{-# LANGUAGE OverloadedStrings #-}
module Vishnje.Data where

import Vishnje.ToTimeSeries
import qualified Data.Text as T
import Data.Time (UTCTime)

data TextFloat = TextFloat { getText :: T.Text, getFloat :: Float }

squashOrConcat a b
  | a == "" = b
  | b == "" = a
  | a == b = a
  | otherwise = T.concat [a, ", ", b]

instance Monoid TextFloat where
  mempty = TextFloat "" 0
  mappend (TextFloat t1 f1) (TextFloat t2 f2) = TextFloat (squashOrConcat t1 t2) (f1 + f2)

toTimestampedTextFloat :: (T.Text, Float, UTCTime) -> Timestamped TextFloat
toTimestampedTextFloat (te, fl, ti) = Timestamped (TextFloat te fl) ti
