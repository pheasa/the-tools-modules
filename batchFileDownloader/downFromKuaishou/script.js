// Get the video element using XPath
function getElementByXPath(xpath) {
  return document.evaluate(
    xpath,
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  ).singleNodeValue;
}
function downloadArrayAsJSON(array, filename) {
  // Convert the array to a JSON string
  const jsonContent = JSON.stringify(array);

  // Create a blob object with the JSON content and the 'application/json' content type
  const blob = new Blob([jsonContent], { type: 'application/json' });

  // Create a URL for the blob
  const url = URL.createObjectURL(blob);

  // Create a temporary anchor element
  const a = document.createElement('a');
  a.href = url;
  a.download
    = filename;

  // Trigger the download
  a.click();

  // Clean up by revoking the URL
  URL.revokeObjectURL(url);
}

// Your XPath expression
var videoElement = getElementByXPath('//*[@id="app"]/div[1]/section/div/div/div/div[1]/div[2]/div[1]/div[2]/video');
var list_link = new Array();

// Check if the element exists
if (videoElement) {
  console.log("Video element found!");

  // Create a MutationObserver to watch for changes in the video element
  var observer = new MutationObserver(function (mutationsList) {
    mutationsList.forEach(function (mutation) {
      if (mutation.type === "attributes") {
        console.log(mutation.target.getAttribute("src"));
        if (!list_link.includes(mutation.target.getAttribute("src"))) {
          const get_link = mutation.target.getAttribute("src");
          if (get_link && !list_link.includes(get_link)) {
            list_link.push(get_link);
          }
          if (
            getElementByXPath(
              '//*[@id="app"]/div[1]/section/div/div/div/div[1]/div[2]/div[2]/div[2]'
            )
          ) {
            setTimeout(() =>
              getElementByXPath(
                '//*[@id="app"]/div[1]/section/div/div/div/div[1]/div[2]/div[2]/div[2]'
              ).click(),
              600);
          }
        }
      }
    });
  });

  // Start observing the video element for attribute changes
  observer.observe(videoElement, {
    attributes: true, // Watch for attribute changes
    childList: false, // Do not watch for child node changes
    subtree: false, // Do not observe the descendants
  });
} else {
  console.log("Video element not found.");
}

function executDownload() {
  downloadArrayAsJSON(list_link, 'for-testing.json')
}
