module Visie.ToTimeSeries where

import Data.DateTime (DateTime)
import Data.List (sortOn)
import Data.Time.Clock (NominalDiffTime,addUTCTime)
import Data.Ord (compare)
import Data.Time (UTCTime)

data Timestamped a = Timestamped { getStamped :: a, getTime :: UTCTime }

fill :: Monoid a => DateTime -> Timestamped a
fill t = Timestamped mempty t

-- | sort `elements` concatenating their monoid when their time falls
-- within the same interval
convert :: Monoid a => NominalDiffTime -> [Timestamped a] -> [Timestamped a]
convert interval elements = sampler sorted
  where sorted = sortOn getTime elements
        times = iterator interval (getTime (head sorted))
        sampler = consume times
        iterator :: NominalDiffTime -> DateTime -> [DateTime]
        iterator interval start = iterate (addUTCTime interval) start
        -- at every call, the recursive function returns a processed list, and
        -- it gets a non processed list and a reference date about the last
        -- emitted element. if the next element would have a date greater than
        -- the reference + the interval, a filling element is
        -- created. otherwise, the function will look ahead and merge all
        -- elements within the same interval, pick a representative date for
        -- the merged elements and use it as the new reference
        consume :: Monoid a => [DateTime] -> [Timestamped a] -> [Timestamped a]
        consume (t:ts) [] = []
        consume (t:ts) elements
          | length preceding == 0 = filled : rest
          | otherwise = foldl (merge t) filled preceding : rest
          where (preceding, succeeding) = span ((<= t) . getTime) elements
                filled = fill t
                rest = consume ts succeeding
                merge :: Monoid a => DateTime -> Timestamped a -> Timestamped a -> Timestamped a
                merge t (Timestamped a _) (Timestamped b _) = Timestamped (mappend a b) t

convertFill :: Monoid a => DateTime -> NominalDiffTime -> [Timestamped a] -> [Timestamped a]
convertFill dateTime interval elements = convert interval filledElements
  where filledElements = (fill dateTime):elements
