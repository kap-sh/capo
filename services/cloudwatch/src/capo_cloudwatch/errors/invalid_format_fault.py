"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InvalidFormatFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element
from capo_cloudwatch.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch.types.error_message


class InvalidFormatFault_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch.types.error_message.ErrorMessage"]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidFormatFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidFormatFault_:
    out: InvalidFormatFault_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidFormatFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidFormatFault_:
    out: InvalidFormatFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidFormatFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatch#InvalidFormatFault``."""

    code: str | None = "InvalidFormatFault"

    def __init__(
        self,
        data: InvalidFormatFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFormatFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidFormatFault":
        return cls(deserialize_aws_json_1_0(data), message, response=response)

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidFormatFault":
        return cls(deserialize_query(el), message, response=response)
