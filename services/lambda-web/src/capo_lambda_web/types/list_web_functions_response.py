"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ListWebFunctionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.function_summary_list
    import capo_lambda_web.types.next_token


class ListWebFunctionsResponse(TypedDict, closed=True):
    functions: "capo_lambda_web.types.function_summary_list.FunctionSummaryList"
    """<p>A list of web function summaries.</p>"""
    next_token: NotRequired["capo_lambda_web.types.next_token.NextToken"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebFunctionsResponse) -> dict:
    out: dict = {}
    import capo_lambda_web.types.function_summary_list

    out["functions"] = capo_lambda_web.types.function_summary_list.serialize_json(
        value["functions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWebFunctionsResponse:
    out: ListWebFunctionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("functions") is not None:
        import capo_lambda_web.types.function_summary_list

        out["functions"] = capo_lambda_web.types.function_summary_list.deserialize_json(
            data["functions"]
        )
    else:
        raise DeserializationError("ListWebFunctionsResponse.functions required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
