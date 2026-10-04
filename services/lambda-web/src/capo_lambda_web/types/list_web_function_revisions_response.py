"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ListWebFunctionRevisionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.function_revision_summary_list
    import capo_lambda_web.types.next_token


class ListWebFunctionRevisionsResponse(TypedDict, closed=True):
    revisions: "capo_lambda_web.types.function_revision_summary_list.FunctionRevisionSummaryList"
    """<p>A list of revision summaries for the web function.</p>"""
    next_token: NotRequired["capo_lambda_web.types.next_token.NextToken"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebFunctionRevisionsResponse) -> dict:
    out: dict = {}
    import capo_lambda_web.types.function_revision_summary_list

    out["revisions"] = (
        capo_lambda_web.types.function_revision_summary_list.serialize_json(
            value["revisions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWebFunctionRevisionsResponse:
    out: ListWebFunctionRevisionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("revisions") is not None:
        import capo_lambda_web.types.function_revision_summary_list

        out["revisions"] = (
            capo_lambda_web.types.function_revision_summary_list.deserialize_json(
                data["revisions"]
            )
        )
    else:
        raise DeserializationError(
            "ListWebFunctionRevisionsResponse.revisions required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
