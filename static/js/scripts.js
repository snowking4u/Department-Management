document.addEventListener("DOMContentLoaded", function () {

    const roleButtons = document.querySelectorAll(".role");

    roleButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            roleButtons.forEach(function (btn) {
                btn.classList.remove("active");
            });

           
            this.classList.add("active");

        });

    });

});