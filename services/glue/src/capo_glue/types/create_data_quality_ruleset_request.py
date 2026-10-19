"""Generated from Smithy shape ``com.amazonaws.glue#CreateDataQualityRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_ruleset_string
    import capo_glue.types.data_quality_target_table
    import capo_glue.types.description_string
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.tags_map


class CreateDataQualityRulesetRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>A unique name for the data quality ruleset.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the data quality ruleset.</p>"""
    ruleset: "capo_glue.types.data_quality_ruleset_string.DataQualityRulesetString"
    """<p>A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>A list of tags applied to the data quality ruleset.</p>"""
    target_table: NotRequired[
        "capo_glue.types.data_quality_target_table.DataQualityTargetTable"
    ]
    """<p>A target table associated with the data quality ruleset.</p>"""
    data_quality_security_configuration: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>The name of the security configuration created with the data quality encryption option.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataQualityRulesetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Ruleset"] = value["ruleset"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "target_table" in value:
        import capo_glue.types.data_quality_target_table

        out["TargetTable"] = (
            capo_glue.types.data_quality_target_table.serialize_aws_json_1_1(
                value["target_table"]
            )
        )
    if "data_quality_security_configuration" in value:
        out["DataQualitySecurityConfiguration"] = value[
            "data_quality_security_configuration"
        ]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataQualityRulesetRequest:
    out: CreateDataQualityRulesetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Ruleset") is not None:
        out["ruleset"] = data["Ruleset"]
    else:
        out["ruleset"] = ""
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("TargetTable") is not None:
        import capo_glue.types.data_quality_target_table

        out["target_table"] = (
            capo_glue.types.data_quality_target_table.deserialize_aws_json_1_1(
                data["TargetTable"]
            )
        )
    if data.get("DataQualitySecurityConfiguration") is not None:
        out["data_quality_security_configuration"] = data[
            "DataQualitySecurityConfiguration"
        ]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
