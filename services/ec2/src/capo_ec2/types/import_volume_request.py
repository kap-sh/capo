"""Generated from Smithy shape ``com.amazonaws.ec2#ImportVolumeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.boolean
    import capo_ec2.types.disk_image_detail
    import capo_ec2.types.string
    import capo_ec2.types.volume_detail


class ImportVolumeRequest(TypedDict, closed=True):
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone for the resulting EBS volume.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone for the resulting EBS volume.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""
    image: NotRequired["capo_ec2.types.disk_image_detail.DiskImageDetail"]
    """<p>The disk image.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the volume.</p>"""
    volume: NotRequired["capo_ec2.types.volume_detail.VolumeDetail"]
    """<p>The volume size.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportVolumeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "image" in value:
        import capo_ec2.types.disk_image_detail

        capo_ec2.types.disk_image_detail.serialize_ec2_query(
            value["image"], pairs, f"{key_prefix}Image"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "volume" in value:
        import capo_ec2.types.volume_detail

        capo_ec2.types.volume_detail.serialize_ec2_query(
            value["volume"], pairs, f"{key_prefix}Volume"
        )


def deserialize_ec2_query(el: Element) -> ImportVolumeRequest:
    out: ImportVolumeRequest = {}  # type: ignore[typeddict-item]
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_image = el.find("image")
    if child_image is not None:
        import capo_ec2.types.disk_image_detail

        out["image"] = capo_ec2.types.disk_image_detail.deserialize_ec2_query(
            child_image
        )
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_volume = el.find("volume")
    if child_volume is not None:
        import capo_ec2.types.volume_detail

        out["volume"] = capo_ec2.types.volume_detail.deserialize_ec2_query(child_volume)
    return out


def redact_sensitive(value: ImportVolumeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image" in value:
        import capo_ec2.types.disk_image_detail

        out["image"] = capo_ec2.types.disk_image_detail.redact_sensitive(value["image"])
    return out
