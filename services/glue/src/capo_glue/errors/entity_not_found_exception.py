"""Generated from Smithy shape ``com.amazonaws.glue#EntityNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string
    import capo_glue.types.nullable_boolean


class EntityNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""
    from_federation_source: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether or not the exception relates to a federated source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "from_federation_source" in value:
        out["FromFederationSource"] = value["from_federation_source"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityNotFoundException_:
    out: EntityNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("FromFederationSource") is not None:
        out["from_federation_source"] = data["FromFederationSource"]
    return out


class EntityNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#EntityNotFoundException``."""

    code: str | None = "EntityNotFoundException"

    def __init__(
        self,
        data: EntityNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntityNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EntityNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
