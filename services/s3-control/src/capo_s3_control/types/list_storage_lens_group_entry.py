"""Generated from Smithy shape ``com.amazonaws.s3control#ListStorageLensGroupEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_aws_region
    import capo_s3_control.types.storage_lens_group_arn
    import capo_s3_control.types.storage_lens_group_name


class ListStorageLensGroupEntry(TypedDict, closed=True):
    name: "capo_s3_control.types.storage_lens_group_name.StorageLensGroupName"
    """<p> Contains the name of the Storage Lens group that exists in the specified home Region. </p>"""
    storage_lens_group_arn: (
        "capo_s3_control.types.storage_lens_group_arn.StorageLensGroupArn"
    )
    """<p> Contains the Amazon Resource Name (ARN) of the Storage Lens group. This property is read-only. </p>"""
    home_region: "capo_s3_control.types.s3_aws_region.S3AWSRegion"
    """<p> Contains the Amazon Web Services Region where the Storage Lens group was created. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListStorageLensGroupEntry, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "StorageLensGroupArn").text = str(value["storage_lens_group_arn"])
    SubElement(el, "HomeRegion").text = str(value["home_region"])


def deserialize_xml(el: Element) -> ListStorageLensGroupEntry:
    out: ListStorageLensGroupEntry = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_storage_lens_group_arn = el.find("StorageLensGroupArn")
    if child_storage_lens_group_arn is not None:
        out["storage_lens_group_arn"] = str(child_storage_lens_group_arn.text or "")
    else:
        out["storage_lens_group_arn"] = ""
    child_home_region = el.find("HomeRegion")
    if child_home_region is not None:
        out["home_region"] = str(child_home_region.text or "")
    else:
        out["home_region"] = ""
    return out
