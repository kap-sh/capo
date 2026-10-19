"""Generated from Smithy shape ``com.amazonaws.shield#AssociateHealthCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.health_check_arn
    import capo_shield.types.protection_id


class AssociateHealthCheckRequest(TypedDict, closed=True):
    protection_id: "capo_shield.types.protection_id.ProtectionId"
    """<p>The unique identifier (ID) for the <a>Protection</a> object to add the health check association to. </p>"""
    health_check_arn: "capo_shield.types.health_check_arn.HealthCheckArn"
    """<p>The Amazon Resource Name (ARN) of the health check to associate with the protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateHealthCheckRequest) -> dict:
    out: dict = {}
    out["ProtectionId"] = value["protection_id"]
    out["HealthCheckArn"] = value["health_check_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateHealthCheckRequest:
    out: AssociateHealthCheckRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionId") is not None:
        out["protection_id"] = data["ProtectionId"]
    else:
        out["protection_id"] = ""
    if data.get("HealthCheckArn") is not None:
        out["health_check_arn"] = data["HealthCheckArn"]
    else:
        out["health_check_arn"] = ""
    return out
