"""Generated from Smithy shape ``com.amazonaws.dataexchange#ServiceLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_dataexchange.types.__double
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.limit_name


class ServiceLimitExceededException_(TypedDict, closed=True):
    limit_name: NotRequired["capo_dataexchange.types.limit_name.LimitName"]
    """<p>The name of the limit that was reached.</p>"""
    limit_value: "capo_dataexchange.types.__double.__double"
    """<p>The value of the exceeded limit.</p>"""
    message: "capo_dataexchange.types.__string.__string"
    """<p>The request has exceeded the quotas imposed by the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLimitExceededException_) -> dict:
    out: dict = {}
    if "limit_name" in value:
        out["LimitName"] = value["limit_name"]
    out["LimitValue"] = (
        "NaN"
        if value.get("limit_value", 0) != value.get("limit_value", 0)
        else "Infinity"
        if value.get("limit_value", 0) == float("inf")
        else "-Infinity"
        if value.get("limit_value", 0) == float("-inf")
        else value.get("limit_value", 0)
    )
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceLimitExceededException_:
    out: ServiceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("LimitName") is not None:
        out["limit_name"] = data["LimitName"]
    if data.get("LimitValue") is not None:
        out["limit_value"] = float(data["LimitValue"])
    else:
        out["limit_value"] = 0
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ServiceLimitExceededException_.message required")
    return out


class ServiceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dataexchange#ServiceLimitExceededException``."""

    code: str | None = "ServiceLimitExceededException"

    def __init__(
        self,
        data: ServiceLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
