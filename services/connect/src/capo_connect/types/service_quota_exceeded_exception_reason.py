"""Generated from Smithy shape ``com.amazonaws.connect#ServiceQuotaExceededExceptionReason``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.attached_file_service_quota_exceeded_exception_reason


class _ServiceQuotaExceededExceptionReason_AttachedFileServiceQuotaExceededExceptionReason(
    TypedDict, closed=True
):
    AttachedFileServiceQuotaExceededExceptionReason: "capo_connect.types.attached_file_service_quota_exceeded_exception_reason.AttachedFileServiceQuotaExceededExceptionReason"


ServiceQuotaExceededExceptionReason: TypeAlias = (
    _ServiceQuotaExceededExceptionReason_AttachedFileServiceQuotaExceededExceptionReason
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededExceptionReason) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ServiceQuotaExceededExceptionReason: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AttachedFileServiceQuotaExceededExceptionReason" in value:
        import capo_connect.types.attached_file_service_quota_exceeded_exception_reason

        return {
            "AttachedFileServiceQuotaExceededExceptionReason": capo_connect.types.attached_file_service_quota_exceeded_exception_reason.serialize_json(
                value["AttachedFileServiceQuotaExceededExceptionReason"]
            )
        }
    else:
        raise SerializationError(
            "ServiceQuotaExceededExceptionReason: no variant present"
        )


def deserialize_json(data: dict) -> ServiceQuotaExceededExceptionReason:
    if data.get("AttachedFileServiceQuotaExceededExceptionReason") is not None:
        import capo_connect.types.attached_file_service_quota_exceeded_exception_reason

        return {
            "AttachedFileServiceQuotaExceededExceptionReason": capo_connect.types.attached_file_service_quota_exceeded_exception_reason.deserialize_json(
                data["AttachedFileServiceQuotaExceededExceptionReason"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ServiceQuotaExceededExceptionReason: no recognized variant key"
        )
