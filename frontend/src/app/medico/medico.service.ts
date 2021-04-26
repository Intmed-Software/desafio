import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Especialidade } from 'src/app/especialidade/especialidade.model';

@Injectable({
  providedIn: 'root'
})
export class MedicoService {

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(
    private http: HttpClient
  ) { }

  getMedicos(){
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
    return this.http.get(this.urlAPI + 'medicos/', {'headers':headers});
  }

  getMedicosEspecialidade(especialidade_id){
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
    return this.http.get(this.urlAPI + 'medicos/?especialidade=' + especialidade_id, {'headers':headers});
  }

}
