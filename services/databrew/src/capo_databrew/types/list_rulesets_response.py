"""Generated from Smithy shape ``com.amazonaws.databrew#ListRulesetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.next_token
    import capo_databrew.types.ruleset_item_list


class ListRulesetsResponse(TypedDict, closed=True):
    rulesets: "capo_databrew.types.ruleset_item_list.RulesetItemList"
    """<p>A list of RulesetItem. RulesetItem contains meta data of a ruleset.</p>"""
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesetsResponse) -> dict:
    out: dict = {}
    import capo_databrew.types.ruleset_item_list

    out["Rulesets"] = capo_databrew.types.ruleset_item_list.serialize_json(
        value["rulesets"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRulesetsResponse:
    out: ListRulesetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Rulesets") is not None:
        import capo_databrew.types.ruleset_item_list

        out["rulesets"] = capo_databrew.types.ruleset_item_list.deserialize_json(
            data["Rulesets"]
        )
    else:
        out["rulesets"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
