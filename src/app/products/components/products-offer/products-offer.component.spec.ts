import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductsOfferComponent } from './products-offer.component';

describe('ProductsOfferComponent', () => {
  let component: ProductsOfferComponent;
  let fixture: ComponentFixture<ProductsOfferComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProductsOfferComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductsOfferComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
