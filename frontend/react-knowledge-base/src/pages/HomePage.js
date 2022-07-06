import React from "react";

import SearchBar from "../components/ui/SearchBar";
import ContentCard from "../components/ui/ContentCard";

import styles from "./HomePage.module.css";

const HomePage = () => {
  return (
    <div className={`d-flex flex-column align-items-center gap-2 mt-2`}>
      <SearchBar />
      <ContentCard>
        <div className={styles.content_title}>
          <h2>What is Lorem Ipsum?</h2>
        </div>
        <div className={styles.content_body}>
          <p>
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book. It has survived not
            only five centuries, but also the leap into electronic typesetting,
            remaining essentially unchanged. It was popularised in the 1960s
            with the release of Letraset sheets containing Lorem Ipsum passages,
            and more recently with desktop publishing software like Aldus
            PageMaker including versions of Lorem Ipsum.
          </p>
        </div>
      </ContentCard>
    </div>
  );
};

export default HomePage;
