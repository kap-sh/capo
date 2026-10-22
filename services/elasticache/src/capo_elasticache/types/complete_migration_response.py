"""Generated from Smithy shape ``com.amazonaws.elasticache#CompleteMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.replication_group
    import capo_elasticache.types.serverless_cache


class CompleteMigrationResponse(TypedDict, closed=True):
    replication_group: NotRequired[
        "capo_elasticache.types.replication_group.ReplicationGroup"
    ]
    serverless_cache: NotRequired[
        "capo_elasticache.types.serverless_cache.ServerlessCache"
    ]
    """<p>Provides the details of the serverless cache for which the migration completed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CompleteMigrationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "replication_group" in value:
        import capo_elasticache.types.replication_group

        capo_elasticache.types.replication_group.serialize_query(
            value["replication_group"], pairs, f"{key_prefix}ReplicationGroup"
        )
    if "serverless_cache" in value:
        import capo_elasticache.types.serverless_cache

        capo_elasticache.types.serverless_cache.serialize_query(
            value["serverless_cache"], pairs, f"{key_prefix}ServerlessCache"
        )


def deserialize_query(el: Element) -> CompleteMigrationResponse:
    out: CompleteMigrationResponse = {}  # type: ignore[typeddict-item]
    child_replication_group = el.find("ReplicationGroup")
    if child_replication_group is not None:
        import capo_elasticache.types.replication_group

        out["replication_group"] = (
            capo_elasticache.types.replication_group.deserialize_query(
                child_replication_group
            )
        )
    child_serverless_cache = el.find("ServerlessCache")
    if child_serverless_cache is not None:
        import capo_elasticache.types.serverless_cache

        out["serverless_cache"] = (
            capo_elasticache.types.serverless_cache.deserialize_query(
                child_serverless_cache
            )
        )
    return out
