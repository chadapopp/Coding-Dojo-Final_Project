function handleEditFormSubmission(event, listingId) {
    event.preventDefault();
    hideMessages();

    // Get the form data to be edited
    const title = document.querySelector('input[name="title"]').value;
    const description = document.querySelector('input[name="description"]').value;
    const rate = document.querySelector('input[name="rate"]').value;
    const location = document.querySelector('input[name="location"]').value;
    const availability = document.querySelector('input[name="availability"]').value;

    // Validate the form data
    if (!validateFormData(title, description, rate, location, availability)) {
        showErrorMessage("Please fill in all the required fields.");
        return;
    }

    // Prepare the data to be sent to the server
    const formData = new FormData();
    formData.append("title", title);
    formData.append("description", description);
    formData.append("rate", rate);
    formData.append("location", location);
    formData.append("availability", availability);

    // Create an XMLHttpRequest
    const xhr = new XMLHttpRequest();

    xhr.onload = function () {
        const response = JSON.parse(xhr.response);
        if ("error" in response) {
            showErrorMessage(response.error);
        } else if ("success" in response) {
            const redirect_path = response.redirect_path;
            window.location.href = redirect_path;
        } else {
            showErrorMessage("Unknown server response");
        }
        console.log(xhr.response);
    };

    xhr.open("POST", `/edit_listing/${listingId}`);
    xhr.send(formData);
    console.log(formData);
}
