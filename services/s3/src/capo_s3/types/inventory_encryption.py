"""Generated from Smithy shape ``com.amazonaws.s3#InventoryEncryption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.ssekms
    import capo_s3.types.sses3


class InventoryEncryption(TypedDict, closed=True):
    sses3: NotRequired["capo_s3.types.sses3.SSES3"]
    """<p>Specifies the use of SSE-S3 to encrypt delivered inventory reports.</p>"""
    ssekms: NotRequired["capo_s3.types.ssekms.SSEKMS"]
    """<p>Specifies the use of SSE-KMS to encrypt delivered inventory reports.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InventoryEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "sses3" in value:
        import capo_s3.types.sses3

        capo_s3.types.sses3.serialize_xml(value["sses3"], el, "SSE-S3")
    if "ssekms" in value:
        import capo_s3.types.ssekms

        capo_s3.types.ssekms.serialize_xml(value["ssekms"], el, "SSE-KMS")


def deserialize_xml(el: Element) -> InventoryEncryption:
    out: InventoryEncryption = {}  # type: ignore[typeddict-item]
    child_sses3 = el.find("SSE-S3")
    if child_sses3 is not None:
        import capo_s3.types.sses3

        out["sses3"] = capo_s3.types.sses3.deserialize_xml(child_sses3)
    child_ssekms = el.find("SSE-KMS")
    if child_ssekms is not None:
        import capo_s3.types.ssekms

        out["ssekms"] = capo_s3.types.ssekms.deserialize_xml(child_ssekms)
    return out


def redact_sensitive(value: InventoryEncryption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ssekms" in value:
        import capo_s3.types.ssekms

        out["ssekms"] = capo_s3.types.ssekms.redact_sensitive(value["ssekms"])
    return out
