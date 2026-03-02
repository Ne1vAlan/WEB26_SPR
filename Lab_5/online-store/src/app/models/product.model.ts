export interface Product {
  id: number;
  name: string;
  description: string;
  price: number; //KZT
  rating: number; //1..5
  likes: number; //starts 0
  categoryId: number; //link to Category.id
  imageUrl: string;
  kaspiUrl: string;
}