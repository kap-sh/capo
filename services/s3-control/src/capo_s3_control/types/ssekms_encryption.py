"""Generated from Smithy shape ``com.amazonaws.s3control#SSEKMSEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.kms_key_arn_string


class SSEKMSEncryption(TypedDict, closed=True):
    key_id: "capo_s3_control.types.kms_key_arn_string.KmsKeyArnString"
    """<p>Specifies the ID of the Amazon Web Services Key Management Service (Amazon Web Services KMS) symmetric encryption customer managed key to use for encrypting generated manifest objects.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SSEKMSEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "KeyId").text = str(value["key_id"])


def deserialize_xml(el: Element) -> SSEKMSEncryption:
    out: SSEKMSEncryption = {}  # type: ignore[typeddict-item]
    child_key_id = el.find("KeyId")
    if child_key_id is not None:
        out["key_id"] = str(child_key_id.text or "")
    else:
        out["key_id"] = ""
    return out
