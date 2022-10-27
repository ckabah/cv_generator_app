const side_bar = document.getElementById('sideid')
const side_app_icon = document.getElementById('appid')
const close_side = document.getElementById('close_side')

if (side_app_icon){
    side_app_icon.addEventListener('click' , () => {
        side_bar.classList.add('active-side')
    })
}
if (close_side){
    close_side.addEventListener('click', ()=>{
        side_bar.classList.remove('active-side')
    })
}