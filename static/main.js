const side_bar = document.getElementById('sideid')
const side_app_icon = document.getElementById('appid')
const close_side = document.getElementById('close_side')
const cancel_icon = document.getElementById('cancel_icon');
const menubtn = document.getElementById('menubtn')
const nav_links = document.querySelector('.nav-links')

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
menubtn.addEventListener('click', ()=>{
    if (nav_links){
      nav_links.classList.add('active')
    }
  })
  cancel_icon.addEventListener('click', ()=>{
    if (nav_links){
      nav_links.classList.remove('active')
    }
  })