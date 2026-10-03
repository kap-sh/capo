"""Generated from Smithy shape ``com.amazonaws.iam#UpdateAccountPasswordPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_object_type
    import capo_iam.types.boolean_type
    import capo_iam.types.max_password_age_type
    import capo_iam.types.minimum_password_length_type
    import capo_iam.types.password_reuse_prevention_type


class UpdateAccountPasswordPolicyRequest(TypedDict, closed=True):
    minimum_password_length: NotRequired[
        "capo_iam.types.minimum_password_length_type.minimumPasswordLengthType"
    ]
    """<p>The minimum number of characters allowed in an IAM user password.</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>6</code>.</p>"""
    require_symbols: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters:</p> <p>! @ # $ % ^ & * ( ) _ + - = [ ] { } | '</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>false</code>. The result is that passwords do not require at least one symbol character.</p>"""
    require_numbers: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>false</code>. The result is that passwords do not require at least one numeric character.</p>"""
    require_uppercase_characters: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>false</code>. The result is that passwords do not require at least one uppercase character.</p>"""
    require_lowercase_characters: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>false</code>. The result is that passwords do not require at least one lowercase character.</p>"""
    allow_users_to_change_password: "capo_iam.types.boolean_type.booleanType"
    """<p> Allows all IAM users in your account to use the Amazon Web Services Management Console to change their own passwords. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user-change.html">Permitting IAM users to change their own passwords</a> in the <i>IAM User Guide</i>.</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>false</code>. The result is that IAM users in the account do not automatically have permissions to change their own password.</p>"""
    max_password_age: NotRequired[
        "capo_iam.types.max_password_age_type.maxPasswordAgeType"
    ]
    """<p>The number of days that an IAM user password is valid.</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>0</code>. The result is that IAM user passwords never expire.</p>"""
    password_reuse_prevention: NotRequired[
        "capo_iam.types.password_reuse_prevention_type.passwordReusePreventionType"
    ]
    """<p>Specifies the number of previous passwords that IAM users are prevented from reusing.</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>0</code>. The result is that IAM users are not prevented from reusing previous passwords.</p>"""
    hard_expiry: NotRequired["capo_iam.types.boolean_object_type.booleanObjectType"]
    """<p> Prevents IAM users who are accessing the account via the Amazon Web Services Management Console from setting a new console password after their password has expired. The IAM user cannot access the console until an administrator resets the password.</p> <p>If you do not specify a value for this parameter, then the operation uses the default value of <code>false</code>. The result is that IAM users can change their passwords after they expire and continue to sign in as the user.</p> <note> <p> In the Amazon Web Services Management Console, the custom password policy option <b>Allow users to change their own password</b> gives IAM users permissions to <code>iam:ChangePassword</code> for only their user and to the <code>iam:GetAccountPasswordPolicy</code> action. This option does not attach a permissions policy to each user, rather the permissions are applied at the account-level for all users by IAM. IAM users with <code>iam:ChangePassword</code> permission and active access keys can reset their own expired console password using the CLI or API.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateAccountPasswordPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "minimum_password_length" in value:
        pairs.append(
            (
                f"{key_prefix}MinimumPasswordLength",
                str(value["minimum_password_length"]),
            )
        )
    pairs.append(
        (
            f"{key_prefix}RequireSymbols",
            "true" if value.get("require_symbols", False) else "false",
        )
    )
    pairs.append(
        (
            f"{key_prefix}RequireNumbers",
            "true" if value.get("require_numbers", False) else "false",
        )
    )
    pairs.append(
        (
            f"{key_prefix}RequireUppercaseCharacters",
            "true" if value.get("require_uppercase_characters", False) else "false",
        )
    )
    pairs.append(
        (
            f"{key_prefix}RequireLowercaseCharacters",
            "true" if value.get("require_lowercase_characters", False) else "false",
        )
    )
    pairs.append(
        (
            f"{key_prefix}AllowUsersToChangePassword",
            "true" if value.get("allow_users_to_change_password", False) else "false",
        )
    )
    if "max_password_age" in value:
        pairs.append((f"{key_prefix}MaxPasswordAge", str(value["max_password_age"])))
    if "password_reuse_prevention" in value:
        pairs.append(
            (
                f"{key_prefix}PasswordReusePrevention",
                str(value["password_reuse_prevention"]),
            )
        )
    if "hard_expiry" in value:
        pairs.append(
            (f"{key_prefix}HardExpiry", "true" if value["hard_expiry"] else "false")
        )


def deserialize_query(el: Element) -> UpdateAccountPasswordPolicyRequest:
    out: UpdateAccountPasswordPolicyRequest = {}  # type: ignore[typeddict-item]
    child_minimum_password_length = el.find("MinimumPasswordLength")
    if child_minimum_password_length is not None:
        out["minimum_password_length"] = int(child_minimum_password_length.text or "")
    child_require_symbols = el.find("RequireSymbols")
    if child_require_symbols is not None:
        out["require_symbols"] = (child_require_symbols.text or "").lower() == "true"
    else:
        out["require_symbols"] = False
    child_require_numbers = el.find("RequireNumbers")
    if child_require_numbers is not None:
        out["require_numbers"] = (child_require_numbers.text or "").lower() == "true"
    else:
        out["require_numbers"] = False
    child_require_uppercase_characters = el.find("RequireUppercaseCharacters")
    if child_require_uppercase_characters is not None:
        out["require_uppercase_characters"] = (
            child_require_uppercase_characters.text or ""
        ).lower() == "true"
    else:
        out["require_uppercase_characters"] = False
    child_require_lowercase_characters = el.find("RequireLowercaseCharacters")
    if child_require_lowercase_characters is not None:
        out["require_lowercase_characters"] = (
            child_require_lowercase_characters.text or ""
        ).lower() == "true"
    else:
        out["require_lowercase_characters"] = False
    child_allow_users_to_change_password = el.find("AllowUsersToChangePassword")
    if child_allow_users_to_change_password is not None:
        out["allow_users_to_change_password"] = (
            child_allow_users_to_change_password.text or ""
        ).lower() == "true"
    else:
        out["allow_users_to_change_password"] = False
    child_max_password_age = el.find("MaxPasswordAge")
    if child_max_password_age is not None:
        out["max_password_age"] = int(child_max_password_age.text or "")
    child_password_reuse_prevention = el.find("PasswordReusePrevention")
    if child_password_reuse_prevention is not None:
        out["password_reuse_prevention"] = int(
            child_password_reuse_prevention.text or ""
        )
    child_hard_expiry = el.find("HardExpiry")
    if child_hard_expiry is not None:
        out["hard_expiry"] = (child_hard_expiry.text or "").lower() == "true"
    return out
