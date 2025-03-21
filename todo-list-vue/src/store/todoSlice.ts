import { createSlice } from '@reduxjs/toolkit';
import type { PayloadAction } from '@reduxjs/toolkit';

interface Todo {
    id: number;
    text: string;
    completed: boolean;
}

interface TodoState {
    todos: Todo[];
}

const loadState = (): TodoState => {
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
        return { todos: JSON.parse(savedTodos) };
    }
    return { todos: [] };
};

const initialState: TodoState = loadState();

const todoSlice = createSlice({
    name: 'todos',
    initialState,
    reducers: {
        addTodo: (state, action: PayloadAction<string>) => {
            state.todos.push({
                id: Date.now(),
                text: action.payload,
                completed: false,
            });
            localStorage.setItem('todos', JSON.stringify(state.todos));
        },
        toggleTodo: (state, action: PayloadAction<number>) => {
            const todo = state.todos.find((todo) => todo.id === action.payload);
            if (todo) {
                todo.completed = !todo.completed;
            }
            localStorage.setItem('todos', JSON.stringify(state.todos));
        },
        deleteTodo: (state, action: PayloadAction<number>) => {
            state.todos = state.todos.filter((todo) => todo.id !== action.payload);
            localStorage.setItem('todos', JSON.stringify(state.todos));
        },
        editTodo: (state, action: PayloadAction<{ id: number; text: string }>) => {
            const todo = state.todos.find((todo) => todo.id === action.payload.id);
            if (todo) {
                todo.text = action.payload.text;
            }
            localStorage.setItem('todos', JSON.stringify(state.todos));
        },
    },
});

export const { addTodo, toggleTodo, deleteTodo, editTodo } = todoSlice.actions;
export default todoSlice.reducer;