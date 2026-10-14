"""Generated from Smithy shape ``com.amazonaws.cloudsearch#InternalException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudsearch.types.error_code
    import capo_cloudsearch.types.error_message


class InternalException_(TypedDict, closed=True):
    code: NotRequired["capo_cloudsearch.types.error_code.ErrorCode"]
    message: NotRequired["capo_cloudsearch.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InternalException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        pairs.append((f"{key_prefix}Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> InternalException_:
    out: InternalException_ = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudsearch#InternalException``."""

    code: str | None = "InternalException"

    def __init__(
        self,
        data: InternalException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InternalException":
        return cls(deserialize_query(el), message, response=response)
