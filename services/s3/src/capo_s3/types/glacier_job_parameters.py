"""Generated from Smithy shape ``com.amazonaws.s3#GlacierJobParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.tier


class GlacierJobParameters(TypedDict, closed=True):
    tier: "capo_s3.types.tier.Tier"
    """<p>Retrieval tier at which the restore will be processed.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GlacierJobParameters, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.tier

    capo_s3.types.tier.serialize_xml(value["tier"], el, "Tier")


def deserialize_xml(el: Element) -> GlacierJobParameters:
    out: GlacierJobParameters = {}  # type: ignore[typeddict-item]
    child_tier = el.find("Tier")
    if child_tier is not None:
        import capo_s3.types.tier

        out["tier"] = capo_s3.types.tier.deserialize_xml(child_tier)
    else:
        import typing

        out["tier"] = typing.cast("capo_s3.types.tier.Tier", "")
    return out
