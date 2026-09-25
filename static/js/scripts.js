

        function togglePassword() {

            const password =
                document.getElementById("password");

            if (password.type === "password") {

                password.type = "text";

            } else {

                password.type = "password";

            }

        }


        const roleButtons =
            document.querySelectorAll(".role-btn");

        roleButtons.forEach(button => {

            button.addEventListener("click", () => {

                roleButtons.forEach(btn => {
                    btn.classList.remove("active");
                });

                button.classList.add("active");

            });

        });


