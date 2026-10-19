"""Generated from Smithy shape ``com.amazonaws.xray#CancelTraceRetrievalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.retrieval_token


class CancelTraceRetrievalRequest(TypedDict, closed=True):
    retrieval_token: "capo_xray.types.retrieval_token.RetrievalToken"
    """<p> Retrieval token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelTraceRetrievalRequest) -> dict:
    out: dict = {}
    out["RetrievalToken"] = value["retrieval_token"]
    return out


def deserialize_json(data: dict) -> CancelTraceRetrievalRequest:
    out: CancelTraceRetrievalRequest = {}  # type: ignore[typeddict-item]
    if data.get("RetrievalToken") is not None:
        out["retrieval_token"] = data["RetrievalToken"]
    else:
        out["retrieval_token"] = ""
    return out
