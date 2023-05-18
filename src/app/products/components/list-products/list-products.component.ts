import { Component } from '@angular/core';
import { ProductService } from '../../services/product.service';
import { Product } from '../../modules/product';

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

  public search(event: Event):void {
    this.page = 0;
    const element = event.target as HTMLInputElement;
    this.name = element.value;
  }

  get servicio(){
    return this.service;
  }

  public nextPage():void{
    this.page += 10;
    this.numbrePage += 1;
  }

  public prevPage():void{
    if(this.page > 0){
      this.page -= 10;
      this.numbrePage -= 1;
    }
  }

  public filter(event: Event):void {
    const element = event.target as HTMLSelectElement;
    this.service.filterProduct(
      element.value
      ).subscribe(result => {
        if(result){
          this.listFilter = result;
        }
    }, error => {
      console.log(error);
    })
  }

}
