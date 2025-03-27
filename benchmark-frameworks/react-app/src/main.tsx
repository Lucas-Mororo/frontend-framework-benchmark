import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { Provider } from 'react-redux'
import store from './store/store.ts'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Provider store={store}>
      <div className="bg-[#58c4dc] text-white p-4">
        <h1 className="text-white">Lista de Tarefas - React</h1>
      </div>
      <App />
    </Provider>
  </StrictMode>,
)
