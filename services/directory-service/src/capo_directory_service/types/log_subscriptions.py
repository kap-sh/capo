"""Generated from Smithy shape ``com.amazonaws.directoryservice#LogSubscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.log_subscription

LogSubscriptions: TypeAlias = list[
    "capo_directory_service.types.log_subscription.LogSubscription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogSubscriptions) -> list:
    import capo_directory_service.types.log_subscription

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.log_subscription.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogSubscriptions:
    import capo_directory_service.types.log_subscription

    out: LogSubscriptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.log_subscription.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogSubscriptions) -> list:
    import capo_directory_service.types.log_subscription

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.log_subscription.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LogSubscriptions:
    import capo_directory_service.types.log_subscription

    out: LogSubscriptions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.log_subscription.deserialize_cbor(item))
    return out
