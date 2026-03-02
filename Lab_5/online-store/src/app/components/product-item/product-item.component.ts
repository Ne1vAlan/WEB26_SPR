import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css',
})
export class ProductItemComponent {
  @Input({ required: true }) product!: Product;
  @Output() delete = new EventEmitter<number>();

  like() {
    this.product.likes += 1;
  }

  askDelete() {
    const ok = confirm(`Delete "${this.product.name}"?`);
    if (ok) this.delete.emit(this.product.id);
  }

  shareWhatsapp() {
    const text = encodeURIComponent(`${this.product.name}\n${this.product.kaspiUrl}`);
    window.open(`https://wa.me/?text=${text}`, '_blank');
  }

  shareTelegram() {
    const url = encodeURIComponent(this.product.kaspiUrl);
    const text = encodeURIComponent(this.product.name);
    window.open(`https://t.me/share/url?url=${url}&text=${text}`, '_blank');
  }
}