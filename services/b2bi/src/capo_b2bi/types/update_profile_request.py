"""Generated from Smithy shape ``com.amazonaws.b2bi#UpdateProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.business_name
    import capo_b2bi.types.email
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.profile_name


class UpdateProfileRequest(TypedDict, closed=True):
    profile_id: "capo_b2bi.types.profile_id.ProfileId"
    """<p>Specifies the unique, system-generated identifier for the profile.</p>"""
    name: NotRequired["capo_b2bi.types.profile_name.ProfileName"]
    """<p>The name of the profile, used to identify it.</p>"""
    email: NotRequired["capo_b2bi.types.email.Email"]
    """<p>Specifies the email address associated with this customer profile.</p>"""
    phone: NotRequired["capo_b2bi.types.phone.Phone"]
    """<p>Specifies the phone number associated with the profile.</p>"""
    business_name: NotRequired["capo_b2bi.types.business_name.BusinessName"]
    """<p>Specifies the name for the business associated with this profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProfileRequest) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    if "phone" in value:
        out["phone"] = value["phone"]
    if "business_name" in value:
        out["businessName"] = value["business_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProfileRequest:
    out: UpdateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("UpdateProfileRequest.profile_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    if data.get("phone") is not None:
        out["phone"] = data["phone"]
    if data.get("businessName") is not None:
        out["business_name"] = data["businessName"]
    return out


def redact_sensitive(value: UpdateProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    return out
