"""Generated from Smithy shape ``com.amazonaws.connect#PropertyValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_connect.types.message
    import capo_connect.types.property_validation_exception_property_list


class PropertyValidationException_(TypedDict, closed=True):
    message: "capo_connect.types.message.Message"
    property_list: NotRequired[
        "capo_connect.types.property_validation_exception_property_list.PropertyValidationExceptionPropertyList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "property_list" in value:
        import capo_connect.types.property_validation_exception_property_list

        out["PropertyList"] = (
            capo_connect.types.property_validation_exception_property_list.serialize_json(
                value["property_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> PropertyValidationException_:
    out: PropertyValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("PropertyValidationException_.message required")
    if data.get("PropertyList") is not None:
        import capo_connect.types.property_validation_exception_property_list

        out["property_list"] = (
            capo_connect.types.property_validation_exception_property_list.deserialize_json(
                data["PropertyList"]
            )
        )
    return out


class PropertyValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#PropertyValidationException``."""

    code: str | None = "PropertyValidationException"

    def __init__(
        self,
        data: PropertyValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PropertyValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PropertyValidationException":
        return cls(deserialize_json(data), message, response=response)
