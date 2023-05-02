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

const whTooltips = {colorLinks: true, iconizeLinks: true, renameLinks: true};
const scriptTag = document.createElement('script');
scriptTag.src = 'https://wow.zamimg.com/js/tooltips.js';
document.body.appendChild(scriptTag);