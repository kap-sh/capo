"""Generated from Smithy shape ``com.amazonaws.kendra#ListExperienceEntitiesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.experience_entities_summary_list
    import capo_kendra.types.next_token


class ListExperienceEntitiesResponse(TypedDict, closed=True):
    summary_items: NotRequired[
        "capo_kendra.types.experience_entities_summary_list.ExperienceEntitiesSummaryList"
    ]
    """<p>An array of summary information for one or more users or groups.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token, which you can use in a later request to retrieve the next set of users or groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExperienceEntitiesResponse) -> dict:
    out: dict = {}
    if "summary_items" in value:
        import capo_kendra.types.experience_entities_summary_list

        out["SummaryItems"] = (
            capo_kendra.types.experience_entities_summary_list.serialize_aws_json_1_1(
                value["summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExperienceEntitiesResponse:
    out: ListExperienceEntitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("SummaryItems") is not None:
        import capo_kendra.types.experience_entities_summary_list

        out["summary_items"] = (
            capo_kendra.types.experience_entities_summary_list.deserialize_aws_json_1_1(
                data["SummaryItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListExperienceEntitiesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "summary_items" in value:
        import capo_kendra.types.experience_entities_summary_list

        out["summary_items"] = (
            capo_kendra.types.experience_entities_summary_list.redact_sensitive(
                value["summary_items"]
            )
        )
    return out
