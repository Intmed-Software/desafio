import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EspecialidadeService {

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  getEspecialidades(){

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
    return this.http.get(this.urlAPI + 'especialidades/', {'headers':headers});
  }
}
