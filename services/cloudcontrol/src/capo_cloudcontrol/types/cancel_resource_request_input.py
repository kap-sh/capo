"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CancelResourceRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.request_token


class CancelResourceRequestInput(TypedDict, closed=True):
    request_token: "capo_cloudcontrol.types.request_token.RequestToken"
    """<p>The <code>RequestToken</code> of the <code>ProgressEvent</code> object returned by the resource operation request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelResourceRequestInput) -> dict:
    out: dict = {}
    out["RequestToken"] = value["request_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelResourceRequestInput:
    out: CancelResourceRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("RequestToken") is not None:
        out["request_token"] = data["RequestToken"]
    else:
        out["request_token"] = ""
    return out
