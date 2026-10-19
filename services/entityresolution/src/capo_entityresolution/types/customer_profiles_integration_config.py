"""Generated from Smithy shape ``com.amazonaws.entityresolution#CustomerProfilesIntegrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.customer_profiles_domain_arn
    import capo_entityresolution.types.customer_profiles_object_type_arn


class CustomerProfilesIntegrationConfig(TypedDict, closed=True):
    domain_arn: "capo_entityresolution.types.customer_profiles_domain_arn.CustomerProfilesDomainArn"
    """<p>The Amazon Resource Name (ARN) of the Customer Profiles domain where the matched output will be sent.</p>"""
    object_type_arn: "capo_entityresolution.types.customer_profiles_object_type_arn.CustomerProfilesObjectTypeArn"
    """<p>The Amazon Resource Name (ARN) of the Customer Profiles object type that defines the structure for the matched customer data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfilesIntegrationConfig) -> dict:
    out: dict = {}
    out["domainArn"] = value["domain_arn"]
    out["objectTypeArn"] = value["object_type_arn"]
    return out


def deserialize_json(data: dict) -> CustomerProfilesIntegrationConfig:
    out: CustomerProfilesIntegrationConfig = {}  # type: ignore[typeddict-item]
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    if data.get("objectTypeArn") is not None:
        out["object_type_arn"] = data["objectTypeArn"]
    else:
        out["object_type_arn"] = ""
    return out
