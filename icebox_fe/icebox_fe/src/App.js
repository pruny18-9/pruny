import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <button>냉장고 보기</button>
        <button>음식 넣기</button>
        <button>음식 버리기</button>
      </header>
    </div>
  );
}

export default App;
