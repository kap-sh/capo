"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeSubscribersForNotificationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.generic_string
    import capo_budgets.types.subscribers


class DescribeSubscribersForNotificationResponse(TypedDict, closed=True):
    subscribers: NotRequired["capo_budgets.types.subscribers.Subscribers"]
    """<p>A list of subscribers that are associated with a notification.</p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]
    """<p>The pagination token in the service response that indicates the next set of results that you can retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscribersForNotificationResponse) -> dict:
    out: dict = {}
    if "subscribers" in value:
        import capo_budgets.types.subscribers

        out["Subscribers"] = capo_budgets.types.subscribers.serialize_aws_json_1_1(
            value["subscribers"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscribersForNotificationResponse:
    out: DescribeSubscribersForNotificationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Subscribers") is not None:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.deserialize_aws_json_1_1(
            data["Subscribers"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: DescribeSubscribersForNotificationResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subscribers" in value:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.redact_sensitive(
            value["subscribers"]
        )
    return out
