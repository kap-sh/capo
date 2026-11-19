"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListServiceQuotaWarningsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.max_results
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.plan_arn_list


class ListServiceQuotaWarningsRequest(TypedDict, closed=True):
    plan_arns: NotRequired["capo_arc_region_switch.types.plan_arn_list.PlanArnList"]
    """<p>The Amazon Resource Names (ARNs) of the plans to return service quota warnings for. You can specify up to 100 plan ARNs. Region switch ignores any plan ARN that you can't access. If you omit this parameter, Region switch returns the warnings for all of your accessible plans.</p>"""
    max_results: NotRequired["capo_arc_region_switch.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with this call. Valid values are <code>1</code> to <code>100</code>. If you don't specify a value, the operation returns up to the maximum number of results.</p>"""
    next_token: NotRequired["capo_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceQuotaWarningsRequest) -> dict:
    out: dict = {}
    if "plan_arns" in value:
        import capo_arc_region_switch.types.plan_arn_list

        out["planArns"] = (
            capo_arc_region_switch.types.plan_arn_list.serialize_aws_json_1_0(
                value["plan_arns"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceQuotaWarningsRequest:
    out: ListServiceQuotaWarningsRequest = {}  # type: ignore[typeddict-item]
    if data.get("planArns") is not None:
        import capo_arc_region_switch.types.plan_arn_list

        out["plan_arns"] = (
            capo_arc_region_switch.types.plan_arn_list.deserialize_aws_json_1_0(
                data["planArns"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListServiceQuotaWarningsRequest) -> dict:
    out: dict = {}
    if "plan_arns" in value:
        import capo_arc_region_switch.types.plan_arn_list

        out["planArns"] = capo_arc_region_switch.types.plan_arn_list.serialize_cbor(
            value["plan_arns"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListServiceQuotaWarningsRequest:
    out: ListServiceQuotaWarningsRequest = {}  # type: ignore[typeddict-item]
    if data.get("planArns") is not None:
        import capo_arc_region_switch.types.plan_arn_list

        out["plan_arns"] = capo_arc_region_switch.types.plan_arn_list.deserialize_cbor(
            data["planArns"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
