$(document).ready(function(){
	$('#addItem').on('click', function(){
		let data = {};
		makeDisplayTemplate("",'#newItemTemplate','#itemsListForForm')
	})
})

function makeDisplayTemplate(data, template, output) {
	debugger
	let displayTemplate =  $(template).html();
	let finalTemplate = Handlebars.compile(displayTemplate);
	let html = finalTemplate(data);
	$(output).append(html);
}