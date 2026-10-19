"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#LakehouseSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class LakehouseSettings(TypedDict, closed=True):
    arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Lakehouse resource that serves as the target for this endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LakehouseSettings) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LakehouseSettings:
    out: LakehouseSettings = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
