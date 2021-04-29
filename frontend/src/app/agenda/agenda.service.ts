import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AgendaService {

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(
    private http: HttpClient
  ) { }

  getAgendas(){
    return this.http.get(this.urlAPI + 'agendas/');
  }

  getAgendasMedico(medico_id: Number){
    return this.http.get(this.urlAPI + 'agendas/?medico=' + medico_id);
  }

}
