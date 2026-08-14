const messageInput = document.getElementById("message");
const askButton = document.getElementById("askButton");
const responseArea = document.getElementById("response");


askButton.addEventListener("click", async function () {

    const message = messageInput.value.trim();

    if (!message) {
        responseArea.textContent = "Please enter a message.";
        return;
    }

    responseArea.textContent = "Thinking...";

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (!response.ok) {
            responseArea.textContent =
                data.error || "Something went wrong.";

            return;
        }


        responseArea.textContent = data.response;


    } catch (error) {

        responseArea.textContent =
            "Could not connect to the server.";

        console.error(error);
    }

});