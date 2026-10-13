"""Generated from Smithy shape ``com.amazonaws.rekognition#AuditImages``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.audit_image

AuditImages: TypeAlias = list["capo_rekognition.types.audit_image.AuditImage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuditImages) -> list:
    import capo_rekognition.types.audit_image

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.audit_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AuditImages:
    import capo_rekognition.types.audit_image

    out: AuditImages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_rekognition.types.audit_image.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: AuditImages) -> list[Any]:
    import capo_rekognition.types.audit_image

    return [capo_rekognition.types.audit_image.redact_sensitive(item) for item in value]
