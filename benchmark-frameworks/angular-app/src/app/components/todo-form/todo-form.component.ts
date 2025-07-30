import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import store from '../../../store/store';
import { addTodo } from '../../../store/todoSlice';

@Component({
    selector: 'app-todo-form',
    templateUrl: './todo-form.component.html',
    standalone: true,
    imports: [CommonModule, ReactiveFormsModule]
})
export class TodoFormComponent {
    todoForm: FormGroup;

    constructor(private fb: FormBuilder) {
        this.todoForm = this.fb.group({
            text: ['', [Validators.required, Validators.minLength(1)]]
        });
    }

    onSubmit(): void {
        if (this.todoForm.valid) {
            store.dispatch(addTodo(this.todoForm.value.text));
            this.todoForm.reset();
        }
    }
}