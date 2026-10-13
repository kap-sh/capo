"""Generated from Smithy shape ``com.amazonaws.taxsettings#ValidationException``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_taxsettings.types.error_message
    import capo_taxsettings.types.validation_exception_error_code
    import capo_taxsettings.types.validation_exception_field_list


class ValidationException_(TypedDict, closed=True):
    message: "capo_taxsettings.types.error_message.ErrorMessage"
    error_code: "capo_taxsettings.types.validation_exception_error_code.ValidationExceptionErrorCode"
    """<p>400</p>"""
    field_list: NotRequired[
        "capo_taxsettings.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>400</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_taxsettings.types.validation_exception_error_code

    out["errorCode"] = (
        capo_taxsettings.types.validation_exception_error_code.serialize_json(
            value["error_code"]
        )
    )
    if "field_list" in value:
        import capo_taxsettings.types.validation_exception_field_list

        out["fieldList"] = (
            capo_taxsettings.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("errorCode") is not None:
        import capo_taxsettings.types.validation_exception_error_code

        out["error_code"] = (
            capo_taxsettings.types.validation_exception_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.error_code required")
    if data.get("fieldList") is not None:
        import capo_taxsettings.types.validation_exception_field_list

        out["field_list"] = (
            capo_taxsettings.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ValidationException":
        return cls(deserialize_json(data), message)


def redact_sensitive(value: ValidationException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
