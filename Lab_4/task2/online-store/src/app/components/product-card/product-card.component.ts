import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-card',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article class="card">
      <a class="imageWrap" [href]="product.link" target="_blank" rel="noopener">
        <img class="mainImage" [src]="selectedImage" [alt]="product.name" />
      </a>

      <div class="thumbs">
        @for (img of product.images; track img) {
          <button
            type="button"
            class="thumb"
            [class.active]="img === selectedImage"
            (click)="select(img)"
            aria-label="Select image"
          >
            <img [src]="img" [alt]="product.name" />
          </button>
        }
      </div>

      <h3 class="title" [title]="product.name">
        {{ product.name }}
      </h3>

      <p class="desc">
        {{ product.description }}
      </p>

      <div class="meta">
        <div class="price">{{ product.price | number:'1.0-0' }} ₸</div>

        <div class="rating" [title]="'Rating: ' + product.rating">
          <span class="stars" aria-label="Rating stars">
            @for (s of stars; track s) {
              <span class="star" [class.filled]="s <= roundedRating">★</span>
            }
          </span>
          <span class="badge">{{ product.rating.toFixed(1) }}</span>
        </div>
      </div>

      <div class="actions">
        <a class="btn primary" [href]="product.link" target="_blank" rel="noopener">
          Open on Kaspi
        </a>

        <button class="btn" type="button" (click)="shareWhatsApp()">
          Share WhatsApp
        </button>

        <button class="btn" type="button" (click)="shareTelegram()">
          Share Telegram
        </button>
      </div>
    </article>
  `,
  styleUrl: './product-card.component.css'
})
export class ProductCardComponent {
  @Input({ required: true }) product!: Product;

  selectedImage = '';
  stars = [1, 2, 3, 4, 5];

  ngOnInit(): void {
    // main image по умолчанию: product.image, если нет — первая из images
    this.selectedImage = this.product.image || this.product.images[0] || '';
  }

  get roundedRating(): number {
    return Math.round(this.product.rating);
  }

  select(img: string): void {
    this.selectedImage = img;
  }

  shareWhatsApp(): void {
    const text = `Check out this product: ${this.product.link}`;
    const url = `https://wa.me/?text=${encodeURIComponent(text)}`;
    window.open(url, '_blank', 'noopener');
  }

  shareTelegram(): void {
    const url = `https://t.me/share/url?url=${encodeURIComponent(this.product.link)}&text=${encodeURIComponent(this.product.name)}`;
    window.open(url, '_blank', 'noopener');
  }
}