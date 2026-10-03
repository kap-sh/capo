"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ResourceExplorer``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_resource_explorer_2._auth._signers
import capo_resource_explorer_2._auth._sigv4
from capo_resource_explorer_2._auth._identity import Credentials
from capo_resource_explorer_2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_resource_explorer_2._auth._zapros_handler import AuthMiddleware
from capo_resource_explorer_2._pagination import resolve_path as _resolve_path
from capo_resource_explorer_2._resources.resource_explorer.cfn_index import (
    AsyncCfnIndex,
)
from capo_resource_explorer_2._resources.resource_explorer.cfn_view import AsyncCfnView
from capo_resource_explorer_2._resources.resource_explorer.default_view_association import (
    AsyncDefaultViewAssociation,
)
from capo_resource_explorer_2._services._aws_config import aaws_config
from capo_resource_explorer_2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.account_id_list
    import capo_resource_explorer_2.types.associate_default_view_input
    import capo_resource_explorer_2.types.associate_default_view_output
    import capo_resource_explorer_2.types.batch_get_view_input
    import capo_resource_explorer_2.types.batch_get_view_output
    import capo_resource_explorer_2.types.create_index_input
    import capo_resource_explorer_2.types.create_index_output
    import capo_resource_explorer_2.types.create_resource_explorer_setup_input
    import capo_resource_explorer_2.types.create_resource_explorer_setup_output
    import capo_resource_explorer_2.types.create_view_input
    import capo_resource_explorer_2.types.create_view_output
    import capo_resource_explorer_2.types.delete_index_input
    import capo_resource_explorer_2.types.delete_index_output
    import capo_resource_explorer_2.types.delete_resource_explorer_setup_input
    import capo_resource_explorer_2.types.delete_resource_explorer_setup_output
    import capo_resource_explorer_2.types.delete_view_input
    import capo_resource_explorer_2.types.delete_view_output
    import capo_resource_explorer_2.types.get_account_level_service_configuration_output
    import capo_resource_explorer_2.types.get_default_view_output
    import capo_resource_explorer_2.types.get_index_output
    import capo_resource_explorer_2.types.get_managed_view_input
    import capo_resource_explorer_2.types.get_managed_view_output
    import capo_resource_explorer_2.types.get_resource_explorer_setup_input
    import capo_resource_explorer_2.types.get_resource_explorer_setup_output
    import capo_resource_explorer_2.types.get_service_index_output
    import capo_resource_explorer_2.types.get_service_view_input
    import capo_resource_explorer_2.types.get_service_view_output
    import capo_resource_explorer_2.types.get_view_input
    import capo_resource_explorer_2.types.get_view_output
    import capo_resource_explorer_2.types.included_property_list
    import capo_resource_explorer_2.types.index
    import capo_resource_explorer_2.types.index_type
    import capo_resource_explorer_2.types.list_indexes_for_members_input
    import capo_resource_explorer_2.types.list_indexes_for_members_output
    import capo_resource_explorer_2.types.list_indexes_input
    import capo_resource_explorer_2.types.list_indexes_output
    import capo_resource_explorer_2.types.list_managed_views_input
    import capo_resource_explorer_2.types.list_managed_views_output
    import capo_resource_explorer_2.types.list_resources_input
    import capo_resource_explorer_2.types.list_resources_output
    import capo_resource_explorer_2.types.list_service_indexes_input
    import capo_resource_explorer_2.types.list_service_indexes_output
    import capo_resource_explorer_2.types.list_service_views_input
    import capo_resource_explorer_2.types.list_service_views_output
    import capo_resource_explorer_2.types.list_streaming_access_for_services_input
    import capo_resource_explorer_2.types.list_streaming_access_for_services_output
    import capo_resource_explorer_2.types.list_supported_resource_types_input
    import capo_resource_explorer_2.types.list_supported_resource_types_output
    import capo_resource_explorer_2.types.list_tags_for_resource_input
    import capo_resource_explorer_2.types.list_tags_for_resource_output
    import capo_resource_explorer_2.types.list_views_input
    import capo_resource_explorer_2.types.list_views_output
    import capo_resource_explorer_2.types.member_index
    import capo_resource_explorer_2.types.query_string
    import capo_resource_explorer_2.types.region_list
    import capo_resource_explorer_2.types.region_status
    import capo_resource_explorer_2.types.resource
    import capo_resource_explorer_2.types.search_filter
    import capo_resource_explorer_2.types.search_input
    import capo_resource_explorer_2.types.search_output
    import capo_resource_explorer_2.types.streaming_access_details
    import capo_resource_explorer_2.types.string_list
    import capo_resource_explorer_2.types.supported_resource_type
    import capo_resource_explorer_2.types.tag_map
    import capo_resource_explorer_2.types.tag_resource_input
    import capo_resource_explorer_2.types.tag_resource_output
    import capo_resource_explorer_2.types.untag_resource_input
    import capo_resource_explorer_2.types.untag_resource_output
    import capo_resource_explorer_2.types.update_index_type_input
    import capo_resource_explorer_2.types.update_index_type_output
    import capo_resource_explorer_2.types.update_view_input
    import capo_resource_explorer_2.types.update_view_output
    import capo_resource_explorer_2.types.view_arn_list
    import capo_resource_explorer_2.types.view_name


