// Created a makeshift sleep function to use in setFilters()
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function setFilters() {
    try {
        // Get the desect button by classname
        var buttons = document.getElementsByClassName('mUIrbf-LgbsSe mUIrbf-LgbsSe-OWXEXe-dgl2Hf wMI9H');
        const deselectButton = buttons[1];

        deselectButton.click();

        // Adding awaits to ensure operations run after the prev one has been completed
        await sleep(1000)

        // Getting the Checkboxes
        let checkboxes = Array.from(document.getElementsByClassName('VfPpkd-muHVFf-bMcfAe'));
        let youtubeCheckbox = checkboxes[checkboxes.length - 1];    // Youtube Checkbox is the last one
        youtubeCheckbox.click();

        await sleep(500);
        // Getting the next button by class
        let nextButton = document.getElementsByClassName('UywwFc-LgbsSe UywwFc-LgbsSe-OWXEXe-dgl2Hf wMI9H iK4Buc')[0];
        nextButton.click();

        await sleep(500);
        // Export button and next button have the same class (which has 2 elements)
        let exportButton = document.getElementsByClassName('UywwFc-LgbsSe UywwFc-LgbsSe-OWXEXe-dgl2Hf wMI9H iK4Buc')[1];
        exportButton.click();
    }
    catch (error) {
        console.log("An error occured: ", error)
    }
}

setFilters();