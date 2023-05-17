import { TestBed } from '@angular/core/testing';

import { SesionRequiredGuard } from './sesion-required.guard';

describe('SesionRequiredGuard', () => {
  let guard: SesionRequiredGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(SesionRequiredGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
