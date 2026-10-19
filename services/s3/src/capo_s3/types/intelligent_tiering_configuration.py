"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.intelligent_tiering_filter
    import capo_s3.types.intelligent_tiering_id
    import capo_s3.types.intelligent_tiering_status
    import capo_s3.types.tiering_list


class IntelligentTieringConfiguration(TypedDict, closed=True):
    id: "capo_s3.types.intelligent_tiering_id.IntelligentTieringId"
    """<p>The ID used to identify the S3 Intelligent-Tiering configuration.</p>"""
    filter: NotRequired[
        "capo_s3.types.intelligent_tiering_filter.IntelligentTieringFilter"
    ]
    """<p>Specifies a bucket filter. The configuration only includes objects that meet the filter's criteria.</p>"""
    status: "capo_s3.types.intelligent_tiering_status.IntelligentTieringStatus"
    """<p>Specifies the status of the configuration.</p>"""
    tierings: "capo_s3.types.tiering_list.TieringList"
    """<p>Specifies the S3 Intelligent-Tiering storage class tier of the configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: IntelligentTieringConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    if "filter" in value:
        import capo_s3.types.intelligent_tiering_filter

        capo_s3.types.intelligent_tiering_filter.serialize_xml(
            value["filter"], el, "Filter"
        )
    import capo_s3.types.intelligent_tiering_status

    capo_s3.types.intelligent_tiering_status.serialize_xml(
        value["status"], el, "Status"
    )
    import capo_s3.types.tiering_list

    capo_s3.types.tiering_list.serialize_xml_flat(value["tierings"], el, "Tiering")


def deserialize_xml(el: Element) -> IntelligentTieringConfiguration:
    out: IntelligentTieringConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3.types.intelligent_tiering_filter

        out["filter"] = capo_s3.types.intelligent_tiering_filter.deserialize_xml(
            child_filter
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.intelligent_tiering_status

        out["status"] = capo_s3.types.intelligent_tiering_status.deserialize_xml(
            child_status
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3.types.intelligent_tiering_status.IntelligentTieringStatus", ""
        )
    if el.find("Tiering") is not None:
        import capo_s3.types.tiering_list

        out["tierings"] = capo_s3.types.tiering_list.deserialize_xml_flat(el, "Tiering")
    else:
        out["tierings"] = []
    return out
