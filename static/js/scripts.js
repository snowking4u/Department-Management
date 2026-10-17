
// ROLE SELECTION
let roles = document.querySelectorAll(".role");
let selectedRole = document.getElementById("selected-role");

roles.forEach(function(role) {

    role.addEventListener("click", function() {

        // Remove active class from all roles
        roles.forEach(function(item) {
            item.classList.remove("active");
        });

        // Activate selected role
        role.classList.add("active");

        // Save selected role in hidden input
        selectedRole.value = role.dataset.role;

    });

});


// SHOW / HIDE PASSWORD
function showPassword() {

    let password = document.getElementById("password");

    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }

}
