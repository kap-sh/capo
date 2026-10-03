"""Generated from Smithy shape ``com.amazonaws.ec2#RunScheduledInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.scheduled_instance_id
    import capo_ec2.types.scheduled_instances_launch_specification
    import capo_ec2.types.string


class RunScheduledInstancesRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances.</p> <p>Default: 1</p>"""
    launch_specification: NotRequired[
        "capo_ec2.types.scheduled_instances_launch_specification.ScheduledInstancesLaunchSpecification"
    ]
    """<p>The launch specification. You must match the instance type, Availability Zone, network, and platform of the schedule that you purchased.</p>"""
    scheduled_instance_id: NotRequired[
        "capo_ec2.types.scheduled_instance_id.ScheduledInstanceId"
    ]
    """<p>The Scheduled Instance ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RunScheduledInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "launch_specification" in value:
        import capo_ec2.types.scheduled_instances_launch_specification

        capo_ec2.types.scheduled_instances_launch_specification.serialize_ec2_query(
            value["launch_specification"], pairs, f"{key_prefix}LaunchSpecification"
        )
    if "scheduled_instance_id" in value:
        pairs.append(
            (f"{key_prefix}ScheduledInstanceId", str(value["scheduled_instance_id"]))
        )


def deserialize_ec2_query(el: Element) -> RunScheduledInstancesRequest:
    out: RunScheduledInstancesRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_launch_specification = el.find("LaunchSpecification")
    if child_launch_specification is not None:
        import capo_ec2.types.scheduled_instances_launch_specification

        out["launch_specification"] = (
            capo_ec2.types.scheduled_instances_launch_specification.deserialize_ec2_query(
                child_launch_specification
            )
        )
    child_scheduled_instance_id = el.find("ScheduledInstanceId")
    if child_scheduled_instance_id is not None:
        out["scheduled_instance_id"] = str(child_scheduled_instance_id.text or "")
    return out
