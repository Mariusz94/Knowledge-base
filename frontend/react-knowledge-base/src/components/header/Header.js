import React from "react";
import { Row, Col } from "react-bootstrap";

import styles from "./Header.module.css";

const Header = () => {
  return (
    <Row>
      <Col className={`p-0`}>
        <div className={`d-flex justify-content-center ${styles.header__root}`}>
          <div className={`d-flex align-items-center ${styles.logo}`}>
            <p>Knowledge base</p>
          </div>
        </div>
      </Col>
    </Row>
  );
};

export default Header;
