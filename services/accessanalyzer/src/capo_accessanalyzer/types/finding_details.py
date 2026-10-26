"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.external_access_details
    import capo_accessanalyzer.types.internal_access_details
    import capo_accessanalyzer.types.unused_iam_role_details
    import capo_accessanalyzer.types.unused_iam_user_access_key_details
    import capo_accessanalyzer.types.unused_iam_user_password_details
    import capo_accessanalyzer.types.unused_permission_details


class _FindingDetails_internalAccessDetails(TypedDict, closed=True):
    internalAccessDetails: (
        "capo_accessanalyzer.types.internal_access_details.InternalAccessDetails"
    )


class _FindingDetails_externalAccessDetails(TypedDict, closed=True):
    externalAccessDetails: (
        "capo_accessanalyzer.types.external_access_details.ExternalAccessDetails"
    )


class _FindingDetails_unusedPermissionDetails(TypedDict, closed=True):
    unusedPermissionDetails: (
        "capo_accessanalyzer.types.unused_permission_details.UnusedPermissionDetails"
    )


class _FindingDetails_unusedIamUserAccessKeyDetails(TypedDict, closed=True):
    unusedIamUserAccessKeyDetails: "capo_accessanalyzer.types.unused_iam_user_access_key_details.UnusedIamUserAccessKeyDetails"


class _FindingDetails_unusedIamRoleDetails(TypedDict, closed=True):
    unusedIamRoleDetails: (
        "capo_accessanalyzer.types.unused_iam_role_details.UnusedIamRoleDetails"
    )


class _FindingDetails_unusedIamUserPasswordDetails(TypedDict, closed=True):
    unusedIamUserPasswordDetails: "capo_accessanalyzer.types.unused_iam_user_password_details.UnusedIamUserPasswordDetails"


FindingDetails: TypeAlias = (
    _FindingDetails_internalAccessDetails
    | _FindingDetails_externalAccessDetails
    | _FindingDetails_unusedPermissionDetails
    | _FindingDetails_unusedIamUserAccessKeyDetails
    | _FindingDetails_unusedIamRoleDetails
    | _FindingDetails_unusedIamUserPasswordDetails
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FindingDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "internalAccessDetails" in value:
        import capo_accessanalyzer.types.internal_access_details

        return {
            "internalAccessDetails": capo_accessanalyzer.types.internal_access_details.serialize_json(
                value["internalAccessDetails"]
            )
        }
    elif "externalAccessDetails" in value:
        import capo_accessanalyzer.types.external_access_details

        return {
            "externalAccessDetails": capo_accessanalyzer.types.external_access_details.serialize_json(
                value["externalAccessDetails"]
            )
        }
    elif "unusedPermissionDetails" in value:
        import capo_accessanalyzer.types.unused_permission_details

        return {
            "unusedPermissionDetails": capo_accessanalyzer.types.unused_permission_details.serialize_json(
                value["unusedPermissionDetails"]
            )
        }
    elif "unusedIamUserAccessKeyDetails" in value:
        import capo_accessanalyzer.types.unused_iam_user_access_key_details

        return {
            "unusedIamUserAccessKeyDetails": capo_accessanalyzer.types.unused_iam_user_access_key_details.serialize_json(
                value["unusedIamUserAccessKeyDetails"]
            )
        }
    elif "unusedIamRoleDetails" in value:
        import capo_accessanalyzer.types.unused_iam_role_details

        return {
            "unusedIamRoleDetails": capo_accessanalyzer.types.unused_iam_role_details.serialize_json(
                value["unusedIamRoleDetails"]
            )
        }
    elif "unusedIamUserPasswordDetails" in value:
        import capo_accessanalyzer.types.unused_iam_user_password_details

        return {
            "unusedIamUserPasswordDetails": capo_accessanalyzer.types.unused_iam_user_password_details.serialize_json(
                value["unusedIamUserPasswordDetails"]
            )
        }
    else:
        raise SerializationError("FindingDetails: no variant present")


def deserialize_json(data: dict) -> FindingDetails:
    if data.get("internalAccessDetails") is not None:
        import capo_accessanalyzer.types.internal_access_details

        return {
            "internalAccessDetails": capo_accessanalyzer.types.internal_access_details.deserialize_json(
                data["internalAccessDetails"]
            )
        }
    elif data.get("externalAccessDetails") is not None:
        import capo_accessanalyzer.types.external_access_details

        return {
            "externalAccessDetails": capo_accessanalyzer.types.external_access_details.deserialize_json(
                data["externalAccessDetails"]
            )
        }
    elif data.get("unusedPermissionDetails") is not None:
        import capo_accessanalyzer.types.unused_permission_details

        return {
            "unusedPermissionDetails": capo_accessanalyzer.types.unused_permission_details.deserialize_json(
                data["unusedPermissionDetails"]
            )
        }
    elif data.get("unusedIamUserAccessKeyDetails") is not None:
        import capo_accessanalyzer.types.unused_iam_user_access_key_details

        return {
            "unusedIamUserAccessKeyDetails": capo_accessanalyzer.types.unused_iam_user_access_key_details.deserialize_json(
                data["unusedIamUserAccessKeyDetails"]
            )
        }
    elif data.get("unusedIamRoleDetails") is not None:
        import capo_accessanalyzer.types.unused_iam_role_details

        return {
            "unusedIamRoleDetails": capo_accessanalyzer.types.unused_iam_role_details.deserialize_json(
                data["unusedIamRoleDetails"]
            )
        }
    elif data.get("unusedIamUserPasswordDetails") is not None:
        import capo_accessanalyzer.types.unused_iam_user_password_details

        return {
            "unusedIamUserPasswordDetails": capo_accessanalyzer.types.unused_iam_user_password_details.deserialize_json(
                data["unusedIamUserPasswordDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FindingDetails: no recognized variant key")
