import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { CartRoutingModule } from './cart-routing.module';
import { ComponentCartComponent } from './component-cart/component-cart.component';
import { CartService } from './services/cart.service';
import { TokenInterceptorService } from '../services/token-interceptor.service';


@NgModule({
  declarations: [
    ComponentCartComponent
  ],
  imports: [
    CommonModule,
    CartRoutingModule,
    HttpClientModule,
    RouterModule
  ],
  providers: [
    CartService,
    {provide: HTTP_INTERCEPTORS, useClass: TokenInterceptorService, multi: true}
  ]
})
export class CartModule { }
