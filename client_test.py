import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def assertQuotes(self, quotes):
    for quote in quotes:
      price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'], quote['top_ask']['price'], price))
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertQuotes(quotes)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertQuotes(quotes)

  """ ------------ Add more unit tests ------------ """
  def test_price_a_zero(self):
    self.assertEqual(getRatio(0, 2), 0)

  def test_price_b_zero(self):
    self.assertIsNone(getRatio(10, 0))

  def test_both_positive(self):
      self.assertEqual(getRatio(10, 2), 5)

  def test_price_a_negative(self):
    self.assertEqual(getRatio(-10, 2), -5)

  def test_price_b_negative(self):
    self.assertEqual(getRatio(10, -2), -5)

  def test_both_negative(self):
    self.assertEqual(getRatio(-10, -2), 5)



if __name__ == '__main__':
    unittest.main()
