import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

const loadNotions = function(callback) {
  // GetCookie
  var cookieValue = null;
  var name = "csrftoken";
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const url = "http://localhost:8000/api/notions/";
  const responseType = "json";

  xhr.responseType = responseType;
  xhr.open(method, url);
  xhr.setRequestHeader("Content-Type", "application/json");
  //xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest");
  xhr.setRequestHeader("X-Requested-with", "XMLHttpRequest");
  xhr.setRequestHeader("X-CSRFToken", cookieValue);
  xhr.onload = function() {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = function(e) {
    console.log(e);
    callback({ message: "The request was an error" }, 400);
  };
  xhr.send();
};

function App() {
  const [notions, setNotions] = useState([]);

  useEffect(() => {
    const myCallback = (response, status) => {
      console.log(response, status);
      if (status === 200) {
        setNotions(response);
      } else {
        console.log("There was an error");
      }
    };
    loadNotions(myCallback);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          {notions.map((notion, index) => {
            return <li>{notion.content}</li>;
          })}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
