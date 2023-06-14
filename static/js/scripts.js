/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

$(document).ready(function(){
        var date_input=$('input[name="birthdayDate"]'); //our date input has the name "birthdayDate"
        var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
        date_input.datepicker({
            format: 'mm/dd/yyyy',
            container: container,
            todayHighlight: true,
            autoclose: true,
        })
    })

// Match the password and confirm password....  
  // check the password and confirm password are same and valid.....
  
  function verifyPassword() {  
    var pw = document.getElementById("passw1").value;  
    var pw2 = document.getElementById("passw2").value;  

    //check empty password field  
   //minimum password length validation  
    if(pw.length < 8) {  
       document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";  
       return false;  
    }    
  //maximum length of password validation  
    else if(pw.length > 15) {  
       document.getElementById("message").innerHTML = "**Password length must not exceed 15 characters";  
       return false;  
    } 
    else if(pw1 != pw2)  
    {   
      alert("Passwords did not match");  
    } else {  
      alert("Password created successfully");  
    }  

  }  