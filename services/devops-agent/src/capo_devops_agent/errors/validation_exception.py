"""Generated from Smithy shape ``com.amazonaws.devopsagent#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_devops_agent.types.validation_exception_field_list


class ValidationException_(TypedDict, closed=True):
    message: "str"
    """<p>A summary of the validation failure.</p>"""
    field_list: NotRequired[
        "capo_devops_agent.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "field_list" in value:
        import capo_devops_agent.types.validation_exception_field_list

        out["fieldList"] = (
            capo_devops_agent.types.validation_exception_field_list.serialize_json(
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
    if data.get("fieldList") is not None:
        import capo_devops_agent.types.validation_exception_field_list

        out["field_list"] = (
            capo_devops_agent.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsagent#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_json(data), message, response=response)
