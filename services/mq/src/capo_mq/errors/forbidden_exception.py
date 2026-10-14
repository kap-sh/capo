"""Generated from Smithy shape ``com.amazonaws.mq#ForbiddenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mq.errors import ServiceError

if TYPE_CHECKING:
    import capo_mq.types.__list_of_resource_share_error
    import capo_mq.types.__string


class ForbiddenException_(TypedDict, closed=True):
    error_attribute: NotRequired["capo_mq.types.__string.__string"]
    """<p>The attribute which caused the error.</p>"""
    message: NotRequired["capo_mq.types.__string.__string"]
    """<p>The explanation of the error.</p>"""
    resource_share_errors: NotRequired[
        "capo_mq.types.__list_of_resource_share_error.__listOfResourceShareError"
    ]
    """<p>The list of resource share errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenException_) -> dict:
    out: dict = {}
    if "error_attribute" in value:
        out["errorAttribute"] = value["error_attribute"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_share_errors" in value:
        import capo_mq.types.__list_of_resource_share_error

        out["resourceShareErrors"] = (
            capo_mq.types.__list_of_resource_share_error.serialize_json(
                value["resource_share_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    if data.get("errorAttribute") is not None:
        out["error_attribute"] = data["errorAttribute"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceShareErrors") is not None:
        import capo_mq.types.__list_of_resource_share_error

        out["resource_share_errors"] = (
            capo_mq.types.__list_of_resource_share_error.deserialize_json(
                data["resourceShareErrors"]
            )
        )
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mq#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(
        self,
        data: ForbiddenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ForbiddenException":
        return cls(deserialize_json(data), message, response=response)
