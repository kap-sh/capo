"""Generated from Smithy shape ``com.amazonaws.s3control#SseKmsEncryptedObjects``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.sse_kms_encrypted_objects_status


class SseKmsEncryptedObjects(TypedDict, closed=True):
    status: "capo_s3_control.types.sse_kms_encrypted_objects_status.SseKmsEncryptedObjectsStatus"
    """<p>Specifies whether Amazon S3 replicates objects that are created with server-side encryption by using an KMS key stored in Key Management Service.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SseKmsEncryptedObjects, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.sse_kms_encrypted_objects_status

    capo_s3_control.types.sse_kms_encrypted_objects_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> SseKmsEncryptedObjects:
    out: SseKmsEncryptedObjects = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3_control.types.sse_kms_encrypted_objects_status

        out["status"] = (
            capo_s3_control.types.sse_kms_encrypted_objects_status.deserialize_xml(
                child_status
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3_control.types.sse_kms_encrypted_objects_status.SseKmsEncryptedObjectsStatus",
            "",
        )
    return out
