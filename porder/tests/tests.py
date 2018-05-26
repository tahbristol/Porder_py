import capybara
import capybara.dsl as cb
import unittest
from selenium import webdriver

capybara.default_driver = "selenium"

class CapybaraTestCase(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_home_page(self):
		cb.visit('/home')
		import pdb; pdb.set_trace()
		
if __name__ == '__main__':
	unittest.main()