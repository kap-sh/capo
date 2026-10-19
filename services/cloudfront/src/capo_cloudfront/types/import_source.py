"""Generated from Smithy shape ``com.amazonaws.cloudfront#ImportSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.import_source_type
    import capo_cloudfront.types.string


class ImportSource(TypedDict, closed=True):
    source_type: "capo_cloudfront.types.import_source_type.ImportSourceType"
    """<p>The source type of the import source for the key value store.</p>"""
    source_arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the import source for the key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ImportSource, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.import_source_type

    capo_cloudfront.types.import_source_type.serialize_xml(
        value["source_type"], el, "SourceType"
    )
    SubElement(el, "SourceARN").text = str(value["source_arn"])


def deserialize_xml(el: Element) -> ImportSource:
    out: ImportSource = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import capo_cloudfront.types.import_source_type

        out["source_type"] = capo_cloudfront.types.import_source_type.deserialize_xml(
            child_source_type
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_cloudfront.types.import_source_type.ImportSourceType", ""
        )
    child_source_arn = el.find("SourceARN")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    else:
        out["source_arn"] = ""
    return out
