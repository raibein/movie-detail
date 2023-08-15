import { Component  } from "react"

import Header from "../Components/Header";
import Footer from "../Components/Footer";

// Import small html content which send the data from api and APIs data send from this page
import MovieDetailByIdComponent from '../Components/MovieDetailByIdComponent';


class MovieByIdContainer extends Component{
    
    render() {
        return (
            <div>
                
                <Header />

                <MovieDetailByIdComponent />

                <Footer />


            </div>
        )
    }
}

export default MovieByIdContainer