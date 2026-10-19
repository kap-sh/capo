"""Generated from Smithy shape ``com.amazonaws.s3#ObjectEncryption``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError, SerializationError
from capo_s3.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3.types.ssekms_encryption


class _ObjectEncryption_SSEKMS(TypedDict, closed=True):
    SSEKMS: "capo_s3.types.ssekms_encryption.SSEKMSEncryption"


ObjectEncryption: TypeAlias = _ObjectEncryption_SSEKMS | UnknownUnionMember


# --- restXml ser/de ---
def serialize_xml(value: ObjectEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ObjectEncryption: cannot serialize unknown variant {value.name!r}"
        )
    elif "SSEKMS" in value:
        import capo_s3.types.ssekms_encryption

        capo_s3.types.ssekms_encryption.serialize_xml(value["SSEKMS"], el, "SSE-KMS")
    else:
        raise SerializationError("ObjectEncryption: no variant present")


def deserialize_xml(el: Element) -> ObjectEncryption:
    for child in el:
        if child.tag == "SSE-KMS":
            import capo_s3.types.ssekms_encryption

            return {"SSEKMS": capo_s3.types.ssekms_encryption.deserialize_xml(child)}
        else:
            return UnknownUnionMember(child.tag)
    raise DeserializationError("ObjectEncryption: no recognized variant element")


def redact_sensitive(value: ObjectEncryption) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "SSEKMS" in value:
        import capo_s3.types.ssekms_encryption

        out["SSEKMS"] = capo_s3.types.ssekms_encryption.redact_sensitive(
            value["SSEKMS"]
        )
    return out
