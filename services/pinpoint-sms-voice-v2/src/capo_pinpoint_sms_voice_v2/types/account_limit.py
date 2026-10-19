"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccountLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.account_limit_name


class AccountLimit(TypedDict, closed=True):
    name: "capo_pinpoint_sms_voice_v2.types.account_limit_name.AccountLimitName"
    """<p>The name of the attribute to apply the account limit to.</p>"""
    used: "int"
    """<p>The current amount that has been spent, in US dollars.</p>"""
    max: "int"
    """<p>The Amazon Web Services set limit for that resource type, in US dollars.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountLimit) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Used"] = value.get("used", 0)
    out["Max"] = value.get("max", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountLimit:
    out: AccountLimit = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Used") is not None:
        out["used"] = data["Used"]
    else:
        out["used"] = 0
    if data.get("Max") is not None:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    return out
