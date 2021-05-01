import { Component, OnInit } from '@angular/core';
import { Router, Event, NavigationEnd } from '@angular/router';
import { MinhaContaService } from 'src/app/cliente/minha-conta/minha-conta.service';
import { MinhaConta } from 'src/app/cliente/minha-conta/minha-conta.model';
import { InterceptorService } from 'src/app/interceptor/interceptor.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  minhaConta: MinhaConta;
  show: boolean = false;

  constructor(
    private router: Router,
    private minhaContaService: MinhaContaService
  ) { }

  ngOnInit(): void {
    let intSer = new InterceptorService();
    this.router.events.subscribe((event: Event) => {
      if (event instanceof NavigationEnd) {
        if(intSer.getAuthToken()){
          this.show = true;
          if(!this.minhaConta){
            this.getUserData();
          }
        }
      }
    })
  }

  getUserData(){
    this.minhaContaService.getMinhaConta().subscribe(data => {
      let minhaConta = new MinhaConta();
      minhaConta.id = data['id'];
      minhaConta.nome = data['nome'];
      minhaConta.usuario = data['usuario'];
      minhaConta.email = data['email'];
      this.minhaConta = minhaConta;
    });    
  }

  logout(){
    localStorage.clear();
    sessionStorage.clear();
    this.show = false;
    this.router.navigate(['/login']);
  }

}
