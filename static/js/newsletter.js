$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    form =$("form")

    $.ajax({
      'url':'/ajax/newsletter/',
      'type':'POST',
      'data':form.serialize(),
      'dataType': 'json',
      'success':function(data){
        alert(data['success'])
      },
    })//End of ajax method
    $('#id_your_name').val('')
    $('#id_email').val('')
  }) //end of submit event
})// end of document ready function