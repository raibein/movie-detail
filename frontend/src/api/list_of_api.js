// import axios from 'axios';

// export function getMovieContent() {
//     // return axios.get('https://dummyjson.com/products');
//     return axios.get('http://127.0.0.1:5000/api/v1/movies')
//         .then(response => response.data);
// }



const base_url = "http://127.0.0.1:5000/api/v1";


export function getMovieContent(data, setData) {
    fetch(base_url + '/movies')
        .then((response) => response.json())
        .then((actualData) => {
            console.log(actualData);
            setData(actualData.data);
            console.log(data);
        })
        .catch((err) => {
            console.log(err.message);
    });
}

export function getSingleMovieContent(data, setData) {
    
    fetch(base_url + '/movie/')
        .then((response) => response.json())
        .then((actualData) => {
            console.log(actualData);
            setData(actualData.data);
            console.log(data);
        })
        .catch((err) => {
            console.log(err.message);
    });
}