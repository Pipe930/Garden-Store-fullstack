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
}

export interface ResetPassword {
  email: string;
}
