chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "openTakeout") {
        chrome.tabs.create({ url: "https://takeout.google.com/settings/takeout" });
        sendResponse({ status: "Tab opened" });
    }
});
