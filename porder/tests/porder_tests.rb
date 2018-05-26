require_relative 'capy_config'

class PorderTests
	
		def initialize
			@session = Capybara::Session.new(:selenium)
		end
		
		def visit_home
			@session.visit('http://localhost:5000/home')
			
			if @session.has_content?("Welcome to pOrder")
				puts "visit_home: Passed"
			else
				puts "visit_home: Failed"
			end
			
		end
		
end

new_test = PorderTests.new 
new_test.visit_home