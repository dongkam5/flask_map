## 구현목표 / 진행현황

### 지도 검색 기능 X
  - 데이터 베이스 기반으로 검색 기능 구현 X
### 동백전 가맹가게 지도 표시 O
  - 카카오 API 기능을 추가하여 가맹가게를 지도에 표시하였다.
### 지도 표시된 마커위에 마우스를 올리면 정보 표시 O
  - 여러가지 방법을 찾아보았으나, 여러 마커들에 대해 각 마커를 클릭하여 정보가 표시되게하는 것은 카카오맵 API에서 제공하는 기능으로 구현하는게 어려웠다.
  - 차선책으로 마커위에 마우스를 올리면 정보가 표시되는 방법으로 변경하였다.
### GPS 기능을 사용하여 현재 위치 파악 O
  - navigator 라이브러리를 사용하여 위치를 파악하게 하였다.