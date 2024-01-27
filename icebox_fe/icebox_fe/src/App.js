import logo from './logo.svg';
import './App.css';
import ItemList from './ItemList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <ItemList/>
        <button>음식 넣기</button>
      </header>
    </div>
  );
}

export default App;
