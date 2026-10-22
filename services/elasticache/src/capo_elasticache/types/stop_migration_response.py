"""Generated from Smithy shape ``com.amazonaws.elasticache#StopMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.serverless_cache


class StopMigrationResponse(TypedDict, closed=True):
    serverless_cache: NotRequired[
        "capo_elasticache.types.serverless_cache.ServerlessCache"
    ]
    """<p>Provides the details of the serverless cache for which the data sync stopped.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopMigrationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache" in value:
        import capo_elasticache.types.serverless_cache

        capo_elasticache.types.serverless_cache.serialize_query(
            value["serverless_cache"], pairs, f"{key_prefix}ServerlessCache"
        )


def deserialize_query(el: Element) -> StopMigrationResponse:
    out: StopMigrationResponse = {}  # type: ignore[typeddict-item]
    child_serverless_cache = el.find("ServerlessCache")
    if child_serverless_cache is not None:
        import capo_elasticache.types.serverless_cache

        out["serverless_cache"] = (
            capo_elasticache.types.serverless_cache.deserialize_query(
                child_serverless_cache
            )
        )
    return out
