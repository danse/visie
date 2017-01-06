import Vishnje (vishnjeFiles)
import Paths_vishnje (getDataFileName)
import qualified Data.Text as T

testVishnje = vishnjeFiles getDataFileName (T.pack . show)

main = do
  testVishnje [1, 2, 3]
  testVishnje [1..50]
