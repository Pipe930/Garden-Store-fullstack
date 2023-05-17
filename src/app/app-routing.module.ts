import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { SesionRequiredGuard } from './guards/sesion-required.guard';

const routes: Routes = [
  {
    path: "",
    redirectTo: "home",
    pathMatch: "full"
  },
  {
    path: "home",
    component: HomeComponent
  },
  {
    path: "auth",
    loadChildren: () => import("./authentication/authentication.module").then(module => module.AuthenticationModule)
  },
  {
    path: "products",
    loadChildren: () => import("./products/products.module").then(module => module.ProductsModule)
  },
  {
    path: "cart",
    loadChildren: () => import("./cart/cart.module").then(module => module.CartModule),
    canActivate: [SesionRequiredGuard]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
