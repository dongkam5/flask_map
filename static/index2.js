var mapContainer = document.getElementById('map');
var enter=document.getElementById('enter');
var traffic_btn=document.getElementById('traffic_btn');
var CLICKED_CLASS="clicked";
var options = {
center: new kakao.maps.LatLng(35.23924, 129.0146854),
level: 1, 
}; 
var map = new kakao.maps.Map(mapContainer, options);	
var imageSrc = "data:image/jpeg;base64,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", // 마커이미지의 주소입니다    
    imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
    imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
      
// 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
    markerPosition = new kakao.maps.LatLng(37.54699, 127.09598); // 마커가 표시될 위치입니다

// 마커를 생성합니다
var marker = new kakao.maps.Marker({
    position: markerPosition, 
    image: markerImage // 마커이미지 설정 
});

marker.setMap(map);

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
kakao.maps.event.addListener(map,'click',(mouseEvent)=>{
    var lating=mouseEvent.latLng;
    marker.setPosition(lating);
    var message='클릭한 위치의 위도는' + lating.getLat() + "이고, ";
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

marker.setDraggable(true);

console.log(getinfo());