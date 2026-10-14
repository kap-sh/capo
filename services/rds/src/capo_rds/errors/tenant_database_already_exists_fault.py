"""Generated from Smithy shape ``com.amazonaws.rds#TenantDatabaseAlreadyExistsFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class TenantDatabaseAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TenantDatabaseAlreadyExistsFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> TenantDatabaseAlreadyExistsFault_:
    out: TenantDatabaseAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TenantDatabaseAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#TenantDatabaseAlreadyExistsFault``."""

    code: str | None = "TenantDatabaseAlreadyExistsFault"

    def __init__(
        self,
        data: TenantDatabaseAlreadyExistsFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TenantDatabaseAlreadyExistsFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "TenantDatabaseAlreadyExistsFault":
        return cls(deserialize_query(el), message, response=response)
