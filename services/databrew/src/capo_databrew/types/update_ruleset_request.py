"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.rule_list
    import capo_databrew.types.ruleset_description
    import capo_databrew.types.ruleset_name


class UpdateRulesetRequest(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset to be updated.</p>"""
    description: NotRequired[
        "capo_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    rules: "capo_databrew.types.rule_list.RuleList"
    """<p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRulesetRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_databrew.types.rule_list

    out["Rules"] = capo_databrew.types.rule_list.serialize_json(value["rules"])
    return out


def deserialize_json(data: dict) -> UpdateRulesetRequest:
    out: UpdateRulesetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Rules") is not None:
        import capo_databrew.types.rule_list

        out["rules"] = capo_databrew.types.rule_list.deserialize_json(data["Rules"])
    else:
        out["rules"] = []
    return out
