import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ComponentCartComponent } from './component-cart/component-cart.component';

const routes: Routes = [
  {
    path: "",
    component: ComponentCartComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CartRoutingModule { }
