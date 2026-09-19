import pytest
from capo_s3.transfer import MAX_PARTS, MIN_PART_SIZE, TransferConfig
from capo_s3.transfer._config import split_upload_args

MIB = 1024 * 1024
GIB = 1024**3


def test_threshold_routing():
    config = TransferConfig(multipart_threshold=25 * MIB)
    assert not config.is_multipart(25 * MIB - 1)
    assert config.is_multipart(25 * MIB)


def test_chunksize_below_floor_rejected():
    with pytest.raises(ValueError, match="multipart_chunksize"):
        TransferConfig(multipart_chunksize=MIN_PART_SIZE - 1)


def test_chunksize_grows_to_fit_the_part_limit():
    """8 MiB parts would need ~12800 parts for 100 GB; the chunk grows instead."""
    config = TransferConfig(multipart_chunksize=8 * MIB)
    size = 100 * GIB
    chunk = config.resolved_chunksize(size)
    assert chunk > 8 * MIB
    assert -(-size // chunk) <= MAX_PARTS


def test_chunksize_left_alone_when_it_already_fits():
    config = TransferConfig(multipart_chunksize=8 * MIB)
    assert config.resolved_chunksize(100 * MIB) == 8 * MIB


def test_part_ranges_cover_the_object_exactly():
    config = TransferConfig(multipart_chunksize=5 * MIB)
    size = 12 * MIB
    ranges = config.part_ranges(size)
    assert ranges == [(0, 5 * MIB), (5 * MIB, 5 * MIB), (10 * MIB, 2 * MIB)]
    assert sum(length for _, length in ranges) == size


def test_split_upload_args_routes_object_metadata_to_create_only():
    create, part = split_upload_args(
        {"content_type": "video/mp4", "sse_customer_algorithm": "AES256"}
    )
    assert create == {"content_type": "video/mp4"}
    assert part == {"sse_customer_algorithm": "AES256"}


def test_split_upload_args_handles_none():
    assert split_upload_args(None) == ({}, {})
