import React, { useState, useEffect } from "react";
import { Row, Col } from "react-bootstrap";

import styles from "./Footer.module.css";

const Footer = (props) => {
  const [year, setYear] = useState(2000);

  useEffect(() => {
    const today = new Date();
    setYear(today.getFullYear());
    console.log(today.getFullYear());
  }, []);

  return (
    <Row>
      <Col className={`p-0`}>
        <div className={styles.footer__root}>
          <p>{year} © Made with passion by Mariusz Łyszczarz</p>
        </div>
      </Col>
    </Row>
  );
};

export default Footer;
