import { Component, OnInit } from '@angular/core';
import { LoginService } from './login.service';
import { Login } from './login.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  login = new Login();
  passwordVisibility = false;

  constructor(
    private router: Router,
    private loginService :LoginService,
  ) { }

  ngOnInit(): void {
  }

  clearAccess() {
    console.log("Limpando os Storages");
    localStorage.clear();
    sessionStorage.clear();
  }

  userLogin() {
    this.loginService.userLogin(this.login).subscribe(data => {
      this.clearAccess();
      if (this.login.rememberme) {
        localStorage.setItem("medicarToken", data['token']);
      }
      else {
        sessionStorage.setItem("medicarToken", data['token']);
      }
      this.router.navigate(['/']);
    })
  }

  setPasswordVisibility() {
    this.passwordVisibility = !this.passwordVisibility;    
  }

}
