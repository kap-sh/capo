"""Generated from Smithy shape ``com.amazonaws.ec2#BundleInstanceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id
    import capo_ec2.types.storage


class BundleInstanceRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance to bundle.</p> <p>Default: None</p>"""
    storage: NotRequired["capo_ec2.types.storage.Storage"]
    """<p>The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BundleInstanceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "storage" in value:
        import capo_ec2.types.storage

        capo_ec2.types.storage.serialize_ec2_query(
            value["storage"], pairs, f"{key_prefix}Storage"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> BundleInstanceRequest:
    out: BundleInstanceRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_storage = el.find("Storage")
    if child_storage is not None:
        import capo_ec2.types.storage

        out["storage"] = capo_ec2.types.storage.deserialize_ec2_query(child_storage)
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out


def redact_sensitive(value: BundleInstanceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "storage" in value:
        import capo_ec2.types.storage

        out["storage"] = capo_ec2.types.storage.redact_sensitive(value["storage"])
    return out
