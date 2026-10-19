"""Generated from Smithy shape ``com.amazonaws.shield#GetSubscriptionStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.subscription_state


class GetSubscriptionStateResponse(TypedDict, closed=True):
    subscription_state: "capo_shield.types.subscription_state.SubscriptionState"
    """<p>The status of the subscription.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSubscriptionStateResponse) -> dict:
    out: dict = {}
    import capo_shield.types.subscription_state

    out["SubscriptionState"] = (
        capo_shield.types.subscription_state.serialize_aws_json_1_1(
            value["subscription_state"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSubscriptionStateResponse:
    out: GetSubscriptionStateResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionState") is not None:
        import capo_shield.types.subscription_state

        out["subscription_state"] = (
            capo_shield.types.subscription_state.deserialize_aws_json_1_1(
                data["SubscriptionState"]
            )
        )
    else:
        import typing

        out["subscription_state"] = typing.cast(
            "capo_shield.types.subscription_state.SubscriptionState", ""
        )
    return out
