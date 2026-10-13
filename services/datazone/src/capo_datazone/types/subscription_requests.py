"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionRequests``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.subscription_request_summary

SubscriptionRequests: TypeAlias = list[
    "capo_datazone.types.subscription_request_summary.SubscriptionRequestSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionRequests) -> list:
    import capo_datazone.types.subscription_request_summary

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.subscription_request_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubscriptionRequests:
    import capo_datazone.types.subscription_request_summary

    out: SubscriptionRequests = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_datazone.types.subscription_request_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SubscriptionRequests) -> list[Any]:
    import capo_datazone.types.subscription_request_summary

    return [
        capo_datazone.types.subscription_request_summary.redact_sensitive(item)
        for item in value
    ]
