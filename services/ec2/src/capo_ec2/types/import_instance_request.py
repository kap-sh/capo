"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.disk_image_list
    import capo_ec2.types.import_instance_launch_specification
    import capo_ec2.types.platform_values
    import capo_ec2.types.string


class ImportInstanceRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the instance being imported.</p>"""
    launch_specification: NotRequired[
        "capo_ec2.types.import_instance_launch_specification.ImportInstanceLaunchSpecification"
    ]
    """<p>The launch specification.</p>"""
    disk_images: NotRequired["capo_ec2.types.disk_image_list.DiskImageList"]
    """<p>The disk image.</p>"""
    platform: NotRequired["capo_ec2.types.platform_values.PlatformValues"]
    """<p>The instance operating system.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "launch_specification" in value:
        import capo_ec2.types.import_instance_launch_specification

        capo_ec2.types.import_instance_launch_specification.serialize_ec2_query(
            value["launch_specification"], pairs, f"{key_prefix}LaunchSpecification"
        )
    if "disk_images" in value:
        import capo_ec2.types.disk_image_list

        capo_ec2.types.disk_image_list.serialize_ec2_query(
            value["disk_images"], pairs, f"{key_prefix}DiskImage"
        )
    if "platform" in value:
        import capo_ec2.types.platform_values

        capo_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{key_prefix}Platform"
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceRequest:
    out: ImportInstanceRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_launch_specification = el.find("launchSpecification")
    if child_launch_specification is not None:
        import capo_ec2.types.import_instance_launch_specification

        out["launch_specification"] = (
            capo_ec2.types.import_instance_launch_specification.deserialize_ec2_query(
                child_launch_specification
            )
        )
    child_disk_images = el.find("diskImage")
    if child_disk_images is not None:
        import capo_ec2.types.disk_image_list

        out["disk_images"] = capo_ec2.types.disk_image_list.deserialize_ec2_query(
            child_disk_images
        )
    child_platform = el.find("platform")
    if child_platform is not None:
        import capo_ec2.types.platform_values

        out["platform"] = capo_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    return out


def redact_sensitive(value: ImportInstanceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_specification" in value:
        import capo_ec2.types.import_instance_launch_specification

        out["launch_specification"] = (
            capo_ec2.types.import_instance_launch_specification.redact_sensitive(
                value["launch_specification"]
            )
        )
    if "disk_images" in value:
        import capo_ec2.types.disk_image_list

        out["disk_images"] = capo_ec2.types.disk_image_list.redact_sensitive(
            value["disk_images"]
        )
    return out
