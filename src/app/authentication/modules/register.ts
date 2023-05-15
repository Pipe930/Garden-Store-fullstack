export interface Register {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
}

export interface RegisterResponse {
  id: number;
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
  last_login: string;
  is_active: boolean;
  is_staff: boolean;
}
