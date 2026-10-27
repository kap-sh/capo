"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetSourceEndpointError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_arn


class BatchGetSourceEndpointError(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the source endpoint that MediaConnect couldn't retrieve.</p>"""
    code: "str"
    """<p>The error code.</p>"""
    message: "str"
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSourceEndpointError) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetSourceEndpointError:
    out: BatchGetSourceEndpointError = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
