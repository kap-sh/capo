"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateUsageLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.usage_limit_breach_action


class UpdateUsageLimitRequest(TypedDict, closed=True):
    usage_limit_id: "str"
    """<p>The identifier of the usage limit to update.</p>"""
    amount: NotRequired["int"]
    """<p>The new limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>"""
    breach_action: NotRequired[
        "capo_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
    ]
    """<p>The new action that Amazon Redshift Serverless takes when the limit is reached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUsageLimitRequest) -> dict:
    out: dict = {}
    out["usageLimitId"] = value["usage_limit_id"]
    if "amount" in value:
        out["amount"] = value["amount"]
    if "breach_action" in value:
        out["breachAction"] = value["breach_action"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUsageLimitRequest:
    out: UpdateUsageLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("usageLimitId") is not None:
        out["usage_limit_id"] = data["usageLimitId"]
    else:
        out["usage_limit_id"] = ""
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("breachAction") is not None:
        out["breach_action"] = data["breachAction"]
    return out
