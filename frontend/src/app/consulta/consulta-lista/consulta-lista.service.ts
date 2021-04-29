import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ConsultaListaService {

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  getConsultas(){
    return this.http.get(this.urlAPI + 'consultas/');
  }

  deleteConsulta(id=null){
    return this.http.delete(this.urlAPI + 'consultas/' + id + '/');
  }

}
