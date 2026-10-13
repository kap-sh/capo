"""Generated from Smithy shape ``com.amazonaws.gamelift#RegisterComputeInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name
    import capo_gamelift.types.dns_name_input
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.non_zero_and_max_string


class RegisterComputeInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to register the compute to. You can use either the fleet ID or ARN value.</p>"""
    compute_name: NotRequired["capo_gamelift.types.compute_name.ComputeName"]
    """<p>A descriptive label for the compute resource.</p>"""
    certificate_path: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>The path to a TLS certificate on your compute resource. Amazon GameLift Servers doesn't validate the path and certificate.</p>"""
    dns_name: NotRequired["capo_gamelift.types.dns_name_input.DnsNameInput"]
    """<p>The DNS name of the compute resource. Amazon GameLift Servers requires either a DNS name or IP address.</p>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>The IP address of the compute resource. Amazon GameLift Servers requires either a DNS name or IP address. When registering an Anywhere fleet, an IP address is required.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The name of a custom location to associate with the compute resource being registered. This parameter is required when registering a compute for an Anywhere fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterComputeInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "certificate_path" in value:
        out["CertificatePath"] = value["certificate_path"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterComputeInput:
    out: RegisterComputeInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    if data.get("CertificatePath") is not None:
        out["certificate_path"] = data["CertificatePath"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out


def redact_sensitive(value: RegisterComputeInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_address" in value:
        out["ip_address"] = "*** Sensitive Data Redacted ***"
    return out
