"""Generated from Smithy shape ``com.amazonaws.ssm#ResourcePolicyInvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.resource_policy_parameter_names_list
    import capo_ssm.types.string


class ResourcePolicyInvalidParameterException_(TypedDict, closed=True):
    parameter_names: NotRequired[
        "capo_ssm.types.resource_policy_parameter_names_list.ResourcePolicyParameterNamesList"
    ]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicyInvalidParameterException_) -> dict:
    out: dict = {}
    if "parameter_names" in value:
        import capo_ssm.types.resource_policy_parameter_names_list

        out["ParameterNames"] = (
            capo_ssm.types.resource_policy_parameter_names_list.serialize_aws_json_1_1(
                value["parameter_names"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePolicyInvalidParameterException_:
    out: ResourcePolicyInvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("ParameterNames") is not None:
        import capo_ssm.types.resource_policy_parameter_names_list

        out["parameter_names"] = (
            capo_ssm.types.resource_policy_parameter_names_list.deserialize_aws_json_1_1(
                data["ParameterNames"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourcePolicyInvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourcePolicyInvalidParameterException``."""

    code: str | None = "ResourcePolicyInvalidParameterException"

    def __init__(
        self,
        data: ResourcePolicyInvalidParameterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourcePolicyInvalidParameterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourcePolicyInvalidParameterException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
