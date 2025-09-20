// Dark/Light mode toggle
const themeSwitch = document.getElementById("themeSwitch");

// Initialize theme
if (!localStorage.getItem("theme")) localStorage.setItem("theme", "dark");
document.body.classList.add(localStorage.getItem("theme"));
themeSwitch.checked = localStorage.getItem("theme") === "light";

themeSwitch.addEventListener("change", () => {
    if (themeSwitch.checked) {
        document.body.classList.replace("dark", "light");
        localStorage.setItem("theme", "light");
    } else {
        document.body.classList.replace("light", "dark");
        localStorage.setItem("theme", "dark");
    }
});

// Password toggle
const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

if(togglePassword && password) {
    togglePassword.addEventListener("click", () => {
        if(password.type === "password") {
            password.type = "text";
        } else {
            password.type = "password";
        }
    });
}
