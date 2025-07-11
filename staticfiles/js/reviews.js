const reviewEditButtons = document.getElementsByClassName("btn-review-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const reviewSubmitButton = document.getElementById("reviewSubmitButton");

const reviewDeleteModal = new bootstrap.Modal(document.getElementById("reviewDeleteModal"));
const reviewDeleteButtons = document.getElementsByClassName("btn-review-delete");
const reviewDeleteConfirm = document.getElementById("reviewDeleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/
for (let button of reviewEditButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewContent;
    reviewSubmitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of reviewDeleteButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    reviewDeleteConfirm.href = `delete_review/${reviewId}`;
    reviewDeleteModal.show();
  });
}