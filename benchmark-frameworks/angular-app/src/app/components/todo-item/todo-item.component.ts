import { Component, Input, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormControl, ReactiveFormsModule, Validators } from '@angular/forms';
import { Todo } from '../../models/todo.model';
import store from '../../../store/store';
import { deleteTodo, editTodo, toggleTodo } from '../../../store/todoSlice';

@Component({
    selector: 'app-todo-item',
    templateUrl: './todo-item.component.html',
    standalone: true,
    imports: [CommonModule, ReactiveFormsModule]
})
export class TodoItemComponent implements OnInit {
    @Input() todo!: Todo;
    isEditing = false;
    textControl!: FormControl;

    ngOnInit(): void {
        this.textControl = new FormControl(this.todo.text, [
            Validators.required,
            Validators.minLength(3)
        ]);
    }

    onToggle(): void {
        store.dispatch(toggleTodo(this.todo.id));
    }

    onDelete(): void {
        store.dispatch(deleteTodo(this.todo.id));
    }

    startEditing(): void {
        this.isEditing = true;
    }

    saveEdit(): void {
        if (this.textControl.valid) {
            store.dispatch(
                editTodo({ id: this.todo.id, text: this.textControl.value })
            );
            this.isEditing = false;
        }
    }

    cancelEdit(): void {
        this.textControl.setValue(this.todo.text);
        this.isEditing = false;
    }
}