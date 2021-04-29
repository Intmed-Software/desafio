import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './cliente/login/login.component';
import { ClienteCadastroComponent } from './cliente/cliente-cadastro/cliente-cadastro.component'
import { ConsultaListaComponent } from './consulta/consulta-lista/consulta-lista.component';
import { ConsultaCadastroComponent } from './consulta/consulta-cadastro/consulta-cadastro.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent},
  { path: '', component: ConsultaListaComponent},
  { path: 'conta/cadastrar', component: ClienteCadastroComponent },
  { path: 'consultas', component: ConsultaListaComponent},
  { path: 'consultas/cadastrar', component:ConsultaCadastroComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
