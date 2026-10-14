"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import ServiceError

if TYPE_CHECKING:
    import capo_kendra.types.conflicting_items
    import capo_kendra.types.string


class FeaturedResultsConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_kendra.types.string.String"]
    """<p>An explanation for the conflicting queries.</p>"""
    conflicting_items: NotRequired[
        "capo_kendra.types.conflicting_items.ConflictingItems"
    ]
    """<p>A list of the conflicting queries, including the query text, the name for the featured results set, and the identifier of the featured results set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "conflicting_items" in value:
        import capo_kendra.types.conflicting_items

        out["ConflictingItems"] = (
            capo_kendra.types.conflicting_items.serialize_aws_json_1_1(
                value["conflicting_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedResultsConflictException_:
    out: FeaturedResultsConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ConflictingItems") is not None:
        import capo_kendra.types.conflicting_items

        out["conflicting_items"] = (
            capo_kendra.types.conflicting_items.deserialize_aws_json_1_1(
                data["ConflictingItems"]
            )
        )
    return out


class FeaturedResultsConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kendra#FeaturedResultsConflictException``."""

    code: str | None = "FeaturedResultsConflictException"

    def __init__(
        self,
        data: FeaturedResultsConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FeaturedResultsConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FeaturedResultsConflictException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
