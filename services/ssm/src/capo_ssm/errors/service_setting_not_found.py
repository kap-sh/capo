"""Generated from Smithy shape ``com.amazonaws.ssm#ServiceSettingNotFound``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ServiceSettingNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceSettingNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceSettingNotFound_:
    out: ServiceSettingNotFound_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ServiceSettingNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ServiceSettingNotFound``."""

    code: str | None = "ServiceSettingNotFound"

    def __init__(
        self,
        data: ServiceSettingNotFound_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceSettingNotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceSettingNotFound":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
