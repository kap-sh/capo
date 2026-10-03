"""Generated from Smithy shape ``com.amazonaws.acm#CertificateManager``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_acm._auth._signers
import capo_acm._auth._sigv4
from capo_acm._auth._identity import Credentials
from capo_acm._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_acm._auth._zapros_handler import AuthMiddleware
from capo_acm._pagination import resolve_path as _resolve_path
from capo_acm._services._aws_config import aaws_config
from capo_acm._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_acm.types.acme_account_summary
    import capo_acm.types.acme_authorization_behavior
    import capo_acm.types.acme_contact
    import capo_acm.types.acme_domain_validation_arn
    import capo_acm.types.acme_domain_validation_summary
    import capo_acm.types.acme_endpoint_arn
    import capo_acm.types.acme_endpoint_summary
    import capo_acm.types.acme_external_account_binding_arn
    import capo_acm.types.acme_external_account_binding_summary
    import capo_acm.types.add_tags_to_certificate_request
    import capo_acm.types.arn
    import capo_acm.types.certificate_arn
    import capo_acm.types.certificate_authority
    import capo_acm.types.certificate_body_blob
    import capo_acm.types.certificate_chain_blob
    import capo_acm.types.certificate_filter_statement
    import capo_acm.types.certificate_key_pair_origins
    import capo_acm.types.certificate_managed_by
    import capo_acm.types.certificate_options
    import capo_acm.types.certificate_search_result
    import capo_acm.types.certificate_statuses
    import capo_acm.types.certificate_summary
    import capo_acm.types.create_acme_domain_validation_request
    import capo_acm.types.create_acme_domain_validation_response
    import capo_acm.types.create_acme_endpoint_request
    import capo_acm.types.create_acme_endpoint_response
    import capo_acm.types.create_acme_external_account_binding_request
    import capo_acm.types.create_acme_external_account_binding_response
    import capo_acm.types.delete_acme_domain_validation_request
    import capo_acm.types.delete_acme_endpoint_request
    import capo_acm.types.delete_acme_external_account_binding_request
    import capo_acm.types.delete_certificate_request
    import capo_acm.types.describe_acme_account_request
    import capo_acm.types.describe_acme_account_response
    import capo_acm.types.describe_acme_domain_validation_request
    import capo_acm.types.describe_acme_domain_validation_response
    import capo_acm.types.describe_acme_endpoint_request
    import capo_acm.types.describe_acme_endpoint_response
    import capo_acm.types.describe_acme_external_account_binding_request
    import capo_acm.types.describe_acme_external_account_binding_response
    import capo_acm.types.describe_certificate_request
    import capo_acm.types.describe_certificate_response
    import capo_acm.types.domain_list
    import capo_acm.types.domain_name
    import capo_acm.types.domain_name_string
    import capo_acm.types.domain_validation_option_list
    import capo_acm.types.domain_validation_summary
    import capo_acm.types.expiration
    import capo_acm.types.expiry_events_configuration
    import capo_acm.types.export_certificate_request
    import capo_acm.types.export_certificate_response
    import capo_acm.types.filters
    import capo_acm.types.get_account_configuration_response
    import capo_acm.types.get_acme_external_account_binding_credentials_request
    import capo_acm.types.get_acme_external_account_binding_credentials_response
    import capo_acm.types.get_certificate_request
    import capo_acm.types.get_certificate_response
    import capo_acm.types.idempotency_token
    import capo_acm.types.import_certificate_request
    import capo_acm.types.import_certificate_response
    import capo_acm.types.key_algorithm
    import capo_acm.types.list_acme_accounts_request
    import capo_acm.types.list_acme_accounts_response
    import capo_acm.types.list_acme_domain_validations_request
    import capo_acm.types.list_acme_domain_validations_response
    import capo_acm.types.list_acme_endpoints_request
    import capo_acm.types.list_acme_endpoints_response
    import capo_acm.types.list_acme_external_account_bindings_request
    import capo_acm.types.list_acme_external_account_bindings_response
    import capo_acm.types.list_certificate_domain_validations_request
    import capo_acm.types.list_certificate_domain_validations_response
    import capo_acm.types.list_certificates_request
    import capo_acm.types.list_certificates_response
    import capo_acm.types.list_tags_for_certificate_request
    import capo_acm.types.list_tags_for_certificate_response
    import capo_acm.types.list_tags_for_resource_request
    import capo_acm.types.list_tags_for_resource_response
    import capo_acm.types.max_items
    import capo_acm.types.next_token
    import capo_acm.types.passphrase_blob
    import capo_acm.types.pca_arn
    import capo_acm.types.prevalidation_options
    import capo_acm.types.private_key_blob
    import capo_acm.types.put_account_configuration_request
    import capo_acm.types.remove_tags_from_certificate_request
    import capo_acm.types.renew_certificate_request
    import capo_acm.types.request_certificate_request
    import capo_acm.types.request_certificate_response
    import capo_acm.types.resend_validation_email_request
    import capo_acm.types.revocation_reason
    import capo_acm.types.revoke_acme_account_request
    import capo_acm.types.revoke_acme_external_account_binding_request
    import capo_acm.types.revoke_certificate_request
    import capo_acm.types.revoke_certificate_response
    import capo_acm.types.role_arn
    import capo_acm.types.search_certificates_request
    import capo_acm.types.search_certificates_response
    import capo_acm.types.search_certificates_sort_by
    import capo_acm.types.search_certificates_sort_order
    import capo_acm.types.search_max_results
    import capo_acm.types.sort_by
    import capo_acm.types.sort_order
    import capo_acm.types.tag_key_list
    import capo_acm.types.tag_list
    import capo_acm.types.tag_resource_request
    import capo_acm.types.untag_resource_request
    import capo_acm.types.update_acme_domain_validation_request
    import capo_acm.types.update_acme_endpoint_request
    import capo_acm.types.update_certificate_options_request
    import capo_acm.types.validation_method


class AsyncACMClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    endpoint: str | None
    use_fips: bool | None
    use_dual_stack: bool | None
    credentials_provider: IdentityProvider[Credentials] | None
    service_type: str | None


class AsyncACMClient:
    """A client for the ``ACM`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        service_type: The service type: ACM or ACM-ACME. Injected via @staticContextParams.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        endpoint: str | None = None,
        use_fips: bool | None = None,
        use_dual_stack: bool | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        service_type: str | None = None,
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
        self._config = AsyncACMClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "endpoint": endpoint,
                "use_fips": use_fips,
                "use_dual_stack": use_dual_stack,
                "credentials_provider": resolved_credentials_provider,
                "service_type": service_type,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncACMClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncACMClientConfig = config_overrides or {}
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
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            service_type=overrides.get(
                "service_type", self._config.get("service_type")
            ),
        )
        return interceptors_, options_

    async def add_tags_to_certificate(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        tags: "capo_acm.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Adds one or more tags to an ACM certificate. Tags are labels that you can use to identify and organize your Amazon Web Services resources. Each tag consists of a <code>key</code> and an optional <code>value</code>. You specify the certificate on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. </p> <note> <p>This action applies only to the <code>certificate</code> resource type. For all other ACM resource types, use <a>TagResource</a> instead.</p> </note> <p>You can apply a tag to just one certificate if you want to identify a specific characteristic of that certificate, or you can apply the same tag to multiple certificates if you want to filter for a common relationship among those certificates. Similarly, you can apply the same tag to multiple resources if you want to specify a relationship among those resources. For example, you can add the same tag to an ACM certificate and an Elastic Load Balancing load balancer to indicate that they are both used by the same website. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/tags.html">Tagging ACM certificates</a>. </p> <p>To remove one or more tags, use the <a>RemoveTagsFromCertificate</a> action. To view all of the tags that have been applied to the certificate, use the <a>ListTagsForCertificate</a> action. </p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate to which the tag is to be applied. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>
            tags: <p>The key-value pair that defines the tag. The tag value is optional.</p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter was invalid.</p>
            capo_acm.errors.invalid_tag_exception.InvalidTagException: <p>One or both of the values that make up the key-value pair is not valid. For example, you cannot specify a tag value that begins with <code>aws:</code>.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.tag_policy_exception.TagPolicyException: <p>A specified tag did not comply with an existing tag policy and was rejected.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains too many tags. Try the request again with fewer tags.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.add_tags_to_certificate_request.AddTagsToCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.add_tags_to_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.add_tags_to_certificate.async_add_tags_to_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.add_tags_to_certificate_request.AddTagsToCertificateRequest = {
            "certificate_arn": certificate_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_acme_domain_validation(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        domain_name: "capo_acm.types.domain_name.DomainName",
        prevalidation_options: "capo_acm.types.prevalidation_options.PrevalidationOptions",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        idempotency_token: Optional[str] = None,
        tags: Optional["capo_acm.types.tag_list.TagList"] = None,
    ) -> "capo_acm.types.create_acme_domain_validation_response.CreateAcmeDomainValidationResponse":
        """<p>Creates a domain validation for an ACME endpoint. Domain validations authorize the endpoint to issue certificates for specified domain names. You configure prevalidation to prove domain ownership.</p>

        Args:
            idempotency_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>
            domain_name: <p>The domain name to validate.</p>
            prevalidation_options: <p>The prevalidation options for the domain.</p>
            tags: <p>One or more tags to associate with the domain validation.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.create_acme_domain_validation_request.CreateAcmeDomainValidationRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.create_acme_domain_validation_response.CreateAcmeDomainValidationResponse"
        ]:
            import capo_acm._operations.certificate_manager.create_acme_domain_validation

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.create_acme_domain_validation.async_create_acme_domain_validation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.create_acme_domain_validation_request.CreateAcmeDomainValidationRequest = {
            "acme_endpoint_arn": acme_endpoint_arn,
            "domain_name": domain_name,
            "prevalidation_options": prevalidation_options,
        }
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_acme_endpoint(
        self,
        authorization_behavior: "capo_acm.types.acme_authorization_behavior.AcmeAuthorizationBehavior",
        certificate_authority: "capo_acm.types.certificate_authority.CertificateAuthority",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        idempotency_token: Optional[str] = None,
        contact: Optional["capo_acm.types.acme_contact.AcmeContact"] = None,
        tags: Optional["capo_acm.types.tag_list.TagList"] = None,
        certificate_tags: Optional["capo_acm.types.tag_list.TagList"] = None,
    ) -> "capo_acm.types.create_acme_endpoint_response.CreateAcmeEndpointResponse":
        """<p>Creates an ACME endpoint, which is a managed ACME server with a unique endpoint URL. After creation, ACME clients can use the endpoint URL to automate certificate issuance using the ACME protocol.</p>

        Args:
            idempotency_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            authorization_behavior: <p>The authorization behavior for the ACME endpoint.</p>
            contact: <p>Specifies whether ACME clients must provide contact information during account registration.</p>
            certificate_authority: <p>The type of certificate authority to use for issuing certificates through this ACME endpoint.</p>
            tags: <p>One or more tags to associate with the ACME endpoint.</p>
            certificate_tags: <p>Tags to apply to certificates issued through this ACME endpoint.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.create_acme_endpoint_request.CreateAcmeEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.create_acme_endpoint_response.CreateAcmeEndpointResponse"
        ]:
            import capo_acm._operations.certificate_manager.create_acme_endpoint

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.create_acme_endpoint.async_create_acme_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.create_acme_endpoint_request.CreateAcmeEndpointRequest = {
            "authorization_behavior": authorization_behavior,
            "certificate_authority": certificate_authority,
        }
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if contact is not None:
            input_["contact"] = contact
        if tags is not None:
            input_["tags"] = tags
        if certificate_tags is not None:
            input_["certificate_tags"] = certificate_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_acme_external_account_binding(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        role_arn: "capo_acm.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        idempotency_token: Optional[str] = None,
        expiration: Optional["capo_acm.types.expiration.Expiration"] = None,
        tags: Optional["capo_acm.types.tag_list.TagList"] = None,
    ) -> "capo_acm.types.create_acme_external_account_binding_response.CreateAcmeExternalAccountBindingResponse":
        """<p>Creates an external account binding (EAB) for an ACME endpoint. An EAB provides credentials that authorize an ACME client to register an account with the endpoint. Each EAB is associated with an IAM role that controls what certificate operations the ACME client can perform.</p>

        Args:
            idempotency_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to associate with the external account binding.</p>
            expiration: <p>The expiration configuration for the external account binding.</p>
            tags: <p>One or more tags to associate with the external account binding.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.create_acme_external_account_binding_request.CreateAcmeExternalAccountBindingRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.create_acme_external_account_binding_response.CreateAcmeExternalAccountBindingResponse"
        ]:
            import capo_acm._operations.certificate_manager.create_acme_external_account_binding

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.create_acme_external_account_binding.async_create_acme_external_account_binding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.create_acme_external_account_binding_request.CreateAcmeExternalAccountBindingRequest = {
            "acme_endpoint_arn": acme_endpoint_arn,
            "role_arn": role_arn,
        }
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if expiration is not None:
            input_["expiration"] = expiration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_acme_domain_validation(
        self,
        acme_domain_validation_arn: "capo_acm.types.acme_domain_validation_arn.AcmeDomainValidationArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Deletes a domain validation. After deletion, the ACME endpoint can no longer issue certificates for the associated domain.</p>

        Args:
            acme_domain_validation_arn: <p>The Amazon Resource Name (ARN) of the ACME domain validation to delete.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.delete_acme_domain_validation_request.DeleteAcmeDomainValidationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.delete_acme_domain_validation

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.delete_acme_domain_validation.async_delete_acme_domain_validation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.delete_acme_domain_validation_request.DeleteAcmeDomainValidationRequest = {
            "acme_domain_validation_arn": acme_domain_validation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_acme_endpoint(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Deletes an ACME endpoint. After deletion, the endpoint URL is no longer accessible and ACME clients cannot issue certificates through it. Any existing external account bindings and domain validations associated with the endpoint are also deleted.</p>

        Args:
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint to delete.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.delete_acme_endpoint_request.DeleteAcmeEndpointRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.delete_acme_endpoint

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.delete_acme_endpoint.async_delete_acme_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.delete_acme_endpoint_request.DeleteAcmeEndpointRequest = {
            "acme_endpoint_arn": acme_endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_acme_external_account_binding(
        self,
        acme_external_account_binding_arn: "capo_acm.types.acme_external_account_binding_arn.AcmeExternalAccountBindingArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Deletes an external account binding. Previously fetched credentials for this binding will no longer be usable for account registration. A deleted binding cannot be recovered.</p>

        Args:
            acme_external_account_binding_arn: <p>The Amazon Resource Name (ARN) of the ACME external account binding to delete.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.delete_acme_external_account_binding_request.DeleteAcmeExternalAccountBindingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.delete_acme_external_account_binding

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.delete_acme_external_account_binding.async_delete_acme_external_account_binding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.delete_acme_external_account_binding_request.DeleteAcmeExternalAccountBindingRequest = {
            "acme_external_account_binding_arn": acme_external_account_binding_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_certificate(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Deletes a certificate and its associated private key. If this action succeeds, the certificate is not available for use by Amazon Web Services services integrated with ACM. Deleting a certificate is eventually consistent. The may be a short delay before the certificate no longer appears in the list that can be displayed by calling the <a>ListCertificates</a> action or be retrieved by calling the <a>GetCertificate</a> action.</p> <note> <p>You cannot delete an ACM certificate that is being used by another Amazon Web Services service. To delete a certificate that is in use, you must first remove the certificate association using the console or the CLI for the associated service.</p> <p>Deleting a certificate issued by a private certificate authority (CA) has no effect on the CA. You will continue to be charged for the CA until it is deleted. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PCADeleteCA.html"> Deleting Your Private CA</a> in the <i>Private Certificate Authority User Guide</i>.</p> <p>You cannot delete a certificate with a <code>CertificateKeyPairOrigin</code> of <code>ACME</code>. ACM automatically deletes these certificates 1 year after they expire.</p> </note> <p>Deleting a certificate issued by a private certificate authority (CA) has no effect on the CA. You will continue to be charged for the CA until it is deleted. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PCADeleteCA.html">Deleting your private CA</a> in the <i>Amazon Web Services Private Certificate Authority User Guide</i>.</p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate to be deleted. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.resource_in_use_exception.ResourceInUseException: <p>The certificate is in use by another Amazon Web Services service in the caller's account. Remove the association and try again.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.delete_certificate_request.DeleteCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.delete_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.delete_certificate.async_delete_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.delete_certificate_request.DeleteCertificateRequest = {
            "certificate_arn": certificate_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_acme_account(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        account_url: str,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.describe_acme_account_response.DescribeAcmeAccountResponse":
        """<p>Returns detailed metadata about the specified ACME account, including its status, public key thumbprint, and associated external account binding.</p>

        Args:
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>
            account_url: <p>The URL of the ACME account.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.describe_acme_account_request.DescribeAcmeAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.describe_acme_account_response.DescribeAcmeAccountResponse"
        ]:
            import capo_acm._operations.certificate_manager.describe_acme_account

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.describe_acme_account.async_describe_acme_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.describe_acme_account_request.DescribeAcmeAccountRequest = {
            "acme_endpoint_arn": acme_endpoint_arn,
            "account_url": account_url,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_acme_domain_validation(
        self,
        acme_domain_validation_arn: "capo_acm.types.acme_domain_validation_arn.AcmeDomainValidationArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.describe_acme_domain_validation_response.DescribeAcmeDomainValidationResponse":
        """<p>Returns detailed metadata about the specified domain validation, including its status, domain scope, and DNS resource records required for validation.</p>

        Args:
            acme_domain_validation_arn: <p>The Amazon Resource Name (ARN) of the ACME domain validation.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.describe_acme_domain_validation_request.DescribeAcmeDomainValidationRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.describe_acme_domain_validation_response.DescribeAcmeDomainValidationResponse"
        ]:
            import capo_acm._operations.certificate_manager.describe_acme_domain_validation

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.describe_acme_domain_validation.async_describe_acme_domain_validation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.describe_acme_domain_validation_request.DescribeAcmeDomainValidationRequest = {
            "acme_domain_validation_arn": acme_domain_validation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_acme_endpoint(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.describe_acme_endpoint_response.DescribeAcmeEndpointResponse":
        """<p>Returns detailed metadata about the specified ACME endpoint, including its status, URL, authorization behavior, and certificate authority configuration.</p>

        Args:
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.describe_acme_endpoint_request.DescribeAcmeEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.describe_acme_endpoint_response.DescribeAcmeEndpointResponse"
        ]:
            import capo_acm._operations.certificate_manager.describe_acme_endpoint

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.describe_acme_endpoint.async_describe_acme_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.describe_acme_endpoint_request.DescribeAcmeEndpointRequest = {
            "acme_endpoint_arn": acme_endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_acme_external_account_binding(
        self,
        acme_external_account_binding_arn: "capo_acm.types.acme_external_account_binding_arn.AcmeExternalAccountBindingArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.describe_acme_external_account_binding_response.DescribeAcmeExternalAccountBindingResponse":
        """<p>Returns detailed metadata about the specified external account binding, including the associated IAM role, expiration time, and usage history.</p>

        Args:
            acme_external_account_binding_arn: <p>The Amazon Resource Name (ARN) of the ACME external account binding.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.describe_acme_external_account_binding_request.DescribeAcmeExternalAccountBindingRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.describe_acme_external_account_binding_response.DescribeAcmeExternalAccountBindingResponse"
        ]:
            import capo_acm._operations.certificate_manager.describe_acme_external_account_binding

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.describe_acme_external_account_binding.async_describe_acme_external_account_binding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.describe_acme_external_account_binding_request.DescribeAcmeExternalAccountBindingRequest = {
            "acme_external_account_binding_arn": acme_external_account_binding_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_certificate(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.describe_certificate_response.DescribeCertificateResponse":
        """<p>Returns detailed metadata about the specified ACM certificate.</p> <p>If you have just created a certificate using the <code>RequestCertificate</code> action, there is a delay of several seconds before you can retrieve information about it.</p>

        Args:
            certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.describe_certificate_request.DescribeCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.describe_certificate_response.DescribeCertificateResponse"
        ]:
            import capo_acm._operations.certificate_manager.describe_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.describe_certificate.async_describe_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.describe_certificate_request.DescribeCertificateRequest = {
            "certificate_arn": certificate_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_certificate(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        passphrase: "capo_acm.types.passphrase_blob.PassphraseBlob",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.export_certificate_response.ExportCertificateResponse":
        """<p>Exports a private certificate issued by a private certificate authority (CA) or a public certificate for use anywhere. The exported file contains the certificate, the certificate chain, and the encrypted private key associated with the public key that is embedded in the certificate. For security, you must assign a passphrase for the private key when exporting it. </p> <p>For information about exporting and formatting a certificate using the ACM console or CLI, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/export-private.html">Export a private certificate</a> and <a href="https://docs.aws.amazon.com/acm/latest/userguide/export-public-certificate">Export a public certificate</a>.</p> <note> <p>ACM public certificates created prior to June 17, 2025 cannot be exported.</p> </note>

        Args:
            certificate_arn: <p>An Amazon Resource Name (ARN) of the issued certificate. This must be of the form:</p> <p> <code>arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012</code> </p>
            passphrase: <p>Passphrase to associate with the encrypted exported private key. </p> <note> <p>When creating your passphrase, you can use any ASCII character except #, $, or %.</p> </note> <p>If you want to later decrypt the private key, you must have the passphrase. You can use the following OpenSSL command to decrypt a private key. After entering the command, you are prompted for the passphrase.</p> <p> <code>openssl rsa -in encrypted_key.pem -out decrypted_key.pem</code> </p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.request_in_progress_exception.RequestInProgressException: <p>The certificate request is in process and the certificate in your account has not yet been issued.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.export_certificate_request.ExportCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.export_certificate_response.ExportCertificateResponse"
        ]:
            import capo_acm._operations.certificate_manager.export_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.export_certificate.async_export_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.export_certificate_request.ExportCertificateRequest = {
            "certificate_arn": certificate_arn,
            "passphrase": passphrase,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_configuration(
        self, *, config_overrides: Optional[AsyncACMClientConfig] = None
    ) -> "capo_acm.types.get_account_configuration_response.GetAccountConfigurationResponse":
        """<p>Returns the account configuration options associated with an Amazon Web Services account.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.get_account_configuration_response.GetAccountConfigurationResponse"
        ]:
            import capo_acm._operations.certificate_manager.get_account_configuration

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.get_account_configuration.async_get_account_configuration(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_acme_external_account_binding_credentials(
        self,
        acme_external_account_binding_arn: "capo_acm.types.acme_external_account_binding_arn.AcmeExternalAccountBindingArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.get_acme_external_account_binding_credentials_response.GetAcmeExternalAccountBindingCredentialsResponse":
        """<p>Retrieves the key ID and MAC key credentials for an external account binding. These credentials are used by ACME clients during account registration to bind to the endpoint.</p>

        Args:
            acme_external_account_binding_arn: <p>The Amazon Resource Name (ARN) of the ACME external account binding.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.get_acme_external_account_binding_credentials_request.GetAcmeExternalAccountBindingCredentialsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.get_acme_external_account_binding_credentials_response.GetAcmeExternalAccountBindingCredentialsResponse"
        ]:
            import capo_acm._operations.certificate_manager.get_acme_external_account_binding_credentials

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.get_acme_external_account_binding_credentials.async_get_acme_external_account_binding_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.get_acme_external_account_binding_credentials_request.GetAcmeExternalAccountBindingCredentialsRequest = {
            "acme_external_account_binding_arn": acme_external_account_binding_arn
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
        certificate_arn: "capo_acm.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.get_certificate_response.GetCertificateResponse":
        """<p>Retrieves a certificate and its certificate chain. The certificate may be either a public or private certificate issued using the ACM <code>RequestCertificate</code> action, or a certificate imported into ACM using the <code>ImportCertificate</code> action. The chain consists of the certificate of the issuing CA and the intermediate certificates of any other subordinate CAs. All of the certificates are base64 encoded. You can use <a href="https://wiki.openssl.org/index.php/Command_Line_Utilities">OpenSSL</a> to decode the certificates and inspect individual fields.</p>

        Args:
            certificate_arn: <p>String that contains a certificate ARN in the following format:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.request_in_progress_exception.RequestInProgressException: <p>The certificate request is in process and the certificate in your account has not yet been issued.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.get_certificate_request.GetCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.get_certificate_response.GetCertificateResponse"
        ]:
            import capo_acm._operations.certificate_manager.get_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.get_certificate.async_get_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.get_certificate_request.GetCertificateRequest = {
            "certificate_arn": certificate_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_certificate(
        self,
        certificate: "capo_acm.types.certificate_body_blob.CertificateBodyBlob",
        private_key: "capo_acm.types.private_key_blob.PrivateKeyBlob",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        certificate_arn: Optional["capo_acm.types.arn.Arn"] = None,
        certificate_chain: Optional[
            "capo_acm.types.certificate_chain_blob.CertificateChainBlob"
        ] = None,
        tags: Optional["capo_acm.types.tag_list.TagList"] = None,
    ) -> "capo_acm.types.import_certificate_response.ImportCertificateResponse":
        r"""<p>Imports a certificate into Certificate Manager (ACM) to use with services that are integrated with ACM. Note that <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html">integrated services</a> allow only certificate types and keys they support to be associated with their resources. Further, their support differs depending on whether the certificate is imported into IAM or into ACM. For more information, see the documentation for each service. For more information about importing certificates into ACM, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html">Importing Certificates</a> in the <i>Certificate Manager User Guide</i>. </p> <note> <p>ACM does not provide <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html">managed renewal</a> for certificates that you import.</p> </note> <p>Note the following guidelines when importing third party certificates:</p> <ul> <li> <p>You must enter the private key that matches the certificate you are importing.</p> </li> <li> <p>The private key must be unencrypted. You cannot import a private key that is protected by a password or a passphrase.</p> </li> <li> <p>The private key must be no larger than 5 KB (5,120 bytes).</p> </li> <li> <p>The certificate, private key, and certificate chain must be PEM-encoded.</p> </li> <li> <p>The current time must be between the <code>Not Before</code> and <code>Not After</code> certificate fields.</p> </li> <li> <p>The <code>Issuer</code> field must not be empty.</p> </li> <li> <p>The OCSP authority URL, if present, must not exceed 1000 characters.</p> </li> <li> <p>To import a new certificate, omit the <code>CertificateArn</code> argument. Include this argument only when you want to replace a previously imported certificate.</p> </li> <li> <p>When you import a certificate by using the CLI, you must specify the certificate, the certificate chain, and the private key by their file names preceded by <code>fileb://</code>. For example, you can specify a certificate saved in the <code>C:\temp</code> folder as <code>fileb://C:\temp\certificate_to_import.pem</code>. If you are making an HTTP or HTTPS Query request, include these arguments as BLOBs. </p> </li> <li> <p>When you import a certificate by using an SDK, you must specify the certificate, the certificate chain, and the private key files in the manner required by the programming language you're using. </p> </li> <li> <p>The cryptographic algorithm of an imported certificate must match the algorithm of the signing CA. For example, if the signing CA key type is RSA, then the certificate key type must also be RSA.</p> </li> </ul> <p>This operation returns the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the imported certificate.</p>

        Args:
            certificate_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an imported certificate to replace. To import a new certificate, omit this field. </p>
            certificate: <p>The certificate to import.</p>
            private_key: <p>The private key that matches the public key in the certificate.</p>
            certificate_chain: <p>The PEM encoded certificate chain.</p>
            tags: <p>One or more resource tags to associate with the imported certificate. </p> <p>Note: You cannot apply tags when reimporting a certificate.</p>

        Raises:
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter was invalid.</p>
            capo_acm.errors.invalid_tag_exception.InvalidTagException: <p>One or both of the values that make up the key-value pair is not valid. For example, you cannot specify a tag value that begins with <code>aws:</code>.</p>
            capo_acm.errors.limit_exceeded_exception.LimitExceededException: <p>An ACM quota has been exceeded.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.tag_policy_exception.TagPolicyException: <p>A specified tag did not comply with an existing tag policy and was rejected.</p>
            capo_acm.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains too many tags. Try the request again with fewer tags.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.import_certificate_request.ImportCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.import_certificate_response.ImportCertificateResponse"
        ]:
            import capo_acm._operations.certificate_manager.import_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.import_certificate.async_import_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.import_certificate_request.ImportCertificateRequest = {
            "certificate": certificate,
            "private_key": private_key,
        }
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if certificate_chain is not None:
            input_["certificate_chain"] = certificate_chain
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_acme_accounts(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_acm.types.list_acme_accounts_response.ListAcmeAccountsResponse":
        """<p>Retrieves a list of ACME accounts registered with the specified ACME endpoint. ACME accounts are created when clients use external account binding credentials to register.</p>

        Args:
            next_token: <p>A token for pagination.</p>
            max_results: <p>The maximum number of results to return.</p>
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_acme_accounts_request.ListAcmeAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_acme_accounts_response.ListAcmeAccountsResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_acme_accounts

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_acme_accounts.async_list_acme_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_acme_accounts_request.ListAcmeAccountsRequest = {
            "acme_endpoint_arn": acme_endpoint_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_acme_accounts(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_acm.types.acme_account_summary.AcmeAccountSummary]":
        _token = next_token
        while True:
            _response = await self.list_acme_accounts(
                acme_endpoint_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("acme_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_acme_domain_validations(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_acm.types.list_acme_domain_validations_response.ListAcmeDomainValidationsResponse":
        """<p>Retrieves a list of domain validations for the specified ACME endpoint.</p>

        Args:
            next_token: <p>A token for pagination.</p>
            max_results: <p>The maximum number of results to return.</p>
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_acme_domain_validations_request.ListAcmeDomainValidationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_acme_domain_validations_response.ListAcmeDomainValidationsResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_acme_domain_validations

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_acme_domain_validations.async_list_acme_domain_validations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_acme_domain_validations_request.ListAcmeDomainValidationsRequest = {
            "acme_endpoint_arn": acme_endpoint_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_acme_domain_validations(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_acm.types.acme_domain_validation_summary.AcmeDomainValidationSummary]":
        _token = next_token
        while True:
            _response = await self.list_acme_domain_validations(
                acme_endpoint_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("acme_domain_validations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_acme_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_acm.types.list_acme_endpoints_response.ListAcmeEndpointsResponse":
        """<p>Retrieves a list of ACME endpoints in your account. Use this operation to view all configured ACME endpoints and their current status.</p>

        Args:
            next_token: <p>A token for pagination.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_acme_endpoints_request.ListAcmeEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_acme_endpoints_response.ListAcmeEndpointsResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_acme_endpoints

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_acme_endpoints.async_list_acme_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_acme_endpoints_request.ListAcmeEndpointsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_acme_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_acm.types.acme_endpoint_summary.AcmeEndpointSummary]":
        _token = next_token
        while True:
            _response = await self.list_acme_endpoints(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("acme_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_acme_external_account_bindings(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_acm.types.list_acme_external_account_bindings_response.ListAcmeExternalAccountBindingsResponse":
        """<p>Retrieves a list of external account bindings for the specified ACME endpoint.</p>

        Args:
            next_token: <p>A token for pagination.</p>
            max_results: <p>The maximum number of results to return.</p>
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_acme_external_account_bindings_request.ListAcmeExternalAccountBindingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_acme_external_account_bindings_response.ListAcmeExternalAccountBindingsResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_acme_external_account_bindings

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_acme_external_account_bindings.async_list_acme_external_account_bindings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_acme_external_account_bindings_request.ListAcmeExternalAccountBindingsRequest = {
            "acme_endpoint_arn": acme_endpoint_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_acme_external_account_bindings(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_acm.types.acme_external_account_binding_summary.AcmeExternalAccountBindingSummary]":
        _token = next_token
        while True:
            _response = await self.list_acme_external_account_bindings(
                acme_endpoint_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("external_account_bindings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_certificate_domain_validations(
        self,
        certificate_arn: "capo_acm.types.certificate_arn.CertificateArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional["capo_acm.types.next_token.NextToken"] = None,
        max_items: Optional["capo_acm.types.max_items.MaxItems"] = None,
    ) -> "capo_acm.types.list_certificate_domain_validations_response.ListCertificateDomainValidationsResponse":
        """<p>Returns per-domain validation summaries for an ACM certificate. Each summary includes the domain name, the active validation configuration, and the requested validation configuration when a validation method migration is in progress. You can use the results to monitor the progress of an email-to-DNS validation migration and to retrieve the CNAME records required for DNS validation.</p>

        Args:
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate for which to list domain validation summaries.</p>
            next_token: <p>A token returned by a previous call to <code>ListCertificateDomainValidations</code>. If the number of results exceeds <code>MaxItems</code>, use this token to retrieve the next page of results.</p>
            max_items: <p>The maximum number of domain validation summaries to return. If you don't specify a value, the default is 1000.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.invalid_args_exception.InvalidArgsException: <p>One or more of request parameters specified is not valid.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_certificate_domain_validations_request.ListCertificateDomainValidationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_certificate_domain_validations_response.ListCertificateDomainValidationsResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_certificate_domain_validations

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_certificate_domain_validations.async_list_certificate_domain_validations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_certificate_domain_validations_request.ListCertificateDomainValidationsRequest = {
            "certificate_arn": certificate_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_certificate_domain_validations(
        self,
        certificate_arn: "capo_acm.types.certificate_arn.CertificateArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        next_token: Optional["capo_acm.types.next_token.NextToken"] = None,
        max_items: Optional["capo_acm.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_acm.types.domain_validation_summary.DomainValidationSummary]":
        _token = next_token
        while True:
            _response = await self.list_certificate_domain_validations(
                certificate_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("domain_validation_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_certificates(
        self,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        certificate_statuses: Optional[
            "capo_acm.types.certificate_statuses.CertificateStatuses"
        ] = None,
        certificate_key_pair_origins: Optional[
            "capo_acm.types.certificate_key_pair_origins.CertificateKeyPairOrigins"
        ] = None,
        includes: Optional["capo_acm.types.filters.Filters"] = None,
        next_token: Optional["capo_acm.types.next_token.NextToken"] = None,
        max_items: Optional["capo_acm.types.max_items.MaxItems"] = None,
        sort_by: Optional["capo_acm.types.sort_by.SortBy"] = None,
        sort_order: Optional["capo_acm.types.sort_order.SortOrder"] = None,
    ) -> "capo_acm.types.list_certificates_response.ListCertificatesResponse":
        """<p>Retrieves a list of certificate ARNs and domain names. You can request that only certificates that match a specific status be listed. You can also filter by specific attributes of the certificate. Default filtering returns only <code>RSA_2048</code> certificates. For more information, see <a>Filters</a>.</p> <note> <p>By default, this action does not return certificates with a <code>CertificateKeyPairOrigin</code> of <code>ACME</code>. To include ACME certificates, specify <code>ACME</code> in the <code>CertificateKeyPairOrigins</code> filter.</p> </note>

        Args:
            certificate_statuses: <p>Filter the certificate list by status value.</p>
            certificate_key_pair_origins: <p>Filter the certificate list by certificate key pair origin. Specify one or more <code>CertificateKeyPairOrigin</code> values. Default filtering returns only certificates with key pair origin of <code>AWS_MANAGED</code> and <code>CUSTOMER_PROVIDED</code>.</p>
            includes: <p>Filter the certificate list. For more information, see the <a>Filters</a> structure.</p>
            next_token: <p>Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the response you just received.</p>
            max_items: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            sort_by: <p>Specifies the field to sort results by. If you specify <code>SortBy</code>, you must also specify <code>SortOrder</code>.</p>
            sort_order: <p>Specifies the order of sorted results. If you specify <code>SortOrder</code>, you must also specify <code>SortBy</code>.</p>

        Raises:
            capo_acm.errors.invalid_args_exception.InvalidArgsException: <p>One or more of request parameters specified is not valid.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_certificates_request.ListCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_certificates_response.ListCertificatesResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_certificates

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_certificates.async_list_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_certificates_request.ListCertificatesRequest = {}
        if certificate_statuses is not None:
            input_["certificate_statuses"] = certificate_statuses
        if certificate_key_pair_origins is not None:
            input_["certificate_key_pair_origins"] = certificate_key_pair_origins
        if includes is not None:
            input_["includes"] = includes
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_certificates(
        self,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        certificate_statuses: Optional[
            "capo_acm.types.certificate_statuses.CertificateStatuses"
        ] = None,
        certificate_key_pair_origins: Optional[
            "capo_acm.types.certificate_key_pair_origins.CertificateKeyPairOrigins"
        ] = None,
        includes: Optional["capo_acm.types.filters.Filters"] = None,
        next_token: Optional["capo_acm.types.next_token.NextToken"] = None,
        max_items: Optional["capo_acm.types.max_items.MaxItems"] = None,
        sort_by: Optional["capo_acm.types.sort_by.SortBy"] = None,
        sort_order: Optional["capo_acm.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_acm.types.certificate_summary.CertificateSummary]":
        _token = next_token
        while True:
            _response = await self.list_certificates(
                config_overrides=config_overrides,
                certificate_statuses=certificate_statuses,
                certificate_key_pair_origins=certificate_key_pair_origins,
                includes=includes,
                next_token=_token,
                max_items=max_items,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("certificate_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_certificate(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.list_tags_for_certificate_response.ListTagsForCertificateResponse":
        """<p>Lists the tags that have been applied to the ACM certificate. Use the certificate's Amazon Resource Name (ARN) to specify the certificate. To add a tag to an ACM certificate, use the <a>AddTagsToCertificate</a> action. To delete a tag, use the <a>RemoveTagsFromCertificate</a> action. </p> <note> <p>This action applies only to the <code>certificate</code> resource type. For all other ACM resource types, use <a>ListTagsForResource</a> instead.</p> </note>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate for which you want to list the tags. This must have the following form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_tags_for_certificate_request.ListTagsForCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_tags_for_certificate_response.ListTagsForCertificateResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_tags_for_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_tags_for_certificate.async_list_tags_for_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_tags_for_certificate_request.ListTagsForCertificateRequest = {
            "certificate_arn": certificate_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_acm.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with an ACM resource.</p> <note> <p>Use this action for all ACM resource types except the <code>certificate</code> resource type. For certificate resources, use <a>ListTagsForCertificate</a> instead.</p> </note> <p>To add one or more tags, use the <a>TagResource</a> action. To remove one or more tags, use the <a>UntagResource</a> action.</p>

        Args:
            resource_arn: <p>The ARN of the ACM resource for which to list tags.</p>

        Raises:
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_acm._operations.certificate_manager.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_configuration(
        self,
        idempotency_token: "capo_acm.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        expiry_events: Optional[
            "capo_acm.types.expiry_events_configuration.ExpiryEventsConfiguration"
        ] = None,
    ) -> None:
        """<p>Adds or modifies account-level configurations in ACM. </p> <p>The supported configuration option is <code>DaysBeforeExpiry</code>. This option specifies the number of days prior to certificate expiration when ACM starts generating <code>EventBridge</code> events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.</p>

        Args:
            expiry_events: <p>Specifies expiration events associated with an account.</p>
            idempotency_token: <p>Customer-chosen string used to distinguish between calls to <code>PutAccountConfiguration</code>. Idempotency tokens time out after one hour. If you call <code>PutAccountConfiguration</code> multiple times with the same unexpired idempotency token, ACM treats it as the same request and returns the original result. If you change the idempotency token for each call, ACM treats each call as a new request.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.put_account_configuration_request.PutAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.put_account_configuration

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.put_account_configuration.async_put_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.put_account_configuration_request.PutAccountConfigurationRequest = {
            "idempotency_token": idempotency_token
        }
        if expiry_events is not None:
            input_["expiry_events"] = expiry_events

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags_from_certificate(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        tags: "capo_acm.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Remove one or more tags from an ACM certificate. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this function, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value. </p> <note> <p>This action applies only to the <code>certificate</code> resource type. For all other ACM resource types, use <a>UntagResource</a> instead.</p> </note> <p>To add tags to a certificate, use the <a>AddTagsToCertificate</a> action. To view all of the tags that have been applied to a specific ACM certificate, use the <a>ListTagsForCertificate</a> action. </p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM Certificate with one or more tags that you want to remove. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>
            tags: <p>The key-value pair that defines the tag to remove.</p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter was invalid.</p>
            capo_acm.errors.invalid_tag_exception.InvalidTagException: <p>One or both of the values that make up the key-value pair is not valid. For example, you cannot specify a tag value that begins with <code>aws:</code>.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.tag_policy_exception.TagPolicyException: <p>A specified tag did not comply with an existing tag policy and was rejected.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.remove_tags_from_certificate_request.RemoveTagsFromCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.remove_tags_from_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.remove_tags_from_certificate.async_remove_tags_from_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.remove_tags_from_certificate_request.RemoveTagsFromCertificateRequest = {
            "certificate_arn": certificate_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def renew_certificate(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Renews an <a href="https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html">eligible ACM certificate</a>. In order to renew your Amazon Web Services Private CA certificates with ACM, you must first <a href="https://docs.aws.amazon.com/privateca/latest/userguide/assign-permissions.html#PcaPermissions">grant the ACM service principal permission to do so</a>. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html">Testing Managed Renewal</a> in the ACM User Guide.</p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate to be renewed. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.request_in_progress_exception.RequestInProgressException: <p>The certificate request is in process and the certificate in your account has not yet been issued.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.renew_certificate_request.RenewCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.renew_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.renew_certificate.async_renew_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.renew_certificate_request.RenewCertificateRequest = {
            "certificate_arn": certificate_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def request_certificate(
        self,
        domain_name: "capo_acm.types.domain_name_string.DomainNameString",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        validation_method: Optional[
            "capo_acm.types.validation_method.ValidationMethod"
        ] = None,
        subject_alternative_names: Optional[
            "capo_acm.types.domain_list.DomainList"
        ] = None,
        idempotency_token: Optional[
            "capo_acm.types.idempotency_token.IdempotencyToken"
        ] = None,
        domain_validation_options: Optional[
            "capo_acm.types.domain_validation_option_list.DomainValidationOptionList"
        ] = None,
        options: Optional[
            "capo_acm.types.certificate_options.CertificateOptions"
        ] = None,
        certificate_authority_arn: Optional["capo_acm.types.pca_arn.PcaArn"] = None,
        tags: Optional["capo_acm.types.tag_list.TagList"] = None,
        key_algorithm: Optional["capo_acm.types.key_algorithm.KeyAlgorithm"] = None,
        managed_by: Optional[
            "capo_acm.types.certificate_managed_by.CertificateManagedBy"
        ] = None,
    ) -> "capo_acm.types.request_certificate_response.RequestCertificateResponse":
        """<p>Requests an ACM certificate for use with other Amazon Web Services services. To request an ACM certificate, you must specify a fully qualified domain name (FQDN) in the <code>DomainName</code> parameter. You can also specify additional FQDNs in the <code>SubjectAlternativeNames</code> parameter. </p> <p>If you are requesting a private certificate, domain validation is not required. If you are requesting a public certificate, each domain name that you specify must be validated to verify that you own or control the domain. You can use <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html">DNS validation</a> or <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html">email validation</a>. We recommend that you use DNS validation.</p> <note> <p>ACM behavior differs from the <a href="https://datatracker.ietf.org/doc/html/rfc6125#appendix-B.2">RFC 6125</a> specification of the certificate validation process. ACM first checks for a Subject Alternative Name, and, if it finds one, ignores the common name (CN).</p> </note> <p>After successful completion of the <code>RequestCertificate</code> action, there is a delay of several seconds before you can retrieve information about the new certificate.</p>

        Args:
            domain_name: <p>Fully qualified domain name (FQDN), such as www.example.com, that you want to secure with an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com. </p> <p>In compliance with <a href="https://datatracker.ietf.org/doc/html/rfc5280">RFC 5280</a>, the length of the domain name (technically, the Common Name) that you provide cannot exceed 64 octets (characters), including periods. To add a longer domain name, specify it in the Subject Alternative Name field, which supports names up to 253 octets in length. </p>
            validation_method: <p>The method you want to use if you are requesting a public certificate to validate that you own or control domain. You can <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html">validate with DNS</a> or <a href="https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html">validate with email</a>. We recommend that you use DNS validation. </p>
            subject_alternative_names: <p>Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. For example, add the name www.example.net to a certificate for which the <code>DomainName</code> field is www.example.com if users can reach your site by using either name. The maximum number of domain names that you can add to an ACM certificate is 100. However, the initial quota is 10 domain names. If you need more than 10 names, you must request a quota increase. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html">Quotas</a>.</p> <p> The maximum length of a SAN DNS name is 253 octets. The name is made up of multiple labels separated by periods. No label can be longer than 63 octets. Consider the following examples: </p> <ul> <li> <p> <code>(63 octets).(63 octets).(63 octets).(61 octets)</code> is legal because the total length is 253 octets (63+1+63+1+63+1+61) and no label exceeds 63 octets.</p> </li> <li> <p> <code>(64 octets).(63 octets).(63 octets).(61 octets)</code> is not legal because the total length exceeds 253 octets (64+1+63+1+63+1+61) and the first label exceeds 63 octets.</p> </li> <li> <p> <code>(63 octets).(63 octets).(63 octets).(62 octets)</code> is not legal because the total length of the DNS name (63+1+63+1+63+1+62) exceeds 253 octets.</p> </li> </ul>
            idempotency_token: <p>Customer chosen string that can be used to distinguish between calls to <code>RequestCertificate</code>. Idempotency tokens time out after one hour. Therefore, if you call <code>RequestCertificate</code> multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.</p>
            domain_validation_options: <p>The domain name that you want ACM to use to send you emails so that you can validate domain ownership.</p>
            options: <p>You can use this parameter to specify whether to export your certificate.</p> <p>Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency">Certificate Transparency Logging</a>.</p> <p>You can export public ACM certificates to use with Amazon Web Services services as well as outside the Amazon Web Services Cloud. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html">Certificate Manager exportable public certificate</a>.</p>
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate. If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html">Amazon Web Services Private Certificate Authority</a> user guide. The ARN must have the following form: </p> <p> <code>arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012</code> </p>
            tags: <p>One or more resource tags to associate with the certificate.</p>
            key_algorithm: <p>Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. RSA is the default key algorithm for ACM certificates. Elliptic Curve Digital Signature Algorithm (ECDSA) keys are smaller, offering security comparable to RSA keys but with greater computing efficiency. However, ECDSA is not supported by all network clients. Some Amazon Web Services services may require RSA keys, or only support ECDSA keys of a particular size, while others allow the use of either RSA and ECDSA keys to ensure that compatibility is not broken. Check the requirements for the Amazon Web Services service where you plan to deploy your certificate. For more information about selecting an algorithm, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-characteristics.html#algorithms-term">Key algorithms</a>.</p> <note> <p>Algorithms supported for an ACM certificate request include: </p> <ul> <li> <p> <code>RSA_2048</code> </p> </li> <li> <p> <code>EC_prime256v1</code> </p> </li> <li> <p> <code>EC_secp384r1</code> </p> </li> </ul> <p>Other listed algorithms are for imported certificates only. </p> </note> <note> <p>When you request a private PKI certificate signed by a CA from Amazon Web Services Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</p> </note> <p>Default: RSA_2048</p>
            managed_by: <p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.invalid_domain_validation_options_exception.InvalidDomainValidationOptionsException: <p>One or more values in the <a>DomainValidationOption</a> structure is incorrect.</p>
            capo_acm.errors.invalid_parameter_exception.InvalidParameterException: <p>An input parameter was invalid.</p>
            capo_acm.errors.invalid_tag_exception.InvalidTagException: <p>One or both of the values that make up the key-value pair is not valid. For example, you cannot specify a tag value that begins with <code>aws:</code>.</p>
            capo_acm.errors.limit_exceeded_exception.LimitExceededException: <p>An ACM quota has been exceeded.</p>
            capo_acm.errors.tag_policy_exception.TagPolicyException: <p>A specified tag did not comply with an existing tag policy and was rejected.</p>
            capo_acm.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains too many tags. Try the request again with fewer tags.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.request_certificate_request.RequestCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.request_certificate_response.RequestCertificateResponse"
        ]:
            import capo_acm._operations.certificate_manager.request_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.request_certificate.async_request_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.request_certificate_request.RequestCertificateRequest = {
            "domain_name": domain_name
        }
        if validation_method is not None:
            input_["validation_method"] = validation_method
        if subject_alternative_names is not None:
            input_["subject_alternative_names"] = subject_alternative_names
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if domain_validation_options is not None:
            input_["domain_validation_options"] = domain_validation_options
        if options is not None:
            input_["options"] = options
        if certificate_authority_arn is not None:
            input_["certificate_authority_arn"] = certificate_authority_arn
        if tags is not None:
            input_["tags"] = tags
        if key_algorithm is not None:
            input_["key_algorithm"] = key_algorithm
        if managed_by is not None:
            input_["managed_by"] = managed_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resend_validation_email(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        domain: "capo_acm.types.domain_name_string.DomainNameString",
        validation_domain: "capo_acm.types.domain_name_string.DomainNameString",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Resends the email that requests domain ownership validation. The domain owner or an authorized representative must approve the ACM certificate before it can be issued. The certificate can be approved by clicking a link in the mail to navigate to the Amazon certificate approval website and then clicking <b>I Approve</b>. However, the validation email can be blocked by spam filters. Therefore, if you do not receive the original mail, you can request that the mail be resent within 72 hours of requesting the ACM certificate. If more than 72 hours have elapsed since your original request or since your last attempt to resend validation mail, you must request a new certificate. For more information about setting up your contact email addresses, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/setup-email.html">Configure Email for your Domain</a>. </p>

        Args:
            certificate_arn: <p>String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the <a>RequestCertificate</a> action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request. The ARN must be of the form: </p> <p> <code>arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p>
            domain: <p>The fully qualified domain name (FQDN) of the certificate that needs to be validated.</p>
            validation_domain: <p>The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the <code>Domain</code> value or a superdomain of the <code>Domain</code> value. For example, if you requested a certificate for <code>site.subdomain.example.com</code> and specify a <b>ValidationDomain</b> of <code>subdomain.example.com</code>, ACM sends email to the the following five addresses:</p> <ul> <li> <p>admin@subdomain.example.com</p> </li> <li> <p>administrator@subdomain.example.com</p> </li> <li> <p>hostmaster@subdomain.example.com</p> </li> <li> <p>postmaster@subdomain.example.com</p> </li> <li> <p>webmaster@subdomain.example.com</p> </li> </ul>

        Raises:
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.invalid_domain_validation_options_exception.InvalidDomainValidationOptionsException: <p>One or more values in the <a>DomainValidationOption</a> structure is incorrect.</p>
            capo_acm.errors.invalid_state_exception.InvalidStateException: <p>Processing has reached an invalid state.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.resend_validation_email_request.ResendValidationEmailRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.resend_validation_email

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.resend_validation_email.async_resend_validation_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.resend_validation_email_request.ResendValidationEmailRequest = {
            "certificate_arn": certificate_arn,
            "domain": domain,
            "validation_domain": validation_domain,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_acme_account(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        account_url: str,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Revokes an ACME account, preventing it from requesting or revoking certificates. This operation is irreversible.</p>

        Args:
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint.</p>
            account_url: <p>The URL of the ACME account to revoke.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.revoke_acme_account_request.RevokeAcmeAccountRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.revoke_acme_account

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.revoke_acme_account.async_revoke_acme_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.revoke_acme_account_request.RevokeAcmeAccountRequest = {
            "acme_endpoint_arn": acme_endpoint_arn,
            "account_url": account_url,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_acme_external_account_binding(
        self,
        acme_external_account_binding_arn: "capo_acm.types.acme_external_account_binding_arn.AcmeExternalAccountBindingArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Revokes an external account binding, preventing new ACME accounts from being registered using this binding. Existing ACME accounts that were previously registered using the binding are not affected and must be revoked separately.</p>

        Args:
            acme_external_account_binding_arn: <p>The Amazon Resource Name (ARN) of the ACME external account binding to revoke.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.revoke_acme_external_account_binding_request.RevokeAcmeExternalAccountBindingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.revoke_acme_external_account_binding

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.revoke_acme_external_account_binding.async_revoke_acme_external_account_binding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.revoke_acme_external_account_binding_request.RevokeAcmeExternalAccountBindingRequest = {
            "acme_external_account_binding_arn": acme_external_account_binding_arn
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
        certificate_arn: "capo_acm.types.arn.Arn",
        revocation_reason: "capo_acm.types.revocation_reason.RevocationReason",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> "capo_acm.types.revoke_certificate_response.RevokeCertificateResponse":
        """<p>Revokes a public ACM certificate. You can only revoke certificates that have been previously exported.</p> <important> <p>Once a certificate is revoked, you cannot reuse the certificate. Revoking a certificate is permanent.</p> </important>

        Args:
            certificate_arn: <p>The Amazon Resource Name (ARN) of the public or private certificate that will be revoked. The ARN must have the following form: </p> <p> <code>arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012</code> </p>
            revocation_reason: <p>Specifies why you revoked the certificate.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.resource_in_use_exception.ResourceInUseException: <p>The certificate is in use by another Amazon Web Services service in the caller's account. Remove the association and try again.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.revoke_certificate_request.RevokeCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.revoke_certificate_response.RevokeCertificateResponse"
        ]:
            import capo_acm._operations.certificate_manager.revoke_certificate

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.revoke_certificate.async_revoke_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.revoke_certificate_request.RevokeCertificateRequest = {
            "certificate_arn": certificate_arn,
            "revocation_reason": revocation_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_certificates(
        self,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        filter_statement: Optional[
            "capo_acm.types.certificate_filter_statement.CertificateFilterStatement"
        ] = None,
        max_results: Optional[
            "capo_acm.types.search_max_results.SearchMaxResults"
        ] = None,
        next_token: Optional["capo_acm.types.next_token.NextToken"] = None,
        sort_by: Optional[
            "capo_acm.types.search_certificates_sort_by.SearchCertificatesSortBy"
        ] = None,
        sort_order: Optional[
            "capo_acm.types.search_certificates_sort_order.SearchCertificatesSortOrder"
        ] = None,
    ) -> "capo_acm.types.search_certificates_response.SearchCertificatesResponse":
        """<p>Retrieves a list of certificates matching search criteria. You can filter certificates by X.509 attributes and ACM specific properties like certificate status, type and renewal eligibility. This operation provides more flexible filtering than <a>ListCertificates</a> by supporting complex filter statements.</p>

        Args:
            filter_statement: <p>A filter statement that defines the search criteria. You can combine multiple filters using AND, OR, and NOT logical operators to create complex queries.</p>
            max_results: <p>The maximum number of results to return in the response. Default is 100.</p>
            next_token: <p>Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the response you just received.</p>
            sort_by: <p>Specifies the field to sort results by. Valid values are CREATED_AT, NOT_AFTER, STATUS, RENEWAL_STATUS, EXPORTED, IN_USE, NOT_BEFORE, KEY_ALGORITHM, TYPE, CERTIFICATE_ARN, COMMON_NAME, REVOKED_AT, RENEWAL_ELIGIBILITY, ISSUED_AT, MANAGED_BY, EXPORT_OPTION, VALIDATION_METHOD, and IMPORTED_AT.</p>
            sort_order: <p>Specifies the order of sorted results. Valid values are ASCENDING or DESCENDING.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.search_certificates_request.SearchCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_acm.types.search_certificates_response.SearchCertificatesResponse"
        ]:
            import capo_acm._operations.certificate_manager.search_certificates

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.search_certificates.async_search_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.search_certificates_request.SearchCertificatesRequest = {}
        if filter_statement is not None:
            input_["filter_statement"] = filter_statement
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_certificates(
        self,
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        filter_statement: Optional[
            "capo_acm.types.certificate_filter_statement.CertificateFilterStatement"
        ] = None,
        max_results: Optional[
            "capo_acm.types.search_max_results.SearchMaxResults"
        ] = None,
        next_token: Optional["capo_acm.types.next_token.NextToken"] = None,
        sort_by: Optional[
            "capo_acm.types.search_certificates_sort_by.SearchCertificatesSortBy"
        ] = None,
        sort_order: Optional[
            "capo_acm.types.search_certificates_sort_order.SearchCertificatesSortOrder"
        ] = None,
    ) -> "AsyncIterator[capo_acm.types.certificate_search_result.CertificateSearchResult]":
        _token = next_token
        while True:
            _response = await self.search_certificates(
                config_overrides=config_overrides,
                filter_statement=filter_statement,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: "capo_acm.types.arn.Arn",
        tags: "capo_acm.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Adds one or more tags to an ACM resource. Tags are labels that you can use to identify and organize your Amazon Web Services resources. Each tag consists of a <code>key</code> and an optional <code>value</code>.</p> <note> <p>Use this action for all ACM resource types except the <code>certificate</code> resource type. For certificate resources, use <a>AddTagsToCertificate</a> instead.</p> </note> <p>To remove one or more tags, use the <a>UntagResource</a> action. To view all of the tags that have been applied to a resource, use the <a>ListTagsForResource</a> action.</p>

        Args:
            resource_arn: <p>The ARN of the ACM resource to which the tag is to be applied.</p>
            tags: <p>The key-value pair that defines the tag to apply.</p>

        Raises:
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.tag_resource

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_acm.types.arn.Arn",
        tag_keys: "capo_acm.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags from an ACM resource.</p> <note> <p>Use this action for all ACM resource types except the <code>certificate</code> resource type. For certificate resources, use <a>RemoveTagsFromCertificate</a> instead.</p> </note> <p>To add one or more tags, use the <a>TagResource</a> action. To view all of the tags that have been applied to a resource, use the <a>ListTagsForResource</a> action.</p>

        Args:
            resource_arn: <p>The ARN of the ACM resource from which the tag is to be removed.</p>
            tag_keys: <p>The key of each tag to remove.</p>

        Raises:
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.untag_resource

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_acme_domain_validation(
        self,
        acme_domain_validation_arn: "capo_acm.types.acme_domain_validation_arn.AcmeDomainValidationArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        prevalidation_options: Optional[
            "capo_acm.types.prevalidation_options.PrevalidationOptions"
        ] = None,
    ) -> None:
        """<p>Updates the prevalidation configuration of an existing domain validation.</p>

        Args:
            acme_domain_validation_arn: <p>The Amazon Resource Name (ARN) of the ACME domain validation to update.</p>
            prevalidation_options: <p>The updated prevalidation options.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.update_acme_domain_validation_request.UpdateAcmeDomainValidationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.update_acme_domain_validation

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.update_acme_domain_validation.async_update_acme_domain_validation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.update_acme_domain_validation_request.UpdateAcmeDomainValidationRequest = {
            "acme_domain_validation_arn": acme_domain_validation_arn
        }
        if prevalidation_options is not None:
            input_["prevalidation_options"] = prevalidation_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_acme_endpoint(
        self,
        acme_endpoint_arn: "capo_acm.types.acme_endpoint_arn.AcmeEndpointArn",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
        authorization_behavior: Optional[
            "capo_acm.types.acme_authorization_behavior.AcmeAuthorizationBehavior"
        ] = None,
        contact: Optional["capo_acm.types.acme_contact.AcmeContact"] = None,
        certificate_authority: Optional[
            "capo_acm.types.certificate_authority.CertificateAuthority"
        ] = None,
    ) -> None:
        """<p>Updates the configuration of an existing ACME endpoint. You can change the authorization behavior, contact requirement, or certificate authority settings.</p>

        Args:
            acme_endpoint_arn: <p>The Amazon Resource Name (ARN) of the ACME endpoint to update.</p>
            authorization_behavior: <p>The updated authorization behavior.</p>
            contact: <p>The updated contact requirement.</p>
            certificate_authority: <p>The updated certificate authority configuration.</p>

        Raises:
            capo_acm.errors.access_denied_exception.AccessDeniedException: <p>You do not have access required to perform this action.</p>
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded a quota.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.update_acme_endpoint_request.UpdateAcmeEndpointRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.update_acme_endpoint

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.update_acme_endpoint.async_update_acme_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.update_acme_endpoint_request.UpdateAcmeEndpointRequest = {
            "acme_endpoint_arn": acme_endpoint_arn
        }
        if authorization_behavior is not None:
            input_["authorization_behavior"] = authorization_behavior
        if contact is not None:
            input_["contact"] = contact
        if certificate_authority is not None:
            input_["certificate_authority"] = certificate_authority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_certificate_options(
        self,
        certificate_arn: "capo_acm.types.arn.Arn",
        options: "capo_acm.types.certificate_options.CertificateOptions",
        *,
        config_overrides: Optional[AsyncACMClientConfig] = None,
    ) -> None:
        """<p>Updates certificate options. You can use this operation to change the domain validation method or specify whether to export your certificate. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/email-to-dns-migration.html">Migrate from email to DNS validation</a> and <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html">Certificate Manager Exportable Managed Certificates</a>.</p>

        Args:
            certificate_arn: <p>ARN of the requested certificate to update. This must be of the form:</p> <p> <code>arn:aws:acm:us-east-1:<i>account</i>:certificate/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            options: <p>Use to update the options for your certificate. Currently, you can change the domain validation method or specify whether to export your certificate. For more information about migrating from email to DNS validation, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/email-to-dns-migration.html">Migrate from email to DNS validation</a>.</p>

        Raises:
            capo_acm.errors.conflict_exception.ConflictException: <p>You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.</p>
            capo_acm.errors.invalid_arn_exception.InvalidArnException: <p>The requested Amazon Resource Name (ARN) does not refer to an existing resource.</p>
            capo_acm.errors.invalid_state_exception.InvalidStateException: <p>Processing has reached an invalid state.</p>
            capo_acm.errors.limit_exceeded_exception.LimitExceededException: <p>An ACM quota has been exceeded.</p>
            capo_acm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified certificate cannot be found in the caller's account or the caller's account cannot be found.</p>
            capo_acm.errors.validation_exception.ValidationException: <p>The supplied input failed to satisfy constraints of an Amazon Web Services service.</p>
            capo_acm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_acm.types.update_certificate_options_request.UpdateCertificateOptionsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_acm._operations.certificate_manager.update_certificate_options

            (
                output,
                http_response,
            ) = await capo_acm._operations.certificate_manager.update_certificate_options.async_update_certificate_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_acm.types.update_certificate_options_request.UpdateCertificateOptionsRequest = {
            "certificate_arn": certificate_arn,
            "options": options,
        }

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
