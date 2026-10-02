/* Role Selection */

let roles = document.querySelectorAll(".role");

roles.forEach(function(role) {

    role.addEventListener("click", function() {

        roles.forEach(function(item) {
            item.classList.remove("active");
        });

        role.classList.add("active");

    });

});


/* Show / Hide Password */

function showPassword() {

    let password = document.getElementById("password");

    if (password.type === "password") {

        password.type = "text";

    } else {

        password.type = "password";

    }

}