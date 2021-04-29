import { Injectable } from '@angular/core';
import { 
  HttpEvent,
  HttpInterceptor,
  HttpHandler,
  HttpRequest }
from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class InterceptorService implements HttpInterceptor {

  constructor() { }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    const token = this.getAuthToken();

    if (token){
      const authReq = request.clone({ 
        setHeaders: { 
          Authorization: "Token " + this.getAuthToken(),
          'Content-Type': 'application/json',
        } 
      });
      return next.handle(authReq);
    }
    const authReq = request.clone({ 
      setHeaders: { 
        'Content-Type': 'application/json',
      } 
    });

    return next.handle(authReq);
  }

  getAuthToken(){
    return (localStorage['medicarToken']) ? localStorage['medicarToken'] : sessionStorage.getItem('medicarToken');
  }

}
