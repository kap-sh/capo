"""Generated from Smithy shape ``com.amazonaws.m2#GetSignedBluinsightsUrlResponse``."""

from typing_extensions import TypedDict


class GetSignedBluinsightsUrlResponse(TypedDict, closed=True):
    signed_bi_url: "str"
    """<p>Single sign-on AWS Blu Insights URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSignedBluinsightsUrlResponse) -> dict:
    out: dict = {}
    out["signedBiUrl"] = value["signed_bi_url"]
    return out


def deserialize_json(data: dict) -> GetSignedBluinsightsUrlResponse:
    out: GetSignedBluinsightsUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("signedBiUrl") is not None:
        out["signed_bi_url"] = data["signedBiUrl"]
    else:
        out["signed_bi_url"] = ""
    return out
