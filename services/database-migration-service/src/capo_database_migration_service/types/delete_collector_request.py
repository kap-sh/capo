"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteCollectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteCollectorRequest(TypedDict, closed=True):
    collector_referenced_id: "capo_database_migration_service.types.string.String"
    """<p>The reference ID of the Fleet Advisor collector to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCollectorRequest) -> dict:
    out: dict = {}
    out["CollectorReferencedId"] = value["collector_referenced_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCollectorRequest:
    out: DeleteCollectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("CollectorReferencedId") is not None:
        out["collector_referenced_id"] = data["CollectorReferencedId"]
    else:
        out["collector_referenced_id"] = ""
    return out
