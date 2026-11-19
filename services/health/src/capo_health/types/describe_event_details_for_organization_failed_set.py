"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventDetailsForOrganizationFailedSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.organization_event_details_error_item

DescribeEventDetailsForOrganizationFailedSet: TypeAlias = list[
    "capo_health.types.organization_event_details_error_item.OrganizationEventDetailsErrorItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventDetailsForOrganizationFailedSet) -> list:
    import capo_health.types.organization_event_details_error_item

    out: list = []
    for item in value:
        out.append(
            capo_health.types.organization_event_details_error_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> DescribeEventDetailsForOrganizationFailedSet:
    import capo_health.types.organization_event_details_error_item

    out: DescribeEventDetailsForOrganizationFailedSet = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.organization_event_details_error_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventDetailsForOrganizationFailedSet) -> list:
    import capo_health.types.organization_event_details_error_item

    out: list = []
    for item in value:
        out.append(
            capo_health.types.organization_event_details_error_item.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> DescribeEventDetailsForOrganizationFailedSet:
    import capo_health.types.organization_event_details_error_item

    out: DescribeEventDetailsForOrganizationFailedSet = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.organization_event_details_error_item.deserialize_cbor(
                item
            )
        )
    return out
