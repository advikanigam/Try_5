$(document).ready(function(){


	$('#show').click(show)

	function show(){
		

		let fn = $('#firstname').val()
		let ps = $('#password').val()
		

		//alert(fn)

		let obj = {firstname: fn, password:ps}

		$.ajax({
			method: 'POST',
			url: 'http://127.0.0.1:5000/a',
			contentType: 'application/json',
			data: JSON.stringify(obj)
		})

		.done(function(res){
			if(res ==0)
			{
				alert("User Does Not Exist!")
			}
			else if(res ==2)
			{
				location.href='mode.html'
			}
			else if(res==1)
			{
				alert("Password does not match")

			}
			else if(res ==10)
			{
				alert("Please use the sign in option to create a new user! This user does not exist!")
			}
			else
			{
				alert("Please enter both the user name and password")
			}
			
				

		})
		.fail(function(xhr, status, error){
			alert(status)
		})

	}

	$('#newuser').click(newuser)

	function newuser()
	{

		let fn = $('#firstname').val()
		let ps1 = $('#password1').val()
		let ps2= $('#password2').val()

		let obj = {firstname: fn, password1:ps1, password2: ps2}

		$.ajax({
			method: 'POST',
			url: 'http://127.0.0.1:5000/b',
			contentType: 'application/json',
			data: JSON.stringify(obj)
		})

		.done(function(res){
			if(res ==1)
			{
				alert("passwords not same")
			}
			else if(res ==0)
			{
				alert("username already exists")
			}
			else if(res==500)
			{
				alert("Please enter a user name and password")
			}
			else if(res==10)
			{
				alert("Inserted")
				location.href='index.html'
			}
			else
			{
				alert(res)
			}
				

		})
		.fail(function(xhr, status, error){
			alert(error)
		})


		
	}



	$('#profile').click(profile)

	function profile()
	{
		
		let fn = $('#name').val()
		let ad= $('#Address').val()
		let ph = $('#Phone').val()

		let obj = {name: fn, Address: ad, Phone:ph }

		$.ajax({
			method: 'POST',
			url: 'http://127.0.0.1:5000/c',
			contentType: 'application/json',
			data: JSON.stringify(obj)
		})

		.done(function(res){

			if(res ==0)
			{
				alert("Client Inserted in Database")
				location.href='phonesystem.html'
			}
		    else
		    {
				alert("Client already exists in the system!")
			}
			
			
				

		})
		.fail(function(xhr, status, error){
			alert(error)
		})


		
	}

})
