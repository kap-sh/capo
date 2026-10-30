"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#TokenLogprob``."""

from typing_extensions import TypedDict


class TokenLogprob(TypedDict, closed=True):
    token_id: "int"
    """<p>The vocabulary token ID.</p>"""
    logprob: "float"
    """<p>The log-probability of the token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenLogprob) -> dict:
    out: dict = {}
    out["tokenId"] = value["token_id"]
    out["logprob"] = (
        "NaN"
        if value["logprob"] != value["logprob"]
        else "Infinity"
        if value["logprob"] == float("inf")
        else "-Infinity"
        if value["logprob"] == float("-inf")
        else value["logprob"]
    )
    return out


def deserialize_json(data: dict) -> TokenLogprob:
    out: TokenLogprob = {}  # type: ignore[typeddict-item]
    if data.get("tokenId") is not None:
        out["token_id"] = data["tokenId"]
    else:
        out["token_id"] = 0
    if data.get("logprob") is not None:
        out["logprob"] = float(data["logprob"])
    else:
        out["logprob"] = 0.0
    return out
