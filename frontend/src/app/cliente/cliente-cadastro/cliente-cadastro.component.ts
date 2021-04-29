import { Component, OnInit } from '@angular/core';
import { ClienteCadastroService } from './cliente-cadastro.service';
import { ClienteCadastro } from './cliente-cadastro.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cliente-cadastro',
  templateUrl: './cliente-cadastro.component.html',
  styleUrls: ['./cliente-cadastro.component.css']
})
export class ClienteCadastroComponent implements OnInit {

  title = 'Cadastro de Cliente';
  clientes: ClienteCadastro[];
  cliente = new ClienteCadastro();

  constructor(
    private clienteCadastroService: ClienteCadastroService, 
    private router: Router
  ) { }

  ngOnInit(): void {
    this.cliente = new ClienteCadastro;
  }

  clearForm() {
    this.cliente = new ClienteCadastro;
    this.router.navigate(['/login']);
  }

  createCliente() {
    this.clienteCadastroService.createCliente(this.cliente).subscribe(data => {
      this.cliente = new ClienteCadastro;
      this.router.navigate(['/login']);
    })
  }

}
