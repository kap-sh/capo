"""Generated from Smithy shape ``com.amazonaws.securityir#CaseAttachmentAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.attachment_id
    import capo_security_ir.types.case_attachment_status
    import capo_security_ir.types.file_name
    import capo_security_ir.types.principal_id


class CaseAttachmentAttributes(TypedDict, closed=True):
    attachment_id: "capo_security_ir.types.attachment_id.AttachmentId"
    """<p/>"""
    file_name: "capo_security_ir.types.file_name.FileName"
    """<p/>"""
    attachment_status: (
        "capo_security_ir.types.case_attachment_status.CaseAttachmentStatus"
    )
    """<p/>"""
    creator: "capo_security_ir.types.principal_id.PrincipalId"
    """<p/>"""
    created_date: "datetime.datetime"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseAttachmentAttributes) -> dict:
    out: dict = {}
    out["attachmentId"] = value["attachment_id"]
    out["fileName"] = value["file_name"]
    import capo_security_ir.types.case_attachment_status

    out["attachmentStatus"] = (
        capo_security_ir.types.case_attachment_status.serialize_json(
            value["attachment_status"]
        )
    )
    out["creator"] = value["creator"]
    import capo_security_ir.types._prelude.timestamp

    out["createdDate"] = capo_security_ir.types._prelude.timestamp.serialize_json(
        value["created_date"]
    )
    return out


def deserialize_json(data: dict) -> CaseAttachmentAttributes:
    out: CaseAttachmentAttributes = {}  # type: ignore[typeddict-item]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    else:
        raise DeserializationError("CaseAttachmentAttributes.attachment_id required")
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("CaseAttachmentAttributes.file_name required")
    if data.get("attachmentStatus") is not None:
        import capo_security_ir.types.case_attachment_status

        out["attachment_status"] = (
            capo_security_ir.types.case_attachment_status.deserialize_json(
                data["attachmentStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CaseAttachmentAttributes.attachment_status required"
        )
    if data.get("creator") is not None:
        out["creator"] = data["creator"]
    else:
        raise DeserializationError("CaseAttachmentAttributes.creator required")
    if data.get("createdDate") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["created_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("CaseAttachmentAttributes.created_date required")
    return out


def redact_sensitive(value: CaseAttachmentAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_name" in value:
        out["file_name"] = "*** Sensitive Data Redacted ***"
    return out
