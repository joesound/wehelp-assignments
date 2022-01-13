
const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

// function replace_photo_DOM_element(index, information){
//     let img_content = document.querySelector(`.imag${index}`);
//     let text_content = document.getElementById(`text_cotainer${index}`);
//     let imag_src = information["file"].toLowerCase();
//     imag_src_split_by_jpg = imag_src.split("jpg");
//     let imag_text = information["stitle"];
//     img_content.src = imag_src_split_by_jpg[0] + "jpg";
//     text_content.textContent = imag_text
//     console.log(imag_text)
// }

function get_imag_stitle(information){
    var imag_src = information["file"].toLowerCase();
    var stitle_text = information["stitle"];
    imag_src_split_by_jpg = imag_src.split("jpg");
    image_url = imag_src_split_by_jpg[0] + "jpg";

    return [image_url, stitle_text];
}

function replace_photo_by_creatElement_appedChild(information){
    var all_imag_container = document.querySelectorAll(".pic_container");
    var all_text_container = document.querySelectorAll(".text_cotainer");
    var choosed_number = [];
    for (const i in all_imag_container){
        var random_number =  Math.floor(Math.random() * information.length)
        var data_imagurl_stitle_text = get_imag_stitle(information[random_number]);
        while(choosed_number.includes(random_number)){
            random_number =  Math.floor(Math.random() * information.length)
        }
        console.log(choosed_number.includes(random_number))
        var newNode = document.createElement('img');
        newNode.src = data_imagurl_stitle_text[0];
        all_text_container[i].textContent = data_imagurl_stitle_text[1];
        all_imag_container[i].appendChild(newNode);
        choosed_number.push(random_number);
    }

}
    

fetch(url)
.then(response => response.json())
.then(datas => {
   const Taipei_data =  datas.result.results;
   replace_photo_by_creatElement_appedChild(Taipei_data)
})

