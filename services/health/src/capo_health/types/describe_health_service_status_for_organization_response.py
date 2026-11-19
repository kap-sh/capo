"""Generated from Smithy shape ``com.amazonaws.health#DescribeHealthServiceStatusForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.health_service_access_status_for_organization


class DescribeHealthServiceStatusForOrganizationResponse(TypedDict, closed=True):
    health_service_access_status_for_organization: NotRequired[
        "capo_health.types.health_service_access_status_for_organization.healthServiceAccessStatusForOrganization"
    ]
    """<p>Information about the status of enabling or disabling the Health organizational view feature in your organization.</p> <p>Valid values are <code>ENABLED | DISABLED | PENDING</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeHealthServiceStatusForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "health_service_access_status_for_organization" in value:
        out["healthServiceAccessStatusForOrganization"] = value[
            "health_service_access_status_for_organization"
        ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeHealthServiceStatusForOrganizationResponse:
    out: DescribeHealthServiceStatusForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("healthServiceAccessStatusForOrganization") is not None:
        out["health_service_access_status_for_organization"] = data[
            "healthServiceAccessStatusForOrganization"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeHealthServiceStatusForOrganizationResponse) -> dict:
    out: dict = {}
    if "health_service_access_status_for_organization" in value:
        out["healthServiceAccessStatusForOrganization"] = value[
            "health_service_access_status_for_organization"
        ]
    return out


def deserialize_cbor(data: dict) -> DescribeHealthServiceStatusForOrganizationResponse:
    out: DescribeHealthServiceStatusForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("healthServiceAccessStatusForOrganization") is not None:
        out["health_service_access_status_for_organization"] = data[
            "healthServiceAccessStatusForOrganization"
        ]
    return out
