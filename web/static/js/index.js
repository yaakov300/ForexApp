
$(function() {  //this is jQuery's short notation for "fire all this when page is ready"
    $('#login').on('click', submitLogin);
    $('#register').on('click', submitRegister);
});


function submitRegister() {
    var email = $('#reg_email').val();
    var password = $('#reg_password').val();
    $.ajax({
		url:'/register',
		type:'GET',
		dataType:'json',
        data:{mail:email, password:password},
		success:function(data, status, xhr) {
            location.reload();
		},
		error:function(xhr, status, error) {
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}


function submitLogin() {
    var username = $('#login_username').val();
    var password = $('#login_password').val();
    $.ajax({
		url:'/login',
		type:'GET',
		dataType:'json',
        data:{username:username, password:password},
		success:function(data, status, xhr) {
            location.reload();
		},
		error:function(xhr, status, error) {
            alert(xhr.responseText);
			console.error(xhr, status, error);
		}
	});
}