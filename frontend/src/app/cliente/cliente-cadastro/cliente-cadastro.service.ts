import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ClienteCadastro } from './cliente-cadastro.model';

@Injectable({
  providedIn: 'root'
})
export class ClienteCadastroService {

  urlAPI: string = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) { }

  createCliente(cliente: ClienteCadastro) {
    const body=JSON.stringify(cliente);
    return this.http.post(this.urlAPI + 'conta/cadastrar/', body)
  }

}
