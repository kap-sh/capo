"""Generated from Smithy shape ``com.amazonaws.rds#InvalidDBCapacityReservationStateFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element
from capo_rds.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds.types.exception_message


class InvalidDBCapacityReservationStateFault_(TypedDict, closed=True):
    message: NotRequired["capo_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidDBCapacityReservationStateFault_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidDBCapacityReservationStateFault_:
    out: InvalidDBCapacityReservationStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidDBCapacityReservationStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidDBCapacityReservationStateFault``."""

    code: str | None = "InvalidDBCapacityReservationStateFault"

    def __init__(
        self,
        data: InvalidDBCapacityReservationStateFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDBCapacityReservationStateFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidDBCapacityReservationStateFault":
        return cls(deserialize_query(el), message, response=response)
