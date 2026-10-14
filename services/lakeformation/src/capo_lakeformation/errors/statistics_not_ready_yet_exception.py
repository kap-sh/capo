"""Generated from Smithy shape ``com.amazonaws.lakeformation#StatisticsNotReadyYetException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string


class StatisticsNotReadyYetException_(TypedDict, closed=True):
    message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticsNotReadyYetException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StatisticsNotReadyYetException_:
    out: StatisticsNotReadyYetException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class StatisticsNotReadyYetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#StatisticsNotReadyYetException``."""

    code: str | None = "StatisticsNotReadyYetException"

    def __init__(
        self,
        data: StatisticsNotReadyYetException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StatisticsNotReadyYetException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "StatisticsNotReadyYetException":
        return cls(deserialize_json(data), message, response=response)
