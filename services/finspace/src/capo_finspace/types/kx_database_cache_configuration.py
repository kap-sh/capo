"""Generated from Smithy shape ``com.amazonaws.finspace#KxDatabaseCacheConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.db_paths
    import capo_finspace.types.kx_cache_storage_type
    import capo_finspace.types.kx_dataview_name


class KxDatabaseCacheConfiguration(TypedDict, closed=True):
    cache_type: "capo_finspace.types.kx_cache_storage_type.KxCacheStorageType"
    """<p>The type of disk cache. This parameter is used to map the database path to cache storage. The valid values are:</p> <ul> <li> <p>CACHE_1000 – This type provides at least 1000 MB/s disk access throughput. </p> </li> </ul>"""
    db_paths: "capo_finspace.types.db_paths.DbPaths"
    """<p>Specifies the portions of database that will be loaded into the cache for access.</p>"""
    dataview_name: NotRequired["capo_finspace.types.kx_dataview_name.KxDataviewName"]
    """<p> The name of the dataview to be used for caching historical data on disk. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxDatabaseCacheConfiguration) -> dict:
    out: dict = {}
    out["cacheType"] = value["cache_type"]
    import capo_finspace.types.db_paths

    out["dbPaths"] = capo_finspace.types.db_paths.serialize_json(value["db_paths"])
    if "dataview_name" in value:
        out["dataviewName"] = value["dataview_name"]
    return out


def deserialize_json(data: dict) -> KxDatabaseCacheConfiguration:
    out: KxDatabaseCacheConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("cacheType") is not None:
        out["cache_type"] = data["cacheType"]
    else:
        out["cache_type"] = ""
    if data.get("dbPaths") is not None:
        import capo_finspace.types.db_paths

        out["db_paths"] = capo_finspace.types.db_paths.deserialize_json(data["dbPaths"])
    else:
        out["db_paths"] = []
    if data.get("dataviewName") is not None:
        out["dataview_name"] = data["dataviewName"]
    return out
