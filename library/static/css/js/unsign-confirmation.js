function confirmUnsign(button) {
    if (confirm("Are you sure you want to unsign from this event?")) {
        button.form.submit();
    }
}