"""Generated from Smithy shape ``com.amazonaws.securityir#CaseAttachmentsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.case_attachment_attributes

CaseAttachmentsList: TypeAlias = list[
    "capo_security_ir.types.case_attachment_attributes.CaseAttachmentAttributes"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaseAttachmentsList) -> list:
    import capo_security_ir.types.case_attachment_attributes

    out: list = []
    for item in value:
        out.append(
            capo_security_ir.types.case_attachment_attributes.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CaseAttachmentsList:
    import capo_security_ir.types.case_attachment_attributes

    out: CaseAttachmentsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_security_ir.types.case_attachment_attributes.deserialize_json(item)
        )
    return out


def redact_sensitive(value: CaseAttachmentsList) -> list[Any]:
    import capo_security_ir.types.case_attachment_attributes

    return [
        capo_security_ir.types.case_attachment_attributes.redact_sensitive(item)
        for item in value
    ]
