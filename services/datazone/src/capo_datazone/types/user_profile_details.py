"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.iam_user_profile_details
    import capo_datazone.types.sso_user_profile_details


class UserProfileDetailsIamMember(TypedDict, closed=True):
    iam: "capo_datazone.types.iam_user_profile_details.IamUserProfileDetails"


class UserProfileDetailsSsoMember(TypedDict, closed=True):
    sso: "capo_datazone.types.sso_user_profile_details.SsoUserProfileDetails"


UserProfileDetails: TypeAlias = (
    UserProfileDetailsIamMember | UserProfileDetailsSsoMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UserProfileDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "iam" in value:
        import capo_datazone.types.iam_user_profile_details

        return {
            "iam": capo_datazone.types.iam_user_profile_details.serialize_json(
                value["iam"]
            )
        }
    elif "sso" in value:
        import capo_datazone.types.sso_user_profile_details

        return {
            "sso": capo_datazone.types.sso_user_profile_details.serialize_json(
                value["sso"]
            )
        }
    else:
        raise SerializationError("UserProfileDetails: no variant present")


def deserialize_json(data: dict) -> UserProfileDetails:
    if data.get("iam") is not None:
        import capo_datazone.types.iam_user_profile_details

        return {
            "iam": capo_datazone.types.iam_user_profile_details.deserialize_json(
                data["iam"]
            )
        }
    elif data.get("sso") is not None:
        import capo_datazone.types.sso_user_profile_details

        return {
            "sso": capo_datazone.types.sso_user_profile_details.deserialize_json(
                data["sso"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("UserProfileDetails: no recognized variant key")


def redact_sensitive(value: UserProfileDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sso" in value:
        import capo_datazone.types.sso_user_profile_details

        out["sso"] = capo_datazone.types.sso_user_profile_details.redact_sensitive(
            value["sso"]
        )
    return out
