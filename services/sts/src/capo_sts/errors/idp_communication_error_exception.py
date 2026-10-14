"""Generated from Smithy shape ``com.amazonaws.sts#IDPCommunicationErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import ServiceError

if TYPE_CHECKING:
    import capo_sts.types.idp_communication_error_message


class IDPCommunicationErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_sts.types.idp_communication_error_message.idpCommunicationErrorMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: IDPCommunicationErrorException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> IDPCommunicationErrorException_:
    out: IDPCommunicationErrorException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class IDPCommunicationErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#IDPCommunicationErrorException``."""

    code: str | None = "IDPCommunicationErrorException"

    def __init__(
        self,
        data: IDPCommunicationErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IDPCommunicationErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "IDPCommunicationErrorException":
        return cls(deserialize_query(el), message, response=response)
