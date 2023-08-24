import { Component  } from "react"

import Header from "../Components/Header";
import Footer from "../Components/Footer";

import How from "../Components/How";
import About from "../Components/About";

// Import small html content which send the data from api and APIs data send from this page
import MovideDetailComponent from '../Components/MovieDetailComponent';


class DefaultContainer extends Component{
    
    render() {
        return (
            <div>
                
                <Header />

                <How />

                <About />
            
                <MovideDetailComponent />

                <Footer />

            </div>
        )
    }
}

export default DefaultContainer