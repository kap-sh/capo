"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListManagedInsightRulesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.insight_rule_max_results
    import capo_cloudwatch.types.next_token


class ListManagedInsightRulesInput(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p> The ARN of an Amazon Web Services resource that has managed Contributor Insights rules. </p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p> Include this value to get the next set of rules if the value was returned by the previous operation. </p>"""
    max_results: NotRequired[
        "capo_cloudwatch.types.insight_rule_max_results.InsightRuleMaxResults"
    ]
    """<p> The maximum number of results to return in one operation. If you omit this parameter, the default number is used. The default number is <code>100</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListManagedInsightRulesInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListManagedInsightRulesInput:
    out: ListManagedInsightRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListManagedInsightRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceARN", str(value["resource_arn"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListManagedInsightRulesInput:
    out: ListManagedInsightRulesInput = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceARN")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListManagedInsightRulesInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListManagedInsightRulesInput:
    out: ListManagedInsightRulesInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
