"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListRuntimeVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_version_list


class ListRuntimeVersionsResponse(TypedDict, closed=True):
    items: "capo_lambda_core.types.runtime_version_list.RuntimeVersionList"
    """The list of runtime versions for the current page of results."""
    next_token: NotRequired["str"]
    """The pagination token to include in a subsequent request to retrieve the next page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuntimeVersionsResponse) -> dict:
    out: dict = {}
    import capo_lambda_core.types.runtime_version_list

    out["Items"] = capo_lambda_core.types.runtime_version_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRuntimeVersionsResponse:
    out: ListRuntimeVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_lambda_core.types.runtime_version_list

        out["items"] = capo_lambda_core.types.runtime_version_list.deserialize_json(
            data["Items"]
        )
    else:
        out["items"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
