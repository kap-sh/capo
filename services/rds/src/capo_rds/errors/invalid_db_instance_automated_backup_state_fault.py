"""Generated from Smithy shape ``com.amazonaws.rds#InvalidDBInstanceAutomatedBackupStateFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class InvalidDBInstanceAutomatedBackupStateFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidDBInstanceAutomatedBackupStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidDBInstanceAutomatedBackupStateFault_:
    out: InvalidDBInstanceAutomatedBackupStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidDBInstanceAutomatedBackupStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidDBInstanceAutomatedBackupStateFault``."""

    code: str | None = "InvalidDBInstanceAutomatedBackupStateFault"

    def __init__(
        self,
        data: InvalidDBInstanceAutomatedBackupStateFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDBInstanceAutomatedBackupStateFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidDBInstanceAutomatedBackupStateFault":
        return cls(deserialize_query(el), message, response=response)
