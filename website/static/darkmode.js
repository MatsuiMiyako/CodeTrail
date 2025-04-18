document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM loaded");

  let darkmode = localStorage.getItem("darkmode");
  const themeSwitch = document.getElementById("theme-switch");

  if (!themeSwitch) {
    console.error("Theme switch button not found!");
    return;
  }

  const enableDarkmode = () => {
    console.log("Dark mode enabled");
    document.body.classList.add("darkmode");
    localStorage.setItem("darkmode", "active");
  };

  const disableDarkmode = () => {
    console.log("Dark mode disabled");
    document.body.classList.remove("darkmode");
    localStorage.setItem("darkmode", null);
  };

  if (darkmode === "active") enableDarkmode();

  themeSwitch.addEventListener("click", () => {
    darkmode = localStorage.getItem("darkmode");
    darkmode !== "active" ? enableDarkmode() : disableDarkmode();
  });
});
