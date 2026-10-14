"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#TooManyTagsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import ServiceError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.amazon_resource_name


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_name: NotRequired[
        "capo_redshift_serverless.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The name of the resource that exceeded the number of tags allowed for a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshiftserverless#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(
        self,
        data: TooManyTagsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyTagsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
