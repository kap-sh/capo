"""Generated from Smithy shape ``com.amazonaws.glue#FederationSourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.federation_source_error_code
    import capo_glue.types.message_string


class FederationSourceException_(TypedDict, closed=True):
    federation_source_error_code: NotRequired[
        "capo_glue.types.federation_source_error_code.FederationSourceErrorCode"
    ]
    """<p>The error code of the problem.</p>"""
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>The message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederationSourceException_) -> dict:
    out: dict = {}
    if "federation_source_error_code" in value:
        import capo_glue.types.federation_source_error_code

        out["FederationSourceErrorCode"] = (
            capo_glue.types.federation_source_error_code.serialize_aws_json_1_1(
                value["federation_source_error_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederationSourceException_:
    out: FederationSourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("FederationSourceErrorCode") is not None:
        import capo_glue.types.federation_source_error_code

        out["federation_source_error_code"] = (
            capo_glue.types.federation_source_error_code.deserialize_aws_json_1_1(
                data["FederationSourceErrorCode"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class FederationSourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#FederationSourceException``."""

    code: str | None = "FederationSourceException"

    def __init__(
        self,
        data: FederationSourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FederationSourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FederationSourceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
