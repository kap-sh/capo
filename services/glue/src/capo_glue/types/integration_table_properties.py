"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationTableProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.source_table_config
    import capo_glue.types.string128
    import capo_glue.types.string512
    import capo_glue.types.target_table_config


class IntegrationTableProperties(TypedDict, closed=True):
    resource_arn: "capo_glue.types.string512.String512"
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""
    table_name: "capo_glue.types.string128.String128"
    """<p>The name of the source table to be replicated.</p>"""
    source_table_config: NotRequired[
        "capo_glue.types.source_table_config.SourceTableConfig"
    ]
    """<p>A structure for the source table configuration.</p>"""
    target_table_config: NotRequired[
        "capo_glue.types.target_table_config.TargetTableConfig"
    ]
    """<p>A structure for the target table configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationTableProperties) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["TableName"] = value["table_name"]
    if "source_table_config" in value:
        import capo_glue.types.source_table_config

        out["SourceTableConfig"] = (
            capo_glue.types.source_table_config.serialize_aws_json_1_1(
                value["source_table_config"]
            )
        )
    if "target_table_config" in value:
        import capo_glue.types.target_table_config

        out["TargetTableConfig"] = (
            capo_glue.types.target_table_config.serialize_aws_json_1_1(
                value["target_table_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationTableProperties:
    out: IntegrationTableProperties = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("SourceTableConfig") is not None:
        import capo_glue.types.source_table_config

        out["source_table_config"] = (
            capo_glue.types.source_table_config.deserialize_aws_json_1_1(
                data["SourceTableConfig"]
            )
        )
    if data.get("TargetTableConfig") is not None:
        import capo_glue.types.target_table_config

        out["target_table_config"] = (
            capo_glue.types.target_table_config.deserialize_aws_json_1_1(
                data["TargetTableConfig"]
            )
        )
    return out
