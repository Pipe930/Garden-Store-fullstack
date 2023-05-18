type offer = {
  id: number,
  name_offer: string,
  discount: number
}

export interface Product {
  id: number;
  name_product: string;
  price: number;
  stock: number;
  image: string;
  slug: string;
  description: string;
  condition: boolean;
  create: string;
  id_category: number;
  id_offer: offer;
}

export interface ResponseProducts {
  count: number;
  next?: string;
  previous?: string;
  results: Array<Product>;
}
