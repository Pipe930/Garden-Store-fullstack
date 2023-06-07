import { Component, OnDestroy, OnInit } from '@angular/core';
import { CartService } from '../services/cart.service';
import { Cart } from '../modules/cart';

@Component({
  selector: 'app-component-cart',
  templateUrl: './component-cart.component.html',
  styleUrls: ['./component-cart.component.scss']
})
export class ComponentCartComponent implements OnInit, OnDestroy {
  public items: Array<any> = [];
  public cart: Cart =  {
    id: 0,
    id_user: 0,
    items: [],
    total: 0,
    total_quantity: 0,
    total_products: 0
  };

  public user = JSON.parse(sessionStorage.getItem('user')!);

  constructor(
    private service: CartService
  ) { }

  ngOnInit(): void {
    this.getCart();
  }

  ngOnDestroy(): void {
    window.location.reload();
  }

  public getCart():void{
    this.service.getCart(
      this.user.user_id
      ).pipe(result => result).subscribe(result => {

        this.items = result.items;
        this.cart = result;

      }, error => {
        console.log(error);
      });

  }

  public substractProduct(productid: number):void{

    const json = {
      product: productid,
      id_user: this.user.user_id

    }

    this.service.cartSubstract(json);

    window.location.reload();

  }

  public sumProduct(productid: number):void {
    const json = {
      product: productid,
      quantity: 1,
      id_user: this.user.user_id
    }

    this.service.cartSum(json);

    window.location.reload();

  }

  public clearCart():void{

    this.service.cartClear(this.user.user_id);

    window.location.reload();
  }

  public deleteProduct(productID: number):void{

    this.service.deleteProductCart(this.cart.id, productID);

    window.location.reload();
  }
}
