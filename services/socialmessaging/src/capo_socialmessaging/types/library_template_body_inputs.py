"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LibraryTemplateBodyInputs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.add_contact_number
    import capo_socialmessaging.types.add_learn_more_link
    import capo_socialmessaging.types.add_security_recommendation
    import capo_socialmessaging.types.add_track_package_link
    import capo_socialmessaging.types.code_expiration_minutes


class LibraryTemplateBodyInputs(TypedDict, closed=True):
    add_contact_number: NotRequired[
        "capo_socialmessaging.types.add_contact_number.AddContactNumber"
    ]
    """<p>When true, includes a contact number in the template body.</p>"""
    add_learn_more_link: NotRequired[
        "capo_socialmessaging.types.add_learn_more_link.AddLearnMoreLink"
    ]
    """<p>When true, includes a "learn more" link in the template body.</p>"""
    add_security_recommendation: NotRequired[
        "capo_socialmessaging.types.add_security_recommendation.AddSecurityRecommendation"
    ]
    """<p>When true, includes security recommendations in the template body.</p>"""
    add_track_package_link: NotRequired[
        "capo_socialmessaging.types.add_track_package_link.AddTrackPackageLink"
    ]
    """<p>When true, includes a package tracking link in the template body.</p>"""
    code_expiration_minutes: NotRequired[
        "capo_socialmessaging.types.code_expiration_minutes.CodeExpirationMinutes"
    ]
    """<p>The number of minutes until a verification code or OTP expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LibraryTemplateBodyInputs) -> dict:
    out: dict = {}
    if "add_contact_number" in value:
        out["addContactNumber"] = value["add_contact_number"]
    if "add_learn_more_link" in value:
        out["addLearnMoreLink"] = value["add_learn_more_link"]
    if "add_security_recommendation" in value:
        out["addSecurityRecommendation"] = value["add_security_recommendation"]
    if "add_track_package_link" in value:
        out["addTrackPackageLink"] = value["add_track_package_link"]
    if "code_expiration_minutes" in value:
        out["codeExpirationMinutes"] = value["code_expiration_minutes"]
    return out


def deserialize_json(data: dict) -> LibraryTemplateBodyInputs:
    out: LibraryTemplateBodyInputs = {}  # type: ignore[typeddict-item]
    if data.get("addContactNumber") is not None:
        out["add_contact_number"] = data["addContactNumber"]
    if data.get("addLearnMoreLink") is not None:
        out["add_learn_more_link"] = data["addLearnMoreLink"]
    if data.get("addSecurityRecommendation") is not None:
        out["add_security_recommendation"] = data["addSecurityRecommendation"]
    if data.get("addTrackPackageLink") is not None:
        out["add_track_package_link"] = data["addTrackPackageLink"]
    if data.get("codeExpirationMinutes") is not None:
        out["code_expiration_minutes"] = data["codeExpirationMinutes"]
    return out
