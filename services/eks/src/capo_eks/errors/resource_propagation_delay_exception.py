"""Generated from Smithy shape ``com.amazonaws.eks#ResourcePropagationDelayException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import ServiceError

if TYPE_CHECKING:
    import capo_eks.types.string


class ResourcePropagationDelayException_(TypedDict, closed=True):
    message: NotRequired["capo_eks.types.string.String"]
    """<p>Required resources (such as service-linked roles) were created and are still propagating. Retry later.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePropagationDelayException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourcePropagationDelayException_:
    out: ResourcePropagationDelayException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourcePropagationDelayException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#ResourcePropagationDelayException``."""

    code: str | None = "ResourcePropagationDelayException"

    def __init__(
        self,
        data: ResourcePropagationDelayException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourcePropagationDelayException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourcePropagationDelayException":
        return cls(deserialize_json(data), message, response=response)
