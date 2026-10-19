"""Generated from Smithy shape ``com.amazonaws.qconnect#ProactiveRecommendationDataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.next_token


class ProactiveRecommendationDataDetails(TypedDict, closed=True):
    next_message_token: "capo_qconnect.types.next_token.NextToken"
    """<p>The token used to retrieve the next message in the proactive recommendation. Pass this token in a <code>GetNextMessage</code> request to continue receiving the chunked proactive response. Each response returns the next token to use until the chunked response is complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveRecommendationDataDetails) -> dict:
    out: dict = {}
    out["nextMessageToken"] = value["next_message_token"]
    return out


def deserialize_json(data: dict) -> ProactiveRecommendationDataDetails:
    out: ProactiveRecommendationDataDetails = {}  # type: ignore[typeddict-item]
    if data.get("nextMessageToken") is not None:
        out["next_message_token"] = data["nextMessageToken"]
    else:
        out["next_message_token"] = ""
    return out
