import { Component, OnInit} from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthenticationService } from '../../services/authentication.service';
@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.scss']
})
export class ResetPasswordComponent implements OnInit {
  public formularioEmail: FormGroup | any;

  constructor(
    private builder: FormBuilder,
    private servicio: AuthenticationService
  ) { }

  ngOnInit(): void {
    this.construirFormulario();
  }

  public construirFormulario():void {
    this.formularioEmail = this.builder.group({
      email: new FormControl("", [Validators.required, Validators.email])
    });
  }

  public enviarCorreo():void{
    const formulario = this.formularioEmail.value

    if(this.formularioEmail.invalid){
      this.formularioEmail.markAllAsTouched();
    } else {
      this.servicio.resetPassword(formulario);
    }
  }

  get email(){
    return this.formularioEmail.get('email');
  }
}
