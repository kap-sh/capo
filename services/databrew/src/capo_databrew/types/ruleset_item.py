"""Generated from Smithy shape ``com.amazonaws.databrew#RulesetItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.account_id
    import capo_databrew.types.arn
    import capo_databrew.types.created_by
    import capo_databrew.types.date
    import capo_databrew.types.last_modified_by
    import capo_databrew.types.rule_count
    import capo_databrew.types.ruleset_description
    import capo_databrew.types.ruleset_name
    import capo_databrew.types.tag_map


class RulesetItem(TypedDict, closed=True):
    account_id: NotRequired["capo_databrew.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the ruleset.</p>"""
    created_by: NotRequired["capo_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the ruleset.</p>"""
    create_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time that the ruleset was created.</p>"""
    description: NotRequired[
        "capo_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    last_modified_by: NotRequired["capo_databrew.types.last_modified_by.LastModifiedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the ruleset.</p>"""
    last_modified_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The modification date and time of the ruleset.</p>"""
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset.</p>"""
    resource_arn: NotRequired["capo_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the ruleset.</p>"""
    rule_count: "capo_databrew.types.rule_count.RuleCount"
    """<p>The number of rules that are defined in the ruleset.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the ruleset.</p>"""
    target_arn: "capo_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RulesetItem) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import capo_databrew.types.date

        out["CreateDate"] = capo_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import capo_databrew.types.date

        out["LastModifiedDate"] = capo_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    out["Name"] = value["name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    out["RuleCount"] = value.get("rule_count", 0)
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    out["TargetArn"] = value["target_arn"]
    return out


def deserialize_json(data: dict) -> RulesetItem:
    out: RulesetItem = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("CreateDate") is not None:
        import capo_databrew.types.date

        out["create_date"] = capo_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedDate") is not None:
        import capo_databrew.types.date

        out["last_modified_date"] = capo_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("RuleCount") is not None:
        out["rule_count"] = data["RuleCount"]
    else:
        out["rule_count"] = 0
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    else:
        out["target_arn"] = ""
    return out
