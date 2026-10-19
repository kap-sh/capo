"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.aws_account_id
    import capo_devops_guru.types.insight_id
    import capo_devops_guru.types.locale
    import capo_devops_guru.types.uuid_next_token


class ListRecommendationsRequest(TypedDict, closed=True):
    insight_id: "capo_devops_guru.types.insight_id.InsightId"
    """<p> The ID of the requested insight. </p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    locale: NotRequired["capo_devops_guru.types.locale.Locale"]
    """<p>A locale that specifies the language to use for recommendations.</p>"""
    account_id: NotRequired["capo_devops_guru.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "locale" in value:
        import capo_devops_guru.types.locale

        out["Locale"] = capo_devops_guru.types.locale.serialize_json(value["locale"])
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        out["insight_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Locale") is not None:
        import capo_devops_guru.types.locale

        out["locale"] = capo_devops_guru.types.locale.deserialize_json(data["Locale"])
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
