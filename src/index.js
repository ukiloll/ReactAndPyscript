import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './pages/runpy/App';
import Home from './pages/home/App';
import Game from './pages/game/App'
import reportWebVitals from './reportWebVitals';
import {RouterProvider,createBrowserRouter} from "react-router-dom"

const route = createBrowserRouter([
  {
    path:"/",
    element:<Home/>
  },
  {
    path:"/runpy",
    element:<App/>
  },
  {
    path:"/pygame",
    element:<Game/>
  }

])


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={route} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
