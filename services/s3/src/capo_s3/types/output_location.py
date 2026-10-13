"""Generated from Smithy shape ``com.amazonaws.s3#OutputLocation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.s3_location


class OutputLocation(TypedDict, closed=True):
    s3: NotRequired["capo_s3.types.s3_location.S3Location"]
    """<p>Describes an S3 location that will receive the results of the restore request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OutputLocation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "s3" in value:
        import capo_s3.types.s3_location

        capo_s3.types.s3_location.serialize_xml(value["s3"], el, "S3")


def deserialize_xml(el: Element) -> OutputLocation:
    out: OutputLocation = {}  # type: ignore[typeddict-item]
    child_s3 = el.find("S3")
    if child_s3 is not None:
        import capo_s3.types.s3_location

        out["s3"] = capo_s3.types.s3_location.deserialize_xml(child_s3)
    return out


def redact_sensitive(value: OutputLocation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3" in value:
        import capo_s3.types.s3_location

        out["s3"] = capo_s3.types.s3_location.redact_sensitive(value["s3"])
    return out
