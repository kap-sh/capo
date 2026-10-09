"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PcaConnectorAd``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pca_connector_ad._auth._signers
import capo_pca_connector_ad._auth._sigv4
from capo_pca_connector_ad._auth._identity import Credentials
from capo_pca_connector_ad._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pca_connector_ad._auth._zapros_handler import AuthMiddleware
from capo_pca_connector_ad._pagination import resolve_path as _resolve_path
from capo_pca_connector_ad._resources.pca_connector_ad.connector_resource import (
    AsyncConnectorResource,
)
from capo_pca_connector_ad._resources.pca_connector_ad.directory_registration_resource import (
    AsyncDirectoryRegistrationResource,
)
from capo_pca_connector_ad._resources.pca_connector_ad.service_principal_name_resource import (
    AsyncServicePrincipalNameResource,
)
from capo_pca_connector_ad._resources.pca_connector_ad.template_group_access_control_entry_resource import (
    AsyncTemplateGroupAccessControlEntryResource,
)
from capo_pca_connector_ad._resources.pca_connector_ad.template_resource import (
    AsyncTemplateResource,
)
from capo_pca_connector_ad._services._aws_config import aaws_config
from capo_pca_connector_ad._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.access_control_entry_summary
    import capo_pca_connector_ad.types.access_rights
    import capo_pca_connector_ad.types.certificate_authority_arn
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.connector_summary
    import capo_pca_connector_ad.types.create_connector_request
    import capo_pca_connector_ad.types.create_connector_response
    import capo_pca_connector_ad.types.create_directory_registration_request
    import capo_pca_connector_ad.types.create_directory_registration_response
    import capo_pca_connector_ad.types.create_service_principal_name_request
    import capo_pca_connector_ad.types.create_template_group_access_control_entry_request
    import capo_pca_connector_ad.types.create_template_request
    import capo_pca_connector_ad.types.create_template_response
    import capo_pca_connector_ad.types.delete_connector_request
    import capo_pca_connector_ad.types.delete_directory_registration_request
    import capo_pca_connector_ad.types.delete_service_principal_name_request
    import capo_pca_connector_ad.types.delete_template_group_access_control_entry_request
    import capo_pca_connector_ad.types.delete_template_request
    import capo_pca_connector_ad.types.directory_id
    import capo_pca_connector_ad.types.directory_registration_arn
    import capo_pca_connector_ad.types.directory_registration_summary
    import capo_pca_connector_ad.types.display_name
    import capo_pca_connector_ad.types.get_connector_request
    import capo_pca_connector_ad.types.get_connector_response
    import capo_pca_connector_ad.types.get_directory_registration_request
    import capo_pca_connector_ad.types.get_directory_registration_response
    import capo_pca_connector_ad.types.get_service_principal_name_request
    import capo_pca_connector_ad.types.get_service_principal_name_response
    import capo_pca_connector_ad.types.get_template_group_access_control_entry_request
    import capo_pca_connector_ad.types.get_template_group_access_control_entry_response
    import capo_pca_connector_ad.types.get_template_request
    import capo_pca_connector_ad.types.get_template_response
    import capo_pca_connector_ad.types.group_security_identifier
    import capo_pca_connector_ad.types.list_connectors_request
    import capo_pca_connector_ad.types.list_connectors_response
    import capo_pca_connector_ad.types.list_directory_registrations_request
    import capo_pca_connector_ad.types.list_directory_registrations_response
    import capo_pca_connector_ad.types.list_service_principal_names_request
    import capo_pca_connector_ad.types.list_service_principal_names_response
    import capo_pca_connector_ad.types.list_tags_for_resource_request
    import capo_pca_connector_ad.types.list_tags_for_resource_response
    import capo_pca_connector_ad.types.list_template_group_access_control_entries_request
    import capo_pca_connector_ad.types.list_template_group_access_control_entries_response
    import capo_pca_connector_ad.types.list_templates_request
    import capo_pca_connector_ad.types.list_templates_response
    import capo_pca_connector_ad.types.max_results
    import capo_pca_connector_ad.types.next_token
    import capo_pca_connector_ad.types.service_principal_name_summary
    import capo_pca_connector_ad.types.tag_key_list
    import capo_pca_connector_ad.types.tag_resource_request
    import capo_pca_connector_ad.types.tags
    import capo_pca_connector_ad.types.template_arn
    import capo_pca_connector_ad.types.template_definition
    import capo_pca_connector_ad.types.template_name
    import capo_pca_connector_ad.types.template_summary
    import capo_pca_connector_ad.types.untag_resource_request
    import capo_pca_connector_ad.types.update_template_group_access_control_entry_request
    import capo_pca_connector_ad.types.update_template_request
    import capo_pca_connector_ad.types.vpc_information


class AsyncPcaConnectorAdClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPcaConnectorAdClient:
    """A client for the ``PcaConnectorAd`` service.

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
        self._config = AsyncPcaConnectorAdClientConfig(
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

        # resources
        self.connector_resource = AsyncConnectorResource(self)
        self.directory_registration_resource = AsyncDirectoryRegistrationResource(self)
        self.service_principal_name_resource = AsyncServicePrincipalNameResource(self)
        self.template_group_access_control_entry_resource = (
            AsyncTemplateGroupAccessControlEntryResource(self)
        )
        self.template_resource = AsyncTemplateResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPcaConnectorAdClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags, if any, that are associated with your resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that was returned when you created the resource. </p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_pca_connector_ad.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Adds one or more tags to your resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that was returned when you created the resource. </p>
            tags: <p>Metadata assigned to a directory registration consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.tag_resource

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_pca_connector_ad.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags from your resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that was returned when you created the resource.</p>
            tag_keys: <p>Specifies a list of tag keys that you want to remove from the specified resources.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.untag_resource

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_connector(
        self,
        directory_id: "capo_pca_connector_ad.types.directory_id.DirectoryId",
        certificate_authority_arn: "capo_pca_connector_ad.types.certificate_authority_arn.CertificateAuthorityArn",
        vpc_information: "capo_pca_connector_ad.types.vpc_information.VpcInformation",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_ad.types.tags.Tags"] = None,
    ) -> (
        "capo_pca_connector_ad.types.create_connector_response.CreateConnectorResponse"
    ):
        """<p>Creates a connector between Amazon Web Services Private CA and an Active Directory. You must specify the private CA, directory ID, and security groups.</p>

        Args:
            directory_id: <p>The identifier of the Active Directory.</p>
            certificate_authority_arn: <p> The Amazon Resource Name (ARN) of the certificate authority being used.</p>
            vpc_information: <p>Information about your VPC and security groups used with the connector.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a connector consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.create_connector_response.CreateConnectorResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_connector

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_connector_request.CreateConnectorRequest = {
            "directory_id": directory_id,
            "certificate_authority_arn": certificate_authority_arn,
            "vpc_information": vpc_information,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connector(
        self,
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_connector_response.GetConnectorResponse":
        """<p>Lists information about your connector. You specify the connector on input by its ARN (Amazon Resource Name). </p>

        Args:
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_connector_request.GetConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_connector_response.GetConnectorResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_connector

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_connector.async_get_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_connector_request.GetConnectorRequest = {
            "connector_arn": connector_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector(
        self,
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a connector for Active Directory. You must provide the Amazon Resource Name (ARN) of the connector that you want to delete. You can find the ARN by calling the <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors</a> action. Deleting a connector does not deregister your directory with Amazon Web Services Private CA. You can deregister your directory by calling the <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration</a> action.</p>

        Args:
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_connector

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_arn": connector_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_connectors_response.ListConnectorsResponse":
        """<p>Lists the connectors that you created by using the <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector</a> action.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_connectors

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_connectors_request.ListConnectorsRequest = {}
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

    async def iter_list_connectors(
        self,
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[capo_pca_connector_ad.types.connector_summary.ConnectorSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_connectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_directory_registration(
        self,
        directory_id: "capo_pca_connector_ad.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_ad.types.create_directory_registration_response.CreateDirectoryRegistrationResponse":
        """<p>Creates a directory registration that authorizes communication between Amazon Web Services Private CA and an Active Directory</p>

        Args:
            directory_id: <p> The identifier of the Active Directory.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a directory registration consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_directory_registration_request.CreateDirectoryRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.create_directory_registration_response.CreateDirectoryRegistrationResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_directory_registration

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_directory_registration.async_create_directory_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_directory_registration_request.CreateDirectoryRegistrationRequest = {
            "directory_id": directory_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_directory_registration(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_directory_registration_response.GetDirectoryRegistrationResponse":
        """<p>A structure that contains information about your directory registration.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_directory_registration_request.GetDirectoryRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_directory_registration_response.GetDirectoryRegistrationResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_directory_registration

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_directory_registration.async_get_directory_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_directory_registration_request.GetDirectoryRegistrationRequest = {
            "directory_registration_arn": directory_registration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_directory_registration(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a directory registration. Deleting a directory registration deauthorizes Amazon Web Services Private CA with the directory. </p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_directory_registration_request.DeleteDirectoryRegistrationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_directory_registration

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_directory_registration.async_delete_directory_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_directory_registration_request.DeleteDirectoryRegistrationRequest = {
            "directory_registration_arn": directory_registration_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_directory_registrations(
        self,
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_directory_registrations_response.ListDirectoryRegistrationsResponse":
        """<p>Lists the directory registrations that you created by using the <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration</a> action.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_directory_registrations_request.ListDirectoryRegistrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_directory_registrations_response.ListDirectoryRegistrationsResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_directory_registrations

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_directory_registrations.async_list_directory_registrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_directory_registrations_request.ListDirectoryRegistrationsRequest = {}
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

    async def iter_list_directory_registrations(
        self,
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_pca_connector_ad.types.directory_registration_summary.DirectoryRegistrationSummary]":
        _token = next_token
        while True:
            _response = await self.list_directory_registrations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("directory_registrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_service_principal_name(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Creates a service principal name (SPN) for the service account in Active Directory. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>
            client_token: <p>Idempotency token.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name.async_create_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_principal_name(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse":
        """<p>Lists the service principal name that the connector uses to authenticate with Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name.async_get_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service_principal_name(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes the service principal name (SPN) used by a connector to authenticate with your Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name.async_delete_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest = {
            "directory_registration_arn": directory_registration_arn,
            "connector_arn": connector_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_service_principal_names(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse":
        """<p>Lists the service principal names that the connector uses to authenticate with Active Directory.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names.async_list_service_principal_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest = {
            "directory_registration_arn": directory_registration_arn
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

    async def iter_list_service_principal_names(
        self,
        directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_pca_connector_ad.types.service_principal_name_summary.ServicePrincipalNameSummary]":
        _token = next_token
        while True:
            _response = await self.list_service_principal_names(
                directory_registration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_principal_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_template_group_access_control_entry(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        group_display_name: "capo_pca_connector_ad.types.display_name.DisplayName",
        access_rights: "capo_pca_connector_ad.types.access_rights.AccessRights",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Create a group access control entry. Allow or deny Active Directory groups from enrolling and/or autoenrolling with the template based on the group security identifiers (SIDs).</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>
            group_display_name: <p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>
            access_rights: <p> Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>
            client_token: <p>Idempotency token.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_template_group_access_control_entry_request.CreateTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_template_group_access_control_entry.async_create_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_template_group_access_control_entry_request.CreateTemplateGroupAccessControlEntryRequest = {
            "template_arn": template_arn,
            "group_security_identifier": group_security_identifier,
            "group_display_name": group_display_name,
            "access_rights": access_rights,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_template_group_access_control_entry(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_template_group_access_control_entry_response.GetTemplateGroupAccessControlEntryResponse":
        """<p>Retrieves the group access control entries for a template.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_template_group_access_control_entry_request.GetTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_template_group_access_control_entry_response.GetTemplateGroupAccessControlEntryResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_template_group_access_control_entry.async_get_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_template_group_access_control_entry_request.GetTemplateGroupAccessControlEntryRequest = {
            "template_arn": template_arn,
            "group_security_identifier": group_security_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_template_group_access_control_entry(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        group_display_name: Optional[
            "capo_pca_connector_ad.types.display_name.DisplayName"
        ] = None,
        access_rights: Optional[
            "capo_pca_connector_ad.types.access_rights.AccessRights"
        ] = None,
    ) -> None:
        """<p>Update a group access control entry you created using <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html">CreateTemplateGroupAccessControlEntry</a>. </p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>
            group_display_name: <p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>
            access_rights: <p>Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.update_template_group_access_control_entry_request.UpdateTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.update_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.update_template_group_access_control_entry.async_update_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.update_template_group_access_control_entry_request.UpdateTemplateGroupAccessControlEntryRequest = {
            "template_arn": template_arn,
            "group_security_identifier": group_security_identifier,
        }
        if group_display_name is not None:
            input_["group_display_name"] = group_display_name
        if access_rights is not None:
            input_["access_rights"] = access_rights

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_template_group_access_control_entry(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a group access control entry.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_template_group_access_control_entry_request.DeleteTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_template_group_access_control_entry.async_delete_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_template_group_access_control_entry_request.DeleteTemplateGroupAccessControlEntryRequest = {
            "template_arn": template_arn,
            "group_security_identifier": group_security_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_template_group_access_control_entries(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_template_group_access_control_entries_response.ListTemplateGroupAccessControlEntriesResponse":
        """<p>Lists group access control entries you created. </p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_template_group_access_control_entries_request.ListTemplateGroupAccessControlEntriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_template_group_access_control_entries_response.ListTemplateGroupAccessControlEntriesResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_template_group_access_control_entries

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_template_group_access_control_entries.async_list_template_group_access_control_entries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_template_group_access_control_entries_request.ListTemplateGroupAccessControlEntriesRequest = {
            "template_arn": template_arn
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

    async def iter_list_template_group_access_control_entries(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_pca_connector_ad.types.access_control_entry_summary.AccessControlEntrySummary]":
        _token = next_token
        while True:
            _response = await self.list_template_group_access_control_entries(
                template_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("access_control_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_template(
        self,
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        name: "capo_pca_connector_ad.types.template_name.TemplateName",
        definition: "capo_pca_connector_ad.types.template_definition.TemplateDefinition",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_ad.types.create_template_response.CreateTemplateResponse":
        """<p>Creates an Active Directory compatible certificate template. The connectors issues certificates using these templates based on the requester’s Active Directory group membership.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>
            name: <p>Name of the template. The template name must be unique.</p>
            definition: <p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a template consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_template_request.CreateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_template.async_create_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_template_request.CreateTemplateRequest = {
            "connector_arn": connector_arn,
            "name": name,
            "definition": definition,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_template(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_template_response.GetTemplateResponse":
        """<p>Retrieves a certificate template that the connector uses to issue certificates from a private CA.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_template_request.GetTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_template_response.GetTemplateResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_template.async_get_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_template_request.GetTemplateRequest = {
            "template_arn": template_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_template(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        definition: Optional[
            "capo_pca_connector_ad.types.template_definition.TemplateDefinition"
        ] = None,
        reenroll_all_certificate_holders: Optional[bool] = None,
    ) -> None:
        """<p>Update template configuration to define the information included in certificates.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>
            definition: <p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>
            reenroll_all_certificate_holders: <p>This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.update_template_request.UpdateTemplateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.update_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.update_template.async_update_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.update_template_request.UpdateTemplateRequest = {
            "template_arn": template_arn
        }
        if definition is not None:
            input_["definition"] = definition
        if reenroll_all_certificate_holders is not None:
            input_["reenroll_all_certificate_holders"] = (
                reenroll_all_certificate_holders
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_template(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a template. Certificates issued using the template are still valid until they are revoked or expired.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_template_request.DeleteTemplateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_template.async_delete_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_template_request.DeleteTemplateRequest = {
            "template_arn": template_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_templates(
        self,
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_templates_response.ListTemplatesResponse":
        """<p>Lists the templates, if any, that are associated with a connector.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_templates_request.ListTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_templates

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_templates_request.ListTemplatesRequest = {
            "connector_arn": connector_arn
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

    async def iter_list_templates(
        self,
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_pca_connector_ad.types.template_summary.TemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_templates(
                connector_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
