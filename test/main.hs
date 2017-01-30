import Visie
import Paths_visie (getDataFileName)
import qualified Data.Text as T

testVisie = visie getDataFileName (T.pack . show)

main = do
  testVisie [1, 2, 3]
  testVisie [1..50]
