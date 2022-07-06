# React
## 코드라이언: 프론트엔드 트랙 - React 정리
<br>

## **1. React기초**
<hr>

### **리액트란**
React는 웹 프레임워크로, 자바스크립트 라이브러리의 하나로서 사용자 인터페이스를 만들기 위해 사용된다.

- 참고 페이지: https://velog.io/@jini_eun/React-React.js%EB%9E%80-%EA%B0%84%EB%8B%A8-%EC%A0%95%EB%A6%AC

<br><br><br>


## **2. JSX 문법**
<hr>

### **JSX란**
- JSX는 자바스크립트의 확장 문법이다.
- XML과 매우 비슷하게 생겼으며, 브라우저에서 실행하기 전에 코드가 번들링되는 과정에서 바벨을 사용하여 일반 자바스크립트 형태의 코드로 변환된다.
- JSX는 자바스크립트의 공식적인 문법이라고 할 수는 없다. <br> 즉, 자바스크립트에서 HTML을 작성하듯이 비슷하게 작성할 수 있도록 해 주는 것이 JSX의 가장 큰 장점이자, 이를 사용하는 이유가 된다.<br><br>
- 참고 페이지: https://developerntraveler.tistory.com/54
- 참고페이지: https://chanhuiseok.github.io/posts/react-3/

<br><br><br>


## **3. Styled-Components**
<hr>

### **3-1. Styled-Components**
- 패키지 설치: `npm i styled-components`

- 참고 페이지: https://www.daleseo.com/react-styled-components/

<br><br>

### **3-2. 전역 스타일 적용하기(GlobalStyle)**
- 패키지 설치: `npm i styled-components`<br>
styled-comonents를 설치하여 createGlobalStyle를 적용한다.
<br>

- 패키지 설치: `npm i styled-reset`<br>
styled-reset을 사용하여 기존의 css를 초기화한다.<br>
styled-reset은 styled-components와 연결되어, 여러 브라우저마다 기본적으로 설치되어 있는 스타일을 지워주는 Node.js 패키지이다.

- 참고 페이지: https://defineall.tistory.com/919
- 참고 페이지: https://velog.io/@shyunju7/react13

<br><br><br>


## **4. state 사용하기 & 컴포넌트 사용하기 & props**
<hr>

### **4-1. 컴포넌트란**
- 리액트로 만들어진 앱을 이루는 최소한의 단위

- 기존의 웹 프레임워크는 MVC방식으로 분리하여 관리하여 각 요소의 의존성이 높아 재활용이 어렵다는 단점이 있었다. 반면 컴포넌트는 MVC의 뷰를 독립적으로 구성하여 재사용을 할 수 있고 이를 통해 새로운 컴포넌트를 쉽게 만들 수 있다.

- 컴포넌트는 데이터(props)를 입력받아 View(state) 상태에 따라 DOM Node를 출력하는 함수이다.

- 컴포넌트 이름은 항상 대문자로 시작한다. (리액트는 소문자로 시작하는 컴포넌트를 DOM 태그로 취급하기 때문이다.)

- UI를 재사용 가능한 개별적인 여러 조각으로 나누고, 각 조각을 개별적으로 나누어 코딩한다.

<br><br>

### **4-2. 함수형 컴포넌트 VS 클래스형 컴포넌트**

 **[함수형 컴포넌트]**

- JSX를 return문을 사용해서 반환한다.

- state를 사용할 수 없다.

- 생명 주기 함수를 작성할 수 없다.

- 리액트 버전 16.8부터 훅(Hook)이 등장하면서 함수형 컴포넌트에서도 state와 생명 주기 함수 코드를 작성 할 수 있게 되었다.

<br>

```
import React from 'react';

function Hello({ color, name, isSpecial }) {
  return (
    <div style={{ color }}>
      {isSpecial && <b>*</b>}
      안녕하세요 {name}
    </div>
  );
}

export default Hello;
```

<br><br>
**[클래스형 컴포넌트]**

- class 키워드로 시작

- Component로 상속 받음

- render() 함수를 사용해서 JSX를 반환

- props를 조회할 때 this 키워드 사용

<br>

```
import React, { Component } from 'react';

class Hello extends Component {
  render() {
    const { color, name, isSpecial } = this.props;
    return (
      <div style={{ color }}>
        {isSpecial && <b>*</b>}
        안녕하세요 {name}
      </div>
    );
  }
}

export default Hello;
```

<br><br>

### **4-3. 컴포넌트의 반복**
- 반복되는 컴포넌트를 렌더링하기 위하여 자바스크립트 배열의 내장 함수인 map()을 사용한다.

- map 함수는 파라미터로 전달된 함수를 사용하여 배열 각 요소를 원하는 규칙에 따라 변환한 다음 새로운 배열을 생성한다. 즉, callbackFunction을 실행한 결과를 이용해 새로운 배열을 만들어 내는 함수이다.

- `arr.map(callbackFunction(currentValue, index, array), thisArg);`

- callback function을 작성할 때 맨 앞의 인자는 현재 배열(arr) 내의 값들을 의미하며, 두 번째 인자는 현재 배열 내 값의 인덱스를 의미하고, 마지막 인자는 현재 배열을 의미한다. <br>
thisArg는 callbackFunction 안에서 사용할 this 레퍼런스를 의미한다.

<br><br>

