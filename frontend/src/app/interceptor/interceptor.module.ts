import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { InterceptorService } from './interceptor.service';


@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ],
  providers: [
    InterceptorService,
    {
      provide: HTTP_INTERCEPTORS, 
      useClass: InterceptorService, 
      multi: true,
    },
  ],
})
export class InterceptorModule { }
