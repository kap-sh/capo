"""Generated from Smithy shape ``com.amazonaws.iam#UpdateRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_object_type
    import capo_iam.types.max_signin_session_duration_type
    import capo_iam.types.role_description_type
    import capo_iam.types.role_max_session_duration_type
    import capo_iam.types.role_name_type


class UpdateRoleRequest(TypedDict, closed=True):
    role_name: "capo_iam.types.role_name_type.roleNameType"
    """<p>The name of the role that you want to modify.</p>"""
    description: NotRequired["capo_iam.types.role_description_type.roleDescriptionType"]
    """<p>The new description that you want to apply to the specified role.</p>"""
    max_session_duration: NotRequired[
        "capo_iam.types.role_max_session_duration_type.roleMaxSessionDurationType"
    ]
    """<p>The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours.</p> <p>Anyone who assumes the role from the CLI or API can use the <code>DurationSeconds</code> API parameter or the <code>duration-seconds</code> CLI parameter to request a longer session. The <code>MaxSessionDuration</code> setting determines the maximum duration that can be requested using the <code>DurationSeconds</code> parameter. If users don't specify a value for the <code>DurationSeconds</code> parameter, their security credentials are valid for one hour by default. This applies when you use the <code>AssumeRole*</code> API operations or the <code>assume-role*</code> CLI operations but does not apply when you use those operations to create a console URL. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html">Using IAM roles</a> in the <i>IAM User Guide</i>.</p> <note> <p>IAM role credentials provided by Amazon EC2 instances assigned to the role are not subject to the specified maximum session duration.</p> </note>"""
    max_signin_session_duration: NotRequired[
        "capo_iam.types.max_signin_session_duration_type.maxSigninSessionDurationType"
    ]
    """<p>The maximum duration (in seconds) of an Amazon Web Services Sign-In session for users who sign in with the specified role. This setting can have a value from 1 hour (3600 seconds) to 90 days (7776000 seconds), inclusive, and replaces any value currently configured for the role. This setting is independent of <code>MaxSessionDuration</code>.</p> <p>If you omit both this parameter and <code>ResetMaxSigninSessionDuration</code>, the current setting is unchanged. You cannot specify this parameter and set <code>ResetMaxSigninSessionDuration</code> to <code>true</code> in the same request.</p> <p>Changes to this setting apply to new sign-in sessions. Sessions that are already established are not affected.</p> <note> <p>You cannot set this value on a service-linked role.</p> </note>"""
    reset_max_signin_session_duration: NotRequired[
        "capo_iam.types.boolean_object_type.booleanObjectType"
    ]
    """<p>Specifies whether to clear the role's maximum sign-in session duration. Set this value to <code>true</code> to return the setting to its unset state, so that the existing sign-in session behavior applies. When the setting is unset, the role's <code>MaxSigninSessionDuration</code> is omitted from responses.</p> <p>If you set this value to <code>false</code> or omit it, the current setting is not cleared. You cannot set this value to <code>true</code> and specify <code>MaxSigninSessionDuration</code> in the same request. Clearing a setting that is already unset has no effect.</p> <note> <p>You cannot reset this value on a service-linked role.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "max_session_duration" in value:
        pairs.append(
            (f"{key_prefix}MaxSessionDuration", str(value["max_session_duration"]))
        )
    if "max_signin_session_duration" in value:
        pairs.append(
            (
                f"{key_prefix}MaxSigninSessionDuration",
                str(value["max_signin_session_duration"]),
            )
        )
    if "reset_max_signin_session_duration" in value:
        pairs.append(
            (
                f"{key_prefix}ResetMaxSigninSessionDuration",
                "true" if value["reset_max_signin_session_duration"] else "false",
            )
        )


def deserialize_query(el: Element) -> UpdateRoleRequest:
    out: UpdateRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        out["role_name"] = ""
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_max_session_duration = el.find("MaxSessionDuration")
    if child_max_session_duration is not None:
        out["max_session_duration"] = int(child_max_session_duration.text or "")
    child_max_signin_session_duration = el.find("MaxSigninSessionDuration")
    if child_max_signin_session_duration is not None:
        out["max_signin_session_duration"] = int(
            child_max_signin_session_duration.text or ""
        )
    child_reset_max_signin_session_duration = el.find("ResetMaxSigninSessionDuration")
    if child_reset_max_signin_session_duration is not None:
        out["reset_max_signin_session_duration"] = (
            child_reset_max_signin_session_duration.text or ""
        ).lower() == "true"
    return out
