import { useState } from "react";

export default function HandEvaluatorForm() {
    const [cards, setCards] = useState([{ rank: "", suit: "" }, { rank: "", suit: "" }]);
    const [result, setResult] = useState(null);

    const updateField = (index, field, value) => {
        const updated = [...cards]
        updated[index][field] = value.toUpperCase();
        setCards(updated);
    }

    const addCard = () => {
        if (cards.length < 5){
            setCards([...cards, { rank: "", suit: ""}])
        }
    }

    const evaluate = async () => {
        const response = await fetch("http://127.0.0.1:5000/evaluate-hand", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify( {cards} )
        });
        const data = await response.json();
        setResult(data);
    }

    return (
        <div>
            <h2>Enter Cards:</h2>
            {cards.map((card,index) => (
                <div key={index}>
                    <input 
                        placeholder="Rank (e.g., A, K, T)"
                        value = {card.rank}
                        onChange={e => updateField(index, "rank", e.target.value)} 
                    />
                    <input
                        placeholder="Suit (S, C, H, D)"
                        value = {card.suit}
                        onChange={e => updateField(index, "suit", e.target.value)}
                    />
                </div>
            ))}
             <button onClick={addCard}>
                Add Card
            </button>
            <button onClick={evaluate}>
                Evaluate
            </button>

            {result && (
                <div>
                    <h3> Result </h3>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>    
            )}
        </div>


       
    )




}

