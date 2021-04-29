import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { InterceptorService } from 'src/app/interceptor/interceptor.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'medicar-app';
  constructor(
    private router: Router,
    private interceptorService: InterceptorService
  ) { }
  ngOnInit(): void {
    if(!this.interceptorService.getAuthToken())
    {
      this.router.navigate(['/login']);
    }
  }
}
