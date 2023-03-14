var mapContainer = document.getElementById('map');
var enter=document.getElementById('enter');
var options = {
center: new kakao.maps.LatLng(33.450701, 126.570667),
level: 1, 
}; 
var map = new kakao.maps.Map(mapContainer, options);	

enter.addEventListener('click',(lat,lng)=>{
    lat=parseFloat(document.getElementById('lat').value);
    lng=parseFloat(document.getElementById('lng').value);
    var Newlocation=new kakao.maps.LatLng(lat,lng)
    map.setCenter(Newlocation);
})
