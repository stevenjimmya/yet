const button = document.getElementById("submit-btn")
const input = document.getElementById("intention-input")

button.addEventListener("click", function() {
    const intention = input.value
    console.log("Intention set:", intention)

    fetch("/set_intention", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ intention: intention })
    })
    .then(function(response) {
        return response.json()
    })
    .then(function(data) {
        console.log("Server response:", data)
    })
})

/*
document.getElementById goes and finds an HTML element by its id
button and input are variables that store those elements
addEventListener listens for a click on the button
input.value gets whatever text is currently in the input box
console.log prints something to the browser's hidden console, not the page itself
fetch sends a message to python server at that address
method: "POST" means we are sending data to the server
body: JSON.stringify(...) packages the intention text to send over
.then(...) what to do when python responds back

*/