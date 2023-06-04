import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { Cart } from '../modules/cart';
import { AddCart } from '../modules/add-cart';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CartService {

  public urlCart: string = 'http://192.168.1.11:8000/api/v1/cart/';

  constructor(
    private http: HttpClient,
    private rout: Router
  ) { }

  public cartAdd(product: AddCart):void{
    this.http.post<Cart>(`${this.urlCart}item/add`, product, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        "Authorization": 'Token ' + sessionStorage.getItem('token')!
      })
    }).subscribe(result => {
      if(result){
        Swal.fire({
          title: "Se agrego con exito el producto la carrito",
          icon: "success"
        });
        this.rout.navigate(['cart']);
      }
    }, error => {
      Swal.fire({
        title: "Ocurrio un error no se agrego el producto al carrito",
        icon: "error"
      });
      console.log(error);
    });
  }

  public getCart(id: number):Observable<Cart>{
    return this.http.get<Cart>(`${this.urlCart}user/${id}`, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    });
  }

  public cartSubstract(product: any):void{
    this.http.post<any>(`${this.urlCart}item/substract`, product, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    });
  }

  public cartSum(product: AddCart):void{
    this.http.post<Cart>(`${this.urlCart}item/add`, product, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).subscribe(result => {
      if(result){
        // console.log(result);
      }
    }, error => {
      console.log(error);
    });
  }

  public cartClear(id_cart: number):void{
    this.http.delete(`${this.urlCart}clear/${id_cart}`, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).subscribe(result => {
      if(result){
        console.log(result);
      }
    }, error => {
      console.log(error);
    });
  }
}
