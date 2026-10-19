"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CustomerProfilesIntegrationIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn


class CustomerProfilesIntegrationIdentifier(TypedDict, closed=True):
    domain_arn: "capo_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfilesIntegrationIdentifier) -> dict:
    out: dict = {}
    out["domainArn"] = value["domain_arn"]
    return out


def deserialize_json(data: dict) -> CustomerProfilesIntegrationIdentifier:
    out: CustomerProfilesIntegrationIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    return out
