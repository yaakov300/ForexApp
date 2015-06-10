

$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#login_button').on('click', submitLogin);
    $('#register_button').on('click', submitRegister);


});


function submitRegister() {
    var email = $('#reg_email').val();
    var password = $('#reg_password').val();
    $.ajax({
		url:'/register',
		type:'POST',
		dataType:'json',
        data:{mail:email, password:password},
		success:function(data, status, xhr) {

		},
		error:function(xhr, status, error) {
           // alert(xhr.responseText);

		}
	});
}


function submitLogin() {
    var username = $('#login_username').val();
    var password = $('#login_password').val();
    $.ajax({
		url:'/login',
		type:'POST',
		dataType:'json',
        data:{username:username, password:password},
        success:function(data, status, xhr)
        {
            alert('success');
            window.location.href = "/home";
		},
		error:function(xhr, status, error)
        {
            alert('error');
            alert(xhr.status);
            alert(xhr.responseText);
            console.error(xhr, status, error);
            window.location.href = "/login";

        }
	});
}