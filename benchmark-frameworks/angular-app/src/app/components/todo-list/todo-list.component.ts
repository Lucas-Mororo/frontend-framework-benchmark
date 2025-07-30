import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Todo } from '../../models/todo.model';
import { TodoItemComponent } from '../todo-item/todo-item.component';
import { TodoFormComponent } from '../todo-form/todo-form.component';
import store, { RootState } from '../../../store/store';

@Component({
    selector: 'app-todo-list',
    templateUrl: './todo-list.component.html',
    standalone: true,
    imports: [CommonModule, TodoItemComponent, TodoFormComponent]
})
export class TodoListComponent implements OnInit {
    todos: Todo[] = [];

    ngOnInit(): void {
        this.updateTodos();

        store.subscribe(() => {
            this.updateTodos();
        });
    }

    updateTodos(): void {
        const state = store.getState() as RootState;
        this.todos = state.todos.todos;
    }
}