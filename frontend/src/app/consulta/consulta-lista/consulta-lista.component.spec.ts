import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsultaListaComponent } from './consulta-lista.component';

describe('ConsultaListaComponent', () => {
  let component: ConsultaListaComponent;
  let fixture: ComponentFixture<ConsultaListaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConsultaListaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConsultaListaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
