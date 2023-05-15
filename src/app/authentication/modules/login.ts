export interface Login {
  username: string;
  password: string;
}

export interface LoginResponse {
  token: string;
  username: string;
  user_id: string;
  active: boolean;
  staff: boolean;
  idCart: number;
}

export interface ResetPassword {
  email: string;
}
