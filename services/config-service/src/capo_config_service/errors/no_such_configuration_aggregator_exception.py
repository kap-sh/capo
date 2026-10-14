"""Generated from Smithy shape ``com.amazonaws.configservice#NoSuchConfigurationAggregatorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class NoSuchConfigurationAggregatorException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchConfigurationAggregatorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoSuchConfigurationAggregatorException_:
    out: NoSuchConfigurationAggregatorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class NoSuchConfigurationAggregatorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoSuchConfigurationAggregatorException``."""

    code: str | None = "NoSuchConfigurationAggregatorException"

    def __init__(
        self,
        data: NoSuchConfigurationAggregatorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchConfigurationAggregatorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoSuchConfigurationAggregatorException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
