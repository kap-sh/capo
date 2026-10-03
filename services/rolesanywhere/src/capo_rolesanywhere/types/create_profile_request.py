"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CreateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.managed_policy_list
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.role_arn_list
    import capo_rolesanywhere.types.tag_list


class CreateProfileRequest(TypedDict, closed=True):
    name: "capo_rolesanywhere.types.resource_name.ResourceName"
    """<p>The name of the profile.</p>"""
    require_instance_properties: NotRequired["bool"]
    """<p>Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile. </p>"""
    session_policy: NotRequired["str"]
    """<p>A session policy that applies to the trust boundary of the vended session credentials. </p>"""
    role_arns: "capo_rolesanywhere.types.role_arn_list.RoleArnList"
    """<p>A list of IAM roles that this profile can assume in a temporary credential request.</p>"""
    managed_policy_arns: NotRequired[
        "capo_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
    ]
    """<p>A list of managed policy ARNs that apply to the vended session credentials. </p>"""
    duration_seconds: NotRequired["int"]
    """<p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether the profile is enabled.</p>"""
    tags: NotRequired["capo_rolesanywhere.types.tag_list.TagList"]
    """<p>The tags to attach to the profile.</p>"""
    accept_role_session_name: NotRequired["bool"]
    """<p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "require_instance_properties" in value:
        out["requireInstanceProperties"] = value["require_instance_properties"]
    if "session_policy" in value:
        out["sessionPolicy"] = value["session_policy"]
    import capo_rolesanywhere.types.role_arn_list

    out["roleArns"] = capo_rolesanywhere.types.role_arn_list.serialize_json(
        value["role_arns"]
    )
    if "managed_policy_arns" in value:
        import capo_rolesanywhere.types.managed_policy_list

        out["managedPolicyArns"] = (
            capo_rolesanywhere.types.managed_policy_list.serialize_json(
                value["managed_policy_arns"]
            )
        )
    if "duration_seconds" in value:
        out["durationSeconds"] = value["duration_seconds"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.serialize_json(value["tags"])
    if "accept_role_session_name" in value:
        out["acceptRoleSessionName"] = value["accept_role_session_name"]
    return out


def deserialize_json(data: dict) -> CreateProfileRequest:
    out: CreateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProfileRequest.name required")
    if data.get("requireInstanceProperties") is not None:
        out["require_instance_properties"] = data["requireInstanceProperties"]
    if data.get("sessionPolicy") is not None:
        out["session_policy"] = data["sessionPolicy"]
    if data.get("roleArns") is not None:
        import capo_rolesanywhere.types.role_arn_list

        out["role_arns"] = capo_rolesanywhere.types.role_arn_list.deserialize_json(
            data["roleArns"]
        )
    else:
        raise DeserializationError("CreateProfileRequest.role_arns required")
    if data.get("managedPolicyArns") is not None:
        import capo_rolesanywhere.types.managed_policy_list

        out["managed_policy_arns"] = (
            capo_rolesanywhere.types.managed_policy_list.deserialize_json(
                data["managedPolicyArns"]
            )
        )
    if data.get("durationSeconds") is not None:
        out["duration_seconds"] = data["durationSeconds"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("tags") is not None:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.deserialize_json(data["tags"])
    if data.get("acceptRoleSessionName") is not None:
        out["accept_role_session_name"] = data["acceptRoleSessionName"]
    return out
