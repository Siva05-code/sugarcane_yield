document.addEventListener("DOMContentLoaded", function () {
    let alertBox = document.querySelector(".alert");
    if (alertBox) {
        setTimeout(() => {
            alertBox.style.display = "none";
        }, 3000);
    }
});
