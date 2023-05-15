import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  public isMenuOpen: boolean = false;
  public username: string = '';
  public icon: boolean = false;

  constructor(){
    if(sessionStorage.getItem('user')){
      let user = JSON.parse(sessionStorage.getItem('user')!);
      this.username = user.username;
    }
  }

  public toggleMenu():void {
    this.isMenuOpen = !this.isMenuOpen;
  }

  public linkMenu():void {
    this.isMenuOpen = !this.isMenuOpen;
  }

  public obtenerToken():boolean{
    let token = sessionStorage.getItem('token');

    if(token){
      return true;
    } else {
      return false;
    }
  }

  ngOnInit(): void {

    setInterval(() => {
      let screenWidth = window.innerWidth;
      if(screenWidth >= 920){
        this.icon = true;
      } else{
        this.icon = false;
      }
    }, 10);
  }
}
