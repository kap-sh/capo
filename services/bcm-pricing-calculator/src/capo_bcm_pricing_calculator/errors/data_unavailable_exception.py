"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#DataUnavailableException``."""

import zapros
from typing_extensions import TypedDict

from capo_bcm_pricing_calculator.errors import ServiceError


class DataUnavailableException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataUnavailableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataUnavailableException_:
    out: DataUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class DataUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmpricingcalculator#DataUnavailableException``."""

    code: str | None = "DataUnavailableException"

    def __init__(
        self,
        data: DataUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DataUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DataUnavailableException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
