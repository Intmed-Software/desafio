import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ConsultaListaService } from './consulta-lista.service';
import { ConsultaLista } from './consulta-lista.model'

@Component({
  selector: 'app-consulta-lista',
  templateUrl: './consulta-lista.component.html',
  styleUrls: ['./consulta-lista.component.css']
})
export class ConsultaListaComponent implements OnInit {

  consultas: ConsultaLista[] = [];

  constructor(
    private router: Router,
    private consultaListaService: ConsultaListaService
  ) { }

  ngOnInit(): void {
    this.getConsultas();
  }

  getConsultas(){
    this.consultas.length = 0
    this.consultaListaService.getConsultas().subscribe(data => {
      for(let i = 0; i<data['length']; i++){
        let consultaLista = new ConsultaLista();
        let consulta = data[i];
        consultaLista.id = consulta.id;
        consultaLista.especialidade = consulta.especialidade;
        consultaLista.medico = consulta.medico;
        consultaLista.dia = this.convertDate(consulta.dia);
        consultaLista.horario = this.convertTime(consulta.horario);
        consultaLista.data_agendamento = consulta.data_agendamento;
        this.consultas.push(consultaLista);
      }
    });
  }

  deleteConsulta(id=null){
    this.consultaListaService.deleteConsulta(id).subscribe(data => {
      this.getConsultas();
    });    
  }

  convertDate(date = null){
    date = date.split("-")
    return date[2] + "/" + date[1] + "/" + date[0];
  }

  convertTime(time = null){
    return time.slice(0, 5);
  }

}
