import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Contact } from '../modules/contact';

@Injectable({
  providedIn: 'root'
})
export class ContactService {

  public ruta: string = "http://192.168.1.11:8000/api/v1/user/sendEmail";

  constructor(
    private http: HttpClient
  ) { }

  public sendEmail(formulario: Contact):void {

    this.http.post<any>(this.ruta, formulario, {
      headers: new HttpHeaders({
        "Content-Type": "application/json",
        "Authorization": "Token " + sessionStorage.getItem("token")!
      })
    }).subscribe(result => {
      if(result){
        console.log(result);
      }
    }, error => {
      console.log(error);
    })
  }
}
