import React from "react";

import styles from "./SearchBar.module.css";

const SearchBar = () => {
  return (
    <div className={styles.search_bar}>
      <p>Wyszukaj:</p>
      <div>
        <input type="text" placeholder="Tu wpisz frazę do wyszukania" />
        <button>
          <span className={`material-symbols-outlined`}> search </span>
        </button>
      </div>
    </div>
  );
};

export default SearchBar;
