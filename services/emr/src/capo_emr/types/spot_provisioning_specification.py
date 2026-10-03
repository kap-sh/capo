"""Generated from Smithy shape ``com.amazonaws.emr#SpotProvisioningSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.spot_provisioning_allocation_strategy
    import capo_emr.types.spot_provisioning_timeout_action
    import capo_emr.types.whole_number


class SpotProvisioningSpecification(TypedDict, closed=True):
    timeout_duration_minutes: NotRequired["capo_emr.types.whole_number.WholeNumber"]
    """<p>The Spot provisioning timeout period in minutes. If Spot Instances are not provisioned within this time period, the <code>TimeOutAction</code> is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.</p>"""
    timeout_action: NotRequired[
        "capo_emr.types.spot_provisioning_timeout_action.SpotProvisioningTimeoutAction"
    ]
    """<p>The action to take when <code>TargetSpotCapacity</code> has not been fulfilled when the <code>TimeoutDurationMinutes</code> has expired; that is, when all Spot Instances could not be provisioned within the Spot provisioning timeout. Valid values are <code>TERMINATE_CLUSTER</code> and <code>SWITCH_TO_ON_DEMAND</code>. SWITCH_TO_ON_DEMAND specifies that if no Spot Instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.</p>"""
    block_duration_minutes: NotRequired["capo_emr.types.whole_number.WholeNumber"]
    """<p>The defined duration for Spot Instances (also known as Spot blocks) in minutes. When specified, the Spot Instance does not terminate before the defined duration expires, and defined duration pricing for Spot Instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot Instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates. </p> <note> <p>Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022. </p> </note>"""
    allocation_strategy: NotRequired[
        "capo_emr.types.spot_provisioning_allocation_strategy.SpotProvisioningAllocationStrategy"
    ]
    """<p>Specifies one of the following strategies to launch Spot Instance fleets: <code>capacity-optimized</code>, <code>price-capacity-optimized</code>, <code>lowest-price</code>, or <code>diversified</code>, and <code>capacity-optimized-prioritized</code>. For more information on the provisioning strategies, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html">Allocation strategies for Spot Instances</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>.</p> <note> <p>When you launch a Spot Instance fleet with the old console, it automatically launches with the <code>capacity-optimized</code> strategy. You can't change the allocation strategy from the old console.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpotProvisioningSpecification) -> dict:
    out: dict = {}
    if "timeout_duration_minutes" in value:
        out["TimeoutDurationMinutes"] = value["timeout_duration_minutes"]
    if "timeout_action" in value:
        import capo_emr.types.spot_provisioning_timeout_action

        out["TimeoutAction"] = (
            capo_emr.types.spot_provisioning_timeout_action.serialize_aws_json_1_1(
                value["timeout_action"]
            )
        )
    if "block_duration_minutes" in value:
        out["BlockDurationMinutes"] = value["block_duration_minutes"]
    if "allocation_strategy" in value:
        import capo_emr.types.spot_provisioning_allocation_strategy

        out["AllocationStrategy"] = (
            capo_emr.types.spot_provisioning_allocation_strategy.serialize_aws_json_1_1(
                value["allocation_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpotProvisioningSpecification:
    out: SpotProvisioningSpecification = {}  # type: ignore[typeddict-item]
    if data.get("TimeoutDurationMinutes") is not None:
        out["timeout_duration_minutes"] = data["TimeoutDurationMinutes"]
    if data.get("TimeoutAction") is not None:
        import capo_emr.types.spot_provisioning_timeout_action

        out["timeout_action"] = (
            capo_emr.types.spot_provisioning_timeout_action.deserialize_aws_json_1_1(
                data["TimeoutAction"]
            )
        )
    if data.get("BlockDurationMinutes") is not None:
        out["block_duration_minutes"] = data["BlockDurationMinutes"]
    if data.get("AllocationStrategy") is not None:
        import capo_emr.types.spot_provisioning_allocation_strategy

        out["allocation_strategy"] = (
            capo_emr.types.spot_provisioning_allocation_strategy.deserialize_aws_json_1_1(
                data["AllocationStrategy"]
            )
        )
    return out
