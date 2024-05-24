var intervalId;

function startSendingLocation() {
    intervalId = setInterval(sendLocation, 30000);
}

function stopSendingLocation() {
    if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
    }
}

function sendLocation() {
    fetch("/send_location")
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("result").innerText = data.result;
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}
