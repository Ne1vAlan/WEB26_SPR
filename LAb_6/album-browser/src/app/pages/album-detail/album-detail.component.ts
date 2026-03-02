import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { Observable, map, switchMap, catchError, of, shareReplay, tap } from 'rxjs';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album.model';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css',
})
export class AlbumDetailComponent {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private albumService = inject(AlbumService);

  error = '';
  title = '';

  albumId$: Observable<number> = this.route.paramMap.pipe(
    map((pm) => Number(pm.get('id')))
  );

  album$: Observable<Album | null> = this.albumId$.pipe(
    switchMap((id) =>
      this.albumService.getAlbum(id).pipe(
        tap((album) => {
          this.title = album.title;
        }),
        catchError((e) => {
          console.error(e);
          this.error = 'Failed to load album';
          return of(null);
        })
      )
    ),
    shareReplay(1)
  );

  back(): void {
    this.router.navigate(['/albums']);
  }

  save(album: Album): void {
    const updated: Album = { ...album, title: this.title };
    this.albumService.updateAlbum(updated).subscribe({
      next: () => alert('Saved!'),
      error: (e) => {
        console.error(e);
        alert('Save failed');
      },
    });
  }
}