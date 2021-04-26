import { TestBed } from '@angular/core/testing';

import { ConsultaCadastroService } from './consulta-cadastro.service';

describe('ConsultaCadastroService', () => {
  let service: ConsultaCadastroService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ConsultaCadastroService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
