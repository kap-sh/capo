"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListRoute53HealthChecksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.max_results
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.route53_hosted_zone_id
    import capo_arc_region_switch.types.route53_record_name


class ListRoute53HealthChecksRequest(TypedDict, closed=True):
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Route 53 health check request.</p>"""
    hosted_zone_id: NotRequired[
        "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
    ]
    """<p>The hosted zone ID for the health checks.</p>"""
    record_name: NotRequired[
        "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
    ]
    """<p>The record name for the health checks.</p>"""
    max_results: NotRequired["capo_arc_region_switch.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRoute53HealthChecksRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "hosted_zone_id" in value:
        out["hostedZoneId"] = value["hosted_zone_id"]
    if "record_name" in value:
        out["recordName"] = value["record_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRoute53HealthChecksRequest:
    out: ListRoute53HealthChecksRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("hostedZoneId") is not None:
        out["hosted_zone_id"] = data["hostedZoneId"]
    if data.get("recordName") is not None:
        out["record_name"] = data["recordName"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
