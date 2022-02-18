
function fetch_userdata_by_username(member_search_username){
    username = member_search_username.value
    fetch(`/api/members?username=${username}`)
    .then(response => response.json())
    .then(data => show_user_name_data.textContent = check_username_data(data));
        // 
};



function update_userdata_by_username(member_update_username){
    update_username = member_update_username.value
    console.log(update_username)
    let check_update_username = update_username.replace(/(^\s*)|(\s*$)/g, '');//去除空格;
    if (check_update_username == '' || check_update_username == undefined || check_update_username == null){
        showupdate_user_name_data.textContent = "請勿空白";
    }else{
    fetch(`/api/member`,{
        method: "POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({"username": check_update_username})
    })
    .then(response => response.json())
    .then(data => {
        response_condition = update_username_status(data);
        member_update_username.value = ""
        showupdate_user_name_data.textContent = response_condition;}
    );
    }  
};

function check_username_data(response_data){
    if (response_data["data"]){
        return response_data["data"]["name"]
    }else{
        console.log(response_data["data"])
        return "user no found"
    }
}



function update_username_status(response_data){
    getReskey = Object.keys(response_data);
    if (getReskey == "ok"){
        return "更新成功"
    }
    else{
        return "尚未登入"
    }

}






const member_search_form = document.getElementById("search_form");
const member_search_username = document.getElementById("search_bar");
const show_user_name_data = document.getElementById("show_user_name");
member_search_form.addEventListener('submit', function(event){fetch_userdata_by_username(member_search_username);event.preventDefault();});


const member_update_form = document.getElementById("update_form");
const member_update_username = document.getElementById("update_bar");
const showupdate_user_name_data = document.getElementById("update_user_name");
member_update_form.addEventListener('submit', function(event){update_userdata_by_username(member_update_username);event.preventDefault();});