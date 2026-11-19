"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListRuntimeVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier


class ListRuntimeVersionsRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime whose versions to list."""
    next_token: NotRequired["str"]
    """The pagination token from a previous response. Use it to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of runtime versions to return per page. Valid range: 1 to 100."""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuntimeVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRuntimeVersionsRequest:
    out: ListRuntimeVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
