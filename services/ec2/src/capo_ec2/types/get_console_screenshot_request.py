"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleScreenshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id


class GetConsoleScreenshotRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    wake_up: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>When set to <code>true</code>, acts as keystroke input and wakes up an instance that's in standby or "sleep" mode.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetConsoleScreenshotRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "wake_up" in value:
        pairs.append((f"{key_prefix}WakeUp", "true" if value["wake_up"] else "false"))


def deserialize_ec2_query(el: Element) -> GetConsoleScreenshotRequest:
    out: GetConsoleScreenshotRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_wake_up = el.find("WakeUp")
    if child_wake_up is not None:
        out["wake_up"] = (child_wake_up.text or "").lower() == "true"
    return out
