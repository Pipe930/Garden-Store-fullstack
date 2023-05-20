type product = {
  id: number;
  name_product: string;
  price: number;
}

type items = {
  price: number;
  product: product;
  quantity: number;
}

export interface Cart {
  id: number;
  items: Array<items>;
  total: number;
  id_user: number;
  total_quantity: number;
  total_products: number;
}
