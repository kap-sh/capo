"""Generated from Smithy shape ``com.amazonaws.wafv2#ImmunityTimeProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.time_window_second


class ImmunityTimeProperty(TypedDict, closed=True):
    immunity_time: "capo_wafv2.types.time_window_second.TimeWindowSecond"
    """<p>The amount of time, in seconds, that a <code>CAPTCHA</code> or challenge timestamp is considered valid by WAF. The default setting is 300. </p> <p>For the Challenge action, the minimum setting is 300. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImmunityTimeProperty) -> dict:
    out: dict = {}
    out["ImmunityTime"] = value["immunity_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImmunityTimeProperty:
    out: ImmunityTimeProperty = {}  # type: ignore[typeddict-item]
    if data.get("ImmunityTime") is not None:
        out["immunity_time"] = data["ImmunityTime"]
    else:
        out["immunity_time"] = 0
    return out
