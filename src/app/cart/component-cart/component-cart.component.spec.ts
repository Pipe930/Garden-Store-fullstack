import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentCartComponent } from './component-cart.component';

describe('ComponentCartComponent', () => {
  let component: ComponentCartComponent;
  let fixture: ComponentFixture<ComponentCartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComponentCartComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponentCartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
