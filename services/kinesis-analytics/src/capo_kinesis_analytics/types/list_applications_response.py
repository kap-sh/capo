"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.application_summaries
    import capo_kinesis_analytics.types.boolean_object


class ListApplicationsResponse(TypedDict, closed=True):
    application_summaries: (
        "capo_kinesis_analytics.types.application_summaries.ApplicationSummaries"
    )
    """<p>List of <code>ApplicationSummary</code> objects. </p>"""
    has_more_applications: "capo_kinesis_analytics.types.boolean_object.BooleanObject"
    """<p>Returns true if there are more applications to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import capo_kinesis_analytics.types.application_summaries

    out["ApplicationSummaries"] = (
        capo_kinesis_analytics.types.application_summaries.serialize_aws_json_1_1(
            value["application_summaries"]
        )
    )
    out["HasMoreApplications"] = value["has_more_applications"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationSummaries") is not None:
        import capo_kinesis_analytics.types.application_summaries

        out["application_summaries"] = (
            capo_kinesis_analytics.types.application_summaries.deserialize_aws_json_1_1(
                data["ApplicationSummaries"]
            )
        )
    else:
        out["application_summaries"] = []
    if data.get("HasMoreApplications") is not None:
        out["has_more_applications"] = data["HasMoreApplications"]
    else:
        out["has_more_applications"] = False
    return out
