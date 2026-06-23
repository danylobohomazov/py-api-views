from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet
)

movie_list = MovieViewSet.as_view(actions={"get": "list", "post": "create"})
movie_detail = MovieViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        )

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path(
        "cinema_halls/",
        CinemaHallList.as_view(actions={"get": "list", "post": "create"}),
        name="cinema_hall_list",
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallDetail.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="cinema_hall_detail"
    ),
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:pk>/", movie_detail, name="movie_detail"),
]

app_name = "cinema"
