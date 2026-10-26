"""Generated from Smithy shape ``com.amazonaws.xray#UpdateIndexingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.indexing_rule_value_update
    import capo_xray.types.string


class UpdateIndexingRuleRequest(TypedDict, closed=True):
    name: "capo_xray.types.string.String"
    """<p> Name of the indexing rule to be updated. </p>"""
    rule: "capo_xray.types.indexing_rule_value_update.IndexingRuleValueUpdate"
    """<p> Rule configuration to be updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexingRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_xray.types.indexing_rule_value_update

    out["Rule"] = capo_xray.types.indexing_rule_value_update.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateIndexingRuleRequest:
    out: UpdateIndexingRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Rule") is not None:
        import capo_xray.types.indexing_rule_value_update

        out["rule"] = capo_xray.types.indexing_rule_value_update.deserialize_json(
            data["Rule"]
        )
    else:
        out["rule"] = {"$unknown": {"name": ""}}
    return out
