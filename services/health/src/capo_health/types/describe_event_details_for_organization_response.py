"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventDetailsForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.describe_event_details_for_organization_failed_set
    import capo_health.types.describe_event_details_for_organization_successful_set


class DescribeEventDetailsForOrganizationResponse(TypedDict, closed=True):
    successful_set: NotRequired[
        "capo_health.types.describe_event_details_for_organization_successful_set.DescribeEventDetailsForOrganizationSuccessfulSet"
    ]
    """<p>Information about the events that could be retrieved.</p>"""
    failed_set: NotRequired[
        "capo_health.types.describe_event_details_for_organization_failed_set.DescribeEventDetailsForOrganizationFailedSet"
    ]
    """<p>Error messages for any events that could not be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventDetailsForOrganizationResponse) -> dict:
    out: dict = {}
    if "successful_set" in value:
        import capo_health.types.describe_event_details_for_organization_successful_set

        out["successfulSet"] = (
            capo_health.types.describe_event_details_for_organization_successful_set.serialize_aws_json_1_1(
                value["successful_set"]
            )
        )
    if "failed_set" in value:
        import capo_health.types.describe_event_details_for_organization_failed_set

        out["failedSet"] = (
            capo_health.types.describe_event_details_for_organization_failed_set.serialize_aws_json_1_1(
                value["failed_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventDetailsForOrganizationResponse:
    out: DescribeEventDetailsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("successfulSet") is not None:
        import capo_health.types.describe_event_details_for_organization_successful_set

        out["successful_set"] = (
            capo_health.types.describe_event_details_for_organization_successful_set.deserialize_aws_json_1_1(
                data["successfulSet"]
            )
        )
    if data.get("failedSet") is not None:
        import capo_health.types.describe_event_details_for_organization_failed_set

        out["failed_set"] = (
            capo_health.types.describe_event_details_for_organization_failed_set.deserialize_aws_json_1_1(
                data["failedSet"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventDetailsForOrganizationResponse) -> dict:
    out: dict = {}
    if "successful_set" in value:
        import capo_health.types.describe_event_details_for_organization_successful_set

        out["successfulSet"] = (
            capo_health.types.describe_event_details_for_organization_successful_set.serialize_cbor(
                value["successful_set"]
            )
        )
    if "failed_set" in value:
        import capo_health.types.describe_event_details_for_organization_failed_set

        out["failedSet"] = (
            capo_health.types.describe_event_details_for_organization_failed_set.serialize_cbor(
                value["failed_set"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEventDetailsForOrganizationResponse:
    out: DescribeEventDetailsForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("successfulSet") is not None:
        import capo_health.types.describe_event_details_for_organization_successful_set

        out["successful_set"] = (
            capo_health.types.describe_event_details_for_organization_successful_set.deserialize_cbor(
                data["successfulSet"]
            )
        )
    if data.get("failedSet") is not None:
        import capo_health.types.describe_event_details_for_organization_failed_set

        out["failed_set"] = (
            capo_health.types.describe_event_details_for_organization_failed_set.deserialize_cbor(
                data["failedSet"]
            )
        )
    return out
