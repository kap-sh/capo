"""Generated from Smithy shape ``com.amazonaws.iam#GetMFADeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.certification_map_type
    import capo_iam.types.date_type
    import capo_iam.types.serial_number_type
    import capo_iam.types.user_name_type


class GetMFADeviceResponse(TypedDict, closed=True):
    user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>The friendly name identifying the user.</p>"""
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>Serial number that uniquely identifies the MFA device. For this API, we only accept FIDO security key <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">ARNs</a>.</p>"""
    enable_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date that a specified user's MFA device was first enabled.</p>"""
    certifications: NotRequired[
        "capo_iam.types.certification_map_type.CertificationMapType"
    ]
    """<p>The certifications of a specified user's MFA device. We currently provide FIPS-140-2, FIPS-140-3, and FIDO certification levels obtained from <a href="https://fidoalliance.org/metadata/"> FIDO Alliance Metadata Service (MDS)</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMFADeviceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    if "enable_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["enable_date"], pairs, f"{key_prefix}EnableDate"
        )
    if "certifications" in value:
        import capo_iam.types.certification_map_type

        capo_iam.types.certification_map_type.serialize_query(
            value["certifications"], pairs, f"{key_prefix}Certifications"
        )


def deserialize_query(el: Element) -> GetMFADeviceResponse:
    out: GetMFADeviceResponse = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("GetMFADeviceResponse.serial_number required")
    child_enable_date = el.find("EnableDate")
    if child_enable_date is not None:
        import capo_iam.types.date_type

        out["enable_date"] = capo_iam.types.date_type.deserialize_query(
            child_enable_date
        )
    child_certifications = el.find("Certifications")
    if child_certifications is not None:
        import capo_iam.types.certification_map_type

        out["certifications"] = capo_iam.types.certification_map_type.deserialize_query(
            child_certifications
        )
    return out
