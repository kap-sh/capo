"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetNotifyMessageSpendLimitOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.monthly_limit


class SetNotifyMessageSpendLimitOverrideRequest(TypedDict, closed=True):
    monthly_limit: "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit"
    """<p>The new monthly limit to enforce on notify messages.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetNotifyMessageSpendLimitOverrideRequest) -> dict:
    out: dict = {}
    out["MonthlyLimit"] = value["monthly_limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetNotifyMessageSpendLimitOverrideRequest:
    out: SetNotifyMessageSpendLimitOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("MonthlyLimit") is not None:
        out["monthly_limit"] = data["MonthlyLimit"]
    else:
        out["monthly_limit"] = 0
    return out
