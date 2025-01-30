document.getElementById('uploadBox').addEventListener('click', () => {
    document.getElementById('fileInput').click();
});

document.getElementById('convertBtn').addEventListener('click', async () => {
    let files = document.getElementById('fileInput').files;
    if (files.length === 0) {
        alert("Please upload at least one image.");
        return;
    }

    let formData = new FormData();
    for (let file of files) {
        formData.append('images', file);
    }

    let response = await fetch('/convert', { method: 'POST', body: formData });
    let blob = await response.blob();
    let url = window.URL.createObjectURL(blob);
    
    let downloadLink = document.getElementById('downloadLink');
    downloadLink.href = url;
    downloadLink.style.display = "block";
});