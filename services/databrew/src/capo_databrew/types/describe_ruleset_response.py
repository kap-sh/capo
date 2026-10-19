"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.created_by
    import capo_databrew.types.date
    import capo_databrew.types.last_modified_by
    import capo_databrew.types.rule_list
    import capo_databrew.types.ruleset_description
    import capo_databrew.types.ruleset_name
    import capo_databrew.types.tag_map


class DescribeRulesetResponse(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset.</p>"""
    description: NotRequired[
        "capo_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    target_arn: NotRequired["capo_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.</p>"""
    rules: NotRequired["capo_databrew.types.rule_list.RuleList"]
    """<p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>"""
    create_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time that the ruleset was created.</p>"""
    created_by: NotRequired["capo_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the ruleset.</p>"""
    last_modified_by: NotRequired["capo_databrew.types.last_modified_by.LastModifiedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the ruleset.</p>"""
    last_modified_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The modification date and time of the ruleset.</p>"""
    resource_arn: NotRequired["capo_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the ruleset.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRulesetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "rules" in value:
        import capo_databrew.types.rule_list

        out["Rules"] = capo_databrew.types.rule_list.serialize_json(value["rules"])
    if "create_date" in value:
        import capo_databrew.types.date

        out["CreateDate"] = capo_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import capo_databrew.types.date

        out["LastModifiedDate"] = capo_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeRulesetResponse:
    out: DescribeRulesetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("Rules") is not None:
        import capo_databrew.types.rule_list

        out["rules"] = capo_databrew.types.rule_list.deserialize_json(data["Rules"])
    if data.get("CreateDate") is not None:
        import capo_databrew.types.date

        out["create_date"] = capo_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedDate") is not None:
        import capo_databrew.types.date

        out["last_modified_date"] = capo_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
