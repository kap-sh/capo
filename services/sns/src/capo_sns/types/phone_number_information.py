"""Generated from Smithy shape ``com.amazonaws.sns#PhoneNumberInformation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.iso2_country_code
    import capo_sns.types.number_capability_list
    import capo_sns.types.phone_number
    import capo_sns.types.route_type
    import capo_sns.types.string
    import capo_sns.types.timestamp


class PhoneNumberInformation(TypedDict, closed=True):
    created_at: NotRequired["capo_sns.types.timestamp.Timestamp"]
    """<p>The date and time when the phone number was created.</p>"""
    phone_number: NotRequired["capo_sns.types.phone_number.PhoneNumber"]
    """<p>The phone number.</p>"""
    status: NotRequired["capo_sns.types.string.String"]
    """<p>The status of the phone number.</p>"""
    iso2_country_code: NotRequired["capo_sns.types.iso2_country_code.Iso2CountryCode"]
    """<p>The two-character code for the country or region, in ISO 3166-1 alpha-2 format.</p>"""
    route_type: NotRequired["capo_sns.types.route_type.RouteType"]
    """<p>The list of supported routes.</p>"""
    number_capabilities: NotRequired[
        "capo_sns.types.number_capability_list.NumberCapabilityList"
    ]
    """<p>The capabilities of each phone number.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PhoneNumberInformation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "created_at" in value:
        import capo_sns.types.timestamp

        capo_sns.types.timestamp.serialize_query(
            value["created_at"], pairs, f"{key_prefix}CreatedAt"
        )
    if "phone_number" in value:
        pairs.append((f"{key_prefix}PhoneNumber", str(value["phone_number"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "iso2_country_code" in value:
        pairs.append((f"{key_prefix}Iso2CountryCode", str(value["iso2_country_code"])))
    if "route_type" in value:
        import capo_sns.types.route_type

        capo_sns.types.route_type.serialize_query(
            value["route_type"], pairs, f"{key_prefix}RouteType"
        )
    if "number_capabilities" in value:
        import capo_sns.types.number_capability_list

        capo_sns.types.number_capability_list.serialize_query(
            value["number_capabilities"], pairs, f"{key_prefix}NumberCapabilities"
        )


def deserialize_query(el: Element) -> PhoneNumberInformation:
    out: PhoneNumberInformation = {}  # type: ignore[typeddict-item]
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import capo_sns.types.timestamp

        out["created_at"] = capo_sns.types.timestamp.deserialize_query(child_created_at)
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_iso2_country_code = el.find("Iso2CountryCode")
    if child_iso2_country_code is not None:
        out["iso2_country_code"] = str(child_iso2_country_code.text or "")
    child_route_type = el.find("RouteType")
    if child_route_type is not None:
        import capo_sns.types.route_type

        out["route_type"] = capo_sns.types.route_type.deserialize_query(
            child_route_type
        )
    child_number_capabilities = el.find("NumberCapabilities")
    if child_number_capabilities is not None:
        import capo_sns.types.number_capability_list

        out["number_capabilities"] = (
            capo_sns.types.number_capability_list.deserialize_query(
                child_number_capabilities
            )
        )
    return out


def redact_sensitive(value: PhoneNumberInformation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    return out
