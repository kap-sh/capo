"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_summaries


class ListApplicationsResponse(TypedDict, closed=True):
    application_summaries: (
        "capo_kinesis_analytics_v2.types.application_summaries.ApplicationSummaries"
    )
    """<p>A list of <code>ApplicationSummary</code> objects.</p>"""
    next_token: NotRequired[
        "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    ]
    """<p>The pagination token for the next set of results, or <code>null</code> if there are no additional results. Pass this token into a subsequent command to retrieve the next set of items For more information about pagination, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Using the Amazon Command Line Interface's Pagination Options</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.application_summaries

    out["ApplicationSummaries"] = (
        capo_kinesis_analytics_v2.types.application_summaries.serialize_aws_json_1_1(
            value["application_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationSummaries") is not None:
        import capo_kinesis_analytics_v2.types.application_summaries

        out["application_summaries"] = (
            capo_kinesis_analytics_v2.types.application_summaries.deserialize_aws_json_1_1(
                data["ApplicationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListApplicationsResponse.application_summaries required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
