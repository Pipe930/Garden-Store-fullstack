import { Component } from '@angular/core';
import { ProductService } from '../../services/product.service';

@Component({
  selector: 'app-list-products',
  templateUrl: './list-products.component.html',
  styleUrls: ['./list-products.component.scss']
})
export class ListProductsComponent {

  public listFilter: any;
  public name: string = "";
  public activeList: boolean = true;
  public isNavOpen: boolean = false;
  public page: number = 0;
  public numbrePage: number = 1;
  public category: string = "";

  constructor(
    private service: ProductService
  ) { }

  ngOnInit(): void {
    this.service.getCategories();
    this.service.getProducts();
  }

  public toggleNav():void {
    this.isNavOpen = !this.isNavOpen;
  }

  // public search(event: Event):void {
  //   this.page = 0;
  //   const element = event.target as HTMLInputElement;
  //   this.name = element.value;
  // }

  public search(name_product:string):void{
    this.page = 0;
    this.name = name_product;
    console.log(this.name);
  }

  get servicio(){
    return this.service;
  }

  public nextPage():void{
    this.page += 10;
    this.numbrePage += 1;
    window.scrollTo({
      top: 0
    });
  }

  public prevPage():void{
    if(this.page > 0){
      this.page -= 10;
      this.numbrePage -= 1;
      window.scrollTo({
        top: 0
      });
    }
  }

  public getCategory(name_category: string):void{
    this.category = name_category;
  }

  public noneFilter():void{
    this.category = "";
  }

  public filter(event: Event):void {
    const element = event.target as HTMLSelectElement;
    this.category = element.value;
  }

}
