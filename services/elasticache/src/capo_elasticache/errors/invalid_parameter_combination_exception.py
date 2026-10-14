"""Generated from Smithy shape ``com.amazonaws.elasticache#InvalidParameterCombinationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element
from capo_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticache.types.aws_query_error_message


class InvalidParameterCombinationException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elasticache.types.aws_query_error_message.AwsQueryErrorMessage"
    ]
    """<p>Two or more parameters that must not be used together were used together.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidParameterCombinationException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidParameterCombinationException_:
    out: InvalidParameterCombinationException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidParameterCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#InvalidParameterCombinationException``."""

    code: str | None = "InvalidParameterCombinationException"

    def __init__(
        self,
        data: InvalidParameterCombinationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterCombinationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParameterCombinationException":
        return cls(deserialize_query(el), message, response=response)
