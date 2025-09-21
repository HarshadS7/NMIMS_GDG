// Dark/Light mode toggle
const themeSwitch = document.getElementById('themeSwitch');

if (!localStorage.getItem('theme')) localStorage.setItem('theme', 'dark');
document.body.classList.add(localStorage.getItem('theme'));
themeSwitch.checked = localStorage.getItem('theme') === 'light';

themeSwitch.addEventListener('change', () => {
  if (themeSwitch.checked) {
    document.body.classList.replace('dark', 'light');
    localStorage.setItem('theme', 'light');
  } else {
    document.body.classList.replace('light', 'dark');
    localStorage.setItem('theme', 'dark');
  }
});

const logoutBtn = document.getElementById("logoutBtn");

logoutBtn.addEventListener("click", () => {
    // Redirect to the landing/index page
    window.location.href = "/";
});