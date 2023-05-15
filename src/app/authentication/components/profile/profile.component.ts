import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../../services/authentication.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  constructor(
    private service: AuthenticationService
  ) { }

  public logout():void {
    let token = sessionStorage.getItem('token')!;
    this.service.logout(token);
  }

  ngOnInit(): void {

  }

}
