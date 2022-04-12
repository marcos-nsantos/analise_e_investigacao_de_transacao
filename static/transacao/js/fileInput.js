const fileInput = document.querySelector('#fileInput input[type=file]');
fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
        const fileName = document.querySelector('#fileInput .file-name');
        fileName.textContent = fileInput.files[0].name;
    }
}