"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationAllFeaturesNotEnabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_config_service.types.error_message


class OrganizationAllFeaturesNotEnabledException_(TypedDict, closed=True):
    message: NotRequired["capo_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationAllFeaturesNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationAllFeaturesNotEnabledException_:
    out: OrganizationAllFeaturesNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class OrganizationAllFeaturesNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#OrganizationAllFeaturesNotEnabledException``."""

    code: str | None = "OrganizationAllFeaturesNotEnabledException"

    def __init__(
        self,
        data: OrganizationAllFeaturesNotEnabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OrganizationAllFeaturesNotEnabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OrganizationAllFeaturesNotEnabledException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
