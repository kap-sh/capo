"""Generated from Smithy shape ``com.amazonaws.supportauthz#RejectSupportPermitRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.request_arn


class RejectSupportPermitRequestInput(TypedDict, closed=True):
    request_arn: "capo_supportauthz.types.request_arn.RequestArn"
    """<p>The ARN of the permit request to reject.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectSupportPermitRequestInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RejectSupportPermitRequestInput:
    out: RejectSupportPermitRequestInput = {}  # type: ignore[typeddict-item]
    return out
