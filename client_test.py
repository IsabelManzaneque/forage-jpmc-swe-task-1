import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
    
  def test_getDataPoint_calculatePrice(self):
      
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        result = getDataPoint(quote)
        expectedResult = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2 )
        self.assertEqual(result, expectedResult)
    
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
      
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        result = getDataPoint(quote)
        expectedResult = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2 )
        self.assertEqual(result, expectedResult)
        
        

  """ ------------ Add more unit tests ------------ """
  
  def test_getRatio(self):
      
      prices = [(110.755, 112.035), (110.31,112.035), (110.31,112.035), (110.31,112.035)]
      for price in prices:
          expectedRatio = price[0]/price[1]
          ratio = getRatio(price[0], price[1])
          self.assertEqual(ratio, expectedRatio)

  def test_getRatio_BisCero(self):
      
      prices = [(110.755,0), (110.31,0), (110.31,0), (110.31,0)]
      for price in prices:
          expectedRatio = None
          ratio = getRatio(price[0], price[1])
          self.assertEqual(ratio, expectedRatio)
      
        
  def test_getRatio_AisCero(self):
       
       prices = [(0,112.035), (0,112.035), (0,112.035), (0,112.035)]
       for price in prices:
           expectedRatio = 0
           ratio = getRatio(price[0], price[1])
           self.assertEqual(ratio, expectedRatio)


if __name__ == '__main__':
    unittest.main()
