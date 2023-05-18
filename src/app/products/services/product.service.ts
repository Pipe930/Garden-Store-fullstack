import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Product, ResponseProducts } from '../modules/product';
import { Category } from '../modules/category';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private url: string = "http://127.0.0.1:8000/api/v1/products/";

  public listProducts: Array<Product> = [];
  public activateMessage: boolean = true;

  public listCategories: Array<Category> = [];
  public activeFooter: boolean = false;

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

  public filterProduct(id: string):Observable<ResponseProducts>{
    return this.http.get<ResponseProducts>(`${this.url}category/${id}`)
  }

  public getCategories():void{
    this.http.get<Array<Category>>('http://127.0.0.1:8000/api/v1/categories/').subscribe(resultado => {
      this.listCategories = resultado;
    }, error => {
      console.log(error);
    })
  }
}
