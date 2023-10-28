// Card.js
function Card(props) {
    let img = 'https://test.api.weniv.co.kr/' + props.thumbnailImg;
    return (
        <section>
            <h2>{props.productName}!</h2>
            <p>{props.price}!</p>
            <img src={img}/>
        </section>
    );
}

export default Card;
