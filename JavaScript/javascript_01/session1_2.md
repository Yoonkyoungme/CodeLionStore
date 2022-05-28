# JavaScript
## 코드라이언: 프론트엔드 트랙 - JavaScript chapter1 ~ 2 정리
<br>

## **1. DOM**
---
- 브라우저가 HTML 웹 페이지를 인식하는 방식을 계층화시켜 트리구조로 만든 객체(Object) 모델이다.
- DOM은 tree 형식의 자료 구조로 되어 있다.
- DOM은 HTML인 웹페이지와 스크립팅 언어(JavaScript)를 서로 잇는 역할을 한다.
- 참고 페이지: https://velog.io/@solmii/TIL-DOM%EC%9D%B4%EB%9E%80
<br><br><br>


### **DOM 접근 메서드**
---
JavaScript는 document라는 전역객체를 통해 HTML에 접근할 수 있다. <br>
⇒ JavaScript의 document 객체는 DOM 구조를 접근하는 관문이며, document 객체는 HTML 문서를 나타낸다.

- `document.getElementById("id명")`: 해당 id명을 가진 요소 하나를 반환

- `document.quertSelector("선택자")`: 해당 선택자를 만족하는 요소 하나를 반환

- `document.getElementsByClassName("class명")[i]`: 해당 class명을 가진 요소들을 배열에 담아 인덱스에 맞는 요소를 반환

- `document.getElementsByTagName("tag명")[i]`: 해당 tag명을 가진 요소들을 배열에 담아 인덱스에 맞는 요소를 반환

- `document.quertSelectorAll("선택자")[i]`: 해당 선택자를 만족하는 모든 요소들을 배열에 담아 인덱스에 맞는 요소를 반환

<br><br><br>


### **DOM 조작**
---
- `innerHTML`: Element 속성(property) innerHTML은 요소(element) 내에 포함 된 HTML 또는 XML 마크업을 가져오거나 설정한다. <br>
태그 자체를 가져오거나 바꾸는 기능 (바뀌는 범위 : (<태그>텍스트</태그>) ⇒  전체 다 바뀜)

<br>

- `classList`: 요소의 클래스 이름을 반환한다.<br>
이 속성은 추가, 제거 및 CSS 클래스를 전환 할 요소에 사용된다.<br><br>
        - `Element.classList.add` : 명시된 클래스를 추가하는 메서드<br>
        - `Element.classList.remove` : 명시된 클래스를 제거하는 메서드<br>
        - `Element.classList.toggle` : 클래스가 존재한다면 클래스를 제거하고, 클래스가 존재하지 않는다면 클래스를 추가하는 메서드<br>  


 

<br><br><br>


## **2. Event**
---
- 어떤 사건을 의미한다. ex) 특정 버튼을 클릭했을때, 돔이 다 로드 되었을 때
- 브라우저는 이벤트를 감지할 수 있으며 이벤트 발생 시 알려 줄 수 있으며 이를 통해 사용자와 웹페이지가 상호 작용이 가능하다.

- 이벤트 핸들러를 통하여 이벤트가 발생시 원하는 함수에 연결하여 실행 시킬 수 있다.

- 참고 페이지: https://goddaehee.tistory.com/269
- 참고 페이지: https://inpa.tistory.com/entry/JS-%F0%9F%93%9A-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%F0%9F%92%AF-%EC%B4%9D-%EC%A0%95%EB%A6%AC


