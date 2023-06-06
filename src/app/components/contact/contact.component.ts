import { Component, OnInit } from '@angular/core';
import { Validators, FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { ContactService } from 'src/app/services/contact.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent implements OnInit {

  public formContact: FormGroup | any;

  constructor(
    private builder: FormBuilder,
    private service: ContactService
  ) { }

  ngOnInit(): void {
    this.builderForm();
  }

  public builderForm():void{

    this.formContact = this.builder.group({
      nombre: new FormControl("" ,[Validators.maxLength(20), Validators.minLength(4), Validators.required]),
      apellido: new FormControl("" ,[Validators.maxLength(20), Validators.minLength(4), Validators.required]),
      rut: new FormControl("", [Validators.maxLength(10), Validators.minLength(9), Validators.required]),
      telefono: new FormControl("+56", [Validators.required, Validators.maxLength(12)]),
      correo: new FormControl("", [Validators.maxLength(255), Validators.required, Validators.email]),
      mensaje: new FormControl("", [Validators.maxLength(255), Validators.required])
    })
  }

  public sendMessage():void{

    let formulario = this.formContact.value;

    let formulairoJSON = {
      full_name: `${formulario.nombre} ${formulario.apellido}`,
      email: formulario.correo,
      message: formulario.mensaje
    }

    if(this.formContact.invalid){
      this.formContact.markAllAsTouched();
    } else {
      this.service.sendEmail(formulairoJSON);
    }
  }

  get nombre(){
    return this.formContact.get('nombre');
  }

  get apellido(){
    return this.formContact.get('apellido');
  }

  get rut(){
    return this.formContact.get('rut');
  }

  get telefono(){
    return this.formContact.get('telefono');
  }

  get correo(){
    return this.formContact.get('correo');
  }

  get mensaje(){
    return this.formContact.get('mensaje');
  }
}
