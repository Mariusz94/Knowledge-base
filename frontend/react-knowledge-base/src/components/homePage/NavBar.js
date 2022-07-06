import React from "react";
import { NavLink } from "react-router-dom";

import styles from "./NavBar.module.css";

const NavBar = (props) => {
  return (
    <div className={` ${styles.nav_bar__root}`}>
      <nav>
        <ul>
          <li>
            <NavLink to="/">
              <div>Home</div>
            </NavLink>
          </li>
          <li>
            <NavLink to="/">
              <div>Add article</div>
            </NavLink>
          </li>
          <li>
            <NavLink to="/">
              <div>Categories</div>
            </NavLink>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default NavBar;
