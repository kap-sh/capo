"""Generated from Smithy shape ``com.amazonaws.s3#UseSourceMultiRegionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.use_source_multi_region_key_status


class UseSourceMultiRegionKey(TypedDict, closed=True):
    status: (
        "capo_s3.types.use_source_multi_region_key_status.UseSourceMultiRegionKeyStatus"
    )
    """<p>Specifies whether Amazon S3 uses the related multi-Region KMS key in the destination Amazon Web Services Region to encrypt the replica.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UseSourceMultiRegionKey, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.use_source_multi_region_key_status

    capo_s3.types.use_source_multi_region_key_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> UseSourceMultiRegionKey:
    out: UseSourceMultiRegionKey = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.use_source_multi_region_key_status

        out["status"] = (
            capo_s3.types.use_source_multi_region_key_status.deserialize_xml(
                child_status
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3.types.use_source_multi_region_key_status.UseSourceMultiRegionKeyStatus",
            "",
        )
    return out
