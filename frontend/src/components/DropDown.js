import React from "react";
import { slide as Menu } from "react-burger-menu";

export default props => {
  return (
    <Menu>
      <a className="menu-item" href="App.js">
        Home
      </a>

      <a className="menu-item" href="/templates/profile.html">
        Profile
      </a>

      <a className="menu-item" href="./RecommendedBooks.js">
        Recommended Books
      </a>

      <a className="menu-item" href="/RandomBook">
        Random Book
      </a>
    </Menu>
  );
};