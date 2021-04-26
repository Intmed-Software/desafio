import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Time } from '@angular/common';
import { EspecialidadeService } from 'src/app/especialidade/especialidade.service';
import { Especialidade } from 'src/app/especialidade/especialidade.model';
import { MedicoService } from 'src/app/medico/medico.service';
import { Medico } from 'src/app/medico/medico.model';
import { AgendaService } from 'src/app/agenda/agenda.service';
import { Agenda } from 'src/app/agenda/agenda.model';
import { ConsultaCadastroService } from './consulta-cadastro.service';

@Component({
  selector: 'app-consulta-cadastro',
  templateUrl: './consulta-cadastro.component.html',
  styleUrls: ['./consulta-cadastro.component.css']
})
export class ConsultaCadastroComponent implements OnInit {

  especialidades: Especialidade[] = []; 
  medicos: Medico[] = [];
  agendas: Agenda[] = [];
  horarios: Time[] = [];

  slcEspecialidade: Number = 0;
  slcMedico: Number = 0;
  slcData: Number = 0;
  slcHora: Time = null;

  slcMedicoDisable: Boolean = true;
  slcDataDisable: Boolean = true;
  slcHoraDisable: Boolean = true;
  slcCadastroDisable: Boolean = true;

  constructor(
    private router: Router,
    private especialidadesService: EspecialidadeService,
    private medicosService: MedicoService,
    private agendaService: AgendaService,
    private consultaCadastroService: ConsultaCadastroService
  ) { }

  ngOnInit(): void {
    if (localStorage['medicarToken'] == null && sessionStorage.getItem('medicarToken') == null) {
      this.router.navigate(['/login']);
    }
    this.getEspecialidades();
  }

  clearForm() {
    this.horarios = [];
    this.agendas = [];
    this.medicos = [];
    this.especialidades = [];
    this.slcHora = null;
    this.slcData = null;
    this.slcMedico = null;
    this.slcEspecialidade = null;
    this.slcMedicoDisable = true;
    this.slcDataDisable = true;
    this.slcHoraDisable = true;
    this.slcCadastroDisable = true;
    this.getEspecialidades();
  }

  marcarConsulta(){
    this.consultaCadastroService.marcarConsulta(this.slcData, this.slcHora).subscribe(data => {
      this.clearForm();
      this.router.navigate(['/']);
    })
  }

  getEspecialidades() {
    let especialidadesArray = [];
    this.especialidadesService.getEspecialidades().subscribe(data => {
      for (let index = 0; index < data['length']; index++) {
        especialidadesArray.push(data[index]);
      }      
    });
    this.especialidades = especialidadesArray;
  }

  getMedicos() {
    this.medicos = [];
    if (this.slcEspecialidade == 0 || this.slcEspecialidade == null) return null;
    let medicosArray = [];
    this.medicosService.getMedicosEspecialidade(this.slcEspecialidade).subscribe(data => {
      for (let index = 0; index < data['length']; index++) {
        medicosArray.push(data[index]);
      }
    });
    this.medicos = medicosArray;
    this.slcMedicoDisable = null;
  }

  getAgendas(){
    this.agendas = [];
    if (this.slcMedico == 0 || this.slcMedico == null) return null;
    let agendasArray = [];
    this.agendaService.getAgendasMedico(this.slcMedico).subscribe(data => {
      for (let index = 0; index < data['length']; index++) {
        agendasArray.push(data[index]);
      }
    });
    this.agendas = agendasArray;
    this.slcDataDisable = null;
  }

  getHorarios(){
    this.horarios = [];
    let agenda_id = this.slcData;
    let agenda = this.agendas.find(agenda => agenda.id == agenda_id);
    this.horarios = agenda.horarios;
    this.slcHoraDisable = null;
  }

}
