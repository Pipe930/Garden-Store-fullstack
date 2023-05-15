import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthenticationService } from '../../services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public formularioLogin: FormGroup | any;

  constructor(
    private service: AuthenticationService,
    private builder: FormBuilder
    ){ }

  public construirFormulario():void{
    this.formularioLogin = this.builder.group({
      username: new FormControl("", [Validators.required, Validators.minLength(5), Validators.maxLength(60)]),
      password: new FormControl("", [Validators.required, Validators.minLength(8), Validators.maxLength(16)])
    });
  }

  public enviar():void{
    const formulario = this.formularioLogin.value
    const login = {
      username: formulario.username,
      password: formulario.password
    }

    if(this.formularioLogin.invalid){
      this.formularioLogin.markAllAsTouched();
    } else {
      this.service.login(login);
    }
  }

  ngOnInit(): void {
    this.construirFormulario();
  }

  get username(){
    return this.formularioLogin.get('username');
  }

  get password(){
    return this.formularioLogin.get('password');
  }
}
