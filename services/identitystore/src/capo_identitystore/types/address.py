"""Generated from Smithy shape ``com.amazonaws.identitystore#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.boolean_type
    import capo_identitystore.types.sensitive_string_type


class Address(TypedDict, closed=True):
    street_address: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The street of the address.</p>"""
    locality: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string of the address locality.</p>"""
    region: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The region of the address.</p>"""
    postal_code: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The postal code of the address.</p>"""
    country: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The country of the address.</p>"""
    formatted: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing a formatted version of the address for display.</p>"""
    type: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string representing the type of address. For example, "Home."</p>"""
    primary: "capo_identitystore.types.boolean_type.BooleanType"
    """<p>A Boolean value representing whether this is the primary address for the associated resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Address) -> dict:
    out: dict = {}
    if "street_address" in value:
        out["StreetAddress"] = value["street_address"]
    if "locality" in value:
        out["Locality"] = value["locality"]
    if "region" in value:
        out["Region"] = value["region"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "country" in value:
        out["Country"] = value["country"]
    if "formatted" in value:
        out["Formatted"] = value["formatted"]
    if "type" in value:
        out["Type"] = value["type"]
    out["Primary"] = value.get("primary", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("StreetAddress") is not None:
        out["street_address"] = data["StreetAddress"]
    if data.get("Locality") is not None:
        out["locality"] = data["Locality"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("Formatted") is not None:
        out["formatted"] = data["Formatted"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    else:
        out["primary"] = False
    return out
