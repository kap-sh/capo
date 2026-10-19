"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFeedPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.policy_document


class GetFeedPolicyResponse(TypedDict, closed=True):
    policy: "capo_elementalinference.types.policy_document.PolicyDocument"
    """<p>The resource-based policy document attached to the feed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFeedPolicyResponse) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetFeedPolicyResponse:
    out: GetFeedPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
