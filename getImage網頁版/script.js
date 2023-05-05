let btn = document.querySelector(".btn");
btn.onclick = () => {
  const input_image = document.getElementById("imageUrl").value;
  const encoded_image = encodeURIComponent(input_image);
  const data = { value: encoded_image };
  fetch("api.php", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((response) => response.text())
    .then((res) => {
    //   console.log(res);
      JSON.parse(res).forEach((link) => {
        const div = document.createElement("div");
        const img = document.createElement("img");
        const a = document.createElement("a");

        const parts = link.split("/");
        const fileName = parts[parts.length - 1];

        a.href = link;
        a.textContent = "下載圖片";

        img.src = link;
        img.alt = fileName;

        const downloadImage = document.querySelector(".downloadImage");

        div.append(img);
        div.append(a);

        downloadImage.append(div);
      });
    })
    .catch((error) => console.error(error));
};
