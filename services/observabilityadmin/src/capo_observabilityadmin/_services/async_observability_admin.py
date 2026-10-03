"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ObservabilityAdmin``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_observabilityadmin._auth._signers
import capo_observabilityadmin._auth._sigv4
from capo_observabilityadmin._auth._identity import Credentials
from capo_observabilityadmin._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_observabilityadmin._auth._zapros_handler import AuthMiddleware
from capo_observabilityadmin._pagination import resolve_path as _resolve_path
from capo_observabilityadmin._resources.observability_admin.telemetry_pipeline_resource import (
    AsyncTelemetryPipelineResource,
)
from capo_observabilityadmin._services._aws_config import aaws_config
from capo_observabilityadmin._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_observabilityadmin.types.account_identifiers
    import capo_observabilityadmin.types.all_regions
    import capo_observabilityadmin.types.centralization_rule
    import capo_observabilityadmin.types.centralization_rule_summary
    import capo_observabilityadmin.types.create_centralization_rule_for_organization_input
    import capo_observabilityadmin.types.create_centralization_rule_for_organization_output
    import capo_observabilityadmin.types.create_dataset_integration_input
    import capo_observabilityadmin.types.create_dataset_integration_output
    import capo_observabilityadmin.types.create_s3_table_integration_input
    import capo_observabilityadmin.types.create_s3_table_integration_output
    import capo_observabilityadmin.types.create_telemetry_pipeline_input
    import capo_observabilityadmin.types.create_telemetry_pipeline_output
    import capo_observabilityadmin.types.create_telemetry_rule_for_organization_input
    import capo_observabilityadmin.types.create_telemetry_rule_for_organization_output
    import capo_observabilityadmin.types.create_telemetry_rule_input
    import capo_observabilityadmin.types.create_telemetry_rule_output
    import capo_observabilityadmin.types.dataset_integration_summary
    import capo_observabilityadmin.types.delete_centralization_rule_for_organization_input
    import capo_observabilityadmin.types.delete_dataset_integration_input
    import capo_observabilityadmin.types.delete_s3_table_integration_input
    import capo_observabilityadmin.types.delete_telemetry_pipeline_input
    import capo_observabilityadmin.types.delete_telemetry_pipeline_output
    import capo_observabilityadmin.types.delete_telemetry_rule_for_organization_input
    import capo_observabilityadmin.types.delete_telemetry_rule_input
    import capo_observabilityadmin.types.encryption
    import capo_observabilityadmin.types.get_centralization_rule_for_organization_input
    import capo_observabilityadmin.types.get_centralization_rule_for_organization_output
    import capo_observabilityadmin.types.get_dataset_integration_input
    import capo_observabilityadmin.types.get_dataset_integration_output
    import capo_observabilityadmin.types.get_s3_table_integration_input
    import capo_observabilityadmin.types.get_s3_table_integration_output
    import capo_observabilityadmin.types.get_telemetry_enrichment_status_output
    import capo_observabilityadmin.types.get_telemetry_evaluation_status_for_organization_output
    import capo_observabilityadmin.types.get_telemetry_evaluation_status_output
    import capo_observabilityadmin.types.get_telemetry_pipeline_input
    import capo_observabilityadmin.types.get_telemetry_pipeline_output
    import capo_observabilityadmin.types.get_telemetry_rule_for_organization_input
    import capo_observabilityadmin.types.get_telemetry_rule_for_organization_output
    import capo_observabilityadmin.types.get_telemetry_rule_input
    import capo_observabilityadmin.types.get_telemetry_rule_output
    import capo_observabilityadmin.types.integration_summary
    import capo_observabilityadmin.types.list_centralization_rules_for_organization_input
    import capo_observabilityadmin.types.list_centralization_rules_for_organization_max_results
    import capo_observabilityadmin.types.list_centralization_rules_for_organization_output
    import capo_observabilityadmin.types.list_dataset_integrations_input
    import capo_observabilityadmin.types.list_dataset_integrations_max_results
    import capo_observabilityadmin.types.list_dataset_integrations_output
    import capo_observabilityadmin.types.list_resource_telemetry_for_organization_input
    import capo_observabilityadmin.types.list_resource_telemetry_for_organization_max_results
    import capo_observabilityadmin.types.list_resource_telemetry_for_organization_output
    import capo_observabilityadmin.types.list_resource_telemetry_input
    import capo_observabilityadmin.types.list_resource_telemetry_max_results
    import capo_observabilityadmin.types.list_resource_telemetry_output
    import capo_observabilityadmin.types.list_s3_table_integrations_input
    import capo_observabilityadmin.types.list_s3_table_integrations_max_results
    import capo_observabilityadmin.types.list_s3_table_integrations_output
    import capo_observabilityadmin.types.list_tags_for_resource_input
    import capo_observabilityadmin.types.list_tags_for_resource_output
    import capo_observabilityadmin.types.list_telemetry_pipelines_input
    import capo_observabilityadmin.types.list_telemetry_pipelines_max_results
    import capo_observabilityadmin.types.list_telemetry_pipelines_output
    import capo_observabilityadmin.types.list_telemetry_rules_for_organization_input
    import capo_observabilityadmin.types.list_telemetry_rules_for_organization_max_results
    import capo_observabilityadmin.types.list_telemetry_rules_for_organization_output
    import capo_observabilityadmin.types.list_telemetry_rules_input
    import capo_observabilityadmin.types.list_telemetry_rules_max_results
    import capo_observabilityadmin.types.list_telemetry_rules_output
    import capo_observabilityadmin.types.next_token
    import capo_observabilityadmin.types.organization_unit_identifiers
    import capo_observabilityadmin.types.records
    import capo_observabilityadmin.types.regions
    import capo_observabilityadmin.types.resource_arn
    import capo_observabilityadmin.types.resource_identifier_prefix
    import capo_observabilityadmin.types.resource_types
    import capo_observabilityadmin.types.rule_identifier
    import capo_observabilityadmin.types.rule_name
    import capo_observabilityadmin.types.signal_type
    import capo_observabilityadmin.types.start_telemetry_enrichment_output
    import capo_observabilityadmin.types.start_telemetry_evaluation_for_organization_input
    import capo_observabilityadmin.types.start_telemetry_evaluation_input
    import capo_observabilityadmin.types.stop_telemetry_enrichment_output
    import capo_observabilityadmin.types.tag_key_list
    import capo_observabilityadmin.types.tag_map_input
    import capo_observabilityadmin.types.tag_resource_input
    import capo_observabilityadmin.types.telemetry_configuration
    import capo_observabilityadmin.types.telemetry_configuration_state
    import capo_observabilityadmin.types.telemetry_pipeline_configuration
    import capo_observabilityadmin.types.telemetry_pipeline_identifier
    import capo_observabilityadmin.types.telemetry_pipeline_name
    import capo_observabilityadmin.types.telemetry_pipeline_summary
    import capo_observabilityadmin.types.telemetry_rule
    import capo_observabilityadmin.types.telemetry_rule_summary
    import capo_observabilityadmin.types.test_telemetry_pipeline_input
    import capo_observabilityadmin.types.test_telemetry_pipeline_output
    import capo_observabilityadmin.types.untag_resource_input
    import capo_observabilityadmin.types.update_centralization_rule_for_organization_input
    import capo_observabilityadmin.types.update_centralization_rule_for_organization_output
    import capo_observabilityadmin.types.update_dataset_integration_input
    import capo_observabilityadmin.types.update_dataset_integration_output
    import capo_observabilityadmin.types.update_telemetry_pipeline_input
    import capo_observabilityadmin.types.update_telemetry_pipeline_output
    import capo_observabilityadmin.types.update_telemetry_rule_for_organization_input
    import capo_observabilityadmin.types.update_telemetry_rule_for_organization_output
    import capo_observabilityadmin.types.update_telemetry_rule_input
    import capo_observabilityadmin.types.update_telemetry_rule_output
    import capo_observabilityadmin.types.validate_telemetry_pipeline_configuration_input
    import capo_observabilityadmin.types.validate_telemetry_pipeline_configuration_output


class AsyncObservabilityAdminClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncObservabilityAdminClient:
    """A client for the ``ObservabilityAdmin`` service.

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
        self._config = AsyncObservabilityAdminClientConfig(
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
        self.telemetry_pipeline_resource = AsyncTelemetryPipelineResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncObservabilityAdminClientConfig = config_overrides or {}
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

    async def create_centralization_rule_for_organization(
        self,
        rule_name: "capo_observabilityadmin.types.rule_name.RuleName",
        rule: "capo_observabilityadmin.types.centralization_rule.CentralizationRule",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_centralization_rule_for_organization_output.CreateCentralizationRuleForOrganizationOutput":
        """<p>Creates a centralization rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_name: <p>A unique name for the organization-wide centralization rule being created.</p>
            rule: <p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>
            tags: <p>The key-value pairs to associate with the organization telemetry rule resource for categorization and management purposes.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.create_centralization_rule_for_organization_input.CreateCentralizationRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.create_centralization_rule_for_organization_output.CreateCentralizationRuleForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_centralization_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.create_centralization_rule_for_organization.async_create_centralization_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_centralization_rule_for_organization_input.CreateCentralizationRuleForOrganizationInput = {
            "rule_name": rule_name,
            "rule": rule,
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

    async def create_dataset_integration(
        self,
        role_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_dataset_integration_output.CreateDatasetIntegrationOutput":
        """<p>Creates a dataset integration for the caller's account in the current region and returns its ARN.</p> <p>To use this operation, you must have permission to access the dataset integration resources through the IAM role specified in the <code>RoleArn</code> parameter.</p> <p>If a dataset integration already exists for the account, this operation fails with a <code>ConflictException</code>.</p>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon CloudWatch permission to access the resources needed for the dataset integration.</p>
            tags: <p>The key-value pairs to associate with the dataset integration resource for categorization and management purposes.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.create_dataset_integration_input.CreateDatasetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.create_dataset_integration_output.CreateDatasetIntegrationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_dataset_integration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.create_dataset_integration.async_create_dataset_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_dataset_integration_input.CreateDatasetIntegrationInput = {
            "role_arn": role_arn
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

    async def create_s3_table_integration(
        self,
        encryption: "capo_observabilityadmin.types.encryption.Encryption",
        role_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_s3_table_integration_output.CreateS3TableIntegrationOutput":
        """<p>Creates an integration between CloudWatch and S3 Tables for analytics. This integration enables querying CloudWatch telemetry data using analytics engines like Amazon Athena, Amazon Redshift, and Apache Spark.</p>

        Args:
            encryption: <p>The encryption configuration for the S3 Table integration, including the encryption algorithm and KMS key settings.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.</p>
            tags: <p>The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.create_s3_table_integration_input.CreateS3TableIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.create_s3_table_integration_output.CreateS3TableIntegrationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_s3_table_integration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.create_s3_table_integration.async_create_s3_table_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_s3_table_integration_input.CreateS3TableIntegrationInput = {
            "encryption": encryption,
            "role_arn": role_arn,
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

    async def create_telemetry_rule(
        self,
        rule_name: "capo_observabilityadmin.types.rule_name.RuleName",
        rule: "capo_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_telemetry_rule_output.CreateTelemetryRuleOutput":
        """<p> Creates a telemetry rule that defines how telemetry should be configured for Amazon Web Services resources in your account. The rule specifies which resources should have telemetry enabled and how that telemetry data should be collected based on resource type, telemetry type, and selection criteria. </p>

        Args:
            rule_name: <p> A unique name for the telemetry rule being created. </p>
            rule: <p> The configuration details for the telemetry rule, including the resource type, telemetry type, destination configuration, and selection criteria for which resources the rule applies to. </p>
            tags: <p> The key-value pairs to associate with the telemetry rule resource for categorization and management purposes. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.create_telemetry_rule_input.CreateTelemetryRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.create_telemetry_rule_output.CreateTelemetryRuleOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_telemetry_rule

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.create_telemetry_rule.async_create_telemetry_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_telemetry_rule_input.CreateTelemetryRuleInput = {
            "rule_name": rule_name,
            "rule": rule,
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

    async def create_telemetry_rule_for_organization(
        self,
        rule_name: "capo_observabilityadmin.types.rule_name.RuleName",
        rule: "capo_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_telemetry_rule_for_organization_output.CreateTelemetryRuleForOrganizationOutput":
        """<p> Creates a telemetry rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_name: <p> A unique name for the organization-wide telemetry rule being created. </p>
            rule: <p> The configuration details for the organization-wide telemetry rule, including the resource type, telemetry type, destination configuration, and selection criteria for which resources the rule applies to across the organization. </p>
            tags: <p> The key-value pairs to associate with the organization telemetry rule resource for categorization and management purposes. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.create_telemetry_rule_for_organization_input.CreateTelemetryRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.create_telemetry_rule_for_organization_output.CreateTelemetryRuleForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_telemetry_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.create_telemetry_rule_for_organization.async_create_telemetry_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_telemetry_rule_for_organization_input.CreateTelemetryRuleForOrganizationInput = {
            "rule_name": rule_name,
            "rule": rule,
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

    async def delete_centralization_rule_for_organization(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an organization-wide centralization rule. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_identifier: <p>The identifier (name or ARN) of the organization centralization rule to delete.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.delete_centralization_rule_for_organization_input.DeleteCentralizationRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.delete_centralization_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.delete_centralization_rule_for_organization.async_delete_centralization_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_centralization_rule_for_organization_input.DeleteCentralizationRuleForOrganizationInput = {
            "rule_identifier": rule_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset_integration(
        self,
        arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes a dataset integration for the caller's account in the current region. This operation is idempotent; if you submit the same delete more than once, each call succeeds.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the dataset integration to delete.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.delete_dataset_integration_input.DeleteDatasetIntegrationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.delete_dataset_integration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.delete_dataset_integration.async_delete_dataset_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_dataset_integration_input.DeleteDatasetIntegrationInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_s3_table_integration(
        self,
        arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an S3 Table integration and its associated data. This operation removes the connection between CloudWatch Observability Admin and S3 Tables.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the S3 Table integration to delete.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.invalid_state_exception.InvalidStateException: <p> The requested operation cannot be completed on the specified resource in the current state. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.delete_s3_table_integration_input.DeleteS3TableIntegrationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.delete_s3_table_integration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.delete_s3_table_integration.async_delete_s3_table_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_s3_table_integration_input.DeleteS3TableIntegrationInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_telemetry_rule(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Deletes a telemetry rule from your account. Any telemetry configurations previously created by the rule will remain but no new resources will be configured by this rule. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the telemetry rule to delete. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.delete_telemetry_rule_input.DeleteTelemetryRuleInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.delete_telemetry_rule

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.delete_telemetry_rule.async_delete_telemetry_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_telemetry_rule_input.DeleteTelemetryRuleInput = {
            "rule_identifier": rule_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_telemetry_rule_for_organization(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Deletes an organization-wide telemetry rule. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the organization telemetry rule to delete. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.delete_telemetry_rule_for_organization_input.DeleteTelemetryRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.delete_telemetry_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.delete_telemetry_rule_for_organization.async_delete_telemetry_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_telemetry_rule_for_organization_input.DeleteTelemetryRuleForOrganizationInput = {
            "rule_identifier": rule_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_centralization_rule_for_organization(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.get_centralization_rule_for_organization_output.GetCentralizationRuleForOrganizationOutput":
        """<p>Retrieves the details of a specific organization centralization rule. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_identifier: <p>The identifier (name or ARN) of the organization centralization rule to retrieve.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.get_centralization_rule_for_organization_input.GetCentralizationRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_centralization_rule_for_organization_output.GetCentralizationRuleForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_centralization_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_centralization_rule_for_organization.async_get_centralization_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_centralization_rule_for_organization_input.GetCentralizationRuleForOrganizationInput = {
            "rule_identifier": rule_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dataset_integration(
        self,
        arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.get_dataset_integration_output.GetDatasetIntegrationOutput":
        """<p>Returns the dataset integration for the caller's account in the current region.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the dataset integration to retrieve.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.get_dataset_integration_input.GetDatasetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_dataset_integration_output.GetDatasetIntegrationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_dataset_integration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_dataset_integration.async_get_dataset_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_dataset_integration_input.GetDatasetIntegrationInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_s3_table_integration(
        self,
        arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.get_s3_table_integration_output.GetS3TableIntegrationOutput":
        """<p>Retrieves information about a specific S3 Table integration, including its configuration, status, and metadata.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the S3 Table integration to retrieve.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.get_s3_table_integration_input.GetS3TableIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_s3_table_integration_output.GetS3TableIntegrationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_s3_table_integration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_s3_table_integration.async_get_s3_table_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_s3_table_integration_input.GetS3TableIntegrationInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_telemetry_enrichment_status(
        self, *, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> "capo_observabilityadmin.types.get_telemetry_enrichment_status_output.GetTelemetryEnrichmentStatusOutput":
        """<p> Returns the current status of the resource tags for telemetry feature, which enhances telemetry data with additional resource metadata from Resource Explorer. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_telemetry_enrichment_status_output.GetTelemetryEnrichmentStatusOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_enrichment_status

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_telemetry_enrichment_status.async_get_telemetry_enrichment_status(
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

    async def get_telemetry_evaluation_status(
        self, *, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> "capo_observabilityadmin.types.get_telemetry_evaluation_status_output.GetTelemetryEvaluationStatusOutput":
        """<p> Returns the current onboarding status of the telemetry config feature, including the status of the feature and reason the feature failed to start or stop. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_telemetry_evaluation_status_output.GetTelemetryEvaluationStatusOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status.async_get_telemetry_evaluation_status(
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

    async def get_telemetry_evaluation_status_for_organization(
        self, *, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> "capo_observabilityadmin.types.get_telemetry_evaluation_status_for_organization_output.GetTelemetryEvaluationStatusForOrganizationOutput":
        """<p> This returns the onboarding status of the telemetry configuration feature for the organization. It can only be called by a Management Account of an Amazon Web Services Organization or an assigned Delegated Admin Account of Amazon CloudWatch telemetry config. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_telemetry_evaluation_status_for_organization_output.GetTelemetryEvaluationStatusForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status_for_organization.async_get_telemetry_evaluation_status_for_organization(
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

    async def get_telemetry_rule(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> (
        "capo_observabilityadmin.types.get_telemetry_rule_output.GetTelemetryRuleOutput"
    ):
        """<p> Retrieves the details of a specific telemetry rule in your account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the telemetry rule to retrieve. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.get_telemetry_rule_input.GetTelemetryRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_telemetry_rule_output.GetTelemetryRuleOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_rule

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_telemetry_rule.async_get_telemetry_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_telemetry_rule_input.GetTelemetryRuleInput = {
            "rule_identifier": rule_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_telemetry_rule_for_organization(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.get_telemetry_rule_for_organization_output.GetTelemetryRuleForOrganizationOutput":
        """<p> Retrieves the details of a specific organization telemetry rule. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the organization telemetry rule to retrieve. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.get_telemetry_rule_for_organization_input.GetTelemetryRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_telemetry_rule_for_organization_output.GetTelemetryRuleForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_telemetry_rule_for_organization.async_get_telemetry_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_telemetry_rule_for_organization_input.GetTelemetryRuleForOrganizationInput = {
            "rule_identifier": rule_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_centralization_rules_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        all_regions: Optional[bool] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_centralization_rules_for_organization_max_results.ListCentralizationRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_centralization_rules_for_organization_output.ListCentralizationRulesForOrganizationOutput":
        """<p>Lists all centralization rules in your organization. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_name_prefix: <p>A string to filter organization centralization rules whose names begin with the specified prefix.</p>
            all_regions: <p>A flag determining whether to return organization centralization rules from all regions or only the current region.</p>
            max_results: <p>The maximum number of organization centralization rules to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_centralization_rules_for_organization_input.ListCentralizationRulesForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_centralization_rules_for_organization_output.ListCentralizationRulesForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_centralization_rules_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_centralization_rules_for_organization.async_list_centralization_rules_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_centralization_rules_for_organization_input.ListCentralizationRulesForOrganizationInput = {}
        if rule_name_prefix is not None:
            input_["rule_name_prefix"] = rule_name_prefix
        if all_regions is not None:
            input_["all_regions"] = all_regions
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

    async def iter_list_centralization_rules_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        all_regions: Optional[bool] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_centralization_rules_for_organization_max_results.ListCentralizationRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.centralization_rule_summary.CentralizationRuleSummary]":
        _token = next_token
        while True:
            _response = await self.list_centralization_rules_for_organization(
                config_overrides=config_overrides,
                rule_name_prefix=rule_name_prefix,
                all_regions=all_regions,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("centralization_rule_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dataset_integrations(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_dataset_integrations_max_results.ListDatasetIntegrationsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_dataset_integrations_output.ListDatasetIntegrationsOutput":
        """<p>Returns the dataset integrations in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_dataset_integrations_input.ListDatasetIntegrationsInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_dataset_integrations_output.ListDatasetIntegrationsOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_dataset_integrations

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_dataset_integrations.async_list_dataset_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_dataset_integrations_input.ListDatasetIntegrationsInput = {}
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

    async def iter_list_dataset_integrations(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_dataset_integrations_max_results.ListDatasetIntegrationsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.dataset_integration_summary.DatasetIntegrationSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_integrations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dataset_integration_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_telemetry(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        resource_identifier_prefix: Optional[
            "capo_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "capo_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "capo_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_resource_telemetry_max_results.ListResourceTelemetryMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_resource_telemetry_output.ListResourceTelemetryOutput":
        """<p> Returns a list of telemetry configurations for Amazon Web Services resources supported by telemetry config. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html">Auditing CloudWatch telemetry configurations</a>. </p>

        Args:
            resource_identifier_prefix: <p> A string used to filter resources which have a <code>ResourceIdentifier</code> starting with the <code>ResourceIdentifierPrefix</code>. </p>
            resource_types: <p> A list of resource types used to filter resources supported by telemetry config. If this parameter is provided, the service returns the resources in the same order as specified in the request. Currently supported resource types for discovery are:</p> <ul> <li> <p> <code>AWS::EC2::Instance</code> </p> </li> <li> <p> <code>AWS::EC2::VPC</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::EKS::Cluster</code> </p> </li> <li> <p> <code>AWS::WAFv2::WebACL</code> </p> </li> <li> <p> <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code> (Network Load Balancers only)</p> </li> </ul>
            telemetry_configuration_state: <p> A key-value pair to filter resources based on the telemetry type and the state of the telemetry configuration. The key is the telemetry type and the value is the state. </p>
            resource_tags: <p> A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see <a href="https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html">What are tags?</a> </p>
            max_results: <p> A number field used to limit the number of results within the returned list. </p>
            next_token: <p> The token for the next set of items to return. A previous call generates this token. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_resource_telemetry_input.ListResourceTelemetryInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_resource_telemetry_output.ListResourceTelemetryOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_resource_telemetry

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_resource_telemetry.async_list_resource_telemetry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_resource_telemetry_input.ListResourceTelemetryInput = {}
        if resource_identifier_prefix is not None:
            input_["resource_identifier_prefix"] = resource_identifier_prefix
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if telemetry_configuration_state is not None:
            input_["telemetry_configuration_state"] = telemetry_configuration_state
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
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

    async def iter_list_resource_telemetry(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        resource_identifier_prefix: Optional[
            "capo_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "capo_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "capo_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_resource_telemetry_max_results.ListResourceTelemetryMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.telemetry_configuration.TelemetryConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_resource_telemetry(
                config_overrides=config_overrides,
                resource_identifier_prefix=resource_identifier_prefix,
                resource_types=resource_types,
                telemetry_configuration_state=telemetry_configuration_state,
                resource_tags=resource_tags,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_telemetry_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        account_identifiers: Optional[
            "capo_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        resource_identifier_prefix: Optional[
            "capo_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "capo_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "capo_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_resource_telemetry_for_organization_max_results.ListResourceTelemetryForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_resource_telemetry_for_organization_output.ListResourceTelemetryForOrganizationOutput":
        """<p> Returns a list of telemetry configurations for Amazon Web Services resources supported by telemetry config in the organization. </p>

        Args:
            account_identifiers: <p> A list of Amazon Web Services accounts used to filter the resources to those associated with the specified accounts. </p>
            resource_identifier_prefix: <p> A string used to filter resources in the organization which have a <code>ResourceIdentifier</code> starting with the <code>ResourceIdentifierPrefix</code>. </p>
            resource_types: <p> A list of resource types used to filter resources in the organization. If this parameter is provided, the service returns the resources in the same order as specified in the request. Currently supported resource types for discovery are:</p> <ul> <li> <p> <code>AWS::EC2::Instance</code> </p> </li> <li> <p> <code>AWS::EC2::VPC</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::EKS::Cluster</code> </p> </li> <li> <p> <code>AWS::WAFv2::WebACL</code> </p> </li> <li> <p> <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code> (Network Load Balancers only)</p> </li> </ul>
            telemetry_configuration_state: <p> A key-value pair to filter resources in the organization based on the telemetry type and the state of the telemetry configuration. The key is the telemetry type and the value is the state. </p>
            resource_tags: <p> A key-value pair to filter resources in the organization based on tags associated with the resource. Fore more information about tags, see <a href="https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html">What are tags?</a> </p>
            max_results: <p> A number field used to limit the number of results within the returned list. </p>
            next_token: <p> The token for the next set of items to return. A previous call provides this token. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_resource_telemetry_for_organization_input.ListResourceTelemetryForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_resource_telemetry_for_organization_output.ListResourceTelemetryForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_resource_telemetry_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_resource_telemetry_for_organization.async_list_resource_telemetry_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_resource_telemetry_for_organization_input.ListResourceTelemetryForOrganizationInput = {}
        if account_identifiers is not None:
            input_["account_identifiers"] = account_identifiers
        if resource_identifier_prefix is not None:
            input_["resource_identifier_prefix"] = resource_identifier_prefix
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if telemetry_configuration_state is not None:
            input_["telemetry_configuration_state"] = telemetry_configuration_state
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
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

    async def iter_list_resource_telemetry_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        account_identifiers: Optional[
            "capo_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        resource_identifier_prefix: Optional[
            "capo_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "capo_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "capo_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_resource_telemetry_for_organization_max_results.ListResourceTelemetryForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.telemetry_configuration.TelemetryConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_resource_telemetry_for_organization(
                config_overrides=config_overrides,
                account_identifiers=account_identifiers,
                resource_identifier_prefix=resource_identifier_prefix,
                resource_types=resource_types,
                telemetry_configuration_state=telemetry_configuration_state,
                resource_tags=resource_tags,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_s3_table_integrations(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_s3_table_integrations_max_results.ListS3TableIntegrationsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_s3_table_integrations_output.ListS3TableIntegrationsOutput":
        """<p>Lists all S3 Table integrations in your account. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of S3 Table integrations to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_s3_table_integrations_input.ListS3TableIntegrationsInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_s3_table_integrations_output.ListS3TableIntegrationsOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_s3_table_integrations

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_s3_table_integrations.async_list_s3_table_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_s3_table_integrations_input.ListS3TableIntegrationsInput = {}
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

    async def iter_list_s3_table_integrations(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_s3_table_integrations_max_results.ListS3TableIntegrationsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.integration_summary.IntegrationSummary]":
        _token = next_token
        while True:
            _response = await self.list_s3_table_integrations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("integration_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p> Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the telemetry rule resource whose tags you want to list. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_telemetry_rules(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_rules_max_results.ListTelemetryRulesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_telemetry_rules_output.ListTelemetryRulesOutput":
        """<p> Lists all telemetry rules in your account. You can filter the results by specifying a rule name prefix. </p>

        Args:
            rule_name_prefix: <p> A string to filter telemetry rules whose names begin with the specified prefix. </p>
            max_results: <p> The maximum number of telemetry rules to return in a single call. </p>
            next_token: <p> The token for the next set of results. A previous call generates this token. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_telemetry_rules_input.ListTelemetryRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_telemetry_rules_output.ListTelemetryRulesOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_telemetry_rules

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_telemetry_rules.async_list_telemetry_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_telemetry_rules_input.ListTelemetryRulesInput = {}
        if rule_name_prefix is not None:
            input_["rule_name_prefix"] = rule_name_prefix
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

    async def iter_list_telemetry_rules(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_rules_max_results.ListTelemetryRulesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.telemetry_rule_summary.TelemetryRuleSummary]":
        _token = next_token
        while True:
            _response = await self.list_telemetry_rules(
                config_overrides=config_overrides,
                rule_name_prefix=rule_name_prefix,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_rule_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_telemetry_rules_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        source_account_ids: Optional[
            "capo_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        source_organization_unit_ids: Optional[
            "capo_observabilityadmin.types.organization_unit_identifiers.OrganizationUnitIdentifiers"
        ] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_rules_for_organization_max_results.ListTelemetryRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_telemetry_rules_for_organization_output.ListTelemetryRulesForOrganizationOutput":
        """<p> Lists all telemetry rules in your organization. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_name_prefix: <p> A string to filter organization telemetry rules whose names begin with the specified prefix. </p>
            source_account_ids: <p> The list of account IDs to filter organization telemetry rules by their source accounts. </p>
            source_organization_unit_ids: <p> The list of organizational unit IDs to filter organization telemetry rules by their source organizational units. </p>
            max_results: <p> The maximum number of organization telemetry rules to return in a single call. </p>
            next_token: <p> The token for the next set of results. A previous call generates this token. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_telemetry_rules_for_organization_input.ListTelemetryRulesForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_telemetry_rules_for_organization_output.ListTelemetryRulesForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_telemetry_rules_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_telemetry_rules_for_organization.async_list_telemetry_rules_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_telemetry_rules_for_organization_input.ListTelemetryRulesForOrganizationInput = {}
        if rule_name_prefix is not None:
            input_["rule_name_prefix"] = rule_name_prefix
        if source_account_ids is not None:
            input_["source_account_ids"] = source_account_ids
        if source_organization_unit_ids is not None:
            input_["source_organization_unit_ids"] = source_organization_unit_ids
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

    async def iter_list_telemetry_rules_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        source_account_ids: Optional[
            "capo_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        source_organization_unit_ids: Optional[
            "capo_observabilityadmin.types.organization_unit_identifiers.OrganizationUnitIdentifiers"
        ] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_rules_for_organization_max_results.ListTelemetryRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.telemetry_rule_summary.TelemetryRuleSummary]":
        _token = next_token
        while True:
            _response = await self.list_telemetry_rules_for_organization(
                config_overrides=config_overrides,
                rule_name_prefix=rule_name_prefix,
                source_account_ids=source_account_ids,
                source_organization_unit_ids=source_organization_unit_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_rule_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_telemetry_enrichment(
        self, *, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> "capo_observabilityadmin.types.start_telemetry_enrichment_output.StartTelemetryEnrichmentOutput":
        """<p> Enables the resource tags for telemetry feature for your account, which enhances telemetry data with additional resource metadata from Resource Explorer to provide richer context for monitoring and observability. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.start_telemetry_enrichment_output.StartTelemetryEnrichmentOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.start_telemetry_enrichment

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.start_telemetry_enrichment.async_start_telemetry_enrichment(
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

    async def start_telemetry_evaluation(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        regions: Optional["capo_observabilityadmin.types.regions.Regions"] = None,
        all_regions: Optional[
            "capo_observabilityadmin.types.all_regions.AllRegions"
        ] = None,
    ) -> None:
        """<p> This action begins onboarding the caller Amazon Web Services account to the telemetry config feature. </p>

        Args:
            regions: <p> An optional list of Amazon Web Services Regions to include in multi-region telemetry evaluation. The current region is always implicitly included and must not be specified in this list. When provided, telemetry evaluation starts in the current region and propagates to all specified regions. Mutually exclusive with <code>AllRegions</code>. If neither <code>Regions</code> nor <code>AllRegions</code> is provided, the operation applies only to the current region. </p>
            all_regions: <p> If set to <code>true</code>, telemetry evaluation starts in all Amazon Web Services Regions where Amazon CloudWatch Observability Admin is available in the current partition. The current region becomes the home region for managing multi-region evaluation. When new regions become available, evaluation automatically expands to include them. Mutually exclusive with <code>Regions</code>. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.start_telemetry_evaluation_input.StartTelemetryEvaluationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.start_telemetry_evaluation

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.start_telemetry_evaluation.async_start_telemetry_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.start_telemetry_evaluation_input.StartTelemetryEvaluationInput = {}
        if regions is not None:
            input_["regions"] = regions
        if all_regions is not None:
            input_["all_regions"] = all_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_telemetry_evaluation_for_organization(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        regions: Optional["capo_observabilityadmin.types.regions.Regions"] = None,
        all_regions: Optional[
            "capo_observabilityadmin.types.all_regions.AllRegions"
        ] = None,
    ) -> None:
        """<p> This actions begins onboarding the organization and all member accounts to the telemetry config feature. </p>

        Args:
            regions: <p> An optional list of Amazon Web Services Regions to include in multi-region telemetry evaluation for the organization. The current region is always implicitly included and must not be specified in this list. When provided, telemetry evaluation starts in the current region and propagates to all specified regions for the organization. Mutually exclusive with <code>AllRegions</code>. If neither <code>Regions</code> nor <code>AllRegions</code> is provided, the operation applies only to the current region. </p>
            all_regions: <p> If set to <code>true</code>, telemetry evaluation for the organization starts in all Amazon Web Services Regions where Amazon CloudWatch Observability Admin is available in the current partition. The current region becomes the home region for managing multi-region evaluation for the organization. When new regions become available, evaluation automatically expands to include them. Mutually exclusive with <code>Regions</code>. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.start_telemetry_evaluation_for_organization_input.StartTelemetryEvaluationForOrganizationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.start_telemetry_evaluation_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.start_telemetry_evaluation_for_organization.async_start_telemetry_evaluation_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.start_telemetry_evaluation_for_organization_input.StartTelemetryEvaluationForOrganizationInput = {}
        if regions is not None:
            input_["regions"] = regions
        if all_regions is not None:
            input_["all_regions"] = all_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_telemetry_enrichment(
        self, *, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> "capo_observabilityadmin.types.stop_telemetry_enrichment_output.StopTelemetryEnrichmentOutput":
        """<p> Disables the resource tags for telemetry feature for your account, stopping the enhancement of telemetry data with additional resource metadata. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.stop_telemetry_enrichment_output.StopTelemetryEnrichmentOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.stop_telemetry_enrichment

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.stop_telemetry_enrichment.async_stop_telemetry_enrichment(
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

    async def stop_telemetry_evaluation(
        self, *, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> None:
        """<p> This action begins offboarding the caller Amazon Web Services account from the telemetry config feature. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation.async_stop_telemetry_evaluation(
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

    async def stop_telemetry_evaluation_for_organization(
        self, *, config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None
    ) -> None:
        """<p> This action offboards the Organization of the caller Amazon Web Services account from the telemetry config feature. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation_for_organization.async_stop_telemetry_evaluation_for_organization(
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

    async def tag_resource(
        self,
        resource_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        tags: "capo_observabilityadmin.types.tag_map_input.TagMapInput",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Adds or updates tags for a resource. Supports telemetry rule resources and telemetry pipeline resources. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the telemetry rule resource to tag. </p>
            tags: <p> The key-value pairs to add or update for the telemetry rule resource. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.tag_resource

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.tag_resource_input.TagResourceInput = {
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

    async def test_telemetry_pipeline(
        self,
        records: "capo_observabilityadmin.types.records.Records",
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        signal_type: Optional[
            "capo_observabilityadmin.types.signal_type.SignalType"
        ] = None,
    ) -> "capo_observabilityadmin.types.test_telemetry_pipeline_output.TestTelemetryPipelineOutput":
        """<p>Tests a pipeline configuration with sample records to validate data processing before deployment. This operation helps ensure your pipeline configuration works as expected. </p>

        Args:
            records: <p>The sample records to process through the pipeline configuration for testing purposes.</p>
            configuration: <p>The pipeline configuration to test with the provided sample records.</p>
            signal_type: <p>The type of telemetry signal to test. If not specified, defaults to log processing.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.test_telemetry_pipeline_input.TestTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.test_telemetry_pipeline_output.TestTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.test_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.test_telemetry_pipeline.async_test_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.test_telemetry_pipeline_input.TestTelemetryPipelineInput = {
            "records": records,
            "configuration": configuration,
        }
        if signal_type is not None:
            input_["signal_type"] = signal_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        tag_keys: "capo_observabilityadmin.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Removes tags from a resource. Supports telemetry rule resources and telemetry pipeline resources. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the telemetry rule resource to remove tags from. </p>
            tag_keys: <p> The list of tag keys to remove from the telemetry rule resource. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_observabilityadmin._operations.observability_admin.untag_resource

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.untag_resource_input.UntagResourceInput = {
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

    async def update_centralization_rule_for_organization(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        rule: "capo_observabilityadmin.types.centralization_rule.CentralizationRule",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.update_centralization_rule_for_organization_output.UpdateCentralizationRuleForOrganizationOutput":
        """<p>Updates an existing centralization rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_identifier: <p>The identifier (name or ARN) of the organization centralization rule to update.</p>
            rule: <p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.update_centralization_rule_for_organization_input.UpdateCentralizationRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.update_centralization_rule_for_organization_output.UpdateCentralizationRuleForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.update_centralization_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.update_centralization_rule_for_organization.async_update_centralization_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.update_centralization_rule_for_organization_input.UpdateCentralizationRuleForOrganizationInput = {
            "rule_identifier": rule_identifier,
            "rule": rule,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_dataset_integration(
        self,
        arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        role_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.update_dataset_integration_output.UpdateDatasetIntegrationOutput":
        """<p>Updates a dataset integration for the caller's account in the current region. This operation is idempotent; if you submit the same update more than once, each call succeeds.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the dataset integration to update.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to associate with the dataset integration.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.update_dataset_integration_input.UpdateDatasetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.update_dataset_integration_output.UpdateDatasetIntegrationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.update_dataset_integration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.update_dataset_integration.async_update_dataset_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.update_dataset_integration_input.UpdateDatasetIntegrationInput = {
            "arn": arn,
            "role_arn": role_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_telemetry_rule(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        rule: "capo_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.update_telemetry_rule_output.UpdateTelemetryRuleOutput":
        """<p> Updates an existing telemetry rule in your account. If multiple users attempt to modify the same telemetry rule simultaneously, a ConflictException is returned to provide specific error information for concurrent modification scenarios. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the telemetry rule to update. </p>
            rule: <p> The new configuration details for the telemetry rule. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.update_telemetry_rule_input.UpdateTelemetryRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.update_telemetry_rule_output.UpdateTelemetryRuleOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.update_telemetry_rule

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.update_telemetry_rule.async_update_telemetry_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.update_telemetry_rule_input.UpdateTelemetryRuleInput = {
            "rule_identifier": rule_identifier,
            "rule": rule,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_telemetry_rule_for_organization(
        self,
        rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier",
        rule: "capo_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.update_telemetry_rule_for_organization_output.UpdateTelemetryRuleForOrganizationOutput":
        """<p> Updates an existing telemetry rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the organization telemetry rule to update. </p>
            rule: <p> The new configuration details for the organization telemetry rule, including resource type, telemetry type, and destination configuration. </p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.update_telemetry_rule_for_organization_input.UpdateTelemetryRuleForOrganizationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.update_telemetry_rule_for_organization_output.UpdateTelemetryRuleForOrganizationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.update_telemetry_rule_for_organization

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.update_telemetry_rule_for_organization.async_update_telemetry_rule_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.update_telemetry_rule_for_organization_input.UpdateTelemetryRuleForOrganizationInput = {
            "rule_identifier": rule_identifier,
            "rule": rule,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def validate_telemetry_pipeline_configuration(
        self,
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.validate_telemetry_pipeline_configuration_output.ValidateTelemetryPipelineConfigurationOutput":
        """<p>Validates a pipeline configuration without creating the pipeline. This operation checks the configuration for syntax errors and compatibility issues.</p>

        Args:
            configuration: <p>The pipeline configuration to validate for syntax and compatibility.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.validate_telemetry_pipeline_configuration_input.ValidateTelemetryPipelineConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.validate_telemetry_pipeline_configuration_output.ValidateTelemetryPipelineConfigurationOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.validate_telemetry_pipeline_configuration

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.validate_telemetry_pipeline_configuration.async_validate_telemetry_pipeline_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.validate_telemetry_pipeline_configuration_input.ValidateTelemetryPipelineConfigurationInput = {
            "configuration": configuration
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_telemetry_pipeline(
        self,
        name: "capo_observabilityadmin.types.telemetry_pipeline_name.TelemetryPipelineName",
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        tags: Optional[
            "capo_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "capo_observabilityadmin.types.create_telemetry_pipeline_output.CreateTelemetryPipelineOutput":
        """<p>Creates a telemetry pipeline for processing and transforming telemetry data. The pipeline defines how data flows from sources through processors to destinations, enabling data transformation and delivering capabilities. </p>

        Args:
            name: <p>The name of the telemetry pipeline to create. The name must be unique within your account.</p>
            configuration: <p>The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations. For more information about pipeline components, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-components-reference.html">Amazon CloudWatch User Guide</a> </p>
            tags: <p>The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The requested operation would exceed the allowed quota for the specified resource type. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.create_telemetry_pipeline_input.CreateTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.create_telemetry_pipeline_output.CreateTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.create_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.create_telemetry_pipeline.async_create_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.create_telemetry_pipeline_input.CreateTelemetryPipelineInput = {
            "name": name,
            "configuration": configuration,
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

    async def get_telemetry_pipeline(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.get_telemetry_pipeline_output.GetTelemetryPipelineOutput":
        """<p>Retrieves information about a specific telemetry pipeline, including its configuration, status, and metadata.</p>

        Args:
            pipeline_identifier: <p>The identifier (name or ARN) of the telemetry pipeline to retrieve.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.get_telemetry_pipeline_input.GetTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.get_telemetry_pipeline_output.GetTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.get_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.get_telemetry_pipeline.async_get_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.get_telemetry_pipeline_input.GetTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_telemetry_pipeline(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        configuration: "capo_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.update_telemetry_pipeline_output.UpdateTelemetryPipelineOutput":
        """<p>Updates the configuration of an existing telemetry pipeline.</p> <note> <p>The following attributes cannot be updated after pipeline creation:</p> <ul> <li> <p> <b>Pipeline name</b> - The pipeline name is immutable</p> </li> <li> <p> <b>Pipeline ARN</b> - The ARN is automatically generated and cannot be changed</p> </li> <li> <p> <b>Source type</b> - Once a pipeline is created with a specific source type (such as S3, CloudWatch Logs, GitHub, or third-party sources), it cannot be changed to a different source type</p> </li> </ul> <p>Processors can be added, removed, or modified. However, some processors are not supported for third-party pipelines and cannot be added through updates.</p> </note> <p> <b>Source-Specific Update Rules</b> </p> <dl> <dt>CloudWatch Logs Sources (Vended and Custom)</dt> <dd> <p> <b>Updatable:</b> <code>sts_role_arn</code> </p> <p> <b>Fixed:</b> <code>data_source_name</code>, <code>data_source_type</code>, sink (must remain <code>@original</code>)</p> </dd> <dt>S3 Sources (Crowdstrike, Zscaler, SentinelOne, Custom)</dt> <dd> <p> <b>Updatable:</b> All SQS configuration parameters, <code>sts_role_arn</code>, codec settings, compression type, bucket ownership settings, sink log group</p> <p> <b>Fixed:</b> <code>notification_type</code>, <code>aws.region</code> </p> </dd> <dt>GitHub Audit Logs</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>scope</code> (can switch between ORGANIZATION/ENTERPRISE), <code>organization</code> or <code>enterprise</code> name, <code>range</code>, authentication credentials (PAT or GitHub App)</p> </dd> <dt>Microsoft Sources (Entra ID, Office365, Windows)</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>tenant_id</code>, <code>workspace_id</code> (Windows only), OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Okta Sources (SSO, Auth0)</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>domain</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Palo Alto Networks</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>hostname</code>, basic authentication credentials (<code>username</code>, <code>password</code>)</p> </dd> <dt>ServiceNow CMDB</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>instance_url</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> <dt>Wiz CNAPP</dt> <dd> <p> <b>Updatable:</b> All Amazon Web Services Secrets Manager attributes, <code>region</code>, <code>range</code>, OAuth2 credentials (<code>client_id</code>, <code>client_secret</code>)</p> </dd> </dl>

        Args:
            pipeline_identifier: <p>The ARN of the telemetry pipeline to update.</p>
            configuration: <p>The new configuration for the telemetry pipeline, including updated sources, processors, and destinations.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.update_telemetry_pipeline_input.UpdateTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.update_telemetry_pipeline_output.UpdateTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.update_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.update_telemetry_pipeline.async_update_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.update_telemetry_pipeline_input.UpdateTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_telemetry_pipeline(
        self,
        pipeline_identifier: "capo_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier",
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
    ) -> "capo_observabilityadmin.types.delete_telemetry_pipeline_output.DeleteTelemetryPipelineOutput":
        """<p>Deletes a telemetry pipeline and its associated resources. This operation stops data processing and removes the pipeline configuration.</p>

        Args:
            pipeline_identifier: <p>The ARN of the telemetry pipeline to delete.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.conflict_exception.ConflictException: <p> The requested operation conflicts with the current state of the specified resource or with another request. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource (such as a telemetry rule) could not be found. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.delete_telemetry_pipeline_input.DeleteTelemetryPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.delete_telemetry_pipeline_output.DeleteTelemetryPipelineOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.delete_telemetry_pipeline

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.delete_telemetry_pipeline.async_delete_telemetry_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.delete_telemetry_pipeline_input.DeleteTelemetryPipelineInput = {
            "pipeline_identifier": pipeline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_telemetry_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_pipelines_max_results.ListTelemetryPipelinesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "capo_observabilityadmin.types.list_telemetry_pipelines_output.ListTelemetryPipelinesOutput":
        """<p>Returns a list of telemetry pipelines in your account. Returns up to 100 results. If more than 100 telemetry pipelines exist, include the <code>NextToken</code> value from the response to retrieve the next set of results.</p>

        Args:
            max_results: <p>The maximum number of telemetry pipelines to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>

        Raises:
            capo_observabilityadmin.errors.access_denied_exception.AccessDeniedException: <p> Indicates you don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management for Amazon Web Services resources</a> in the IAM user guide. </p>
            capo_observabilityadmin.errors.internal_server_exception.InternalServerException: <p> Indicates the request has failed to process because of an unknown server error, exception, or failure. </p>
            capo_observabilityadmin.errors.too_many_requests_exception.TooManyRequestsException: <p> The request throughput limit was exceeded. </p>
            capo_observabilityadmin.errors.validation_exception.ValidationException: <p> Indicates input validation failed. Check your request parameters and retry the request. </p>
            capo_observabilityadmin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_observabilityadmin.types.list_telemetry_pipelines_input.ListTelemetryPipelinesInput]",
        ) -> AsyncOperationResponse[
            "capo_observabilityadmin.types.list_telemetry_pipelines_output.ListTelemetryPipelinesOutput"
        ]:
            import capo_observabilityadmin._operations.observability_admin.list_telemetry_pipelines

            (
                output,
                http_response,
            ) = await capo_observabilityadmin._operations.observability_admin.list_telemetry_pipelines.async_list_telemetry_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_observabilityadmin.types.list_telemetry_pipelines_input.ListTelemetryPipelinesInput = {}
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

    async def iter_list_telemetry_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "capo_observabilityadmin.types.list_telemetry_pipelines_max_results.ListTelemetryPipelinesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_observabilityadmin.types.telemetry_pipeline_summary.TelemetryPipelineSummary]":
        _token = next_token
        while True:
            _response = await self.list_telemetry_pipelines(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pipeline_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
