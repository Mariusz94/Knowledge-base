import { Container, Row, Col } from "react-bootstrap";
import "./App.css";

import { Navigate, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import Header from "./components/header/Header";
import Footer from "./components/footer/Footer";
import Body from "./components/Body";

function App() {
  return (
    <Container fluid>
      <Header />
      <Body>
        <Routes>
          <Route path="/" element={<Navigate to="/home" />} exact />
          <Route path="/home" element={<HomePage />} exact />
        </Routes>
      </Body>
      <Footer />
    </Container>
  );
}

export default App;
