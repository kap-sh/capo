"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sts.types.arn_type
    import capo_sts.types.external_id_type
    import capo_sts.types.minimum_session_token_size_type
    import capo_sts.types.policy_descriptor_list_type
    import capo_sts.types.provided_contexts_list_type
    import capo_sts.types.role_duration_seconds_type
    import capo_sts.types.role_session_name_type
    import capo_sts.types.serial_number_type
    import capo_sts.types.source_identity_type
    import capo_sts.types.tag_key_list_type
    import capo_sts.types.tag_list_type
    import capo_sts.types.token_code_type
    import capo_sts.types.unrestricted_session_policy_document_type


class AssumeRoleRequest(TypedDict, closed=True):
    role_arn: "capo_sts.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the role to assume.</p>"""
    role_session_name: "capo_sts.types.role_session_name_type.roleSessionNameType"
    """<p>An identifier for the assumed role session.</p> <p>Use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. In cross-account scenarios, the role session name is visible to, and can be logged by the account that owns the role. The role session name is also used in the ARN of the assumed role principal. This means that subsequent cross-account API requests that use the temporary security credentials will expose the role session name to the external account in their CloudTrail logs.</p> <p>For security purposes, administrators can view this field in <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html#cloudtrail-integration_signin-tempcreds">CloudTrail logs</a> to help identify who performed an action in Amazon Web Services. Your administrator might require that you specify your user name as the session name when you assume the role. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_rolesessionname"> <code>sts:RoleSessionName</code> </a>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=,.@-</p>"""
    policy_arns: NotRequired[
        "capo_sts.types.policy_descriptor_list_type.policyDescriptorListType"
    ]
    """<p>The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.</p> <p>This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the Amazon Web Services General Reference.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p>"""
    policy: NotRequired[
        "capo_sts.types.unrestricted_session_policy_document_type.unrestrictedSessionPolicyDocumentType"
    ]
    r"""<p>An IAM policy in JSON format that you want to use as an inline session policy.</p> <p>This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p>The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (\u0020 through \u00FF). It can also include the tab (\u0009), linefeed (\u000A), and carriage return (\u000D) characters.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>For more information about role session permissions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session policies</a>.</p>"""
    duration_seconds: NotRequired[
        "capo_sts.types.role_duration_seconds_type.roleDurationSecondsType"
    ]
    """<p>The duration, in seconds, of the role session. The value specified can range from 900 seconds (15 minutes) up to the maximum session duration set for the role. The maximum session duration setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting or the administrator setting (whichever is lower), the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. </p> <p>Role chaining limits your Amazon Web Services CLI or Amazon Web Services API role session to a maximum of one hour. When you use the <code>AssumeRole</code> API operation to assume a role, you can specify the duration of your role session with the <code>DurationSeconds</code> parameter. You can specify a parameter value of up to 43200 seconds (12 hours), depending on the maximum session duration setting for your role. However, if you assume a role using role chaining and provide a <code>DurationSeconds</code> parameter value greater than one hour, the operation fails. To learn how to view the maximum value for your role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html#id_roles_update-session-duration">Update the maximum session duration for a role</a>.</p> <p>By default, the value is set to <code>3600</code> seconds. </p> <note> <p>The <code>DurationSeconds</code> parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a <code>SessionDuration</code> parameter that specifies the maximum length of the console session. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html">Creating a URL that Enables Federated Users to Access the Amazon Web Services Management Console</a> in the <i>IAM User Guide</i>.</p> </note>"""
    tags: NotRequired["capo_sts.types.tag_list_type.tagListType"]
    """<p>A list of session tags that you want to pass. Each session tag consists of a key name and an associated value. For more information about session tags, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Tagging Amazon Web Services STS Sessions</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters, and the values can’t exceed 256 characters. For these and additional limits, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length">IAM and STS Character Limits</a> in the <i>IAM User Guide</i>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>You can pass a session tag with the same key as a tag that is already attached to the role. When you do, session tags override a role tag with the same key. </p> <p>Tag key–value pairs are not case sensitive, but case is preserved. This means that you cannot have separate <code>Department</code> and <code>department</code> tag keys. Assume that the role has the <code>Department</code>=<code>Marketing</code> tag and you pass the <code>department</code>=<code>engineering</code> session tag. <code>Department</code> and <code>department</code> are not saved as separate tags, and the session tag passed in the request takes precedence over the role tag.</p> <p>Additionally, if you used temporary credentials to perform this operation, the new session inherits any transitive session tags from the calling session. If you pass a session tag with the same key as an inherited tag, the operation fails. To view the inherited tags for a session, see the CloudTrail logs. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_ctlogs">Viewing Session Tags in CloudTrail</a> in the <i>IAM User Guide</i>.</p>"""
    transitive_tag_keys: NotRequired["capo_sts.types.tag_key_list_type.tagKeyListType"]
    """<p>A list of keys for session tags that you want to set as transitive. If you set a tag key as transitive, the corresponding key and value passes to subsequent sessions in a role chain. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining">Chaining Roles with Session Tags</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. The transitive status of a session tag does not impact its packed binary size.</p> <p>If you choose not to specify a transitive tag key, then no tags are passed from this session to any subsequent sessions.</p>"""
    external_id: NotRequired["capo_sts.types.external_id_type.externalIdType"]
    r"""<p>A unique identifier that might be required when you assume a role in another account. If the administrator of the account to which the role belongs provided you with an external ID, then provide that value in the <code>ExternalId</code> parameter. This value can be any string, such as a passphrase or account number. A cross-account role is usually set up to trust everyone in an account. Therefore, the administrator of the trusting account might send an external ID to the administrator of the trusted account. That way, only someone with the ID can assume the role, rather than everyone in the account. For more information about the external ID, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html">How to Use an External ID When Granting Access to Your Amazon Web Services Resources to a Third Party</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=,.@:\/-</p>"""
    serial_number: NotRequired["capo_sts.types.serial_number_type.serialNumberType"]
    """<p>The identification number of the MFA device that is associated with the user who is making the <code>AssumeRole</code> call. Specify this value if the trust policy of the role being assumed includes a condition that requires MFA authentication. The value is either the serial number for a hardware device (such as <code>GAHT12345678</code>) or an Amazon Resource Name (ARN) for a virtual device (such as <code>arn:aws:iam::123456789012:mfa/user</code>).</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=/:,.@-</p>"""
    token_code: NotRequired["capo_sts.types.token_code_type.tokenCodeType"]
    """<p>The value provided by the MFA device, if the trust policy of the role being assumed requires MFA. (In other words, if the policy includes a condition that tests for MFA). If the role being assumed requires MFA and if the <code>TokenCode</code> value is missing or expired, the <code>AssumeRole</code> call returns an "access denied" error.</p> <p>The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.</p>"""
    source_identity: NotRequired[
        "capo_sts.types.source_identity_type.sourceIdentityType"
    ]
    """<p>The source identity specified by the principal that is calling the <code>AssumeRole</code> operation. The source identity value persists across <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-role-chaining">chained role</a> sessions.</p> <p>You can require users to specify a source identity when they assume a role. You do this by using the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceidentity"> <code>sts:SourceIdentity</code> </a> condition key in a role trust policy. You can use source identity information in CloudTrail logs to determine who took actions with a role. You can use the <code>aws:SourceIdentity</code> condition key to further control access to Amazon Web Services resources based on the value of source identity. For more information about using source identity, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html">Monitor and control actions taken with assumed roles</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=,.@-. You cannot use a value that begins with the text <code>aws:</code>. This prefix is reserved for Amazon Web Services internal use.</p>"""
    provided_contexts: NotRequired[
        "capo_sts.types.provided_contexts_list_type.ProvidedContextsListType"
    ]
    """<p>A list of previously acquired trusted context assertions in the format of a JSON array. The trusted context assertion is signed and encrypted by Amazon Web Services STS.</p> <p>The following is an example of a <code>ProvidedContext</code> value that includes a single trusted context assertion and the ARN of the context provider from which the trusted context assertion was generated.</p> <p> <code>[{"ProviderArn":"arn:aws:iam::aws:contextProvider/IdentityCenter","ContextAssertion":"trusted-context-assertion"}]</code> </p>"""
    minimum_session_token_size: NotRequired[
        "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleArn", str(value["role_arn"])))
    pairs.append((f"{key_prefix}RoleSessionName", str(value["role_session_name"])))
    if "policy_arns" in value:
        import capo_sts.types.policy_descriptor_list_type

        capo_sts.types.policy_descriptor_list_type.serialize_query(
            value["policy_arns"], pairs, f"{key_prefix}PolicyArns"
        )
    if "policy" in value:
        pairs.append((f"{key_prefix}Policy", str(value["policy"])))
    if "duration_seconds" in value:
        pairs.append((f"{key_prefix}DurationSeconds", str(value["duration_seconds"])))
    if "tags" in value:
        import capo_sts.types.tag_list_type

        capo_sts.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "transitive_tag_keys" in value:
        import capo_sts.types.tag_key_list_type

        capo_sts.types.tag_key_list_type.serialize_query(
            value["transitive_tag_keys"], pairs, f"{key_prefix}TransitiveTagKeys"
        )
    if "external_id" in value:
        pairs.append((f"{key_prefix}ExternalId", str(value["external_id"])))
    if "serial_number" in value:
        pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    if "token_code" in value:
        pairs.append((f"{key_prefix}TokenCode", str(value["token_code"])))
    if "source_identity" in value:
        pairs.append((f"{key_prefix}SourceIdentity", str(value["source_identity"])))
    if "provided_contexts" in value:
        import capo_sts.types.provided_contexts_list_type

        capo_sts.types.provided_contexts_list_type.serialize_query(
            value["provided_contexts"], pairs, f"{key_prefix}ProvidedContexts"
        )
    if "minimum_session_token_size" in value:
        pairs.append(
            (
                f"{key_prefix}MinimumSessionTokenSize",
                str(value["minimum_session_token_size"]),
            )
        )


