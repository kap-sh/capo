"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateUsageLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.usage_limit_breach_action
    import capo_redshift_serverless.types.usage_limit_period
    import capo_redshift_serverless.types.usage_limit_usage_type


class CreateUsageLimitRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Amazon Redshift Serverless resource to create the usage limit for.</p>"""
    usage_type: (
        "capo_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
    )
    """<p>The type of Amazon Redshift Serverless usage to create a usage limit for.</p>"""
    amount: "int"
    """<p>The limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>"""
    period: NotRequired[
        "capo_redshift_serverless.types.usage_limit_period.UsageLimitPeriod"
    ]
    """<p>The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.</p>"""
    breach_action: NotRequired[
        "capo_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
    ]
    """<p>The action that Amazon Redshift Serverless takes when the limit is reached. The default is log.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUsageLimitRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["usageType"] = value["usage_type"]
    out["amount"] = value["amount"]
    if "period" in value:
        out["period"] = value["period"]
    if "breach_action" in value:
        out["breachAction"] = value["breach_action"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUsageLimitRequest:
    out: CreateUsageLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("usageType") is not None:
        out["usage_type"] = data["usageType"]
    else:
        out["usage_type"] = ""
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    else:
        out["amount"] = 0
    if data.get("period") is not None:
        out["period"] = data["period"]
    if data.get("breachAction") is not None:
        out["breach_action"] = data["breachAction"]
    return out
