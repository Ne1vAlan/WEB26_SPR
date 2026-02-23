export interface Product {
  id: number;
  name: string;
  description: string;
  price: number; //KZT
  rating: number; //1..5 (может быть 4.7)
  image: string; //main image
  images: string[]; //gallery (min 3)
  link: string; //kaspi.kz URL
}