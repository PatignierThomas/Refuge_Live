// add a new div with bootstrap classes to every img in the galleries and display a message if there is not
let galleries = document.querySelectorAll(".gallery")
for (let i = 0; i < galleries.length; ++i){
    let gallery = galleries[i]
    let counter = 0
        for (let p = 0 ; p < gallery.childNodes.length; ++p){
            let child = gallery.childNodes[p]
            if (child.localName === "img"){
                let div = document.createElement("div")
                div.classList.add("col-lg-3","col-md-4","col-6");
                gallery.replaceChild(div, child)
                div.appendChild(child)
                ++counter
            }
        }
    if (counter === 0){
        let empty = document.createElement("p")
        gallery.appendChild(empty)
        empty.innerText = "Aucun de disponible actuellement"
    }
}