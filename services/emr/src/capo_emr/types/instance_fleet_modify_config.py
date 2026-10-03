"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetModifyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_fleet_id
    import capo_emr.types.instance_fleet_resizing_specifications
    import capo_emr.types.instance_type_config_list
    import capo_emr.types.whole_number
    import capo_emr.types.xml_string_max_len256


class InstanceFleetModifyConfig(TypedDict, closed=True):
    instance_fleet_id: NotRequired["capo_emr.types.instance_fleet_id.InstanceFleetId"]
    """<p>A unique identifier for the instance fleet.</p>"""
    target_on_demand_capacity: NotRequired["capo_emr.types.whole_number.WholeNumber"]
    """<p>The target capacity of On-Demand units for the instance fleet. For more information see <a>InstanceFleetConfig$TargetOnDemandCapacity</a>.</p>"""
    target_spot_capacity: NotRequired["capo_emr.types.whole_number.WholeNumber"]
    """<p>The target capacity of Spot units for the instance fleet. For more information, see <a>InstanceFleetConfig$TargetSpotCapacity</a>.</p>"""
    resize_specifications: NotRequired[
        "capo_emr.types.instance_fleet_resizing_specifications.InstanceFleetResizingSpecifications"
    ]
    """<p>The resize specification for the instance fleet.</p>"""
    instance_type_configs: NotRequired[
        "capo_emr.types.instance_type_config_list.InstanceTypeConfigList"
    ]
    """<p>An array of InstanceTypeConfig objects that specify how Amazon EMR provisions Amazon EC2 instances when it fulfills On-Demand and Spot capacities. For more information, see <a href="https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceTypeConfig.html">InstanceTypeConfig</a>.</p>"""
    context: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Reserved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetModifyConfig) -> dict:
    out: dict = {}
    if "instance_fleet_id" in value:
        out["InstanceFleetId"] = value["instance_fleet_id"]
    if "target_on_demand_capacity" in value:
        out["TargetOnDemandCapacity"] = value["target_on_demand_capacity"]
    if "target_spot_capacity" in value:
        out["TargetSpotCapacity"] = value["target_spot_capacity"]
    if "resize_specifications" in value:
        import capo_emr.types.instance_fleet_resizing_specifications

        out["ResizeSpecifications"] = (
            capo_emr.types.instance_fleet_resizing_specifications.serialize_aws_json_1_1(
                value["resize_specifications"]
            )
        )
    if "instance_type_configs" in value:
        import capo_emr.types.instance_type_config_list

        out["InstanceTypeConfigs"] = (
            capo_emr.types.instance_type_config_list.serialize_aws_json_1_1(
                value["instance_type_configs"]
            )
        )
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleetModifyConfig:
    out: InstanceFleetModifyConfig = {}  # type: ignore[typeddict-item]
    if data.get("InstanceFleetId") is not None:
        out["instance_fleet_id"] = data["InstanceFleetId"]
    if data.get("TargetOnDemandCapacity") is not None:
        out["target_on_demand_capacity"] = data["TargetOnDemandCapacity"]
    if data.get("TargetSpotCapacity") is not None:
        out["target_spot_capacity"] = data["TargetSpotCapacity"]
    if data.get("ResizeSpecifications") is not None:
        import capo_emr.types.instance_fleet_resizing_specifications

        out["resize_specifications"] = (
            capo_emr.types.instance_fleet_resizing_specifications.deserialize_aws_json_1_1(
                data["ResizeSpecifications"]
            )
        )
    if data.get("InstanceTypeConfigs") is not None:
        import capo_emr.types.instance_type_config_list

        out["instance_type_configs"] = (
            capo_emr.types.instance_type_config_list.deserialize_aws_json_1_1(
                data["InstanceTypeConfigs"]
            )
        )
    if data.get("Context") is not None:
        out["context"] = data["Context"]
    return out
