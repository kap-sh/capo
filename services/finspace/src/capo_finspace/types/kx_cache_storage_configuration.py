"""Generated from Smithy shape ``com.amazonaws.finspace#KxCacheStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_cache_storage_size
    import capo_finspace.types.kx_cache_storage_type


class KxCacheStorageConfiguration(TypedDict, closed=True):
    type: "capo_finspace.types.kx_cache_storage_type.KxCacheStorageType"
    """<p>The type of cache storage. The valid values are: </p> <ul> <li> <p>CACHE_1000 – This type provides at least 1000 MB/s disk access throughput. </p> </li> <li> <p>CACHE_250 – This type provides at least 250 MB/s disk access throughput. </p> </li> <li> <p>CACHE_12 – This type provides at least 12 MB/s disk access throughput. </p> </li> </ul> <p>For cache type <code>CACHE_1000</code> and <code>CACHE_250</code> you can select cache size as 1200 GB or increments of 2400 GB. For cache type <code>CACHE_12</code> you can select the cache size in increments of 6000 GB.</p>"""
    size: "capo_finspace.types.kx_cache_storage_size.KxCacheStorageSize"
    """<p>The size of cache in Gigabytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxCacheStorageConfiguration) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["size"] = value["size"]
    return out


def deserialize_json(data: dict) -> KxCacheStorageConfiguration:
    out: KxCacheStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("size") is not None:
        out["size"] = data["size"]
    else:
        out["size"] = 0
    return out
