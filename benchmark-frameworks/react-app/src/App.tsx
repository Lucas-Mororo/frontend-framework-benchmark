import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addTodo, toggleTodo, deleteTodo, editTodo } from './store/todoSlice';
import { RootState } from './store/store';

function App() {
  const [inputValue, setInputValue] = useState<string>('');
  const [editingId, setEditingId] = useState<number | null>(null); // ID da tarefa sendo editada
  const [editText, setEditText] = useState<string>(''); // Texto editado
  const dispatch = useDispatch();
  const todos = useSelector((state: RootState) => state.todos.todos);

  const handleAddTodo = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputValue.trim()) {
      dispatch(addTodo(inputValue));
      setInputValue('');
    }
  };

  const startEditing = (id: number, text: string) => {
    setEditingId(id);
    setEditText(text);
  };

  const saveEdit = (id: number) => {
    if (editText.trim()) {
      dispatch(editTodo({ id, text: editText }));
      setEditingId(null);
      setEditText('');
    }
  };

  const cancelEdit = () => {
    setEditingId(null);
    setEditText('');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-gray-200 flex items-center justify-center p-4">
      <div className="bg-white p-6 rounded-xl shadow-2xl w-full max-w-lg transform transition-all hover:shadow-xl">
        <h1 className="text-3xl font-extrabold text-center mb-6 text-gray-800">
          Minha Todo List
        </h1>

        {/* Formulário */}
        <form onSubmit={handleAddTodo} className="mb-6">
          <div className="flex gap-3">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Digite uma tarefa..."
              className="flex-1 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-200"
            />
            <button
              type="submit"
              className="bg-blue-600 text-white px-5 py-3 rounded-lg hover:bg-blue-700 transition duration-200 font-semibold"
            >
              Adicionar
            </button>
          </div>
        </form>

        {/* Lista de tarefas */}
        <ul className="space-y-3">
          {todos.length === 0 ? (
            <p className="text-gray-500 text-center italic">
              Nenhuma tarefa ainda. Adicione uma!
            </p>
          ) : (
            todos.map((todo) => (
              <li
                key={todo.id}
                className="flex items-center justify-between p-3 bg-gray-50 rounded-lg shadow-sm hover:bg-gray-100 transition duration-150"
              >
                {editingId === todo.id ? (
                  <div className="flex items-center gap-2 w-full">
                    <input
                      type="text"
                      value={editText}
                      onChange={(e) => setEditText(e.target.value)}
                      className="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
                    />
                    <button
                      onClick={() => saveEdit(todo.id)}
                      className="bg-green-500 text-white px-3 py-1 rounded-lg hover:bg-green-600 transition duration-150"
                    >
                      Salvar
                    </button>
                    <button
                      onClick={cancelEdit}
                      className="bg-gray-500 text-white px-3 py-1 rounded-lg hover:bg-gray-600 transition duration-150"
                    >
                      Cancelar
                    </button>
                  </div>
                ) : (
                  <>
                    <div className="flex items-center gap-3">
                      <input
                        type="checkbox"
                        checked={todo.completed}
                        onChange={() => dispatch(toggleTodo(todo.id))}
                        className="h-5 w-5 text-blue-600 rounded focus:ring-blue-400"
                      />
                      <span
                        onClick={() => startEditing(todo.id, todo.text)}
                        className={`text-lg cursor-pointer ${todo.completed
                          ? 'line-through text-gray-400'
                          : 'text-gray-700'
                          }`}
                      >
                        {todo.text}
                      </span>
                    </div>
                    <button
                      onClick={() => dispatch(deleteTodo(todo.id))}
                      className="text-red-500 hover:text-red-700 font-medium transition duration-150"
                    >
                      Excluir
                    </button>
                  </>
                )}
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  );
}

export default App;