let modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
let images = document.querySelectorAll("img");
for (image of images) {
    if (!image.src.includes("static/")) {
        image.addEventListener("click", (event) =>{
            let span = document.createElement("span");
            modal.appendChild(span)
            span.classList.add("close");
            span.innerHTML = "&times;";
            let newImg = document.createElement("img");
            newImg.src = event.target.src;
            modal.appendChild(newImg)
            modal.style.display = "block";
            newImg.classList.add("modal-personal-content");
            span.addEventListener("click", (event) =>{
                modal.style.display = "none";
                modal.removeChild(newImg)
            })
        })
    }
}


/**
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  img.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}*/