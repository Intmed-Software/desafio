import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MinhaConta } from './minha-conta.model';

@Injectable({
  providedIn: 'root'
})
export class MinhaContaService {

  minhaConta: MinhaConta;

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  getMinhaConta(){
    let token: String;

    if (localStorage['medicarToken'])
    {
      token = localStorage['medicarToken'];
    }
    else {
      token = sessionStorage.getItem('medicarToken')
    }

    const headers = {
      'Authorization': "Token " + token
    }
    return this.http.get(this.urlAPI + 'conta/minha-conta/', {'headers':headers});
  }
}
