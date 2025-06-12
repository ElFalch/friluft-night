const postEditButtons = document.getElementsByClassName("btn-post-edit");
const postText = document.getElementById("id_content");
const postForm = document.getElementById("postForm");
const postSubmitButton = document.getElementById("postSubmitButton");

const postDeleteModal = new bootstrap.Modal(document.getElementById("postDeleteModal"));
const postDeleteButtons = document.getElementsByClassName("btn-post-delete");
const postDeleteConfirm = document.getElementById("postDeleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `postEditButtons` collection:
* - Retrieves the associated post's ID upon click.
* - Fetches the content of the corresponding post.
* - Populates the `postText` input/textarea with the post's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_post/{postId}` endpoint.
*/ 
for (let button of postEditButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    let postContent = document.getElementById(`post${postId}`).innerText;
    postText.value = postContent;
    postSubmitButton.innerText = "Update";
    postForm.setAttribute("action", `edit_post/${postId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `postDeleteButtons` collection:
* - Retrieves the associated posts's ID upon click.
* - Updates the `postDeleteConfirm` link's href to point to the 
* deletion endpoint for the specific post.
* - Displays a confirmation modal (`postDeleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of postDeleteButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    postDeleteConfirm.href = `delete_post/${postId}`;
    postDeleteModal.show();
  });
}