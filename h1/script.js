// === Theme toggle ===
const themeSwitch = document.getElementById("themeSwitch");

if (!localStorage.getItem("theme")) localStorage.setItem("theme", "dark");
document.body.classList.add(localStorage.getItem("theme"));
if (themeSwitch) themeSwitch.checked = localStorage.getItem("theme") === "light";

if (themeSwitch) {
  themeSwitch.addEventListener("change", () => {
    if (themeSwitch.checked) {
      document.body.classList.replace("dark", "light");
      localStorage.setItem("theme", "light");
    } else {
      document.body.classList.replace("light", "dark");
      localStorage.setItem("theme", "dark");
    }
  });
}

// === Password toggle (login/signup only) ===
const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

if (togglePassword && password) {
  togglePassword.addEventListener("click", () => {
    password.type = password.type === "password" ? "text" : "password";
  });
}
