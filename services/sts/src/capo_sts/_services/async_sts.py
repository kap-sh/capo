"""Generated from Smithy shape ``com.amazonaws.sts#AWSSecurityTokenServiceV20110615``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sts._auth._signers
import capo_sts._auth._sigv4
from capo_sts._auth._identity import Credentials
from capo_sts._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sts._auth._zapros_handler import AuthMiddleware
from capo_sts._services._aws_config import aaws_config
from capo_sts._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sts.types.access_key_id_type
    import capo_sts.types.arn_type
    import capo_sts.types.assume_role_request
    import capo_sts.types.assume_role_response
    import capo_sts.types.assume_role_with_saml_request
    import capo_sts.types.assume_role_with_saml_response
    import capo_sts.types.assume_role_with_web_identity_request
    import capo_sts.types.assume_role_with_web_identity_response
    import capo_sts.types.assume_root_request
    import capo_sts.types.assume_root_response
    import capo_sts.types.client_token_type
    import capo_sts.types.decode_authorization_message_request
    import capo_sts.types.decode_authorization_message_response
    import capo_sts.types.duration_seconds_type
    import capo_sts.types.encoded_message_type
    import capo_sts.types.external_id_type
    import capo_sts.types.get_access_key_info_request
    import capo_sts.types.get_access_key_info_response
    import capo_sts.types.get_caller_identity_request
    import capo_sts.types.get_caller_identity_response
    import capo_sts.types.get_delegated_access_token_request
    import capo_sts.types.get_delegated_access_token_response
    import capo_sts.types.get_federation_token_request
    import capo_sts.types.get_federation_token_response
    import capo_sts.types.get_session_token_request
    import capo_sts.types.get_session_token_response
    import capo_sts.types.get_web_identity_token_request
    import capo_sts.types.get_web_identity_token_response
    import capo_sts.types.jwt_algorithm_type
    import capo_sts.types.minimum_session_token_size_type
    import capo_sts.types.policy_descriptor_list_type
    import capo_sts.types.policy_descriptor_type
    import capo_sts.types.provided_contexts_list_type
    import capo_sts.types.role_duration_seconds_type
    import capo_sts.types.role_session_name_type
    import capo_sts.types.root_duration_seconds_type
    import capo_sts.types.saml_assertion_type
    import capo_sts.types.serial_number_type
    import capo_sts.types.session_policy_document_type
    import capo_sts.types.source_identity_type
    import capo_sts.types.tag_key_list_type
    import capo_sts.types.tag_list_type
    import capo_sts.types.target_principal_type
    import capo_sts.types.token_code_type
    import capo_sts.types.trade_in_token_type
    import capo_sts.types.unrestricted_session_policy_document_type
    import capo_sts.types.url_type
    import capo_sts.types.user_name_type
    import capo_sts.types.web_identity_token_audience_list_type
    import capo_sts.types.web_identity_token_duration_seconds_type


class AsyncSTSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    use_global_endpoint: bool | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSTSClient:
    """A client for the ``STS`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        use_global_endpoint: The value of the ``AWS::STS::UseGlobalEndpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        use_global_endpoint: bool | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncSTSClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "use_global_endpoint": use_global_endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSTSClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSTSClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            use_global_endpoint=overrides.get(
                "use_global_endpoint", self._config.get("use_global_endpoint")
            ),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def assume_role(
        self,
        role_arn: "capo_sts.types.arn_type.arnType",
        role_session_name: "capo_sts.types.role_session_name_type.roleSessionNameType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
        policy_arns: Optional[
            "capo_sts.types.policy_descriptor_list_type.policyDescriptorListType"
        ] = None,
        policy: Optional[
            "capo_sts.types.unrestricted_session_policy_document_type.unrestrictedSessionPolicyDocumentType"
        ] = None,
        duration_seconds: Optional[
            "capo_sts.types.role_duration_seconds_type.roleDurationSecondsType"
        ] = None,
        tags: Optional["capo_sts.types.tag_list_type.tagListType"] = None,
        transitive_tag_keys: Optional[
            "capo_sts.types.tag_key_list_type.tagKeyListType"
        ] = None,
        external_id: Optional["capo_sts.types.external_id_type.externalIdType"] = None,
        serial_number: Optional[
            "capo_sts.types.serial_number_type.serialNumberType"
        ] = None,
        token_code: Optional["capo_sts.types.token_code_type.tokenCodeType"] = None,
        source_identity: Optional[
            "capo_sts.types.source_identity_type.sourceIdentityType"
        ] = None,
        provided_contexts: Optional[
            "capo_sts.types.provided_contexts_list_type.ProvidedContextsListType"
        ] = None,
        minimum_session_token_size: Optional[
            "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
        ] = None,
    ) -> "capo_sts.types.assume_role_response.AssumeRoleResponse":
        r"""<p>Returns a set of temporary security credentials that you can use to access Amazon Web Services resources. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use <code>AssumeRole</code> within your account or for cross-account access. For a comparison of <code>AssumeRole</code> with other API operations that produce temporary credentials, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html">Requesting Temporary Security Credentials</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html">Compare STS credentials</a> in the <i>IAM User Guide</i>.</p> <p> <b>Permissions</b> </p> <p>The temporary security credentials created by <code>AssumeRole</code> can be used to make API calls to any Amazon Web Services service with the following exception: You cannot call the Amazon Web Services STS <code>GetFederationToken</code> or <code>GetSessionToken</code> API operations.</p> <p>(Optional) You can pass inline or managed session policies to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p>When you create a role, you create two policies: a role trust policy that specifies <i>who</i> can assume the role, and a permissions policy that specifies <i>what</i> can be done with the role. You specify the trusted principal that is allowed to assume the role in the role trust policy.</p> <p>To assume a role from a different account, your Amazon Web Services account must be trusted by the role. The trust relationship is defined in the role's trust policy when the role is created. That trust policy states which accounts are allowed to delegate that access to users in the account. </p> <p>A user who wants to access a role in a different account must also have permissions that are delegated from the account administrator. The administrator must attach a policy that allows the user to call <code>AssumeRole</code> for the ARN of the role in the other account.</p> <p>To allow a user to assume a role in the same account, you can do either of the following:</p> <ul> <li> <p>Attach a policy to the user that allows the user to call <code>AssumeRole</code> (as long as the role's trust policy trusts the account).</p> </li> <li> <p>Add the user as a principal directly in the role's trust policy.</p> </li> </ul> <p>You can do either because the role’s trust policy acts as an IAM resource-based policy. When a resource-based policy grants access to a principal in the same account, no additional identity-based policy is required. For more information about trust policies and resource-based policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">IAM Policies</a> in the <i>IAM User Guide</i>.</p> <p> <b>Tags</b> </p> <p>(Optional) You can pass tag key-value pairs to your session. These tags are called session tags. For more information about session tags, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html">Tutorial: Using Tags for Attribute-Based Access Control</a> in the <i>IAM User Guide</i>.</p> <p>You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining">Chaining Roles with Session Tags</a> in the <i>IAM User Guide</i>.</p> <p> <b>Using MFA with AssumeRole</b> </p> <p>(Optional) You can include multi-factor authentication (MFA) information when you call <code>AssumeRole</code>. This is useful for cross-account scenarios to ensure that the user that assumes the role has been authenticated with an Amazon Web Services MFA device. In that scenario, the trust policy of the role being assumed includes a condition that tests for MFA authentication. If the caller does not include valid MFA information, the request to assume the role is denied. The condition in a trust policy that tests for MFA authentication might look like the following example.</p> <p> <code>"Condition": {"Bool": {"aws:MultiFactorAuthPresent": true}}</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/MFAProtectedAPI.html">Configuring MFA-Protected API Access</a> in the <i>IAM User Guide</i> guide.</p> <p>To use MFA with <code>AssumeRole</code>, you pass values for the <code>SerialNumber</code> and <code>TokenCode</code> parameters. The <code>SerialNumber</code> value identifies the user's hardware or virtual MFA device. The <code>TokenCode</code> is the time-based one-time password (TOTP) that the MFA device produces. </p>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the role to assume.</p>
            role_session_name: <p>An identifier for the assumed role session.</p> <p>Use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. In cross-account scenarios, the role session name is visible to, and can be logged by the account that owns the role. The role session name is also used in the ARN of the assumed role principal. This means that subsequent cross-account API requests that use the temporary security credentials will expose the role session name to the external account in their CloudTrail logs.</p> <p>For security purposes, administrators can view this field in <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html#cloudtrail-integration_signin-tempcreds">CloudTrail logs</a> to help identify who performed an action in Amazon Web Services. Your administrator might require that you specify your user name as the session name when you assume the role. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_rolesessionname"> <code>sts:RoleSessionName</code> </a>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=,.@-</p>
            policy_arns: <p>The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.</p> <p>This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the Amazon Web Services General Reference.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p>
            policy: <p>An IAM policy in JSON format that you want to use as an inline session policy.</p> <p>This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p>The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (\u0020 through \u00FF). It can also include the tab (\u0009), linefeed (\u000A), and carriage return (\u000D) characters.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>For more information about role session permissions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session policies</a>.</p>
            duration_seconds: <p>The duration, in seconds, of the role session. The value specified can range from 900 seconds (15 minutes) up to the maximum session duration set for the role. The maximum session duration setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting or the administrator setting (whichever is lower), the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. </p> <p>Role chaining limits your Amazon Web Services CLI or Amazon Web Services API role session to a maximum of one hour. When you use the <code>AssumeRole</code> API operation to assume a role, you can specify the duration of your role session with the <code>DurationSeconds</code> parameter. You can specify a parameter value of up to 43200 seconds (12 hours), depending on the maximum session duration setting for your role. However, if you assume a role using role chaining and provide a <code>DurationSeconds</code> parameter value greater than one hour, the operation fails. To learn how to view the maximum value for your role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html#id_roles_update-session-duration">Update the maximum session duration for a role</a>.</p> <p>By default, the value is set to <code>3600</code> seconds. </p> <note> <p>The <code>DurationSeconds</code> parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a <code>SessionDuration</code> parameter that specifies the maximum length of the console session. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html">Creating a URL that Enables Federated Users to Access the Amazon Web Services Management Console</a> in the <i>IAM User Guide</i>.</p> </note>
            tags: <p>A list of session tags that you want to pass. Each session tag consists of a key name and an associated value. For more information about session tags, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Tagging Amazon Web Services STS Sessions</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters, and the values can’t exceed 256 characters. For these and additional limits, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length">IAM and STS Character Limits</a> in the <i>IAM User Guide</i>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>You can pass a session tag with the same key as a tag that is already attached to the role. When you do, session tags override a role tag with the same key. </p> <p>Tag key–value pairs are not case sensitive, but case is preserved. This means that you cannot have separate <code>Department</code> and <code>department</code> tag keys. Assume that the role has the <code>Department</code>=<code>Marketing</code> tag and you pass the <code>department</code>=<code>engineering</code> session tag. <code>Department</code> and <code>department</code> are not saved as separate tags, and the session tag passed in the request takes precedence over the role tag.</p> <p>Additionally, if you used temporary credentials to perform this operation, the new session inherits any transitive session tags from the calling session. If you pass a session tag with the same key as an inherited tag, the operation fails. To view the inherited tags for a session, see the CloudTrail logs. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_ctlogs">Viewing Session Tags in CloudTrail</a> in the <i>IAM User Guide</i>.</p>
            transitive_tag_keys: <p>A list of keys for session tags that you want to set as transitive. If you set a tag key as transitive, the corresponding key and value passes to subsequent sessions in a role chain. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining">Chaining Roles with Session Tags</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. The transitive status of a session tag does not impact its packed binary size.</p> <p>If you choose not to specify a transitive tag key, then no tags are passed from this session to any subsequent sessions.</p>
            external_id: <p>A unique identifier that might be required when you assume a role in another account. If the administrator of the account to which the role belongs provided you with an external ID, then provide that value in the <code>ExternalId</code> parameter. This value can be any string, such as a passphrase or account number. A cross-account role is usually set up to trust everyone in an account. Therefore, the administrator of the trusting account might send an external ID to the administrator of the trusted account. That way, only someone with the ID can assume the role, rather than everyone in the account. For more information about the external ID, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html">How to Use an External ID When Granting Access to Your Amazon Web Services Resources to a Third Party</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=,.@:\/-</p>
            serial_number: <p>The identification number of the MFA device that is associated with the user who is making the <code>AssumeRole</code> call. Specify this value if the trust policy of the role being assumed includes a condition that requires MFA authentication. The value is either the serial number for a hardware device (such as <code>GAHT12345678</code>) or an Amazon Resource Name (ARN) for a virtual device (such as <code>arn:aws:iam::123456789012:mfa/user</code>).</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=/:,.@-</p>
            token_code: <p>The value provided by the MFA device, if the trust policy of the role being assumed requires MFA. (In other words, if the policy includes a condition that tests for MFA). If the role being assumed requires MFA and if the <code>TokenCode</code> value is missing or expired, the <code>AssumeRole</code> call returns an "access denied" error.</p> <p>The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.</p>
            source_identity: <p>The source identity specified by the principal that is calling the <code>AssumeRole</code> operation. The source identity value persists across <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-role-chaining">chained role</a> sessions.</p> <p>You can require users to specify a source identity when they assume a role. You do this by using the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceidentity"> <code>sts:SourceIdentity</code> </a> condition key in a role trust policy. You can use source identity information in CloudTrail logs to determine who took actions with a role. You can use the <code>aws:SourceIdentity</code> condition key to further control access to Amazon Web Services resources based on the value of source identity. For more information about using source identity, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html">Monitor and control actions taken with assumed roles</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: +=,.@-. You cannot use a value that begins with the text <code>aws:</code>. This prefix is reserved for Amazon Web Services internal use.</p>
            provided_contexts: <p>A list of previously acquired trusted context assertions in the format of a JSON array. The trusted context assertion is signed and encrypted by Amazon Web Services STS.</p> <p>The following is an example of a <code>ProvidedContext</code> value that includes a single trusted context assertion and the ARN of the context provider from which the trusted context assertion was generated.</p> <p> <code>[{"ProviderArn":"arn:aws:iam::aws:contextProvider/IdentityCenter","ContextAssertion":"trusted-context-assertion"}]</code> </p>

        Raises:
            capo_sts.errors.expired_token_exception.ExpiredTokenException: <p>The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.</p>
            capo_sts.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The request was rejected because the policy document was malformed. The error message describes the specific error.</p>
            capo_sts.errors.packed_policy_too_large_exception.PackedPolicyTooLargeException: <p>The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, session policy ARNs, and session tags into a packed binary format that has a separate limit. The error message indicates by percentage how close the policies and tags are to the upper size limit. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>You could receive this error even though you meet other defined session policy and session tag limits. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-limits-entity-length">IAM and STS Entity Character Limits</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.region_disabled_exception.RegionDisabledException: <p>STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate">Activating and Deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To assume a role

            >>> await client.assume_role(role_arn='arn:aws:iam::123456789012:role/demo', role_session_name='testAssumeRoleSession', policy='escaped-JSON-IAM-POLICY', tags=[{'Key': 'Project', 'Value': 'Unicorn'}, {'Key': 'Team', 'Value': 'Automation'}, {'Key': 'Cost-Center', 'Value': '12345'}], transitive_tag_keys=['Project', 'Cost-Center'], external_id='123ABC')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.assume_role_request.AssumeRoleRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.assume_role_response.AssumeRoleResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.assume_role

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.assume_role.async_assume_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.assume_role_request.AssumeRoleRequest = {
            "role_arn": role_arn,
            "role_session_name": role_session_name,
        }
        if policy_arns is not None:
            input_["policy_arns"] = policy_arns
        if policy is not None:
            input_["policy"] = policy
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if tags is not None:
            input_["tags"] = tags
        if transitive_tag_keys is not None:
            input_["transitive_tag_keys"] = transitive_tag_keys
        if external_id is not None:
            input_["external_id"] = external_id
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if token_code is not None:
            input_["token_code"] = token_code
        if source_identity is not None:
            input_["source_identity"] = source_identity
        if provided_contexts is not None:
            input_["provided_contexts"] = provided_contexts
        if minimum_session_token_size is not None:
            input_["minimum_session_token_size"] = minimum_session_token_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def assume_role_with_saml(
        self,
        role_arn: "capo_sts.types.arn_type.arnType",
        principal_arn: "capo_sts.types.arn_type.arnType",
        saml_assertion: "capo_sts.types.saml_assertion_type.SAMLAssertionType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
        policy_arns: Optional[
            "capo_sts.types.policy_descriptor_list_type.policyDescriptorListType"
        ] = None,
        policy: Optional[
            "capo_sts.types.session_policy_document_type.sessionPolicyDocumentType"
        ] = None,
        duration_seconds: Optional[
            "capo_sts.types.role_duration_seconds_type.roleDurationSecondsType"
        ] = None,
        minimum_session_token_size: Optional[
            "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
        ] = None,
    ) -> "capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse":
        r"""<p>Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response. This operation provides a mechanism for tying an enterprise identity store or directory to role-based Amazon Web Services access without user-specific credentials or configuration. For a comparison of <code>AssumeRoleWithSAML</code> with the other API operations that produce temporary credentials, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html">Requesting Temporary Security Credentials</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html">Compare STS credentials</a> in the <i>IAM User Guide</i>.</p> <p>The temporary security credentials returned by this operation consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to Amazon Web Services services.</p> <note> <p>AssumeRoleWithSAML will not work on IAM Identity Center managed roles. These roles' names start with <code>AWSReservedSSO_</code>.</p> </note> <p> <b>Session Duration</b> </p> <p>By default, the temporary security credentials created by <code>AssumeRoleWithSAML</code> last for one hour. However, you can use the optional <code>DurationSeconds</code> parameter to specify the duration of your session. Your role session lasts for the duration that you specify, or until the time specified in the SAML authentication response's <code>SessionNotOnOrAfter</code> value, whichever is shorter. You can provide a <code>DurationSeconds</code> value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session">View the Maximum Session Duration Setting for a Role</a> in the <i>IAM User Guide</i>. The maximum session duration limit applies when you use the <code>AssumeRole*</code> API operations or the <code>assume-role*</code> CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html">Using IAM Roles</a> in the <i>IAM User Guide</i>.</p> <note> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-role-chaining">Role chaining</a> limits your CLI or Amazon Web Services API role session to a maximum of one hour. When you use the <code>AssumeRole</code> API operation to assume a role, you can specify the duration of your role session with the <code>DurationSeconds</code> parameter. You can specify a parameter value of up to 43200 seconds (12 hours), depending on the maximum session duration setting for your role. However, if you assume a role using role chaining and provide a <code>DurationSeconds</code> parameter value greater than one hour, the operation fails.</p> </note> <p> <b>Permissions</b> </p> <p>The temporary security credentials created by <code>AssumeRoleWithSAML</code> can be used to make API calls to any Amazon Web Services service with the following exception: you cannot call the STS <code>GetFederationToken</code> or <code>GetSessionToken</code> API operations.</p> <p>(Optional) You can pass inline or managed <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">session policies</a> to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p>Calling <code>AssumeRoleWithSAML</code> does not require the use of Amazon Web Services security credentials. The identity of the caller is validated by using keys in the metadata document that is uploaded for the SAML provider entity for your identity provider. </p> <important> <p>Calling <code>AssumeRoleWithSAML</code> can result in an entry in your CloudTrail logs. The entry includes the value in the <code>NameID</code> element of the SAML assertion. We recommend that you use a <code>NameIDType</code> that is not associated with any personally identifiable information (PII). For example, you could instead use the persistent identifier (<code>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</code>).</p> </important> <p> <b>Tags</b> </p> <p>(Optional) You can configure your IdP to pass attributes into your SAML assertion as session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters and the values can’t exceed 256 characters. For these and additional limits, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length">IAM and STS Character Limits</a> in the <i>IAM User Guide</i>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>You can pass a session tag with the same key as a tag that is attached to the role. When you do, session tags override the role's tags with the same key.</p> <p>An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html">Tutorial: Using Tags for Attribute-Based Access Control</a> in the <i>IAM User Guide</i>.</p> <p>You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining">Chaining Roles with Session Tags</a> in the <i>IAM User Guide</i>.</p> <p> <b>SAML Configuration</b> </p> <p>Before your application can call <code>AssumeRoleWithSAML</code>, you must configure your SAML identity provider (IdP) to issue the claims required by Amazon Web Services. Additionally, you must use Identity and Access Management (IAM) to create a SAML provider entity in your Amazon Web Services account that represents your identity provider. You must also create an IAM role that specifies this SAML provider in its trust policy. </p> <p>For more information, see the following resources:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html">About SAML 2.0-based Federation</a> in the <i>IAM User Guide</i>. </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html">Creating SAML Identity Providers</a> in the <i>IAM User Guide</i>. </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.html">Configuring a Relying Party and Claims</a> in the <i>IAM User Guide</i>. </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_saml.html">Creating a Role for SAML 2.0 Federation</a> in the <i>IAM User Guide</i>. </p> </li> </ul>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the role that the caller is assuming.</p>
            principal_arn: <p>The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.</p>
            saml_assertion: <p>The base64 encoded SAML authentication response provided by the IdP.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/create-role-saml-IdP-tasks.html">Configuring a Relying Party and Adding Claims</a> in the <i>IAM User Guide</i>. </p>
            policy_arns: <p>The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.</p> <p>This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the Amazon Web Services General Reference.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p>
            policy: <p>An IAM policy in JSON format that you want to use as an inline session policy.</p> <p>This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>. </p> <p>The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (\u0020 through \u00FF). It can also include the tab (\u0009), linefeed (\u000A), and carriage return (\u000D) characters.</p> <p>For more information about role session permissions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session policies</a>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note>
            duration_seconds: <p>The duration, in seconds, of the role session. Your role session lasts for the duration that you specify for the <code>DurationSeconds</code> parameter, or until the time specified in the SAML authentication response's <code>SessionNotOnOrAfter</code> value, whichever is shorter. You can provide a <code>DurationSeconds</code> value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session">View the Maximum Session Duration Setting for a Role</a> in the <i>IAM User Guide</i>.</p> <p>By default, the value is set to <code>3600</code> seconds. </p> <note> <p>The <code>DurationSeconds</code> parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a <code>SessionDuration</code> parameter that specifies the maximum length of the console session. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html">Creating a URL that Enables Federated Users to Access the Amazon Web Services Management Console</a> in the <i>IAM User Guide</i>.</p> </note>

        Raises:
            capo_sts.errors.expired_token_exception.ExpiredTokenException: <p>The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.</p>
            capo_sts.errors.idp_rejected_claim_exception.IDPRejectedClaimException: <p>The identity provider (IdP) reported that authentication failed. This might be because the claim is invalid.</p> <p>If this error is returned for the <code>AssumeRoleWithWebIdentity</code> operation, it can also mean that the claim has expired or has been explicitly revoked. </p>
            capo_sts.errors.invalid_identity_token_exception.InvalidIdentityTokenException: <p>The web identity token that was passed could not be validated by Amazon Web Services. Get a new identity token from the identity provider and then retry the request.</p>
            capo_sts.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The request was rejected because the policy document was malformed. The error message describes the specific error.</p>
            capo_sts.errors.packed_policy_too_large_exception.PackedPolicyTooLargeException: <p>The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, session policy ARNs, and session tags into a packed binary format that has a separate limit. The error message indicates by percentage how close the policies and tags are to the upper size limit. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>You could receive this error even though you meet other defined session policy and session tag limits. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-limits-entity-length">IAM and STS Entity Character Limits</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.region_disabled_exception.RegionDisabledException: <p>STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate">Activating and Deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To assume a role using a SAML assertion

            >>> await client.assume_role_with_saml(role_arn='arn:aws:iam::123456789012:role/TestSaml', principal_arn='arn:aws:iam::123456789012:saml-provider/SAML-test', saml_assertion='VERYLONGENCODEDASSERTIONEXAMPLExzYW1sOkF1ZGllbmNlPmJsYW5rPC9zYW1sOkF1ZGllbmNlPjwvc2FtbDpBdWRpZW5jZVJlc3RyaWN0aW9uPjwvc2FtbDpDb25kaXRpb25zPjxzYW1sOlN1YmplY3Q+PHNhbWw6TmFtZUlEIEZvcm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6dHJhbnNpZW50Ij5TYW1sRXhhbXBsZTwvc2FtbDpOYW1lSUQ+PHNhbWw6U3ViamVjdENvbmZpcm1hdGlvbiBNZXRob2Q9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpjbTpiZWFyZXIiPjxzYW1sOlN1YmplY3RDb25maXJtYXRpb25EYXRhIE5vdE9uT3JBZnRlcj0iMjAxOS0xMS0wMVQyMDoyNTowNS4xNDVaIiBSZWNpcGllbnQ9Imh0dHBzOi8vc2lnbmluLmF3cy5hbWF6b24uY29tL3NhbWwiLz48L3NhbWw6U3ViamVjdENvbmZpcm1hdGlvbj48L3NhbWw6U3ViamVjdD48c2FtbDpBdXRoblN0YXRlbWVudCBBdXRoPD94bWwgdmpSZXNwb25zZT4=', duration_seconds=3600)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.assume_role_with_saml_request.AssumeRoleWithSAMLRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.assume_role_with_saml_response.AssumeRoleWithSAMLResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.assume_role_with_saml

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.assume_role_with_saml.async_assume_role_with_saml(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.assume_role_with_saml_request.AssumeRoleWithSAMLRequest = {
            "role_arn": role_arn,
            "principal_arn": principal_arn,
            "saml_assertion": saml_assertion,
        }
        if policy_arns is not None:
            input_["policy_arns"] = policy_arns
        if policy is not None:
            input_["policy"] = policy
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if minimum_session_token_size is not None:
            input_["minimum_session_token_size"] = minimum_session_token_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def assume_role_with_web_identity(
        self,
        role_arn: "capo_sts.types.arn_type.arnType",
        role_session_name: "capo_sts.types.role_session_name_type.roleSessionNameType",
        web_identity_token: "capo_sts.types.client_token_type.clientTokenType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
        provider_id: Optional["capo_sts.types.url_type.urlType"] = None,
        policy_arns: Optional[
            "capo_sts.types.policy_descriptor_list_type.policyDescriptorListType"
        ] = None,
        policy: Optional[
            "capo_sts.types.session_policy_document_type.sessionPolicyDocumentType"
        ] = None,
        duration_seconds: Optional[
            "capo_sts.types.role_duration_seconds_type.roleDurationSecondsType"
        ] = None,
        minimum_session_token_size: Optional[
            "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
        ] = None,
    ) -> "capo_sts.types.assume_role_with_web_identity_response.AssumeRoleWithWebIdentityResponse":
        r"""<p>Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider. Example providers include the OAuth 2.0 providers Login with Amazon and Facebook, or any OpenID Connect-compatible identity provider such as Google or <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html">Amazon Cognito federated identities</a>.</p> <note> <p>For mobile applications, we recommend that you use Amazon Cognito. You can use Amazon Cognito with the <a href="http://aws.amazon.com/sdkforios/">Amazon Web Services SDK for iOS Developer Guide</a> and the <a href="http://aws.amazon.com/sdkforandroid/">Amazon Web Services SDK for Android Developer Guide</a> to uniquely identify a user. You can also supply the user with a consistent identity throughout the lifetime of an application.</p> <p>To learn more about Amazon Cognito, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html">Amazon Cognito identity pools</a> in <i>Amazon Cognito Developer Guide</i>.</p> </note> <p>Calling <code>AssumeRoleWithWebIdentity</code> does not require the use of Amazon Web Services security credentials. Therefore, you can distribute an application (for example, on mobile devices) that requests temporary security credentials without including long-term Amazon Web Services credentials in the application. You also don't need to deploy server-based proxy services that use long-term Amazon Web Services credentials. Instead, the identity of the caller is validated by using a token from the web identity provider. For a comparison of <code>AssumeRoleWithWebIdentity</code> with the other API operations that produce temporary credentials, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html">Requesting Temporary Security Credentials</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html">Compare STS credentials</a> in the <i>IAM User Guide</i>.</p> <p>The temporary security credentials returned by this API consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to Amazon Web Services service API operations.</p> <p> <b>Session Duration</b> </p> <p>By default, the temporary security credentials created by <code>AssumeRoleWithWebIdentity</code> last for one hour. However, you can use the optional <code>DurationSeconds</code> parameter to specify the duration of your session. You can provide a value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html#id_roles_update-session-duration">Update the maximum session duration for a role </a> in the <i>IAM User Guide</i>. The maximum session duration limit applies when you use the <code>AssumeRole*</code> API operations or the <code>assume-role*</code> CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html">Using IAM Roles</a> in the <i>IAM User Guide</i>. </p> <p> <b>Permissions</b> </p> <p>The temporary security credentials created by <code>AssumeRoleWithWebIdentity</code> can be used to make API calls to any Amazon Web Services service with the following exception: you cannot call the STS <code>GetFederationToken</code> or <code>GetSessionToken</code> API operations.</p> <p>(Optional) You can pass inline or managed <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">session policies</a> to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p> <b>Tags</b> </p> <p>(Optional) You can configure your IdP to pass attributes into your web identity token as session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_adding-assume-role-idp">Passing session tags using AssumeRoleWithWebIdentity</a> in the <i>IAM User Guide</i>.</p> <p>You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters and the values can’t exceed 256 characters. For these and additional limits, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length">IAM and STS Character Limits</a> in the <i>IAM User Guide</i>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>You can pass a session tag with the same key as a tag that is attached to the role. When you do, the session tag overrides the role tag with the same key.</p> <p>An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html">Tutorial: Using Tags for Attribute-Based Access Control</a> in the <i>IAM User Guide</i>.</p> <p>You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining">Chaining Roles with Session Tags</a> in the <i>IAM User Guide</i>.</p> <p> <b>Identities</b> </p> <p>Before your application can call <code>AssumeRoleWithWebIdentity</code>, you must have an identity token from a supported identity provider and create a role that the application can assume. The role that your application assumes must trust the identity provider that is associated with the identity token. In other words, the identity provider must be specified in the role's trust policy. </p> <important> <p>Calling <code>AssumeRoleWithWebIdentity</code> can result in an entry in your CloudTrail logs. The entry includes the <a href="http://openid.net/specs/openid-connect-core-1_0.html#Claims">Subject</a> of the provided web identity token. We recommend that you avoid using any personally identifiable information (PII) in this field. For example, you could instead use a GUID or a pairwise identifier, as <a href="http://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes">suggested in the OIDC specification</a>.</p> </important> <p>For more information about how to use OIDC federation and the <code>AssumeRoleWithWebIdentity</code> API, see the following resources: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_manual.html">Using Web Identity Federation API Operations for Mobile Apps</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity">Federation Through a Web-based Identity Provider</a>. </p> </li> <li> <p> <a href="http://aws.amazon.com/sdkforios/">Amazon Web Services SDK for iOS Developer Guide</a> and <a href="http://aws.amazon.com/sdkforandroid/">Amazon Web Services SDK for Android Developer Guide</a>. These toolkits contain sample apps that show how to invoke the identity providers. The toolkits then show how to use the information from these providers to get and use temporary security credentials. </p> </li> </ul>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the role that the caller is assuming.</p> <note> <p>Additional considerations apply to Amazon Cognito identity pools that assume <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html">cross-account IAM roles</a>. The trust policies of these roles must accept the <code>cognito-identity.amazonaws.com</code> service principal and must contain the <code>cognito-identity.amazonaws.com:aud</code> condition key to restrict role assumption to users from your intended identity pools. A policy that trusts Amazon Cognito identity pools without this condition creates a risk that a user from an unintended identity pool can assume the role. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html#trust-policies"> Trust policies for IAM roles in Basic (Classic) authentication </a> in the <i>Amazon Cognito Developer Guide</i>.</p> </note>
            role_session_name: <p>An identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user who is using your application. That way, the temporary security credentials that your application will use are associated with that user. This session name is included as part of the ARN and assumed role ID in the <code>AssumedRoleUser</code> response element.</p> <p>For security purposes, administrators can view this field in <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html#cloudtrail-integration_signin-tempcreds">CloudTrail logs</a> to help identify who performed an action in Amazon Web Services. Your administrator might require that you specify your user name as the session name when you assume the role. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_rolesessionname"> <code>sts:RoleSessionName</code> </a>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-</p>
            web_identity_token: <p>The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Your application must get this token by authenticating the user who is using your application with a web identity provider before the application makes an <code>AssumeRoleWithWebIdentity</code> call. Timestamps in the token must be formatted as either an integer or a long integer. Tokens must be signed using either RSA keys (RS256, RS384, or RS512) or ECDSA keys (ES256, ES384, or ES512).</p>
            provider_id: <p>The fully qualified host component of the domain name of the OAuth 2.0 identity provider. Do not specify this value for an OpenID Connect identity provider.</p> <p>Currently <code>www.amazon.com</code> and <code>graph.facebook.com</code> are the only supported identity providers for OAuth 2.0 access tokens. Do not include URL schemes and port numbers.</p> <p>Do not specify this value for OpenID Connect ID tokens.</p>
            policy_arns: <p>The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.</p> <p>This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the Amazon Web Services General Reference.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p>
            policy: <p>An IAM policy in JSON format that you want to use as an inline session policy.</p> <p>This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p>The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (\u0020 through \u00FF). It can also include the tab (\u0009), linefeed (\u000A), and carriage return (\u000D) characters.</p> <p>For more information about role session permissions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session policies</a>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note>
            duration_seconds: <p>The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session">View the Maximum Session Duration Setting for a Role</a> in the <i>IAM User Guide</i>.</p> <p>By default, the value is set to <code>3600</code> seconds. </p> <note> <p>The <code>DurationSeconds</code> parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a <code>SessionDuration</code> parameter that specifies the maximum length of the console session. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html">Creating a URL that Enables Federated Users to Access the Amazon Web Services Management Console</a> in the <i>IAM User Guide</i>.</p> </note>

        Raises:
            capo_sts.errors.expired_token_exception.ExpiredTokenException: <p>The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.</p>
            capo_sts.errors.idp_communication_error_exception.IDPCommunicationErrorException: <p>The request could not be fulfilled because the identity provider (IDP) that was asked to verify the incoming identity token could not be reached. This is often a transient error caused by network conditions. Retry the request a limited number of times so that you don't exceed the request rate. If the error persists, the identity provider might be down or not responding.</p>
            capo_sts.errors.idp_rejected_claim_exception.IDPRejectedClaimException: <p>The identity provider (IdP) reported that authentication failed. This might be because the claim is invalid.</p> <p>If this error is returned for the <code>AssumeRoleWithWebIdentity</code> operation, it can also mean that the claim has expired or has been explicitly revoked. </p>
            capo_sts.errors.invalid_identity_token_exception.InvalidIdentityTokenException: <p>The web identity token that was passed could not be validated by Amazon Web Services. Get a new identity token from the identity provider and then retry the request.</p>
            capo_sts.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The request was rejected because the policy document was malformed. The error message describes the specific error.</p>
            capo_sts.errors.packed_policy_too_large_exception.PackedPolicyTooLargeException: <p>The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, session policy ARNs, and session tags into a packed binary format that has a separate limit. The error message indicates by percentage how close the policies and tags are to the upper size limit. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>You could receive this error even though you meet other defined session policy and session tag limits. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-limits-entity-length">IAM and STS Entity Character Limits</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.region_disabled_exception.RegionDisabledException: <p>STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate">Activating and Deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To assume a role as an OpenID Connect-federated user

            >>> await client.assume_role_with_web_identity(role_arn='arn:aws:iam::123456789012:role/FederatedWebIdentityRole', role_session_name='app1', policy='escaped-JSON-IAM-POLICY', web_identity_token='Atza%7CIQEBLjAsAhRFiXuWpUXuRvQ9PZL3GMFcYevydwIUFAHZwXZXXXXXXXXJnrulxKDHwy87oGKPznh0D6bEQZTSCzyoCtL_8S07pLpr0zMbn6w1lfVZKNTBdDansFBmtGnIsIapjI6xKR02Yc_2bQ8LZbUXSGm6Ry6_BG7PrtLZtj_dfCTj92xNGed-CrKqjG7nPBjNIL016GGvuS5gSvPRUxWES3VYfm1wl7WTI7jn-Pcb6M-buCgHhFOzTQxod27L9CqnOLio7N3gZAGpsp6n1-AJBOCJckcyXe2c6uD0srOJeZlKUm2eTDVMf8IehDVI0r1QOnTV6KzzAI3OY87Vd_cVMQ', provider_id='www.amazon.com', duration_seconds=3600)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.assume_role_with_web_identity_request.AssumeRoleWithWebIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.assume_role_with_web_identity_response.AssumeRoleWithWebIdentityResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.assume_role_with_web_identity

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.assume_role_with_web_identity.async_assume_role_with_web_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.assume_role_with_web_identity_request.AssumeRoleWithWebIdentityRequest = {
            "role_arn": role_arn,
            "role_session_name": role_session_name,
            "web_identity_token": web_identity_token,
        }
        if provider_id is not None:
            input_["provider_id"] = provider_id
        if policy_arns is not None:
            input_["policy_arns"] = policy_arns
        if policy is not None:
            input_["policy"] = policy
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if minimum_session_token_size is not None:
            input_["minimum_session_token_size"] = minimum_session_token_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def assume_root(
        self,
        target_principal: "capo_sts.types.target_principal_type.TargetPrincipalType",
        task_policy_arn: "capo_sts.types.policy_descriptor_type.PolicyDescriptorType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
        duration_seconds: Optional[
            "capo_sts.types.root_duration_seconds_type.RootDurationSecondsType"
        ] = None,
        minimum_session_token_size: Optional[
            "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
        ] = None,
    ) -> "capo_sts.types.assume_root_response.AssumeRootResponse":
        """<p>Returns a set of short term credentials you can use to perform privileged tasks on a member account in your organization. You must use credentials from an Organizations management account or a delegated administrator account for IAM to call <code>AssumeRoot</code>. You cannot use root user credentials to make this call.</p> <p>Before you can launch a privileged session, you must have centralized root access in your organization. For steps to enable this feature, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html">Centralize root access for member accounts</a> in the <i>IAM User Guide</i>.</p> <note> <p>The STS global endpoint is not supported for AssumeRoot. You must send this request to a Regional STS endpoint. For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html#sts-endpoints">Endpoints</a>.</p> </note> <p>You can track AssumeRoot in CloudTrail logs to determine what actions were performed in a session. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html">Track privileged tasks in CloudTrail</a> in the <i>IAM User Guide</i>.</p> <p>When granting access to privileged tasks you should only grant the necessary permissions required to perform that task. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html">Security best practices in IAM</a>. In addition, you can use <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html">service control policies</a> (SCPs) to manage and limit permissions in your organization. See <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html">General examples</a> in the <i>Organizations User Guide</i> for more information on SCPs.</p>

        Args:
            target_principal: <p>The member account principal ARN or account ID.</p>
            task_policy_arn: <p>The identity based policy that scopes the session to the privileged tasks that can be performed. You must use one of following Amazon Web Services managed policies to scope root session actions:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMAuditRootUserCredentials">IAMAuditRootUserCredentials</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMCreateRootUserPassword">IAMCreateRootUserPassword</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMDeleteRootUserCredentials">IAMDeleteRootUserCredentials</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-S3UnlockBucketPolicy">S3UnlockBucketPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-SQSUnlockQueuePolicy">SQSUnlockQueuePolicy</a> </p> </li> </ul>
            duration_seconds: <p>The duration, in seconds, of the privileged session. The value can range from 0 seconds up to the maximum session duration of 900 seconds (15 minutes). If you specify a value higher than this setting, the operation fails.</p> <p>By default, the value is set to <code>900</code> seconds.</p>

        Raises:
            capo_sts.errors.expired_token_exception.ExpiredTokenException: <p>The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.</p>
            capo_sts.errors.region_disabled_exception.RegionDisabledException: <p>STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate">Activating and Deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To launch a privileged session
            The following command retrieves a set of short-term credentials you can use to unlock an S3 bucket for a member account by removing the bucket policy.

            >>> await client.assume_root(target_principal='111122223333', task_policy_arn={'arn': 'arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy'}, duration_seconds=900)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.assume_root_request.AssumeRootRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.assume_root_response.AssumeRootResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.assume_root

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.assume_root.async_assume_root(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.assume_root_request.AssumeRootRequest = {
            "target_principal": target_principal,
            "task_policy_arn": task_policy_arn,
        }
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if minimum_session_token_size is not None:
            input_["minimum_session_token_size"] = minimum_session_token_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def decode_authorization_message(
        self,
        encoded_message: "capo_sts.types.encoded_message_type.encodedMessageType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
    ) -> "capo_sts.types.decode_authorization_message_response.DecodeAuthorizationMessageResponse":
        """<p>Decodes additional information about the authorization status of a request from an encoded message returned in response to an Amazon Web Services request.</p> <p>For example, if a user is not authorized to perform an operation that he or she has requested, the request returns a <code>Client.UnauthorizedOperation</code> response (an HTTP 403 response). Some Amazon Web Services operations additionally return an encoded message that can provide details about this authorization failure. </p> <note> <p>Only certain Amazon Web Services operations return an encoded authorization message. The documentation for an individual operation indicates whether that operation returns an encoded message in addition to returning an HTTP code.</p> </note> <p>The message is encoded because the details of the authorization status can contain privileged information that the user who requested the operation should not see. To decode an authorization status message, a user must be granted permissions through an IAM <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">policy</a> to request the <code>DecodeAuthorizationMessage</code> (<code>sts:DecodeAuthorizationMessage</code>) action. </p> <p>The decoded message includes the following type of information:</p> <ul> <li> <p>Whether the request was denied due to an explicit deny or due to the absence of an explicit allow. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow">Determining Whether a Request is Allowed or Denied</a> in the <i>IAM User Guide</i>. </p> </li> <li> <p>The principal who made the request.</p> </li> <li> <p>The requested action.</p> </li> <li> <p>The requested resource.</p> </li> <li> <p>The values of condition keys in the context of the user's request.</p> </li> </ul>

        Args:
            encoded_message: <p>The encoded message that was returned with the response.</p>

        Raises:
            capo_sts.errors.invalid_authorization_message_exception.InvalidAuthorizationMessageException: <p>The error returned if the message passed to <code>DecodeAuthorizationMessage</code> was invalid. This can happen if the token contains invalid characters, such as line breaks, or if the message has expired.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To decode information about an authorization status of a request

            >>> await client.decode_authorization_message(encoded_message='<encoded-message>')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.decode_authorization_message_request.DecodeAuthorizationMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.decode_authorization_message_response.DecodeAuthorizationMessageResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.decode_authorization_message

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.decode_authorization_message.async_decode_authorization_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.decode_authorization_message_request.DecodeAuthorizationMessageRequest = {
            "encoded_message": encoded_message
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_key_info(
        self,
        access_key_id: "capo_sts.types.access_key_id_type.accessKeyIdType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
    ) -> "capo_sts.types.get_access_key_info_response.GetAccessKeyInfoResponse":
        """<p>Returns the account identifier for the specified access key ID.</p> <p>Access keys consist of two parts: an access key ID (for example, <code>AKIAIOSFODNN7EXAMPLE</code>) and a secret access key (for example, <code>wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY</code>). For more information about access keys, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html">Managing Access Keys for IAM Users</a> in the <i>IAM User Guide</i>.</p> <p>When you pass an access key ID to this operation, it returns the ID of the Amazon Web Services account to which the keys belong. Access key IDs beginning with <code>AKIA</code> are long-term credentials for an IAM user or the Amazon Web Services account root user. Access key IDs beginning with <code>ASIA</code> are temporary credentials that are created using STS operations. If the account in the response belongs to you, you can sign in as the root user and review your root user access keys. Then, you can pull a <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html">credentials report</a> to learn which IAM user owns the keys. To learn who requested the temporary credentials for an <code>ASIA</code> access key, view the STS events in your <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html">CloudTrail logs</a> in the <i>IAM User Guide</i>.</p> <p>This operation does not indicate the state of the access key. The key might be active, inactive, or deleted. Active keys might not have permissions to perform an operation. Providing a deleted access key might return an error that the key doesn't exist.</p>

        Args:
            access_key_id: <p>The identifier of an access key.</p> <p>This parameter allows (through its regex pattern) a string of characters that can consist of any upper- or lowercase letter or digit.</p>

        Raises:
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.get_access_key_info_request.GetAccessKeyInfoRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.get_access_key_info_response.GetAccessKeyInfoResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.get_access_key_info

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.get_access_key_info.async_get_access_key_info(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.get_access_key_info_request.GetAccessKeyInfoRequest = {
            "access_key_id": access_key_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_caller_identity(
        self, *, config_overrides: Optional[AsyncSTSClientConfig] = None
    ) -> "capo_sts.types.get_caller_identity_response.GetCallerIdentityResponse":
        """<p>Returns details about the IAM user or role whose credentials are used to call the operation.</p> <note> <p>No permissions are required to perform this operation. If an administrator attaches a policy to your identity that explicitly denies access to the <code>sts:GetCallerIdentity</code> action, you can still perform this operation. Permissions are not required because the same information is returned when access is denied. To view an example response, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_access-denied-delete-mfa">I Am Not Authorized to Perform: iam:DeleteVirtualMFADevice</a> in the <i>IAM User Guide</i>.</p> </note>

        Raises:
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get details about a calling IAM user
            This example shows a request and response made with the credentials for a user named Alice in the AWS account 123456789012.

            >>> await client.get_caller_identity()
            To get details about a calling user federated with AssumeRole
            This example shows a request and response made with temporary credentials created by AssumeRole. The name of the assumed role is my-role-name, and the RoleSessionName is set to my-role-session-name.

            >>> await client.get_caller_identity()
            To get details about a calling user federated with GetFederationToken
            This example shows a request and response made with temporary credentials created by using GetFederationToken. The Name parameter is set to my-federated-user-name.

            >>> await client.get_caller_identity()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.get_caller_identity_request.GetCallerIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.get_caller_identity_response.GetCallerIdentityResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.get_caller_identity

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.get_caller_identity.async_get_caller_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.get_caller_identity_request.GetCallerIdentityRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_delegated_access_token(
        self,
        trade_in_token: "capo_sts.types.trade_in_token_type.tradeInTokenType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
    ) -> "capo_sts.types.get_delegated_access_token_response.GetDelegatedAccessTokenResponse":
        """<p>Exchanges a trade-in token for temporary Amazon Web Services credentials with the permissions associated with the assumed principal. This operation allows you to obtain credentials for a specific principal based on a trade-in token, enabling delegation of access to Amazon Web Services resources.</p>

        Args:
            trade_in_token: <p>The token to exchange for temporary Amazon Web Services credentials. This token must be valid and unexpired at the time of the request.</p>

        Raises:
            capo_sts.errors.expired_trade_in_token_exception.ExpiredTradeInTokenException: <p>The trade-in token provided in the request has expired and can no longer be exchanged for credentials. Request a new token and retry the operation.</p>
            capo_sts.errors.packed_policy_too_large_exception.PackedPolicyTooLargeException: <p>The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, session policy ARNs, and session tags into a packed binary format that has a separate limit. The error message indicates by percentage how close the policies and tags are to the upper size limit. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>You could receive this error even though you meet other defined session policy and session tag limits. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-limits-entity-length">IAM and STS Entity Character Limits</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.region_disabled_exception.RegionDisabledException: <p>STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate">Activating and Deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.get_delegated_access_token_request.GetDelegatedAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.get_delegated_access_token_response.GetDelegatedAccessTokenResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.get_delegated_access_token

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.get_delegated_access_token.async_get_delegated_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.get_delegated_access_token_request.GetDelegatedAccessTokenRequest = {
            "trade_in_token": trade_in_token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_federation_token(
        self,
        name: "capo_sts.types.user_name_type.userNameType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
        policy: Optional[
            "capo_sts.types.session_policy_document_type.sessionPolicyDocumentType"
        ] = None,
        policy_arns: Optional[
            "capo_sts.types.policy_descriptor_list_type.policyDescriptorListType"
        ] = None,
        duration_seconds: Optional[
            "capo_sts.types.duration_seconds_type.durationSecondsType"
        ] = None,
        tags: Optional["capo_sts.types.tag_list_type.tagListType"] = None,
        minimum_session_token_size: Optional[
            "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
        ] = None,
    ) -> "capo_sts.types.get_federation_token_response.GetFederationTokenResponse":
        r"""<p>Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a user. A typical use is in a proxy application that gets temporary security credentials on behalf of distributed applications inside a corporate network.</p> <p>You must call the <code>GetFederationToken</code> operation using the long-term security credentials of an IAM user. As a result, this call is appropriate in contexts where those credentials can be safeguarded, usually in a server-based application. For a comparison of <code>GetFederationToken</code> with the other API operations that produce temporary credentials, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html">Requesting Temporary Security Credentials</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html">Compare STS credentials</a> in the <i>IAM User Guide</i>.</p> <p>Although it is possible to call <code>GetFederationToken</code> using the security credentials of an Amazon Web Services account root user rather than an IAM user that you create for the purpose of a proxy application, we do not recommend it. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials">Safeguard your root user credentials and don't use them for everyday tasks</a> in the <i>IAM User Guide</i>. </p> <note> <p>You can create a mobile-based or browser-based app that can authenticate users using a web identity provider like Login with Amazon, Facebook, Google, or an OpenID Connect-compatible identity provider. In this case, we recommend that you use <a href="http://aws.amazon.com/cognito/">Amazon Cognito</a> or <code>AssumeRoleWithWebIdentity</code>. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity">Federation Through a Web-based Identity Provider</a> in the <i>IAM User Guide</i>.</p> </note> <p> <b>Session duration</b> </p> <p>The temporary credentials are valid for the specified duration, from 900 seconds (15 minutes) up to a maximum of 129,600 seconds (36 hours). The default session duration is 43,200 seconds (12 hours). Temporary credentials obtained by using the root user credentials have a maximum duration of 3,600 seconds (1 hour).</p> <p> <b>Permissions</b> </p> <p>You can use the temporary credentials created by <code>GetFederationToken</code> in any Amazon Web Services service with the following exceptions:</p> <ul> <li> <p>You cannot call any IAM operations using the CLI or the Amazon Web Services API. This limitation does not apply to console sessions.</p> </li> <li> <p>You cannot call any STS operations except <code>GetCallerIdentity</code>.</p> </li> </ul> <p>You can use temporary credentials for single sign-on (SSO) to the console.</p> <p>You must pass an inline or managed <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">session policy</a> to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters.</p> <p>Though the session policy parameters are optional, if you do not pass a policy, then the resulting federated user session has no permissions. When you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>. For information about using <code>GetFederationToken</code> to create temporary security credentials, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_getfederationtoken">GetFederationToken—Federation Through a Custom Identity Broker</a>. </p> <p>You can use the credentials to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the <code>Principal</code> element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions granted by the session policies.</p> <p> <b>Tags</b> </p> <p>(Optional) You can pass tag key-value pairs to your session. These are called session tags. For more information about session tags, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <note> <p>You can create a mobile-based or browser-based app that can authenticate users using a web identity provider like Login with Amazon, Facebook, Google, or an OpenID Connect-compatible identity provider. In this case, we recommend that you use <a href="http://aws.amazon.com/cognito/">Amazon Cognito</a> or <code>AssumeRoleWithWebIdentity</code>. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity">Federation Through a Web-based Identity Provider</a> in the <i>IAM User Guide</i>.</p> </note> <p>An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html">Tutorial: Using Tags for Attribute-Based Access Control</a> in the <i>IAM User Guide</i>.</p> <p>Tag key–value pairs are not case sensitive, but case is preserved. This means that you cannot have separate <code>Department</code> and <code>department</code> tag keys. Assume that the user that you are federating has the <code>Department</code>=<code>Marketing</code> tag and you pass the <code>department</code>=<code>engineering</code> session tag. <code>Department</code> and <code>department</code> are not saved as separate tags, and the session tag passed in the request takes precedence over the user tag.</p>

        Args:
            name: <p>The name of the federated user. The name is used as an identifier for the temporary security credentials (such as <code>Bob</code>). For example, you can reference the federated user name in a resource-based policy, such as in an Amazon S3 bucket policy.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-</p>
            policy: <p>An IAM policy in JSON format that you want to use as an inline session policy.</p> <p>You must pass an inline or managed <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">session policy</a> to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies.</p> <p>This parameter is optional. However, if you do not pass any session policies, then the resulting federated user session has no permissions.</p> <p>When you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p>The resulting credentials can be used to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the <code>Principal</code> element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions that are granted by the session policies.</p> <p>The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (\u0020 through \u00FF). It can also include the tab (\u0009), linefeed (\u000A), and carriage return (\u000D) characters.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note>
            policy_arns: <p>The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as a managed session policy. The policies must exist in the same account as the IAM user that is requesting federated access.</p> <p>You must pass an inline or managed <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">session policy</a> to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. You can provide up to 10 managed policy ARNs. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the Amazon Web Services General Reference.</p> <p>This parameter is optional. However, if you do not pass any session policies, then the resulting federated user session has no permissions.</p> <p>When you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session">Session Policies</a> in the <i>IAM User Guide</i>.</p> <p>The resulting credentials can be used to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the <code>Principal</code> element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions that are granted by the session policies.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note>
            duration_seconds: <p>The duration, in seconds, that the session should last. Acceptable durations for federation sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default. Sessions obtained using root user credentials are restricted to a maximum of 3,600 seconds (one hour). If the specified duration is longer than one hour, the session obtained by using root user credentials defaults to one hour.</p>
            tags: <p>A list of session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters and the values can’t exceed 256 characters. For these and additional limits, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length">IAM and STS Character Limits</a> in the <i>IAM User Guide</i>.</p> <note> <p>An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The <code>PackedPolicySize</code> response element indicates by percentage how close the policies and tags for your request are to the upper size limit.</p> </note> <p>You can pass a session tag with the same key as a tag that is already attached to the user you are federating. When you do, session tags override a user tag with the same key. </p> <p>Tag key–value pairs are not case sensitive, but case is preserved. This means that you cannot have separate <code>Department</code> and <code>department</code> tag keys. Assume that the role has the <code>Department</code>=<code>Marketing</code> tag and you pass the <code>department</code>=<code>engineering</code> session tag. <code>Department</code> and <code>department</code> are not saved as separate tags, and the session tag passed in the request takes precedence over the role tag.</p>

        Raises:
            capo_sts.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>The request was rejected because the policy document was malformed. The error message describes the specific error.</p>
            capo_sts.errors.packed_policy_too_large_exception.PackedPolicyTooLargeException: <p>The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, session policy ARNs, and session tags into a packed binary format that has a separate limit. The error message indicates by percentage how close the policies and tags are to the upper size limit. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html">Passing Session Tags in STS</a> in the <i>IAM User Guide</i>.</p> <p>You could receive this error even though you meet other defined session policy and session tag limits. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-limits-entity-length">IAM and STS Entity Character Limits</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.region_disabled_exception.RegionDisabledException: <p>STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate">Activating and Deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get temporary credentials for a role by using GetFederationToken

            >>> await client.get_federation_token(name='testFedUserSession', policy='escaped-JSON-IAM-POLICY', duration_seconds=3600, tags=[{'Key': 'Project', 'Value': 'Pegasus'}, {'Key': 'Cost-Center', 'Value': '98765'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.get_federation_token_request.GetFederationTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.get_federation_token_response.GetFederationTokenResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.get_federation_token

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.get_federation_token.async_get_federation_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.get_federation_token_request.GetFederationTokenRequest = {
            "name": name
        }
        if policy is not None:
            input_["policy"] = policy
        if policy_arns is not None:
            input_["policy_arns"] = policy_arns
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if tags is not None:
            input_["tags"] = tags
        if minimum_session_token_size is not None:
            input_["minimum_session_token_size"] = minimum_session_token_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session_token(
        self,
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
        duration_seconds: Optional[
            "capo_sts.types.duration_seconds_type.durationSecondsType"
        ] = None,
        serial_number: Optional[
            "capo_sts.types.serial_number_type.serialNumberType"
        ] = None,
        token_code: Optional["capo_sts.types.token_code_type.tokenCodeType"] = None,
        minimum_session_token_size: Optional[
            "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
        ] = None,
    ) -> "capo_sts.types.get_session_token_response.GetSessionTokenResponse":
        """<p>Returns a set of temporary credentials for an Amazon Web Services account or IAM user. The credentials consist of an access key ID, a secret access key, and a security token. Typically, you use <code>GetSessionToken</code> if you want to use MFA to protect programmatic calls to specific Amazon Web Services API operations like Amazon EC2 <code>StopInstances</code>.</p> <p>MFA-enabled IAM users must call <code>GetSessionToken</code> and submit an MFA code that is associated with their MFA device. Using the temporary security credentials that the call returns, IAM users can then make programmatic calls to API operations that require MFA authentication. An incorrect MFA code causes the API to return an access denied error. For a comparison of <code>GetSessionToken</code> with the other API operations that produce temporary credentials, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html">Requesting Temporary Security Credentials</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts-comparison.html">Compare STS credentials</a> in the <i>IAM User Guide</i>.</p> <note> <p>No permissions are required for users to perform this operation. The purpose of the <code>sts:GetSessionToken</code> operation is to authenticate the user using MFA. You cannot use policies to control authentication operations. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_getsessiontoken.html">Permissions for GetSessionToken</a> in the <i>IAM User Guide</i>.</p> </note> <p> <b>Session Duration</b> </p> <p>The <code>GetSessionToken</code> operation must be called by using the long-term Amazon Web Services security credentials of an IAM user. Credentials that are created by IAM users are valid for the duration that you specify. This duration can range from 900 seconds (15 minutes) up to a maximum of 129,600 seconds (36 hours), with a default of 43,200 seconds (12 hours). Credentials based on account credentials can range from 900 seconds (15 minutes) up to 3,600 seconds (1 hour), with a default of 1 hour. </p> <p> <b>Permissions</b> </p> <p>The temporary security credentials created by <code>GetSessionToken</code> can be used to make API calls to any Amazon Web Services service with the following exceptions:</p> <ul> <li> <p>You cannot call any IAM API operations unless MFA authentication information is included in the request.</p> </li> <li> <p>You cannot call any STS API <i>except</i> <code>AssumeRole</code> or <code>GetCallerIdentity</code>.</p> </li> </ul> <p>The credentials that <code>GetSessionToken</code> returns are based on permissions associated with the IAM user whose credentials were used to call the operation. The temporary credentials have the same permissions as the IAM user.</p> <note> <p>Although it is possible to call <code>GetSessionToken</code> using the security credentials of an Amazon Web Services account root user rather than an IAM user, we do not recommend it. If <code>GetSessionToken</code> is called using root user credentials, the temporary credentials have root user permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials">Safeguard your root user credentials and don't use them for everyday tasks</a> in the <i>IAM User Guide</i> </p> </note> <p>For more information about using <code>GetSessionToken</code> to create temporary credentials, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_getsessiontoken">Temporary Credentials for Users in Untrusted Environments</a> in the <i>IAM User Guide</i>. </p>

        Args:
            duration_seconds: <p>The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default. Sessions for Amazon Web Services account owners are restricted to a maximum of 3,600 seconds (one hour). If the duration is longer than one hour, the session for Amazon Web Services account owners defaults to one hour.</p>
            serial_number: <p>The identification number of the MFA device that is associated with the IAM user who is making the <code>GetSessionToken</code> call. Specify this value if the IAM user has a policy that requires MFA authentication. The value is either the serial number for a hardware device (such as <code>GAHT12345678</code>) or an Amazon Resource Name (ARN) for a virtual device (such as <code>arn:aws:iam::123456789012:mfa/user</code>). You can find the device for an IAM user by going to the Amazon Web Services Management Console and viewing the user's security credentials. </p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>
            token_code: <p>The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, specify this value. If MFA authentication is required, the user must provide a code when requesting a set of temporary security credentials. A user who fails to provide the code receives an "access denied" response when requesting resources that require MFA authentication.</p> <p>The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.</p>

        Raises:
            capo_sts.errors.region_disabled_exception.RegionDisabledException: <p>STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate">Activating and Deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get temporary credentials for an IAM user or an AWS account

            >>> await client.get_session_token(duration_seconds=3600, serial_number='YourMFASerialNumber', token_code='123456')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.get_session_token_request.GetSessionTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.get_session_token_response.GetSessionTokenResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.get_session_token

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.get_session_token.async_get_session_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.get_session_token_request.GetSessionTokenRequest = {}
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if token_code is not None:
            input_["token_code"] = token_code
        if minimum_session_token_size is not None:
            input_["minimum_session_token_size"] = minimum_session_token_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_web_identity_token(
        self,
        audience: "capo_sts.types.web_identity_token_audience_list_type.webIdentityTokenAudienceListType",
        signing_algorithm: "capo_sts.types.jwt_algorithm_type.jwtAlgorithmType",
        *,
        config_overrides: Optional[AsyncSTSClientConfig] = None,
        duration_seconds: Optional[
            "capo_sts.types.web_identity_token_duration_seconds_type.webIdentityTokenDurationSecondsType"
        ] = None,
        tags: Optional["capo_sts.types.tag_list_type.tagListType"] = None,
    ) -> "capo_sts.types.get_web_identity_token_response.GetWebIdentityTokenResponse":
        """<p>Returns a signed JSON Web Token (JWT) that represents the calling Amazon Web Services identity. The returned JWT can be used to authenticate with external services that support OIDC discovery. The token is signed by Amazon Web Services STS and can be publicly verified using the verification keys published at the issuer's JWKS endpoint.</p> <note> <p>The <code>GetWebIdentityToken</code> API is not available on the STS Global endpoint.</p> </note>

        Args:
            audience: <p>The intended recipient of the web identity token. This value populates the <code>aud</code> claim in the JWT and should identify the service or application that will validate and use the token. The external service should verify this claim to ensure the token was intended for their use.</p>
            duration_seconds: <p>The duration, in seconds, for which the JSON Web Token (JWT) will remain valid. The value can range from 60 seconds (1 minute) to 3600 seconds (1 hour). If not specified, the default duration is 300 seconds (5 minutes). The token is designed to be short-lived and should be used for proof of identity, then exchanged for credentials or short-lived tokens in the external service.</p>
            signing_algorithm: <p>The cryptographic algorithm to use for signing the JSON Web Token (JWT). Valid values are RS256 (RSA with SHA-256) and ES384 (ECDSA using P-384 curve with SHA-384). </p>
            tags: <p>An optional list of tags to include in the JSON Web Token (JWT). These tags are added as custom claims to the JWT and can be used by the downstream service for authorization decisions. </p>

        Raises:
            capo_sts.errors.jwt_payload_size_exceeded_exception.JWTPayloadSizeExceededException: <p>The requested token payload size exceeds the maximum allowed size. Reduce the number of request tags included in the <code>GetWebIdentityToken</code> API call to reduce the token payload size.</p>
            capo_sts.errors.outbound_web_identity_federation_disabled_exception.OutboundWebIdentityFederationDisabledException: <p>The outbound web identity federation feature is not enabled for this account. To use this feature, you must first enable it through the Amazon Web Services Management Console or API.</p>
            capo_sts.errors.session_duration_escalation_exception.SessionDurationEscalationException: <p>The requested token duration would extend the session beyond its original expiration time. You cannot use this operation to extend the lifetime of a session beyond what was granted when the session was originally created.</p>
            capo_sts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sts.types.get_web_identity_token_request.GetWebIdentityTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_sts.types.get_web_identity_token_response.GetWebIdentityTokenResponse"
        ]:
            import capo_sts._operations.aws_security_token_service_v20110615.get_web_identity_token

            (
                output,
                http_response,
            ) = await capo_sts._operations.aws_security_token_service_v20110615.get_web_identity_token.async_get_web_identity_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sts.types.get_web_identity_token_request.GetWebIdentityTokenRequest = {
            "audience": audience,
            "signing_algorithm": signing_algorithm,
        }
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
