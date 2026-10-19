"""Generated from Smithy shape ``com.amazonaws.s3control#ListStorageLensConfigurationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.config_id
    import capo_s3_control.types.is_enabled
    import capo_s3_control.types.s3_aws_region
    import capo_s3_control.types.storage_lens_arn


class ListStorageLensConfigurationEntry(TypedDict, closed=True):
    id: "capo_s3_control.types.config_id.ConfigId"
    """<p>A container for the S3 Storage Lens configuration ID.</p>"""
    storage_lens_arn: "capo_s3_control.types.storage_lens_arn.StorageLensArn"
    """<p>The ARN of the S3 Storage Lens configuration. This property is read-only.</p>"""
    home_region: "capo_s3_control.types.s3_aws_region.S3AWSRegion"
    """<p>A container for the S3 Storage Lens home Region. Your metrics data is stored and retained in your designated S3 Storage Lens home Region.</p>"""
    is_enabled: "capo_s3_control.types.is_enabled.IsEnabled"
    """<p>A container for whether the S3 Storage Lens configuration is enabled. This property is required.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStorageLensConfigurationEntry, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "StorageLensArn").text = str(value["storage_lens_arn"])
    SubElement(el, "HomeRegion").text = str(value["home_region"])
    SubElement(el, "IsEnabled").text = (
        "true" if value.get("is_enabled", False) else "false"
    )


def deserialize_xml(el: Element) -> ListStorageLensConfigurationEntry:
    out: ListStorageLensConfigurationEntry = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_storage_lens_arn = el.find("StorageLensArn")
    if child_storage_lens_arn is not None:
        out["storage_lens_arn"] = str(child_storage_lens_arn.text or "")
    else:
        out["storage_lens_arn"] = ""
    child_home_region = el.find("HomeRegion")
    if child_home_region is not None:
        out["home_region"] = str(child_home_region.text or "")
    else:
        out["home_region"] = ""
    child_is_enabled = el.find("IsEnabled")
    if child_is_enabled is not None:
        out["is_enabled"] = (child_is_enabled.text or "").lower() == "true"
    else:
        out["is_enabled"] = False
    return out