class AsyncResourceExplorer2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncResourceExplorer2Client:
    """A client for the ``ResourceExplorer2`` service.

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
        self._config = AsyncResourceExplorer2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.cfn_index = AsyncCfnIndex(self)
        self.cfn_view = AsyncCfnView(self)
        self.default_view_association = AsyncDefaultViewAssociation(self)

    def operation_options(
        self, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncResourceExplorer2ClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def batch_get_view(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        view_arns: Optional[
            "capo_resource_explorer_2.types.view_arn_list.ViewArnList"
        ] = None,
    ) -> "capo_resource_explorer_2.types.batch_get_view_output.BatchGetViewOutput":
        """<p>Retrieves details about a list of views.</p>

        Args:
            view_arns: <p>A list of <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource names (ARNs)</a> that identify the views you want details for.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.batch_get_view_input.BatchGetViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.batch_get_view_output.BatchGetViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.batch_get_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.batch_get_view.async_batch_get_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.batch_get_view_input.BatchGetViewInput = {}
        if view_arns is not None:
            input_["view_arns"] = view_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resource_explorer_setup(
        self,
        region_list: "capo_resource_explorer_2.types.region_list.RegionList",
        view_name: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        aggregator_regions: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
    ) -> "capo_resource_explorer_2.types.create_resource_explorer_setup_output.CreateResourceExplorerSetupOutput":
        """<p>Creates a Resource Explorer setup configuration across multiple Amazon Web Services Regions. This operation sets up indexes and views in the specified Regions. This operation can also be used to set an aggregator Region for cross-Region resource search.</p>

        Args:
            region_list: <p>A list of Amazon Web Services Regions where Resource Explorer should be configured. Each Region in the list will have a user-owned index created.</p>
            aggregator_regions: <p>A list of Amazon Web Services Regions that should be configured as aggregator Regions. Aggregator Regions receive replicated index information from all other Regions where there is a user-owned index.</p>
            view_name: <p>The name for the view to be created as part of the Resource Explorer setup. The view name must be unique within the Amazon Web Services account and Region.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.create_resource_explorer_setup_input.CreateResourceExplorerSetupInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.create_resource_explorer_setup_output.CreateResourceExplorerSetupOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.create_resource_explorer_setup

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.create_resource_explorer_setup.async_create_resource_explorer_setup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.create_resource_explorer_setup_input.CreateResourceExplorerSetupInput = {
            "region_list": region_list,
            "view_name": view_name,
        }
        if aggregator_regions is not None:
            input_["aggregator_regions"] = aggregator_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_explorer_setup(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        region_list: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        delete_in_all_regions: Optional[bool] = None,
    ) -> "capo_resource_explorer_2.types.delete_resource_explorer_setup_output.DeleteResourceExplorerSetupOutput":
        """<p>Deletes a Resource Explorer setup configuration. This operation removes indexes and views from the specified Regions or all Regions where Resource Explorer is configured.</p>

        Args:
            region_list: <p>A list of Amazon Web Services Regions from which to delete the Resource Explorer configuration. If not specified, the operation uses the <code>DeleteInAllRegions</code> parameter to determine scope.</p>
            delete_in_all_regions: <p>Specifies whether to delete Resource Explorer configuration from all Regions where it is currently enabled. If this parameter is set to <code>true</code>, a value for <code>RegionList</code> must not be provided. Otherwise, the operation fails with a <code>ValidationException</code> error.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.delete_resource_explorer_setup_input.DeleteResourceExplorerSetupInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.delete_resource_explorer_setup_output.DeleteResourceExplorerSetupOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.delete_resource_explorer_setup

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.delete_resource_explorer_setup.async_delete_resource_explorer_setup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.delete_resource_explorer_setup_input.DeleteResourceExplorerSetupInput = {}
        if region_list is not None:
            input_["region_list"] = region_list
        if delete_in_all_regions is not None:
            input_["delete_in_all_regions"] = delete_in_all_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_default_view(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> None:
        """<p>After you call this operation, the affected Amazon Web Services Region no longer has a default view. All <a>Search</a> operations in that Region must explicitly specify a view or the operation fails. You can configure a new default by calling the <a>AssociateDefaultView</a> operation.</p> <p>If an Amazon Web Services Region doesn't have a default view configured, then users must explicitly specify a view with every <code>Search</code> operation performed in that Region.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import capo_resource_explorer_2._operations.resource_explorer.disassociate_default_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.disassociate_default_view.async_disassociate_default_view(
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

    async def get_account_level_service_configuration(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> "capo_resource_explorer_2.types.get_account_level_service_configuration_output.GetAccountLevelServiceConfigurationOutput":
        """<p>Retrieves the status of your account's Amazon Web Services service access, and validates the service linked role required to access the multi-account search feature. Only the management account can invoke this API call. </p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_account_level_service_configuration_output.GetAccountLevelServiceConfigurationOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_account_level_service_configuration

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_account_level_service_configuration.async_get_account_level_service_configuration(
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

    async def get_default_view(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> "capo_resource_explorer_2.types.get_default_view_output.GetDefaultViewOutput":
        """<p>Retrieves the Amazon Resource Name (ARN) of the view that is the default for the Amazon Web Services Region in which you call this operation. You can then call <a>GetView</a> to retrieve the details of that view.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_default_view_output.GetDefaultViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_default_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_default_view.async_get_default_view(
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

    async def get_index(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> "capo_resource_explorer_2.types.get_index_output.GetIndexOutput":
        """<p>Retrieves details about the Amazon Web Services Resource Explorer index in the Amazon Web Services Region in which you invoked the operation.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_index_output.GetIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_index

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_index.async_get_index(
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

    async def get_managed_view(
        self,
        managed_view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.get_managed_view_output.GetManagedViewOutput":
        """<p>Retrieves details of the specified <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html">Amazon Web Services-managed view</a>. </p>

        Args:
            managed_view_arn: <p>The Amazon resource name (ARN) of the managed view.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.get_managed_view_input.GetManagedViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_managed_view_output.GetManagedViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_managed_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_managed_view.async_get_managed_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.get_managed_view_input.GetManagedViewInput = {
            "managed_view_arn": managed_view_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_explorer_setup(
        self,
        task_id: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.get_resource_explorer_setup_output.GetResourceExplorerSetupOutput":
        """<p>Retrieves the status and details of a Resource Explorer setup operation. This operation returns information about the progress of creating or deleting Resource Explorer configurations across Regions.</p>

        Args:
            task_id: <p>The unique identifier of the setup task to retrieve status information for. This ID is returned by <code>CreateResourceExplorerSetup</code> or <code>DeleteResourceExplorerSetup</code> operations.</p>
            max_results: <p>The maximum number of Region status results to return in a single response. Valid values are between <code>1</code> and <code>100</code>.</p>
            next_token: <p>The pagination token from a previous <code>GetResourceExplorerSetup</code> response. Use this token to retrieve the next set of results.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.get_resource_explorer_setup_input.GetResourceExplorerSetupInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_resource_explorer_setup_output.GetResourceExplorerSetupOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_resource_explorer_setup

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_resource_explorer_setup.async_get_resource_explorer_setup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.get_resource_explorer_setup_input.GetResourceExplorerSetupInput = {
            "task_id": task_id
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

    async def iter_get_resource_explorer_setup(
        self,
        task_id: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.region_status.RegionStatus]":
        _token = next_token
        while True:
            _response = await self.get_resource_explorer_setup(
                task_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("regions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_service_index(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> (
        "capo_resource_explorer_2.types.get_service_index_output.GetServiceIndexOutput"
    ):
        """<p>Retrieves information about the Resource Explorer index in the current Amazon Web Services Region. This operation returns the ARN and type of the index if one exists.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_service_index_output.GetServiceIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_service_index

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_service_index.async_get_service_index(
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

    async def get_service_view(
        self,
        service_view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.get_service_view_output.GetServiceViewOutput":
        """<p>Retrieves details about a specific Resource Explorer service view. This operation returns the configuration and properties of the specified view.</p>

        Args:
            service_view_arn: <p>The Amazon Resource Name (ARN) of the service view to retrieve details for.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.get_service_view_input.GetServiceViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_service_view_output.GetServiceViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_service_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_service_view.async_get_service_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.get_service_view_input.GetServiceViewInput = {
            "service_view_arn": service_view_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_indexes_for_members(
        self,
        account_id_list: "capo_resource_explorer_2.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_indexes_for_members_output.ListIndexesForMembersOutput":
        """<p>Retrieves a list of a member's indexes in all Amazon Web Services Regions that are currently collecting resource information for Amazon Web Services Resource Explorer. Only the management account or a delegated administrator with service access enabled can invoke this API call. </p>

        Args:
            account_id_list: <p>The account IDs will limit the output to only indexes from these accounts.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_indexes_for_members_input.ListIndexesForMembersInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_indexes_for_members_output.ListIndexesForMembersOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_indexes_for_members

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_indexes_for_members.async_list_indexes_for_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_indexes_for_members_input.ListIndexesForMembersInput = {
            "account_id_list": account_id_list
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

    async def iter_list_indexes_for_members(
        self,
        account_id_list: "capo_resource_explorer_2.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.member_index.MemberIndex]":
        _token = next_token
        while True:
            _response = await self.list_indexes_for_members(
                account_id_list,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("indexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_managed_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        service_principal: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_managed_views_output.ListManagedViewsOutput":
        """<p>Lists the Amazon resource names (ARNs) of the <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html">Amazon Web Services-managed views</a> available in the Amazon Web Services Region in which you call this operation. </p>

        Args:
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>
            service_principal: <p>Specifies a service principal name. If specified, then the operation only returns the managed views that are managed by the input service. </p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_managed_views_input.ListManagedViewsInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_managed_views_output.ListManagedViewsOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_managed_views

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_managed_views.async_list_managed_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_managed_views_input.ListManagedViewsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if service_principal is not None:
            input_["service_principal"] = service_principal

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_managed_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        service_principal: Optional[str] = None,
    ) -> "AsyncIterator[str]":
        _token = next_token
        while True:
            _response = await self.list_managed_views(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                service_principal=service_principal,
            )
            _page = _resolve_path(_response, ("managed_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        filters: Optional[
            "capo_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_resources_output.ListResourcesOutput":
        """<p>Returns a list of resources and their details that match the specified criteria. This query must use a view. If you don’t explicitly specify a view, then Resource Explorer uses the default view for the Amazon Web Services Region in which you call this operation. </p>

        Args:
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters">filter prefixes</a> with optional <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            view_arn: <p>Specifies the Amazon resource name (ARN) of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a 401 Unauthorized exception.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p> <note> <p>The <code>ListResources</code> operation does not generate a <code>NextToken</code> if you set <code>MaxResults</code> to 1000. </p> </note>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_resources_input.ListResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_resources_output.ListResourcesOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_resources

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_resources.async_list_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_resources_input.ListResourcesInput = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if view_arn is not None:
            input_["view_arn"] = view_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        filters: Optional[
            "capo_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.resource.Resource]":
        _token = next_token
        while True:
            _response = await self.list_resources(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                view_arn=view_arn,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_indexes(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        regions: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_service_indexes_output.ListServiceIndexesOutput":
        """<p>Lists all Resource Explorer indexes across the specified Amazon Web Services Regions. This operation returns information about indexes including their ARNs, types, and Regions.</p>

        Args:
            regions: <p>A list of Amazon Web Services Regions to include in the search for indexes. If not specified, indexes from all Regions are returned.</p>
            max_results: <p>The maximum number of index results to return in a single response. Valid values are between <code>1</code> and <code>100</code>.</p>
            next_token: <p>The pagination token from a previous <code>ListServiceIndexes</code> response. Use this token to retrieve the next set of results.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_service_indexes_input.ListServiceIndexesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_service_indexes_output.ListServiceIndexesOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_service_indexes

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_service_indexes.async_list_service_indexes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_service_indexes_input.ListServiceIndexesInput = {}
        if regions is not None:
            input_["regions"] = regions
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

    async def iter_list_service_indexes(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        regions: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.index.Index]":
        _token = next_token
        while True:
            _response = await self.list_service_indexes(
                config_overrides=config_overrides,
                regions=regions,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("indexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_service_views_output.ListServiceViewsOutput":
        """<p>Lists all Resource Explorer service views available in the current Amazon Web Services account. This operation returns the ARNs of available service views.</p>

        Args:
            max_results: <p>The maximum number of service view results to return in a single response. Valid values are between <code>1</code> and <code>50</code>.</p>
            next_token: <p>The pagination token from a previous <code>ListServiceViews</code> response. Use this token to retrieve the next set of results.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_service_views_input.ListServiceViewsInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_service_views_output.ListServiceViewsOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_service_views

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_service_views.async_list_service_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_service_views_input.ListServiceViewsInput = {}
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

    async def iter_list_service_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[str]":
        _token = next_token
        while True:
            _response = await self.list_service_views(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_streaming_access_for_services(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_streaming_access_for_services_output.ListStreamingAccessForServicesOutput":
        """<p>Returns a list of Amazon Web Services services that have been granted streaming access to your Resource Explorer data. Streaming access allows Amazon Web Services services to receive real-time updates about your resources as they are indexed by Resource Explorer.</p>

        Args:
            max_results: <p>The maximum number of streaming access entries to return in the response. If there are more results available, the response includes a NextToken value that you can use in a subsequent call to get the next set of results. The value must be between 1 and 50. If you don't specify a value, the default is 50.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_streaming_access_for_services_input.ListStreamingAccessForServicesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_streaming_access_for_services_output.ListStreamingAccessForServicesOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_streaming_access_for_services

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_streaming_access_for_services.async_list_streaming_access_for_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_streaming_access_for_services_input.ListStreamingAccessForServicesInput = {}
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

    async def iter_list_streaming_access_for_services(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.streaming_access_details.StreamingAccessDetails]":
        _token = next_token
        while True:
            _response = await self.list_streaming_access_for_services(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("streaming_access_for_services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_supported_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_resource_explorer_2.types.list_supported_resource_types_output.ListSupportedResourceTypesOutput":
        """<p>Retrieves a list of all resource types currently supported by Amazon Web Services Resource Explorer.</p>

        Args:
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_supported_resource_types_input.ListSupportedResourceTypesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_supported_resource_types_output.ListSupportedResourceTypesOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_supported_resource_types

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_supported_resource_types.async_list_supported_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_supported_resource_types_input.ListSupportedResourceTypesInput = {}
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

    async def iter_list_supported_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.supported_resource_type.SupportedResourceType]":
        _token = next_token
        while True:
            _response = await self.list_supported_resource_types(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resource_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags that are attached to the specified resource.</p>

        Args:
            resource_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view or index that you want to attach tags to.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search(
        self,
        query_string: "capo_resource_explorer_2.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.search_output.SearchOutput":
        """<p>Searches for resources and displays details about all resources that match the specified criteria. You must specify a query string.</p> <p>All search queries must use a view. If you don't explicitly specify a view, then Amazon Web Services Resource Explorer uses the default view for the Amazon Web Services Region in which you call this operation. The results are the logical intersection of the results that match both the <code>QueryString</code> parameter supplied to this operation and the <code>SearchFilter</code> parameter attached to the view.</p> <p>For the complete syntax supported by the <code>QueryString</code> parameter, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/APIReference/about-query-syntax.html">Search query syntax reference for Resource Explorer</a>.</p> <p>If your search results are empty, or are missing results that you think should be there, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html">Troubleshooting Resource Explorer search</a>.</p>

        Args:
            query_string: <p>A string that includes keywords and filters that specify the resources that you want to include in the results.</p> <p>For the complete syntax supported by the <code>QueryString</code> parameter, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html">Search query syntax reference for Resource Explorer</a>.</p> <p>The search is completely case insensitive. You can specify an empty string to return all results up to the limit of 1,000 total results.</p> <note> <p>The operation can return only the first 1,000 results. If the resource you want is not included, then use a different value for <code>QueryString</code> to refine the results.</p> </note>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            view_arn: <p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a <code>401 Unauthorized</code> exception.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.search_input.SearchInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.search_output.SearchOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.search

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.search.async_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.search_input.SearchInput = {
            "query_string": query_string
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if view_arn is not None:
            input_["view_arn"] = view_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search(
        self,
        query_string: "capo_resource_explorer_2.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.resource.Resource]":
        _token = next_token
        while True:
            _response = await self.search(
                query_string,
                config_overrides=config_overrides,
                max_results=max_results,
                view_arn=view_arn,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        tags: Optional["capo_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "capo_resource_explorer_2.types.tag_resource_output.TagResourceOutput":
        """<p>Adds one or more tag key and value pairs to an Amazon Web Services Resource Explorer view or index.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the view or index that you want to attach tags to.</p>
            tags: <p>A list of tag key and value pairs that you want to attach to the specified view or index.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.tag_resource

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

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
        tag_keys: "capo_resource_explorer_2.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tag key and value pairs from an Amazon Web Services Resource Explorer view or index.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the view or index that you want to remove tags from.</p>
            tag_keys: <p>A list of the keys for the tags that you want to remove from the specified view or index.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.untag_resource

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.untag_resource_input.UntagResourceInput = {
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

    async def create_index(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "capo_resource_explorer_2.types.create_index_output.CreateIndexOutput":
        """<p>Turns on Amazon Web Services Resource Explorer in the Amazon Web Services Region in which you called this operation by creating an index. Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the <a>Search</a> operation. You can create only one index in a Region.</p> <note> <p>This operation creates only a <i>local</i> index. To promote the local index in one Amazon Web Services Region into the aggregator index for the Amazon Web Services account, use the <a>UpdateIndexType</a> operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search by creating an aggregator index</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> </note> <p>For more details about what happens when you turn on Resource Explorer in an Amazon Web Services Region, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html">Turn on Resource Explorer to index your resources in an Amazon Web Services Region</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <p>If this is the first Amazon Web Services Region in which you've created an index for Resource Explorer, then this operation also <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html">creates a service-linked role</a> in your Amazon Web Services account that allows Resource Explorer to enumerate your resources to populate the index.</p> <ul> <li> <p> <b>Action</b>: <code>resource-explorer-2:CreateIndex</code> </p> <p> <b>Resource</b>: The ARN of the index (as it will exist after the operation completes) in the Amazon Web Services Region and account in which you're trying to create the index. Use the wildcard character (<code>*</code>) at the end of the string to match the eventual UUID. For example, the following <code>Resource</code> element restricts the role or user to creating an index in only the <code>us-east-2</code> Region of the specified account.</p> <p> <code>"Resource": "arn:aws:resource-explorer-2:us-west-2:<i>&lt;account-id&gt;</i>:index/*"</code> </p> <p>Alternatively, you can use <code>"Resource": "*"</code> to allow the role or user to create an index in any Region.</p> </li> <li> <p> <b>Action</b>: <code>iam:CreateServiceLinkedRole</code> </p> <p> <b>Resource</b>: No specific resource (*). </p> <p>This permission is required only the first time you create an index to turn on Resource Explorer in the account. Resource Explorer uses this to create the <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html">service-linked role needed to index the resources in your account</a>. Resource Explorer uses the same service-linked role for all additional indexes you create afterwards.</p> </li> </ul>

        Args:
            client_token: <p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type value</a> to ensure the uniqueness of your index.</p>
            tags: <p>The specified tags are attached only to the index created in this Amazon Web Services Region. The tags aren't attached to any of the resources listed in the index.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.create_index_input.CreateIndexInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.create_index_output.CreateIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.create_index

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.create_index.async_create_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.create_index_input.CreateIndexInput = {}
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

    async def update_index_type(
        self,
        arn: str,
        type: "capo_resource_explorer_2.types.index_type.IndexType",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> (
        "capo_resource_explorer_2.types.update_index_type_output.UpdateIndexTypeOutput"
    ):
        """<p>Changes the type of the index from one of the following types to the other. For more information about indexes and the role they perform in Amazon Web Services Resource Explorer, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search by creating an aggregator index</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <ul> <li> <p> <b> <code>AGGREGATOR</code> index type</b> </p> <p>The index contains information about resources from all Amazon Web Services Regions in the Amazon Web Services account in which you've created a Resource Explorer index. Resource information from all other Regions is replicated to this Region's index.</p> <p>When you change the index type to <code>AGGREGATOR</code>, Resource Explorer turns on replication of all discovered resource information from the other Amazon Web Services Regions in your account to this index. You can then, from this Region only, perform resource search queries that span all Amazon Web Services Regions in the Amazon Web Services account. Turning on replication from all other Regions is performed by asynchronous background tasks. You can check the status of the asynchronous tasks by using the <a>GetIndex</a> operation. When the asynchronous tasks complete, the <code>Status</code> response of that operation changes from <code>UPDATING</code> to <code>ACTIVE</code>. After that, you can start to see results from other Amazon Web Services Regions in query results. However, it can take several hours for replication from all other Regions to complete.</p> <important> <p>You can have only one aggregator index per Amazon Web Services account. Before you can promote a different index to be the aggregator index for the account, you must first demote the existing aggregator index to type <code>LOCAL</code>.</p> </important> </li> <li> <p> <b> <code>LOCAL</code> index type</b> </p> <p>The index contains information about resources in only the Amazon Web Services Region in which the index exists. If an aggregator index in another Region exists, then information in this local index is replicated to the aggregator index.</p> <p>When you change the index type to <code>LOCAL</code>, Resource Explorer turns off the replication of resource information from all other Amazon Web Services Regions in the Amazon Web Services account to this Region. The aggregator index remains in the <code>UPDATING</code> state until all replication with other Regions successfully stops. You can check the status of the asynchronous task by using the <a>GetIndex</a> operation. When Resource Explorer successfully stops all replication with other Regions, the <code>Status</code> response of that operation changes from <code>UPDATING</code> to <code>ACTIVE</code>. Separately, the resource information from other Regions that was previously stored in the index is deleted within 30 days by another background task. Until that asynchronous task completes, some results from other Regions can continue to appear in search results.</p> <important> <p>After you demote an aggregator index to a local index, you must wait 24 hours before you can promote another index to be the new aggregator index for the account.</p> </important> </li> </ul>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you want to update.</p>
            type: <p>The type of the index. To understand the difference between <code>LOCAL</code> and <code>AGGREGATOR</code>, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it exceeds a service quota.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.update_index_type_input.UpdateIndexTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.update_index_type_output.UpdateIndexTypeOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.update_index_type

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.update_index_type.async_update_index_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.update_index_type_input.UpdateIndexTypeInput = {
            "arn": arn,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_index(
        self,
        arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.delete_index_output.DeleteIndexOutput":
        """<p>Deletes the specified index and turns off Amazon Web Services Resource Explorer in the specified Amazon Web Services Region. When you delete an index, Resource Explorer stops discovering and indexing resources in that Region. Resource Explorer also deletes all views in that Region. These actions occur as asynchronous background tasks. You can check to see when the actions are complete by using the <a>GetIndex</a> operation and checking the <code>Status</code> response value.</p> <note> <p>If the index you delete is the aggregator index for the Amazon Web Services account, you must wait 24 hours before you can promote another local index to be the aggregator index for the account. Users can't perform account-wide searches using Resource Explorer until another aggregator index is configured.</p> </note>

        Args:
            arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index that you want to delete.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.delete_index_input.DeleteIndexInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.delete_index_output.DeleteIndexOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.delete_index

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.delete_index.async_delete_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.delete_index_input.DeleteIndexInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_indexes(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        type: Optional["capo_resource_explorer_2.types.index_type.IndexType"] = None,
        regions: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_resource_explorer_2.types.list_indexes_output.ListIndexesOutput":
        """<p>Retrieves a list of all of the indexes in Amazon Web Services Regions that are currently collecting resource information for Amazon Web Services Resource Explorer.</p>

        Args:
            type: <p>If specified, limits the output to only indexes of the specified Type, either <code>LOCAL</code> or <code>AGGREGATOR</code>.</p> <p>Use this option to discover the aggregator index for your account.</p>
            regions: <p>If specified, limits the response to only information about the index in the specified list of Amazon Web Services Regions.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_indexes_input.ListIndexesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_indexes_output.ListIndexesOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_indexes

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_indexes.async_list_indexes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_indexes_input.ListIndexesInput = {}
        if type is not None:
            input_["type"] = type
        if regions is not None:
            input_["regions"] = regions
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

    async def iter_list_indexes(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        type: Optional["capo_resource_explorer_2.types.index_type.IndexType"] = None,
        regions: Optional[
            "capo_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_resource_explorer_2.types.index.Index]":
        _token = next_token
        while True:
            _response = await self.list_indexes(
                config_overrides=config_overrides,
                type=type,
                regions=regions,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("indexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_view(
        self,
        view_name: "capo_resource_explorer_2.types.view_name.ViewName",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        client_token: Optional[str] = None,
        included_properties: Optional[
            "capo_resource_explorer_2.types.included_property_list.IncludedPropertyList"
        ] = None,
        scope: Optional[str] = None,
        filters: Optional[
            "capo_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
        tags: Optional["capo_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "capo_resource_explorer_2.types.create_view_output.CreateViewOutput":
        """<p>Creates a view that users can query by using the <a>Search</a> operation. Results from queries that you make using this view include only resources that match the view's <code>Filters</code>. For more information about Amazon Web Services Resource Explorer views, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views.html">Managing views</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <p>Only the principals with an IAM identity-based policy that grants <code>Allow</code> to the <code>Search</code> action on a <code>Resource</code> with the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of this view can <a>Search</a> using views you create with this operation.</p>

        Args:
            client_token: <p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type value</a> to ensure the uniqueness of your views.</p>
            view_name: <p>The name of the new view. This name appears in the list of views in Resource Explorer.</p> <p>The name must be no more than 64 characters long, and can include letters, digits, and the dash (-) character. The name must be unique within its Amazon Web Services Region.</p>
            included_properties: <p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>
            scope: <p>The root ARN of the account, an organizational unit (OU), or an organization ARN. If left empty, the default is account.</p>
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters">filter prefixes</a> with optional <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>
            tags: <p>Tag key and value pairs that are attached to the view.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it exceeds a service quota.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.create_view_input.CreateViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.create_view_output.CreateViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.create_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.create_view.async_create_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.create_view_input.CreateViewInput = {
            "view_name": view_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if included_properties is not None:
            input_["included_properties"] = included_properties
        if scope is not None:
            input_["scope"] = scope
        if filters is not None:
            input_["filters"] = filters
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_view(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.get_view_output.GetViewOutput":
        """<p>Retrieves details of the specified view.</p>

        Args:
            view_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that you want information about.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.get_view_input.GetViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.get_view_output.GetViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.get_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.get_view.async_get_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.get_view_input.GetViewInput = {
            "view_arn": view_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_view(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        included_properties: Optional[
            "capo_resource_explorer_2.types.included_property_list.IncludedPropertyList"
        ] = None,
        filters: Optional[
            "capo_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
    ) -> "capo_resource_explorer_2.types.update_view_output.UpdateViewOutput":
        """<p>Modifies some of the details of a view. You can change the filter string and the list of included properties. You can't change the name of the view.</p>

        Args:
            view_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that you want to modify.</p>
            included_properties: <p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters">filter prefixes</a> with optional <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because it exceeds a service quota.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.update_view_input.UpdateViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.update_view_output.UpdateViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.update_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.update_view.async_update_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.update_view_input.UpdateViewInput = {
            "view_arn": view_arn
        }
        if included_properties is not None:
            input_["included_properties"] = included_properties
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_view(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.delete_view_output.DeleteViewOutput":
        """<p>Deletes the specified view.</p> <p>If the specified view is the default view for its Amazon Web Services Region, then all <a>Search</a> operations in that Region must explicitly specify the view to use until you configure a new default by calling the <a>AssociateDefaultView</a> operation.</p>

        Args:
            view_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that you want to delete.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.delete_view_input.DeleteViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.delete_view_output.DeleteViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.delete_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.delete_view.async_delete_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.delete_view_input.DeleteViewInput = {
            "view_arn": view_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_resource_explorer_2.types.list_views_output.ListViewsOutput":
        """<p>Lists the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource names (ARNs)</a> of the views available in the Amazon Web Services Region in which you call this operation.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.list_views_input.ListViewsInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.list_views_output.ListViewsOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.list_views

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.list_views.async_list_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.list_views_input.ListViewsInput = {}
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

    async def iter_list_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[str]":
        _token = next_token
        while True:
            _response = await self.list_views(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_default_view(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "capo_resource_explorer_2.types.associate_default_view_output.AssociateDefaultViewOutput":
        """<p>Sets the specified view as the default for the Amazon Web Services Region in which you call this operation. When a user performs a <a>Search</a> that doesn't explicitly specify which view to use, then Amazon Web Services Resource Explorer automatically chooses this default view for searches performed in this Amazon Web Services Region.</p> <p>If an Amazon Web Services Region doesn't have a default view configured, then users must explicitly specify a view with every <code>Search</code> operation performed in that Region.</p>

        Args:
            view_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view to set as the default for the Amazon Web Services Region and Amazon Web Services account in which you call this operation. The specified view must already exist in the called Region.</p>

        Raises:
            capo_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            capo_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            capo_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            capo_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html">Quotas for Resource Explorer</a>.</p>
            capo_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            capo_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_explorer_2.types.associate_default_view_input.AssociateDefaultViewInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_explorer_2.types.associate_default_view_output.AssociateDefaultViewOutput"
        ]:
            import capo_resource_explorer_2._operations.resource_explorer.associate_default_view

            (
                output,
                http_response,
            ) = await capo_resource_explorer_2._operations.resource_explorer.associate_default_view.async_associate_default_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_explorer_2.types.associate_default_view_input.AssociateDefaultViewInput = {
            "view_arn": view_arn
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
