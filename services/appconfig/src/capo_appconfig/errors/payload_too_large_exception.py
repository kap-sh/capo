"""Generated from Smithy shape ``com.amazonaws.appconfig#PayloadTooLargeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appconfig.errors import ServiceError

if TYPE_CHECKING:
    import capo_appconfig.types.bytes_measure
    import capo_appconfig.types.float
    import capo_appconfig.types.string


class PayloadTooLargeException_(TypedDict, closed=True):
    message: NotRequired["capo_appconfig.types.string.String"]
    measure: NotRequired["capo_appconfig.types.bytes_measure.BytesMeasure"]
    limit: "capo_appconfig.types.float.Float"
    size: "capo_appconfig.types.float.Float"


# --- restJson1 ser/de ---
def serialize_json(value: PayloadTooLargeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "measure" in value:
        import capo_appconfig.types.bytes_measure

        out["Measure"] = capo_appconfig.types.bytes_measure.serialize_json(
            value["measure"]
        )
    out["Limit"] = (
        "NaN"
        if value.get("limit", 0) != value.get("limit", 0)
        else "Infinity"
        if value.get("limit", 0) == float("inf")
        else "-Infinity"
        if value.get("limit", 0) == float("-inf")
        else value.get("limit", 0)
    )
    out["Size"] = (
        "NaN"
        if value.get("size", 0) != value.get("size", 0)
        else "Infinity"
        if value.get("size", 0) == float("inf")
        else "-Infinity"
        if value.get("size", 0) == float("-inf")
        else value.get("size", 0)
    )
    return out


def deserialize_json(data: dict) -> PayloadTooLargeException_:
    out: PayloadTooLargeException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Measure") is not None:
        import capo_appconfig.types.bytes_measure

        out["measure"] = capo_appconfig.types.bytes_measure.deserialize_json(
            data["Measure"]
        )
    if data.get("Limit") is not None:
        out["limit"] = float(data["Limit"])
    else:
        out["limit"] = 0
    if data.get("Size") is not None:
        out["size"] = float(data["Size"])
    else:
        out["size"] = 0
    return out


class PayloadTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appconfig#PayloadTooLargeException``."""

    code: str | None = "PayloadTooLargeException"

    def __init__(
        self,
        data: PayloadTooLargeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PayloadTooLargeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PayloadTooLargeException":
        return cls(deserialize_json(data), message, response=response)
