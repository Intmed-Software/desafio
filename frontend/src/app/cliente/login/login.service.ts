import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Login } from './login.model';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  urlAPI: string = 'http://127.0.0.1:8000/';
  login = new Login;

  constructor(private http: HttpClient) { }

  userLogin(login: Login) {
    const headers = { 'content-type': 'application/json'}  
    const body=JSON.stringify(login);
    return this.http.post(this.urlAPI + 'conta/login/', body,{'headers':headers})
  }

}
