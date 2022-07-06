import React from "react";
import { Row, Col } from "react-bootstrap";

import NavBar from "../components/homePage/NavBar";

const Body = (props) => {
  return (
    <Row>
      <Col xs="12" sm="4" md="3" lg="2">
        <NavBar />
      </Col>
      <Col xs="12" sm="8" md="9" lg="10" className={`p-0`}>
        {props.children}
      </Col>
    </Row>
  );
};

export default Body;
