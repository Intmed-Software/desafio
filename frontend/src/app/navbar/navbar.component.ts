import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MinhaContaService } from 'src/app/cliente/minha-conta/minha-conta.service';
import { MinhaConta } from 'src/app/cliente/minha-conta/minha-conta.model';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  minhaConta: MinhaConta;

  constructor(
    private router: Router,
    private  minhaContaService: MinhaContaService
  ) { }

  ngOnInit(): void {
    if (localStorage['medicarToken'] == null && sessionStorage.getItem('medicarToken') == null) {
      this.router.navigate(['/login']);
    }
    this.getUserData();
  }

  getUserData(){
    this.minhaContaService.getMinhaConta().subscribe(data => {
      let minhaConta = new MinhaConta();
      minhaConta.id = data['id'];
      minhaConta.nome = data['nome'];
      minhaConta.usuario = data['usuario'];
      minhaConta.email = data['email'];
      this.minhaConta = minhaConta;
    })
    
  }

  logout(){
    localStorage.clear();
    sessionStorage.clear();
    this.router.navigate(['/login']);
  }

}
