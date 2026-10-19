"""Generated from Smithy shape ``com.amazonaws.s3#OwnershipControlsRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_ownership


class OwnershipControlsRule(TypedDict, closed=True):
    object_ownership: "capo_s3.types.object_ownership.ObjectOwnership"


# --- restXml ser/de ---
def serialize_xml(value: OwnershipControlsRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.object_ownership

    capo_s3.types.object_ownership.serialize_xml(
        value["object_ownership"], el, "ObjectOwnership"
    )


def deserialize_xml(el: Element) -> OwnershipControlsRule:
    out: OwnershipControlsRule = {}  # type: ignore[typeddict-item]
    child_object_ownership = el.find("ObjectOwnership")
    if child_object_ownership is not None:
        import capo_s3.types.object_ownership

        out["object_ownership"] = capo_s3.types.object_ownership.deserialize_xml(
            child_object_ownership
        )
    else:
        import typing

        out["object_ownership"] = typing.cast(
            "capo_s3.types.object_ownership.ObjectOwnership", ""
        )
    return out
