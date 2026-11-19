"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.allocation_strategy
    import capo_compute_optimizer.types.asg_type
    import capo_compute_optimizer.types.desired_capacity
    import capo_compute_optimizer.types.max_size
    import capo_compute_optimizer.types.min_size
    import capo_compute_optimizer.types.mixed_instance_types
    import capo_compute_optimizer.types.nullable_estimated_instance_hour_reduction_percentage
    import capo_compute_optimizer.types.nullable_instance_type


class AutoScalingGroupConfiguration(TypedDict, closed=True):
    desired_capacity: "capo_compute_optimizer.types.desired_capacity.DesiredCapacity"
    """<p>The desired capacity, or number of instances, for the EC2 Auto Scaling group.</p>"""
    min_size: "capo_compute_optimizer.types.min_size.MinSize"
    """<p>The minimum size, or minimum number of instances, for the EC2 Auto Scaling group.</p>"""
    max_size: "capo_compute_optimizer.types.max_size.MaxSize"
    """<p>The maximum size, or maximum number of instances, for the EC2 Auto Scaling group.</p>"""
    instance_type: NotRequired[
        "capo_compute_optimizer.types.nullable_instance_type.NullableInstanceType"
    ]
    """<p>The instance type for the EC2 Auto Scaling group.</p>"""
    allocation_strategy: NotRequired[
        "capo_compute_optimizer.types.allocation_strategy.AllocationStrategy"
    ]
    """<p> Describes the allocation strategy that the EC2 Auto Scaling group uses. This field is only available for EC2 Auto Scaling groups with mixed instance types. </p>"""
    estimated_instance_hour_reduction_percentage: NotRequired[
        "capo_compute_optimizer.types.nullable_estimated_instance_hour_reduction_percentage.NullableEstimatedInstanceHourReductionPercentage"
    ]
    """<p> Describes the projected percentage reduction in instance hours after adopting the recommended configuration. This field is only available for EC2 Auto Scaling groups with scaling policies. </p>"""
    type: NotRequired["capo_compute_optimizer.types.asg_type.AsgType"]
    """<p> Describes whether the EC2 Auto Scaling group has a single instance type or a mixed instance type configuration. </p>"""
    mixed_instance_types: NotRequired[
        "capo_compute_optimizer.types.mixed_instance_types.MixedInstanceTypes"
    ]
    """<p> List the instance types within an EC2 Auto Scaling group that has mixed instance types. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingGroupConfiguration) -> dict:
    out: dict = {}
    out["desiredCapacity"] = value.get("desired_capacity", 0)
    out["minSize"] = value.get("min_size", 0)
    out["maxSize"] = value.get("max_size", 0)
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "allocation_strategy" in value:
        import capo_compute_optimizer.types.allocation_strategy

        out["allocationStrategy"] = (
            capo_compute_optimizer.types.allocation_strategy.serialize_aws_json_1_0(
                value["allocation_strategy"]
            )
        )
    if "estimated_instance_hour_reduction_percentage" in value:
        out["estimatedInstanceHourReductionPercentage"] = (
            "NaN"
            if value["estimated_instance_hour_reduction_percentage"]
            != value["estimated_instance_hour_reduction_percentage"]
            else "Infinity"
            if value["estimated_instance_hour_reduction_percentage"] == float("inf")
            else "-Infinity"
            if value["estimated_instance_hour_reduction_percentage"] == float("-inf")
            else value["estimated_instance_hour_reduction_percentage"]
        )
    if "type" in value:
        import capo_compute_optimizer.types.asg_type

        out["type"] = capo_compute_optimizer.types.asg_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "mixed_instance_types" in value:
        import capo_compute_optimizer.types.mixed_instance_types

        out["mixedInstanceTypes"] = (
            capo_compute_optimizer.types.mixed_instance_types.serialize_aws_json_1_0(
                value["mixed_instance_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingGroupConfiguration:
    out: AutoScalingGroupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("desiredCapacity") is not None:
        out["desired_capacity"] = data["desiredCapacity"]
    else:
        out["desired_capacity"] = 0
    if data.get("minSize") is not None:
        out["min_size"] = data["minSize"]
    else:
        out["min_size"] = 0
    if data.get("maxSize") is not None:
        out["max_size"] = data["maxSize"]
    else:
        out["max_size"] = 0
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("allocationStrategy") is not None:
        import capo_compute_optimizer.types.allocation_strategy

        out["allocation_strategy"] = (
            capo_compute_optimizer.types.allocation_strategy.deserialize_aws_json_1_0(
                data["allocationStrategy"]
            )
        )
    if data.get("estimatedInstanceHourReductionPercentage") is not None:
        out["estimated_instance_hour_reduction_percentage"] = float(
            data["estimatedInstanceHourReductionPercentage"]
        )
    if data.get("type") is not None:
        import capo_compute_optimizer.types.asg_type

        out["type"] = capo_compute_optimizer.types.asg_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if data.get("mixedInstanceTypes") is not None:
        import capo_compute_optimizer.types.mixed_instance_types

        out["mixed_instance_types"] = (
            capo_compute_optimizer.types.mixed_instance_types.deserialize_aws_json_1_0(
                data["mixedInstanceTypes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoScalingGroupConfiguration) -> dict:
    out: dict = {}
    out["desiredCapacity"] = value.get("desired_capacity", 0)
    out["minSize"] = value.get("min_size", 0)
    out["maxSize"] = value.get("max_size", 0)
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "allocation_strategy" in value:
        import capo_compute_optimizer.types.allocation_strategy

        out["allocationStrategy"] = (
            capo_compute_optimizer.types.allocation_strategy.serialize_cbor(
                value["allocation_strategy"]
            )
        )
    if "estimated_instance_hour_reduction_percentage" in value:
        out["estimatedInstanceHourReductionPercentage"] = value[
            "estimated_instance_hour_reduction_percentage"
        ]
    if "type" in value:
        import capo_compute_optimizer.types.asg_type

        out["type"] = capo_compute_optimizer.types.asg_type.serialize_cbor(
            value["type"]
        )
    if "mixed_instance_types" in value:
        import capo_compute_optimizer.types.mixed_instance_types

        out["mixedInstanceTypes"] = (
            capo_compute_optimizer.types.mixed_instance_types.serialize_cbor(
                value["mixed_instance_types"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AutoScalingGroupConfiguration:
    out: AutoScalingGroupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("desiredCapacity") is not None:
        out["desired_capacity"] = data["desiredCapacity"]
    else:
        out["desired_capacity"] = 0
    if data.get("minSize") is not None:
        out["min_size"] = data["minSize"]
    else:
        out["min_size"] = 0
    if data.get("maxSize") is not None:
        out["max_size"] = data["maxSize"]
    else:
        out["max_size"] = 0
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("allocationStrategy") is not None:
        import capo_compute_optimizer.types.allocation_strategy

        out["allocation_strategy"] = (
            capo_compute_optimizer.types.allocation_strategy.deserialize_cbor(
                data["allocationStrategy"]
            )
        )
    if data.get("estimatedInstanceHourReductionPercentage") is not None:
        out["estimated_instance_hour_reduction_percentage"] = float(
            data["estimatedInstanceHourReductionPercentage"]
        )
    if data.get("type") is not None:
        import capo_compute_optimizer.types.asg_type

        out["type"] = capo_compute_optimizer.types.asg_type.deserialize_cbor(
            data["type"]
        )
    if data.get("mixedInstanceTypes") is not None:
        import capo_compute_optimizer.types.mixed_instance_types

        out["mixed_instance_types"] = (
            capo_compute_optimizer.types.mixed_instance_types.deserialize_cbor(
                data["mixedInstanceTypes"]
            )
        )
    return out
