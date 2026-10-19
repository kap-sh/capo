"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DisallowIntermediateTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.membership_identifier


class DisallowIntermediateTableInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table to disallow.</p>"""
    intermediate_table_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the intermediate table to disallow.</p>"""
    include_descendants: NotRequired["bool"]
    """<p>Specifies whether to cascade the disallow action to descendant intermediate tables. Default is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisallowIntermediateTableInput) -> dict:
    out: dict = {}
    out["intermediateTableName"] = value["intermediate_table_name"]
    if "include_descendants" in value:
        out["includeDescendants"] = value["include_descendants"]
    return out


def deserialize_json(data: dict) -> DisallowIntermediateTableInput:
    out: DisallowIntermediateTableInput = {}  # type: ignore[typeddict-item]
    if data.get("intermediateTableName") is not None:
        out["intermediate_table_name"] = data["intermediateTableName"]
    else:
        raise DeserializationError(
            "DisallowIntermediateTableInput.intermediate_table_name required"
        )
    if data.get("includeDescendants") is not None:
        out["include_descendants"] = data["includeDescendants"]
    return out
