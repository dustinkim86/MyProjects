// 1. 무작위 숫자 배열 생성
var arr = Array.apply(null, new Array(value*value)).map(() => Math.floor(Math.random()* 99)+1);


// 2. 3초 타이머 함수 설정
var SetTime = 3;
function msg_time() { // 1초씩 카운트
    m = (SetTime % 60); // 남은 시간 계산
    var msg = m;
    document.all.ViewTimer.innerHTML = msg; // div 영역에 보여줌
    SetTime--;
    if (SetTime < 0) {
        clearInterval(tid); // 타이머 해제
        if(m == 0){
            document.getElementById('ViewTimer').style.visibility = 'hidden';
            start(); // 스톱워치 시작 함수 실행
            function shuffle(a) { // 숫자 위치 무작위 변경
                var j, x;
                for (var i = 1; i<=a.length; i++) {
                    j = Math.floor(Math.random() * i);
                    x = a[i - 1];
                    a[i - 1] = a[j];
                    a[j] = x;
                }
            }
            shuffle(arr); // 무작위 숫자 배열 위치변경 함수 실행

            // HTML 반영
            var number = document.getElementsByClassName('number');
            for(var i = 0; i<number.length; i++){
                number[i].innerHTML = arr[i];
            }
        }
    }
}


// 3. 웹페이지 접속과 동시에 3초 타이머 시작
window.onload = function(){
    tid=setInterval('msg_time()',1000) // 3초 Timer
}


// 4. 스톱워치
var stopwatch,
i = 0,
divide = 100;
function start(){ // 스톱워치 시작 함수
    stopwatch = self.setInterval('increment()', (1000 / divide));
}
function increment(){ // 시간 증가 함수(시작 함수에 사용)
    i++;
    document.getElementById('time_out').innerHTML = (i / divide);
}
function stop(){ // 스톱워치 종료 함수
    clearInterval(stopwatch);
    usersTime = document.getElementById('time_out').textContent; 
    return usersTime; // 최종 소요시간 반환
}


// 5. 게임 시작 및 종료 후 score 페이지 이동
var userTime;
var cnt = 0;
function click_event(numbers_){ // 버튼 onclick 이벤트로부터 받은 value로 함수 시작
    var number = Number(numbers_.textContent);
    var arr_sort = arr.sort(function(a,b){return a-b;}); // 무작위 숫자 배열 오름차순 정렬
    // onclick한 버튼 value와 정렬한 배열 value 비교
    if(number == arr_sort[cnt]){
        cnt++; // 맞춘 경우 카운트 + 1
        document.getElementById('trueOrFalse').innerHTML = '정답! 계속 진행하세요';
        numbers_.disabled = true; // 맞춘 버튼 비활성화
        numbers_.style.backgroundColor = 'white'; // 맞춘 버튼 배경색 변경
        numbers_.style.color = 'white'; // 맞춘 버튼 글씨 색상 변경
    }else{
        document.getElementById('trueOrFalse').innerHTML = '틀렸어요! 다시 찾아봐요';
    }
    if(cnt >= value*value){ // 카운트가 배열의 수보다 크거나 같아질 경우
        userTime = stop(); // 스톱워치 종료 함수 실행 및 소요시간 반환
        window.open("score.html?userTime:"+userTime); // score.html 실행 및 소요시간 전달
    }
}






