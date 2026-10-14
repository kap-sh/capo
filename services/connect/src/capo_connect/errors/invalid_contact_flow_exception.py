"""Generated from Smithy shape ``com.amazonaws.connect#InvalidContactFlowException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.problems


class InvalidContactFlowException_(TypedDict, closed=True):
    problems: NotRequired["capo_connect.types.problems.Problems"]
    """<p>The problems with the flow. Please fix before trying again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidContactFlowException_) -> dict:
    out: dict = {}
    if "problems" in value:
        import capo_connect.types.problems

        out["problems"] = capo_connect.types.problems.serialize_json(value["problems"])
    return out


def deserialize_json(data: dict) -> InvalidContactFlowException_:
    out: InvalidContactFlowException_ = {}  # type: ignore[typeddict-item]
    if data.get("problems") is not None:
        import capo_connect.types.problems

        out["problems"] = capo_connect.types.problems.deserialize_json(data["problems"])
    return out


class InvalidContactFlowException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#InvalidContactFlowException``."""

    code: str | None = "InvalidContactFlowException"

    def __init__(
        self,
        data: InvalidContactFlowException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidContactFlowException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidContactFlowException":
        return cls(deserialize_json(data), message, response=response)
