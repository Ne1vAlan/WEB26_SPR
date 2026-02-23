import { Component } from '@angular/core';
import { ProductCardComponent } from '../product-card/product-card.component';
import { PRODUCTS } from '../../data/products';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [ProductCardComponent],
  template: `
    <div class="page">
      <header class="topbar">
        <div class="brand">Online Store</div>
        <div class="hint">Kaspi-style catalog</div>
      </header>

      <main class="grid">
        @for (p of products; track p.id) {
          <app-product-card [product]="p"></app-product-card>
        }
      </main>
    </div>
  `,
  styleUrl: './product-list.component.css'
})
export class ProductListComponent {
  products: Product[] = PRODUCTS;
}