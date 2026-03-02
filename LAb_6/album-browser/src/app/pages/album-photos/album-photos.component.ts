import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable, map, switchMap, catchError, of, shareReplay } from 'rxjs';

import { AlbumService } from '../../services/album.service';
import { Photo } from '../../models/photo.model';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css',
})
export class AlbumPhotosComponent {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private albumService = inject(AlbumService);
  error = '';
  albumId$: Observable<number> = this.route.paramMap.pipe(
    map((pm) => Number(pm.get('id')))
  );

  photos$: Observable<Photo[]> = this.albumId$.pipe(
    switchMap((id) =>
      this.albumService.getAlbumPhotos(id).pipe(
        catchError((e) => {
          console.error(e);
          this.error = 'Failed to load photos';
          return of([] as Photo[]);
        })
      )
    ),
    shareReplay(1)
  );

  back(id: number): void {
    this.router.navigate(['/albums', id]);
  }
}