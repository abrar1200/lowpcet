// core/static/js/scripts.js

document.addEventListener("DOMContentLoaded", function () {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const sidebar = document.getElementById("sidebar");

    // Show the sidebar when clicking the hamburger icon
    hamburgerMenu.addEventListener("click", function () {
        // Toggle the sidebar visibility
        if (sidebar.style.left === "-250px") {
            sidebar.style.left = "0";  // Slide in
        } else {
            sidebar.style.left = "-250px";  // Slide out
        }
    });
});
document.getElementById('hamburger-menu').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('open');
});
// Sidebar Toggle Script
document.addEventListener("DOMContentLoaded", function () {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const sidebar = document.getElementById("sidebar");

    hamburgerMenu.addEventListener("click", function () {
        sidebar.classList.toggle("open");
    });
});
