import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import Swal from 'sweetalert2';

@Injectable({
  providedIn: 'root'
})
export class SesionRequiredGuard implements CanActivate {

  constructor(
    private ruta: Router
    ) {}

  canActivate() {
    if(sessionStorage.getItem('token')!=null){
      return true;
    }

    Swal.fire({
      title: "Debes Iniciar Sesion",
      text: "Para poder Acceder esta ruta debes iniciar sesion",
      icon: "info"
    })
    this.ruta.navigate(['auth/login']);
    return false;

  }

}
