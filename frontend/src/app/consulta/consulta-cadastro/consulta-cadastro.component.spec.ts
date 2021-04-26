import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsultaCadastroComponent } from './consulta-cadastro.component';

describe('ConsultaCadastroComponent', () => {
  let component: ConsultaCadastroComponent;
  let fixture: ComponentFixture<ConsultaCadastroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConsultaCadastroComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConsultaCadastroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
