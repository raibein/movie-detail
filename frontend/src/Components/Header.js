import { Component  } from "react"

import "../css/bootstrap.css";
import "../css/responsive.css";
import "../css/style.css";
import "../css/style.css.map";

class Header extends Component{
    render() {
        return (
                <div class="hero_area">
                    <header class="header_section">
                    <div class="container-fluid">
                        <nav class="navbar navbar-expand-lg custom_nav-container ">
                        <a class="navbar-brand" href="/">
                            <span>Movie Detail  </span>
                        </a>
                        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>

                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                            <div class="d-flex ml-auto flex-column flex-lg-row align-items-center">
                            <ul class="navbar-nav  ">
                                <li class="nav-item active"><a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a></li>
                                <li class="nav-item "><a class="nav-link" href="#about"> About </a></li>
                                <li class="nav-item"><a class="nav-link" href="#how"> How </a></li>
                                <li class="nav-item"><a class="nav-link" href="#movie"> Movie </a></li>
                                <li class="nav-item"><a class="nav-link" href="#"> Login</a></li>
                                <li class="nav-item"><a class="nav-link" href="#"> Sign Up</a></li>
                            </ul>
                            <div class="user_option">
                                <form class="form-inline my-2 my-lg-0 ml-0 ml-lg-4 mb-3 mb-lg-0">
                                <button class="btn  my-2 my-sm-0 nav_search-btn" type="submit"></button>
                                </form>
                            </div>
                            </div>
                        </div>
                        </nav>
                    </div>
                    </header>

                    <section class=" slider_section position-relative">
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                        </ol>
                        <div class="carousel-inner">
                        <div class="carousel-item active">
                            <div class="container">
                            <div class="box">
                                <div class="row">
                                <div class="col-md-7">
                                    <div class="detail-box">
                                    <div>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                        <br/>
                                    </div>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </section>
                </div>
        )
    }
}

export default Header