"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.rule_list
    import capo_databrew.types.ruleset_description
    import capo_databrew.types.ruleset_name
    import capo_databrew.types.tag_map


class CreateRulesetRequest(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    description: NotRequired[
        "capo_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    target_arn: "capo_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.</p>"""
    rules: "capo_databrew.types.rule_list.RuleList"
    """<p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to the ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRulesetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["TargetArn"] = value["target_arn"]
    import capo_databrew.types.rule_list

    out["Rules"] = capo_databrew.types.rule_list.serialize_json(value["rules"])
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRulesetRequest:
    out: CreateRulesetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    else:
        out["target_arn"] = ""
    if data.get("Rules") is not None:
        import capo_databrew.types.rule_list

        out["rules"] = capo_databrew.types.rule_list.deserialize_json(data["Rules"])
    else:
        out["rules"] = []
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
