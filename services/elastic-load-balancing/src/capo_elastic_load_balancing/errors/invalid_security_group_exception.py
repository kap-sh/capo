"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#InvalidSecurityGroupException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element
from capo_elastic_load_balancing.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.error_description


class InvalidSecurityGroupException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_load_balancing.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidSecurityGroupException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidSecurityGroupException_:
    out: InvalidSecurityGroupException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidSecurityGroupException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancing#InvalidSecurityGroupException``."""

    code: str | None = "InvalidSecurityGroupException"

    def __init__(
        self,
        data: InvalidSecurityGroupException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSecurityGroupException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidSecurityGroupException":
        return cls(deserialize_query(el), message, response=response)
