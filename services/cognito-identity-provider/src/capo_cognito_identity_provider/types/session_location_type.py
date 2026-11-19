"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SessionLocationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.session_location_city_type
    import capo_cognito_identity_provider.types.session_location_country_type


class SessionLocationType(TypedDict, closed=True):
    city: NotRequired[
        "capo_cognito_identity_provider.types.session_location_city_type.SessionLocationCityType"
    ]
    """<p>The city of the most recent activity on the session, derived from the IP address. This value can be null if geo-IP resolution fails. The maximum length is 256 characters.</p>"""
    country: NotRequired[
        "capo_cognito_identity_provider.types.session_location_country_type.SessionLocationCountryType"
    ]
    """<p>The country of the most recent activity on the session, derived from the IP address and returned in English (for example, <code>United States</code>). This is a country name as returned by the geo-IP database, not an ISO country code, and can be <code>unknown</code> if geo-IP resolution fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionLocationType) -> dict:
    out: dict = {}
    if "city" in value:
        out["City"] = value["city"]
    if "country" in value:
        out["Country"] = value["country"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionLocationType:
    out: SessionLocationType = {}  # type: ignore[typeddict-item]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    return out
