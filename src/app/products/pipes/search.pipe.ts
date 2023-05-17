import { Pipe, PipeTransform } from '@angular/core';
import { Product } from '../modules/product';

@Pipe({
  name: 'search'
})
export class SearchPipe implements PipeTransform {

  transform(products: Array<Product>, name: string): Array<Product> {

    const filterProducts = products.filter(product => product.name_product.includes(name));

    return filterProducts;

  }

}
