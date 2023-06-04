import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../services/product.service';

@Component({
  selector: 'app-products-offer',
  templateUrl: './products-offer.component.html',
  styleUrls: ['./products-offer.component.scss']
})
export class ProductsOfferComponent implements OnInit {

  constructor(
    private service: ProductService
  ) { }

  ngOnInit(): void {
    this.service.getProductsOffer();
  }

  get servicio(){
    return this.service;
  }

}
