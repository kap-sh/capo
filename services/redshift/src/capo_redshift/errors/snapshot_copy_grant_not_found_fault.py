"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotCopyGrantNotFoundFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift.types.exception_message


class SnapshotCopyGrantNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotCopyGrantNotFoundFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> SnapshotCopyGrantNotFoundFault_:
    out: SnapshotCopyGrantNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SnapshotCopyGrantNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#SnapshotCopyGrantNotFoundFault``."""

    code: str | None = "SnapshotCopyGrantNotFoundFault"

    def __init__(
        self,
        data: SnapshotCopyGrantNotFoundFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapshotCopyGrantNotFoundFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "SnapshotCopyGrantNotFoundFault":
        return cls(deserialize_query(el), message, response=response)
