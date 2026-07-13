import React, { useState, useEffect } from "react";

function Home() {

    const [count, setCount] = useState(0);

    useEffect(() => {

        document.title = `Counter ${count}`;

    }, [count]);

    return (

        <div className="page">

            <h2>Home Page</h2>

            <h3>Counter : {count}</h3>

            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>

        </div>

    );

}

export default Home;