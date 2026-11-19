"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ProfileDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.alias_name
    import capo_rolesanywhere.types.attribute_mappings
    import capo_rolesanywhere.types.managed_policy_list
    import capo_rolesanywhere.types.profile_alias_arn
    import capo_rolesanywhere.types.profile_resource_arn
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.role_arn_list
    import capo_rolesanywhere.types.uuid


class ProfileDetail(TypedDict, closed=True):
    profile_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The unique identifier of the profile.</p>"""
    profile_arn: NotRequired[
        "capo_rolesanywhere.types.profile_resource_arn.ProfileResourceArn"
    ]
    """<p>The ARN of the profile.</p>"""
    name: NotRequired["capo_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the profile.</p>"""
    require_instance_properties: NotRequired["bool"]
    """<p>Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile. </p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the profile is enabled.</p>"""
    created_by: NotRequired["str"]
    """<p>The Amazon Web Services account that created the profile.</p>"""
    session_policy: NotRequired["str"]
    """<p>A session policy that applies to the trust boundary of the vended session credentials. </p>"""
    role_arns: NotRequired["capo_rolesanywhere.types.role_arn_list.RoleArnList"]
    """<p>A list of IAM roles that this profile can assume in a temporary credential request.</p>"""
    managed_policy_arns: NotRequired[
        "capo_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
    ]
    """<p>A list of managed policy ARNs that apply to the vended session credentials. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the profile was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the profile was last updated. </p>"""
    duration_seconds: NotRequired["int"]
    """<p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href="https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>"""
    accept_role_session_name: NotRequired["bool"]
    """<p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>"""
    attribute_mappings: NotRequired[
        "capo_rolesanywhere.types.attribute_mappings.AttributeMappings"
    ]
    """<p>A mapping applied to the authenticating end-entity certificate.</p>"""
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias of the profile. Present only if the profile has an alias.</p>"""
    alias_arn: NotRequired["capo_rolesanywhere.types.profile_alias_arn.ProfileAliasArn"]
    """<p>The alias ARN of the profile, in the form <code>arn:<i>partition</i>:rolesanywhere:<i>region</i>:<i>account</i>:alias/profile/<i>alias-name</i> </code>. Present only if the profile has an alias.</p> <p>You can use the alias ARN in place of the resource ID or ARN in the request parameters whose descriptions say that they accept an alias ARN. Don't use the alias ARN in Identity and Access Management (IAM) policies. A policy statement that names an alias ARN doesn't apply to the resource that holds the alias. Write policies with the ARN that contains the resource ID instead.</p>"""
    previous_alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias that the resource had before the update request. IAM Roles Anywhere returns this value only in the response to an update request that changed or removed an existing alias. It isn't returned when the alias was unchanged, when the resource had no alias before the request, or by other operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileDetail) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    if "profile_arn" in value:
        out["profileArn"] = value["profile_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "require_instance_properties" in value:
        out["requireInstanceProperties"] = value["require_instance_properties"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
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
    if "created_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["createdAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["updatedAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "duration_seconds" in value:
        out["durationSeconds"] = value["duration_seconds"]
    if "accept_role_session_name" in value:
        out["acceptRoleSessionName"] = value["accept_role_session_name"]
    if "attribute_mappings" in value:
        import capo_rolesanywhere.types.attribute_mappings

        out["attributeMappings"] = (
            capo_rolesanywhere.types.attribute_mappings.serialize_json(
                value["attribute_mappings"]
            )
        )
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    if "alias_arn" in value:
        out["aliasArn"] = value["alias_arn"]
    if "previous_alias_name" in value:
        out["previousAliasName"] = value["previous_alias_name"]
    return out


def deserialize_json(data: dict) -> ProfileDetail:
    out: ProfileDetail = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("requireInstanceProperties") is not None:
        out["require_instance_properties"] = data["requireInstanceProperties"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
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
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("durationSeconds") is not None:
        out["duration_seconds"] = data["durationSeconds"]
    if data.get("acceptRoleSessionName") is not None:
        out["accept_role_session_name"] = data["acceptRoleSessionName"]
    if data.get("attributeMappings") is not None:
        import capo_rolesanywhere.types.attribute_mappings

        out["attribute_mappings"] = (
            capo_rolesanywhere.types.attribute_mappings.deserialize_json(
                data["attributeMappings"]
            )
        )
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    if data.get("aliasArn") is not None:
        out["alias_arn"] = data["aliasArn"]
    if data.get("previousAliasName") is not None:
        out["previous_alias_name"] = data["previousAliasName"]
    return out
