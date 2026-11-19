"""Generated from Smithy shape ``com.amazonaws.wafv2#AnalyticsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.analytics_mode


class AnalyticsConfig(TypedDict, closed=True):
    mode: "capo_wafv2.types.analytics_mode.AnalyticsMode"
    """<p>The security analytics mode for the web ACL. Valid values:</p> <ul> <li> <p> <code>CROSS_REGION</code> - Enables security analytics. WAF transfers and stores the web ACL's request logs outside the Amazon Web Services Region where the web ACL is hosted, for aggregation and processing. </p> </li> <li> <p> <code>DISABLED</code> - Disables security analytics. WAF stops transferring the web ACL's request logs. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyticsConfig) -> dict:
    out: dict = {}
    import capo_wafv2.types.analytics_mode

    out["Mode"] = capo_wafv2.types.analytics_mode.serialize_aws_json_1_1(value["mode"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyticsConfig:
    out: AnalyticsConfig = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_wafv2.types.analytics_mode

        out["mode"] = capo_wafv2.types.analytics_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    else:
        import typing

        out["mode"] = typing.cast("capo_wafv2.types.analytics_mode.AnalyticsMode", "")
    return out
