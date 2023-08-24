import { Component  } from "react"

import "../css/bootstrap.css";
import "../css/responsive.css";
import "../css/style.css";
import "../css/style.css.map";

class Slider extends Component{
    render() {
        return (
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
        )
    }
}

export default Slider