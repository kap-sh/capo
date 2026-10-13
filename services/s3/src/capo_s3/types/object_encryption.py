"""Generated from Smithy shape ``com.amazonaws.s3#ObjectEncryption``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_s3.types.ssekms_encryption


class _ObjectEncryption_SSEKMS(TypedDict, closed=True):
    SSEKMS: "capo_s3.types.ssekms_encryption.SSEKMSEncryption"


ObjectEncryption: TypeAlias = _ObjectEncryption_SSEKMS


# --- restXml ser/de ---
def serialize_xml(value: ObjectEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "SSEKMS" in value:
        import capo_s3.types.ssekms_encryption

        capo_s3.types.ssekms_encryption.serialize_xml(value["SSEKMS"], el, "SSE-KMS")
    else:
        raise SerializationError("ObjectEncryption: no variant present")


def deserialize_xml(el: Element) -> ObjectEncryption:
    for child in el:
        if child.tag == "SSE-KMS":
            import capo_s3.types.ssekms_encryption

            return {"SSEKMS": capo_s3.types.ssekms_encryption.deserialize_xml(child)}
    raise DeserializationError("ObjectEncryption: no recognized variant element")


def redact_sensitive(value: ObjectEncryption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "SSEKMS" in value:
        import capo_s3.types.ssekms_encryption

        out["SSEKMS"] = capo_s3.types.ssekms_encryption.redact_sensitive(
            value["SSEKMS"]
        )
    return out
