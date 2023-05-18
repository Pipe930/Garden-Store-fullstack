import { Pipe, PipeTransform } from '@angular/core';
import { Product } from '../modules/product';

@Pipe({
  name: 'search'
})
export class SearchPipe implements PipeTransform {

  transform(products: Array<Product>, name: string, page:number = 0): Array<Product> {

    if(name.length == 0) return products.slice(page, page + 10);

    const filterProducts = products.filter(product => product.name_product.includes(name));

    return filterProducts.slice(page, page + 10);

  }

}
