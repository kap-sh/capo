"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemInvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_parameter_names_list
    import capo_ssm.types.string


class OpsItemInvalidParameterException_(TypedDict, closed=True):
    parameter_names: NotRequired[
        "capo_ssm.types.ops_item_parameter_names_list.OpsItemParameterNamesList"
    ]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemInvalidParameterException_) -> dict:
    out: dict = {}
    if "parameter_names" in value:
        import capo_ssm.types.ops_item_parameter_names_list

        out["ParameterNames"] = (
            capo_ssm.types.ops_item_parameter_names_list.serialize_aws_json_1_1(
                value["parameter_names"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemInvalidParameterException_:
    out: OpsItemInvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("ParameterNames") is not None:
        import capo_ssm.types.ops_item_parameter_names_list

        out["parameter_names"] = (
            capo_ssm.types.ops_item_parameter_names_list.deserialize_aws_json_1_1(
                data["ParameterNames"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class OpsItemInvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemInvalidParameterException``."""

    code: str | None = "OpsItemInvalidParameterException"

    def __init__(
        self,
        data: OpsItemInvalidParameterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemInvalidParameterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OpsItemInvalidParameterException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
