document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector(".resume-form");

    if (form) {

        form.addEventListener("submit", function () {

            const button =
                form.querySelector("button[type='submit']");

            button.innerText = "Generating Resume...";

            button.disabled = true;

        });

    }

});