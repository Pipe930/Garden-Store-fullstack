import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ListProductsComponent } from './components/list-products/list-products.component';
import { ProductComponent } from './components/product/product.component';
import { ProductOfferComponent } from './components/product-offer/product-offer.component';

const routes: Routes = [
  {
    path: "",
    component: ListProductsComponent,
    children: [
      {
        path: "offer",
        component: ProductOfferComponent
      }
    ]
  },
  {
    path: "product/:slug",
    component: ProductComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductsRoutingModule { }
