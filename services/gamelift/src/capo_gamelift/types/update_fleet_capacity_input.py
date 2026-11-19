"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateFleetCapacityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.managed_capacity_configuration
    import capo_gamelift.types.whole_number


class UpdateFleetCapacityInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to update capacity settings for. You can use either the fleet ID or ARN value.</p>"""
    desired_instances: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.</p>"""
    min_size: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0. This parameter cannot be set when using a ManagedCapacityConfiguration where ZeroCapacityStrategy has a value of SCALE_TO_AND_FROM_ZERO.</p>"""
    max_size: NotRequired["capo_gamelift.types.whole_number.WholeNumber"]
    """<p>The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The name of a remote location to update fleet capacity settings for, in the form of an Amazon Web Services Region code such as <code>us-west-2</code>.</p>"""
    managed_capacity_configuration: NotRequired[
        "capo_gamelift.types.managed_capacity_configuration.ManagedCapacityConfiguration"
    ]
    """<p>Configuration for Amazon GameLift Servers-managed capacity scaling options.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFleetCapacityInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "desired_instances" in value:
        out["DesiredInstances"] = value["desired_instances"]
    if "min_size" in value:
        out["MinSize"] = value["min_size"]
    if "max_size" in value:
        out["MaxSize"] = value["max_size"]
    if "location" in value:
        out["Location"] = value["location"]
    if "managed_capacity_configuration" in value:
        import capo_gamelift.types.managed_capacity_configuration

        out["ManagedCapacityConfiguration"] = (
            capo_gamelift.types.managed_capacity_configuration.serialize_aws_json_1_1(
                value["managed_capacity_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFleetCapacityInput:
    out: UpdateFleetCapacityInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("DesiredInstances") is not None:
        out["desired_instances"] = data["DesiredInstances"]
    if data.get("MinSize") is not None:
        out["min_size"] = data["MinSize"]
    if data.get("MaxSize") is not None:
        out["max_size"] = data["MaxSize"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("ManagedCapacityConfiguration") is not None:
        import capo_gamelift.types.managed_capacity_configuration

        out["managed_capacity_configuration"] = (
            capo_gamelift.types.managed_capacity_configuration.deserialize_aws_json_1_1(
                data["ManagedCapacityConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateFleetCapacityInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "desired_instances" in value:
        out["DesiredInstances"] = value["desired_instances"]
    if "min_size" in value:
        out["MinSize"] = value["min_size"]
    if "max_size" in value:
        out["MaxSize"] = value["max_size"]
    if "location" in value:
        out["Location"] = value["location"]
    if "managed_capacity_configuration" in value:
        import capo_gamelift.types.managed_capacity_configuration

        out["ManagedCapacityConfiguration"] = (
            capo_gamelift.types.managed_capacity_configuration.serialize_cbor(
                value["managed_capacity_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateFleetCapacityInput:
    out: UpdateFleetCapacityInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("DesiredInstances") is not None:
        out["desired_instances"] = data["DesiredInstances"]
    if data.get("MinSize") is not None:
        out["min_size"] = data["MinSize"]
    if data.get("MaxSize") is not None:
        out["max_size"] = data["MaxSize"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("ManagedCapacityConfiguration") is not None:
        import capo_gamelift.types.managed_capacity_configuration

        out["managed_capacity_configuration"] = (
            capo_gamelift.types.managed_capacity_configuration.deserialize_cbor(
                data["ManagedCapacityConfiguration"]
            )
        )
    return out
