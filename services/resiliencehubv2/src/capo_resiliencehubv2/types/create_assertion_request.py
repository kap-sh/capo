"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateAssertionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assertion_text
    import capo_resiliencehubv2.types.client_token


class CreateAssertionRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    text: "capo_resiliencehubv2.types.assertion_text.AssertionText"
    """<p>The text content of the assertion.</p>"""
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssertionRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["text"] = value["text"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssertionRequest:
    out: CreateAssertionRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
