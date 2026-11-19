"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RestorePreviewType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.long_type
    import capo_cognito_identity_provider.types.string_type


class RestorePreviewType(TypedDict, closed=True):
    entity: NotRequired["capo_cognito_identity_provider.types.string_type.StringType"]
    """<p>The type of user pool entity that the recovery changes. Can be one of the following values.</p> <dl> <dt>Users</dt> <dd> <p>User profiles, including their attributes.</p> </dd> <dt>Groups</dt> <dd> <p>User pool groups.</p> </dd> <dt>User MFAs</dt> <dd> <p>The MFA settings of users.</p> </dd> <dt>Passkeys</dt> <dd> <p>The passkeys that users registered.</p> </dd> </dl>"""
    create_count: "capo_cognito_identity_provider.types.long_type.LongType"
    """<p>The number of entities of this type that the recovery creates. These entities existed at the recovery point and were deleted after it.</p>"""
    update_count: "capo_cognito_identity_provider.types.long_type.LongType"
    """<p>The number of entities of this type that the recovery reverts to their state at the recovery point. These entities were modified after the recovery point.</p>"""
    delete_count: "capo_cognito_identity_provider.types.long_type.LongType"
    """<p>The number of entities of this type that the recovery deletes. These entities were created after the recovery point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestorePreviewType) -> dict:
    out: dict = {}
    if "entity" in value:
        out["Entity"] = value["entity"]
    out["CreateCount"] = value.get("create_count", 0)
    out["UpdateCount"] = value.get("update_count", 0)
    out["DeleteCount"] = value.get("delete_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RestorePreviewType:
    out: RestorePreviewType = {}  # type: ignore[typeddict-item]
    if data.get("Entity") is not None:
        out["entity"] = data["Entity"]
    if data.get("CreateCount") is not None:
        out["create_count"] = data["CreateCount"]
    else:
        out["create_count"] = 0
    if data.get("UpdateCount") is not None:
        out["update_count"] = data["UpdateCount"]
    else:
        out["update_count"] = 0
    if data.get("DeleteCount") is not None:
        out["delete_count"] = data["DeleteCount"]
    else:
        out["delete_count"] = 0
    return out
