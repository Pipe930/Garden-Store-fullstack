import { Component } from '@angular/core';
import { FormGroup, Validators, FormControl, FormBuilder } from '@angular/forms';
import { AuthenticationService } from '../../services/authentication.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  public formularioRegister: FormGroup | any;

  constructor(
    private builder: FormBuilder,
    private servicio: AuthenticationService
  ) { }

  public construirFormulario():void {
    this.formularioRegister = this.builder.group({
      nombre: new FormControl("", [Validators.minLength(4), Validators.maxLength(20)]),
      apellido: new FormControl("", [Validators.minLength(4), Validators.maxLength(20)]),
      nombre_usuario: new FormControl("", [Validators.required, Validators.minLength(5), Validators.maxLength(60)]),
      correo: new FormControl("", [Validators.required, Validators.email, Validators.maxLength(255)]),
      contrasenia: new FormControl("", [Validators.required, Validators.minLength(8), Validators.maxLength(16)]),
      confirmarContrasenia: new FormControl("", [Validators.required, Validators.minLength(8), Validators.maxLength(16)])
    });
  }

  ngOnInit(): void {
    this.construirFormulario();
  }

  public enviar():void {
    const formulario = this.formularioRegister.value;
    const register = {
      first_name: formulario.nombre,
      last_name: formulario.apellido,
      username: formulario.nombre_usuario,
      email: formulario.correo,
      password: formulario.contrasenia
    }

    if(this.formularioRegister.invalid){
      this.formularioRegister.markAllAsTouched();
    } else {
      if(formulario.contrasenia === formulario.confirmarContrasenia){
        this.servicio.register(register);
      } else {
        console.log("La confirmacion de contraseña no esta correcta");
      }
    }

  }

  get nombre(){
    return this.formularioRegister.get('nombre');
  }

  get apellido(){
    return this.formularioRegister.get('apellido');
  }

  get nombre_usuario(){
    return this.formularioRegister.get('nombre_usuario');
  }

  get correo(){
    return this.formularioRegister.get('correo');
  }

  get contrasenia(){
    return this.formularioRegister.get('contrasenia');
  }

  get confirmarContrasenia(){
    return this.formularioRegister.get('confirmarContrasenia');
  }
}
