"""Generated from Smithy shape ``com.amazonaws.ec2#DetachNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_interface_attachment_id


class DetachNetworkInterfaceRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    attachment_id: NotRequired[
        "capo_ec2.types.network_interface_attachment_id.NetworkInterfaceAttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    force: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to force a detachment.</p> <note> <ul> <li> <p>Use the <code>Force</code> parameter only as a last resort to detach a network interface from a failed instance. </p> </li> <li> <p>If you use the <code>Force</code> parameter to detach a network interface, you might not be able to attach a different network interface to the same index on the instance without first stopping and starting the instance.</p> </li> <li> <p>If you force the detachment of a network interface, the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html">instance metadata</a> might not get updated. This means that the attributes associated with the detached network interface might still be visible. The instance metadata will get updated when you stop and start the instance.</p> </li> </ul> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DetachNetworkInterfaceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "attachment_id" in value:
        pairs.append((f"{key_prefix}AttachmentId", str(value["attachment_id"])))
    if "force" in value:
        pairs.append((f"{key_prefix}Force", "true" if value["force"] else "false"))


def deserialize_ec2_query(el: Element) -> DetachNetworkInterfaceRequest:
    out: DetachNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_attachment_id = el.find("attachmentId")
    if child_attachment_id is not None:
        out["attachment_id"] = str(child_attachment_id.text or "")
    child_force = el.find("force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    return out
