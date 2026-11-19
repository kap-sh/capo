"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CreateProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.alias_name
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
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>An alias for the profile. When you set an alias, the response includes the alias ARN of the profile in <code>aliasArn</code>.</p> <p>An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with <code>aws/</code>, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.</p> <p>The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a <code>ValidationException</code>. An invalid or reserved alias name also causes a <code>ValidationException</code>.</p> <p>If you omit this parameter or specify an empty string, the resource is created without an alias.</p>"""


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
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> CreateProfileRequest:
    out: CreateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
        out["role_arns"] = []
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
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    return out


def redact_sensitive(value: CreateProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.redact_sensitive(value["tags"])
    return out