### **4-4. state**
- state는 props처럼 App 컴포넌트의 렌더링 결과물에 영향을 주는 데이터를 갖고 있는 객체지만, props는 (함수 매개변수처럼) 컴포넌트에 전달되는 반면 state는 (함수 내에 선언된 변수처럼) 컴포넌트 안에서 관리된다는 차이가 있다.

<br>

- props를 사용했는데도 state를 사용하는 이유는 사용하는 쪽과 구현하는 쪽을 철저하게 분리시켜서 양쪽의 편의성을 각자 도모하는 것에 있다.

<br>

**props vs state**
- props
    - 부모 컴포넌트로부터 자녀 컴포넌트에 데이터 등을 전달
    - 읽기 전용으로 자녀 컴포넌트 입장에서 변동 없음

<br>

- state
    - 해당 컴포넌트 내부에서 데이터 전달
    - 변경 가능함

<br>

- 참고 페이지: https://velog.io/@hidaehyunlee/React-State-%EB%9E%80

<br><br><br>


## **5. 리액트 라우터**
<hr>

- ​리액트는 SPA(Single Page Application) 방식으로써, 여러개의 페이지를 사용하며, 새로운 페이지를 로드하는 기존의 MPA 방식과 달리 새로운 페이지를 로드하지 않고 하나의 페이지 안에서 필요한 데이터만 가져오는 형태를 가진다. 

- React Router는 페이지를 새로 불러오지 않는 상황에서 각각의 선택에 따라서 선택된 데이터를 하나의 페이지에서 렌더링 해주는 라이브러리이다.

- 참고 페이지: https://velog.io/@goodenough/React-%EB%A6%AC%EC%95%A1%ED%8A%B8-%EB%9D%BC%EC%9A%B0%ED%84%B0react-router

- 참고 페이지: https://m.blog.naver.com/sejun3278/221797203201

<br><br><br>


## **6. Virtual DOM, useRef, useCallback, React.memo**
<hr>

### **6-1. Virtual DOM**
- 참고 페이지: https://velog.io/@gwak2837/React-Virtual-DOM-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0

<br><br>

### **6-2. useRef**
- useRef는 리렌더링 하지 않는다. 컴포넌트의 속성만 조회&수정한다.

- 참고 페이지: https://www.daleseo.com/react-hooks-use-ref/

- 참고 페이지: https://yoonjong-park.tistory.com/entry/React-useRef-%EB%8A%94-%EC%96%B8%EC%A0%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EA%B0%80

<br><br>

### **6-3. UseCallback**
- useCallback()은 함수를 메모이제이션(memoization)하기 위해서 사용되는 hook 함수이다. <br>첫번째 인자로 넘어온 함수를, 두번째 인자로 넘어온 배열 내의 값이 변경될 때까지 저장해놓고 재사용할 수 있게 한다.

- 참고 페이지: https://www.daleseo.com/react-hooks-use-callback/

<br><br>

### **6-4. React.memo**
- 리액트에서 부모 컴포넌트가 렌더링 될 때 해당 컴포넌트에 속하는 모든 자식 컴포넌트 또한 렌더링 된다. <br>하지만 부모 컴포넌트에서 자식 컴포넌트로 내려주는 props가 바뀌지 않았다면, 해당 자식 컴포넌트를 리 렌더링 하지 않아도 될 것이다. <br>컴포넌트에서 리 렌더링이 필요한 상황에서만 해주도록 설정을 할 수 있는데 이때 사용하는 함수가 바로 React.memo 함수이다.

- `const MyComponent = React.memo(function MyComponent(props) {
  /* props를 사용하여 렌더링 */
});`

- 참고 페이지: https://cocoon1787.tistory.com/799#:~:text=%5BReact%5D%20%EB%A6%AC%EC%95%A1%ED%8A%B8%20Hooks%20%3A%20useMemo()%20%ED%95%A8%EC%88%98%20%EC%82%AC%EC%9A%A9%EB%B2%95%20memozation,%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%20%EA%B8%B0%EB%B2%95%EC%9D%84%20%EC%9D%98%EB%AF%B8%ED%95%A9%EB%8B%88%EB%8B%A4.

- 참고 페이지: https://velog.io/@ansrjsdn/React.memo-%ED%98%84%EB%AA%85%ED%95%98%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

<br><br><br>


## **6. REST api 연동 axios**
<hr>

### **6-1. Axios란**
- Axios는 브라우저, Node.js를 위한 Promise API를 활용하는 HTTP 비동기 통신 라이브러리이다.

<br><br>

### **6-2. Axios 특징**
- 운영 환경에 따라 브라우저의 XMLHttpRequest 객체 또는 Node.js의 HTTP API 사용
- Promise(ES6) API 사용
- 요청과 응답 데이터의 변형
- HTTP 요청 취소 및 요청과 응답을 JSON 형태로 자동 변경

### **6-3. 메서드**
- GET: 데이터 조회
- POST: 데이터 등록
- PUT: 데이터 수정
- DELETE: 데이터 제거

<br>

- 참고 페이지: https://velog.io/@shin6403/React-axios%EB%9E%80-feat.-Fetch-API

- 참고 페이지: https://velog.io/@johnque/React-API-%EC%97%B0%EB%8F%99-v9k692txn5

- 참고 페이지: https://react.vlpt.us/integrate-api/01-basic.html