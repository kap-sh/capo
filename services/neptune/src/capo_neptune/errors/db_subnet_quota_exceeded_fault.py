"""Generated from Smithy shape ``com.amazonaws.neptune#DBSubnetQuotaExceededFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element
from capo_neptune.errors import ServiceError

if TYPE_CHECKING:
    import capo_neptune.types.exception_message


class DBSubnetQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["capo_neptune.types.exception_message.ExceptionMessage"]
    """<p>A message describing the details of the problem.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetQuotaExceededFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> DBSubnetQuotaExceededFault_:
    out: DBSubnetQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBSubnetQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptune#DBSubnetQuotaExceededFault``."""

    code: str | None = "DBSubnetQuotaExceededFault"

    def __init__(
        self,
        data: DBSubnetQuotaExceededFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBSubnetQuotaExceededFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "DBSubnetQuotaExceededFault":
        return cls(deserialize_query(el), message, response=response)
