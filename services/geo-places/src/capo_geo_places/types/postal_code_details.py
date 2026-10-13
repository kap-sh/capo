"""Generated from Smithy shape ``com.amazonaws.geoplaces#PostalCodeDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.postal_authority
    import capo_geo_places.types.postal_code_type
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.usps_zip
    import capo_geo_places.types.usps_zip_plus4


class PostalCodeDetails(TypedDict, closed=True):
    postal_code: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess. </p>"""
    postal_authority: NotRequired[
        "capo_geo_places.types.postal_authority.PostalAuthority"
    ]
    """<p>The postal authority or entity. This could be a governmental authority, a regulatory authority, or a designated postal operator.</p>"""
    postal_code_type: NotRequired[
        "capo_geo_places.types.postal_code_type.PostalCodeType"
    ]
    """<p>The postal code type.</p>"""
    usps_zip: NotRequired["capo_geo_places.types.usps_zip.UspsZip"]
    """<p>The ZIP Classification Code, or in other words what type of postal code is it.</p>"""
    usps_zip_plus4: NotRequired["capo_geo_places.types.usps_zip_plus4.UspsZipPlus4"]
    """<p>The USPS ZIP+4 Record Type Code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostalCodeDetails) -> dict:
    out: dict = {}
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "postal_authority" in value:
        import capo_geo_places.types.postal_authority

        out["PostalAuthority"] = capo_geo_places.types.postal_authority.serialize_json(
            value["postal_authority"]
        )
    if "postal_code_type" in value:
        import capo_geo_places.types.postal_code_type

        out["PostalCodeType"] = capo_geo_places.types.postal_code_type.serialize_json(
            value["postal_code_type"]
        )
    if "usps_zip" in value:
        import capo_geo_places.types.usps_zip

        out["UspsZip"] = capo_geo_places.types.usps_zip.serialize_json(
            value["usps_zip"]
        )
    if "usps_zip_plus4" in value:
        import capo_geo_places.types.usps_zip_plus4

        out["UspsZipPlus4"] = capo_geo_places.types.usps_zip_plus4.serialize_json(
            value["usps_zip_plus4"]
        )
    return out


def deserialize_json(data: dict) -> PostalCodeDetails:
    out: PostalCodeDetails = {}  # type: ignore[typeddict-item]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("PostalAuthority") is not None:
        import capo_geo_places.types.postal_authority

        out["postal_authority"] = (
            capo_geo_places.types.postal_authority.deserialize_json(
                data["PostalAuthority"]
            )
        )
    if data.get("PostalCodeType") is not None:
        import capo_geo_places.types.postal_code_type

        out["postal_code_type"] = (
            capo_geo_places.types.postal_code_type.deserialize_json(
                data["PostalCodeType"]
            )
        )
    if data.get("UspsZip") is not None:
        import capo_geo_places.types.usps_zip

        out["usps_zip"] = capo_geo_places.types.usps_zip.deserialize_json(
            data["UspsZip"]
        )
    if data.get("UspsZipPlus4") is not None:
        import capo_geo_places.types.usps_zip_plus4

        out["usps_zip_plus4"] = capo_geo_places.types.usps_zip_plus4.deserialize_json(
            data["UspsZipPlus4"]
        )
    return out


def redact_sensitive(value: PostalCodeDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "postal_code" in value:
        out["postal_code"] = "*** Sensitive Data Redacted ***"
    if "postal_authority" in value:
        out["postal_authority"] = "*** Sensitive Data Redacted ***"
    if "postal_code_type" in value:
        out["postal_code_type"] = "*** Sensitive Data Redacted ***"
    if "usps_zip" in value:
        import capo_geo_places.types.usps_zip

        out["usps_zip"] = capo_geo_places.types.usps_zip.redact_sensitive(
            value["usps_zip"]
        )
    if "usps_zip_plus4" in value:
        import capo_geo_places.types.usps_zip_plus4

        out["usps_zip_plus4"] = capo_geo_places.types.usps_zip_plus4.redact_sensitive(
            value["usps_zip_plus4"]
        )
    return out
