"""Generated from Smithy shape ``com.amazonaws.connect#InvalidTestCaseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.problems


class InvalidTestCaseException_(TypedDict, closed=True):
    problems: NotRequired["capo_connect.types.problems.Problems"]
    """<p>The problems with the test. Please fix before trying again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidTestCaseException_) -> dict:
    out: dict = {}
    if "problems" in value:
        import capo_connect.types.problems

        out["Problems"] = capo_connect.types.problems.serialize_json(value["problems"])
    return out


def deserialize_json(data: dict) -> InvalidTestCaseException_:
    out: InvalidTestCaseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Problems") is not None:
        import capo_connect.types.problems

        out["problems"] = capo_connect.types.problems.deserialize_json(data["Problems"])
    return out


class InvalidTestCaseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#InvalidTestCaseException``."""

    code: str | None = "InvalidTestCaseException"

    def __init__(
        self,
        data: InvalidTestCaseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTestCaseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidTestCaseException":
        return cls(deserialize_json(data), message, response=response)
