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
    return this.http.get(this.urlAPI + 'agendas/', {'headers':headers});
  }

  getAgendasMedico(medico_id: Number){
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
    return this.http.get(this.urlAPI + 'agendas/?medico=' + medico_id, {'headers':headers});
  }

}
