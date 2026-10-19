"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListABTestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_summary_list


class ListABTestsResponse(TypedDict, closed=True):
    ab_tests: "capo_bedrock_agentcore.types.ab_test_summary_list.ABTestSummaryList"
    """<p>The list of A/B test summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListABTestsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.ab_test_summary_list

    out["abTests"] = capo_bedrock_agentcore.types.ab_test_summary_list.serialize_json(
        value["ab_tests"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListABTestsResponse:
    out: ListABTestsResponse = {}  # type: ignore[typeddict-item]
    if data.get("abTests") is not None:
        import capo_bedrock_agentcore.types.ab_test_summary_list

        out["ab_tests"] = (
            capo_bedrock_agentcore.types.ab_test_summary_list.deserialize_json(
                data["abTests"]
            )
        )
    else:
        out["ab_tests"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
