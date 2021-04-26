import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-medico',
  templateUrl: './medico.component.html',
  styleUrls: ['./medico.component.css']
})
export class MedicoComponent implements OnInit {

  apiUrl = 'http://127.0.0.1:8000/medicos/?format=json';

  medicos = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.getMedicos();
  }

  getMedicos(){
    let result = [];
    this.http.get(this.apiUrl).subscribe(data => {
      for (let index = 0; index < data['length']; index++) {
        result.push(data[index]);
      }
    });
    this.medicos = result;
  }

}
