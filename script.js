const form = document.getElementById('upload-form');
const imageInput = document.getElementById('image-input');
const predictionResultsDiv = document.getElementById('prediction-results');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission

  const formData = new FormData();
  formData.append('image', imageInput.files[0]);

  fetch('/predict-disease', { // Replace with your server-side script URL
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    predictionResultsDiv.textContent = Predicted Disease: ${data.disease}; // Assumes response includes 'disease' property
  })
  .catch(error => {
    console.error('Error:', error);
    predictionResultsDiv.textContent = 'Error predicting disease.';
  });

  imageInput.value = ''; // Clear the image input after submission
});
function redirectToNextPage() {
    // Submit the form
    document.getElementById('upload-form').submit();
}
