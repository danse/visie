import Vishnje (vishnjeStandard)
import Paths_vishnje (getDataFileName)

testVishnje = vishnjeStandard getDataFileName show

main = do
  testVishnje [1, 2, 3]
  testVishnje [1..50]
