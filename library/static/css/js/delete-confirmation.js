function confirmDelete(button) {
    if (confirm("Are you sure you want to delete this character?")) {
        button.form.submit();
    }
}