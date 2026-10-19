"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckRefreshStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.long
    import capo_support.types.string


class TrustedAdvisorCheckRefreshStatus(TypedDict, closed=True):
    check_id: "capo_support.types.string.String"
    """<p>The unique identifier for the Trusted Advisor check.</p>"""
    status: "capo_support.types.string.String"
    """<p>The status of the Trusted Advisor check for which a refresh has been requested: </p> <ul> <li> <p> <code>none</code> - The check is not refreshed or the non-success status exceeds the timeout</p> </li> <li> <p> <code>enqueued</code> - The check refresh requests has entered the refresh queue</p> </li> <li> <p> <code>processing</code> - The check refresh request is picked up by the rule processing engine</p> </li> <li> <p> <code>success</code> - The check is successfully refreshed</p> </li> <li> <p> <code>abandoned</code> - The check refresh has failed</p> </li> </ul>"""
    millis_until_next_refreshable: "capo_support.types.long.Long"
    """<p>The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckRefreshStatus) -> dict:
    out: dict = {}
    out["checkId"] = value["check_id"]
    out["status"] = value["status"]
    out["millisUntilNextRefreshable"] = value.get("millis_until_next_refreshable", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCheckRefreshStatus:
    out: TrustedAdvisorCheckRefreshStatus = {}  # type: ignore[typeddict-item]
    if data.get("checkId") is not None:
        out["check_id"] = data["checkId"]
    else:
        out["check_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("millisUntilNextRefreshable") is not None:
        out["millis_until_next_refreshable"] = data["millisUntilNextRefreshable"]
    else:
        out["millis_until_next_refreshable"] = 0
    return out
