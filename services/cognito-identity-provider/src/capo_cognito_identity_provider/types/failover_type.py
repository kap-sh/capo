"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#FailoverType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.health_check_id_type
    import capo_cognito_identity_provider.types.region_name_type


class FailoverType(TypedDict, closed=True):
    secondary_region: (
        "capo_cognito_identity_provider.types.region_name_type.RegionNameType"
    )
    """<p>The secondary Amazon Web Services Region to use for failover when the primary region becomes unavailable.</p>"""
    primary_route53_health_check_id: (
        "capo_cognito_identity_provider.types.health_check_id_type.HealthCheckIdType"
    )
    """<p>The ID of the Amazon Web Services Route53 healthcheck that controls routing. If the healthcheck is healthy, traffic will be routed to the primary replica, and if the healthcheck is unhealthy, traffic will be routed to the secondary region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailoverType) -> dict:
    out: dict = {}
    out["SecondaryRegion"] = value["secondary_region"]
    out["PrimaryRoute53HealthCheckId"] = value["primary_route53_health_check_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailoverType:
    out: FailoverType = {}  # type: ignore[typeddict-item]
    if data.get("SecondaryRegion") is not None:
        out["secondary_region"] = data["SecondaryRegion"]
    else:
        out["secondary_region"] = ""
    if data.get("PrimaryRoute53HealthCheckId") is not None:
        out["primary_route53_health_check_id"] = data["PrimaryRoute53HealthCheckId"]
    else:
        out["primary_route53_health_check_id"] = ""
    return out
