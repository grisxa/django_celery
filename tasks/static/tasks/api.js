window.addEventListener("load", function () {
    Array.from(document.getElementsByTagName("span"))
        .forEach(span => span.getAttribute("class") == "pending" ? monitorTask(span.id.slice("span-".length)) : null);
});

function expandResponse(response) {
    return Promise.all([response, response.text()])
        .then(([response, text]) => {
            if (response.ok) {
                return text
            }
            throw new Error(response.statusText)
        })
}

function getStatus(id) {
    return fetch(`/tasks/${id}/status`)
        .then(expandResponse)
        .then(response => {
            const span = document.getElementById(`span-${id}`);
            if (span) {
                span.innerText = response;
                span.setAttribute("class", response.toLowerCase());
            }
            const button = document.getElementById(`button-${id}`);
            if (button) {
                button.style.display = 'none';
            }
            return response;
        })
        .catch(error => {
            console.error("Status has failed", error);
            throw error;
        })
}

function monitorTask(id) {
    const intervalId = setInterval(() => getStatus(id)
            .then(response => response == "Ready" ? clearInterval(intervalId) : null)
            .catch(() => clearInterval(intervalId)),
        10000);
}

function startTask(id) {
    fetch(`/tasks/${id}/start`)
        .then(expandResponse)
        .then(() => getStatus(id))
        .then(() => monitorTask(id))
        .catch(error => console.error("Starting has failed", error))
}
