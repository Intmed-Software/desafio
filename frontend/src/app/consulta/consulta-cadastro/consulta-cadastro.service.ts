import { Time } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ConsultaCadastroService {

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(
    private http: HttpClient
  ) { }

  marcarConsulta(agenda_id: Number, horario: Time){
    const body=JSON.stringify({'agenda_id': agenda_id, 'horario': horario});
    return this.http.post(this.urlAPI + 'consultas/', body);
  }

}
