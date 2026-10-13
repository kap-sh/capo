"""Generated from Smithy shape ``com.amazonaws.s3#SSEKMS``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.ssekms_key_id


class SSEKMS(TypedDict, closed=True):
    key_id: "capo_s3.types.ssekms_key_id.SSEKMSKeyId"
    """<p>Specifies the ID of the Key Management Service (KMS) symmetric encryption customer managed key to use for encrypting inventory reports.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SSEKMS, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "KeyId").text = str(value["key_id"])


def deserialize_xml(el: Element) -> SSEKMS:
    out: SSEKMS = {}  # type: ignore[typeddict-item]
    child_key_id = el.find("KeyId")
    if child_key_id is not None:
        out["key_id"] = str(child_key_id.text or "")
    else:
        raise DeserializationError("SSEKMS.key_id required")
    return out


def redact_sensitive(value: SSEKMS) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_id" in value:
        out["key_id"] = "*** Sensitive Data Redacted ***"
    return out
