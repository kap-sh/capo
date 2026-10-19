"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListServiceQuotaWarningsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.service_quota_warning_summary_list


class ListServiceQuotaWarningsResponse(TypedDict, closed=True):
    service_quota_warning_summaries: "capo_arc_region_switch.types.service_quota_warning_summary_list.ServiceQuotaWarningSummaryList"
    """<p>The service quota warnings for the plans that you can access.</p>"""
    next_token: NotRequired["capo_arc_region_switch.types.next_token.NextToken"]
    """<p>A pagination token. A response may contain no results while still including a <code>nextToken</code>. Continue paginating until <code>nextToken</code> is null to retrieve all results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceQuotaWarningsResponse) -> dict:
    out: dict = {}
    import capo_arc_region_switch.types.service_quota_warning_summary_list

    out["serviceQuotaWarningSummaries"] = (
        capo_arc_region_switch.types.service_quota_warning_summary_list.serialize_aws_json_1_0(
            value["service_quota_warning_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceQuotaWarningsResponse:
    out: ListServiceQuotaWarningsResponse = {}  # type: ignore[typeddict-item]
    if data.get("serviceQuotaWarningSummaries") is not None:
        import capo_arc_region_switch.types.service_quota_warning_summary_list

        out["service_quota_warning_summaries"] = (
            capo_arc_region_switch.types.service_quota_warning_summary_list.deserialize_aws_json_1_0(
                data["serviceQuotaWarningSummaries"]
            )
        )
    else:
        out["service_quota_warning_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
