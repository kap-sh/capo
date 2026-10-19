"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTableAutoScalingSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.auto_scaling_specification
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.replica_auto_scaling_specification_list
    import capo_keyspaces.types.table_name


class GetTableAutoScalingSettingsResponse(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace.</p>"""
    table_name: "capo_keyspaces.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    auto_scaling_specification: NotRequired[
        "capo_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
    ]
    """<p>The auto scaling settings of the table.</p>"""
    replica_specifications: NotRequired[
        "capo_keyspaces.types.replica_auto_scaling_specification_list.ReplicaAutoScalingSpecificationList"
    ]
    """<p>The Amazon Web Services Region specific settings of a multi-Region table. Returns the settings for all Regions the table is replicated in.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTableAutoScalingSettingsResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    out["resourceArn"] = value["resource_arn"]
    if "auto_scaling_specification" in value:
        import capo_keyspaces.types.auto_scaling_specification

        out["autoScalingSpecification"] = (
            capo_keyspaces.types.auto_scaling_specification.serialize_aws_json_1_0(
                value["auto_scaling_specification"]
            )
        )
    if "replica_specifications" in value:
        import capo_keyspaces.types.replica_auto_scaling_specification_list

        out["replicaSpecifications"] = (
            capo_keyspaces.types.replica_auto_scaling_specification_list.serialize_aws_json_1_0(
                value["replica_specifications"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTableAutoScalingSettingsResponse:
    out: GetTableAutoScalingSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("autoScalingSpecification") is not None:
        import capo_keyspaces.types.auto_scaling_specification

        out["auto_scaling_specification"] = (
            capo_keyspaces.types.auto_scaling_specification.deserialize_aws_json_1_0(
                data["autoScalingSpecification"]
            )
        )
    if data.get("replicaSpecifications") is not None:
        import capo_keyspaces.types.replica_auto_scaling_specification_list

        out["replica_specifications"] = (
            capo_keyspaces.types.replica_auto_scaling_specification_list.deserialize_aws_json_1_0(
                data["replicaSpecifications"]
            )
        )
    return out
