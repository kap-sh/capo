"""Generated from Smithy shape ``com.amazonaws.s3#CORSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.cors_rules


class CORSConfiguration(TypedDict, closed=True):
    cors_rules: "capo_s3.types.cors_rules.CORSRules"
    """<p>A set of origins and methods (cross-origin access that you want to allow). You can add up to 100 rules to the configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CORSConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.cors_rules

    capo_s3.types.cors_rules.serialize_xml_flat(value["cors_rules"], el, "CORSRule")


def deserialize_xml(el: Element) -> CORSConfiguration:
    out: CORSConfiguration = {}  # type: ignore[typeddict-item]
    if el.find("CORSRule") is not None:
        import capo_s3.types.cors_rules

        out["cors_rules"] = capo_s3.types.cors_rules.deserialize_xml_flat(
            el, "CORSRule"
        )
    else:
        out["cors_rules"] = []
    return out
