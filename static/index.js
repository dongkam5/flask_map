var mapContainer = document.getElementById('map');
var enter=document.getElementById('enter');
var traffic_btn=document.getElementById('traffic_btn');
var CLICKED_CLASS="clicked";
var options = {
center: new kakao.maps.LatLng(33.450701, 126.570667),
level: 1, 
}; 
var map = new kakao.maps.Map(mapContainer, options);	

var mapTypeControl=new kakao.maps.MapTypeControl();//지도/스카이뷰
map.addControl(mapTypeControl,kakao.maps.ControlPosition.TOPRIGHT);

var zoomControl = new kakao.maps.ZoomControl(); //줌 스크롤
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
enter.addEventListener('click',(lat,lng)=>{
    lat=parseFloat(document.getElementById('lat').value);
    lng=parseFloat(document.getElementById('lng').value);
    var Newlocation=new kakao.maps.LatLng(lat,lng)
    map.setCenter(Newlocation);
})

traffic_btn.addEventListener('click',()=>{ //교통정보 표시/끔
    const has_Class=traffic_btn.classList.contains(CLICKED_CLASS);
    if (has_Class){
        traffic_btn.classList.remove(CLICKED_CLASS);
        map.removeOverlayMapTypeId(kakao.maps.MapTypeId.TRAFFIC);   
    }
    else{
        traffic_btn.classList.add(CLICKED_CLASS);
        map.addOverlayMapTypeId(kakao.maps.MapTypeId.TRAFFIC);    
    }
})
kakao.maps.event.addListener(map,'dragend',()=>{
    var lating=map.getCenter();
    var message='변경된 지도 중심좌표는' + lating.getLat() + "이고, ";
    message+="경도는"+lating.getLng()+"입니다"
    var resultDiv=document.getElementById('result');
    resultDiv.innerHTML=message;
})


function getinfo(){
    var center=map.getCenter();
    var level= map.getLevel();
    var mapTypeId=map.getMapTypeId();
    var bounds=map.getBounds();
    var swLatLng=bounds.getSouthWest();
    var neLatLng=bounds.getNorthEast();
    var boundsStr=bounds.toString();
    var message = '지도 중심좌표는 위도 ' + center.getLat() + ', <br>';
message += '경도 ' + center.getLng() + ' 이고 <br>';
message += '지도 레벨은 ' + level + ' 입니다 <br> <br>';
message += '지도 타입은 ' + mapTypeId + ' 이고 <br> ';
message += '지도의 남서쪽 좌표는 ' + swLatLng.getLat() + ', ' + swLatLng.getLng() + ' 이고 <br>';
message += '북동쪽 좌표는 ' + neLatLng.getLat() + ', ' + neLatLng.getLng() + ' 입니다';
console.log(message)
}


console.log(getinfo());