require_relative 'capy_config'

class MembersOfCongress
	
	def initialize
		@session = Capybara::Session.new(:selenium)
		@session.visit "https://localhost/congressplus/index.cfm?controller=Legislators"

		log_in('tyler', 'Looknow11@')
		panelShows?
		canadian_foot_print
	end
	
	def log_in(username, password)
		@session.fill_in('username', :with => username)
		@session.fill_in('password', :with => password)
		@session.click_button('Log In')
	end
	
	def panelShows?
		@session.click_link('Reports')
		
		if @session.has_content?("Select a Report")
			puts "Panel shown"
		else
			puts "Error: No Panel Shown"
		end
	end
	
	def canadian_foot_print
		@session.select('Canadian Footprint Report', :from => 'reportPanel_reportType')
		
		@session.within('#reportPanel_reportForm'){
			
			if @session.has_content?("Title")
				puts "Title Field Shown"
			else
				puts "Title Field Not Shown"
			 return
			end
			
			if @session.has_content?("Format")
				puts "Format Field Shown"
			else
				puts "Format Field Not Shown"
			 return
			end
			
		 	if @session.has_content?("EXTERNAL REPORT") && @session.has_content?("INTERNAL REPORT")
				puts "Report Fields Shown"
			else
				puts "Report Fields Not Shown"
			 return
			end
			
			if @session.find('.buttonDiv input')
					puts "Generate Report Button Shown"
			else
				puts "Generate Report Button Not Shown"
				return
			end
			
		}

		@session.click_button("Generate Report")
		
		if @session.has_content?("This may take a few minutes, please be patient") && @session.find('#cancelLoadingBut')
			puts "Loading Panel Shown"
		else
			puts "Loading Panel Not Shown"
		end
			
	end
end


moc = MembersOfCongress.new