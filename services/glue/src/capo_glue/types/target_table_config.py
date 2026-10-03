"""Generated from Smithy shape ``com.amazonaws.glue#TargetTableConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_partition_spec_list
    import capo_glue.types.string128
    import capo_glue.types.unnest_spec


class TargetTableConfig(TypedDict, closed=True):
    unnest_spec: NotRequired["capo_glue.types.unnest_spec.UnnestSpec"]
    """<p>Specifies how nested objects are flattened to top-level elements. Valid values are: "TOPLEVEL", "FULL", or "NOUNNEST".</p>"""
    partition_spec: NotRequired[
        "capo_glue.types.integration_partition_spec_list.IntegrationPartitionSpecList"
    ]
    """<p>Determines the file layout on the target.</p>"""
    target_table_name: NotRequired["capo_glue.types.string128.String128"]
    """<p>The optional name of a target table.</p>"""
    integration_arn: NotRequired["capo_glue.types.string128.String128"]
    """<p>The ARN of the integration that owns this target table configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTableConfig) -> dict:
    out: dict = {}
    if "unnest_spec" in value:
        import capo_glue.types.unnest_spec

        out["UnnestSpec"] = capo_glue.types.unnest_spec.serialize_aws_json_1_1(
            value["unnest_spec"]
        )
    if "partition_spec" in value:
        import capo_glue.types.integration_partition_spec_list

        out["PartitionSpec"] = (
            capo_glue.types.integration_partition_spec_list.serialize_aws_json_1_1(
                value["partition_spec"]
            )
        )
    if "target_table_name" in value:
        out["TargetTableName"] = value["target_table_name"]
    if "integration_arn" in value:
        out["IntegrationArn"] = value["integration_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTableConfig:
    out: TargetTableConfig = {}  # type: ignore[typeddict-item]
    if data.get("UnnestSpec") is not None:
        import capo_glue.types.unnest_spec

        out["unnest_spec"] = capo_glue.types.unnest_spec.deserialize_aws_json_1_1(
            data["UnnestSpec"]
        )
    if data.get("PartitionSpec") is not None:
        import capo_glue.types.integration_partition_spec_list

        out["partition_spec"] = (
            capo_glue.types.integration_partition_spec_list.deserialize_aws_json_1_1(
                data["PartitionSpec"]
            )
        )
    if data.get("TargetTableName") is not None:
        out["target_table_name"] = data["TargetTableName"]
    if data.get("IntegrationArn") is not None:
        out["integration_arn"] = data["IntegrationArn"]
    return out
