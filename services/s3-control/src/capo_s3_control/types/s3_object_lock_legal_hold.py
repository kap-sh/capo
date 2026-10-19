"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockLegalHold``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_object_lock_legal_hold_status


class S3ObjectLockLegalHold(TypedDict, closed=True):
    status: "capo_s3_control.types.s3_object_lock_legal_hold_status.S3ObjectLockLegalHoldStatus"
    """<p>The Object Lock legal hold status to be applied to all objects in the Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3ObjectLockLegalHold, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.s3_object_lock_legal_hold_status

    capo_s3_control.types.s3_object_lock_legal_hold_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> S3ObjectLockLegalHold:
    out: S3ObjectLockLegalHold = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3_control.types.s3_object_lock_legal_hold_status

        out["status"] = (
            capo_s3_control.types.s3_object_lock_legal_hold_status.deserialize_xml(
                child_status
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3_control.types.s3_object_lock_legal_hold_status.S3ObjectLockLegalHoldStatus",
            "",
        )
    return out
