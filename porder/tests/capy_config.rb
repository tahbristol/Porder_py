require 'capybara'
require 'selenium-webdriver'
require 'pry'

driver_name = :selenium
browser_name = :chrome

Capybara.register_driver driver_name do |app|
  driver_options = {browser: browser_name}.merge({})
  Capybara::Selenium::Driver.new(app, driver_options)
end
