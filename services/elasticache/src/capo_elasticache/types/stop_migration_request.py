"""Generated from Smithy shape ``com.amazonaws.elasticache#StopMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class StopMigrationRequest(TypedDict, closed=True):
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the serverless cache for which to stop the data sync.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopMigrationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{key_prefix}ServerlessCacheName", str(value["serverless_cache_name"]))
        )


def deserialize_query(el: Element) -> StopMigrationRequest:
    out: StopMigrationRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    return out
