import { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/users/")
      .then((response) => response.json())
      .then((data) => {
        console.log("Dados recebidos:", data);
        setUsers(data.users || []); // Garante que `users` sempre seja um array
      })
      .catch((error) => console.error("Erro ao buscar usuários:", error));
  }, []);

  return (
    <div>
      <h1>Lista de Usuários</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.username} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
