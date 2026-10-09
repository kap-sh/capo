"""Generated from Smithy shape ``com.amazonaws.acmpca#ACMPrivateCA``."""

import random
import time
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_acm_pca._auth._signers
import capo_acm_pca._auth._sigv4
from capo_acm_pca._async import anysleep
from capo_acm_pca._auth._identity import Credentials
from capo_acm_pca._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_acm_pca._auth._zapros_handler import AuthMiddleware
from capo_acm_pca._pagination import resolve_path as _resolve_path
from capo_acm_pca._services._aws_config import aaws_config
from capo_acm_pca._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from capo_acm_pca.errors import ServiceError, WaiterFailedError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_acm_pca.types.account_id
    import capo_acm_pca.types.action_list
    import capo_acm_pca.types.api_passthrough
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.audit_report_id
    import capo_acm_pca.types.audit_report_response_format
    import capo_acm_pca.types.aws_policy
    import capo_acm_pca.types.certificate_authority
    import capo_acm_pca.types.certificate_authority_configuration
    import capo_acm_pca.types.certificate_authority_status
    import capo_acm_pca.types.certificate_authority_type
    import capo_acm_pca.types.certificate_authority_usage_mode
    import capo_acm_pca.types.certificate_body_blob
    import capo_acm_pca.types.certificate_chain_blob
    import capo_acm_pca.types.create_certificate_authority_audit_report_request
    import capo_acm_pca.types.create_certificate_authority_audit_report_response
    import capo_acm_pca.types.create_certificate_authority_request
    import capo_acm_pca.types.create_certificate_authority_response
    import capo_acm_pca.types.create_permission_request
    import capo_acm_pca.types.csr_blob
    import capo_acm_pca.types.delete_certificate_authority_request
    import capo_acm_pca.types.delete_permission_request
    import capo_acm_pca.types.delete_policy_request
    import capo_acm_pca.types.describe_certificate_authority_audit_report_request
    import capo_acm_pca.types.describe_certificate_authority_audit_report_response
    import capo_acm_pca.types.describe_certificate_authority_request
    import capo_acm_pca.types.describe_certificate_authority_response
    import capo_acm_pca.types.get_certificate_authority_certificate_request
    import capo_acm_pca.types.get_certificate_authority_certificate_response
    import capo_acm_pca.types.get_certificate_authority_csr_request
    import capo_acm_pca.types.get_certificate_authority_csr_response
    import capo_acm_pca.types.get_certificate_request
    import capo_acm_pca.types.get_certificate_response
    import capo_acm_pca.types.get_policy_request
    import capo_acm_pca.types.get_policy_response
    import capo_acm_pca.types.idempotency_token
    import capo_acm_pca.types.import_certificate_authority_certificate_request
    import capo_acm_pca.types.issue_certificate_request
    import capo_acm_pca.types.issue_certificate_response
    import capo_acm_pca.types.key_storage_security_standard
    import capo_acm_pca.types.list_certificate_authorities_request
    import capo_acm_pca.types.list_certificate_authorities_response
    import capo_acm_pca.types.list_permissions_request
    import capo_acm_pca.types.list_permissions_response
    import capo_acm_pca.types.list_tags_request
    import capo_acm_pca.types.list_tags_response
    import capo_acm_pca.types.max_results
    import capo_acm_pca.types.next_token
    import capo_acm_pca.types.permanent_deletion_time_in_days
    import capo_acm_pca.types.permission
    import capo_acm_pca.types.principal
    import capo_acm_pca.types.put_policy_request
    import capo_acm_pca.types.resource_owner
    import capo_acm_pca.types.restore_certificate_authority_request
    import capo_acm_pca.types.revocation_configuration
    import capo_acm_pca.types.revocation_reason
    import capo_acm_pca.types.revoke_certificate_request
    import capo_acm_pca.types.s3_bucket_name
    import capo_acm_pca.types.signing_algorithm
    import capo_acm_pca.types.string128
    import capo_acm_pca.types.tag
    import capo_acm_pca.types.tag_certificate_authority_request
    import capo_acm_pca.types.tag_list
    import capo_acm_pca.types.untag_certificate_authority_request
    import capo_acm_pca.types.update_certificate_authority_request
    import capo_acm_pca.types.validity


class AsyncACMPCAClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncACMPCAClient:
    """A client for the ``ACMPCA`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AsyncACMPCAClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncACMPCAClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncACMPCAClientConfig = config_overrides or {}
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
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_certificate_authority(
        self,
        certificate_authority_configuration: "capo_acm_pca.types.certificate_authority_configuration.CertificateAuthorityConfiguration",
        certificate_authority_type: "capo_acm_pca.types.certificate_authority_type.CertificateAuthorityType",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        revocation_configuration: Optional[
            "capo_acm_pca.types.revocation_configuration.RevocationConfiguration"
        ] = None,
        idempotency_token: Optional[
            "capo_acm_pca.types.idempotency_token.IdempotencyToken"
        ] = None,
        key_storage_security_standard: Optional[
            "capo_acm_pca.types.key_storage_security_standard.KeyStorageSecurityStandard"
        ] = None,
        tags: Optional["capo_acm_pca.types.tag_list.TagList"] = None,
        usage_mode: Optional[
            "capo_acm_pca.types.certificate_authority_usage_mode.CertificateAuthorityUsageMode"
        ] = None,
    ) -> "capo_acm_pca.types.create_certificate_authority_response.CreateCertificateAuthorityResponse":
        """<p>Creates a root or subordinate private certificate authority (CA). You must specify the CA configuration, an optional configuration for Online Certificate Status Protocol (OCSP) and/or a certificate revocation list (CRL), the CA type, and an optional idempotency token to avoid accidental creation of multiple CAs. The CA configuration specifies the name of the algorithm and key size to be used to create the CA private key, the type of signing algorithm that the CA uses, and X.500 subject information. The OCSP configuration can optionally specify a custom URL for the OCSP responder. The CRL configuration specifies the CRL expiration period in days (the validity period of the CRL), the Amazon S3 bucket that will contain the CRL, and a CNAME alias for the S3 bucket that is included in certificates issued by the CA. If successful, this action returns the Amazon Resource Name (ARN) of the CA.</p> <note> <p>Both Amazon Web Services Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies">Access policies for CRLs in Amazon S3</a>.</p> </note> <p>Amazon Web Services Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#crl-encryption">Encrypting Your CRLs</a>.</p>

        Args:
            certificate_authority_configuration: <p>Name and bit size of the private key algorithm, the name of the signing algorithm, and X.500 certificate subject information.</p>
            revocation_configuration: <p>Contains information to enable support for Online Certificate Status Protocol (OCSP), certificate revocation list (CRL), both protocols, or neither. By default, both certificate validation mechanisms are disabled.</p> <p>The following requirements apply to revocation configurations.</p> <ul> <li> <p>A configuration disabling CRLs or OCSP must contain only the <code>Enabled=False</code> parameter, and will fail if other parameters such as <code>CustomCname</code> or <code>ExpirationInDays</code> are included.</p> </li> <li> <p>In a CRL configuration, the <code>S3BucketName</code> parameter must conform to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">Amazon S3 bucket naming rules</a>.</p> </li> <li> <p>A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to <a href="https://www.ietf.org/rfc/rfc2396.txt">RFC2396</a> restrictions on the use of special characters in a CNAME. </p> </li> <li> <p>In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".</p> </li> </ul> <p> For more information, see the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html">OcspConfiguration</a> and <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html">CrlConfiguration</a> types.</p>
            certificate_authority_type: <p>The type of the certificate authority.</p>
            idempotency_token: <p>Custom string that can be used to distinguish between calls to the <b>CreateCertificateAuthority</b> action. Idempotency tokens for <b>CreateCertificateAuthority</b> time out after five minutes. Therefore, if you call <b>CreateCertificateAuthority</b> multiple times with the same idempotency token within five minutes, Amazon Web Services Private CA recognizes that you are requesting only certificate authority and will issue only one. If you change the idempotency token for each call, Amazon Web Services Private CA recognizes that you are requesting multiple certificate authorities.</p>
            key_storage_security_standard: <p>Specifies a cryptographic key management compliance standard for handling and protecting CA keys.</p> <p>Default: FIPS_140_2_LEVEL_3_OR_HIGHER</p> <note> <p>Some Amazon Web Services Regions don't support the default value. When you create a CA in these Regions, you must use <code>CCPC_LEVEL_1_OR_HIGHER</code> for the <code>KeyStorageSecurityStandard</code> parameter. If you don't, the operation returns an <code>InvalidArgsException</code> with this message: "A certificate authority cannot be created in this region with the specified security standard."</p> <p>For information about security standard support in different Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys">Storage and security compliance of Amazon Web Services Private CA private keys</a>.</p> </note>
            tags: <p>Key-value pairs that will be attached to the new private CA. You can associate up to 50 tags with a private CA. For information using tags with IAM to manage permissions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html">Controlling Access Using IAM Tags</a>.</p>
            usage_mode: <p>Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days.</p> <p>The default value is GENERAL_PURPOSE.</p>

        Raises:
            capo_acm_pca.errors.invalid_args_exception.InvalidArgsException: <p>One or more of the specified arguments was not valid.</p>
            capo_acm_pca.errors.invalid_policy_exception.InvalidPolicyException: <p>The resource policy is invalid or is missing a required statement. For general information about IAM policy and statement structure, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json">Overview of JSON Policies</a>.</p>
            capo_acm_pca.errors.invalid_tag_exception.InvalidTagException: <p>The tag associated with the CA is not valid. The invalid argument is contained in the message field.</p>
            capo_acm_pca.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Web Services Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.create_certificate_authority_request.CreateCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.create_certificate_authority_response.CreateCertificateAuthorityResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.create_certificate_authority

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.create_certificate_authority.async_create_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.create_certificate_authority_request.CreateCertificateAuthorityRequest = {
            "certificate_authority_configuration": certificate_authority_configuration,
            "certificate_authority_type": certificate_authority_type,
        }
        if revocation_configuration is not None:
            input_["revocation_configuration"] = revocation_configuration
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if key_storage_security_standard is not None:
            input_["key_storage_security_standard"] = key_storage_security_standard
        if tags is not None:
            input_["tags"] = tags
        if usage_mode is not None:
            input_["usage_mode"] = usage_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_certificate_authority_audit_report(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        s3_bucket_name: "capo_acm_pca.types.s3_bucket_name.S3BucketName",
        audit_report_response_format: "capo_acm_pca.types.audit_report_response_format.AuditReportResponseFormat",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.create_certificate_authority_audit_report_response.CreateCertificateAuthorityAuditReportResponse":
        """<p>Creates an audit report that lists every time that your CA private key is used to issue a certificate. The <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html">IssueCertificate</a> and <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html">RevokeCertificate</a> actions use the private key.</p> <p>To save the audit report to your designated Amazon S3 bucket, you must create a bucket policy that grants Amazon Web Services Private CA permission to access and write to it. For an example policy, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html#s3-access">Prepare an Amazon S3 bucket for audit reports</a>.</p> <p>Amazon Web Services Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaAuditReport.html#audit-report-encryption">Encrypting Your Audit Reports</a>.</p> <note> <p>You can generate a maximum of one report every 30 minutes.</p> </note>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the CA to be audited. This is of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>.</p>
            s3_bucket_name: <p>The name of the S3 bucket that will contain the audit report.</p>
            audit_report_response_format: <p>The format in which to create the report. This can be either <b>JSON</b> or <b>CSV</b>.</p>

        Raises:
            capo_acm_pca.errors.invalid_args_exception.InvalidArgsException: <p>One or more of the specified arguments was not valid.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.request_in_progress_exception.RequestInProgressException: <p>Your request is already in progress.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.create_certificate_authority_audit_report_request.CreateCertificateAuthorityAuditReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.create_certificate_authority_audit_report_response.CreateCertificateAuthorityAuditReportResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.create_certificate_authority_audit_report

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.create_certificate_authority_audit_report.async_create_certificate_authority_audit_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.create_certificate_authority_audit_report_request.CreateCertificateAuthorityAuditReportRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "s3_bucket_name": s3_bucket_name,
            "audit_report_response_format": audit_report_response_format,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_permission(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        principal: "capo_acm_pca.types.principal.Principal",
        actions: "capo_acm_pca.types.action_list.ActionList",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        source_account: Optional["capo_acm_pca.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Grants one or more permissions on a private CA to the Certificate Manager (ACM) service principal (<code>acm.amazonaws.com</code>). These permissions allow ACM to issue and renew ACM certificates that reside in the same Amazon Web Services account as the CA.</p> <p>You can list current permissions with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html">ListPermissions</a> action and revoke them with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html">DeletePermission</a> action.</p> <p class="title"> <b>About Permissions</b> </p> <ul> <li> <p>If the private CA and the certificates it issues reside in the same account, you can use <code>CreatePermission</code> to grant permissions for ACM to carry out automatic certificate renewals.</p> </li> <li> <p>For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.</p> </li> <li> <p>If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html">Using a Resource Based Policy with Amazon Web Services Private CA</a>.</p> </li> </ul>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the CA that grants the permissions. You can find the ARN by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action. This must have the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>
            principal: <p>The Amazon Web Services service or identity that receives the permission. At this time, the only valid principal is <code>acm.amazonaws.com</code>.</p>
            source_account: <p>The ID of the calling account.</p>
            actions: <p>The actions that the specified Amazon Web Services service principal can use. These include <code>IssueCertificate</code>, <code>GetCertificate</code>, and <code>ListPermissions</code>.</p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Web Services Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.</p>
            capo_acm_pca.errors.permission_already_exists_exception.PermissionAlreadyExistsException: <p>The designated permission has already been given to the user.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.create_permission_request.CreatePermissionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.create_permission

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.create_permission.async_create_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.create_permission_request.CreatePermissionRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "principal": principal,
            "actions": actions,
        }
        if source_account is not None:
            input_["source_account"] = source_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_certificate_authority(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        permanent_deletion_time_in_days: Optional[
            "capo_acm_pca.types.permanent_deletion_time_in_days.PermanentDeletionTimeInDays"
        ] = None,
    ) -> None:
        """<p>Deletes a private certificate authority (CA). You must provide the Amazon Resource Name (ARN) of the private CA that you want to delete. You can find the ARN by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action. </p> <note> <p>Deleting a CA will invalidate other CAs and certificates below it in your CA hierarchy.</p> </note> <p>Before you can delete a CA that you have created and activated, you must disable it. To do this, call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html">UpdateCertificateAuthority</a> action and set the <b>CertificateAuthorityStatus</b> parameter to <code>DISABLED</code>. </p> <p>Additionally, you can delete a CA if you are waiting for it to be created (that is, the status of the CA is <code>CREATING</code>). You can also delete it if the CA has been created but you haven't yet imported the signed certificate into Amazon Web Services Private CA (that is, the status of the CA is <code>PENDING_CERTIFICATE</code>). </p> <p>When you successfully call <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html">DeleteCertificateAuthority</a>, the CA's status changes to <code>DELETED</code>. However, the CA won't be permanently deleted until the restoration period has passed. By default, if you do not set the <code>PermanentDeletionTimeInDays</code> parameter, the CA remains restorable for 30 days. You can set the parameter from 7 to 30 days. The <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html">DescribeCertificateAuthority</a> action returns the time remaining in the restoration window of a private CA in the <code>DELETED</code> state. To restore an eligible CA, call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_RestoreCertificateAuthority.html">RestoreCertificateAuthority</a> action.</p> <important> <p>A private CA can be deleted if it is in the <code>PENDING_CERTIFICATE</code>, <code>CREATING</code>, <code>EXPIRED</code>, <code>DISABLED</code>, or <code>FAILED</code> state. To delete a CA in the <code>ACTIVE</code> state, you must first disable it, or else the delete request results in an exception. If you are deleting a private CA in the <code>PENDING_CERTIFICATE</code> or <code>DISABLED</code> state, you can set the length of its restoration period to 7-30 days. The default is 30. During this time, the status is set to <code>DELETED</code> and the CA can be restored. A private CA deleted in the <code>CREATING</code> or <code>FAILED</code> state has no assigned restoration period and cannot be restored.</p> </important>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must have the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>
            permanent_deletion_time_in_days: <p>The number of days to make a CA restorable after it has been deleted. This can be anywhere from 7 to 30 days, with 30 being the default.</p>

        Raises:
            capo_acm_pca.errors.concurrent_modification_exception.ConcurrentModificationException: <p>A previous update to your private CA is still ongoing.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.delete_certificate_authority_request.DeleteCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.delete_certificate_authority

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.delete_certificate_authority.async_delete_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.delete_certificate_authority_request.DeleteCertificateAuthorityRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }
        if permanent_deletion_time_in_days is not None:
            input_["permanent_deletion_time_in_days"] = permanent_deletion_time_in_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_permission(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        principal: "capo_acm_pca.types.principal.Principal",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        source_account: Optional["capo_acm_pca.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Revokes permissions on a private CA granted to the Certificate Manager (ACM) service principal (acm.amazonaws.com). </p> <p>These permissions allow ACM to issue and renew ACM certificates that reside in the same Amazon Web Services account as the CA. If you revoke these permissions, ACM will no longer renew the affected certificates automatically.</p> <p>Permissions can be granted with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html">CreatePermission</a> action and listed with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html">ListPermissions</a> action. </p> <p class="title"> <b>About Permissions</b> </p> <ul> <li> <p>If the private CA and the certificates it issues reside in the same account, you can use <code>CreatePermission</code> to grant permissions for ACM to carry out automatic certificate renewals.</p> </li> <li> <p>For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.</p> </li> <li> <p>If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html">Using a Resource Based Policy with Amazon Web Services Private CA</a>.</p> </li> </ul>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Number (ARN) of the private CA that issued the permissions. You can find the CA's ARN by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action. This must have the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>
            principal: <p>The Amazon Web Services service or identity that will have its CA permissions revoked. At this time, the only valid service principal is <code>acm.amazonaws.com</code> </p>
            source_account: <p>The Amazon Web Services account that calls this action.</p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.delete_permission_request.DeletePermissionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.delete_permission

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.delete_permission.async_delete_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.delete_permission_request.DeletePermissionRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "principal": principal,
        }
        if source_account is not None:
            input_["source_account"] = source_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_policy(
        self,
        resource_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource-based policy attached to a private CA. Deletion will remove any access that the policy has granted. If there is no policy attached to the private CA, this action will return successful.</p> <p>If you delete a policy that was applied through Amazon Web Services Resource Access Manager (RAM), the CA will be removed from all shares in which it was included. </p> <p>The Certificate Manager Service Linked Role that the policy supports is not affected when you delete the policy. </p> <p>The current policy can be shown with <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html">GetPolicy</a> and updated with <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html">PutPolicy</a>.</p> <p class="title"> <b>About Policies</b> </p> <ul> <li> <p>A policy grants access on a private CA to an Amazon Web Services customer account, to Amazon Web Services Organizations, or to an Amazon Web Services Organizations unit. Policies are under the control of a CA administrator. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html">Using a Resource Based Policy with Amazon Web Services Private CA</a>.</p> </li> <li> <p>A policy permits a user of Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.</p> </li> <li> <p>For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the Amazon Web Services Private CA policy. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html">Using a Service Linked Role with ACM</a>.</p> </li> <li> <p>Updates made in Amazon Web Services Resource Manager (RAM) are reflected in policies. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html">Attach a Policy for Cross-Account Access</a>.</p> </li> </ul>

        Args:
            resource_arn: <p>The Amazon Resource Number (ARN) of the private CA that will have its policy deleted. You can find the CA's ARN by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action. The ARN value must have the form <code>arn:aws:acm-pca:region:account:certificate-authority/01234567-89ab-cdef-0123-0123456789ab</code>. </p>

        Raises:
            capo_acm_pca.errors.concurrent_modification_exception.ConcurrentModificationException: <p>A previous update to your private CA is still ongoing.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.lockout_prevented_exception.LockoutPreventedException: <p>The current action was prevented because it would lock the caller out from performing subsequent actions. Verify that the specified parameters would not result in the caller being denied access to the resource. </p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.delete_policy_request.DeletePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.delete_policy

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.delete_policy.async_delete_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.delete_policy_request.DeletePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_certificate_authority(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.describe_certificate_authority_response.DescribeCertificateAuthorityResponse":
        """<p>Lists information about your private certificate authority (CA) or one that has been shared with you. You specify the private CA on input by its ARN (Amazon Resource Name). The output contains the status of your CA. This can be any of the following: </p> <ul> <li> <p> <code>CREATING</code> - Amazon Web Services Private CA is creating your private certificate authority.</p> </li> <li> <p> <code>PENDING_CERTIFICATE</code> - The certificate is pending. You must use your Amazon Web Services Private CA-hosted or on-premises root or subordinate CA to sign your private CA CSR and then import it into Amazon Web Services Private CA. </p> </li> <li> <p> <code>ACTIVE</code> - Your private CA is active.</p> </li> <li> <p> <code>DISABLED</code> - Your private CA has been disabled.</p> </li> <li> <p> <code>EXPIRED</code> - Your private CA certificate has expired.</p> </li> <li> <p> <code>FAILED</code> - Your private CA has failed. Your CA can fail because of problems such a network outage or back-end Amazon Web Services failure or other errors. A failed CA can never return to the pending state. You must create a new CA. </p> </li> <li> <p> <code>DELETED</code> - Your private CA is within the restoration period, after which it is permanently deleted. The length of time remaining in the CA's restoration period is also included in this action's output.</p> </li> </ul>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.describe_certificate_authority_request.DescribeCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.describe_certificate_authority_response.DescribeCertificateAuthorityResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.describe_certificate_authority

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.describe_certificate_authority.async_describe_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.describe_certificate_authority_request.DescribeCertificateAuthorityRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_certificate_authority_audit_report(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        audit_report_id: "capo_acm_pca.types.audit_report_id.AuditReportId",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.describe_certificate_authority_audit_report_response.DescribeCertificateAuthorityAuditReportResponse":
        """<p>Lists information about a specific audit report created by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html">CreateCertificateAuthorityAuditReport</a> action. Audit information is created every time the certificate authority (CA) private key is used. The private key is used when you call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html">IssueCertificate</a> action or the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html">RevokeCertificate</a> action. </p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the private CA. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>
            audit_report_id: <p>The report ID returned by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html">CreateCertificateAuthorityAuditReport</a> action.</p>

        Raises:
            capo_acm_pca.errors.invalid_args_exception.InvalidArgsException: <p>One or more of the specified arguments was not valid.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.describe_certificate_authority_audit_report_request.DescribeCertificateAuthorityAuditReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.describe_certificate_authority_audit_report_response.DescribeCertificateAuthorityAuditReportResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.describe_certificate_authority_audit_report

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.describe_certificate_authority_audit_report.async_describe_certificate_authority_audit_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.describe_certificate_authority_audit_report_request.DescribeCertificateAuthorityAuditReportRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "audit_report_id": audit_report_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_certificate(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        certificate_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.get_certificate_response.GetCertificateResponse":
        """<p>Retrieves a certificate from your private CA or one that has been shared with you. The ARN of the certificate is returned when you call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html">IssueCertificate</a> action. You must specify both the ARN of your private CA and the ARN of the issued certificate when calling the <b>GetCertificate</b> action. You can retrieve the certificate if it is in the <b>ISSUED</b>, <b>EXPIRED</b>, or <b>REVOKED</b> state. You can call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html">CreateCertificateAuthorityAuditReport</a> action to create a report that contains information about all of the certificates issued and revoked by your private CA. </p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>
            certificate_arn: <p>The ARN of the issued certificate. The ARN contains the certificate serial number and must be in the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i>/certificate/<i>286535153982981100925020015808220737245</i> </code> </p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.request_in_progress_exception.RequestInProgressException: <p>Your request is already in progress.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.get_certificate_request.GetCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.get_certificate_response.GetCertificateResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.get_certificate

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.get_certificate.async_get_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.get_certificate_request.GetCertificateRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "certificate_arn": certificate_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_certificate_issued(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        certificate_arn: "capo_acm_pca.types.arn.Arn",
        *,
        max_wait_time: float,
        min_delay: float = 1,
        max_delay: float = 60,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.get_certificate_response.GetCertificateResponse":
        """Wait until a certificate is issued

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>
            certificate_arn: <p>The ARN of the issued certificate. The ARN contains the certificate serial number and must be in the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i>/certificate/<i>286535153982981100925020015808220737245</i> </code> </p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_acm_pca.types.get_certificate_response.GetCertificateResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.get_certificate(  # noqa: F841
                    certificate_authority_arn,
                    certificate_arn,
                    config_overrides=config_overrides,
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                return op_output
            elif op_error is not None and op_error.code == "RequestInProgressException":
                pass
            elif op_error is not None and op_error.code == "AccessDeniedException":
                raise WaiterFailedError(
                    "certificate_issued",
                    "errorType=AccessDeniedException (state=failure)",
                )
            elif op_error is not None:
                raise op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("certificate_issued", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = random.uniform(min_delay, delay)
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def get_certificate_authority_certificate(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.get_certificate_authority_certificate_response.GetCertificateAuthorityCertificateResponse":
        """<p>Retrieves the certificate and certificate chain for your private certificate authority (CA) or one that has been shared with you. Both the certificate and the chain are base64 PEM-encoded. The chain does not include the CA certificate. Each certificate in the chain signs the one before it. </p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of your private CA. This is of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.get_certificate_authority_certificate_request.GetCertificateAuthorityCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.get_certificate_authority_certificate_response.GetCertificateAuthorityCertificateResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.get_certificate_authority_certificate

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.get_certificate_authority_certificate.async_get_certificate_authority_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.get_certificate_authority_certificate_request.GetCertificateAuthorityCertificateRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_certificate_authority_csr(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.get_certificate_authority_csr_response.GetCertificateAuthorityCsrResponse":
        """<p>Retrieves the certificate signing request (CSR) for your private certificate authority (CA). The CSR is created when you call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action. Sign the CSR with your Amazon Web Services Private CA-hosted or on-premises root or subordinate CA. Then import the signed certificate back into Amazon Web Services Private CA by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html">ImportCertificateAuthorityCertificate</a> action. The CSR is returned as a base64 PEM-encoded string. </p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.request_in_progress_exception.RequestInProgressException: <p>Your request is already in progress.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.get_certificate_authority_csr_request.GetCertificateAuthorityCsrRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.get_certificate_authority_csr_response.GetCertificateAuthorityCsrResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.get_certificate_authority_csr

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.get_certificate_authority_csr.async_get_certificate_authority_csr(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.get_certificate_authority_csr_request.GetCertificateAuthorityCsrRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_certificate_authority_csr_created(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 180,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.get_certificate_authority_csr_response.GetCertificateAuthorityCsrResponse":
        """Wait until a Certificate Authority CSR is created

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_acm_pca.types.get_certificate_authority_csr_response.GetCertificateAuthorityCsrResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.get_certificate_authority_csr(  # noqa: F841
                    certificate_authority_arn, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                return op_output
            elif op_error is not None and op_error.code == "RequestInProgressException":
                pass
            elif op_error is not None and op_error.code == "AccessDeniedException":
                raise WaiterFailedError(
                    "certificate_authority_csr_created",
                    "errorType=AccessDeniedException (state=failure)",
                )
            elif op_error is not None:
                raise op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError(
                    "certificate_authority_csr_created", max_wait_time
                )
            delay = min(max_delay, min_delay * (2**attempt))
            delay = random.uniform(min_delay, delay)
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def get_policy(
        self,
        resource_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> "capo_acm_pca.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves the resource-based policy attached to a private CA. If either the private CA resource or the policy cannot be found, this action returns a <code>ResourceNotFoundException</code>. </p> <p>The policy can be attached or updated with <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html">PutPolicy</a> and removed with <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html">DeletePolicy</a>.</p> <p class="title"> <b>About Policies</b> </p> <ul> <li> <p>A policy grants access on a private CA to an Amazon Web Services customer account, to Amazon Web Services Organizations, or to an Amazon Web Services Organizations unit. Policies are under the control of a CA administrator. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html">Using a Resource Based Policy with Amazon Web Services Private CA</a>.</p> </li> <li> <p>A policy permits a user of Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.</p> </li> <li> <p>For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the Amazon Web Services Private CA policy. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html">Using a Service Linked Role with ACM</a>.</p> </li> <li> <p>Updates made in Amazon Web Services Resource Manager (RAM) are reflected in policies. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html">Attach a Policy for Cross-Account Access</a>.</p> </li> </ul>

        Args:
            resource_arn: <p>The Amazon Resource Number (ARN) of the private CA that will have its policy retrieved. You can find the CA's ARN by calling the ListCertificateAuthorities action. </p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.get_policy_request.GetPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.get_policy

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.get_policy.async_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.get_policy_request.GetPolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_certificate_authority_certificate(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        certificate: "capo_acm_pca.types.certificate_body_blob.CertificateBodyBlob",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        certificate_chain: Optional[
            "capo_acm_pca.types.certificate_chain_blob.CertificateChainBlob"
        ] = None,
    ) -> None:
        """<p>Imports a signed private CA certificate into Amazon Web Services Private CA. This action is used when you are using a chain of trust whose root is located outside Amazon Web Services Private CA. Before you can call this action, the following preparations must in place:</p> <ol> <li> <p>In Amazon Web Services Private CA, call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action to create the private CA that you plan to back with the imported certificate.</p> </li> <li> <p>Call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html">GetCertificateAuthorityCsr</a> action to generate a certificate signing request (CSR).</p> </li> <li> <p>Sign the CSR using a root or intermediate CA hosted by either an on-premises PKI hierarchy or by a commercial CA.</p> </li> <li> <p>Create a certificate chain and copy the signed certificate and the certificate chain to your working directory.</p> </li> </ol> <p>Amazon Web Services Private CA supports three scenarios for installing a CA certificate:</p> <ul> <li> <p>Installing a certificate for a root CA hosted by Amazon Web Services Private CA.</p> </li> <li> <p>Installing a subordinate CA certificate whose parent authority is hosted by Amazon Web Services Private CA.</p> </li> <li> <p>Installing a subordinate CA certificate whose parent authority is externally hosted.</p> </li> </ul> <p>The following additional requirements apply when you import a CA certificate.</p> <ul> <li> <p>Only a self-signed certificate can be imported as a root CA.</p> </li> <li> <p>A self-signed certificate cannot be imported as a subordinate CA.</p> </li> <li> <p>Your certificate chain must not include the private CA certificate that you are importing.</p> </li> <li> <p>Your root CA must be the last certificate in your chain. The subordinate certificate, if any, that your root CA signed must be next to last. The subordinate certificate signed by the preceding subordinate CA must come next, and so on until your chain is built. </p> </li> <li> <p>The chain must be PEM-encoded.</p> </li> <li> <p>The maximum allowed size of a certificate is 32 KB.</p> </li> <li> <p>The maximum allowed size of a certificate chain is 2 MB.</p> </li> </ul> <p> <i>Enforcement of Critical Constraints</i> </p> <p>Amazon Web Services Private CA allows the following extensions to be marked critical in the imported CA certificate or chain.</p> <ul> <li> <p>Authority key identifier</p> </li> <li> <p>Basic constraints (<i>must</i> be marked critical)</p> </li> <li> <p>Certificate policies</p> </li> <li> <p>Extended key usage</p> </li> <li> <p>Inhibit anyPolicy</p> </li> <li> <p>Issuer alternative name</p> </li> <li> <p>Key usage</p> </li> <li> <p>Name constraints</p> </li> <li> <p>Policy mappings</p> </li> <li> <p>Subject alternative name</p> </li> <li> <p>Subject directory attributes</p> </li> <li> <p>Subject key identifier</p> </li> <li> <p>Subject information access</p> </li> </ul> <p>Amazon Web Services Private CA rejects the following extensions when they are marked critical in an imported CA certificate or chain.</p> <ul> <li> <p>Authority information access</p> </li> <li> <p>CRL distribution points</p> </li> <li> <p>Freshest CRL</p> </li> <li> <p>Policy constraints</p> </li> </ul> <p>Amazon Web Services Private Certificate Authority will also reject any other extension marked as critical not contained on the preceding list of allowed extensions.</p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            certificate: <p>The PEM-encoded certificate for a private CA. This may be a self-signed certificate in the case of a root CA, or it may be signed by another CA that you control.</p>
            certificate_chain: <p>A PEM-encoded file that contains all of your certificates, other than the certificate you're importing, chaining up to your root CA. Your Amazon Web Services Private CA-hosted or on-premises root certificate is the last in the chain, and each certificate in the chain signs the one preceding. </p> <p>This parameter must be supplied when you import a subordinate CA. When you import a root CA, there is no chain.</p>

        Raises:
            capo_acm_pca.errors.certificate_mismatch_exception.CertificateMismatchException: <p>The certificate authority certificate you are importing does not comply with conditions specified in the certificate that signed it.</p>
            capo_acm_pca.errors.concurrent_modification_exception.ConcurrentModificationException: <p>A previous update to your private CA is still ongoing.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_request_exception.InvalidRequestException: <p>The request action cannot be performed or is prohibited.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.malformed_certificate_exception.MalformedCertificateException: <p>One or more fields in the certificate are invalid.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.request_in_progress_exception.RequestInProgressException: <p>Your request is already in progress.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.import_certificate_authority_certificate_request.ImportCertificateAuthorityCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.import_certificate_authority_certificate

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.import_certificate_authority_certificate.async_import_certificate_authority_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.import_certificate_authority_certificate_request.ImportCertificateAuthorityCertificateRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "certificate": certificate,
        }
        if certificate_chain is not None:
            input_["certificate_chain"] = certificate_chain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def issue_certificate(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        csr: "capo_acm_pca.types.csr_blob.CsrBlob",
        signing_algorithm: "capo_acm_pca.types.signing_algorithm.SigningAlgorithm",
        validity: "capo_acm_pca.types.validity.Validity",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        api_passthrough: Optional[
            "capo_acm_pca.types.api_passthrough.ApiPassthrough"
        ] = None,
        template_arn: Optional["capo_acm_pca.types.arn.Arn"] = None,
        validity_not_before: Optional["capo_acm_pca.types.validity.Validity"] = None,
        idempotency_token: Optional[
            "capo_acm_pca.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_acm_pca.types.issue_certificate_response.IssueCertificateResponse":
        """<p>Uses your private certificate authority (CA), or one that has been shared with you, to issue a client certificate. This action returns the Amazon Resource Name (ARN) of the certificate. You can retrieve the certificate by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html">GetCertificate</a> action and specifying the ARN. </p> <note> <p>You cannot use the ACM <b>ListCertificateAuthorities</b> action to retrieve the ARNs of the certificates that you issue by using Amazon Web Services Private CA.</p> </note>

        Args:
            api_passthrough: <p>Specifies X.509 certificate information to be included in the issued certificate. An <code>APIPassthrough</code> or <code>APICSRPassthrough</code> template variant must be selected, or else this parameter is ignored. For more information about using these templates, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html">Understanding Certificate Templates</a>.</p> <p>If conflicting or duplicate certificate information is supplied during certificate issuance, Amazon Web Services Private CA applies <a href="https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations">order of operation rules</a> to determine what information is used.</p>
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            csr: <p>The certificate signing request (CSR) for the certificate you want to issue. As an example, you can use the following OpenSSL command to create the CSR and a 2048 bit RSA private key. </p> <p> <code>openssl req -new -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr</code> </p> <p>If you have a configuration file, you can then use the following OpenSSL command. The <code>usr_cert</code> block in the configuration file contains your X509 version 3 extensions. </p> <p> <code>openssl req -new -config openssl_rsa.cnf -extensions usr_cert -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr</code> </p> <p>Note: A CSR must provide either a <i>subject name</i> or a <i>subject alternative name</i> or the request will be rejected. </p>
            signing_algorithm: <p>The name of the algorithm that will be used to sign the certificate to be issued. </p> <p>This parameter should not be confused with the <code>SigningAlgorithm</code> parameter used to sign a CSR in the <code>CreateCertificateAuthority</code> action.</p> <note> <p>The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</p> </note>
            template_arn: <p>Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, Amazon Web Services Private CA defaults to the <code>EndEntityCertificate/V1</code> template. For CA certificates, you should choose the shortest path length that meets your needs. The path length is indicated by the PathLen<i>N</i> portion of the ARN, where <i>N</i> is the <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaTerms.html#terms-cadepth">CA depth</a>.</p> <p>Note: The CA depth configured on a subordinate CA certificate must not exceed the limit set by its parents in the CA hierarchy.</p> <p>For a list of <code>TemplateArn</code> values supported by Amazon Web Services Private CA, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html">Understanding Certificate Templates</a>.</p>
            validity: <p>Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate.</p> <p>Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see <a href="https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5">Validity</a> in RFC 5280. </p> <p>This value is unaffected when <code>ValidityNotBefore</code> is also specified. For example, if <code>Validity</code> is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the <code>ValidityNotBefore</code> value.</p> <p>The end of the validity period configured on a certificate must not exceed the limit set on its parents in the CA hierarchy.</p>
            validity_not_before: <p>Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate.</p> <p>By default, when issuing a certificate, Amazon Web Services Private CA sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The <code>ValidityNotBefore</code> parameter can be used to customize the “Not Before” value. </p> <p>Unlike the <code>Validity</code> parameter, the <code>ValidityNotBefore</code> parameter is optional.</p> <p>The <code>ValidityNotBefore</code> value is expressed as an explicit date and time, using the <code>Validity</code> type value <code>ABSOLUTE</code>. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_Validity.html">Validity</a> in this API reference and <a href="https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5">Validity</a> in RFC 5280.</p>
            idempotency_token: <p>Alphanumeric string that can be used to distinguish between calls to the <b>IssueCertificate</b> action. Idempotency tokens for <b>IssueCertificate</b> time out after five minutes. Therefore, if you call <b>IssueCertificate</b> multiple times with the same idempotency token within five minutes, Amazon Web Services Private CA recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, Amazon Web Services Private CA recognizes that you are requesting multiple certificates.</p>

        Raises:
            capo_acm_pca.errors.invalid_args_exception.InvalidArgsException: <p>One or more of the specified arguments was not valid.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Web Services Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.</p>
            capo_acm_pca.errors.malformed_csr_exception.MalformedCSRException: <p>The certificate signing request is invalid.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.issue_certificate_request.IssueCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.issue_certificate_response.IssueCertificateResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.issue_certificate

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.issue_certificate.async_issue_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.issue_certificate_request.IssueCertificateRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "csr": csr,
            "signing_algorithm": signing_algorithm,
            "validity": validity,
        }
        if api_passthrough is not None:
            input_["api_passthrough"] = api_passthrough
        if template_arn is not None:
            input_["template_arn"] = template_arn
        if validity_not_before is not None:
            input_["validity_not_before"] = validity_not_before
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_certificate_authorities(
        self,
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        max_results: Optional["capo_acm_pca.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_acm_pca.types.next_token.NextToken"] = None,
        resource_owner: Optional[
            "capo_acm_pca.types.resource_owner.ResourceOwner"
        ] = None,
    ) -> "capo_acm_pca.types.list_certificate_authorities_response.ListCertificateAuthoritiesResponse":
        """<p>Lists the private certificate authorities that you created by using the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p> <p>Although the maximum value is 1000, the action only returns a maximum of 100 items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            resource_owner: <p>Use this parameter to filter the returned set of certificate authorities based on their owner. The default is SELF.</p>

        Raises:
            capo_acm_pca.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token specified in the <code>NextToken</code> argument is not valid. Use the token returned from your previous call to <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a>.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.list_certificate_authorities_request.ListCertificateAuthoritiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.list_certificate_authorities_response.ListCertificateAuthoritiesResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.list_certificate_authorities

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.list_certificate_authorities.async_list_certificate_authorities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.list_certificate_authorities_request.ListCertificateAuthoritiesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_certificate_authorities(
        self,
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        max_results: Optional["capo_acm_pca.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_acm_pca.types.next_token.NextToken"] = None,
        resource_owner: Optional[
            "capo_acm_pca.types.resource_owner.ResourceOwner"
        ] = None,
    ) -> "AsyncIterator[capo_acm_pca.types.certificate_authority.CertificateAuthority]":
        _token = next_token
        while True:
            _response = await self.list_certificate_authorities(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_owner=resource_owner,
            )
            _page = _resolve_path(_response, ("certificate_authorities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_permissions(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        max_results: Optional["capo_acm_pca.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_acm_pca.types.next_token.NextToken"] = None,
    ) -> "capo_acm_pca.types.list_permissions_response.ListPermissionsResponse":
        """<p>List all permissions on a private CA, if any, granted to the Certificate Manager (ACM) service principal (acm.amazonaws.com). </p> <p>These permissions allow ACM to issue and renew ACM certificates that reside in the same Amazon Web Services account as the CA. </p> <p>Permissions can be granted with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html">CreatePermission</a> action and revoked with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html">DeletePermission</a> action.</p> <p class="title"> <b>About Permissions</b> </p> <ul> <li> <p>If the private CA and the certificates it issues reside in the same account, you can use <code>CreatePermission</code> to grant permissions for ACM to carry out automatic certificate renewals.</p> </li> <li> <p>For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list certificates.</p> </li> <li> <p>If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html">Using a Resource Based Policy with Amazon Web Services Private CA</a>.</p> </li> </ul>

        Args:
            max_results: <p>When paginating results, use this parameter to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the <b>NextToken</b> element is sent in the response. Use this <b>NextToken</b> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>When paginating results, use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <b>NextToken</b> from the response you just received.</p>
            certificate_authority_arn: <p>The Amazon Resource Number (ARN) of the private CA to inspect. You can find the ARN by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action. This must be of the form: <code>arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012</code> You can get a private CA's ARN by running the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action.</p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token specified in the <code>NextToken</code> argument is not valid. Use the token returned from your previous call to <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a>.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.list_permissions_request.ListPermissionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.list_permissions

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.list_permissions.async_list_permissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.list_permissions_request.ListPermissionsRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_permissions(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        max_results: Optional["capo_acm_pca.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_acm_pca.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_acm_pca.types.permission.Permission]":
        _token = next_token
        while True:
            _response = await self.list_permissions(
                certificate_authority_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("permissions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        max_results: Optional["capo_acm_pca.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_acm_pca.types.next_token.NextToken"] = None,
    ) -> "capo_acm_pca.types.list_tags_response.ListTagsResponse":
        """<p>Lists the tags, if any, that are associated with your private CA or one that has been shared with you. Tags are labels that you can use to identify and organize your CAs. Each tag consists of a key and an optional value. Call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html">TagCertificateAuthority</a> action to add one or more tags to your CA. Call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html">UntagCertificateAuthority</a> action to remove tags. </p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the <b>NextToken</b> element is sent in the response. Use this <b>NextToken</b> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of <b>NextToken</b> from the response you just received.</p>
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm_pca.types.list_tags_response.ListTagsResponse"
        ]:
            import capo_acm_pca._operations.acm_private_ca.list_tags

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.list_tags_request.ListTagsRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tags(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        max_results: Optional["capo_acm_pca.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_acm_pca.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_acm_pca.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags(
                certificate_authority_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_policy(
        self,
        resource_arn: "capo_acm_pca.types.arn.Arn",
        policy: "capo_acm_pca.types.aws_policy.AWSPolicy",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> None:
        """<p>Attaches a resource-based policy to a private CA. </p> <p>A policy can also be applied by sharing a private CA through Amazon Web Services Resource Access Manager (RAM). For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html">Attach a Policy for Cross-Account Access</a>.</p> <p>The policy can be displayed with <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html">GetPolicy</a> and removed with <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html">DeletePolicy</a>.</p> <p class="title"> <b>About Policies</b> </p> <ul> <li> <p>A policy grants access on a private CA to an Amazon Web Services customer account, to Amazon Web Services Organizations, or to an Amazon Web Services Organizations unit. Policies are under the control of a CA administrator. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html">Using a Resource Based Policy with Amazon Web Services Private CA</a>.</p> </li> <li> <p>A policy permits a user of Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.</p> </li> <li> <p>For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the Amazon Web Services Private CA policy. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html">Using a Service Linked Role with ACM</a>.</p> </li> <li> <p>Updates made in Amazon Web Services Resource Manager (RAM) are reflected in policies. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html">Attach a Policy for Cross-Account Access</a>.</p> </li> </ul>

        Args:
            resource_arn: <p>The Amazon Resource Number (ARN) of the private CA to associate with the policy. The ARN of the CA can be found by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action.</p> <p/>
            policy: <p>The path and file name of a JSON-formatted IAM policy to attach to the specified private CA resource. If this policy does not contain all required statements or if it includes any statement that is not allowed, the <code>PutPolicy</code> action returns an <code>InvalidPolicyException</code>. For information about IAM policy and statement structure, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json">Overview of JSON Policies</a>.</p>

        Raises:
            capo_acm_pca.errors.concurrent_modification_exception.ConcurrentModificationException: <p>A previous update to your private CA is still ongoing.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_policy_exception.InvalidPolicyException: <p>The resource policy is invalid or is missing a required statement. For general information about IAM policy and statement structure, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json">Overview of JSON Policies</a>.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.lockout_prevented_exception.LockoutPreventedException: <p>The current action was prevented because it would lock the caller out from performing subsequent actions. Verify that the specified parameters would not result in the caller being denied access to the resource. </p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.put_policy_request.PutPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.put_policy

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.put_policy.async_put_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.put_policy_request.PutPolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_certificate_authority(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> None:
        """<p>Restores a certificate authority (CA) that is in the <code>DELETED</code> state. You can restore a CA during the period that you defined in the <b>PermanentDeletionTimeInDays</b> parameter of the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeleteCertificateAuthority.html">DeleteCertificateAuthority</a> action. Currently, you can specify 7 to 30 days. If you did not specify a <b>PermanentDeletionTimeInDays</b> value, by default you can restore the CA at any time in a 30 day period. You can check the time remaining in the restoration period of a private CA in the <code>DELETED</code> state by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html">DescribeCertificateAuthority</a> or <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> actions. The status of a restored CA is set to its pre-deletion status when the <b>RestoreCertificateAuthority</b> action returns. To change its status to <code>ACTIVE</code>, call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html">UpdateCertificateAuthority</a> action. If the private CA was in the <code>PENDING_CERTIFICATE</code> state at deletion, you must use the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html">ImportCertificateAuthorityCertificate</a> action to import a certificate authority into the private CA before it can be activated. You cannot restore a CA after the restoration period has ended.</p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.restore_certificate_authority_request.RestoreCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.restore_certificate_authority

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.restore_certificate_authority.async_restore_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.restore_certificate_authority_request.RestoreCertificateAuthorityRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_certificate(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        certificate_serial: "capo_acm_pca.types.string128.String128",
        revocation_reason: "capo_acm_pca.types.revocation_reason.RevocationReason",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> None:
        """<p>Revokes a certificate that was issued inside Amazon Web Services Private CA. If you enable a certificate revocation list (CRL) when you create or update your private CA, information about the revoked certificates will be included in the CRL. Amazon Web Services Private CA writes the CRL to an S3 bucket that you specify. A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason the CRL update fails, Amazon Web Services Private CA attempts makes further attempts every 15 minutes. With Amazon CloudWatch, you can create alarms for the metrics <code>CRLGenerated</code> and <code>MisconfiguredCRLBucket</code>. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaCloudWatch.html">Supported CloudWatch Metrics</a>.</p> <note> <p>Both Amazon Web Services Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies">Access policies for CRLs in Amazon S3</a>.</p> </note> <p>Amazon Web Services Private CA also writes revocation information to the audit report. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthorityAuditReport.html">CreateCertificateAuthorityAuditReport</a>.</p> <note> <p>You cannot revoke a root CA self-signed certificate.</p> </note>

        Args:
            certificate_authority_arn: <p>Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            certificate_serial: <p>Serial number of the certificate to be revoked. This must be in hexadecimal format. You can retrieve the serial number by calling <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html">GetCertificate</a> with the Amazon Resource Name (ARN) of the certificate you want and the ARN of your private CA. The <b>GetCertificate</b> action retrieves the certificate in the PEM format. You can use the following OpenSSL command to list the certificate in text format and copy the hexadecimal serial number. </p> <p> <code>openssl x509 -in <i>file_path</i> -text -noout</code> </p> <p>You can also copy the serial number from the console or use the <a href="https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html">DescribeCertificate</a> action in the <i>Certificate Manager API Reference</i>. </p>
            revocation_reason: <p>Specifies why you revoked the certificate.</p>

        Raises:
            capo_acm_pca.errors.concurrent_modification_exception.ConcurrentModificationException: <p>A previous update to your private CA is still ongoing.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_request_exception.InvalidRequestException: <p>The request action cannot be performed or is prohibited.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.limit_exceeded_exception.LimitExceededException: <p>An Amazon Web Services Private CA quota has been exceeded. See the exception message returned to determine the quota that was exceeded.</p>
            capo_acm_pca.errors.request_already_processed_exception.RequestAlreadyProcessedException: <p>Your request has already been completed.</p>
            capo_acm_pca.errors.request_failed_exception.RequestFailedException: <p>The request has failed for an unspecified reason.</p>
            capo_acm_pca.errors.request_in_progress_exception.RequestInProgressException: <p>Your request is already in progress.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.revoke_certificate_request.RevokeCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.revoke_certificate

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.revoke_certificate.async_revoke_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.revoke_certificate_request.RevokeCertificateRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "certificate_serial": certificate_serial,
            "revocation_reason": revocation_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_certificate_authority(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        tags: "capo_acm_pca.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> None:
        """<p>Adds one or more tags to your private CA. Tags are labels that you can use to identify and organize your Amazon Web Services resources. Each tag consists of a key and an optional value. You specify the private CA on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. You can apply a tag to just one private CA if you want to identify a specific characteristic of that CA, or you can apply the same tag to multiple private CAs if you want to filter for a common relationship among those CAs. To remove one or more tags, use the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UntagCertificateAuthority.html">UntagCertificateAuthority</a> action. Call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html">ListTags</a> action to see what tags are associated with your CA. </p> <note> <p>To attach tags to a private CA during the creation procedure, a CA administrator must first associate an inline IAM policy with the <code>CreateCertificateAuthority</code> action and explicitly allow tagging. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/auth-InlinePolicies.html#policy-tag-ca">Attaching tags to a CA at the time of creation</a>.</p> </note>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            tags: <p>List of tags to be associated with the CA.</p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.invalid_tag_exception.InvalidTagException: <p>The tag associated with the CA is not valid. The invalid argument is contained in the message field.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.too_many_tags_exception.TooManyTagsException: <p>You can associate up to 50 tags with a private CA. Exception information is contained in the exception message field.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.tag_certificate_authority_request.TagCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.tag_certificate_authority

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.tag_certificate_authority.async_tag_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.tag_certificate_authority_request.TagCertificateAuthorityRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_certificate_authority(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        tags: "capo_acm_pca.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
    ) -> None:
        """<p>Remove one or more tags from your private CA. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this action, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value. To add tags to a private CA, use the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html">TagCertificateAuthority</a>. Call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html">ListTags</a> action to see what tags are associated with your CA. </p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a>. This must be of the form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            tags: <p>List of tags to be removed from the CA.</p>

        Raises:
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.invalid_tag_exception.InvalidTagException: <p>The tag associated with the CA is not valid. The invalid argument is contained in the message field.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.untag_certificate_authority_request.UntagCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.untag_certificate_authority

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.untag_certificate_authority.async_untag_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.untag_certificate_authority_request.UntagCertificateAuthorityRequest = {
            "certificate_authority_arn": certificate_authority_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_certificate_authority(
        self,
        certificate_authority_arn: "capo_acm_pca.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMPCAClientConfig] = None,
        revocation_configuration: Optional[
            "capo_acm_pca.types.revocation_configuration.RevocationConfiguration"
        ] = None,
        status: Optional[
            "capo_acm_pca.types.certificate_authority_status.CertificateAuthorityStatus"
        ] = None,
    ) -> None:
        """<p>Updates the status or configuration of a private certificate authority (CA). Your private CA must be in the <code>ACTIVE</code> or <code>DISABLED</code> state before you can update it. You can disable a private CA that is in the <code>ACTIVE</code> state or make a CA that is in the <code>DISABLED</code> state active again.</p> <note> <p>Both Amazon Web Services Private CA and the IAM principal must have permission to write to the S3 bucket that you specify. If the IAM principal making the call does not have permission to write to the bucket, then an exception is thrown. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html#s3-policies">Access policies for CRLs in Amazon S3</a>.</p> </note>

        Args:
            certificate_authority_arn: <p>Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            revocation_configuration: <p>Contains information to enable support for Online Certificate Status Protocol (OCSP), certificate revocation list (CRL), both protocols, or neither. If you don't supply this parameter, existing capibilites remain unchanged. For more information, see the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_OcspConfiguration.html">OcspConfiguration</a> and <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html">CrlConfiguration</a> types.</p> <p>The following requirements apply to revocation configurations.</p> <ul> <li> <p>A configuration disabling CRLs or OCSP must contain only the <code>Enabled=False</code> parameter, and will fail if other parameters such as <code>CustomCname</code> or <code>ExpirationInDays</code> are included.</p> </li> <li> <p>In a CRL configuration, the <code>S3BucketName</code> parameter must conform to <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">Amazon S3 bucket naming rules</a>.</p> </li> <li> <p>A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to <a href="https://www.ietf.org/rfc/rfc2396.txt">RFC2396</a> restrictions on the use of special characters in a CNAME. </p> </li> <li> <p>In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".</p> </li> </ul> <important> <p> If you update the <code>S3BucketName</code> of <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html">CrlConfiguration</a>, you can break revocation for existing certificates. In other words, if you call <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html">UpdateCertificateAuthority</a> to update the CRL configuration's S3 bucket name, Amazon Web Services Private CA only writes CRLs to the new S3 bucket. Certificates issued prior to this point will have the old S3 bucket name in your CRL Distribution Point (CDP) extension, essentially breaking revocation. If you must update the S3 bucket, you'll need to reissue old certificates to keep the revocation working. Alternatively, you can use a <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CrlConfiguration.html#privateca-Type-CrlConfiguration-CustomCname">CustomCname</a> in your CRL configuration if you might need to change the S3 bucket name in the future.</p> </important>
            status: <p>Status of your private CA.</p>

        Raises:
            capo_acm_pca.errors.concurrent_modification_exception.ConcurrentModificationException: <p>A previous update to your private CA is still ongoing.</p>
            capo_acm_pca.errors.invalid_args_exception.InvalidArgsException: <p>One or more of the specified arguments was not valid.</p>
            capo_acm_pca.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm_pca.errors.invalid_policy_exception.InvalidPolicyException: <p>The resource policy is invalid or is missing a required statement. For general information about IAM policy and statement structure, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json">Overview of JSON Policies</a>.</p>
            capo_acm_pca.errors.invalid_state_exception.InvalidStateException: <p>The state of the private CA does not allow this action to occur.</p>
            capo_acm_pca.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.</p>
            capo_acm_pca.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm_pca.types.update_certificate_authority_request.UpdateCertificateAuthorityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm_pca._operations.acm_private_ca.update_certificate_authority

            (
                output,
                http_response,
            ) = await capo_acm_pca._operations.acm_private_ca.update_certificate_authority.async_update_certificate_authority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm_pca.types.update_certificate_authority_request.UpdateCertificateAuthorityRequest = {
            "certificate_authority_arn": certificate_authority_arn
        }
        if revocation_configuration is not None:
            input_["revocation_configuration"] = revocation_configuration
        if status is not None:
            input_["status"] = status

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
