"""Generated from Smithy shape ``com.amazonaws.route53resolver#InvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_route53resolver.types.exception_message
    import capo_route53resolver.types.string


class InvalidParameterException_(TypedDict, closed=True):
    message: "capo_route53resolver.types.exception_message.ExceptionMessage"
    field_name: NotRequired["capo_route53resolver.types.string.String"]
    """<p>For an <code>InvalidParameterException</code> error, the name of the parameter that's invalid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InvalidParameterException_.message required")
    if data.get("FieldName") is not None:
        out["field_name"] = data["FieldName"]
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53resolver#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(
        self,
        data: InvalidParameterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParameterException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
