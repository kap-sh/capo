"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#InsufficientPrivilegesException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element
from capo_elastic_beanstalk.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.exception_message


class InsufficientPrivilegesException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_beanstalk.types.exception_message.ExceptionMessage"
    ]
    """<p>The exception error message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InsufficientPrivilegesException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InsufficientPrivilegesException_:
    out: InsufficientPrivilegesException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InsufficientPrivilegesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticbeanstalk#InsufficientPrivilegesException``."""

    code: str | None = "InsufficientPrivilegesException"

    def __init__(
        self,
        data: InsufficientPrivilegesException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientPrivilegesException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InsufficientPrivilegesException":
        return cls(deserialize_query(el), message, response=response)
