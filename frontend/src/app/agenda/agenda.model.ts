import { Time } from "@angular/common";
import { Medico } from "src/app/medico/medico.model";

export class Agenda{
  'id': number;
  'dia': Date;
  'medico': Medico;
  'horarios': Time[];
}