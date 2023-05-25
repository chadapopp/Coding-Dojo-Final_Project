const form = document.querySelector("#form-upload");
const errorMessageDiv = document.querySelector("#error-div");
const successMessageDiv = document.querySelector("#success-div");

// Helper functions
function showErrorMessage(message) {
    errorMessageDiv.innerHTML = message;
    errorMessageDiv.style.display = "block";
}

function showSuccessMessage(message) {
    successMessageDiv.innerHTML = message;
    successMessageDiv.style.display = "block";
}

function hideMessages() {
    errorMessageDiv.style.display = "none";
    successMessageDiv.style.display = "none";
}

form.addEventListener("submit", handleFormSubmission);

/*
Steps to upload a file
1) We need to grab the file that we want to upload
2) Upload the file
3) Check the server response if it's success show a success message
4) Check the server response if its a failed response, show an error message
*/

function handleFormSubmission(event) {
    event.preventDefault();
    hideMessages();

    const input = document.querySelector('input[type="file"]');
    const files = input.files;

    const title = document.querySelector('input[name="title"]').value;
    const description = document.querySelector('input[name="description"]').value;
    const rate = document.querySelector('input[name="rate"]').value;
    const location = document.querySelector('input[name="location"]').value;
    const availability = document.querySelector('input[name="availability"]').value;
    const user_id = document.querySelector('input[name="user_id"]').value;
    const listing_id = document.querySelector('input[name="listing_id"]').value;

    // Validate the form data
    if (!validateFormData(title, description, rate, location, availability)) {
        // If the validation fails, show an error message or perform any other desired actions
        showErrorMessage("Please fill in all the required fields.");
        return;
    }

    const formData = new FormData();
    formData.append("title", title);
    formData.append("description", description);
    formData.append("rate", rate);
    formData.append("location", location);
    formData.append("availability", availability);
    formData.append("user_id", user_id);
    formData.append("listing_id", listing_id);

    for (let i = 0; i < files.length; i++) {
        formData.append("add_photos[]", files[i]);
    }

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

    xhr.open("POST", "/create_listing");
    xhr.send(formData);
    console.log(formData);
}

// Validation function for the form data
function validateFormData(title, description, rate, location, availability) {
    if (title.trim().length === 0) {
        showErrorMessage("What do you call your listing.");
        return false;
    }
    if (description.trim().length === 0) {
        showErrorMessage("Tell us about it.");
        return false;
    }
    if (rate.trim().length === 0) {
        showErrorMessage("How much per night/day?");
        return false;
    }
    if (location.trim().length === 0) {
        showErrorMessage("Where can they pick the camper up?");
        return false;
    }
    if (availability.trim().length === 0) {
        showErrorMessage("When can they start renting?");
        return false;
    }
    return true;
}

// Function to show an error message
function showErrorMessage(message) {
    const errorDiv = document.getElementById('error-div');
    errorDiv.innerText = message;
    errorDiv.style.display = 'block';
}

// Function to hide error messages
function hideMessages() {
    const errorDiv = document.getElementById('error-div');
    errorDiv.style.display = 'none';
}


    
    
    
