"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.service_summary_list


class ListServicesResponse(TypedDict, closed=True):
    service_summaries: (
        "capo_resiliencehubv2.types.service_summary_list.ServiceSummaryList"
    )
    """<p>The list of service summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.service_summary_list

    out["serviceSummaries"] = (
        capo_resiliencehubv2.types.service_summary_list.serialize_json(
            value["service_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServicesResponse:
    out: ListServicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("serviceSummaries") is not None:
        import capo_resiliencehubv2.types.service_summary_list

        out["service_summaries"] = (
            capo_resiliencehubv2.types.service_summary_list.deserialize_json(
                data["serviceSummaries"]
            )
        )
    else:
        out["service_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
