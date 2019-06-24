setTimeout(() => {
    clickDownload();

}, 2000);

function clickDownload() {
    const downloadButton = document.getElementsByClassName('download')[0];
    console.log('Got the download Button', downloadButton);
    downloadButton.click();
    setTimeout(clickNext, 100);
}

function clickNext() {
    const nextButton = document.getElementsByClassName('complete')[0];
    console.log('Got the next Button', nextButton);
    nextButton.click();
    setTimeout(clickDownload, 100);
}