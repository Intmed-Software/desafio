import { TestBed } from '@angular/core/testing';

import { ConsultaListaService } from './consulta-lista.service';

describe('ConsultaListaService', () => {
  let service: ConsultaListaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ConsultaListaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
