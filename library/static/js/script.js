function confirmDelete(button) {
    if (confirm("Are you sure you want to delete this character?")) {
        button.form.submit();
    }
}

function confirmUnsign(button) {
    if (confirm("Are you sure you want to unsign from this event?")) {
        button.form.submit();
    }
}