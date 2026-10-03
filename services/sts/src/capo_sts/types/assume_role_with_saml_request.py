"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRoleWithSAMLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sts.types.arn_type
    import capo_sts.types.minimum_session_token_size_type
    import capo_sts.types.policy_descriptor_list_type
    import capo_sts.types.role_duration_seconds_type
    import capo_sts.types.saml_assertion_type
    import capo_sts.types.session_policy_document_type


class AssumeRoleWithSAMLRequest(TypedDict, closed=True):
    role_arn: "capo_sts.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the role that the caller is assuming.</p>"""
    principal_arn: "capo_sts.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.</p>"""
    saml_assertion: "capo_sts.types.saml_assertion_type.SAMLAssertionType"
    """<p>The base64 encoded SAML authentication response provided by the IdP.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/create-role-saml-IdP-tasks.html">Configuring a Relying Party and Adding Claims</a> in the <i>IAM User Guide</i>. </p>"""
    policy_arns: NotRequired[
        "capo_sts.types.policy_descriptor_list_type.policyDescriptorListType"
    ]
    """<p>The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.</p> <p>This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the Amazon Web Services General Reference.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p>"""
    policy: NotRequired[
        "capo_sts.types.session_policy_document_type.sessionPolicyDocumentType"
    ]
    r"""<p>An IAM policy in JSON format that you want to use as an inline session policy.</p> <p>This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>. </p> <p>The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (\u0020 through \u00FF). It can also include the tab (\u0009), linefeed (\u000A), and carriage return (\u000D) characters.</p> <p>For more information about role session permissions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session policies</a>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note>"""
    duration_seconds: NotRequired[
        "capo_sts.types.role_duration_seconds_type.roleDurationSecondsType"
    ]
    """<p>The duration, in seconds, of the role session. Your role session lasts for the duration that you specify for the <code>DurationSeconds</code> parameter, or until the time specified in the SAML authentication response's <code>SessionNotOnOrAfter</code> value, whichever is shorter. You can provide a <code>DurationSeconds</code> value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session">View the Maximum Session Duration Setting for a Role</a> in the <i>IAM User Guide</i>.</p> <p>By default, the value is set to <code>3600</code> seconds. </p> <note> <p>The <code>DurationSeconds</code> parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a <code>SessionDuration</code> parameter that specifies the maximum length of the console session. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html">Creating a URL that Enables Federated Users to Access the Amazon Web Services Management Console</a> in the <i>IAM User Guide</i>.</p> </note>"""
    minimum_session_token_size: NotRequired[
        "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRoleWithSAMLRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleArn", str(value["role_arn"])))
    pairs.append((f"{key_prefix}PrincipalArn", str(value["principal_arn"])))
    pairs.append((f"{key_prefix}SAMLAssertion", str(value["saml_assertion"])))
    if "policy_arns" in value:
        import capo_sts.types.policy_descriptor_list_type

        capo_sts.types.policy_descriptor_list_type.serialize_query(
            value["policy_arns"], pairs, f"{key_prefix}PolicyArns"
        )
    if "policy" in value:
        pairs.append((f"{key_prefix}Policy", str(value["policy"])))
    if "duration_seconds" in value:
        pairs.append((f"{key_prefix}DurationSeconds", str(value["duration_seconds"])))
    if "minimum_session_token_size" in value:
        pairs.append(
            (
                f"{key_prefix}MinimumSessionTokenSize",
                str(value["minimum_session_token_size"]),
            )
        )


def deserialize_query(el: Element) -> AssumeRoleWithSAMLRequest:
    out: AssumeRoleWithSAMLRequest = {}  # type: ignore[typeddict-item]
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    else:
        raise DeserializationError("AssumeRoleWithSAMLRequest.role_arn required")
    child_principal_arn = el.find("PrincipalArn")
    if child_principal_arn is not None:
        out["principal_arn"] = str(child_principal_arn.text or "")
    else:
        raise DeserializationError("AssumeRoleWithSAMLRequest.principal_arn required")
    child_saml_assertion = el.find("SAMLAssertion")
    if child_saml_assertion is not None:
        out["saml_assertion"] = str(child_saml_assertion.text or "")
    else:
        raise DeserializationError("AssumeRoleWithSAMLRequest.saml_assertion required")
    child_policy_arns = el.find("PolicyArns")
    if child_policy_arns is not None:
        import capo_sts.types.policy_descriptor_list_type

        out["policy_arns"] = (
            capo_sts.types.policy_descriptor_list_type.deserialize_query(
                child_policy_arns
            )
        )
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    child_minimum_session_token_size = el.find("MinimumSessionTokenSize")
    if child_minimum_session_token_size is not None:
        out["minimum_session_token_size"] = int(
            child_minimum_session_token_size.text or ""
        )
    return out
