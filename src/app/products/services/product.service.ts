import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Product, ResponseProducts } from '../modules/product';
import { Category } from '../modules/category';
import { BehaviorSubject, delay, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private url: string = "http://127.0.0.1:8000/api/v1/products/";
  private page: number = 0;

  public listProducts = new BehaviorSubject<Array<Product>>([]);
  public listProducts$ = this.listProducts.asObservable();

  public listSearch: Array<Product> = [];

  public listCategories: Array<Category> = [];
  public activeFooter: boolean = false;

  public listProductsOffer = new BehaviorSubject<Array<Product>>([]);
  public listProductsOffer$ = this.listProductsOffer.asObservable();

  constructor(
    private http: HttpClient
  ) { }

  public getProducts():void{
    this.http.get<ResponseProducts>(this.url, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(
      delay(1000)
    ).subscribe(result => {
      this.page = this.page + 1;
      this.listProducts.next(result.results);
      if(result.results.length){
        this.activeFooter = true;
      }
    }, error => {
      console.log(error);
    });
  }

  public getMoreProducts():void {
    this.http.get<any>(`${this.url}?page=${this.page}`, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(
      delay(1000)
    ).subscribe(result => {
      this.page = this.page + 1;
      this.listProducts.next(this.listProducts.getValue().concat(result.products));
    }, error => {
      console.log(error);
    });
  }

  public getProduct(slug: string):Observable<Product>{
    return this.http.get<Product>(`${this.url}product/${slug}`, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    });
  }

  public searchProduct(name: string):void{
    this.http.get<ResponseProducts>(
      `${this.url}product?search=${name}`,
      {
        headers: new HttpHeaders({
          'Content-Type': 'application/json'
        })
      }
    ).subscribe(resultado => {
      this.listSearch = resultado.results;
    }, error => {
      console.log(error);
    });
  }

  public filterProduct(id: string):Observable<ResponseProducts>{
    return this.http.get<ResponseProducts>(`${this.url}category/${id}`, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    })
  }

  public getCategories():void{
    this.http.get<Array<Category>>('http://127.0.0.1:8000/api/v1/categories/', {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).subscribe(resultado => {
      this.listCategories = resultado;
    }, error => {
      console.log(error);
    })
  }

  public getProductsOffer():void{
    this.http.get<ResponseProducts>(`${this.url}offer/`, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(
      delay(1000)
    ).subscribe(result => {
      this.page = this.page + 1;
      this.listProductsOffer.next(result.results);
      console.log(result.results);
      if(result.results.length){
        this.activeFooter = true;
      }
    }, error => {
      console.log(error);
    });
  }
}
