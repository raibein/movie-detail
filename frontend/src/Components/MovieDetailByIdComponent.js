import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";


// Fetch data from api
import { getSingleMovieContent } from '../api/list_of_api';

function MovieDetailByIdComponent() {

    const [data, setData] = useState([]);
    const param = useParams();
    console.log(param.id);


    useEffect(() => {
        getSingleMovieContent(data, setData, param.id);
    }, []);

    return (
        <section class="client_section layout_padding-bottom">

            <div class="container">
                <div class="heading_container">
                    <h2>Movie's Full Detail</h2>
                </div>

                <div class="box">
                    <div class="b-1 col-sm-12">
                        <h5><b>{ data.name }</b></h5>
                        <p>Release Date : { data.release_date }</p>
                        <p>Rating : { data.rating }</p>
                        <p>{ data.description }</p>
                    </div>
                </div>
            </div>
        
        </section>
    )
};

export default MovieDetailByIdComponent;