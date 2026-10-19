"""Generated from Smithy shape ``com.amazonaws.freetier#ListAccountActivitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.filter_activity_statuses
    import capo_freetier.types.language_code
    import capo_freetier.types.max_results
    import capo_freetier.types.next_page_token


class ListAccountActivitiesRequest(TypedDict, closed=True):
    filter_activity_statuses: NotRequired[
        "capo_freetier.types.filter_activity_statuses.FilterActivityStatuses"
    ]
    """<p> The activity status filter. This field can be used to filter the response by activities status. </p>"""
    next_token: NotRequired["capo_freetier.types.next_page_token.NextPageToken"]
    """<p> A token from a previous paginated response. If this is specified, the response includes records beginning from this token (inclusive), up to the number specified by <code>maxResults</code>. </p>"""
    max_results: NotRequired["capo_freetier.types.max_results.MaxResults"]
    """<p> The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. </p>"""
    language_code: NotRequired["capo_freetier.types.language_code.LanguageCode"]
    """<p> The language code used to return translated titles. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccountActivitiesRequest) -> dict:
    out: dict = {}
    if "filter_activity_statuses" in value:
        import capo_freetier.types.filter_activity_statuses

        out["filterActivityStatuses"] = (
            capo_freetier.types.filter_activity_statuses.serialize_aws_json_1_0(
                value["filter_activity_statuses"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "language_code" in value:
        import capo_freetier.types.language_code

        out["languageCode"] = capo_freetier.types.language_code.serialize_aws_json_1_0(
            value["language_code"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccountActivitiesRequest:
    out: ListAccountActivitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterActivityStatuses") is not None:
        import capo_freetier.types.filter_activity_statuses

        out["filter_activity_statuses"] = (
            capo_freetier.types.filter_activity_statuses.deserialize_aws_json_1_0(
                data["filterActivityStatuses"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("languageCode") is not None:
        import capo_freetier.types.language_code

        out["language_code"] = (
            capo_freetier.types.language_code.deserialize_aws_json_1_0(
                data["languageCode"]
            )
        )
    return out
