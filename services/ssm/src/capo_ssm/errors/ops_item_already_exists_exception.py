"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class OpsItemAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]
    ops_item_id: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemAlreadyExistsException_:
    out: OpsItemAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    return out


class OpsItemAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemAlreadyExistsException``."""

    code: str | None = "OpsItemAlreadyExistsException"

    def __init__(
        self,
        data: OpsItemAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OpsItemAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
