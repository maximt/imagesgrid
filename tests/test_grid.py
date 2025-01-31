import pytest
from unittest.mock import patch

from ..libs.grid import get_grid_size, get_tile_size


@pytest.mark.parametrize("files_count, expected", [
    (1, (1, 1)),
    (2, (2, 1)),
    (3, (2, 2)),
    (4, (2, 2)),
    (5, (3, 2)),
    (6, (3, 2)),
    (7, (3, 3)),
    (8, (3, 3)),
    (9, (3, 3)),
    (10, (4, 3)),
    (15, (4, 4)),
    (16, (4, 4)),
])
def test_get_grid_size(files_count, expected):
    assert get_grid_size(files_count) == expected


def test_get_grid_size_capacity():
    for files_count in range(1, 1000):
        x, y = get_grid_size(files_count)
        grid_count = x * y
        assert grid_count >= files_count


def test_get_tile_size():
    def mock_get_image_size(file_path: str) -> tuple[int, int]:
        sizes = {
            'image1.png': (500, 500),
            'image2.png': (500, 800),
            'image3.png': (800, 500),
        }
        return sizes.get(file_path, (0, 0))

    files = ['image1.png', 'image2.png', 'image3.png']
    expected_tile_size = (800, 800)

    with patch('imagesgrid.libs.grid.get_image_size', side_effect=mock_get_image_size):
        tile_size = get_tile_size(files)

    assert tile_size == expected_tile_size
