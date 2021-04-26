import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ConsultaListaService {

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  getConsultas(){
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
    return this.http.get(this.urlAPI + 'consultas/', {'headers':headers});
  }

  deleteConsulta(id=null){
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
    return this.http.delete(this.urlAPI + 'consultas/' + id + '/', {'headers':headers});
  }

}
