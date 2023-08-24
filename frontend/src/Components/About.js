import { Component  } from "react"

import "../css/bootstrap.css";
import "../css/responsive.css";
import "../css/style.css";
import "../css/style.css.map";

class About extends Component{
    render() {
        return (
               
            <section class="about_section layout_padding-bottom" id="about">
                <div class="container">
                    <div class="heading_container">
                        <h2>
                        About This Site
                        </h2>
                    </div>
                    <div class="box">
                        <div class="img-box">
                        <img src={require ('../images/movie.jpeg')} alt="" />
                        </div>
                        <br/>
                        <br/>
                        <div class="detail-box">
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                            dolore magna aliqua. Ut enim ad minim veniamLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                            eiusmod tempor incididunt ut labore
                            et dolore magna aliqua. Ut enim ad minim
                        </p>
                        </div>
                    </div>
                </div>
            </section>
        )
    }
}

export default About