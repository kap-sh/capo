"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UpdateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.alias_name
    import capo_rolesanywhere.types.managed_policy_list
    import capo_rolesanywhere.types.profile_identifier
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.role_arn_list


class UpdateProfileRequest(TypedDict, closed=True):
    profile_id: "capo_rolesanywhere.types.profile_identifier.ProfileIdentifier"
    """<p>The profile to act on. You can specify one of the following:</p> <ul> <li> <p>The profile ID.</p> </li> <li> <p>The profile ARN.</p> </li> <li> <p>The alias ARN of the profile.</p> </li> </ul> <p>An ARN must be for a profile in your account and Region.</p>"""
    name: NotRequired["capo_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the profile.</p>"""
    session_policy: NotRequired["str"]
    """<p>A session policy that applies to the trust boundary of the vended session credentials. </p>"""
    role_arns: NotRequired["capo_rolesanywhere.types.role_arn_list.RoleArnList"]
    """<p>A list of IAM roles that this profile can assume in a temporary credential request.</p>"""
    managed_policy_arns: NotRequired[
        "capo_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
    ]
    """<p>A list of managed policy ARNs that apply to the vended session credentials. </p>"""
    duration_seconds: NotRequired["int"]
    """<p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>"""
    accept_role_session_name: NotRequired["bool"]
    """<p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>"""
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias for the profile.</p> <p>You can use this parameter in the following ways:</p> <ul> <li> <p>To set or change the alias, specify the new alias name. After the change, the previous alias ARN no longer identifies the resource. You can then assign the previous alias to another resource of the same type. A change can take a short time to take effect for requests that use an alias ARN.</p> </li> <li> <p>To remove the alias, specify an empty string.</p> </li> <li> <p>To keep the current alias, omit this parameter.</p> </li> </ul> <p>An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with <code>aws/</code>, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.</p> <p>The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a <code>ValidationException</code>. An invalid or reserved alias name also causes a <code>ValidationException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "session_policy" in value:
        out["sessionPolicy"] = value["session_policy"]
    if "role_arns" in value:
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
    if "accept_role_session_name" in value:
        out["acceptRoleSessionName"] = value["accept_role_session_name"]
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> UpdateProfileRequest:
    out: UpdateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("sessionPolicy") is not None:
        out["session_policy"] = data["sessionPolicy"]
    if data.get("roleArns") is not None:
        import capo_rolesanywhere.types.role_arn_list

        out["role_arns"] = capo_rolesanywhere.types.role_arn_list.deserialize_json(
            data["roleArns"]
        )
    if data.get("managedPolicyArns") is not None:
        import capo_rolesanywhere.types.managed_policy_list

        out["managed_policy_arns"] = (
            capo_rolesanywhere.types.managed_policy_list.deserialize_json(
                data["managedPolicyArns"]
            )
        )
    if data.get("durationSeconds") is not None:
        out["duration_seconds"] = data["durationSeconds"]
    if data.get("acceptRoleSessionName") is not None:
        out["accept_role_session_name"] = data["acceptRoleSessionName"]
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    return out
