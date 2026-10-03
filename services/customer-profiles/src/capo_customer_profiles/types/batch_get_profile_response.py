"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_get_profile_error_list
    import capo_customer_profiles.types.profile_list


class BatchGetProfileResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_customer_profiles.types.batch_get_profile_error_list.BatchGetProfileErrorList"
    ]
    """<p>For information about the errors that are common to all actions, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""
    profiles: NotRequired["capo_customer_profiles.types.profile_list.ProfileList"]
    """<p>Array of Profile Objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_customer_profiles.types.batch_get_profile_error_list

        out["Errors"] = (
            capo_customer_profiles.types.batch_get_profile_error_list.serialize_json(
                value["errors"]
            )
        )
    if "profiles" in value:
        import capo_customer_profiles.types.profile_list

        out["Profiles"] = capo_customer_profiles.types.profile_list.serialize_json(
            value["profiles"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetProfileResponse:
    out: BatchGetProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_customer_profiles.types.batch_get_profile_error_list

        out["errors"] = (
            capo_customer_profiles.types.batch_get_profile_error_list.deserialize_json(
                data["Errors"]
            )
        )
    if data.get("Profiles") is not None:
        import capo_customer_profiles.types.profile_list

        out["profiles"] = capo_customer_profiles.types.profile_list.deserialize_json(
            data["Profiles"]
        )
    return out
