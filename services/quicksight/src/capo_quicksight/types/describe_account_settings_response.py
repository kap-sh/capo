"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.account_settings
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeAccountSettingsResponse(TypedDict, closed=True):
    account_settings: NotRequired[
        "capo_quicksight.types.account_settings.AccountSettings"
    ]
    """<p>The Amazon Quick Sight settings for this Amazon Web Services account. This information includes the edition of Amazon Quick Sight that you subscribed to (Standard or Enterprise) and the notification email for the Amazon Quick Sight subscription. </p> <p>In the Quick Sight console, the Amazon Quick Sight subscription is sometimes referred to as a Quick Sight "account" even though it's technically not an account by itself. Instead, it's a subscription to the Amazon Quick Sight service for your Amazon Web Services account. The edition that you subscribe to applies to Quick in every Amazon Web Services Region where you use it.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountSettingsResponse) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import capo_quicksight.types.account_settings

        out["AccountSettings"] = capo_quicksight.types.account_settings.serialize_json(
            value["account_settings"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAccountSettingsResponse:
    out: DescribeAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccountSettings") is not None:
        import capo_quicksight.types.account_settings

        out["account_settings"] = (
            capo_quicksight.types.account_settings.deserialize_json(
                data["AccountSettings"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
