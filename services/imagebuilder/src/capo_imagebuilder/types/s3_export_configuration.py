"""Generated from Smithy shape ``com.amazonaws.imagebuilder#S3ExportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.disk_image_format
    import capo_imagebuilder.types.non_empty_string


class S3ExportConfiguration(TypedDict, closed=True):
    role_name: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The name of the role that grants VM Import/Export permission to export images to your S3 bucket.</p>"""
    disk_image_format: "capo_imagebuilder.types.disk_image_format.DiskImageFormat"
    """<p>Export the updated image to one of the following supported disk image formats:</p> <ul> <li> <p> <b>Virtual Hard Disk (VHD)</b> – Compatible with Citrix Xen and Microsoft Hyper-V virtualization products.</p> </li> <li> <p> <b>Stream-optimized ESX Virtual Machine Disk (VMDK)</b> – Compatible with VMware ESX and VMware vSphere versions 4, 5, and 6.</p> </li> <li> <p> <b>Raw</b> – Raw format.</p> </li> </ul>"""
    s3_bucket: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The S3 bucket in which to store the output disk images for your VM.</p>"""
    s3_prefix: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon S3 path for the bucket where the output disk images for your VM are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ExportConfiguration) -> dict:
    out: dict = {}
    out["roleName"] = value["role_name"]
    import capo_imagebuilder.types.disk_image_format

    out["diskImageFormat"] = capo_imagebuilder.types.disk_image_format.serialize_json(
        value["disk_image_format"]
    )
    out["s3Bucket"] = value["s3_bucket"]
    if "s3_prefix" in value:
        out["s3Prefix"] = value["s3_prefix"]
    return out


def deserialize_json(data: dict) -> S3ExportConfiguration:
    out: S3ExportConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("roleName") is not None:
        out["role_name"] = data["roleName"]
    else:
        out["role_name"] = ""
    if data.get("diskImageFormat") is not None:
        import capo_imagebuilder.types.disk_image_format

        out["disk_image_format"] = (
            capo_imagebuilder.types.disk_image_format.deserialize_json(
                data["diskImageFormat"]
            )
        )
    else:
        import typing

        out["disk_image_format"] = typing.cast(
            "capo_imagebuilder.types.disk_image_format.DiskImageFormat", ""
        )
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("s3Prefix") is not None:
        out["s3_prefix"] = data["s3Prefix"]
    return out
