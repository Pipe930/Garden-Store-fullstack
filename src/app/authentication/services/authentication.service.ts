import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { map, first } from 'rxjs/operators';
import Swal from 'sweetalert2';
import { Login, LoginResponse, ResetPassword } from '../modules/login';
import { Register, RegisterResponse } from '../modules/register';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private urlApi: string = "http://127.0.0.1:8000/api/v1/user/";

  constructor(
    private http: HttpClient,
    private route: Router
  ) { }

  public login(formulario: Login):void{
    this.http.post<LoginResponse>(`${this.urlApi}auth/login`, formulario, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(
      map(user => {
        if(user && user.token){
          sessionStorage.setItem('token', user.token);
          sessionStorage.setItem('user', JSON.stringify(user));
        }
        return user;
      })
    ).pipe(first()).subscribe(result => {
      if(result){
        Swal.fire({
          icon: "success",
          title: `Bienvenido ${result.username}`,
          text: "Bienvenido a Garden Store"
        });
        this.route.navigate(['home']);
      }
    }, error => {
      console.log(error);
      Swal.fire({
        icon: "error",
        title: "Error de Inicio Sesion",
        text: "Las credenciales que ingresastes no son correctas"
      });
    }
    );
  }

  public register(formulario: Register):void{
    this.http.post<RegisterResponse>(`${this.urlApi}register`, formulario, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).subscribe(result => {
        if(result){
          Swal.fire({
            icon: "success",
            title: "Te registraste correctamente",
            text: "El registro fue un exito"
          });
          this.route.navigate(['auth/login']);
        }
      }, error => {
        console.log(error);
        Swal.fire({
          icon: "error",
          title: "Error al Registrarse",
          text: "Ocurrio un error, debes ingresar bien los datos"
        });
      }

    );
  }

  public logout(token: string):void{
    this.http.get<any>(`${this.urlApi}auth/logout?token=${token}`, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        "Authorization": 'Token ' + sessionStorage.getItem('token')!
      })
    }).subscribe(result => {
      if(result){
        sessionStorage.clear();
        this.route.navigate(['home']);
      }
    }, error => {
      console.log(error);
    });
  }

  public resetPassword(formulario: ResetPassword): void{
    this.http.post<any>(`${this.urlApi}password-reset/`, formulario, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',

      }),
      withCredentials:true
    }).subscribe(result => {
      if(result){
        Swal.fire({
          title: "Envio Exitoso",
          icon: "success",
          text: "Se envio un correo para reestablezer tu contraseña"
        });
        this.route.navigate(['auth/login']);
      }
  }, error => {
    console.log(error);
  });
  }
}
