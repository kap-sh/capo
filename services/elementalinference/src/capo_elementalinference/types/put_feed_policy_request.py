"""Generated from Smithy shape ``com.amazonaws.elementalinference#PutFeedPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.policy_document


class PutFeedPolicyRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed to attach the policy to.</p>"""
    policy: "capo_elementalinference.types.policy_document.PolicyDocument"
    """<p>The resource-based policy document to attach to the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFeedPolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutFeedPolicyRequest:
    out: PutFeedPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
