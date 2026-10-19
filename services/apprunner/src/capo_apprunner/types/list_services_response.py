"""Generated from Smithy shape ``com.amazonaws.apprunner#ListServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.service_summary_list
    import capo_apprunner.types.string


class ListServicesResponse(TypedDict, closed=True):
    service_summary_list: "capo_apprunner.types.service_summary_list.ServiceSummaryList"
    """<p>A list of service summary information records. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["capo_apprunner.types.string.String"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServicesResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.service_summary_list

    out["ServiceSummaryList"] = (
        capo_apprunner.types.service_summary_list.serialize_aws_json_1_0(
            value["service_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServicesResponse:
    out: ListServicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ServiceSummaryList") is not None:
        import capo_apprunner.types.service_summary_list

        out["service_summary_list"] = (
            capo_apprunner.types.service_summary_list.deserialize_aws_json_1_0(
                data["ServiceSummaryList"]
            )
        )
    else:
        out["service_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
