import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Product, ResponseProducts } from '../modules/product';
import { Category } from '../modules/category';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private url: string = "http://192.168.1.11:8000/api/v1/products/";

  public listProducts: Array<Product> = [];
  public activateMessage: boolean = true;

  public listCategories: Array<Category> = [];
  public activeFooter: boolean = false;

  public listProductsOffer: Array<Product> = [];
  public activateMessageOffer: boolean = true;

  constructor(
    private http: HttpClient
  ) { }

  public getProduct(slug: string):Observable<Product>{
    return this.http.get<Product>(`${this.url}product/${slug}`);
  }

  public getProducts():void{
    this.http.get<Array<Product>>(this.url).subscribe(result => {
      if(result){
        this.activateMessage = false;
        this.listProducts = result;
      }
    })
  }

  public getCategories():void{
    this.http.get<Array<Category>>('http://192.168.1.11:8000/api/v1/categories/').subscribe(result => {
      this.listCategories = result;
    }, error => {
      console.log(error);
    })
  }

  public getProductsOffer():void{
    this.http.get<any>(`${this.url}offer`).subscribe(result => {
      if(result){
        this.listProductsOffer = result.results;
        this.activateMessageOffer = false;
      }
    }, error => {
      console.log(error);
    })
  }
}
