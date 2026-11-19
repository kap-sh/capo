"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListRuntimesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_list


class ListRuntimesResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """The pagination token to include in a subsequent request to retrieve the next page of results."""
    items: "capo_lambda_core.types.runtime_list.RuntimeList"
    """The list of runtimes for the current page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuntimesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_lambda_core.types.runtime_list

    out["Items"] = capo_lambda_core.types.runtime_list.serialize_json(value["items"])
    return out


def deserialize_json(data: dict) -> ListRuntimesResponse:
    out: ListRuntimesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Items") is not None:
        import capo_lambda_core.types.runtime_list

        out["items"] = capo_lambda_core.types.runtime_list.deserialize_json(
            data["Items"]
        )
    else:
        out["items"] = []
    return out
