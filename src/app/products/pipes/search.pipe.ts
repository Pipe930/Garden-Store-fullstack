import { Pipe, PipeTransform } from '@angular/core';
import { Product } from '../modules/product';

@Pipe({
  name: 'search'
})
export class SearchPipe implements PipeTransform {

  transform(products: Array<Product>, name: string, page:number = 0, id_category:string): Array<Product> {

    if (!products) {
      return [];
    }

    if (!id_category && !name) {
      return products.slice(page, page + 10);
    }

    name = name.toLocaleLowerCase();

    const filterProducts = products.filter((product: Product) => {
      const cumpleFiltroNombre = product.name_product.toLowerCase().includes(name);
      const cumpleFiltroCategoria = product.id_category.toString() === id_category;
      if(!id_category || id_category == ""){
        return cumpleFiltroNombre
      }
      return cumpleFiltroNombre && cumpleFiltroCategoria;
    });

    console.log(filterProducts);

    return filterProducts.slice(page, page + 10);

  }

}