def deserialize_query(el: Element) -> AssumeRoleRequest:
    out: AssumeRoleRequest = {}  # type: ignore[typeddict-item]
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    else:
        raise DeserializationError("AssumeRoleRequest.role_arn required")
    child_role_session_name = el.find("RoleSessionName")
    if child_role_session_name is not None:
        out["role_session_name"] = str(child_role_session_name.text or "")
    else:
        raise DeserializationError("AssumeRoleRequest.role_session_name required")
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_sts.types.tag_list_type

        out["tags"] = capo_sts.types.tag_list_type.deserialize_query(child_tags)
    child_transitive_tag_keys = el.find("TransitiveTagKeys")
    if child_transitive_tag_keys is not None:
        import capo_sts.types.tag_key_list_type

        out["transitive_tag_keys"] = capo_sts.types.tag_key_list_type.deserialize_query(
            child_transitive_tag_keys
        )
    child_external_id = el.find("ExternalId")
    if child_external_id is not None:
        out["external_id"] = str(child_external_id.text or "")
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    child_token_code = el.find("TokenCode")
    if child_token_code is not None:
        out["token_code"] = str(child_token_code.text or "")
    child_source_identity = el.find("SourceIdentity")
    if child_source_identity is not None:
        out["source_identity"] = str(child_source_identity.text or "")
    child_provided_contexts = el.find("ProvidedContexts")
    if child_provided_contexts is not None:
        import capo_sts.types.provided_contexts_list_type

        out["provided_contexts"] = (
            capo_sts.types.provided_contexts_list_type.deserialize_query(
                child_provided_contexts
            )
        )
    child_minimum_session_token_size = el.find("MinimumSessionTokenSize")
    if child_minimum_session_token_size is not None:
        out["minimum_session_token_size"] = int(
            child_minimum_session_token_size.text or ""
        )
    return out
