import Vishnje (vishnjeFiles)
import Paths_vishnje (getDataFileName)

testVishnje = vishnjeFiles getDataFileName show

main = do
  testVishnje [1, 2, 3]
  testVishnje [1..50]
