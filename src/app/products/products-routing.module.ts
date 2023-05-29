import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ListProductsComponent } from './components/list-products/list-products.component';
import { ProductComponent } from './components/product/product.component';
import { ProductsOfferComponent } from './components/products-offer/products-offer.component';

const routes: Routes = [
  {
    path: "",
    component: ListProductsComponent,
  },
  {
    path: "product/:slug",
    component: ProductComponent
  },
  {
    path: "offers",
    component: ProductsOfferComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductsRoutingModule { }
