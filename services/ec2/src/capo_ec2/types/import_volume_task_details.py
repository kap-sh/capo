"""Generated from Smithy shape ``com.amazonaws.ec2#ImportVolumeTaskDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disk_image_description
    import capo_ec2.types.disk_image_volume_description
    import capo_ec2.types.long
    import capo_ec2.types.string


class ImportVolumeTaskDetails(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone where the resulting volume will reside.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone where the resulting volume will reside.</p>"""
    bytes_converted: NotRequired["capo_ec2.types.long.Long"]
    """<p>The number of bytes converted so far.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description you provided when starting the import volume task.</p>"""
    image: NotRequired["capo_ec2.types.disk_image_description.DiskImageDescription"]
    """<p>The image.</p>"""
    volume: NotRequired[
        "capo_ec2.types.disk_image_volume_description.DiskImageVolumeDescription"
    ]
    """<p>The volume.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportVolumeTaskDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "bytes_converted" in value:
        pairs.append((f"{key_prefix}BytesConverted", str(value["bytes_converted"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "image" in value:
        import capo_ec2.types.disk_image_description

        capo_ec2.types.disk_image_description.serialize_ec2_query(
            value["image"], pairs, f"{key_prefix}Image"
        )
    if "volume" in value:
        import capo_ec2.types.disk_image_volume_description

        capo_ec2.types.disk_image_volume_description.serialize_ec2_query(
            value["volume"], pairs, f"{key_prefix}Volume"
        )


def deserialize_ec2_query(el: Element) -> ImportVolumeTaskDetails:
    out: ImportVolumeTaskDetails = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_bytes_converted = el.find("bytesConverted")
    if child_bytes_converted is not None:
        out["bytes_converted"] = int(child_bytes_converted.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_image = el.find("image")
    if child_image is not None:
        import capo_ec2.types.disk_image_description

        out["image"] = capo_ec2.types.disk_image_description.deserialize_ec2_query(
            child_image
        )
    child_volume = el.find("volume")
    if child_volume is not None:
        import capo_ec2.types.disk_image_volume_description

        out["volume"] = (
            capo_ec2.types.disk_image_volume_description.deserialize_ec2_query(
                child_volume
            )
        )
    return out


def redact_sensitive(value: ImportVolumeTaskDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image" in value:
        import capo_ec2.types.disk_image_description

        out["image"] = capo_ec2.types.disk_image_description.redact_sensitive(
            value["image"]
        )
    return out
