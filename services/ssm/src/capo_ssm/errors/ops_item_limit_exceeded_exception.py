"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.integer
    import capo_ssm.types.ops_item_parameter_names_list
    import capo_ssm.types.string


class OpsItemLimitExceededException_(TypedDict, closed=True):
    resource_types: NotRequired[
        "capo_ssm.types.ops_item_parameter_names_list.OpsItemParameterNamesList"
    ]
    limit: "capo_ssm.types.integer.Integer"
    limit_type: NotRequired["capo_ssm.types.string.String"]
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemLimitExceededException_) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import capo_ssm.types.ops_item_parameter_names_list

        out["ResourceTypes"] = (
            capo_ssm.types.ops_item_parameter_names_list.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "limit_type" in value:
        out["LimitType"] = value["limit_type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemLimitExceededException_:
    out: OpsItemLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("ResourceTypes") is not None:
        import capo_ssm.types.ops_item_parameter_names_list

        out["resource_types"] = (
            capo_ssm.types.ops_item_parameter_names_list.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if data.get("LimitType") is not None:
        out["limit_type"] = data["LimitType"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class OpsItemLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemLimitExceededException``."""

    code: str | None = "OpsItemLimitExceededException"

    def __init__(
        self,
        data: OpsItemLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OpsItemLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
