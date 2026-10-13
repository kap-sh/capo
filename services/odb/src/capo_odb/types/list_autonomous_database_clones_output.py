"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseClonesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_list


class ListAutonomousDatabaseClonesOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_database_clones: (
        "capo_odb.types.autonomous_database_list.AutonomousDatabaseList"
    )
    """<p>The list of Autonomous Database clones along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseClonesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.autonomous_database_list

    out["autonomousDatabaseClones"] = (
        capo_odb.types.autonomous_database_list.serialize_aws_json_1_0(
            value["autonomous_database_clones"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseClonesOutput:
    out: ListAutonomousDatabaseClonesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autonomousDatabaseClones") is not None:
        import capo_odb.types.autonomous_database_list

        out["autonomous_database_clones"] = (
            capo_odb.types.autonomous_database_list.deserialize_aws_json_1_0(
                data["autonomousDatabaseClones"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutonomousDatabaseClonesOutput.autonomous_database_clones required"
        )
    return out


def redact_sensitive(value: ListAutonomousDatabaseClonesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "autonomous_database_clones" in value:
        import capo_odb.types.autonomous_database_list

        out["autonomous_database_clones"] = (
            capo_odb.types.autonomous_database_list.redact_sensitive(
                value["autonomous_database_clones"]
            )
        )
    return out
