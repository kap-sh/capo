"""Generated from Smithy shape ``com.amazonaws.lambda#ListVersionsByFunctionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_list
    import capo_lambda.types.string


class ListVersionsByFunctionResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    versions: NotRequired["capo_lambda.types.function_list.FunctionList"]
    """<p>A list of Lambda function versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsByFunctionResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "versions" in value:
        import capo_lambda.types.function_list

        out["Versions"] = capo_lambda.types.function_list.serialize_json(
            value["versions"]
        )
    return out


def deserialize_json(data: dict) -> ListVersionsByFunctionResponse:
    out: ListVersionsByFunctionResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Versions") is not None:
        import capo_lambda.types.function_list

        out["versions"] = capo_lambda.types.function_list.deserialize_json(
            data["Versions"]
        )
    return out


def redact_sensitive(value: ListVersionsByFunctionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "versions" in value:
        import capo_lambda.types.function_list

        out["versions"] = capo_lambda.types.function_list.redact_sensitive(
            value["versions"]
        )
    return out
