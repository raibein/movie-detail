import { useEffect, useState } from "react";


// Fetch data from api
import { getMovieContent } from '../api/list_of_api';

function MovideDetailComponent() {

    const [data, setData] = useState([]);


    useEffect(() => {
        getMovieContent(data, setData);
    }, []);

    return (
        <section class="client_section layout_padding-bottom">
            <div class="container">
                <div class="heading_container">
                    <h2>Movie Detail</h2>
                </div>


                {data.map((item, index) => (
                    <div class="box" key={index}>
                        <div class="b-1 col-sm-6">
                            <div class="client_id">
                                <div class="img-box"></div>
                                <a href= { "/movie/" + item.id }>
                                    <div class="name">
                                        <br/>
                                        <h5>{ item.name }</h5>
                                        <p>Release Date : { item.release_date }</p>
                                    </div>
                                </a>
                            </div>
                        </div>
                        <div class="client_detail col-sm-6">
                            <p>Rating : { item.rating }</p>
                            <p>{ item.short_desc }</p>
                        </div>
                    </div>
                ))}

                
                <div class="btn-box">
                    <a href="">
                    Load More
                    </a>
                </div>
            </div>
        
        </section>
    )
};

export default MovideDetailComponent;