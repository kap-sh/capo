"""Generated from Smithy shape ``com.amazonaws.supportauthz#RejectSupportPermitRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.request_arn


class RejectSupportPermitRequestOutput(TypedDict, closed=True):
    request_arn: "capo_supportauthz.types.request_arn.RequestArn"
    """<p>The ARN of the rejected permit request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectSupportPermitRequestOutput) -> dict:
    out: dict = {}
    out["requestArn"] = value["request_arn"]
    return out


def deserialize_json(data: dict) -> RejectSupportPermitRequestOutput:
    out: RejectSupportPermitRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("requestArn") is not None:
        out["request_arn"] = data["requestArn"]
    else:
        raise DeserializationError(
            "RejectSupportPermitRequestOutput.request_arn required"
        )
    return out
