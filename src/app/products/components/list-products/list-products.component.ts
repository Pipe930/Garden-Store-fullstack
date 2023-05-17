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
  public listProducts: Array<Product> = [];
  public name: string = "";
  public filterActivate: boolean = false;
  public activeList: boolean = true;
  public isNavOpen: boolean = false;

  constructor(
    private service: ProductService
  ) { }

  ngOnInit(): void {
    this.service.getCategories();
    this.service.getProducts();

    this.service.listProducts$.subscribe(restult => {
        this.listProducts = restult;
      })
  }

  public toggleNav():void {
    this.isNavOpen = !this.isNavOpen;
  }

  public loadMoreProducts():void{
    this.service.getMoreProducts();
  }

  public search(event: Event):void {
    const element = event.target as HTMLInputElement;
    this.name = element.value;
  }

  get servicio(){
    return this.service;
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

  public activateFilter():void {
    this.filterActivate = !this.filterActivate;
    this.activeList = !this.activeList;
  }
}
