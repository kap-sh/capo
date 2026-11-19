"""Generated from Smithy shape ``com.amazonaws.lightsail#CheckSubdomainAvailabilityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.string


class CheckSubdomainAvailabilityResult(TypedDict, closed=True):
    available: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether the subdomain is available to create.</p>"""
    reservation_expires_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the reservation of the subdomain expires.</p> <p>The expiry is returned only when your account holds an active reservation for the subdomain.</p>"""
    subdomain_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The subdomain that was checked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckSubdomainAvailabilityResult) -> dict:
    out: dict = {}
    if "available" in value:
        out["available"] = value["available"]
    if "reservation_expires_at" in value:
        import capo_lightsail.types.iso_date

        out["reservationExpiresAt"] = (
            capo_lightsail.types.iso_date.serialize_aws_json_1_1(
                value["reservation_expires_at"]
            )
        )
    if "subdomain_name" in value:
        out["subdomainName"] = value["subdomain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckSubdomainAvailabilityResult:
    out: CheckSubdomainAvailabilityResult = {}  # type: ignore[typeddict-item]
    if data.get("available") is not None:
        out["available"] = data["available"]
    if data.get("reservationExpiresAt") is not None:
        import capo_lightsail.types.iso_date

        out["reservation_expires_at"] = (
            capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
                data["reservationExpiresAt"]
            )
        )
    if data.get("subdomainName") is not None:
        out["subdomain_name"] = data["subdomainName"]
    return out
