import React from 'react';
import { Container, Row, Col, Navbar, Nav, Button, Carousel } from 'react-bootstrap';

function HomePage() {

    const prevIcon = (
        <span className="carousel-control-prev-icon" aria-hidden="true">
            <i className="fa fa-angle-left"></i>
        </span>
    );

    const nextIcon = (
        <span className="carousel-control-next-icon" aria-hidden="true">
            <i className="fa fa-angle-right"></i>
        </span>
    );

    return (
        // Aquí irá el contenido JSX que hemos extraído
        <header>
            <div className="layout_padding banner_section_start">
                <div className="header">
                    <Container>
                        <Row>
                            <Col xl={3} lg={3} md={3} sm={3} className="logo_section">
                            <div className="full">
                                <div className="center-desk">
                                <div className="logo">
                                    <a href="#home">
                                    <img className="avatar" src="/images/logo_bañico.png" style={{ maxWidth: '100%' }} />
                                    </a>
                                </div>
                                </div>
                            </div>
                            </Col>
                            <Col xl={9} lg={9} md={9} sm={9}>
                                <Navbar bg="light" expand="lg">
                                        <Navbar.Toggle aria-controls="basic-navbar-nav" />
                                        <Navbar.Collapse id="basic-navbar-nav">
                                            <Nav className="ml-auto">
                                                <Nav.Link href="#home">Inicio</Nav.Link>
                                                <Nav.Link href="#about">Acerca de nosotros</Nav.Link>
                                                <Nav.Link href="#products">Productos y Servicios</Nav.Link>
                                                <Nav.Link href="#gallery">Galeria</Nav.Link>
                                                <Nav.Link href="#contact">Contactanos</Nav.Link>
                                            </Nav>
                                        </Navbar.Collapse>
                                </Navbar>
                            </Col>
                        </Row>
                    </Container>
                </div>
                <div className="layout_padding banner_section">
                     <Container>
                        <Carousel id="main_slider">
                            controls={true}
                            prevIcon={prevIcon}
                            nextIcon={nextIcon}
                            prevLabel="Previous"
                            nextLabel="Next"
                            <Carousel.Item>
                                <Row>
                                <Col md={6} className="taital">
                                    <h1 className="taital">Calidad<strong className="banner_taital">BAÑICO'S Productos con panes dulces</strong></h1>
                                    <p className="lorem_text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim</p>
                                </Col>
                                <Col md={6}>
                                    <div className="banner-image"><img src="/images/banner-image.png" style={{ maxWidth: '100%' }} /></div>
                                </Col>
                                </Row>
                                <div className="banner_bt">
                                <Button className="bt_main"><a href="#">Leer mas</a></Button>
                                </div>
                            </Carousel.Item>
                            <Carousel.Item>
                                <Row>
                                        <Col md={6} className="taital">
                                        <h1>Quality<strong className="banner_taital">BAÑICO'S Productos con panes dulces</strong></h1>
                                        <p className="lorem_text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim</p>
                                        </Col>
                                        <Col md={6}>
                                        <div className="banner-image"><img src="/images/banner-image.png" style={{ maxWidth: '100%' }} /></div>
                                        </Col>
                                </Row>
                                <div className="banner_bt">
                                        <Button className="bt_main"><a href="#">leer mas</a></Button>
                                </div>
                            </Carousel.Item>
                        </Carousel>
                        <Carousel
                            prevIcon={<span className="carousel-control-prev-icon" aria-hidden="true"><i className="fa fa-angle-left"></i></span>}
                            prevLabel="Previous"
                            nextIcon={<span className="carousel-control-next-icon" aria-hidden="true"><i className="fa fa-angle-right"></i></span>}
                            nextLabel="Next"
                        >
                            {/* Items del Carousel */}
                        </Carousel>

                    </Container>
                </div>
            </div>
        </header>
    );
}

export default HomePage;
