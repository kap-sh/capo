"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseCloneConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.clone_type
    import capo_odb.types.resource_id_or_arn


class DatabaseCloneConfiguration(TypedDict, closed=True):
    source_autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the source Autonomous Database to clone.</p>"""
    clone_type: "capo_odb.types.clone_type.CloneType"
    """<p>The type of clone to create, either a full clone, a metadata clone, or a partial clone.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseCloneConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseId"] = value["source_autonomous_database_id"]
    import capo_odb.types.clone_type

    out["cloneType"] = capo_odb.types.clone_type.serialize_aws_json_1_0(
        value["clone_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatabaseCloneConfiguration:
    out: DatabaseCloneConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceAutonomousDatabaseId") is not None:
        out["source_autonomous_database_id"] = data["sourceAutonomousDatabaseId"]
    else:
        out["source_autonomous_database_id"] = ""
    if data.get("cloneType") is not None:
        import capo_odb.types.clone_type

        out["clone_type"] = capo_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    else:
        import typing

        out["clone_type"] = typing.cast("capo_odb.types.clone_type.CloneType", "")
    return out
