"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_version_list


class ListAutonomousDatabaseVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_database_versions: (
        "capo_odb.types.autonomous_database_version_list.AutonomousDatabaseVersionList"
    )
    """<p>The list of available Autonomous Database software versions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.autonomous_database_version_list

    out["autonomousDatabaseVersions"] = (
        capo_odb.types.autonomous_database_version_list.serialize_aws_json_1_0(
            value["autonomous_database_versions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseVersionsOutput:
    out: ListAutonomousDatabaseVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autonomousDatabaseVersions") is not None:
        import capo_odb.types.autonomous_database_version_list

        out["autonomous_database_versions"] = (
            capo_odb.types.autonomous_database_version_list.deserialize_aws_json_1_0(
                data["autonomousDatabaseVersions"]
            )
        )
    else:
        out["autonomous_database_versions"] = []
    return out
