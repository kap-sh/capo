"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidSignalsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.invalid_signals
    import capo_iotfleetwise.types.string


class InvalidSignalsException_(TypedDict, closed=True):
    message: NotRequired["capo_iotfleetwise.types.string.string"]
    invalid_signals: NotRequired[
        "capo_iotfleetwise.types.invalid_signals.InvalidSignals"
    ]
    """<p>The signals which caused the exception.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidSignalsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "invalid_signals" in value:
        import capo_iotfleetwise.types.invalid_signals

        out["invalidSignals"] = (
            capo_iotfleetwise.types.invalid_signals.serialize_aws_json_1_0(
                value["invalid_signals"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidSignalsException_:
    out: InvalidSignalsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("invalidSignals") is not None:
        import capo_iotfleetwise.types.invalid_signals

        out["invalid_signals"] = (
            capo_iotfleetwise.types.invalid_signals.deserialize_aws_json_1_0(
                data["invalidSignals"]
            )
        )
    return out


class InvalidSignalsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#InvalidSignalsException``."""

    code: str | None = "InvalidSignalsException"

    def __init__(
        self,
        data: InvalidSignalsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSignalsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidSignalsException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
