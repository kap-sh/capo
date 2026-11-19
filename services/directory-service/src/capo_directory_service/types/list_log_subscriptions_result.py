"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListLogSubscriptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.log_subscriptions
    import capo_directory_service.types.next_token


class ListLogSubscriptionsResult(TypedDict, closed=True):
    log_subscriptions: NotRequired[
        "capo_directory_service.types.log_subscriptions.LogSubscriptions"
    ]
    """<p>A list of active <a>LogSubscription</a> objects for calling the Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The token for the next set of items to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogSubscriptionsResult) -> dict:
    out: dict = {}
    if "log_subscriptions" in value:
        import capo_directory_service.types.log_subscriptions

        out["LogSubscriptions"] = (
            capo_directory_service.types.log_subscriptions.serialize_aws_json_1_1(
                value["log_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogSubscriptionsResult:
    out: ListLogSubscriptionsResult = {}  # type: ignore[typeddict-item]
    if data.get("LogSubscriptions") is not None:
        import capo_directory_service.types.log_subscriptions

        out["log_subscriptions"] = (
            capo_directory_service.types.log_subscriptions.deserialize_aws_json_1_1(
                data["LogSubscriptions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLogSubscriptionsResult) -> dict:
    out: dict = {}
    if "log_subscriptions" in value:
        import capo_directory_service.types.log_subscriptions

        out["LogSubscriptions"] = (
            capo_directory_service.types.log_subscriptions.serialize_cbor(
                value["log_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListLogSubscriptionsResult:
    out: ListLogSubscriptionsResult = {}  # type: ignore[typeddict-item]
    if data.get("LogSubscriptions") is not None:
        import capo_directory_service.types.log_subscriptions

        out["log_subscriptions"] = (
            capo_directory_service.types.log_subscriptions.deserialize_cbor(
                data["LogSubscriptions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
