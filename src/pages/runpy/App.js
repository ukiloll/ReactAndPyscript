import './App.css';//***can import file in scr other must in public

function App() {

  return (
    <div className="App">
    <h1>Python Code Runner </h1>
    <p>พิมพ์โค้ด Python แล้วกด Run เพื่อดูผลลัพธ์! (รองรับ input() ได้)</p>
    <textarea id="python-code" placeholder="เช่น: name = input('คุณชื่ออะไร? ')\nprint('สวัสดี', name)"></textarea>
    <button py-click="start_code">Run</button>

    <div id="input-section">
      <p id="input-prompt"></p>
      <input type="text" id="input-area" placeholder="พิมพ์คำตอบที่นี่..." />
      <button py-click="submit_input">Submit</button>
    </div>

    <div id="output"></div>

    <script type="py" src='main.py'>//auto import in public
  
    </script>
  
    </div>
  );
}

export default App;
