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
    return this.http.get(this.urlAPI + 'medicos/');
  }

  getMedicosEspecialidade(especialidade_id){
    return this.http.get(this.urlAPI + 'medicos/?especialidade=' + especialidade_id);
  }

}
