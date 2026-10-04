"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ListWebFunctionEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.function_endpoint_summary_list
    import capo_lambda_web.types.next_token


class ListWebFunctionEndpointsResponse(TypedDict, closed=True):
    endpoints: "capo_lambda_web.types.function_endpoint_summary_list.FunctionEndpointSummaryList"
    """<p>A list of endpoint summaries for the web function.</p>"""
    next_token: NotRequired["capo_lambda_web.types.next_token.NextToken"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebFunctionEndpointsResponse) -> dict:
    out: dict = {}
    import capo_lambda_web.types.function_endpoint_summary_list

    out["endpoints"] = (
        capo_lambda_web.types.function_endpoint_summary_list.serialize_json(
            value["endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWebFunctionEndpointsResponse:
    out: ListWebFunctionEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("endpoints") is not None:
        import capo_lambda_web.types.function_endpoint_summary_list

        out["endpoints"] = (
            capo_lambda_web.types.function_endpoint_summary_list.deserialize_json(
                data["endpoints"]
            )
        )
    else:
        raise DeserializationError(
            "ListWebFunctionEndpointsResponse.endpoints required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
