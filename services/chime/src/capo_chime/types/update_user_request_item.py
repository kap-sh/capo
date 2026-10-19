"""Generated from Smithy shape ``com.amazonaws.chime#UpdateUserRequestItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.alexa_for_business_metadata
    import capo_chime.types.license
    import capo_chime.types.non_empty_string
    import capo_chime.types.user_type


class UpdateUserRequestItem(TypedDict, closed=True):
    user_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The user ID.</p>"""
    license_type: NotRequired["capo_chime.types.license.License"]
    """<p>The user license type.</p>"""
    user_type: NotRequired["capo_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""
    alexa_for_business_metadata: NotRequired[
        "capo_chime.types.alexa_for_business_metadata.AlexaForBusinessMetadata"
    ]
    """<p>The Alexa for Business metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequestItem) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
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


def deserialize_json(data: dict) -> UpdateUserRequestItem:
    out: UpdateUserRequestItem = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
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


def redact_sensitive(value: UpdateUserRequestItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "alexa_for_business_metadata" in value:
        import capo_chime.types.alexa_for_business_metadata

        out["alexa_for_business_metadata"] = (
            capo_chime.types.alexa_for_business_metadata.redact_sensitive(
                value["alexa_for_business_metadata"]
            )
        )
    return out
