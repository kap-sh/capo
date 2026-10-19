"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GetResourceRequestStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.request_token


class GetResourceRequestStatusInput(TypedDict, closed=True):
    request_token: "capo_cloudcontrol.types.request_token.RequestToken"
    """<p>A unique token used to track the progress of the resource operation request.</p> <p>Request tokens are included in the <code>ProgressEvent</code> type returned by a resource operation request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceRequestStatusInput) -> dict:
    out: dict = {}
    out["RequestToken"] = value["request_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceRequestStatusInput:
    out: GetResourceRequestStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("RequestToken") is not None:
        out["request_token"] = data["RequestToken"]
    else:
        out["request_token"] = ""
    return out
