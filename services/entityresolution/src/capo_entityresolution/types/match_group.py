"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.matched_records_list


class MatchGroup(TypedDict, closed=True):
    records: "capo_entityresolution.types.matched_records_list.MatchedRecordsList"
    """<p> The matched records.</p>"""
    match_id: "str"
    """<p> The match ID.</p>"""
    match_rule: "str"
    """<p> The match rule of the match group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchGroup) -> dict:
    out: dict = {}
    import capo_entityresolution.types.matched_records_list

    out["records"] = capo_entityresolution.types.matched_records_list.serialize_json(
        value["records"]
    )
    out["matchId"] = value["match_id"]
    out["matchRule"] = value["match_rule"]
    return out


def deserialize_json(data: dict) -> MatchGroup:
    out: MatchGroup = {}  # type: ignore[typeddict-item]
    if data.get("records") is not None:
        import capo_entityresolution.types.matched_records_list

        out["records"] = (
            capo_entityresolution.types.matched_records_list.deserialize_json(
                data["records"]
            )
        )
    else:
        out["records"] = []
    if data.get("matchId") is not None:
        out["match_id"] = data["matchId"]
    else:
        out["match_id"] = ""
    if data.get("matchRule") is not None:
        out["match_rule"] = data["matchRule"]
    else:
        out["match_rule"] = ""
    return out
