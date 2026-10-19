"""Generated from Smithy shape ``com.amazonaws.s3#RequestPaymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.payer


class RequestPaymentConfiguration(TypedDict, closed=True):
    payer: "capo_s3.types.payer.Payer"
    """<p>Specifies who pays for the download and request fees.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: RequestPaymentConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.payer

    capo_s3.types.payer.serialize_xml(value["payer"], el, "Payer")


def deserialize_xml(el: Element) -> RequestPaymentConfiguration:
    out: RequestPaymentConfiguration = {}  # type: ignore[typeddict-item]
    child_payer = el.find("Payer")
    if child_payer is not None:
        import capo_s3.types.payer

        out["payer"] = capo_s3.types.payer.deserialize_xml(child_payer)
    else:
        import typing

        out["payer"] = typing.cast("capo_s3.types.payer.Payer", "")
    return out
