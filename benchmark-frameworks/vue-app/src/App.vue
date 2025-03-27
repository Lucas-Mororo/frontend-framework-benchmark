// App.vue
<template>
  <div className="bg-[#3fb984] text-white p-4">
    <h1 className="text-white">Lista de Tarefas - Vue</h1>
  </div>

  <div class="min-h-screen bg-gradient-to-br from-blue-100 to-gray-200 flex items-center justify-center p-4">
    <div class="bg-white p-6 rounded-xl shadow-2xl w-full max-w-lg transform transition-all hover:shadow-xl">
      <h1 class="text-3xl font-extrabold text-center mb-6 text-gray-800">
        Minha Todo List
      </h1>

      <!-- Formulário -->
      <form @submit.prevent="handleAddTodo" class="mb-6">
        <div class="flex gap-3">
          <input v-model="inputValue" type="text" placeholder="Digite uma tarefa..."
            class="flex-1 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transition duration-200" />
          <button type="submit"
            class="bg-blue-600 text-white px-5 py-3 rounded-lg hover:bg-blue-700 transition duration-200 font-semibold">
            Adicionar
          </button>
        </div>
      </form>

      <!-- Lista de tarefas -->
      <ul class="space-y-3">
        <p v-if="todos.length === 0" class="text-gray-500 text-center italic">
          Nenhuma tarefa ainda. Adicione uma!
        </p>
        <li v-for="todo in todos" :key="todo.id"
          class="flex items-center justify-between p-3 bg-gray-50 rounded-lg shadow-sm hover:bg-gray-100 transition duration-150">
          <div v-if="editingId === todo.id" class="flex items-center gap-2 w-full">
            <input v-model="editText" type="text"
              class="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" />
            <button @click="saveEdit(todo.id)"
              class="bg-green-500 text-white px-3 py-1 rounded-lg hover:bg-green-600 transition duration-150">
              Salvar
            </button>
            <button @click="cancelEdit"
              class="bg-gray-500 text-white px-3 py-1 rounded-lg hover:bg-gray-600 transition duration-150">
              Cancelar
            </button>
          </div>
          <div v-else class="flex items-center gap-3">
            <input type="checkbox" v-model="todo.completed" @change="toggleTodoVue(todo.id)"
              class="h-5 w-5 text-blue-600 rounded focus:ring-blue-400" />
            <span @click="startEditing(todo.id, todo.text)" :class="[
              'text-lg cursor-pointer',
              todo.completed ? 'line-through text-gray-400' : 'text-gray-700',
            ]">
              {{ todo.text }}
            </span>
          </div>
          <button v-if="editingId !== todo.id" @click="removeTodo(todo.id)"
            class="text-red-500 hover:text-red-700 font-medium transition duration-150">
            Excluir
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, inject, onMounted, onUnmounted } from 'vue';
import { addTodo, toggleTodo, deleteTodo, editTodo } from './store/todoSlice';

export default defineComponent({
  name: 'App',
  setup() {
    const store = inject('store') as any;
    const inputValue = ref<string>('');
    const editingId = ref<number | null>(null);
    const editText = ref<string>('');

    // Use a computed property to get todos from store
    const todos = ref(store.getState().todos.todos);

    // Track subscription to prevent memory leaks
    let unsubscribe: (() => void) | undefined;

    onMounted(() => {
      // Create the subscription only once on mount
      unsubscribe = store.subscribe(() => {
        // Update the local state when the store changes
        todos.value = [...store.getState().todos.todos];
      });
    });

    onUnmounted(() => {
      // Clean up subscription when component is destroyed
      if (unsubscribe) {
        unsubscribe();
      }
    });

    const handleAddTodo = () => {
      if (inputValue.value.trim()) {
        store.dispatch(addTodo(inputValue.value));
        inputValue.value = '';
      }
    };

    const toggleTodoVue = (id: number) => {
      store.dispatch(toggleTodo(id));
    };

    const removeTodo = (id: number) => {
      store.dispatch(deleteTodo(id));
    };

    const startEditing = (id: number, text: string) => {
      editingId.value = id;
      editText.value = text;
    };

    const saveEdit = (id: number) => {
      if (editText.value.trim()) {
        store.dispatch(editTodo({ id, text: editText.value }));
        editingId.value = null;
        editText.value = '';
      }
    };

    const cancelEdit = () => {
      editingId.value = null;
      editText.value = '';
    };

    return {
      inputValue,
      todos,
      editingId,
      editText,
      handleAddTodo,
      toggleTodoVue,
      removeTodo,
      startEditing,
      saveEdit,
      cancelEdit,
    };
  },
});
</script>

<style scoped>
/* Estilos locais, se necessário */
</style>