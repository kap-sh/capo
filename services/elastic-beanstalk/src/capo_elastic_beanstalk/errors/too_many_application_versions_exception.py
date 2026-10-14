"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#TooManyApplicationVersionsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element
from capo_elastic_beanstalk.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.exception_message


class TooManyApplicationVersionsException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_beanstalk.types.exception_message.ExceptionMessage"
    ]
    """<p>The exception error message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TooManyApplicationVersionsException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> TooManyApplicationVersionsException_:
    out: TooManyApplicationVersionsException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyApplicationVersionsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticbeanstalk#TooManyApplicationVersionsException``."""

    code: str | None = "TooManyApplicationVersionsException"

    def __init__(
        self,
        data: TooManyApplicationVersionsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyApplicationVersionsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyApplicationVersionsException":
        return cls(deserialize_query(el), message, response=response)
