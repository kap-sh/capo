"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class OpsMetadataNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsMetadataNotFoundException_:
    out: OpsMetadataNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class OpsMetadataNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsMetadataNotFoundException``."""

    code: str | None = "OpsMetadataNotFoundException"

    def __init__(
        self,
        data: OpsMetadataNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsMetadataNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OpsMetadataNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
