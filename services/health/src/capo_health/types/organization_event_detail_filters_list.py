"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventDetailFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_account_filter

OrganizationEventDetailFiltersList: TypeAlias = list[
    "capo_health.types.event_account_filter.EventAccountFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventDetailFiltersList) -> list:
    import capo_health.types.event_account_filter

    out: list = []
    for item in value:
        out.append(capo_health.types.event_account_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationEventDetailFiltersList:
    import capo_health.types.event_account_filter

    out: OrganizationEventDetailFiltersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.event_account_filter.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationEventDetailFiltersList) -> list:
    import capo_health.types.event_account_filter

    out: list = []
    for item in value:
        out.append(capo_health.types.event_account_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OrganizationEventDetailFiltersList:
    import capo_health.types.event_account_filter

    out: OrganizationEventDetailFiltersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_account_filter.deserialize_cbor(item))
    return out
