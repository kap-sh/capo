"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_list
    import capo_lambda.types.string


class ListFunctionsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    functions: NotRequired["capo_lambda.types.function_list.FunctionList"]
    """<p>A list of Lambda functions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "functions" in value:
        import capo_lambda.types.function_list

        out["Functions"] = capo_lambda.types.function_list.serialize_json(
            value["functions"]
        )
    return out


def deserialize_json(data: dict) -> ListFunctionsResponse:
    out: ListFunctionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Functions") is not None:
        import capo_lambda.types.function_list

        out["functions"] = capo_lambda.types.function_list.deserialize_json(
            data["Functions"]
        )
    return out


def redact_sensitive(value: ListFunctionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "functions" in value:
        import capo_lambda.types.function_list

        out["functions"] = capo_lambda.types.function_list.redact_sensitive(
            value["functions"]
        )
    return out
