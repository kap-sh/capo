"""Generated from Smithy shape ``com.amazonaws.support#RefreshTrustedAdvisorCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.string


class RefreshTrustedAdvisorCheckRequest(TypedDict, closed=True):
    check_id: "capo_support.types.string.String"
    """<p>The unique identifier for the Trusted Advisor check to refresh.</p> <note> <p>Specifying the check ID of a check that is automatically refreshed causes an <code>InvalidParameterValue</code> error.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshTrustedAdvisorCheckRequest) -> dict:
    out: dict = {}
    out["checkId"] = value["check_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshTrustedAdvisorCheckRequest:
    out: RefreshTrustedAdvisorCheckRequest = {}  # type: ignore[typeddict-item]
    if data.get("checkId") is not None:
        out["check_id"] = data["checkId"]
    else:
        out["check_id"] = ""
    return out
