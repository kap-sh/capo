"""Generated from Smithy shape ``com.amazonaws.s3control#SSEKMS``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.ssekms_key_id


class SSEKMS(TypedDict, closed=True):
    key_id: "capo_s3_control.types.ssekms_key_id.SSEKMSKeyId"
    """<p>A container for the ARN of the SSE-KMS encryption. This property is read-only and follows the following format: <code> arn:aws:kms:<i>us-east-1</i>:<i>example-account-id</i>:key/<i>example-9a73-4afc-8d29-8f5900cef44e</i> </code> </p>"""


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
        out["key_id"] = ""
    return out
