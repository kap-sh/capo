"""Generated from Smithy shape ``com.amazonaws.appflow#CustomerProfilesDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.domain_name
    import capo_appflow.types.object_type_name


class CustomerProfilesDestinationProperties(TypedDict, closed=True):
    domain_name: "capo_appflow.types.domain_name.DomainName"
    """<p> The unique name of the Connect Customer Customer Profiles domain. </p>"""
    object_type_name: NotRequired["capo_appflow.types.object_type_name.ObjectTypeName"]
    """<p> The object specified in the Connect Customer Customer Profiles flow destination. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfilesDestinationProperties) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    if "object_type_name" in value:
        out["objectTypeName"] = value["object_type_name"]
    return out


def deserialize_json(data: dict) -> CustomerProfilesDestinationProperties:
    out: CustomerProfilesDestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("objectTypeName") is not None:
        out["object_type_name"] = data["objectTypeName"]
    return out
