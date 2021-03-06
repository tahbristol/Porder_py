$(document).ready(function() {
	
	if ($('#flashMessage')) {
		setTimeout(function() {
			$('#flashMessage').fadeOut('slow')
		}, 3000);
	}
	
  $("#addLine").on("click", function() {
    let table = $('.requests');
    table.append('<tr><td><input id="item" name="request[][item]"></td><td><input id="price" name="request[][price]"></td><td><input id="quantity" name="request[][quantity]"></td><td><input id="vendor" name="request[][vendor]"></td><td><input id="url" name="request[][url]"></td></tr>');
  });


  $(".userRequests").on("click", function() {

  });

  $(".requestDeleteCheck").on("click", function() {
    let parent = $(this).parent();
    parent.parent().toggleClass("highlight");
  });

  $("#guestBox").on("click", function() {
    if ($(this).prop("checked") == false) {
      $('#inputEmail').val('');
      $('#inputPassword').val('');
    } 
		else if ($(this).prop("checked") == true) {
			$('#inputEmail').val('guest@account.com');
      $('#inputPassword').val('password');
    }
  });
	
	Array.prototype.forEach.call($('.userItemsList'), function(item){
		$(item).on('click', function(e){
			let id = $(this).attr('id').split('-')[1]
			window.location = `/items/${id}/edit`;
		})
	})
});