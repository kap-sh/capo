"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAccessPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.access_policy_summaries
    import capo_iotsitewise.types.next_token


class ListAccessPoliciesResponse(TypedDict, closed=True):
    access_policy_summaries: (
        "capo_iotsitewise.types.access_policy_summaries.AccessPolicySummaries"
    )
    """<p>A list that summarizes each access policy.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPoliciesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.access_policy_summaries

    out["accessPolicySummaries"] = (
        capo_iotsitewise.types.access_policy_summaries.serialize_json(
            value["access_policy_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessPoliciesResponse:
    out: ListAccessPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessPolicySummaries") is not None:
        import capo_iotsitewise.types.access_policy_summaries

        out["access_policy_summaries"] = (
            capo_iotsitewise.types.access_policy_summaries.deserialize_json(
                data["accessPolicySummaries"]
            )
        )
    else:
        out["access_policy_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
