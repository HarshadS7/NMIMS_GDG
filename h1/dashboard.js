// Theme toggle
const themeSwitch = document.getElementById("themeSwitch");
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

// Sidebar toggle
const sidebar = document.getElementById("sidebar");
const menuToggle = document.getElementById("menuToggle");

menuToggle.addEventListener("click", () => {
  sidebar.classList.toggle("collapsed");
});

// Charts
const expenseCtx = document.getElementById("expenseChart");
const incomeCtx = document.getElementById("incomeChart");

new Chart(expenseCtx, {
  type: "doughnut",
  data: {
    labels: ["Food", "Transport", "Rent", "Other"],
    datasets: [{
      data: [300, 150, 800, 350],
      backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"]
    }]
  }
});

new Chart(incomeCtx, {
  type: "bar",
  data: {
    labels: ["Salary", "Freelance", "Investments"],
    datasets: [{
      label: "Income",
      data: [2000, 500, 300],
      backgroundColor: ["#36A2EB", "#4BC0C0", "#9966FF"]
    }]
  }
});
