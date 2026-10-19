"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DryRunException``."""

import zapros
from typing_extensions import TypedDict

from capo_redshift_serverless.errors import ServiceError


class DryRunException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DryRunException_:
    out: DryRunException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class DryRunException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#DryRunException``."""

    code: str | None = "DryRunException"

    def __init__(
        self,
        data: DryRunException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DryRunException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DryRunException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
