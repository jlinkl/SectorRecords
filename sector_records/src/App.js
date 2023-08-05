import './App.css';
import { useState, useEffect } from 'react';
// https://www.speedrun.com/api/v1/leaderboards/nd2853vd/category/7kj9lyz2

function App() {

  const [data, setData] = useState(null);

  useEffect(() => {
    //fetching the leaderboard for dreaming city lost sectors, as a place to start
    const request = fetch("https://www.speedrun.com/api/v1/games/nd2853vd/records?top=1")
    .then(response => response.json())
    .then(data => console.log(data))
  }, [])

  return (
    <div>
      
    </div>
  );
}

export default App;
