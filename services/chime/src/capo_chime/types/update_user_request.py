"""Generated from Smithy shape ``com.amazonaws.chime#UpdateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.alexa_for_business_metadata
    import capo_chime.types.license
    import capo_chime.types.non_empty_string
    import capo_chime.types.user_type


class UpdateUserRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The user ID.</p>"""
    license_type: NotRequired["capo_chime.types.license.License"]
    """<p>The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to.</p>"""
    user_type: NotRequired["capo_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""
    alexa_for_business_metadata: NotRequired[
        "capo_chime.types.alexa_for_business_metadata.AlexaForBusinessMetadata"
    ]
    """<p>The Alexa for Business metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    if "license_type" in value:
        import capo_chime.types.license

        out["LicenseType"] = capo_chime.types.license.serialize_json(
            value["license_type"]
        )
    if "user_type" in value:
        import capo_chime.types.user_type

        out["UserType"] = capo_chime.types.user_type.serialize_json(value["user_type"])
    if "alexa_for_business_metadata" in value:
        import capo_chime.types.alexa_for_business_metadata

        out["AlexaForBusinessMetadata"] = (
            capo_chime.types.alexa_for_business_metadata.serialize_json(
                value["alexa_for_business_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseType") is not None:
        import capo_chime.types.license

        out["license_type"] = capo_chime.types.license.deserialize_json(
            data["LicenseType"]
        )
    if data.get("UserType") is not None:
        import capo_chime.types.user_type

        out["user_type"] = capo_chime.types.user_type.deserialize_json(data["UserType"])
    if data.get("AlexaForBusinessMetadata") is not None:
        import capo_chime.types.alexa_for_business_metadata

        out["alexa_for_business_metadata"] = (
            capo_chime.types.alexa_for_business_metadata.deserialize_json(
                data["AlexaForBusinessMetadata"]
            )
        )
    return out


def redact_sensitive(value: UpdateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "alexa_for_business_metadata" in value:
        import capo_chime.types.alexa_for_business_metadata

        out["alexa_for_business_metadata"] = (
            capo_chime.types.alexa_for_business_metadata.redact_sensitive(
                value["alexa_for_business_metadata"]
            )
        )
    return out
