import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { ProductsRoutingModule } from './products-routing.module';
import { ListProductsComponent } from './components/list-products/list-products.component';
import { SearchPipe } from './pipes/search.pipe';
import { ProductService } from './services/product.service';


@NgModule({
  declarations: [
    ListProductsComponent,
    SearchPipe
  ],
  imports: [
    CommonModule,
    ProductsRoutingModule,
    HttpClientModule,
    RouterModule
  ],
  providers: [
    ProductService
  ]
})
export class ProductsModule { }
