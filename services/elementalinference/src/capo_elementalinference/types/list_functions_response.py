"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListFunctionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.function_summary_list


class ListFunctionsResponse(TypedDict, closed=True):
    functions: "capo_elementalinference.types.function_summary_list.FunctionSummaryList"
    """<p>An array of function summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use in a subsequent request to get the next page of results. This field is absent when there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsResponse) -> dict:
    out: dict = {}
    import capo_elementalinference.types.function_summary_list

    out["functions"] = (
        capo_elementalinference.types.function_summary_list.serialize_json(
            value["functions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFunctionsResponse:
    out: ListFunctionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("functions") is not None:
        import capo_elementalinference.types.function_summary_list

        out["functions"] = (
            capo_elementalinference.types.function_summary_list.deserialize_json(
                data["functions"]
            )
        )
    else:
        out["functions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListFunctionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "functions" in value:
        import capo_elementalinference.types.function_summary_list

        out["functions"] = (
            capo_elementalinference.types.function_summary_list.redact_sensitive(
                value["functions"]
            )
        )
    return out
