"""Generated from Smithy shape ``com.amazonaws.elasticache#MigrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.endpoint
    import capo_elasticache.types.string


class MigrationSummary(TypedDict, closed=True):
    status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The current status of the migration.</p>"""
    migration_endpoint: NotRequired["capo_elasticache.types.endpoint.Endpoint"]
    """<p>The migration endpoint, which is the standard endpoint of the serverless cache. Point your application at this endpoint during the migration. Until cutover, ElastiCache routes requests on this endpoint to your source.</p>"""
    cutover_mode: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cutover configuration for the migration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MigrationSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "migration_endpoint" in value:
        import capo_elasticache.types.endpoint

        capo_elasticache.types.endpoint.serialize_query(
            value["migration_endpoint"], pairs, f"{key_prefix}MigrationEndpoint"
        )
    if "cutover_mode" in value:
        pairs.append((f"{key_prefix}CutoverMode", str(value["cutover_mode"])))


def deserialize_query(el: Element) -> MigrationSummary:
    out: MigrationSummary = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_migration_endpoint = el.find("MigrationEndpoint")
    if child_migration_endpoint is not None:
        import capo_elasticache.types.endpoint

        out["migration_endpoint"] = capo_elasticache.types.endpoint.deserialize_query(
            child_migration_endpoint
        )
    child_cutover_mode = el.find("CutoverMode")
    if child_cutover_mode is not None:
        out["cutover_mode"] = str(child_cutover_mode.text or "")
    return out
