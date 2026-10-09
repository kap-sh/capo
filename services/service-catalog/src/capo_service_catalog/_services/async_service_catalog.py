"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AWS242ServiceCatalogService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_service_catalog._auth._signers
import capo_service_catalog._auth._sigv4
from capo_service_catalog._auth._identity import Credentials
from capo_service_catalog._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_service_catalog._auth._zapros_handler import AuthMiddleware
from capo_service_catalog._pagination import resolve_path as _resolve_path
from capo_service_catalog._services._aws_config import aaws_config
from capo_service_catalog._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.accept_portfolio_share_input
    import capo_service_catalog.types.accept_portfolio_share_output
    import capo_service_catalog.types.access_level_filter
    import capo_service_catalog.types.account_id
    import capo_service_catalog.types.add_tags
    import capo_service_catalog.types.associate_budget_with_resource_input
    import capo_service_catalog.types.associate_budget_with_resource_output
    import capo_service_catalog.types.associate_principal_with_portfolio_input
    import capo_service_catalog.types.associate_principal_with_portfolio_output
    import capo_service_catalog.types.associate_product_with_portfolio_input
    import capo_service_catalog.types.associate_product_with_portfolio_output
    import capo_service_catalog.types.associate_service_action_with_provisioning_artifact_input
    import capo_service_catalog.types.associate_service_action_with_provisioning_artifact_output
    import capo_service_catalog.types.associate_tag_option_with_resource_input
    import capo_service_catalog.types.associate_tag_option_with_resource_output
    import capo_service_catalog.types.batch_associate_service_action_with_provisioning_artifact_input
    import capo_service_catalog.types.batch_associate_service_action_with_provisioning_artifact_output
    import capo_service_catalog.types.batch_disassociate_service_action_from_provisioning_artifact_input
    import capo_service_catalog.types.batch_disassociate_service_action_from_provisioning_artifact_output
    import capo_service_catalog.types.boolean
    import capo_service_catalog.types.budget_name
    import capo_service_catalog.types.constraint_description
    import capo_service_catalog.types.constraint_parameters
    import capo_service_catalog.types.constraint_type
    import capo_service_catalog.types.copy_options
    import capo_service_catalog.types.copy_product_input
    import capo_service_catalog.types.copy_product_output
    import capo_service_catalog.types.create_constraint_input
    import capo_service_catalog.types.create_constraint_output
    import capo_service_catalog.types.create_portfolio_input
    import capo_service_catalog.types.create_portfolio_output
    import capo_service_catalog.types.create_portfolio_share_input
    import capo_service_catalog.types.create_portfolio_share_output
    import capo_service_catalog.types.create_product_input
    import capo_service_catalog.types.create_product_output
    import capo_service_catalog.types.create_provisioned_product_plan_input
    import capo_service_catalog.types.create_provisioned_product_plan_output
    import capo_service_catalog.types.create_provisioning_artifact_input
    import capo_service_catalog.types.create_provisioning_artifact_output
    import capo_service_catalog.types.create_service_action_input
    import capo_service_catalog.types.create_service_action_output
    import capo_service_catalog.types.create_tag_option_input
    import capo_service_catalog.types.create_tag_option_output
    import capo_service_catalog.types.delete_constraint_input
    import capo_service_catalog.types.delete_constraint_output
    import capo_service_catalog.types.delete_portfolio_input
    import capo_service_catalog.types.delete_portfolio_output
    import capo_service_catalog.types.delete_portfolio_share_input
    import capo_service_catalog.types.delete_portfolio_share_output
    import capo_service_catalog.types.delete_product_input
    import capo_service_catalog.types.delete_product_output
    import capo_service_catalog.types.delete_provisioned_product_plan_input
    import capo_service_catalog.types.delete_provisioned_product_plan_output
    import capo_service_catalog.types.delete_provisioning_artifact_input
    import capo_service_catalog.types.delete_provisioning_artifact_output
    import capo_service_catalog.types.delete_service_action_input
    import capo_service_catalog.types.delete_service_action_output
    import capo_service_catalog.types.delete_tag_option_input
    import capo_service_catalog.types.delete_tag_option_output
    import capo_service_catalog.types.describe_constraint_input
    import capo_service_catalog.types.describe_constraint_output
    import capo_service_catalog.types.describe_copy_product_status_input
    import capo_service_catalog.types.describe_copy_product_status_output
    import capo_service_catalog.types.describe_portfolio_input
    import capo_service_catalog.types.describe_portfolio_output
    import capo_service_catalog.types.describe_portfolio_share_status_input
    import capo_service_catalog.types.describe_portfolio_share_status_output
    import capo_service_catalog.types.describe_portfolio_share_type
    import capo_service_catalog.types.describe_portfolio_shares_input
    import capo_service_catalog.types.describe_portfolio_shares_output
    import capo_service_catalog.types.describe_product_as_admin_input
    import capo_service_catalog.types.describe_product_as_admin_output
    import capo_service_catalog.types.describe_product_input
    import capo_service_catalog.types.describe_product_output
    import capo_service_catalog.types.describe_product_view_input
    import capo_service_catalog.types.describe_product_view_output
    import capo_service_catalog.types.describe_provisioned_product_input
    import capo_service_catalog.types.describe_provisioned_product_output
    import capo_service_catalog.types.describe_provisioned_product_plan_input
    import capo_service_catalog.types.describe_provisioned_product_plan_output
    import capo_service_catalog.types.describe_provisioning_artifact_input
    import capo_service_catalog.types.describe_provisioning_artifact_output
    import capo_service_catalog.types.describe_provisioning_parameters_input
    import capo_service_catalog.types.describe_provisioning_parameters_output
    import capo_service_catalog.types.describe_record_input
    import capo_service_catalog.types.describe_record_output
    import capo_service_catalog.types.describe_service_action_execution_parameters_input
    import capo_service_catalog.types.describe_service_action_execution_parameters_output
    import capo_service_catalog.types.describe_service_action_input
    import capo_service_catalog.types.describe_service_action_output
    import capo_service_catalog.types.describe_tag_option_input
    import capo_service_catalog.types.describe_tag_option_output
    import capo_service_catalog.types.disable_aws_organizations_access_input
    import capo_service_catalog.types.disable_aws_organizations_access_output
    import capo_service_catalog.types.disassociate_budget_from_resource_input
    import capo_service_catalog.types.disassociate_budget_from_resource_output
    import capo_service_catalog.types.disassociate_principal_from_portfolio_input
    import capo_service_catalog.types.disassociate_principal_from_portfolio_output
    import capo_service_catalog.types.disassociate_product_from_portfolio_input
    import capo_service_catalog.types.disassociate_product_from_portfolio_output
    import capo_service_catalog.types.disassociate_service_action_from_provisioning_artifact_input
    import capo_service_catalog.types.disassociate_service_action_from_provisioning_artifact_output
    import capo_service_catalog.types.disassociate_tag_option_from_resource_input
    import capo_service_catalog.types.disassociate_tag_option_from_resource_output
    import capo_service_catalog.types.enable_aws_organizations_access_input
    import capo_service_catalog.types.enable_aws_organizations_access_output
    import capo_service_catalog.types.engine_workflow_failure_reason
    import capo_service_catalog.types.engine_workflow_resource_identifier
    import capo_service_catalog.types.engine_workflow_status
    import capo_service_catalog.types.engine_workflow_token
    import capo_service_catalog.types.execute_provisioned_product_plan_input
    import capo_service_catalog.types.execute_provisioned_product_plan_output
    import capo_service_catalog.types.execute_provisioned_product_service_action_input
    import capo_service_catalog.types.execute_provisioned_product_service_action_output
    import capo_service_catalog.types.execution_parameter_map
    import capo_service_catalog.types.get_aws_organizations_access_status_input
    import capo_service_catalog.types.get_aws_organizations_access_status_output
    import capo_service_catalog.types.get_provisioned_product_outputs_input
    import capo_service_catalog.types.get_provisioned_product_outputs_output
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.ignore_errors
    import capo_service_catalog.types.import_as_provisioned_product_input
    import capo_service_catalog.types.import_as_provisioned_product_output
    import capo_service_catalog.types.list_accepted_portfolio_shares_input
    import capo_service_catalog.types.list_accepted_portfolio_shares_output
    import capo_service_catalog.types.list_budgets_for_resource_input
    import capo_service_catalog.types.list_budgets_for_resource_output
    import capo_service_catalog.types.list_constraints_for_portfolio_input
    import capo_service_catalog.types.list_constraints_for_portfolio_output
    import capo_service_catalog.types.list_launch_paths_input
    import capo_service_catalog.types.list_launch_paths_output
    import capo_service_catalog.types.list_organization_portfolio_access_input
    import capo_service_catalog.types.list_organization_portfolio_access_output
    import capo_service_catalog.types.list_portfolio_access_input
    import capo_service_catalog.types.list_portfolio_access_output
    import capo_service_catalog.types.list_portfolios_for_product_input
    import capo_service_catalog.types.list_portfolios_for_product_output
    import capo_service_catalog.types.list_portfolios_input
    import capo_service_catalog.types.list_portfolios_output
    import capo_service_catalog.types.list_principals_for_portfolio_input
    import capo_service_catalog.types.list_principals_for_portfolio_output
    import capo_service_catalog.types.list_provisioned_product_plans_input
    import capo_service_catalog.types.list_provisioned_product_plans_output
    import capo_service_catalog.types.list_provisioning_artifacts_for_service_action_input
    import capo_service_catalog.types.list_provisioning_artifacts_for_service_action_output
    import capo_service_catalog.types.list_provisioning_artifacts_input
    import capo_service_catalog.types.list_provisioning_artifacts_output
    import capo_service_catalog.types.list_record_history_input
    import capo_service_catalog.types.list_record_history_output
    import capo_service_catalog.types.list_record_history_search_filter
    import capo_service_catalog.types.list_resources_for_tag_option_input
    import capo_service_catalog.types.list_resources_for_tag_option_output
    import capo_service_catalog.types.list_service_actions_for_provisioning_artifact_input
    import capo_service_catalog.types.list_service_actions_for_provisioning_artifact_output
    import capo_service_catalog.types.list_service_actions_input
    import capo_service_catalog.types.list_service_actions_output
    import capo_service_catalog.types.list_stack_instances_for_provisioned_product_input
    import capo_service_catalog.types.list_stack_instances_for_provisioned_product_output
    import capo_service_catalog.types.list_tag_options_filters
    import capo_service_catalog.types.list_tag_options_input
    import capo_service_catalog.types.list_tag_options_output
    import capo_service_catalog.types.notification_arns
    import capo_service_catalog.types.notify_provision_product_engine_workflow_result_input
    import capo_service_catalog.types.notify_provision_product_engine_workflow_result_output
    import capo_service_catalog.types.notify_terminate_provisioned_product_engine_workflow_result_input
    import capo_service_catalog.types.notify_terminate_provisioned_product_engine_workflow_result_output
    import capo_service_catalog.types.notify_update_provisioned_product_engine_workflow_result_input
    import capo_service_catalog.types.notify_update_provisioned_product_engine_workflow_result_output
    import capo_service_catalog.types.nullable_boolean
    import capo_service_catalog.types.organization_node
    import capo_service_catalog.types.organization_node_type
    import capo_service_catalog.types.output_keys
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_size_max100
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.physical_id
    import capo_service_catalog.types.portfolio_description
    import capo_service_catalog.types.portfolio_display_name
    import capo_service_catalog.types.portfolio_share_type
    import capo_service_catalog.types.principal_arn
    import capo_service_catalog.types.principal_type
    import capo_service_catalog.types.product_arn
    import capo_service_catalog.types.product_source
    import capo_service_catalog.types.product_type
    import capo_service_catalog.types.product_view_filters
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.product_view_owner
    import capo_service_catalog.types.product_view_short_description
    import capo_service_catalog.types.product_view_sort_by
    import capo_service_catalog.types.provider_name
    import capo_service_catalog.types.provision_product_input
    import capo_service_catalog.types.provision_product_output
    import capo_service_catalog.types.provisioned_product_filters
    import capo_service_catalog.types.provisioned_product_name
    import capo_service_catalog.types.provisioned_product_name_or_arn
    import capo_service_catalog.types.provisioned_product_plan_name
    import capo_service_catalog.types.provisioned_product_plan_type
    import capo_service_catalog.types.provisioned_product_properties
    import capo_service_catalog.types.provisioning_artifact_active
    import capo_service_catalog.types.provisioning_artifact_description
    import capo_service_catalog.types.provisioning_artifact_guidance
    import capo_service_catalog.types.provisioning_artifact_name
    import capo_service_catalog.types.provisioning_artifact_properties
    import capo_service_catalog.types.provisioning_parameters
    import capo_service_catalog.types.provisioning_preferences
    import capo_service_catalog.types.record_outputs
    import capo_service_catalog.types.reject_portfolio_share_input
    import capo_service_catalog.types.reject_portfolio_share_output
    import capo_service_catalog.types.resource_id
    import capo_service_catalog.types.resource_type
    import capo_service_catalog.types.retain_physical_resources
    import capo_service_catalog.types.scan_provisioned_products_input
    import capo_service_catalog.types.scan_provisioned_products_output
    import capo_service_catalog.types.search_products_as_admin_input
    import capo_service_catalog.types.search_products_as_admin_output
    import capo_service_catalog.types.search_products_input
    import capo_service_catalog.types.search_products_output
    import capo_service_catalog.types.search_provisioned_products_input
    import capo_service_catalog.types.search_provisioned_products_output
    import capo_service_catalog.types.search_provisioned_products_page_size
    import capo_service_catalog.types.service_action_associations
    import capo_service_catalog.types.service_action_definition_map
    import capo_service_catalog.types.service_action_definition_type
    import capo_service_catalog.types.service_action_description
    import capo_service_catalog.types.service_action_name
    import capo_service_catalog.types.sort_field
    import capo_service_catalog.types.sort_order
    import capo_service_catalog.types.source_connection
    import capo_service_catalog.types.source_provisioning_artifact_properties
    import capo_service_catalog.types.support_description
    import capo_service_catalog.types.support_email
    import capo_service_catalog.types.support_url
    import capo_service_catalog.types.tag_keys
    import capo_service_catalog.types.tag_option_active
    import capo_service_catalog.types.tag_option_id
    import capo_service_catalog.types.tag_option_key
    import capo_service_catalog.types.tag_option_value
    import capo_service_catalog.types.tags
    import capo_service_catalog.types.terminate_provisioned_product_input
    import capo_service_catalog.types.terminate_provisioned_product_output
    import capo_service_catalog.types.update_constraint_input
    import capo_service_catalog.types.update_constraint_output
    import capo_service_catalog.types.update_portfolio_input
    import capo_service_catalog.types.update_portfolio_output
    import capo_service_catalog.types.update_portfolio_share_input
    import capo_service_catalog.types.update_portfolio_share_output
    import capo_service_catalog.types.update_product_input
    import capo_service_catalog.types.update_product_output
    import capo_service_catalog.types.update_provisioned_product_input
    import capo_service_catalog.types.update_provisioned_product_output
    import capo_service_catalog.types.update_provisioned_product_properties_input
    import capo_service_catalog.types.update_provisioned_product_properties_output
    import capo_service_catalog.types.update_provisioning_artifact_input
    import capo_service_catalog.types.update_provisioning_artifact_output
    import capo_service_catalog.types.update_provisioning_parameters
    import capo_service_catalog.types.update_provisioning_preferences
    import capo_service_catalog.types.update_service_action_input
    import capo_service_catalog.types.update_service_action_output
    import capo_service_catalog.types.update_tag_option_input
    import capo_service_catalog.types.update_tag_option_output
    import capo_service_catalog.types.verbose


class AsyncServiceCatalogClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncServiceCatalogClient:
    """A client for the ``ServiceCatalog`` service.

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
        self._config = AsyncServiceCatalogClientConfig(
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
        self, config_overrides: Optional[AsyncServiceCatalogClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncServiceCatalogClientConfig = config_overrides or {}
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

    async def accept_portfolio_share(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        portfolio_share_type: Optional[
            "capo_service_catalog.types.portfolio_share_type.PortfolioShareType"
        ] = None,
    ) -> "capo_service_catalog.types.accept_portfolio_share_output.AcceptPortfolioShareOutput":
        """<p>Accepts an offer to share the specified portfolio.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            portfolio_share_type: <p>The type of shared portfolios to accept. The default is to accept imported portfolios.</p> <ul> <li> <p> <code>AWS_ORGANIZATIONS</code> - Accept portfolios shared by the management account of your organization.</p> </li> <li> <p> <code>IMPORTED</code> - Accept imported portfolios.</p> </li> <li> <p> <code>AWS_SERVICECATALOG</code> - Not supported. (Throws ResourceNotFoundException.)</p> </li> </ul> <p>For example, <code>aws servicecatalog accept-portfolio-share --portfolio-id "port-2qwzkwxt3y5fk" --portfolio-share-type AWS_ORGANIZATIONS</code> </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.accept_portfolio_share_input.AcceptPortfolioShareInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.accept_portfolio_share_output.AcceptPortfolioShareOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.accept_portfolio_share

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.accept_portfolio_share.async_accept_portfolio_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.accept_portfolio_share_input.AcceptPortfolioShareInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if portfolio_share_type is not None:
            input_["portfolio_share_type"] = portfolio_share_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_budget_with_resource(
        self,
        budget_name: "capo_service_catalog.types.budget_name.BudgetName",
        resource_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> "capo_service_catalog.types.associate_budget_with_resource_output.AssociateBudgetWithResourceOutput":
        """<p>Associates the specified budget with the specified resource.</p>

        Args:
            budget_name: <p>The name of the budget you want to associate.</p>
            resource_id: <p> The resource identifier. Either a portfolio-id or a product-id.</p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.associate_budget_with_resource_input.AssociateBudgetWithResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.associate_budget_with_resource_output.AssociateBudgetWithResourceOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.associate_budget_with_resource

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.associate_budget_with_resource.async_associate_budget_with_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.associate_budget_with_resource_input.AssociateBudgetWithResourceInput = {
            "budget_name": budget_name,
            "resource_id": resource_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_principal_with_portfolio(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        principal_arn: "capo_service_catalog.types.principal_arn.PrincipalARN",
        principal_type: "capo_service_catalog.types.principal_type.PrincipalType",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.associate_principal_with_portfolio_output.AssociatePrincipalWithPortfolioOutput":
        """<p>Associates the specified principal ARN with the specified portfolio.</p> <p>If you share the portfolio with principal name sharing enabled, the <code>PrincipalARN</code> association is included in the share. </p> <p>The <code>PortfolioID</code>, <code>PrincipalARN</code>, and <code>PrincipalType</code> parameters are required. </p> <p>You can associate a maximum of 10 Principals with a portfolio using <code>PrincipalType</code> as <code>IAM_PATTERN</code>. </p> <note> <p>When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is <i>not</i> an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using <code>PrincipalType</code> as <code>IAM</code>. With this configuration, the <code>PrincipalARN</code> must already exist in the recipient account before it can be associated. </p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            principal_arn: <p>The ARN of the principal (user, role, or group). If the <code>PrincipalType</code> is <code>IAM</code>, the supported value is a fully defined <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM Amazon Resource Name (ARN)</a>. If the <code>PrincipalType</code> is <code>IAM_PATTERN</code>, the supported value is an <code>IAM</code> ARN <i>without an AccountID</i> in the following format:</p> <p> <i>arn:partition:iam:::resource-type/resource-id</i> </p> <p>The ARN resource-id can be either:</p> <ul> <li> <p>A fully formed resource-id. For example, <i>arn:aws:iam:::role/resource-name</i> or <i>arn:aws:iam:::role/resource-path/resource-name</i> </p> </li> <li> <p>A wildcard ARN. The wildcard ARN accepts <code>IAM_PATTERN</code> values with a "*" or "?" in the resource-id segment of the ARN. For example <i>arn:partition:service:::resource-type/resource-path/resource-name</i>. The new symbols are exclusive to the <b>resource-path</b> and <b>resource-name</b> and cannot replace the <b>resource-type</b> or other ARN values. </p> <p>The ARN path and principal name allow unlimited wildcard characters.</p> </li> </ul> <p>Examples of an <b>acceptable</b> wildcard ARN:</p> <ul> <li> <p>arn:aws:iam:::role/ResourceName_*</p> </li> <li> <p>arn:aws:iam:::role/*/ResourceName_?</p> </li> </ul> <p>Examples of an <b>unacceptable</b> wildcard ARN:</p> <ul> <li> <p>arn:aws:iam:::*/ResourceName</p> </li> </ul> <p>You can associate multiple <code>IAM_PATTERN</code>s even if the account has no principal with that name. </p> <p>The "?" wildcard character matches zero or one of any character. This is similar to ".?" in regular regex context. The "*" wildcard character matches any number of any characters. This is similar to ".*" in regular regex context.</p> <p>In the IAM Principal ARN format (<i>arn:partition:iam:::resource-type/resource-path/resource-name</i>), valid resource-type values include <b>user/</b>, <b>group/</b>, or <b>role/</b>. The "?" and "*" characters are allowed only after the resource-type in the resource-id segment. You can use special characters anywhere within the resource-id. </p> <p>The "*" character also matches the "/" character, allowing paths to be formed <i>within</i> the resource-id. For example, <i>arn:aws:iam:::role/<b>*</b>/ResourceName_?</i> matches both <i>arn:aws:iam:::role/pathA/pathB/ResourceName_1</i> and <i>arn:aws:iam:::role/pathA/ResourceName_1</i>. </p>
            principal_type: <p>The principal type. The supported value is <code>IAM</code> if you use a fully defined Amazon Resource Name (ARN), or <code>IAM_PATTERN</code> if you use an ARN with no <code>accountID</code>, with or without wildcard characters. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.associate_principal_with_portfolio_input.AssociatePrincipalWithPortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.associate_principal_with_portfolio_output.AssociatePrincipalWithPortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.associate_principal_with_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.associate_principal_with_portfolio.async_associate_principal_with_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.associate_principal_with_portfolio_input.AssociatePrincipalWithPortfolioInput = {
            "portfolio_id": portfolio_id,
            "principal_arn": principal_arn,
            "principal_type": principal_type,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_product_with_portfolio(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        source_portfolio_id: Optional["capo_service_catalog.types.id.Id"] = None,
    ) -> "capo_service_catalog.types.associate_product_with_portfolio_output.AssociateProductWithPortfolioOutput":
        """<p>Associates the specified product with the specified portfolio.</p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            portfolio_id: <p>The portfolio identifier.</p>
            source_portfolio_id: <p>The identifier of the source portfolio.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.associate_product_with_portfolio_input.AssociateProductWithPortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.associate_product_with_portfolio_output.AssociateProductWithPortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.associate_product_with_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.associate_product_with_portfolio.async_associate_product_with_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.associate_product_with_portfolio_input.AssociateProductWithPortfolioInput = {
            "product_id": product_id,
            "portfolio_id": portfolio_id,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if source_portfolio_id is not None:
            input_["source_portfolio_id"] = source_portfolio_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_service_action_with_provisioning_artifact(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        service_action_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        idempotency_token: Optional[
            "capo_service_catalog.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_service_catalog.types.associate_service_action_with_provisioning_artifact_output.AssociateServiceActionWithProvisioningArtifactOutput":
        """<p>Associates a self-service action with a provisioning artifact.</p>

        Args:
            product_id: <p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>
            service_action_id: <p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests from the same Amazon Web Services account use the same idempotency token, the same response is returned for each repeated request. </p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.associate_service_action_with_provisioning_artifact_input.AssociateServiceActionWithProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.associate_service_action_with_provisioning_artifact_output.AssociateServiceActionWithProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.associate_service_action_with_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.associate_service_action_with_provisioning_artifact.async_associate_service_action_with_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.associate_service_action_with_provisioning_artifact_input.AssociateServiceActionWithProvisioningArtifactInput = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
            "service_action_id": service_action_id,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_tag_option_with_resource(
        self,
        resource_id: "capo_service_catalog.types.resource_id.ResourceId",
        tag_option_id: "capo_service_catalog.types.tag_option_id.TagOptionId",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> "capo_service_catalog.types.associate_tag_option_with_resource_output.AssociateTagOptionWithResourceOutput":
        """<p>Associate the specified TagOption with the specified portfolio or product.</p>

        Args:
            resource_id: <p>The resource identifier.</p>
            tag_option_id: <p>The TagOption identifier.</p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.associate_tag_option_with_resource_input.AssociateTagOptionWithResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.associate_tag_option_with_resource_output.AssociateTagOptionWithResourceOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.associate_tag_option_with_resource

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.associate_tag_option_with_resource.async_associate_tag_option_with_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.associate_tag_option_with_resource_input.AssociateTagOptionWithResourceInput = {
            "resource_id": resource_id,
            "tag_option_id": tag_option_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_associate_service_action_with_provisioning_artifact(
        self,
        service_action_associations: "capo_service_catalog.types.service_action_associations.ServiceActionAssociations",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.batch_associate_service_action_with_provisioning_artifact_output.BatchAssociateServiceActionWithProvisioningArtifactOutput":
        """<p>Associates multiple self-service actions with provisioning artifacts.</p>

        Args:
            service_action_associations: <p>One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.batch_associate_service_action_with_provisioning_artifact_input.BatchAssociateServiceActionWithProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.batch_associate_service_action_with_provisioning_artifact_output.BatchAssociateServiceActionWithProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.batch_associate_service_action_with_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.batch_associate_service_action_with_provisioning_artifact.async_batch_associate_service_action_with_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.batch_associate_service_action_with_provisioning_artifact_input.BatchAssociateServiceActionWithProvisioningArtifactInput = {
            "service_action_associations": service_action_associations
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        service_action_associations: "capo_service_catalog.types.service_action_associations.ServiceActionAssociations",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.batch_disassociate_service_action_from_provisioning_artifact_output.BatchDisassociateServiceActionFromProvisioningArtifactOutput":
        """<p>Disassociates a batch of self-service actions from the specified provisioning artifact.</p>

        Args:
            service_action_associations: <p>One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.batch_disassociate_service_action_from_provisioning_artifact_input.BatchDisassociateServiceActionFromProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.batch_disassociate_service_action_from_provisioning_artifact_output.BatchDisassociateServiceActionFromProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.batch_disassociate_service_action_from_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.batch_disassociate_service_action_from_provisioning_artifact.async_batch_disassociate_service_action_from_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.batch_disassociate_service_action_from_provisioning_artifact_input.BatchDisassociateServiceActionFromProvisioningArtifactInput = {
            "service_action_associations": service_action_associations
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_product(
        self,
        source_product_arn: "capo_service_catalog.types.product_arn.ProductArn",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        target_product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        target_product_name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
        source_provisioning_artifact_identifiers: Optional[
            "capo_service_catalog.types.source_provisioning_artifact_properties.SourceProvisioningArtifactProperties"
        ] = None,
        copy_options: Optional[
            "capo_service_catalog.types.copy_options.CopyOptions"
        ] = None,
    ) -> "capo_service_catalog.types.copy_product_output.CopyProductOutput":
        """<p>Copies the specified source product to the specified target product or a new product.</p> <p>You can copy a product to the same account or another account. You can copy a product to the same Region or another Region. If you copy a product to another account, you must first share the product in a portfolio using <a>CreatePortfolioShare</a>.</p> <p>This operation is performed asynchronously. To track the progress of the operation, use <a>DescribeCopyProductStatus</a>.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            source_product_arn: <p>The Amazon Resource Name (ARN) of the source product.</p>
            target_product_id: <p>The identifier of the target product. By default, a new product is created.</p>
            target_product_name: <p>A name for the target product. The default is the name of the source product.</p>
            source_provisioning_artifact_identifiers: <p>The identifiers of the provisioning artifacts (also known as versions) of the product to copy. By default, all provisioning artifacts are copied.</p>
            copy_options: <p>The copy options. If the value is <code>CopyTags</code>, the tags from the source product are copied to the target product.</p>
            idempotency_token: <p> A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.copy_product_input.CopyProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.copy_product_output.CopyProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.copy_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.copy_product.async_copy_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.copy_product_input.CopyProductInput = {
            "source_product_arn": source_product_arn,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if target_product_id is not None:
            input_["target_product_id"] = target_product_id
        if target_product_name is not None:
            input_["target_product_name"] = target_product_name
        if source_provisioning_artifact_identifiers is not None:
            input_["source_provisioning_artifact_identifiers"] = (
                source_provisioning_artifact_identifiers
            )
        if copy_options is not None:
            input_["copy_options"] = copy_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_constraint(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        product_id: "capo_service_catalog.types.id.Id",
        parameters: "capo_service_catalog.types.constraint_parameters.ConstraintParameters",
        type: "capo_service_catalog.types.constraint_type.ConstraintType",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.constraint_description.ConstraintDescription"
        ] = None,
    ) -> "capo_service_catalog.types.create_constraint_output.CreateConstraintOutput":
        """<p>Creates a constraint.</p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            product_id: <p>The product identifier.</p>
            parameters: <p>The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:</p> <dl> <dt>LAUNCH</dt> <dd> <p>You are required to specify either the <code>RoleArn</code> or the <code>LocalRoleName</code> but can't use both.</p> <p>Specify the <code>RoleArn</code> property as follows:</p> <p> <code>{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}</code> </p> <p>Specify the <code>LocalRoleName</code> property as follows:</p> <p> <code>{"LocalRoleName": "SCBasicLaunchRole"}</code> </p> <p>If you specify the <code>LocalRoleName</code> property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.</p> <note> <p>The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.</p> </note> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>LAUNCH</code> constraint on a product and portfolio.</p> </dd> <dt>NOTIFICATION</dt> <dd> <p>Specify the <code>NotificationArns</code> property as follows:</p> <p> <code>{"NotificationArns" : ["arn:aws:sns:us-east-1:123456789012:Topic"]}</code> </p> </dd> <dt>RESOURCE_UPDATE</dt> <dd> <p>Specify the <code>TagUpdatesOnProvisionedProduct</code> property as follows:</p> <p> <code>{"Version":"2.0","Properties":{"TagUpdateOnProvisionedProduct":"String"}}</code> </p> <p>The <code>TagUpdatesOnProvisionedProduct</code> property accepts a string value of <code>ALLOWED</code> or <code>NOT_ALLOWED</code>.</p> </dd> <dt>STACKSET</dt> <dd> <p>Specify the <code>Parameters</code> property as follows:</p> <p> <code>{"Version": "String", "Properties": {"AccountList": [ "String" ], "RegionList": [ "String" ], "AdminRole": "String", "ExecutionRole": "String"}}</code> </p> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>STACKSET</code> constraint on a product and portfolio.</p> <p>Products with a <code>STACKSET</code> constraint will launch an CloudFormation stack set.</p> </dd> <dt>TEMPLATE</dt> <dd> <p>Specify the <code>Rules</code> property. For more information, see <a href="http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html">Template Constraint Rules</a>.</p> </dd> </dl>
            type: <p>The type of constraint.</p> <ul> <li> <p> <code>LAUNCH</code> </p> </li> <li> <p> <code>NOTIFICATION</code> </p> </li> <li> <p> <code>RESOURCE_UPDATE</code> </p> </li> <li> <p> <code>STACKSET</code> </p> </li> <li> <p> <code>TEMPLATE</code> </p> </li> </ul>
            description: <p>The description of the constraint.</p>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_constraint_input.CreateConstraintInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_constraint_output.CreateConstraintOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_constraint

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_constraint.async_create_constraint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_constraint_input.CreateConstraintInput = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
            "parameters": parameters,
            "type": type,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_portfolio(
        self,
        display_name: "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName",
        provider_name: "capo_service_catalog.types.provider_name.ProviderName",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.portfolio_description.PortfolioDescription"
        ] = None,
        tags: Optional["capo_service_catalog.types.add_tags.AddTags"] = None,
    ) -> "capo_service_catalog.types.create_portfolio_output.CreatePortfolioOutput":
        """<p>Creates a portfolio.</p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            display_name: <p>The name to use for display purposes.</p>
            description: <p>The description of the portfolio.</p>
            provider_name: <p>The name of the portfolio provider.</p>
            tags: <p>One or more tags.</p>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_portfolio_input.CreatePortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_portfolio_output.CreatePortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_portfolio.async_create_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_portfolio_input.CreatePortfolioInput = {
            "display_name": display_name,
            "provider_name": provider_name,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_portfolio_share(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        account_id: Optional["capo_service_catalog.types.account_id.AccountId"] = None,
        organization_node: Optional[
            "capo_service_catalog.types.organization_node.OrganizationNode"
        ] = None,
        share_tag_options: Optional[
            "capo_service_catalog.types.boolean.Boolean"
        ] = None,
        share_principals: Optional["capo_service_catalog.types.boolean.Boolean"] = None,
    ) -> "capo_service_catalog.types.create_portfolio_share_output.CreatePortfolioShareOutput":
        """<p>Shares the specified portfolio with the specified account or organization node. Shares to an organization node can only be created by the management account of an organization or by a delegated administrator. You can share portfolios to an organization, an organizational unit, or a specific account.</p> <p>Note that if a delegated admin is de-registered, they can no longer create portfolio shares.</p> <p> <code>AWSOrganizationsAccess</code> must be enabled in order to create a portfolio share to an organization node.</p> <p>You can't share a shared resource, including portfolios that contain a shared product.</p> <p>If the portfolio share with the specified account or organization node already exists, this action will have no effect and will not return an error. To update an existing share, you must use the <code> UpdatePortfolioShare</code> API instead. </p> <note> <p>When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is <i>not</i> an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using <code>PrincipalType</code> as <code>IAM</code>. With this configuration, the <code>PrincipalARN</code> must already exist in the recipient account before it can be associated. </p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            account_id: <p>The Amazon Web Services account ID. For example, <code>123456789012</code>.</p>
            organization_node: <p>The organization node to whom you are going to share. When you pass <code>OrganizationNode</code>, it creates <code>PortfolioShare</code> for all of the Amazon Web Services accounts that are associated to the <code>OrganizationNode</code>. The output returns a <code>PortfolioShareToken</code>, which enables the administrator to monitor the status of the <code>PortfolioShare</code> creation process.</p>
            share_tag_options: <p>Enables or disables <code>TagOptions </code> sharing when creating the portfolio share. If this flag is not provided, TagOptions sharing is disabled.</p>
            share_principals: <p>This parameter is only supported for portfolios with an <b>OrganizationalNode</b> Type of <code>ORGANIZATION</code> or <code>ORGANIZATIONAL_UNIT</code>. </p> <p>Enables or disables <code>Principal</code> sharing when creating the portfolio share. If you do <b>not</b> provide this flag, principal sharing is disabled. </p> <p>When you enable Principal Name Sharing for a portfolio share, the share recipient account end users with a principal that matches any of the associated IAM patterns can provision products from the portfolio. Once shared, the share recipient can view associations of <code>PrincipalType</code>: <code>IAM_PATTERN</code> on their portfolio. You can create the principals in the recipient account before or after creating the share. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_portfolio_share_input.CreatePortfolioShareInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_portfolio_share_output.CreatePortfolioShareOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_portfolio_share

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_portfolio_share.async_create_portfolio_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_portfolio_share_input.CreatePortfolioShareInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if account_id is not None:
            input_["account_id"] = account_id
        if organization_node is not None:
            input_["organization_node"] = organization_node
        if share_tag_options is not None:
            input_["share_tag_options"] = share_tag_options
        if share_principals is not None:
            input_["share_principals"] = share_principals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_product(
        self,
        name: "capo_service_catalog.types.product_view_name.ProductViewName",
        owner: "capo_service_catalog.types.product_view_owner.ProductViewOwner",
        product_type: "capo_service_catalog.types.product_type.ProductType",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.product_view_short_description.ProductViewShortDescription"
        ] = None,
        distributor: Optional[
            "capo_service_catalog.types.product_view_owner.ProductViewOwner"
        ] = None,
        support_description: Optional[
            "capo_service_catalog.types.support_description.SupportDescription"
        ] = None,
        support_email: Optional[
            "capo_service_catalog.types.support_email.SupportEmail"
        ] = None,
        support_url: Optional[
            "capo_service_catalog.types.support_url.SupportUrl"
        ] = None,
        tags: Optional["capo_service_catalog.types.add_tags.AddTags"] = None,
        provisioning_artifact_parameters: Optional[
            "capo_service_catalog.types.provisioning_artifact_properties.ProvisioningArtifactProperties"
        ] = None,
        source_connection: Optional[
            "capo_service_catalog.types.source_connection.SourceConnection"
        ] = None,
    ) -> "capo_service_catalog.types.create_product_output.CreateProductOutput":
        r"""<p>Creates a product.</p> <p>A delegated admin is authorized to invoke this command.</p> <p>The user or role that performs this operation must have the <code>cloudformation:GetTemplate</code> IAM policy permission. This policy permission is required when using the <code>ImportFromPhysicalId</code> template source in the information data section.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            name: <p>The name of the product.</p>
            owner: <p>The owner of the product.</p>
            description: <p>The description of the product.</p>
            distributor: <p>The distributor of the product.</p>
            support_description: <p>The support information about the product.</p>
            support_email: <p>The contact email for product support.</p>
            support_url: <p>The contact URL for product support.</p> <p> <code>^https?:\/\// </code>/ is the pattern used to validate SupportUrl.</p>
            product_type: <p>The type of product.</p>
            tags: <p>One or more tags.</p>
            provisioning_artifact_parameters: <p>The configuration of the provisioning artifact. </p>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>
            source_connection: <p>Specifies connection details for the created product and syncs the product to the connection source artifact. This automatically manages the product's artifacts based on changes to the source. The <code>SourceConnection</code> parameter consists of the following sub-fields.</p> <ul> <li> <p> <code>Type</code> </p> </li> <li> <p> <code>ConnectionParamters</code> </p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_product_input.CreateProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_product_output.CreateProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_product.async_create_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_product_input.CreateProductInput = {
            "name": name,
            "owner": owner,
            "product_type": product_type,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if description is not None:
            input_["description"] = description
        if distributor is not None:
            input_["distributor"] = distributor
        if support_description is not None:
            input_["support_description"] = support_description
        if support_email is not None:
            input_["support_email"] = support_email
        if support_url is not None:
            input_["support_url"] = support_url
        if tags is not None:
            input_["tags"] = tags
        if provisioning_artifact_parameters is not None:
            input_["provisioning_artifact_parameters"] = (
                provisioning_artifact_parameters
            )
        if source_connection is not None:
            input_["source_connection"] = source_connection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_provisioned_product_plan(
        self,
        plan_name: "capo_service_catalog.types.provisioned_product_plan_name.ProvisionedProductPlanName",
        plan_type: "capo_service_catalog.types.provisioned_product_plan_type.ProvisionedProductPlanType",
        product_id: "capo_service_catalog.types.id.Id",
        provisioned_product_name: "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        notification_arns: Optional[
            "capo_service_catalog.types.notification_arns.NotificationArns"
        ] = None,
        path_id: Optional["capo_service_catalog.types.id.Id"] = None,
        provisioning_parameters: Optional[
            "capo_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
        ] = None,
        tags: Optional["capo_service_catalog.types.tags.Tags"] = None,
    ) -> "capo_service_catalog.types.create_provisioned_product_plan_output.CreateProvisionedProductPlanOutput":
        """<p>Creates a plan.</p> <p>A plan includes the list of resources to be created (when provisioning a new product) or modified (when updating a provisioned product) when the plan is executed.</p> <p>You can create one plan for each provisioned product. To create a plan for an existing provisioned product, the product status must be AVAILABLE or TAINTED.</p> <p>To view the resource changes in the change set, use <a>DescribeProvisionedProductPlan</a>. To create or modify the provisioned product, use <a>ExecuteProvisionedProductPlan</a>.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            plan_name: <p>The name of the plan.</p>
            plan_type: <p>The plan type.</p>
            notification_arns: <p>Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.</p>
            path_id: <p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>.</p>
            product_id: <p>The product identifier.</p>
            provisioned_product_name: <p>A user-friendly name for the provisioned product. This value must be unique for the Amazon Web Services account and cannot be updated after the product is provisioned.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact.</p>
            provisioning_parameters: <p>Parameters specified by the administrator that are required for provisioning the product.</p>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>
            tags: <p>One or more tags.</p> <p>If the plan is for an existing provisioned product, the product must have a <code>RESOURCE_UPDATE</code> constraint with <code>TagUpdatesOnProvisionedProduct</code> set to <code>ALLOWED</code> to allow tag updates.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_provisioned_product_plan_input.CreateProvisionedProductPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_provisioned_product_plan_output.CreateProvisionedProductPlanOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_provisioned_product_plan

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_provisioned_product_plan.async_create_provisioned_product_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_provisioned_product_plan_input.CreateProvisionedProductPlanInput = {
            "plan_name": plan_name,
            "plan_type": plan_type,
            "product_id": product_id,
            "provisioned_product_name": provisioned_product_name,
            "provisioning_artifact_id": provisioning_artifact_id,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if notification_arns is not None:
            input_["notification_arns"] = notification_arns
        if path_id is not None:
            input_["path_id"] = path_id
        if provisioning_parameters is not None:
            input_["provisioning_parameters"] = provisioning_parameters
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_provisioning_artifact(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        parameters: "capo_service_catalog.types.provisioning_artifact_properties.ProvisioningArtifactProperties",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.create_provisioning_artifact_output.CreateProvisioningArtifactOutput":
        """<p>Creates a provisioning artifact (also known as a version) for the specified product.</p> <p>You cannot create a provisioning artifact for a product that was shared with you.</p> <p>The user or role that performs this operation must have the <code>cloudformation:GetTemplate</code> IAM policy permission. This policy permission is required when using the <code>ImportFromPhysicalId</code> template source in the information data section.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            parameters: <p>The configuration for the provisioning artifact.</p>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_provisioning_artifact_input.CreateProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_provisioning_artifact_output.CreateProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_provisioning_artifact.async_create_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_provisioning_artifact_input.CreateProvisioningArtifactInput = {
            "product_id": product_id,
            "parameters": parameters,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_service_action(
        self,
        name: "capo_service_catalog.types.service_action_name.ServiceActionName",
        definition_type: "capo_service_catalog.types.service_action_definition_type.ServiceActionDefinitionType",
        definition: "capo_service_catalog.types.service_action_definition_map.ServiceActionDefinitionMap",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        description: Optional[
            "capo_service_catalog.types.service_action_description.ServiceActionDescription"
        ] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.create_service_action_output.CreateServiceActionOutput":
        r"""<p>Creates a self-service action.</p>

        Args:
            name: <p>The self-service action name.</p>
            definition_type: <p>The service action definition type. For example, <code>SSM_AUTOMATION</code>.</p>
            definition: <p>The self-service action definition. Can be one of the following:</p> <dl> <dt>Name</dt> <dd> <p>The name of the Amazon Web Services Systems Manager document (SSM document). For example, <code>AWS-RestartEC2Instance</code>.</p> <p>If you are using a shared SSM document, you must provide the ARN instead of the name.</p> </dd> <dt>Version</dt> <dd> <p>The Amazon Web Services Systems Manager automation document version. For example, <code>"Version": "1"</code> </p> </dd> <dt>AssumeRole</dt> <dd> <p>The Amazon Resource Name (ARN) of the role that performs the self-service actions on your behalf. For example, <code>"AssumeRole": "arn:aws:iam::12345678910:role/ActionRole"</code>.</p> <p>To reuse the provisioned product launch role, set to <code>"AssumeRole": "LAUNCH_ROLE"</code>.</p> </dd> <dt>Parameters</dt> <dd> <p>The list of parameters in JSON format.</p> <p>For example: <code>[{\"Name\":\"InstanceId\",\"Type\":\"TARGET\"}]</code> or <code>[{\"Name\":\"InstanceId\",\"Type\":\"TEXT_VALUE\"}]</code>.</p> </dd> </dl>
            description: <p>The self-service action description.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_service_action_input.CreateServiceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_service_action_output.CreateServiceActionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_service_action

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_service_action.async_create_service_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_service_action_input.CreateServiceActionInput = {
            "name": name,
            "definition_type": definition_type,
            "definition": definition,
            "idempotency_token": idempotency_token,
        }
        if description is not None:
            input_["description"] = description
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_tag_option(
        self,
        key: "capo_service_catalog.types.tag_option_key.TagOptionKey",
        value: "capo_service_catalog.types.tag_option_value.TagOptionValue",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> "capo_service_catalog.types.create_tag_option_output.CreateTagOptionOutput":
        """<p>Creates a TagOption.</p>

        Args:
            key: <p>The TagOption key.</p>
            value: <p>The TagOption value.</p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.create_tag_option_input.CreateTagOptionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.create_tag_option_output.CreateTagOptionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.create_tag_option

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.create_tag_option.async_create_tag_option(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.create_tag_option_input.CreateTagOptionInput = {
            "key": key,
            "value": value,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_constraint(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.delete_constraint_output.DeleteConstraintOutput":
        """<p>Deletes the specified constraint.</p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The identifier of the constraint.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_constraint_input.DeleteConstraintInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_constraint_output.DeleteConstraintOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_constraint

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_constraint.async_delete_constraint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_constraint_input.DeleteConstraintInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_portfolio(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.delete_portfolio_output.DeletePortfolioOutput":
        """<p>Deletes the specified portfolio.</p> <p>You cannot delete a portfolio if it was shared with you or if it has associated products, users, constraints, or shared accounts.</p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The portfolio identifier.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>A resource that is currently in use. Ensure that the resource is not in use and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_portfolio_input.DeletePortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_portfolio_output.DeletePortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_portfolio.async_delete_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_portfolio_input.DeletePortfolioInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_portfolio_share(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        account_id: Optional["capo_service_catalog.types.account_id.AccountId"] = None,
        organization_node: Optional[
            "capo_service_catalog.types.organization_node.OrganizationNode"
        ] = None,
    ) -> "capo_service_catalog.types.delete_portfolio_share_output.DeletePortfolioShareOutput":
        """<p>Stops sharing the specified portfolio with the specified account or organization node. Shares to an organization node can only be deleted by the management account of an organization or by a delegated administrator.</p> <p>Note that if a delegated admin is de-registered, portfolio shares created from that account are removed.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            account_id: <p>The Amazon Web Services account ID.</p>
            organization_node: <p>The organization node to whom you are going to stop sharing.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_portfolio_share_input.DeletePortfolioShareInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_portfolio_share_output.DeletePortfolioShareOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_portfolio_share

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_portfolio_share.async_delete_portfolio_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_portfolio_share_input.DeletePortfolioShareInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if account_id is not None:
            input_["account_id"] = account_id
        if organization_node is not None:
            input_["organization_node"] = organization_node

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_product(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.delete_product_output.DeleteProductOutput":
        """<p>Deletes the specified product.</p> <p>You cannot delete a product if it was shared with you or is associated with a portfolio.</p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The product identifier.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>A resource that is currently in use. Ensure that the resource is not in use and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_product_input.DeleteProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_product_output.DeleteProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_product.async_delete_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_product_input.DeleteProductInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_provisioned_product_plan(
        self,
        plan_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        ignore_errors: Optional[
            "capo_service_catalog.types.ignore_errors.IgnoreErrors"
        ] = None,
    ) -> "capo_service_catalog.types.delete_provisioned_product_plan_output.DeleteProvisionedProductPlanOutput":
        """<p>Deletes the specified plan.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            plan_id: <p>The plan identifier.</p>
            ignore_errors: <p>If set to true, Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_provisioned_product_plan_input.DeleteProvisionedProductPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_provisioned_product_plan_output.DeleteProvisionedProductPlanOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_provisioned_product_plan

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_provisioned_product_plan.async_delete_provisioned_product_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_provisioned_product_plan_input.DeleteProvisionedProductPlanInput = {
            "plan_id": plan_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if ignore_errors is not None:
            input_["ignore_errors"] = ignore_errors

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_provisioning_artifact(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.delete_provisioning_artifact_output.DeleteProvisioningArtifactOutput":
        """<p>Deletes the specified provisioning artifact (also known as a version) for the specified product.</p> <p>You cannot delete a provisioning artifact associated with a product that was shared with you. You cannot delete the last provisioning artifact for a product, because a product must have at least one provisioning artifact.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>A resource that is currently in use. Ensure that the resource is not in use and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_provisioning_artifact_input.DeleteProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_provisioning_artifact_output.DeleteProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_provisioning_artifact.async_delete_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_provisioning_artifact_input.DeleteProvisioningArtifactInput = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service_action(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        idempotency_token: Optional[
            "capo_service_catalog.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_service_catalog.types.delete_service_action_output.DeleteServiceActionOutput":
        """<p>Deletes a self-service action.</p>

        Args:
            id: <p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests from the same Amazon Web Services account use the same idempotency token, the same response is returned for each repeated request. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>A resource that is currently in use. Ensure that the resource is not in use and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_service_action_input.DeleteServiceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_service_action_output.DeleteServiceActionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_service_action

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_service_action.async_delete_service_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_service_action_input.DeleteServiceActionInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tag_option(
        self,
        id: "capo_service_catalog.types.tag_option_id.TagOptionId",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> "capo_service_catalog.types.delete_tag_option_output.DeleteTagOptionOutput":
        """<p>Deletes the specified TagOption.</p> <p>You cannot delete a TagOption if it is associated with a product or portfolio.</p>

        Args:
            id: <p>The TagOption identifier.</p>

        Raises:
            capo_service_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>A resource that is currently in use. Ensure that the resource is not in use and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.delete_tag_option_input.DeleteTagOptionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.delete_tag_option_output.DeleteTagOptionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.delete_tag_option

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.delete_tag_option.async_delete_tag_option(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.delete_tag_option_input.DeleteTagOptionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_constraint(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> (
        "capo_service_catalog.types.describe_constraint_output.DescribeConstraintOutput"
    ):
        """<p>Gets information about the specified constraint.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The identifier of the constraint.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_constraint_input.DescribeConstraintInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_constraint_output.DescribeConstraintOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_constraint

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_constraint.async_describe_constraint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_constraint_input.DescribeConstraintInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_copy_product_status(
        self,
        copy_product_token: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.describe_copy_product_status_output.DescribeCopyProductStatusOutput":
        """<p>Gets the status of the specified copy product operation.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            copy_product_token: <p>The token for the copy product operation. This token is returned by <a>CopyProduct</a>.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_copy_product_status_input.DescribeCopyProductStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_copy_product_status_output.DescribeCopyProductStatusOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_copy_product_status

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_copy_product_status.async_describe_copy_product_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_copy_product_status_input.DescribeCopyProductStatusInput = {
            "copy_product_token": copy_product_token
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_portfolio(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.describe_portfolio_output.DescribePortfolioOutput":
        """<p>Gets information about the specified portfolio.</p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The portfolio identifier.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_portfolio_input.DescribePortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_portfolio_output.DescribePortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_portfolio.async_describe_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_portfolio_input.DescribePortfolioInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_portfolio_shares(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        type: "capo_service_catalog.types.describe_portfolio_share_type.DescribePortfolioShareType",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "capo_service_catalog.types.describe_portfolio_shares_output.DescribePortfolioSharesOutput":
        """<p>Returns a summary of each of the portfolio shares that were created for the specified portfolio.</p> <p>You can use this API to determine which accounts or organizational nodes this portfolio have been shared, whether the recipient entity has imported the share, and whether TagOptions are included with the share.</p> <p>The <code>PortfolioId</code> and <code>Type</code> parameters are both required.</p>

        Args:
            portfolio_id: <p>The unique identifier of the portfolio for which shares will be retrieved.</p>
            type: <p>The type of portfolio share to summarize. This field acts as a filter on the type of portfolio share, which can be one of the following:</p> <p>1. <code>ACCOUNT</code> - Represents an external account to account share.</p> <p>2. <code>ORGANIZATION</code> - Represents a share to an organization. This share is available to every account in the organization.</p> <p>3. <code>ORGANIZATIONAL_UNIT</code> - Represents a share to an organizational unit.</p> <p>4. <code>ORGANIZATION_MEMBER_ACCOUNT</code> - Represents a share to an account in the organization.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_portfolio_shares_input.DescribePortfolioSharesInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_portfolio_shares_output.DescribePortfolioSharesOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_portfolio_shares

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_portfolio_shares.async_describe_portfolio_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_portfolio_shares_input.DescribePortfolioSharesInput = {
            "portfolio_id": portfolio_id,
            "type": type,
        }
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_portfolio_shares(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        type: "capo_service_catalog.types.describe_portfolio_share_type.DescribePortfolioShareType",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.describe_portfolio_shares_output.DescribePortfolioSharesOutput]":
        _token = page_token
        while True:
            _response = await self.describe_portfolio_shares(
                portfolio_id,
                type,
                config_overrides=config_overrides,
                page_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def describe_portfolio_share_status(
        self,
        portfolio_share_token: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> "capo_service_catalog.types.describe_portfolio_share_status_output.DescribePortfolioShareStatusOutput":
        """<p>Gets the status of the specified portfolio share operation. This API can only be called by the management account in the organization or by a delegated admin.</p>

        Args:
            portfolio_share_token: <p>The token for the portfolio share operation. This token is returned either by CreatePortfolioShare or by DeletePortfolioShare.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_portfolio_share_status_input.DescribePortfolioShareStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_portfolio_share_status_output.DescribePortfolioShareStatusOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_portfolio_share_status

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_portfolio_share_status.async_describe_portfolio_share_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_portfolio_share_status_input.DescribePortfolioShareStatusInput = {
            "portfolio_share_token": portfolio_share_token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_product(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        id: Optional["capo_service_catalog.types.id.Id"] = None,
        name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
    ) -> "capo_service_catalog.types.describe_product_output.DescribeProductOutput":
        """<p>Gets information about the specified product.</p> <note> <p> Running this operation with administrator access results in a failure. <a>DescribeProductAsAdmin</a> should be used instead. </p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The product identifier.</p>
            name: <p>The product name.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_product_input.DescribeProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_product_output.DescribeProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_product.async_describe_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_product_input.DescribeProductInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if id is not None:
            input_["id"] = id
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_product_as_admin(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        id: Optional["capo_service_catalog.types.id.Id"] = None,
        name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
        source_portfolio_id: Optional["capo_service_catalog.types.id.Id"] = None,
    ) -> "capo_service_catalog.types.describe_product_as_admin_output.DescribeProductAsAdminOutput":
        """<p>Gets information about the specified product. This operation is run with administrator access.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The product identifier.</p>
            name: <p>The product name.</p>
            source_portfolio_id: <p>The unique identifier of the shared portfolio that the specified product is associated with.</p> <p>You can provide this parameter to retrieve the shared TagOptions associated with the product. If this parameter is provided and if TagOptions sharing is enabled in the portfolio share, the API returns both local and shared TagOptions associated with the product. Otherwise only local TagOptions will be returned. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_product_as_admin_input.DescribeProductAsAdminInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_product_as_admin_output.DescribeProductAsAdminOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_product_as_admin

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_product_as_admin.async_describe_product_as_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_product_as_admin_input.DescribeProductAsAdminInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if id is not None:
            input_["id"] = id
        if name is not None:
            input_["name"] = name
        if source_portfolio_id is not None:
            input_["source_portfolio_id"] = source_portfolio_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_product_view(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.describe_product_view_output.DescribeProductViewOutput":
        """<p>Gets information about the specified product.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The product view identifier.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_product_view_input.DescribeProductViewInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_product_view_output.DescribeProductViewOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_product_view

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_product_view.async_describe_product_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_product_view_input.DescribeProductViewInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_provisioned_product(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        id: Optional["capo_service_catalog.types.id.Id"] = None,
        name: Optional[
            "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
        ] = None,
    ) -> "capo_service_catalog.types.describe_provisioned_product_output.DescribeProvisionedProductOutput":
        """<p>Gets information about the specified provisioned product.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The provisioned product identifier. You must provide the name or ID, but not both.</p> <p>If you do not provide a name or ID, or you provide both name and ID, an <code>InvalidParametersException</code> will occur.</p>
            name: <p>The name of the provisioned product. You must provide the name or ID, but not both.</p> <p>If you do not provide a name or ID, or you provide both name and ID, an <code>InvalidParametersException</code> will occur.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_provisioned_product_input.DescribeProvisionedProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_provisioned_product_output.DescribeProvisionedProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioned_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioned_product.async_describe_provisioned_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_provisioned_product_input.DescribeProvisionedProductInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if id is not None:
            input_["id"] = id
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_provisioned_product_plan(
        self,
        plan_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.describe_provisioned_product_plan_output.DescribeProvisionedProductPlanOutput":
        """<p>Gets information about the resource changes for the specified plan.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            plan_id: <p>The plan identifier.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_provisioned_product_plan_input.DescribeProvisionedProductPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_provisioned_product_plan_output.DescribeProvisionedProductPlanOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioned_product_plan

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioned_product_plan.async_describe_provisioned_product_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_provisioned_product_plan_input.DescribeProvisionedProductPlanInput = {
            "plan_id": plan_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_provisioning_artifact(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        provisioning_artifact_id: Optional["capo_service_catalog.types.id.Id"] = None,
        product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        provisioning_artifact_name: Optional[
            "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
        ] = None,
        product_name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
        verbose: Optional["capo_service_catalog.types.verbose.Verbose"] = None,
        include_provisioning_artifact_parameters: Optional[
            "capo_service_catalog.types.boolean.Boolean"
        ] = None,
    ) -> "capo_service_catalog.types.describe_provisioning_artifact_output.DescribeProvisioningArtifactOutput":
        """<p>Gets information about the specified provisioning artifact (also known as a version) for the specified product.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact.</p>
            product_id: <p>The product identifier.</p>
            provisioning_artifact_name: <p>The provisioning artifact name.</p>
            product_name: <p>The product name.</p>
            verbose: <p>Indicates whether a verbose level of detail is enabled.</p>
            include_provisioning_artifact_parameters: <p>Indicates if the API call response does or does not include additional details about the provisioning parameters. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_provisioning_artifact_input.DescribeProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_provisioning_artifact_output.DescribeProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioning_artifact.async_describe_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_provisioning_artifact_input.DescribeProvisioningArtifactInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if provisioning_artifact_id is not None:
            input_["provisioning_artifact_id"] = provisioning_artifact_id
        if product_id is not None:
            input_["product_id"] = product_id
        if provisioning_artifact_name is not None:
            input_["provisioning_artifact_name"] = provisioning_artifact_name
        if product_name is not None:
            input_["product_name"] = product_name
        if verbose is not None:
            input_["verbose"] = verbose
        if include_provisioning_artifact_parameters is not None:
            input_["include_provisioning_artifact_parameters"] = (
                include_provisioning_artifact_parameters
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_provisioning_parameters(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        product_name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
        provisioning_artifact_id: Optional["capo_service_catalog.types.id.Id"] = None,
        provisioning_artifact_name: Optional[
            "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
        ] = None,
        path_id: Optional["capo_service_catalog.types.id.Id"] = None,
        path_name: Optional[
            "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
        ] = None,
    ) -> "capo_service_catalog.types.describe_provisioning_parameters_output.DescribeProvisioningParametersOutput":
        """<p>Gets information about the configuration required to provision the specified product using the specified provisioning artifact.</p> <p>If the output contains a TagOption key with an empty list of values, there is a TagOption conflict for that key. The end user cannot take action to fix the conflict, and launch is not blocked. In subsequent calls to <a>ProvisionProduct</a>, do not include conflicted TagOption keys as tags, or this causes the error "Parameter validation failed: Missing required parameter in Tags[<i>N</i>]:<i>Value</i>". Tag the provisioned product with the value <code>sc-tagoption-conflict-portfolioId-productId</code>.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier. You must provide the product name or ID, but not both.</p>
            product_name: <p>The name of the product. You must provide the name or ID, but not both.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact. You must provide the name or ID, but not both.</p>
            provisioning_artifact_name: <p>The name of the provisioning artifact. You must provide the name or ID, but not both.</p>
            path_id: <p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>. You must provide the name or ID, but not both.</p>
            path_name: <p>The name of the path. You must provide the name or ID, but not both.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_provisioning_parameters_input.DescribeProvisioningParametersInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_provisioning_parameters_output.DescribeProvisioningParametersOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioning_parameters

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_provisioning_parameters.async_describe_provisioning_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_provisioning_parameters_input.DescribeProvisioningParametersInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if product_id is not None:
            input_["product_id"] = product_id
        if product_name is not None:
            input_["product_name"] = product_name
        if provisioning_artifact_id is not None:
            input_["provisioning_artifact_id"] = provisioning_artifact_id
        if provisioning_artifact_name is not None:
            input_["provisioning_artifact_name"] = provisioning_artifact_name
        if path_id is not None:
            input_["path_id"] = path_id
        if path_name is not None:
            input_["path_name"] = path_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_record(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
    ) -> "capo_service_catalog.types.describe_record_output.DescribeRecordOutput":
        """<p>Gets information about the specified request operation.</p> <p>Use this operation after calling a request operation (for example, <a>ProvisionProduct</a>, <a>TerminateProvisionedProduct</a>, or <a>UpdateProvisionedProduct</a>). </p> <note> <p>If a provisioned product was transferred to a new owner using <a>UpdateProvisionedProductProperties</a>, the new owner will be able to describe all past records for that product. The previous owner will no longer be able to describe the records, but will be able to use <a>ListRecordHistory</a> to see the product's history from when he was the owner.</p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The record identifier of the provisioned product. This identifier is returned by the request operation.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_record_input.DescribeRecordInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_record_output.DescribeRecordOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_record

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_record.async_describe_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_record_input.DescribeRecordInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_service_action(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.describe_service_action_output.DescribeServiceActionOutput":
        """<p>Describes a self-service action.</p>

        Args:
            id: <p>The self-service action identifier.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_service_action_input.DescribeServiceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_service_action_output.DescribeServiceActionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_service_action

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_service_action.async_describe_service_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_service_action_input.DescribeServiceActionInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_service_action_execution_parameters(
        self,
        provisioned_product_id: "capo_service_catalog.types.id.Id",
        service_action_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.describe_service_action_execution_parameters_output.DescribeServiceActionExecutionParametersOutput":
        """<p>Finds the default parameters for a specific self-service action on a specific provisioned product and returns a map of the results to the user.</p>

        Args:
            provisioned_product_id: <p>The identifier of the provisioned product.</p>
            service_action_id: <p>The self-service action identifier.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_service_action_execution_parameters_input.DescribeServiceActionExecutionParametersInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_service_action_execution_parameters_output.DescribeServiceActionExecutionParametersOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_service_action_execution_parameters

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_service_action_execution_parameters.async_describe_service_action_execution_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_service_action_execution_parameters_input.DescribeServiceActionExecutionParametersInput = {
            "provisioned_product_id": provisioned_product_id,
            "service_action_id": service_action_id,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_tag_option(
        self,
        id: "capo_service_catalog.types.tag_option_id.TagOptionId",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> (
        "capo_service_catalog.types.describe_tag_option_output.DescribeTagOptionOutput"
    ):
        """<p>Gets information about the specified TagOption.</p>

        Args:
            id: <p>The TagOption identifier.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.describe_tag_option_input.DescribeTagOptionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.describe_tag_option_output.DescribeTagOptionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.describe_tag_option

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.describe_tag_option.async_describe_tag_option(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.describe_tag_option_input.DescribeTagOptionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_aws_organizations_access(
        self, *, config_overrides: Optional[AsyncServiceCatalogClientConfig] = None
    ) -> "capo_service_catalog.types.disable_aws_organizations_access_output.DisableAWSOrganizationsAccessOutput":
        """<p>Disable portfolio sharing through the Organizations service. This command will not delete your current shares, but prevents you from creating new shares throughout your organization. Current shares are not kept in sync with your organization structure if the structure changes after calling this API. Only the management account in the organization can call this API.</p> <p>You cannot call this API if there are active delegated administrators in the organization.</p> <p>Note that a delegated administrator is not authorized to invoke <code>DisableAWSOrganizationsAccess</code>.</p> <important> <p>If you share an Service Catalog portfolio in an organization within Organizations, and then disable Organizations access for Service Catalog, the portfolio access permissions will not sync with the latest changes to the organization structure. Specifically, accounts that you removed from the organization after disabling Service Catalog access will retain access to the previously shared portfolio.</p> </important>

        Raises:
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.disable_aws_organizations_access_input.DisableAWSOrganizationsAccessInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.disable_aws_organizations_access_output.DisableAWSOrganizationsAccessOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.disable_aws_organizations_access

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.disable_aws_organizations_access.async_disable_aws_organizations_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.disable_aws_organizations_access_input.DisableAWSOrganizationsAccessInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_budget_from_resource(
        self,
        budget_name: "capo_service_catalog.types.budget_name.BudgetName",
        resource_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> "capo_service_catalog.types.disassociate_budget_from_resource_output.DisassociateBudgetFromResourceOutput":
        """<p>Disassociates the specified budget from the specified resource.</p>

        Args:
            budget_name: <p>The name of the budget you want to disassociate.</p>
            resource_id: <p>The resource identifier you want to disassociate from. Either a portfolio-id or a product-id.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.disassociate_budget_from_resource_input.DisassociateBudgetFromResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.disassociate_budget_from_resource_output.DisassociateBudgetFromResourceOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.disassociate_budget_from_resource

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.disassociate_budget_from_resource.async_disassociate_budget_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.disassociate_budget_from_resource_input.DisassociateBudgetFromResourceInput = {
            "budget_name": budget_name,
            "resource_id": resource_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_principal_from_portfolio(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        principal_arn: "capo_service_catalog.types.principal_arn.PrincipalARN",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        principal_type: Optional[
            "capo_service_catalog.types.principal_type.PrincipalType"
        ] = None,
    ) -> "capo_service_catalog.types.disassociate_principal_from_portfolio_output.DisassociatePrincipalFromPortfolioOutput":
        """<p>Disassociates a previously associated principal ARN from a specified portfolio.</p> <p>The <code>PrincipalType</code> and <code>PrincipalARN</code> must match the <code>AssociatePrincipalWithPortfolio</code> call request details. For example, to disassociate an association created with a <code>PrincipalARN</code> of <code>PrincipalType</code> IAM you must use the <code>PrincipalType</code> IAM when calling <code>DisassociatePrincipalFromPortfolio</code>. </p> <p>For portfolios that have been shared with principal name sharing enabled: after disassociating a principal, share recipient accounts will no longer be able to provision products in this portfolio using a role matching the name of the associated principal. </p> <p>For more information, review <a href="https://docs.aws.amazon.com/cli/latest/reference/servicecatalog/associate-principal-with-portfolio.html#options">associate-principal-with-portfolio</a> in the Amazon Web Services CLI Command Reference. </p> <note> <p>If you disassociate a principal from a portfolio, with PrincipalType as <code>IAM</code>, the same principal will still have access to the portfolio if it matches one of the associated principals of type <code>IAM_PATTERN</code>. To fully remove access for a principal, verify all the associated Principals of type <code>IAM_PATTERN</code>, and then ensure you disassociate any <code>IAM_PATTERN</code> principals that match the principal whose access you are removing.</p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            principal_arn: <p>The ARN of the principal (user, role, or group). This field allows an ARN with no <code>accountID</code> with or without wildcard characters if <code>PrincipalType</code> is <code>IAM_PATTERN</code>.</p>
            principal_type: <p>The supported value is <code>IAM</code> if you use a fully defined ARN, or <code>IAM_PATTERN</code> if you specify an <code>IAM</code> ARN with no AccountId, with or without wildcard characters. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.disassociate_principal_from_portfolio_input.DisassociatePrincipalFromPortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.disassociate_principal_from_portfolio_output.DisassociatePrincipalFromPortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.disassociate_principal_from_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.disassociate_principal_from_portfolio.async_disassociate_principal_from_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.disassociate_principal_from_portfolio_input.DisassociatePrincipalFromPortfolioInput = {
            "portfolio_id": portfolio_id,
            "principal_arn": principal_arn,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if principal_type is not None:
            input_["principal_type"] = principal_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_product_from_portfolio(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.disassociate_product_from_portfolio_output.DisassociateProductFromPortfolioOutput":
        """<p>Disassociates the specified product from the specified portfolio. </p> <p>A delegated admin is authorized to invoke this command.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            portfolio_id: <p>The portfolio identifier.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>A resource that is currently in use. Ensure that the resource is not in use and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.disassociate_product_from_portfolio_input.DisassociateProductFromPortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.disassociate_product_from_portfolio_output.DisassociateProductFromPortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.disassociate_product_from_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.disassociate_product_from_portfolio.async_disassociate_product_from_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.disassociate_product_from_portfolio_input.DisassociateProductFromPortfolioInput = {
            "product_id": product_id,
            "portfolio_id": portfolio_id,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_service_action_from_provisioning_artifact(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        service_action_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        idempotency_token: Optional[
            "capo_service_catalog.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_service_catalog.types.disassociate_service_action_from_provisioning_artifact_output.DisassociateServiceActionFromProvisioningArtifactOutput":
        """<p>Disassociates the specified self-service action association from the specified provisioning artifact.</p>

        Args:
            product_id: <p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>
            service_action_id: <p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests from the same Amazon Web Services account use the same idempotency token, the same response is returned for each repeated request. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.disassociate_service_action_from_provisioning_artifact_input.DisassociateServiceActionFromProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.disassociate_service_action_from_provisioning_artifact_output.DisassociateServiceActionFromProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.disassociate_service_action_from_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.disassociate_service_action_from_provisioning_artifact.async_disassociate_service_action_from_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.disassociate_service_action_from_provisioning_artifact_input.DisassociateServiceActionFromProvisioningArtifactInput = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
            "service_action_id": service_action_id,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_tag_option_from_resource(
        self,
        resource_id: "capo_service_catalog.types.resource_id.ResourceId",
        tag_option_id: "capo_service_catalog.types.tag_option_id.TagOptionId",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
    ) -> "capo_service_catalog.types.disassociate_tag_option_from_resource_output.DisassociateTagOptionFromResourceOutput":
        """<p>Disassociates the specified TagOption from the specified resource.</p>

        Args:
            resource_id: <p>The resource identifier.</p>
            tag_option_id: <p>The TagOption identifier.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.disassociate_tag_option_from_resource_input.DisassociateTagOptionFromResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.disassociate_tag_option_from_resource_output.DisassociateTagOptionFromResourceOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.disassociate_tag_option_from_resource

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.disassociate_tag_option_from_resource.async_disassociate_tag_option_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.disassociate_tag_option_from_resource_input.DisassociateTagOptionFromResourceInput = {
            "resource_id": resource_id,
            "tag_option_id": tag_option_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_aws_organizations_access(
        self, *, config_overrides: Optional[AsyncServiceCatalogClientConfig] = None
    ) -> "capo_service_catalog.types.enable_aws_organizations_access_output.EnableAWSOrganizationsAccessOutput":
        """<p>Enable portfolio sharing feature through Organizations. This API will allow Service Catalog to receive updates on your organization in order to sync your shares with the current structure. This API can only be called by the management account in the organization.</p> <p>When you call this API, Service Catalog calls <code>organizations:EnableAWSServiceAccess</code> on your behalf so that your shares stay in sync with any changes in your Organizations structure.</p> <p>Note that a delegated administrator is not authorized to invoke <code>EnableAWSOrganizationsAccess</code>.</p> <important> <p>If you have previously disabled Organizations access for Service Catalog, and then enable access again, the portfolio access permissions might not sync with the latest changes to the organization structure. Specifically, accounts that you removed from the organization after disabling Service Catalog access, and before you enabled access again, can retain access to the previously shared portfolio. As a result, an account that has been removed from the organization might still be able to create or manage Amazon Web Services resources when it is no longer authorized to do so. Amazon Web Services is working to resolve this issue.</p> </important>

        Raises:
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.enable_aws_organizations_access_input.EnableAWSOrganizationsAccessInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.enable_aws_organizations_access_output.EnableAWSOrganizationsAccessOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.enable_aws_organizations_access

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.enable_aws_organizations_access.async_enable_aws_organizations_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.enable_aws_organizations_access_input.EnableAWSOrganizationsAccessInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_provisioned_product_plan(
        self,
        plan_id: "capo_service_catalog.types.id.Id",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.execute_provisioned_product_plan_output.ExecuteProvisionedProductPlanOutput":
        """<p>Provisions or modifies a product based on the resource changes for the specified plan.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            plan_id: <p>The plan identifier.</p>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.execute_provisioned_product_plan_input.ExecuteProvisionedProductPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.execute_provisioned_product_plan_output.ExecuteProvisionedProductPlanOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.execute_provisioned_product_plan

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.execute_provisioned_product_plan.async_execute_provisioned_product_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.execute_provisioned_product_plan_input.ExecuteProvisionedProductPlanInput = {
            "plan_id": plan_id,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_provisioned_product_service_action(
        self,
        provisioned_product_id: "capo_service_catalog.types.id.Id",
        service_action_id: "capo_service_catalog.types.id.Id",
        execute_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        parameters: Optional[
            "capo_service_catalog.types.execution_parameter_map.ExecutionParameterMap"
        ] = None,
    ) -> "capo_service_catalog.types.execute_provisioned_product_service_action_output.ExecuteProvisionedProductServiceActionOutput":
        """<p>Executes a self-service action against a provisioned product.</p>

        Args:
            provisioned_product_id: <p>The identifier of the provisioned product.</p>
            service_action_id: <p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>
            execute_token: <p>An idempotency token that uniquely identifies the execute request.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            parameters: <p>A map of all self-service action parameters and their values. If a provided parameter is of a special type, such as <code>TARGET</code>, the provided value will override the default value generated by Service Catalog. If the parameters field is not provided, no additional parameters are passed and default values will be used for any special parameters such as <code>TARGET</code>.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.execute_provisioned_product_service_action_input.ExecuteProvisionedProductServiceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.execute_provisioned_product_service_action_output.ExecuteProvisionedProductServiceActionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.execute_provisioned_product_service_action

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.execute_provisioned_product_service_action.async_execute_provisioned_product_service_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.execute_provisioned_product_service_action_input.ExecuteProvisionedProductServiceActionInput = {
            "provisioned_product_id": provisioned_product_id,
            "service_action_id": service_action_id,
            "execute_token": execute_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_aws_organizations_access_status(
        self, *, config_overrides: Optional[AsyncServiceCatalogClientConfig] = None
    ) -> "capo_service_catalog.types.get_aws_organizations_access_status_output.GetAWSOrganizationsAccessStatusOutput":
        """<p>Get the Access Status for Organizations portfolio share feature. This API can only be called by the management account in the organization or by a delegated admin.</p>

        Raises:
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.get_aws_organizations_access_status_input.GetAWSOrganizationsAccessStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.get_aws_organizations_access_status_output.GetAWSOrganizationsAccessStatusOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.get_aws_organizations_access_status

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.get_aws_organizations_access_status.async_get_aws_organizations_access_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.get_aws_organizations_access_status_input.GetAWSOrganizationsAccessStatusInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_provisioned_product_outputs(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        provisioned_product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        provisioned_product_name: Optional[
            "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
        ] = None,
        output_keys: Optional[
            "capo_service_catalog.types.output_keys.OutputKeys"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.get_provisioned_product_outputs_output.GetProvisionedProductOutputsOutput":
        """<p>This API takes either a <code>ProvisonedProductId</code> or a <code>ProvisionedProductName</code>, along with a list of one or more output keys, and responds with the key/value pairs of those outputs.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            provisioned_product_id: <p>The identifier of the provisioned product that you want the outputs from.</p>
            provisioned_product_name: <p>The name of the provisioned product that you want the outputs from.</p>
            output_keys: <p>The list of keys that the API should return with their values. If none are provided, the API will return all outputs of the provisioned product.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.get_provisioned_product_outputs_input.GetProvisionedProductOutputsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.get_provisioned_product_outputs_output.GetProvisionedProductOutputsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.get_provisioned_product_outputs

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.get_provisioned_product_outputs.async_get_provisioned_product_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.get_provisioned_product_outputs_input.GetProvisionedProductOutputsInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if provisioned_product_id is not None:
            input_["provisioned_product_id"] = provisioned_product_id
        if provisioned_product_name is not None:
            input_["provisioned_product_name"] = provisioned_product_name
        if output_keys is not None:
            input_["output_keys"] = output_keys
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_provisioned_product_outputs(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        provisioned_product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        provisioned_product_name: Optional[
            "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
        ] = None,
        output_keys: Optional[
            "capo_service_catalog.types.output_keys.OutputKeys"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.get_provisioned_product_outputs_output.GetProvisionedProductOutputsOutput]":
        _token = page_token
        while True:
            _response = await self.get_provisioned_product_outputs(
                config_overrides=config_overrides,
                accept_language=accept_language,
                provisioned_product_id=provisioned_product_id,
                provisioned_product_name=provisioned_product_name,
                output_keys=output_keys,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def import_as_provisioned_product(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        provisioned_product_name: "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName",
        physical_id: "capo_service_catalog.types.physical_id.PhysicalId",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.import_as_provisioned_product_output.ImportAsProvisionedProductOutput":
        """<p> Requests the import of a resource as an Service Catalog provisioned product that is associated to an Service Catalog product and provisioning artifact. Once imported, all supported governance actions are supported on the provisioned product. </p> <p> Resource import only supports CloudFormation stack ARNs. CloudFormation StackSets, and non-root nested stacks, are not supported. </p> <p> The CloudFormation stack must have one of the following statuses to be imported: <code>CREATE_COMPLETE</code>, <code>UPDATE_COMPLETE</code>, <code>UPDATE_ROLLBACK_COMPLETE</code>, <code>IMPORT_COMPLETE</code>, and <code>IMPORT_ROLLBACK_COMPLETE</code>. </p> <p> Import of the resource requires that the CloudFormation stack template matches the associated Service Catalog product provisioning artifact. </p> <note> <p> When you import an existing CloudFormation stack into a portfolio, Service Catalog does not apply the product's associated constraints during the import process. Service Catalog applies the constraints after you call <code>UpdateProvisionedProduct</code> for the provisioned product. </p> </note> <p> The user or role that performs this operation must have the <code>cloudformation:GetTemplate</code> and <code>cloudformation:DescribeStacks</code> IAM policy permissions. </p> <p>You can only import one provisioned product at a time. The product's CloudFormation stack must have the <code>IMPORT_COMPLETE</code> status before you import another. </p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact.</p>
            provisioned_product_name: <p>The user-friendly name of the provisioned product. The value must be unique for the Amazon Web Services account. The name cannot be updated after the product is provisioned. </p>
            physical_id: <p>The unique identifier of the resource to be imported. It only currently supports CloudFormation stack IDs.</p>
            idempotency_token: <p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.import_as_provisioned_product_input.ImportAsProvisionedProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.import_as_provisioned_product_output.ImportAsProvisionedProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.import_as_provisioned_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.import_as_provisioned_product.async_import_as_provisioned_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.import_as_provisioned_product_input.ImportAsProvisionedProductInput = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
            "provisioned_product_name": provisioned_product_name,
            "physical_id": physical_id,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_accepted_portfolio_shares(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
        portfolio_share_type: Optional[
            "capo_service_catalog.types.portfolio_share_type.PortfolioShareType"
        ] = None,
    ) -> "capo_service_catalog.types.list_accepted_portfolio_shares_output.ListAcceptedPortfolioSharesOutput":
        """<p>Lists all imported portfolios for which account-to-account shares were accepted by this account. By specifying the <code>PortfolioShareType</code>, you can list portfolios for which organizational shares were accepted by this account.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            portfolio_share_type: <p>The type of shared portfolios to list. The default is to list imported portfolios.</p> <ul> <li> <p> <code>AWS_ORGANIZATIONS</code> - List portfolios accepted and shared via organizational sharing by the management account or delegated administrator of your organization.</p> </li> <li> <p> <code>AWS_SERVICECATALOG</code> - Deprecated type.</p> </li> <li> <p> <code>IMPORTED</code> - List imported portfolios that have been accepted and shared through account-to-account sharing.</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_accepted_portfolio_shares_input.ListAcceptedPortfolioSharesInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_accepted_portfolio_shares_output.ListAcceptedPortfolioSharesOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_accepted_portfolio_shares

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_accepted_portfolio_shares.async_list_accepted_portfolio_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_accepted_portfolio_shares_input.ListAcceptedPortfolioSharesInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size
        if portfolio_share_type is not None:
            input_["portfolio_share_type"] = portfolio_share_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_accepted_portfolio_shares(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
        portfolio_share_type: Optional[
            "capo_service_catalog.types.portfolio_share_type.PortfolioShareType"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_accepted_portfolio_shares_output.ListAcceptedPortfolioSharesOutput]":
        _token = page_token
        while True:
            _response = await self.list_accepted_portfolio_shares(
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_token=_token,
                page_size=page_size,
                portfolio_share_type=portfolio_share_type,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_budgets_for_resource(
        self,
        resource_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.list_budgets_for_resource_output.ListBudgetsForResourceOutput":
        """<p>Lists all the budgets associated to the specified resource.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            resource_id: <p>The resource identifier.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_budgets_for_resource_input.ListBudgetsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_budgets_for_resource_output.ListBudgetsForResourceOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_budgets_for_resource

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_budgets_for_resource.async_list_budgets_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_budgets_for_resource_input.ListBudgetsForResourceInput = {
            "resource_id": resource_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_budgets_for_resource(
        self,
        resource_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_budgets_for_resource_output.ListBudgetsForResourceOutput]":
        _token = page_token
        while True:
            _response = await self.list_budgets_for_resource(
                resource_id,
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_constraints_for_portfolio(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.list_constraints_for_portfolio_output.ListConstraintsForPortfolioOutput":
        """<p>Lists the constraints for the specified portfolio and product.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            product_id: <p>The product identifier.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_constraints_for_portfolio_input.ListConstraintsForPortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_constraints_for_portfolio_output.ListConstraintsForPortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_constraints_for_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_constraints_for_portfolio.async_list_constraints_for_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_constraints_for_portfolio_input.ListConstraintsForPortfolioInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if product_id is not None:
            input_["product_id"] = product_id
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_constraints_for_portfolio(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_constraints_for_portfolio_output.ListConstraintsForPortfolioOutput]":
        _token = page_token
        while True:
            _response = await self.list_constraints_for_portfolio(
                portfolio_id,
                config_overrides=config_overrides,
                accept_language=accept_language,
                product_id=product_id,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_launch_paths(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.list_launch_paths_output.ListLaunchPathsOutput":
        """<p> Lists the paths to the specified product. A path describes how the user gets access to a specified product and is necessary when provisioning a product. A path also determines the constraints that are put on a product. A path is dependent on a specific product, porfolio, and principal. </p> <note> <p> When provisioning a product that's been added to a portfolio, you must grant your user, group, or role access to the portfolio. For more information, see <a href="https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html">Granting users access</a> in the <i>Service Catalog User Guide</i>. </p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_launch_paths_input.ListLaunchPathsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_launch_paths_output.ListLaunchPathsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_launch_paths

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_launch_paths.async_list_launch_paths(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_launch_paths_input.ListLaunchPathsInput = {
            "product_id": product_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_launch_paths(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_launch_paths_output.ListLaunchPathsOutput]":
        _token = page_token
        while True:
            _response = await self.list_launch_paths(
                product_id,
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_organization_portfolio_access(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        organization_node_type: "capo_service_catalog.types.organization_node_type.OrganizationNodeType",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
    ) -> "capo_service_catalog.types.list_organization_portfolio_access_output.ListOrganizationPortfolioAccessOutput":
        """<p>Lists the organization nodes that have access to the specified portfolio. This API can only be called by the management account in the organization or by a delegated admin.</p> <p>If a delegated admin is de-registered, they can no longer perform this operation.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier. For example, <code>port-2abcdext3y5fk</code>.</p>
            organization_node_type: <p>The organization node type that will be returned in the output.</p> <ul> <li> <p> <code>ORGANIZATION</code> - Organization that has access to the portfolio. </p> </li> <li> <p> <code>ORGANIZATIONAL_UNIT</code> - Organizational unit that has access to the portfolio within your organization.</p> </li> <li> <p> <code>ACCOUNT</code> - Account that has access to the portfolio within your organization.</p> </li> </ul>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_organization_portfolio_access_input.ListOrganizationPortfolioAccessInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_organization_portfolio_access_output.ListOrganizationPortfolioAccessOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_organization_portfolio_access

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_organization_portfolio_access.async_list_organization_portfolio_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_organization_portfolio_access_input.ListOrganizationPortfolioAccessInput = {
            "portfolio_id": portfolio_id,
            "organization_node_type": organization_node_type,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_organization_portfolio_access(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        organization_node_type: "capo_service_catalog.types.organization_node_type.OrganizationNodeType",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_organization_portfolio_access_output.ListOrganizationPortfolioAccessOutput]":
        _token = page_token
        while True:
            _response = await self.list_organization_portfolio_access(
                portfolio_id,
                organization_node_type,
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_portfolio_access(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        organization_parent_id: Optional["capo_service_catalog.types.id.Id"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "capo_service_catalog.types.list_portfolio_access_output.ListPortfolioAccessOutput":
        """<p>Lists the account IDs that have access to the specified portfolio.</p> <p>A delegated admin can list the accounts that have access to the shared portfolio. Note that if a delegated admin is de-registered, they can no longer perform this operation.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            organization_parent_id: <p>The ID of an organization node the portfolio is shared with. All children of this node with an inherited portfolio share will be returned.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_portfolio_access_input.ListPortfolioAccessInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_portfolio_access_output.ListPortfolioAccessOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_portfolio_access

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_portfolio_access.async_list_portfolio_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_portfolio_access_input.ListPortfolioAccessInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if organization_parent_id is not None:
            input_["organization_parent_id"] = organization_parent_id
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_portfolio_access(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        organization_parent_id: Optional["capo_service_catalog.types.id.Id"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_portfolio_access_output.ListPortfolioAccessOutput]":
        _token = page_token
        while True:
            _response = await self.list_portfolio_access(
                portfolio_id,
                config_overrides=config_overrides,
                accept_language=accept_language,
                organization_parent_id=organization_parent_id,
                page_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_portfolios(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "capo_service_catalog.types.list_portfolios_output.ListPortfoliosOutput":
        """<p>Lists all portfolios in the catalog.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_portfolios_input.ListPortfoliosInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_portfolios_output.ListPortfoliosOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_portfolios

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_portfolios.async_list_portfolios(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_portfolios_input.ListPortfoliosInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_portfolios(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_portfolios_output.ListPortfoliosOutput]":
        _token = page_token
        while True:
            _response = await self.list_portfolios(
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_portfolios_for_product(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "capo_service_catalog.types.list_portfolios_for_product_output.ListPortfoliosForProductOutput":
        """<p>Lists all portfolios that the specified product is associated with.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_portfolios_for_product_input.ListPortfoliosForProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_portfolios_for_product_output.ListPortfoliosForProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_portfolios_for_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_portfolios_for_product.async_list_portfolios_for_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_portfolios_for_product_input.ListPortfoliosForProductInput = {
            "product_id": product_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_portfolios_for_product(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_portfolios_for_product_output.ListPortfoliosForProductOutput]":
        _token = page_token
        while True:
            _response = await self.list_portfolios_for_product(
                product_id,
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_principals_for_portfolio(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.list_principals_for_portfolio_output.ListPrincipalsForPortfolioOutput":
        """<p>Lists all <code>PrincipalARN</code>s and corresponding <code>PrincipalType</code>s associated with the specified portfolio.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_principals_for_portfolio_input.ListPrincipalsForPortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_principals_for_portfolio_output.ListPrincipalsForPortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_principals_for_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_principals_for_portfolio.async_list_principals_for_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_principals_for_portfolio_input.ListPrincipalsForPortfolioInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_principals_for_portfolio(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_principals_for_portfolio_output.ListPrincipalsForPortfolioOutput]":
        _token = page_token
        while True:
            _response = await self.list_principals_for_portfolio(
                portfolio_id,
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_provisioned_product_plans(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        provision_product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        access_level_filter: Optional[
            "capo_service_catalog.types.access_level_filter.AccessLevelFilter"
        ] = None,
    ) -> "capo_service_catalog.types.list_provisioned_product_plans_output.ListProvisionedProductPlansOutput":
        """<p>Lists the plans for the specified provisioned product or all plans to which the user has access.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            provision_product_id: <p>The product identifier.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            access_level_filter: <p>The access level to use to obtain results. The default is <code>User</code>.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_provisioned_product_plans_input.ListProvisionedProductPlansInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_provisioned_product_plans_output.ListProvisionedProductPlansOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_provisioned_product_plans

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_provisioned_product_plans.async_list_provisioned_product_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_provisioned_product_plans_input.ListProvisionedProductPlansInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if provision_product_id is not None:
            input_["provision_product_id"] = provision_product_id
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token
        if access_level_filter is not None:
            input_["access_level_filter"] = access_level_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_provisioning_artifacts(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.list_provisioning_artifacts_output.ListProvisioningArtifactsOutput":
        """<p>Lists all provisioning artifacts (also known as versions) for the specified product.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_provisioning_artifacts_input.ListProvisioningArtifactsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_provisioning_artifacts_output.ListProvisioningArtifactsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_provisioning_artifacts

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_provisioning_artifacts.async_list_provisioning_artifacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_provisioning_artifacts_input.ListProvisioningArtifactsInput = {
            "product_id": product_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_provisioning_artifacts_for_service_action(
        self,
        service_action_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.list_provisioning_artifacts_for_service_action_output.ListProvisioningArtifactsForServiceActionOutput":
        """<p>Lists all provisioning artifacts (also known as versions) for the specified self-service action.</p>

        Args:
            service_action_id: <p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_provisioning_artifacts_for_service_action_input.ListProvisioningArtifactsForServiceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_provisioning_artifacts_for_service_action_output.ListProvisioningArtifactsForServiceActionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_provisioning_artifacts_for_service_action

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_provisioning_artifacts_for_service_action.async_list_provisioning_artifacts_for_service_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_provisioning_artifacts_for_service_action_input.ListProvisioningArtifactsForServiceActionInput = {
            "service_action_id": service_action_id
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_provisioning_artifacts_for_service_action(
        self,
        service_action_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_provisioning_artifacts_for_service_action_output.ListProvisioningArtifactsForServiceActionOutput]":
        _token = page_token
        while True:
            _response = await self.list_provisioning_artifacts_for_service_action(
                service_action_id,
                config_overrides=config_overrides,
                page_size=page_size,
                page_token=_token,
                accept_language=accept_language,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_record_history(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        access_level_filter: Optional[
            "capo_service_catalog.types.access_level_filter.AccessLevelFilter"
        ] = None,
        search_filter: Optional[
            "capo_service_catalog.types.list_record_history_search_filter.ListRecordHistorySearchFilter"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> (
        "capo_service_catalog.types.list_record_history_output.ListRecordHistoryOutput"
    ):
        """<p>Lists the specified requests or all performed requests.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            access_level_filter: <p>The access level to use to obtain results. The default is <code>User</code>.</p>
            search_filter: <p>The search filter to scope the results.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_record_history_input.ListRecordHistoryInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_record_history_output.ListRecordHistoryOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_record_history

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_record_history.async_list_record_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_record_history_input.ListRecordHistoryInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if access_level_filter is not None:
            input_["access_level_filter"] = access_level_filter
        if search_filter is not None:
            input_["search_filter"] = search_filter
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_resources_for_tag_option(
        self,
        tag_option_id: "capo_service_catalog.types.tag_option_id.TagOptionId",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        resource_type: Optional[
            "capo_service_catalog.types.resource_type.ResourceType"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.list_resources_for_tag_option_output.ListResourcesForTagOptionOutput":
        """<p>Lists the resources associated with the specified TagOption.</p>

        Args:
            tag_option_id: <p>The TagOption identifier.</p>
            resource_type: <p>The resource type.</p> <ul> <li> <p> <code>Portfolio</code> </p> </li> <li> <p> <code>Product</code> </p> </li> </ul>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_resources_for_tag_option_input.ListResourcesForTagOptionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_resources_for_tag_option_output.ListResourcesForTagOptionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_resources_for_tag_option

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_resources_for_tag_option.async_list_resources_for_tag_option(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_resources_for_tag_option_input.ListResourcesForTagOptionInput = {
            "tag_option_id": tag_option_id
        }
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resources_for_tag_option(
        self,
        tag_option_id: "capo_service_catalog.types.tag_option_id.TagOptionId",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        resource_type: Optional[
            "capo_service_catalog.types.resource_type.ResourceType"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_resources_for_tag_option_output.ListResourcesForTagOptionOutput]":
        _token = page_token
        while True:
            _response = await self.list_resources_for_tag_option(
                tag_option_id,
                config_overrides=config_overrides,
                resource_type=resource_type,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("page_token",))
            if not _token:
                break

    async def list_service_actions(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.list_service_actions_output.ListServiceActionsOutput":
        """<p>Lists all self-service actions.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_service_actions_input.ListServiceActionsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_service_actions_output.ListServiceActionsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_service_actions

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_service_actions.async_list_service_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_service_actions_input.ListServiceActionsInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_actions(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_service_actions_output.ListServiceActionsOutput]":
        _token = page_token
        while True:
            _response = await self.list_service_actions(
                config_overrides=config_overrides,
                accept_language=accept_language,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_service_actions_for_provisioning_artifact(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.list_service_actions_for_provisioning_artifact_output.ListServiceActionsForProvisioningArtifactOutput":
        """<p>Returns a paginated list of self-service actions associated with the specified Product ID and Provisioning Artifact ID.</p>

        Args:
            product_id: <p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_service_actions_for_provisioning_artifact_input.ListServiceActionsForProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_service_actions_for_provisioning_artifact_output.ListServiceActionsForProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_service_actions_for_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_service_actions_for_provisioning_artifact.async_list_service_actions_for_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_service_actions_for_provisioning_artifact_input.ListServiceActionsForProvisioningArtifactInput = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_service_actions_for_provisioning_artifact(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_service_actions_for_provisioning_artifact_output.ListServiceActionsForProvisioningArtifactOutput]":
        _token = page_token
        while True:
            _response = await self.list_service_actions_for_provisioning_artifact(
                product_id,
                provisioning_artifact_id,
                config_overrides=config_overrides,
                page_size=page_size,
                page_token=_token,
                accept_language=accept_language,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_stack_instances_for_provisioned_product(
        self,
        provisioned_product_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
    ) -> "capo_service_catalog.types.list_stack_instances_for_provisioned_product_output.ListStackInstancesForProvisionedProductOutput":
        """<p>Returns summary information about stack instances that are associated with the specified <code>CFN_STACKSET</code> type provisioned product. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region. </p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            provisioned_product_id: <p>The identifier of the provisioned product.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_stack_instances_for_provisioned_product_input.ListStackInstancesForProvisionedProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_stack_instances_for_provisioned_product_output.ListStackInstancesForProvisionedProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_stack_instances_for_provisioned_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_stack_instances_for_provisioned_product.async_list_stack_instances_for_provisioned_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_stack_instances_for_provisioned_product_input.ListStackInstancesForProvisionedProductInput = {
            "provisioned_product_id": provisioned_product_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tag_options(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        filters: Optional[
            "capo_service_catalog.types.list_tag_options_filters.ListTagOptionsFilters"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.list_tag_options_output.ListTagOptionsOutput":
        """<p>Lists the specified TagOptions or all TagOptions.</p>

        Args:
            filters: <p>The search filters. If no search filters are specified, the output includes all TagOptions.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.list_tag_options_input.ListTagOptionsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.list_tag_options_output.ListTagOptionsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.list_tag_options

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.list_tag_options.async_list_tag_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.list_tag_options_input.ListTagOptionsInput = {}
        if filters is not None:
            input_["filters"] = filters
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tag_options(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        filters: Optional[
            "capo_service_catalog.types.list_tag_options_filters.ListTagOptionsFilters"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.list_tag_options_output.ListTagOptionsOutput]":
        _token = page_token
        while True:
            _response = await self.list_tag_options(
                config_overrides=config_overrides,
                filters=filters,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("page_token",))
            if not _token:
                break

    async def notify_provision_product_engine_workflow_result(
        self,
        workflow_token: "capo_service_catalog.types.engine_workflow_token.EngineWorkflowToken",
        record_id: "capo_service_catalog.types.id.Id",
        status: "capo_service_catalog.types.engine_workflow_status.EngineWorkflowStatus",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        failure_reason: Optional[
            "capo_service_catalog.types.engine_workflow_failure_reason.EngineWorkflowFailureReason"
        ] = None,
        resource_identifier: Optional[
            "capo_service_catalog.types.engine_workflow_resource_identifier.EngineWorkflowResourceIdentifier"
        ] = None,
        outputs: Optional[
            "capo_service_catalog.types.record_outputs.RecordOutputs"
        ] = None,
    ) -> "capo_service_catalog.types.notify_provision_product_engine_workflow_result_output.NotifyProvisionProductEngineWorkflowResultOutput":
        """<p> Notifies the result of the provisioning engine execution. </p>

        Args:
            workflow_token: <p> The encrypted contents of the provisioning engine execution payload that Service Catalog sends after the Terraform product provisioning workflow starts. </p>
            record_id: <p> The identifier of the record. </p>
            status: <p> The status of the provisioning engine execution. </p>
            failure_reason: <p> The reason why the provisioning engine execution failed. </p>
            resource_identifier: <p> The ID for the provisioned product resources that are part of a resource group. </p>
            outputs: <p> The output of the provisioning engine execution. </p>
            idempotency_token: <p> The idempotency token that identifies the provisioning engine execution. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.notify_provision_product_engine_workflow_result_input.NotifyProvisionProductEngineWorkflowResultInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.notify_provision_product_engine_workflow_result_output.NotifyProvisionProductEngineWorkflowResultOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.notify_provision_product_engine_workflow_result

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.notify_provision_product_engine_workflow_result.async_notify_provision_product_engine_workflow_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.notify_provision_product_engine_workflow_result_input.NotifyProvisionProductEngineWorkflowResultInput = {
            "workflow_token": workflow_token,
            "record_id": record_id,
            "status": status,
            "idempotency_token": idempotency_token,
        }
        if failure_reason is not None:
            input_["failure_reason"] = failure_reason
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if outputs is not None:
            input_["outputs"] = outputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def notify_terminate_provisioned_product_engine_workflow_result(
        self,
        workflow_token: "capo_service_catalog.types.engine_workflow_token.EngineWorkflowToken",
        record_id: "capo_service_catalog.types.id.Id",
        status: "capo_service_catalog.types.engine_workflow_status.EngineWorkflowStatus",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        failure_reason: Optional[
            "capo_service_catalog.types.engine_workflow_failure_reason.EngineWorkflowFailureReason"
        ] = None,
    ) -> "capo_service_catalog.types.notify_terminate_provisioned_product_engine_workflow_result_output.NotifyTerminateProvisionedProductEngineWorkflowResultOutput":
        """<p> Notifies the result of the terminate engine execution. </p>

        Args:
            workflow_token: <p> The encrypted contents of the terminate engine execution payload that Service Catalog sends after the Terraform product terminate workflow starts. </p>
            record_id: <p> The identifier of the record. </p>
            status: <p> The status of the terminate engine execution. </p>
            failure_reason: <p> The reason why the terminate engine execution failed. </p>
            idempotency_token: <p> The idempotency token that identifies the terminate engine execution. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.notify_terminate_provisioned_product_engine_workflow_result_input.NotifyTerminateProvisionedProductEngineWorkflowResultInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.notify_terminate_provisioned_product_engine_workflow_result_output.NotifyTerminateProvisionedProductEngineWorkflowResultOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.notify_terminate_provisioned_product_engine_workflow_result

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.notify_terminate_provisioned_product_engine_workflow_result.async_notify_terminate_provisioned_product_engine_workflow_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.notify_terminate_provisioned_product_engine_workflow_result_input.NotifyTerminateProvisionedProductEngineWorkflowResultInput = {
            "workflow_token": workflow_token,
            "record_id": record_id,
            "status": status,
            "idempotency_token": idempotency_token,
        }
        if failure_reason is not None:
            input_["failure_reason"] = failure_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def notify_update_provisioned_product_engine_workflow_result(
        self,
        workflow_token: "capo_service_catalog.types.engine_workflow_token.EngineWorkflowToken",
        record_id: "capo_service_catalog.types.id.Id",
        status: "capo_service_catalog.types.engine_workflow_status.EngineWorkflowStatus",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        failure_reason: Optional[
            "capo_service_catalog.types.engine_workflow_failure_reason.EngineWorkflowFailureReason"
        ] = None,
        outputs: Optional[
            "capo_service_catalog.types.record_outputs.RecordOutputs"
        ] = None,
    ) -> "capo_service_catalog.types.notify_update_provisioned_product_engine_workflow_result_output.NotifyUpdateProvisionedProductEngineWorkflowResultOutput":
        """<p> Notifies the result of the update engine execution. </p>

        Args:
            workflow_token: <p> The encrypted contents of the update engine execution payload that Service Catalog sends after the Terraform product update workflow starts. </p>
            record_id: <p> The identifier of the record. </p>
            status: <p> The status of the update engine execution. </p>
            failure_reason: <p> The reason why the update engine execution failed. </p>
            outputs: <p> The output of the update engine execution. </p>
            idempotency_token: <p> The idempotency token that identifies the update engine execution. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.notify_update_provisioned_product_engine_workflow_result_input.NotifyUpdateProvisionedProductEngineWorkflowResultInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.notify_update_provisioned_product_engine_workflow_result_output.NotifyUpdateProvisionedProductEngineWorkflowResultOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.notify_update_provisioned_product_engine_workflow_result

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.notify_update_provisioned_product_engine_workflow_result.async_notify_update_provisioned_product_engine_workflow_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.notify_update_provisioned_product_engine_workflow_result_input.NotifyUpdateProvisionedProductEngineWorkflowResultInput = {
            "workflow_token": workflow_token,
            "record_id": record_id,
            "status": status,
            "idempotency_token": idempotency_token,
        }
        if failure_reason is not None:
            input_["failure_reason"] = failure_reason
        if outputs is not None:
            input_["outputs"] = outputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def provision_product(
        self,
        provisioned_product_name: "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName",
        provision_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        product_name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
        provisioning_artifact_id: Optional["capo_service_catalog.types.id.Id"] = None,
        provisioning_artifact_name: Optional[
            "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
        ] = None,
        path_id: Optional["capo_service_catalog.types.id.Id"] = None,
        path_name: Optional[
            "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
        ] = None,
        provisioning_parameters: Optional[
            "capo_service_catalog.types.provisioning_parameters.ProvisioningParameters"
        ] = None,
        provisioning_preferences: Optional[
            "capo_service_catalog.types.provisioning_preferences.ProvisioningPreferences"
        ] = None,
        tags: Optional["capo_service_catalog.types.tags.Tags"] = None,
        notification_arns: Optional[
            "capo_service_catalog.types.notification_arns.NotificationArns"
        ] = None,
    ) -> "capo_service_catalog.types.provision_product_output.ProvisionProductOutput":
        """<p> Provisions the specified product. </p> <p> A provisioned product is a resourced instance of a product. For example, provisioning a product that's based on an CloudFormation template launches an CloudFormation stack and its underlying resources. You can check the status of this request using <a>DescribeRecord</a>. </p> <p> If the request contains a tag key with an empty list of values, there's a tag conflict for that key. Don't include conflicted keys as tags, or this will cause the error "Parameter validation failed: Missing required parameter in Tags[<i>N</i>]:<i>Value</i>". </p> <note> <p> When provisioning a product that's been added to a portfolio, you must grant your user, group, or role access to the portfolio. For more information, see <a href="https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html">Granting users access</a> in the <i>Service Catalog User Guide</i>. </p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier. You must provide the name or ID, but not both.</p>
            product_name: <p>The name of the product. You must provide the name or ID, but not both.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact. You must provide the name or ID, but not both.</p>
            provisioning_artifact_name: <p>The name of the provisioning artifact. You must provide the name or ID, but not both.</p>
            path_id: <p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>. You must provide the name or ID, but not both.</p>
            path_name: <p>The name of the path. You must provide the name or ID, but not both.</p>
            provisioned_product_name: <p>A user-friendly name for the provisioned product. This value must be unique for the Amazon Web Services account and cannot be updated after the product is provisioned.</p>
            provisioning_parameters: <p>Parameters specified by the administrator that are required for provisioning the product.</p>
            provisioning_preferences: <p>An object that contains information about the provisioning preferences for a stack set.</p>
            tags: <p>One or more tags.</p>
            notification_arns: <p>Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.</p>
            provision_token: <p>An idempotency token that uniquely identifies the provisioning request.</p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.provision_product_input.ProvisionProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.provision_product_output.ProvisionProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.provision_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.provision_product.async_provision_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.provision_product_input.ProvisionProductInput = {
            "provisioned_product_name": provisioned_product_name,
            "provision_token": provision_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if product_id is not None:
            input_["product_id"] = product_id
        if product_name is not None:
            input_["product_name"] = product_name
        if provisioning_artifact_id is not None:
            input_["provisioning_artifact_id"] = provisioning_artifact_id
        if provisioning_artifact_name is not None:
            input_["provisioning_artifact_name"] = provisioning_artifact_name
        if path_id is not None:
            input_["path_id"] = path_id
        if path_name is not None:
            input_["path_name"] = path_name
        if provisioning_parameters is not None:
            input_["provisioning_parameters"] = provisioning_parameters
        if provisioning_preferences is not None:
            input_["provisioning_preferences"] = provisioning_preferences
        if tags is not None:
            input_["tags"] = tags
        if notification_arns is not None:
            input_["notification_arns"] = notification_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_portfolio_share(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        portfolio_share_type: Optional[
            "capo_service_catalog.types.portfolio_share_type.PortfolioShareType"
        ] = None,
    ) -> "capo_service_catalog.types.reject_portfolio_share_output.RejectPortfolioShareOutput":
        """<p>Rejects an offer to share the specified portfolio.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            portfolio_share_type: <p>The type of shared portfolios to reject. The default is to reject imported portfolios.</p> <ul> <li> <p> <code>AWS_ORGANIZATIONS</code> - Reject portfolios shared by the management account of your organization.</p> </li> <li> <p> <code>IMPORTED</code> - Reject imported portfolios.</p> </li> <li> <p> <code>AWS_SERVICECATALOG</code> - Not supported. (Throws ResourceNotFoundException.)</p> </li> </ul> <p>For example, <code>aws servicecatalog reject-portfolio-share --portfolio-id "port-2qwzkwxt3y5fk" --portfolio-share-type AWS_ORGANIZATIONS</code> </p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.reject_portfolio_share_input.RejectPortfolioShareInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.reject_portfolio_share_output.RejectPortfolioShareOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.reject_portfolio_share

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.reject_portfolio_share.async_reject_portfolio_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.reject_portfolio_share_input.RejectPortfolioShareInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if portfolio_share_type is not None:
            input_["portfolio_share_type"] = portfolio_share_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def scan_provisioned_products(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        access_level_filter: Optional[
            "capo_service_catalog.types.access_level_filter.AccessLevelFilter"
        ] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.scan_provisioned_products_output.ScanProvisionedProductsOutput":
        """<p>Lists the provisioned products that are available (not terminated).</p> <p>To use additional filtering, see <a>SearchProvisionedProducts</a>.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            access_level_filter: <p>The access level to use to obtain results. The default is <code>User</code>.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.scan_provisioned_products_input.ScanProvisionedProductsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.scan_provisioned_products_output.ScanProvisionedProductsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.scan_provisioned_products

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.scan_provisioned_products.async_scan_provisioned_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.scan_provisioned_products_input.ScanProvisionedProductsInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if access_level_filter is not None:
            input_["access_level_filter"] = access_level_filter
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_products(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        filters: Optional[
            "capo_service_catalog.types.product_view_filters.ProductViewFilters"
        ] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
        sort_by: Optional[
            "capo_service_catalog.types.product_view_sort_by.ProductViewSortBy"
        ] = None,
        sort_order: Optional["capo_service_catalog.types.sort_order.SortOrder"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.search_products_output.SearchProductsOutput":
        """<p>Gets information about the products to which the caller has access.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            filters: <p>The search filters. If no search filters are specified, the output includes all products to which the caller has access.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            sort_by: <p>The sort field. If no value is specified, the results are not sorted.</p>
            sort_order: <p>The sort order. If no value is specified, the results are not sorted.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.search_products_input.SearchProductsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.search_products_output.SearchProductsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.search_products

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.search_products.async_search_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.search_products_input.SearchProductsInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if filters is not None:
            input_["filters"] = filters
        if page_size is not None:
            input_["page_size"] = page_size
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_products(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        filters: Optional[
            "capo_service_catalog.types.product_view_filters.ProductViewFilters"
        ] = None,
        page_size: Optional[
            "capo_service_catalog.types.page_size_max100.PageSizeMax100"
        ] = None,
        sort_by: Optional[
            "capo_service_catalog.types.product_view_sort_by.ProductViewSortBy"
        ] = None,
        sort_order: Optional["capo_service_catalog.types.sort_order.SortOrder"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.search_products_output.SearchProductsOutput]":
        _token = page_token
        while True:
            _response = await self.search_products(
                config_overrides=config_overrides,
                accept_language=accept_language,
                filters=filters,
                page_size=page_size,
                sort_by=sort_by,
                sort_order=sort_order,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def search_products_as_admin(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        portfolio_id: Optional["capo_service_catalog.types.id.Id"] = None,
        filters: Optional[
            "capo_service_catalog.types.product_view_filters.ProductViewFilters"
        ] = None,
        sort_by: Optional[
            "capo_service_catalog.types.product_view_sort_by.ProductViewSortBy"
        ] = None,
        sort_order: Optional["capo_service_catalog.types.sort_order.SortOrder"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        product_source: Optional[
            "capo_service_catalog.types.product_source.ProductSource"
        ] = None,
    ) -> "capo_service_catalog.types.search_products_as_admin_output.SearchProductsAsAdminOutput":
        """<p>Gets information about the products for the specified portfolio or all products.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The portfolio identifier.</p>
            filters: <p>The search filters. If no search filters are specified, the output includes all products to which the administrator has access.</p>
            sort_by: <p>The sort field. If no value is specified, the results are not sorted.</p>
            sort_order: <p>The sort order. If no value is specified, the results are not sorted.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            product_source: <p>Access level of the source of the product.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.search_products_as_admin_input.SearchProductsAsAdminInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.search_products_as_admin_output.SearchProductsAsAdminOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.search_products_as_admin

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.search_products_as_admin.async_search_products_as_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.search_products_as_admin_input.SearchProductsAsAdminInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if portfolio_id is not None:
            input_["portfolio_id"] = portfolio_id
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if page_token is not None:
            input_["page_token"] = page_token
        if page_size is not None:
            input_["page_size"] = page_size
        if product_source is not None:
            input_["product_source"] = product_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_products_as_admin(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        portfolio_id: Optional["capo_service_catalog.types.id.Id"] = None,
        filters: Optional[
            "capo_service_catalog.types.product_view_filters.ProductViewFilters"
        ] = None,
        sort_by: Optional[
            "capo_service_catalog.types.product_view_sort_by.ProductViewSortBy"
        ] = None,
        sort_order: Optional["capo_service_catalog.types.sort_order.SortOrder"] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
        page_size: Optional["capo_service_catalog.types.page_size.PageSize"] = None,
        product_source: Optional[
            "capo_service_catalog.types.product_source.ProductSource"
        ] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.search_products_as_admin_output.SearchProductsAsAdminOutput]":
        _token = page_token
        while True:
            _response = await self.search_products_as_admin(
                config_overrides=config_overrides,
                accept_language=accept_language,
                portfolio_id=portfolio_id,
                filters=filters,
                sort_by=sort_by,
                sort_order=sort_order,
                page_token=_token,
                page_size=page_size,
                product_source=product_source,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def search_provisioned_products(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        access_level_filter: Optional[
            "capo_service_catalog.types.access_level_filter.AccessLevelFilter"
        ] = None,
        filters: Optional[
            "capo_service_catalog.types.provisioned_product_filters.ProvisionedProductFilters"
        ] = None,
        sort_by: Optional["capo_service_catalog.types.sort_field.SortField"] = None,
        sort_order: Optional["capo_service_catalog.types.sort_order.SortOrder"] = None,
        page_size: Optional[
            "capo_service_catalog.types.search_provisioned_products_page_size.SearchProvisionedProductsPageSize"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "capo_service_catalog.types.search_provisioned_products_output.SearchProvisionedProductsOutput":
        """<p>Gets information about the provisioned products that meet the specified criteria.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            access_level_filter: <p>The access level to use to obtain results. The default is <code>Account</code>.</p>
            filters: <p>The search filters.</p> <p>When the key is <code>SearchQuery</code>, the searchable fields are <code>arn</code>, <code>createdTime</code>, <code>id</code>, <code>lastRecordId</code>, <code>idempotencyToken</code>, <code>name</code>, <code>physicalId</code>, <code>productId</code>, <code>provisioningArtifactId</code>, <code>type</code>, <code>status</code>, <code>tags</code>, <code>userArn</code>, <code>userArnSession</code>, <code>lastProvisioningRecordId</code>, <code>lastSuccessfulProvisioningRecordId</code>, <code>productName</code>, and <code>provisioningArtifactName</code>.</p> <p>Example: <code>"SearchQuery":["status:AVAILABLE"]</code> </p>
            sort_by: <p>The sort field. If no value is specified, the results are not sorted. The valid values are <code>arn</code>, <code>id</code>, <code>name</code>, and <code>lastRecordId</code>.</p>
            sort_order: <p>The sort order. If no value is specified, the results are not sorted.</p>
            page_size: <p>The maximum number of items to return with this call.</p>
            page_token: <p>The page token for the next set of results. To retrieve the first set of results, use null.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.search_provisioned_products_input.SearchProvisionedProductsInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.search_provisioned_products_output.SearchProvisionedProductsOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.search_provisioned_products

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.search_provisioned_products.async_search_provisioned_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.search_provisioned_products_input.SearchProvisionedProductsInput = {}
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if access_level_filter is not None:
            input_["access_level_filter"] = access_level_filter
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if page_size is not None:
            input_["page_size"] = page_size
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_provisioned_products(
        self,
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        access_level_filter: Optional[
            "capo_service_catalog.types.access_level_filter.AccessLevelFilter"
        ] = None,
        filters: Optional[
            "capo_service_catalog.types.provisioned_product_filters.ProvisionedProductFilters"
        ] = None,
        sort_by: Optional["capo_service_catalog.types.sort_field.SortField"] = None,
        sort_order: Optional["capo_service_catalog.types.sort_order.SortOrder"] = None,
        page_size: Optional[
            "capo_service_catalog.types.search_provisioned_products_page_size.SearchProvisionedProductsPageSize"
        ] = None,
        page_token: Optional["capo_service_catalog.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_service_catalog.types.search_provisioned_products_output.SearchProvisionedProductsOutput]":
        _token = page_token
        while True:
            _response = await self.search_provisioned_products(
                config_overrides=config_overrides,
                accept_language=accept_language,
                access_level_filter=access_level_filter,
                filters=filters,
                sort_by=sort_by,
                sort_order=sort_order,
                page_size=page_size,
                page_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def terminate_provisioned_product(
        self,
        terminate_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        provisioned_product_name: Optional[
            "capo_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
        ] = None,
        provisioned_product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        ignore_errors: Optional[
            "capo_service_catalog.types.ignore_errors.IgnoreErrors"
        ] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        retain_physical_resources: Optional[
            "capo_service_catalog.types.retain_physical_resources.RetainPhysicalResources"
        ] = None,
    ) -> "capo_service_catalog.types.terminate_provisioned_product_output.TerminateProvisionedProductOutput":
        """<p>Terminates the specified provisioned product.</p> <p>This operation does not delete any records associated with the provisioned product.</p> <p>You can check the status of this request using <a>DescribeRecord</a>.</p>

        Args:
            provisioned_product_name: <p>The name of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>
            provisioned_product_id: <p>The identifier of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>
            terminate_token: <p>An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return <b>ResourceNotFound</b>.</p>
            ignore_errors: <p>If set to true, Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            retain_physical_resources: <p>When this boolean parameter is set to true, the <code>TerminateProvisionedProduct</code> API deletes the Service Catalog provisioned product. However, it does not remove the CloudFormation stack, stack set, or the underlying resources of the deleted provisioned product. The default value is false.</p>

        Raises:
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.terminate_provisioned_product_input.TerminateProvisionedProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.terminate_provisioned_product_output.TerminateProvisionedProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.terminate_provisioned_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.terminate_provisioned_product.async_terminate_provisioned_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.terminate_provisioned_product_input.TerminateProvisionedProductInput = {
            "terminate_token": terminate_token
        }
        if provisioned_product_name is not None:
            input_["provisioned_product_name"] = provisioned_product_name
        if provisioned_product_id is not None:
            input_["provisioned_product_id"] = provisioned_product_id
        if ignore_errors is not None:
            input_["ignore_errors"] = ignore_errors
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if retain_physical_resources is not None:
            input_["retain_physical_resources"] = retain_physical_resources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_constraint(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.constraint_description.ConstraintDescription"
        ] = None,
        parameters: Optional[
            "capo_service_catalog.types.constraint_parameters.ConstraintParameters"
        ] = None,
    ) -> "capo_service_catalog.types.update_constraint_output.UpdateConstraintOutput":
        """<p>Updates the specified constraint.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The identifier of the constraint.</p>
            description: <p>The updated description of the constraint.</p>
            parameters: <p>The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:</p> <dl> <dt>LAUNCH</dt> <dd> <p>You are required to specify either the <code>RoleArn</code> or the <code>LocalRoleName</code> but can't use both.</p> <p>Specify the <code>RoleArn</code> property as follows:</p> <p> <code>{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}</code> </p> <p>Specify the <code>LocalRoleName</code> property as follows:</p> <p> <code>{"LocalRoleName": "SCBasicLaunchRole"}</code> </p> <p>If you specify the <code>LocalRoleName</code> property, when an account uses the launch constraint, the IAM role with that name in the account will be used. This allows launch-role constraints to be account-agnostic so the administrator can create fewer resources per shared account.</p> <note> <p>The given role name must exist in the account used to create the launch constraint and the account of the user who launches a product with this launch constraint.</p> </note> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>LAUNCH</code> constraint on a product and portfolio.</p> </dd> <dt>NOTIFICATION</dt> <dd> <p>Specify the <code>NotificationArns</code> property as follows:</p> <p> <code>{"NotificationArns" : ["arn:aws:sns:us-east-1:123456789012:Topic"]}</code> </p> </dd> <dt>RESOURCE_UPDATE</dt> <dd> <p>Specify the <code>TagUpdatesOnProvisionedProduct</code> property as follows:</p> <p> <code>{"Version":"2.0","Properties":{"TagUpdateOnProvisionedProduct":"String"}}</code> </p> <p>The <code>TagUpdatesOnProvisionedProduct</code> property accepts a string value of <code>ALLOWED</code> or <code>NOT_ALLOWED</code>.</p> </dd> <dt>STACKSET</dt> <dd> <p>Specify the <code>Parameters</code> property as follows:</p> <p> <code>{"Version": "String", "Properties": {"AccountList": [ "String" ], "RegionList": [ "String" ], "AdminRole": "String", "ExecutionRole": "String"}}</code> </p> <p>You cannot have both a <code>LAUNCH</code> and a <code>STACKSET</code> constraint.</p> <p>You also cannot have more than one <code>STACKSET</code> constraint on a product and portfolio.</p> <p>Products with a <code>STACKSET</code> constraint will launch an CloudFormation stack set.</p> </dd> <dt>TEMPLATE</dt> <dd> <p>Specify the <code>Rules</code> property. For more information, see <a href="http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html">Template Constraint Rules</a>.</p> </dd> </dl>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_constraint_input.UpdateConstraintInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_constraint_output.UpdateConstraintOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_constraint

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_constraint.async_update_constraint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_constraint_input.UpdateConstraintInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_portfolio(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        display_name: Optional[
            "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.portfolio_description.PortfolioDescription"
        ] = None,
        provider_name: Optional[
            "capo_service_catalog.types.provider_name.ProviderName"
        ] = None,
        add_tags: Optional["capo_service_catalog.types.add_tags.AddTags"] = None,
        remove_tags: Optional["capo_service_catalog.types.tag_keys.TagKeys"] = None,
    ) -> "capo_service_catalog.types.update_portfolio_output.UpdatePortfolioOutput":
        """<p>Updates the specified portfolio.</p> <p>You cannot update a product that was shared with you.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The portfolio identifier.</p>
            display_name: <p>The name to use for display purposes.</p>
            description: <p>The updated description of the portfolio.</p>
            provider_name: <p>The updated name of the portfolio provider.</p>
            add_tags: <p>The tags to add.</p>
            remove_tags: <p>The tags to remove.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.limit_exceeded_exception.LimitExceededException: <p>The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_portfolio_input.UpdatePortfolioInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_portfolio_output.UpdatePortfolioOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_portfolio

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_portfolio.async_update_portfolio(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_portfolio_input.UpdatePortfolioInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if add_tags is not None:
            input_["add_tags"] = add_tags
        if remove_tags is not None:
            input_["remove_tags"] = remove_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_portfolio_share(
        self,
        portfolio_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        account_id: Optional["capo_service_catalog.types.account_id.AccountId"] = None,
        organization_node: Optional[
            "capo_service_catalog.types.organization_node.OrganizationNode"
        ] = None,
        share_tag_options: Optional[
            "capo_service_catalog.types.nullable_boolean.NullableBoolean"
        ] = None,
        share_principals: Optional[
            "capo_service_catalog.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_service_catalog.types.update_portfolio_share_output.UpdatePortfolioShareOutput":
        """<p>Updates the specified portfolio share. You can use this API to enable or disable <code>TagOptions</code> sharing or Principal sharing for an existing portfolio share. </p> <p>The portfolio share cannot be updated if the <code>CreatePortfolioShare</code> operation is <code>IN_PROGRESS</code>, as the share is not available to recipient entities. In this case, you must wait for the portfolio share to be completed.</p> <p>You must provide the <code>accountId</code> or organization node in the input, but not both.</p> <p>If the portfolio is shared to both an external account and an organization node, and both shares need to be updated, you must invoke <code>UpdatePortfolioShare</code> separately for each share type. </p> <p>This API cannot be used for removing the portfolio share. You must use <code>DeletePortfolioShare</code> API for that action. </p> <note> <p>When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is <i>not</i> an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using <code>PrincipalType</code> as <code>IAM</code>. With this configuration, the <code>PrincipalARN</code> must already exist in the recipient account before it can be associated. </p> </note>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            portfolio_id: <p>The unique identifier of the portfolio for which the share will be updated.</p>
            account_id: <p>The Amazon Web Services account Id of the recipient account. This field is required when updating an external account to account type share.</p>
            share_tag_options: <p>Enables or disables <code>TagOptions</code> sharing for the portfolio share. If this field is not provided, the current state of TagOptions sharing on the portfolio share will not be modified.</p>
            share_principals: <p>A flag to enables or disables <code>Principals</code> sharing in the portfolio. If this field is not provided, the current state of the <code>Principals</code> sharing on the portfolio share will not be modified. </p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.operation_not_supported_exception.OperationNotSupportedException: <p>The operation is not supported.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_portfolio_share_input.UpdatePortfolioShareInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_portfolio_share_output.UpdatePortfolioShareOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_portfolio_share

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_portfolio_share.async_update_portfolio_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_portfolio_share_input.UpdatePortfolioShareInput = {
            "portfolio_id": portfolio_id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if account_id is not None:
            input_["account_id"] = account_id
        if organization_node is not None:
            input_["organization_node"] = organization_node
        if share_tag_options is not None:
            input_["share_tag_options"] = share_tag_options
        if share_principals is not None:
            input_["share_principals"] = share_principals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_product(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
        owner: Optional[
            "capo_service_catalog.types.product_view_owner.ProductViewOwner"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.product_view_short_description.ProductViewShortDescription"
        ] = None,
        distributor: Optional[
            "capo_service_catalog.types.product_view_owner.ProductViewOwner"
        ] = None,
        support_description: Optional[
            "capo_service_catalog.types.support_description.SupportDescription"
        ] = None,
        support_email: Optional[
            "capo_service_catalog.types.support_email.SupportEmail"
        ] = None,
        support_url: Optional[
            "capo_service_catalog.types.support_url.SupportUrl"
        ] = None,
        add_tags: Optional["capo_service_catalog.types.add_tags.AddTags"] = None,
        remove_tags: Optional["capo_service_catalog.types.tag_keys.TagKeys"] = None,
        source_connection: Optional[
            "capo_service_catalog.types.source_connection.SourceConnection"
        ] = None,
    ) -> "capo_service_catalog.types.update_product_output.UpdateProductOutput":
        """<p>Updates the specified product.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            id: <p>The product identifier.</p>
            name: <p>The updated product name.</p>
            owner: <p>The updated owner of the product.</p>
            description: <p>The updated description of the product.</p>
            distributor: <p>The updated distributor of the product.</p>
            support_description: <p>The updated support description for the product.</p>
            support_email: <p>The updated support email for the product.</p>
            support_url: <p>The updated support URL for the product.</p>
            add_tags: <p>The tags to add to the product.</p>
            remove_tags: <p>The tags to remove from the product.</p>
            source_connection: <p>Specifies connection details for the updated product and syncs the product to the connection source artifact. This automatically manages the product's artifacts based on changes to the source. The <code>SourceConnection</code> parameter consists of the following sub-fields.</p> <ul> <li> <p> <code>Type</code> </p> </li> <li> <p> <code>ConnectionParamters</code> </p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_product_input.UpdateProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_product_output.UpdateProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_product.async_update_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_product_input.UpdateProductInput = {
            "id": id
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if name is not None:
            input_["name"] = name
        if owner is not None:
            input_["owner"] = owner
        if description is not None:
            input_["description"] = description
        if distributor is not None:
            input_["distributor"] = distributor
        if support_description is not None:
            input_["support_description"] = support_description
        if support_email is not None:
            input_["support_email"] = support_email
        if support_url is not None:
            input_["support_url"] = support_url
        if add_tags is not None:
            input_["add_tags"] = add_tags
        if remove_tags is not None:
            input_["remove_tags"] = remove_tags
        if source_connection is not None:
            input_["source_connection"] = source_connection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_provisioned_product(
        self,
        update_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        provisioned_product_name: Optional[
            "capo_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
        ] = None,
        provisioned_product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        product_id: Optional["capo_service_catalog.types.id.Id"] = None,
        product_name: Optional[
            "capo_service_catalog.types.product_view_name.ProductViewName"
        ] = None,
        provisioning_artifact_id: Optional["capo_service_catalog.types.id.Id"] = None,
        provisioning_artifact_name: Optional[
            "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
        ] = None,
        path_id: Optional["capo_service_catalog.types.id.Id"] = None,
        path_name: Optional[
            "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
        ] = None,
        provisioning_parameters: Optional[
            "capo_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
        ] = None,
        provisioning_preferences: Optional[
            "capo_service_catalog.types.update_provisioning_preferences.UpdateProvisioningPreferences"
        ] = None,
        tags: Optional["capo_service_catalog.types.tags.Tags"] = None,
    ) -> "capo_service_catalog.types.update_provisioned_product_output.UpdateProvisionedProductOutput":
        """<p>Requests updates to the configuration of the specified provisioned product.</p> <p>If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.</p> <p>You can check the status of this request using <a>DescribeRecord</a>.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            provisioned_product_name: <p>The name of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>
            provisioned_product_id: <p>The identifier of the provisioned product. You must provide the name or ID, but not both.</p>
            product_id: <p>The identifier of the product. You must provide the name or ID, but not both.</p>
            product_name: <p>The name of the product. You must provide the name or ID, but not both.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact.</p>
            provisioning_artifact_name: <p>The name of the provisioning artifact. You must provide the name or ID, but not both.</p>
            path_id: <p>The path identifier. This value is optional if the product has a default path, and required if the product has more than one path. You must provide the name or ID, but not both.</p>
            path_name: <p>The name of the path. You must provide the name or ID, but not both.</p>
            provisioning_parameters: <p>The new parameters.</p>
            provisioning_preferences: <p>An object that contains information about the provisioning preferences for a stack set.</p>
            tags: <p>One or more tags. Requires the product to have <code>RESOURCE_UPDATE</code> constraint with <code>TagUpdatesOnProvisionedProduct</code> set to <code>ALLOWED</code> to allow tag updates.</p>
            update_token: <p>The idempotency token that uniquely identifies the provisioning update request.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_provisioned_product_input.UpdateProvisionedProductInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_provisioned_product_output.UpdateProvisionedProductOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_provisioned_product

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_provisioned_product.async_update_provisioned_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_provisioned_product_input.UpdateProvisionedProductInput = {
            "update_token": update_token
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if provisioned_product_name is not None:
            input_["provisioned_product_name"] = provisioned_product_name
        if provisioned_product_id is not None:
            input_["provisioned_product_id"] = provisioned_product_id
        if product_id is not None:
            input_["product_id"] = product_id
        if product_name is not None:
            input_["product_name"] = product_name
        if provisioning_artifact_id is not None:
            input_["provisioning_artifact_id"] = provisioning_artifact_id
        if provisioning_artifact_name is not None:
            input_["provisioning_artifact_name"] = provisioning_artifact_name
        if path_id is not None:
            input_["path_id"] = path_id
        if path_name is not None:
            input_["path_name"] = path_name
        if provisioning_parameters is not None:
            input_["provisioning_parameters"] = provisioning_parameters
        if provisioning_preferences is not None:
            input_["provisioning_preferences"] = provisioning_preferences
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_provisioned_product_properties(
        self,
        provisioned_product_id: "capo_service_catalog.types.id.Id",
        provisioned_product_properties: "capo_service_catalog.types.provisioned_product_properties.ProvisionedProductProperties",
        idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.update_provisioned_product_properties_output.UpdateProvisionedProductPropertiesOutput":
        """<p>Requests updates to the properties of the specified provisioned product.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            provisioned_product_id: <p>The identifier of the provisioned product.</p>
            provisioned_product_properties: <p>A map that contains the provisioned product properties to be updated.</p> <p>The <code>LAUNCH_ROLE</code> key accepts role ARNs. This key allows an administrator to call <code>UpdateProvisionedProductProperties</code> to update the launch role that is associated with a provisioned product. This role is used when an end user calls a provisioning operation such as <code>UpdateProvisionedProduct</code>, <code>TerminateProvisionedProduct</code>, or <code>ExecuteProvisionedProductServiceAction</code>. Only a role ARN is valid. A user ARN is invalid. </p> <p>The <code>OWNER</code> key accepts user ARNs, IAM role ARNs, and STS assumed-role ARNs. The owner is the user that has permission to see, update, terminate, and execute service actions in the provisioned product.</p> <p>The administrator can change the owner of a provisioned product to another IAM or STS entity within the same account. Both end user owners and administrators can see ownership history of the provisioned product using the <code>ListRecordHistory</code> API. The new owner can describe all past records for the provisioned product using the <code>DescribeRecord</code> API. The previous owner can no longer use <code>DescribeRecord</code>, but can still see the product's history from when he was an owner using <code>ListRecordHistory</code>.</p> <p>If a provisioned product ownership is assigned to an end user, they can see and perform any action through the API or Service Catalog console such as update, terminate, and execute service actions. If an end user provisions a product and the owner is updated to someone else, they will no longer be able to see or perform any actions through API or the Service Catalog console on that provisioned product.</p>
            idempotency_token: <p>The idempotency token that uniquely identifies the provisioning product update request.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.invalid_state_exception.InvalidStateException: <p>An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_provisioned_product_properties_input.UpdateProvisionedProductPropertiesInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_provisioned_product_properties_output.UpdateProvisionedProductPropertiesOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_provisioned_product_properties

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_provisioned_product_properties.async_update_provisioned_product_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_provisioned_product_properties_input.UpdateProvisionedProductPropertiesInput = {
            "provisioned_product_id": provisioned_product_id,
            "provisioned_product_properties": provisioned_product_properties,
            "idempotency_token": idempotency_token,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_provisioning_artifact(
        self,
        product_id: "capo_service_catalog.types.id.Id",
        provisioning_artifact_id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
        name: Optional[
            "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.provisioning_artifact_description.ProvisioningArtifactDescription"
        ] = None,
        active: Optional[
            "capo_service_catalog.types.provisioning_artifact_active.ProvisioningArtifactActive"
        ] = None,
        guidance: Optional[
            "capo_service_catalog.types.provisioning_artifact_guidance.ProvisioningArtifactGuidance"
        ] = None,
    ) -> "capo_service_catalog.types.update_provisioning_artifact_output.UpdateProvisioningArtifactOutput":
        """<p>Updates the specified provisioning artifact (also known as a version) for the specified product.</p> <p>You cannot update a provisioning artifact for a product that was shared with you.</p>

        Args:
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>
            product_id: <p>The product identifier.</p>
            provisioning_artifact_id: <p>The identifier of the provisioning artifact.</p>
            name: <p>The updated name of the provisioning artifact.</p>
            description: <p>The updated description of the provisioning artifact.</p>
            active: <p>Indicates whether the product version is active.</p> <p>Inactive provisioning artifacts are invisible to end users. End users cannot launch or update a provisioned product from an inactive provisioning artifact.</p>
            guidance: <p>Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.</p> <p>The <code>DEFAULT</code> value indicates that the product version is active.</p> <p>The administrator can set the guidance to <code>DEPRECATED</code> to inform users that the product version is deprecated. Users are able to make updates to a provisioned product of a deprecated version but cannot launch new provisioned products using a deprecated version.</p>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_provisioning_artifact_input.UpdateProvisioningArtifactInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_provisioning_artifact_output.UpdateProvisioningArtifactOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_provisioning_artifact

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_provisioning_artifact.async_update_provisioning_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_provisioning_artifact_input.UpdateProvisioningArtifactInput = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
        }
        if accept_language is not None:
            input_["accept_language"] = accept_language
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if active is not None:
            input_["active"] = active
        if guidance is not None:
            input_["guidance"] = guidance

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_action(
        self,
        id: "capo_service_catalog.types.id.Id",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        name: Optional[
            "capo_service_catalog.types.service_action_name.ServiceActionName"
        ] = None,
        definition: Optional[
            "capo_service_catalog.types.service_action_definition_map.ServiceActionDefinitionMap"
        ] = None,
        description: Optional[
            "capo_service_catalog.types.service_action_description.ServiceActionDescription"
        ] = None,
        accept_language: Optional[
            "capo_service_catalog.types.accept_language.AcceptLanguage"
        ] = None,
    ) -> "capo_service_catalog.types.update_service_action_output.UpdateServiceActionOutput":
        """<p>Updates a self-service action.</p>

        Args:
            id: <p>The self-service action identifier.</p>
            name: <p>The self-service action name.</p>
            definition: <p>A map that defines the self-service action.</p>
            description: <p>The self-service action description.</p>
            accept_language: <p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>

        Raises:
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_service_action_input.UpdateServiceActionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_service_action_output.UpdateServiceActionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_service_action

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_service_action.async_update_service_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_service_action_input.UpdateServiceActionInput = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if definition is not None:
            input_["definition"] = definition
        if description is not None:
            input_["description"] = description
        if accept_language is not None:
            input_["accept_language"] = accept_language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_tag_option(
        self,
        id: "capo_service_catalog.types.tag_option_id.TagOptionId",
        *,
        config_overrides: Optional[AsyncServiceCatalogClientConfig] = None,
        value: Optional[
            "capo_service_catalog.types.tag_option_value.TagOptionValue"
        ] = None,
        active: Optional[
            "capo_service_catalog.types.tag_option_active.TagOptionActive"
        ] = None,
    ) -> "capo_service_catalog.types.update_tag_option_output.UpdateTagOptionOutput":
        """<p>Updates the specified TagOption.</p>

        Args:
            id: <p>The TagOption identifier.</p>
            value: <p>The updated value.</p>
            active: <p>The updated active state.</p>

        Raises:
            capo_service_catalog.errors.duplicate_resource_exception.DuplicateResourceException: <p>The specified resource is a duplicate.</p>
            capo_service_catalog.errors.invalid_parameters_exception.InvalidParametersException: <p>One or more parameters provided to the operation are not valid.</p>
            capo_service_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_service_catalog.errors.tag_option_not_migrated_exception.TagOptionNotMigratedException: <p>An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the Amazon Web Services Management Console to perform the migration process before retrying the operation.</p>
            capo_service_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_service_catalog.types.update_tag_option_input.UpdateTagOptionInput]",
        ) -> AsyncOperationResponse[
            "capo_service_catalog.types.update_tag_option_output.UpdateTagOptionOutput"
        ]:
            import capo_service_catalog._operations.aws242_service_catalog_service.update_tag_option

            (
                output,
                http_response,
            ) = await capo_service_catalog._operations.aws242_service_catalog_service.update_tag_option.async_update_tag_option(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_service_catalog.types.update_tag_option_input.UpdateTagOptionInput = {
            "id": id
        }
        if value is not None:
            input_["value"] = value
        if active is not None:
            input_["active"] = active

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
