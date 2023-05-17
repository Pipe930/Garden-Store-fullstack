import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor {

  private token: string = sessionStorage.getItem('token')!;

  constructor() { }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    let jwtToken = request.clone({
      setHeaders: {
        Authorization: 'Token ' + this.token
      }
    });

    return next.handle(jwtToken);
  }
}
