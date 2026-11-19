"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeLogPatternResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.log_pattern
    import capo_application_insights.types.resource_group_name


class DescribeLogPatternResponse(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""
    log_pattern: NotRequired["capo_application_insights.types.log_pattern.LogPattern"]
    """<p>The successfully created log pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogPatternResponse) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "log_pattern" in value:
        import capo_application_insights.types.log_pattern

        out["LogPattern"] = (
            capo_application_insights.types.log_pattern.serialize_aws_json_1_1(
                value["log_pattern"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogPatternResponse:
    out: DescribeLogPatternResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("LogPattern") is not None:
        import capo_application_insights.types.log_pattern

        out["log_pattern"] = (
            capo_application_insights.types.log_pattern.deserialize_aws_json_1_1(
                data["LogPattern"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeLogPatternResponse) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "log_pattern" in value:
        import capo_application_insights.types.log_pattern

        out["LogPattern"] = capo_application_insights.types.log_pattern.serialize_cbor(
            value["log_pattern"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeLogPatternResponse:
    out: DescribeLogPatternResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("LogPattern") is not None:
        import capo_application_insights.types.log_pattern

        out["log_pattern"] = (
            capo_application_insights.types.log_pattern.deserialize_cbor(
                data["LogPattern"]
            )
        )
    return out
