"""Generated from Smithy shape ``com.amazonaws.detective#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_detective.errors import ServiceError

if TYPE_CHECKING:
    import capo_detective.types.error_message
    import capo_detective.types.resource_list


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_detective.types.error_message.ErrorMessage"]
    resources: NotRequired["capo_detective.types.resource_list.ResourceList"]
    """<p>The type of resource that has exceeded the service quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resources" in value:
        import capo_detective.types.resource_list

        out["Resources"] = capo_detective.types.resource_list.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Resources") is not None:
        import capo_detective.types.resource_list

        out["resources"] = capo_detective.types.resource_list.deserialize_json(
            data["Resources"]
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.detective#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(
        self,
        data: ServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
