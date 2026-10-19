"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabasesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_list


class ListAutonomousDatabasesOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_databases: (
        "capo_odb.types.autonomous_database_list.AutonomousDatabaseList"
    )
    """<p>The list of Autonomous Databases along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabasesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.autonomous_database_list

    out["autonomousDatabases"] = (
        capo_odb.types.autonomous_database_list.serialize_aws_json_1_0(
            value["autonomous_databases"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabasesOutput:
    out: ListAutonomousDatabasesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autonomousDatabases") is not None:
        import capo_odb.types.autonomous_database_list

        out["autonomous_databases"] = (
            capo_odb.types.autonomous_database_list.deserialize_aws_json_1_0(
                data["autonomousDatabases"]
            )
        )
    else:
        out["autonomous_databases"] = []
    return out


def redact_sensitive(value: ListAutonomousDatabasesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "autonomous_databases" in value:
        import capo_odb.types.autonomous_database_list

        out["autonomous_databases"] = (
            capo_odb.types.autonomous_database_list.redact_sensitive(
                value["autonomous_databases"]
            )
        )
    return out
