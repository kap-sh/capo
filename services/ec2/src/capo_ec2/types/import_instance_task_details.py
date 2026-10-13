"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceTaskDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.import_instance_volume_detail_set
    import capo_ec2.types.platform_values
    import capo_ec2.types.string


class ImportInstanceTaskDetails(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the task.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    platform: NotRequired["capo_ec2.types.platform_values.PlatformValues"]
    """<p>The instance operating system.</p>"""
    volumes: NotRequired[
        "capo_ec2.types.import_instance_volume_detail_set.ImportInstanceVolumeDetailSet"
    ]
    """<p>The volumes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceTaskDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "platform" in value:
        import capo_ec2.types.platform_values

        capo_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{key_prefix}Platform"
        )
    if "volumes" in value:
        import capo_ec2.types.import_instance_volume_detail_set

        capo_ec2.types.import_instance_volume_detail_set.serialize_ec2_query(
            value["volumes"], pairs, f"{key_prefix}Volumes"
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceTaskDetails:
    out: ImportInstanceTaskDetails = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_platform = el.find("platform")
    if child_platform is not None:
        import capo_ec2.types.platform_values

        out["platform"] = capo_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    child_volumes = el.find("volumes")
    if child_volumes is not None:
        import capo_ec2.types.import_instance_volume_detail_set

        out["volumes"] = (
            capo_ec2.types.import_instance_volume_detail_set.deserialize_ec2_query(
                child_volumes
            )
        )
    return out


def redact_sensitive(value: ImportInstanceTaskDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "volumes" in value:
        import capo_ec2.types.import_instance_volume_detail_set

        out["volumes"] = (
            capo_ec2.types.import_instance_volume_detail_set.redact_sensitive(
                value["volumes"]
            )
        )
    return out
