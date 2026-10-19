"""Generated from Smithy shape ``com.amazonaws.s3#OwnershipControls``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.ownership_controls_rules


class OwnershipControls(TypedDict, closed=True):
    rules: "capo_s3.types.ownership_controls_rules.OwnershipControlsRules"
    """<p>The container element for an ownership control rule.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OwnershipControls, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.ownership_controls_rules

    capo_s3.types.ownership_controls_rules.serialize_xml_flat(
        value["rules"], el, "Rule"
    )


def deserialize_xml(el: Element) -> OwnershipControls:
    out: OwnershipControls = {}  # type: ignore[typeddict-item]
    if el.find("Rule") is not None:
        import capo_s3.types.ownership_controls_rules

        out["rules"] = capo_s3.types.ownership_controls_rules.deserialize_xml_flat(
            el, "Rule"
        )
    else:
        out["rules"] = []
    return out
