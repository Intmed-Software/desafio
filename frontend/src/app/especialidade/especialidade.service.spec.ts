import { TestBed } from '@angular/core/testing';

import { EspecialidadeService } from './especialidade.service';

describe('EspecialidadeService', () => {
  let service: EspecialidadeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EspecialidadeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
