"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_lifecycle
    import capo_ec2.types.launch_template_and_overrides_response
    import capo_ec2.types.string


class DescribeFleetError(TypedDict, closed=True):
    launch_template_and_overrides: NotRequired[
        "capo_ec2.types.launch_template_and_overrides_response.LaunchTemplateAndOverridesResponse"
    ]
    """<p>The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.</p>"""
    lifecycle: NotRequired["capo_ec2.types.instance_lifecycle.InstanceLifecycle"]
    """<p>Indicates if the instance that could not be launched was a Spot, On-Demand, Capacity Block for ML, or interruptible Capacity Reservation instance. If you are using <code>ReservedCapacityOptions</code> with <code>on-demand-capacity-reservation</code> in the <code>ReservationTypes</code> list, the value can also be <code>on-demand-capacity-reservation</code>.</p>"""
    error_code: NotRequired["capo_ec2.types.string.String"]
    """<p>The error code that indicates why the instance could not be launched. For more information about error codes, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html">Error codes</a>.</p>"""
    error_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The error message that describes why the instance could not be launched. For more information about error messages, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html">Error codes</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetError, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_and_overrides" in value:
        import capo_ec2.types.launch_template_and_overrides_response

        capo_ec2.types.launch_template_and_overrides_response.serialize_ec2_query(
            value["launch_template_and_overrides"],
            pairs,
            f"{key_prefix}LaunchTemplateAndOverrides",
        )
    if "lifecycle" in value:
        import capo_ec2.types.instance_lifecycle

        capo_ec2.types.instance_lifecycle.serialize_ec2_query(
            value["lifecycle"], pairs, f"{key_prefix}Lifecycle"
        )
    if "error_code" in value:
        pairs.append((f"{key_prefix}ErrorCode", str(value["error_code"])))
    if "error_message" in value:
        pairs.append((f"{key_prefix}ErrorMessage", str(value["error_message"])))


def deserialize_ec2_query(el: Element) -> DescribeFleetError:
    out: DescribeFleetError = {}  # type: ignore[typeddict-item]
    child_launch_template_and_overrides = el.find("launchTemplateAndOverrides")
    if child_launch_template_and_overrides is not None:
        import capo_ec2.types.launch_template_and_overrides_response

        out["launch_template_and_overrides"] = (
            capo_ec2.types.launch_template_and_overrides_response.deserialize_ec2_query(
                child_launch_template_and_overrides
            )
        )
    child_lifecycle = el.find("lifecycle")
    if child_lifecycle is not None:
        import capo_ec2.types.instance_lifecycle

        out["lifecycle"] = capo_ec2.types.instance_lifecycle.deserialize_ec2_query(
            child_lifecycle
        )
    child_error_code = el.find("errorCode")
    if child_error_code is not None:
        out["error_code"] = str(child_error_code.text or "")
    child_error_message = el.find("errorMessage")
    if child_error_message is not None:
        out["error_message"] = str(child_error_message.text or "")
    return out
