const postEditButtons = document.getElementsByClassName("btn-post-edit");
const postText = document.getElementById("id_content");
const postForm = document.getElementById("postForm");
const submitButton = document.getElementById("submitButton");

const postDeleteModal = new bootstrap.Modal(document.getElementById("postdeleteModal"));
const postDeleteButtons = document.getElementsByClassName("btn-post-delete");
const postDeleteConfirm = document.getElementById("postdeleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of postEditButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    let postContent = document.getElementById(`post${postId}`).innerText;
    postText.value = postContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_post/${postId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated posts's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific post.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of postDeleteButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    postDeleteConfirm.href = `delete_post/${postId}`;
    postDeleteModal.show();
  });
}