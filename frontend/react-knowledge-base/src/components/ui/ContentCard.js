import React from "react";

import styles from "./ContentCard.module.css";

const ContentCard = (props) => {
  return <div className={styles.content}>{props.children}</div>;
};

export default ContentCard;
