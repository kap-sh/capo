"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteInstanceProfileMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteInstanceProfileMessage(TypedDict, closed=True):
    instance_profile_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier of the instance profile to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInstanceProfileMessage) -> dict:
    out: dict = {}
    out["InstanceProfileIdentifier"] = value["instance_profile_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInstanceProfileMessage:
    out: DeleteInstanceProfileMessage = {}  # type: ignore[typeddict-item]
    if data.get("InstanceProfileIdentifier") is not None:
        out["instance_profile_identifier"] = data["InstanceProfileIdentifier"]
    else:
        out["instance_profile_identifier"] = ""
    return out
