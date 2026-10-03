"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.fleet_excess_capacity_termination_policy
    import capo_ec2.types.fleet_launch_template_config_list_request
    import capo_ec2.types.fleet_type
    import capo_ec2.types.on_demand_options_request
    import capo_ec2.types.reserved_capacity_options_request
    import capo_ec2.types.spot_options_request
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.target_capacity_specification_request


class CreateFleetRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    spot_options: NotRequired["capo_ec2.types.spot_options_request.SpotOptionsRequest"]
    """<p>Describes the configuration of Spot Instances in an EC2 Fleet.</p>"""
    on_demand_options: NotRequired[
        "capo_ec2.types.on_demand_options_request.OnDemandOptionsRequest"
    ]
    """<p>Describes the configuration of On-Demand Instances in an EC2 Fleet.</p>"""
    reserved_capacity_options: NotRequired[
        "capo_ec2.types.reserved_capacity_options_request.ReservedCapacityOptionsRequest"
    ]
    """<p>Defines EC2 Fleet preferences for utilizing reserved capacity when DefaultTargetCapacityType is set to <code>reserved-capacity</code>.</p> <p>Supported only for fleets of type <code>instant</code>.</p>"""
    excess_capacity_termination_policy: NotRequired[
        "capo_ec2.types.fleet_excess_capacity_termination_policy.FleetExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""
    launch_template_configs: NotRequired[
        "capo_ec2.types.fleet_launch_template_config_list_request.FleetLaunchTemplateConfigListRequest"
    ]
    """<p>The configuration for the EC2 Fleet.</p>"""
    target_capacity_specification: NotRequired[
        "capo_ec2.types.target_capacity_specification_request.TargetCapacitySpecificationRequest"
    ]
    """<p>The number of units to request.</p>"""
    terminate_instances_with_expiration: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether running instances should be terminated when the EC2 Fleet expires.</p>"""
    type: NotRequired["capo_ec2.types.fleet_type.FleetType"]
    """<p>The fleet type. The default value is <code>maintain</code>.</p> <ul> <li> <p> <code>maintain</code> - The EC2 Fleet places an asynchronous request for your desired capacity, and continues to maintain your desired Spot capacity by replenishing interrupted Spot Instances.</p> </li> <li> <p> <code>request</code> - The EC2 Fleet places an asynchronous one-time request for your desired capacity, but does submit Spot requests in alternative capacity pools if Spot capacity is unavailable, and does not maintain Spot capacity if Spot Instances are interrupted.</p> </li> <li> <p> <code>instant</code> - The EC2 Fleet places a synchronous one-time request for your desired capacity, and returns errors for any instances that could not be launched.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-request-type.html">EC2 Fleet request types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    valid_from: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The start date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). The default is to start fulfilling the request immediately.</p>"""
    valid_until: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The end date and time of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). At this point, no new EC2 Fleet requests are placed or able to fulfill the request. If no value is specified, the request remains until you cancel it.</p>"""
    replace_unhealthy_instances: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type <code>maintain</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks">EC2 Fleet health checks</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key-value pair for tagging the EC2 Fleet request on creation. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-resources">Tag your resources</a>.</p> <p>If the fleet type is <code>instant</code>, specify a resource type of <code>fleet</code> to tag the fleet, <code>instance</code> to tag the instances at launch, <code>volume</code> to tag the volumes at launch, or <code>network-interface</code> to tag the network interfaces at launch.</p> <p>If the fleet type is <code>maintain</code> or <code>request</code>, specify a resource type of <code>fleet</code> to tag the fleet. You cannot specify a resource type of <code>instance</code>, <code>volume</code>, or <code>network-interface</code>. To tag instances at launch, specify the tags in a <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template">launch template</a>.</p>"""
    context: NotRequired["capo_ec2.types.string.String"]
    """<p>Reserved.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFleetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "spot_options" in value:
        import capo_ec2.types.spot_options_request

        capo_ec2.types.spot_options_request.serialize_ec2_query(
            value["spot_options"], pairs, f"{key_prefix}SpotOptions"
        )
    if "on_demand_options" in value:
        import capo_ec2.types.on_demand_options_request

        capo_ec2.types.on_demand_options_request.serialize_ec2_query(
            value["on_demand_options"], pairs, f"{key_prefix}OnDemandOptions"
        )
    if "reserved_capacity_options" in value:
        import capo_ec2.types.reserved_capacity_options_request

        capo_ec2.types.reserved_capacity_options_request.serialize_ec2_query(
            value["reserved_capacity_options"],
            pairs,
            f"{key_prefix}ReservedCapacityOptions",
        )
    if "excess_capacity_termination_policy" in value:
        import capo_ec2.types.fleet_excess_capacity_termination_policy

        capo_ec2.types.fleet_excess_capacity_termination_policy.serialize_ec2_query(
            value["excess_capacity_termination_policy"],
            pairs,
            f"{key_prefix}ExcessCapacityTerminationPolicy",
        )
    if "launch_template_configs" in value:
        import capo_ec2.types.fleet_launch_template_config_list_request

        capo_ec2.types.fleet_launch_template_config_list_request.serialize_ec2_query(
            value["launch_template_configs"],
            pairs,
            f"{key_prefix}LaunchTemplateConfigs",
        )
    if "target_capacity_specification" in value:
        import capo_ec2.types.target_capacity_specification_request

        capo_ec2.types.target_capacity_specification_request.serialize_ec2_query(
            value["target_capacity_specification"],
            pairs,
            f"{key_prefix}TargetCapacitySpecification",
        )
    if "terminate_instances_with_expiration" in value:
        pairs.append(
            (
                f"{key_prefix}TerminateInstancesWithExpiration",
                "true" if value["terminate_instances_with_expiration"] else "false",
            )
        )
    if "type" in value:
        import capo_ec2.types.fleet_type

        capo_ec2.types.fleet_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "valid_from" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["valid_from"], pairs, f"{key_prefix}ValidFrom"
        )
    if "valid_until" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["valid_until"], pairs, f"{key_prefix}ValidUntil"
        )
    if "replace_unhealthy_instances" in value:
        pairs.append(
            (
                f"{key_prefix}ReplaceUnhealthyInstances",
                "true" if value["replace_unhealthy_instances"] else "false",
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "context" in value:
        pairs.append((f"{key_prefix}Context", str(value["context"])))


def deserialize_ec2_query(el: Element) -> CreateFleetRequest:
    out: CreateFleetRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_spot_options = el.find("SpotOptions")
    if child_spot_options is not None:
        import capo_ec2.types.spot_options_request

        out["spot_options"] = capo_ec2.types.spot_options_request.deserialize_ec2_query(
            child_spot_options
        )
    child_on_demand_options = el.find("OnDemandOptions")
    if child_on_demand_options is not None:
        import capo_ec2.types.on_demand_options_request

        out["on_demand_options"] = (
            capo_ec2.types.on_demand_options_request.deserialize_ec2_query(
                child_on_demand_options
            )
        )
    child_reserved_capacity_options = el.find("ReservedCapacityOptions")
    if child_reserved_capacity_options is not None:
        import capo_ec2.types.reserved_capacity_options_request

        out["reserved_capacity_options"] = (
            capo_ec2.types.reserved_capacity_options_request.deserialize_ec2_query(
                child_reserved_capacity_options
            )
        )
    child_excess_capacity_termination_policy = el.find(
        "ExcessCapacityTerminationPolicy"
    )
    if child_excess_capacity_termination_policy is not None:
        import capo_ec2.types.fleet_excess_capacity_termination_policy

        out["excess_capacity_termination_policy"] = (
            capo_ec2.types.fleet_excess_capacity_termination_policy.deserialize_ec2_query(
                child_excess_capacity_termination_policy
            )
        )
    child_launch_template_configs = el.find("LaunchTemplateConfigs")
    if child_launch_template_configs is not None:
        import capo_ec2.types.fleet_launch_template_config_list_request

        out["launch_template_configs"] = (
            capo_ec2.types.fleet_launch_template_config_list_request.deserialize_ec2_query(
                child_launch_template_configs
            )
        )
    child_target_capacity_specification = el.find("TargetCapacitySpecification")
    if child_target_capacity_specification is not None:
        import capo_ec2.types.target_capacity_specification_request

        out["target_capacity_specification"] = (
            capo_ec2.types.target_capacity_specification_request.deserialize_ec2_query(
                child_target_capacity_specification
            )
        )
    child_terminate_instances_with_expiration = el.find(
        "TerminateInstancesWithExpiration"
    )
    if child_terminate_instances_with_expiration is not None:
        out["terminate_instances_with_expiration"] = (
            child_terminate_instances_with_expiration.text or ""
        ).lower() == "true"
    child_type = el.find("Type")
    if child_type is not None:
        import capo_ec2.types.fleet_type

        out["type"] = capo_ec2.types.fleet_type.deserialize_ec2_query(child_type)
    child_valid_from = el.find("ValidFrom")
    if child_valid_from is not None:
        import capo_ec2.types.date_time

        out["valid_from"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_valid_from
        )
    child_valid_until = el.find("ValidUntil")
    if child_valid_until is not None:
        import capo_ec2.types.date_time

        out["valid_until"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_valid_until
        )
    child_replace_unhealthy_instances = el.find("ReplaceUnhealthyInstances")
    if child_replace_unhealthy_instances is not None:
        out["replace_unhealthy_instances"] = (
            child_replace_unhealthy_instances.text or ""
        ).lower() == "true"
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_context = el.find("Context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    return out
