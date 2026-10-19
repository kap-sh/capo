"""Generated from Smithy shape ``com.amazonaws.s3control#AccessControlTranslation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.owner_override


class AccessControlTranslation(TypedDict, closed=True):
    owner: "capo_s3_control.types.owner_override.OwnerOverride"
    """<p>Specifies the replica ownership.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AccessControlTranslation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.owner_override

    capo_s3_control.types.owner_override.serialize_xml(value["owner"], el, "Owner")


def deserialize_xml(el: Element) -> AccessControlTranslation:
    out: AccessControlTranslation = {}  # type: ignore[typeddict-item]
    child_owner = el.find("Owner")
    if child_owner is not None:
        import capo_s3_control.types.owner_override

        out["owner"] = capo_s3_control.types.owner_override.deserialize_xml(child_owner)
    else:
        import typing

        out["owner"] = typing.cast(
            "capo_s3_control.types.owner_override.OwnerOverride", ""
        )
    return out
