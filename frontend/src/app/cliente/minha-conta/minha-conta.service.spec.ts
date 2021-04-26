import { TestBed } from '@angular/core/testing';

import { MinhaContaService } from './minha-conta.service';

describe('MinhaContaService', () => {
  let service: MinhaContaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MinhaContaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
