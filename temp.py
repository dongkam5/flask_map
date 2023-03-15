"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>동백지도</title>
    <style>
    .wrap {position: absolute;left: 0;bottom: 40px;width: 288px;height: 132px;margin-left: -144px;text-align: left;overflow: hidden;font-size: 12px;font-family: 'Malgun Gothic', dotum, '돋움', sans-serif;line-height: 1.5;}
    .wrap * {padding: 0;margin: 0;}
    .wrap .info {width: 286px;height: 120px;border-radius: 5px;border-bottom: 2px solid #ccc;border-right: 1px solid #ccc;overflow: hidden;background: #fff;}
    .wrap .info:nth-child(1) {border: 0;box-shadow: 0px 1px 2px #888;}
    .info .title {padding: 5px 0 0 10px;height: 30px;background: #eee;border-bottom: 1px solid #ddd;font-size: 18px;font-weight: bold;}
    .info .close {position: absolute;top: 10px;right: 10px;color: #888;width: 17px;height: 17px;background: url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/overlay_close.png');}
    .info .close:hover {cursor: pointer;}
    .info .body {position: relative;overflow: hidden;}
    .info .desc {position: relative;margin: 13px 0 0 90px;height: 75px;}
    .desc .ellipsis {overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}
    .desc .jibun {font-size: 11px;color: #888;margin-top: -2px;}
    .info .img {position: absolute;top: 6px;left: 5px;width: 73px;height: 71px;border: 1px solid #ddd;color: #888;overflow: hidden;}
    .info:after {content: '';position: absolute;margin-left: -12px;left: 50%;bottom: 0;width: 22px;height: 12px;background: url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/vertex_white.png')}
    .info .link {color: #5085BB;}
</style>
</head>
<body>
<div id="map" style="width:100%;height:350px;"></div>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=9bb347d4f022c0a35791fc41f6552d25"></script>
<script>
var mapContainer = document.getElementById('map'), // 지도의 중심좌표
    mapOption = { 
        center: new kakao.maps.LatLng(35.15764967005048, 129.05912240855056), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    }; 

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

//여기서 부터 반복 시작
// 지도에 마커를 표시합니다 
var marker = new kakao.maps.Marker({
    map: map, 
    position: new kakao.maps.LatLng(35.15764967005048, 129.05912240855056)
});

// 커스텀 오버레이에 표시할 컨텐츠 입니다
// 커스텀 오버레이는 아래와 같이 사용자가 자유롭게 컨텐츠를 구성하고 이벤트를 제어할 수 있기 때문에
// 별도의 이벤트 메소드를 제공하지 않습니다 
var content = '<div class="wrap">
<div class="info">
<div class="title">
<div class="close" onclick="closeOverlay()" title="닫기"></div>  
</div> 
                    <div class="body">  
                        <div class="img"> 
                            <img src="data:image/png;base64,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" width="73" height="70"> 
                        </div>  
                        <div class="desc">  
                            <div class="ellipsis">제주특별자치도 제주시 첨단로 242</div>  
                            <div class="jibun ellipsis">(우) 63309 (지번) 영평동 2181</div>  
                            <div><a href="https://www.kakaocorp.com/main" target="_blank" class="link">홈페이지</a></div>  
                        </div>  
                    </div>  
                </div>     
            '</div>';

// 마커 위에 커스텀오버레이를 표시합니다
// 마커를 중심으로 커스텀 오버레이를 표시하기위해 CSS를 이용해 위치를 설정했습니다
var overlay = new kakao.maps.CustomOverlay({
content: content,
map: map,
position: marker.getPosition()
});

// 마커를 클릭했을 때 커스텀 오버레이를 표시합니다
kakao.maps.event.addListener(marker, 'click', function() {
overlay.setMap(map);
});

// 커스텀 오버레이를 닫기 위해 호출되는 함수입니다 
function closeOverlay() {
overlay.setMap(null);     
}
</script>
</body>
</html>
""".format()

"hi{}".format('a')