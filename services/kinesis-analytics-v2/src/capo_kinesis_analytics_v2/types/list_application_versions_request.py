"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.list_application_versions_input_limit
    import capo_kinesis_analytics_v2.types.next_token


class ListApplicationVersionsRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application for which you want to list all versions.</p>"""
    limit: NotRequired[
        "capo_kinesis_analytics_v2.types.list_application_versions_input_limit.ListApplicationVersionsInputLimit"
    ]
    """<p>The maximum number of versions to list in this invocation of the operation.</p>"""
    next_token: NotRequired["capo_kinesis_analytics_v2.types.next_token.NextToken"]
    """<p>If a previous invocation of this operation returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Using the Amazon Command Line Interface's Pagination Options</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationVersionsRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationVersionsRequest:
    out: ListApplicationVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "ListApplicationVersionsRequest.application_name required"
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
