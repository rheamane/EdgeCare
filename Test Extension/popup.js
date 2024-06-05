// Service worker cant manipulate DOM
document.getElementById("openTakeout").addEventListener("click", () => {
    chrome.runtime.sendMessage({ action: "openTakeout" }, response => {
        console.log(response.status);
    });
});
