"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteMultiRegionAccessPointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.multi_region_access_point_name


class DeleteMultiRegionAccessPointInput(TypedDict, closed=True):
    name: "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName"
    """<p>The name of the Multi-Region Access Point associated with this request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteMultiRegionAccessPointInput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])


def deserialize_xml(el: Element) -> DeleteMultiRegionAccessPointInput:
    out: DeleteMultiRegionAccessPointInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    return out
