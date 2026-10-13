"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disk_image_detail
    import capo_ec2.types.string
    import capo_ec2.types.volume_detail


class DiskImage(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the disk image.</p>"""
    image: NotRequired["capo_ec2.types.disk_image_detail.DiskImageDetail"]
    """<p>Information about the disk image.</p>"""
    volume: NotRequired["capo_ec2.types.volume_detail.VolumeDetail"]
    """<p>Information about the volume.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskImage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "image" in value:
        import capo_ec2.types.disk_image_detail

        capo_ec2.types.disk_image_detail.serialize_ec2_query(
            value["image"], pairs, f"{key_prefix}Image"
        )
    if "volume" in value:
        import capo_ec2.types.volume_detail

        capo_ec2.types.volume_detail.serialize_ec2_query(
            value["volume"], pairs, f"{key_prefix}Volume"
        )


def deserialize_ec2_query(el: Element) -> DiskImage:
    out: DiskImage = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_image = el.find("Image")
    if child_image is not None:
        import capo_ec2.types.disk_image_detail

        out["image"] = capo_ec2.types.disk_image_detail.deserialize_ec2_query(
            child_image
        )
    child_volume = el.find("Volume")
    if child_volume is not None:
        import capo_ec2.types.volume_detail

        out["volume"] = capo_ec2.types.volume_detail.deserialize_ec2_query(child_volume)
    return out


def redact_sensitive(value: DiskImage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image" in value:
        import capo_ec2.types.disk_image_detail

        out["image"] = capo_ec2.types.disk_image_detail.redact_sensitive(value["image"])
    return out
