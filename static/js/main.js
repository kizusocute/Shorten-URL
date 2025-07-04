document.getElementById("shorten-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const urlInput = document.getElementById("url-input").value;
    const message = document.getElementById("message");

    const res = await fetch("/shorten", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: urlInput })
    });

    const data = await res.json();

    if (res.ok) {
        document.getElementById("result").classList.remove("hidden");
        document.getElementById("short-url").value = data.short_url;
        message.textContent = "Rút gọn thành công!";
    } else {
        document.getElementById("result").classList.add("hidden");
        message.textContent = data.error || "Có lỗi xảy ra";
    }
});

function copyToClipboard() {
    const copyText = document.getElementById("short-url");
    copyText.select();
    document.execCommand("copy");
    alert("Đã copy URL!");
}

