import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule }   from '@angular/forms';
import { InterceptorModule } from './interceptor/interceptor.module';
// Import Components
import { LoginComponent } from './cliente/login/login.component';
import { EspecialidadeComponent } from './especialidade/especialidade.component';
import { MedicoComponent } from './medico/medico.component';
import { ClienteCadastroComponent } from './cliente/cliente-cadastro/cliente-cadastro.component';
import { ConsultaCadastroComponent } from './consulta/consulta-cadastro/consulta-cadastro.component';
import { ConsultaListaComponent } from './consulta/consulta-lista/consulta-lista.component';
import { AgendaComponent } from './agenda/agenda.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LogoutComponent } from './cliente/logout/logout.component';
import { MinhaContaComponent } from './cliente/minha-conta/minha-conta.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    EspecialidadeComponent,
    MedicoComponent,
    ClienteCadastroComponent,
    ConsultaCadastroComponent,
    ConsultaListaComponent,
    AgendaComponent,
    NavbarComponent,
    LogoutComponent,
    MinhaContaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    InterceptorModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
