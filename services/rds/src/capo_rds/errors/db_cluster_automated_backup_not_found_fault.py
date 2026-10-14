"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterAutomatedBackupNotFoundFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class DBClusterAutomatedBackupNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterAutomatedBackupNotFoundFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> DBClusterAutomatedBackupNotFoundFault_:
    out: DBClusterAutomatedBackupNotFoundFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBClusterAutomatedBackupNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#DBClusterAutomatedBackupNotFoundFault``."""

    code: str | None = "DBClusterAutomatedBackupNotFoundFault"

    def __init__(
        self,
        data: DBClusterAutomatedBackupNotFoundFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBClusterAutomatedBackupNotFoundFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "DBClusterAutomatedBackupNotFoundFault":
        return cls(deserialize_query(el), message, response=response)
