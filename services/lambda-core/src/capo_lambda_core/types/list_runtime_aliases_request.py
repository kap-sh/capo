"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListRuntimeAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_identifier


class ListRuntimeAliasesRequest(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime whose aliases to list."""
    next_token: NotRequired["str"]
    """The pagination token from a previous response. Use it to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of runtime aliases to return per page. Valid range: 1 to 100."""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuntimeAliasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRuntimeAliasesRequest:
    out: ListRuntimeAliasesRequest = {}  # type: ignore[typeddict-item]
    return out
