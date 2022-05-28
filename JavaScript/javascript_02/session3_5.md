# JavaScript
## 코드라이언: 프론트엔드 트랙 - JavaScript chapter3 ~ 5 정리
<br>

## **1. 함수**
<hr>

### **화살표 함수**
```python
function fun() { // 일반함수
  ...
}

const arrFun = () => { // 화살표 함수
  ...
};
```

- 참고 페이지: https://hhyemi.github.io/2021/06/09/arrow.html
- 참고 페이지: https://webclub.tistory.com/649

<br><br><br>


## **2. 동기 & 비동기**
<hr>

- 참고 페이지: https://velog.io/@open_h/javascriptasync

<br>

### **동기**
- 요청 후 응답을 받아야 다음 동작을 실행하는 방식

### **비동기**
- 요청을 보낸 후 응답과 관계없이 다음 동작을 실행하는 방식
<br>
        - call back <br>
        - Promise <br>

<br><br><br>


## **3. 스프레드**
<hr>


- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 문자를 0개 이상의 인수 (함수로 호출할 경우) 또는 요소 (배열 리터럴의 경우)로 확장하여, 0개 이상의 키-값의 쌍으로 객체로 확장시킬 수 있다.
- 배열, 문자열, 객체 등 반복 가능한 객체 (Iterable Object)를 개별 요소로 분리할 수 있다.
- 객체는 객체에서만, 배열은 배열에서만 사용 가능하다.
- Spread 연산자는 ... 을 통해 사용할 수 있다. 
- 참고 페이지: https://velog.io/@chlwlsdn0828/Js-Spread-%EC%97%B0%EC%82%B0%EC%9E%90-Rest-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0

<br><br><br>


## **4. 레스트**
<hr>

- Rest 파라미터 구문은 정해지지 않은 수(an indefinite number, 부정수) 인수를 배열로 나타낼 수 있게 한다.
- 스프레드의 반대 기능이다.
- 뒤에 남는 것들을 받아준다.
- Rest 파리미터도 마찬가지로 ...를 통해 사용할 수 있다.
