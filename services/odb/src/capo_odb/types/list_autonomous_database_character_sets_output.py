"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseCharacterSetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_character_set_list


class ListAutonomousDatabaseCharacterSetsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_database_character_sets: "capo_odb.types.autonomous_database_character_set_list.AutonomousDatabaseCharacterSetList"
    """<p>The list of available Autonomous Database character sets.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseCharacterSetsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.autonomous_database_character_set_list

    out["autonomousDatabaseCharacterSets"] = (
        capo_odb.types.autonomous_database_character_set_list.serialize_aws_json_1_0(
            value["autonomous_database_character_sets"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseCharacterSetsOutput:
    out: ListAutonomousDatabaseCharacterSetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("autonomousDatabaseCharacterSets") is not None:
        import capo_odb.types.autonomous_database_character_set_list

        out["autonomous_database_character_sets"] = (
            capo_odb.types.autonomous_database_character_set_list.deserialize_aws_json_1_0(
                data["autonomousDatabaseCharacterSets"]
            )
        )
    else:
        out["autonomous_database_character_sets"] = []
    return out
