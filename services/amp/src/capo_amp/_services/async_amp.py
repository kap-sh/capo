"""Generated from Smithy shape ``com.amazonaws.amp#AmazonPrometheusService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_amp._auth._signers
import capo_amp._auth._sigv4
from capo_amp._auth._identity import Credentials
from capo_amp._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_amp._auth._zapros_handler import AuthMiddleware
from capo_amp._pagination import resolve_path as _resolve_path
from capo_amp._resources.amazon_prometheus_service.scraper import AsyncScraper
from capo_amp._resources.amazon_prometheus_service.workspace import AsyncWorkspace
from capo_amp._services._aws_config import aaws_config
from capo_amp._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_amp.types.alert_manager_definition_data
    import capo_amp.types.anomaly_detector_alias
    import capo_amp.types.anomaly_detector_configuration
    import capo_amp.types.anomaly_detector_evaluation_interval
    import capo_amp.types.anomaly_detector_id
    import capo_amp.types.anomaly_detector_missing_data_action
    import capo_amp.types.anomaly_detector_summary
    import capo_amp.types.create_alert_manager_definition_request
    import capo_amp.types.create_alert_manager_definition_response
    import capo_amp.types.create_anomaly_detector_request
    import capo_amp.types.create_anomaly_detector_response
    import capo_amp.types.create_logging_configuration_request
    import capo_amp.types.create_logging_configuration_response
    import capo_amp.types.create_query_logging_configuration_request
    import capo_amp.types.create_query_logging_configuration_response
    import capo_amp.types.create_rule_groups_namespace_request
    import capo_amp.types.create_rule_groups_namespace_response
    import capo_amp.types.create_scraper_request
    import capo_amp.types.create_scraper_response
    import capo_amp.types.create_workspace_request
    import capo_amp.types.create_workspace_response
    import capo_amp.types.delete_alert_manager_definition_request
    import capo_amp.types.delete_anomaly_detector_request
    import capo_amp.types.delete_logging_configuration_request
    import capo_amp.types.delete_query_logging_configuration_request
    import capo_amp.types.delete_resource_policy_request
    import capo_amp.types.delete_rule_groups_namespace_request
    import capo_amp.types.delete_scraper_logging_configuration_request
    import capo_amp.types.delete_scraper_request
    import capo_amp.types.delete_scraper_response
    import capo_amp.types.delete_workspace_request
    import capo_amp.types.describe_alert_manager_definition_request
    import capo_amp.types.describe_alert_manager_definition_response
    import capo_amp.types.describe_anomaly_detector_request
    import capo_amp.types.describe_anomaly_detector_response
    import capo_amp.types.describe_logging_configuration_request
    import capo_amp.types.describe_logging_configuration_response
    import capo_amp.types.describe_query_logging_configuration_request
    import capo_amp.types.describe_query_logging_configuration_response
    import capo_amp.types.describe_resource_policy_request
    import capo_amp.types.describe_resource_policy_response
    import capo_amp.types.describe_rule_groups_namespace_request
    import capo_amp.types.describe_rule_groups_namespace_response
    import capo_amp.types.describe_scraper_logging_configuration_request
    import capo_amp.types.describe_scraper_logging_configuration_response
    import capo_amp.types.describe_scraper_request
    import capo_amp.types.describe_scraper_response
    import capo_amp.types.describe_workspace_configuration_request
    import capo_amp.types.describe_workspace_configuration_response
    import capo_amp.types.describe_workspace_request
    import capo_amp.types.describe_workspace_response
    import capo_amp.types.destination
    import capo_amp.types.exporter_list
    import capo_amp.types.get_default_scraper_configuration_request
    import capo_amp.types.get_default_scraper_configuration_response
    import capo_amp.types.idempotency_token
    import capo_amp.types.kms_key_arn
    import capo_amp.types.limits_per_label_set_list
    import capo_amp.types.list_anomaly_detectors_request
    import capo_amp.types.list_anomaly_detectors_response
    import capo_amp.types.list_rule_groups_namespaces_request
    import capo_amp.types.list_rule_groups_namespaces_response
    import capo_amp.types.list_scrapers_request
    import capo_amp.types.list_scrapers_response
    import capo_amp.types.list_tags_for_resource_request
    import capo_amp.types.list_tags_for_resource_response
    import capo_amp.types.list_workspaces_request
    import capo_amp.types.list_workspaces_response
    import capo_amp.types.log_group_arn
    import capo_amp.types.logging_destinations
    import capo_amp.types.pagination_token
    import capo_amp.types.prometheus_metric_label_map
    import capo_amp.types.put_alert_manager_definition_request
    import capo_amp.types.put_alert_manager_definition_response
    import capo_amp.types.put_anomaly_detector_request
    import capo_amp.types.put_anomaly_detector_response
    import capo_amp.types.put_resource_policy_request
    import capo_amp.types.put_resource_policy_response
    import capo_amp.types.put_rule_groups_namespace_request
    import capo_amp.types.put_rule_groups_namespace_response
    import capo_amp.types.role_configuration
    import capo_amp.types.rule_groups_namespace_data
    import capo_amp.types.rule_groups_namespace_name
    import capo_amp.types.rule_groups_namespace_summary
    import capo_amp.types.scrape_configuration
    import capo_amp.types.scraper_alias
    import capo_amp.types.scraper_components
    import capo_amp.types.scraper_filters
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_logging_destination
    import capo_amp.types.scraper_summary
    import capo_amp.types.source
    import capo_amp.types.tag_keys
    import capo_amp.types.tag_map
    import capo_amp.types.tag_resource_request
    import capo_amp.types.tag_resource_response
    import capo_amp.types.untag_resource_request
    import capo_amp.types.untag_resource_response
    import capo_amp.types.update_logging_configuration_request
    import capo_amp.types.update_logging_configuration_response
    import capo_amp.types.update_query_logging_configuration_request
    import capo_amp.types.update_query_logging_configuration_response
    import capo_amp.types.update_scraper_logging_configuration_request
    import capo_amp.types.update_scraper_logging_configuration_response
    import capo_amp.types.update_scraper_request
    import capo_amp.types.update_scraper_response
    import capo_amp.types.update_workspace_alias_request
    import capo_amp.types.update_workspace_configuration_request
    import capo_amp.types.update_workspace_configuration_response
    import capo_amp.types.workspace_alias
    import capo_amp.types.workspace_id
    import capo_amp.types.workspace_summary


class AsyncampClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncampClient:
    """A client for the ``amp`` service.

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
        self._config = AsyncampClientConfig(
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
        self.scraper = AsyncScraper(self)
        self.workspace = AsyncWorkspace(self)

    def operation_options(
        self, config_overrides: Optional[AsyncampClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncampClientConfig = config_overrides or {}
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

    async def get_default_scraper_configuration(
        self, *, config_overrides: Optional[AsyncampClientConfig] = None
    ) -> "capo_amp.types.get_default_scraper_configuration_response.GetDefaultScraperConfigurationResponse":
        """<p>The <code>GetDefaultScraperConfiguration</code> operation returns the default scraper configuration used when Amazon EKS creates a scraper for you.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetDefaultScraperConfiguration

            >>> await client.get_default_scraper_configuration()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.get_default_scraper_configuration_request.GetDefaultScraperConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.get_default_scraper_configuration_response.GetDefaultScraperConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.get_default_scraper_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.get_default_scraper_configuration.async_get_default_scraper_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.get_default_scraper_configuration_request.GetDefaultScraperConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>The <code>ListTagsForResource</code> operation returns the tags that are associated with an Amazon Managed Service for Prometheus resource. Currently, the only resources that can be tagged are scrapers, workspaces, and rule groups namespaces. </p>

        Args:
            resource_arn: <p>The ARN of the resource to list tages for. Must be a workspace, scraper, or rule groups namespace resource.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        tags: "capo_amp.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.tag_resource_response.TagResourceResponse":
        """<p>The <code>TagResource</code> operation associates tags with an Amazon Managed Service for Prometheus resource. The only resources that can be tagged are rule groups namespaces, scrapers, and workspaces.</p> <p>If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag. To remove a tag, use <code>UntagResource</code>.</p>

        Args:
            resource_arn: <p>The ARN of the resource to apply tags to.</p>
            tags: <p>The list of tag keys and values to associate with the resource.</p> <p>Keys must not begin with <code>aws:</code>.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.tag_resource_request.TagResourceRequest = {
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
        tag_keys: "capo_amp.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from an Amazon Managed Service for Prometheus resource. The only resources that can be tagged are rule groups namespaces, scrapers, and workspaces. </p>

        Args:
            resource_arn: <p>The ARN of the resource from which to remove a tag.</p>
            tag_keys: <p>The keys of the tags to remove.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_scraper(
        self,
        scrape_configuration: "capo_amp.types.scrape_configuration.ScrapeConfiguration",
        source: "capo_amp.types.source.Source",
        destination: "capo_amp.types.destination.Destination",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional["capo_amp.types.scraper_alias.ScraperAlias"] = None,
        role_configuration: Optional[
            "capo_amp.types.role_configuration.RoleConfiguration"
        ] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_amp.types.tag_map.TagMap"] = None,
        exporters: Optional["capo_amp.types.exporter_list.ExporterList"] = None,
    ) -> "capo_amp.types.create_scraper_response.CreateScraperResponse":
        """<p>Creates a scraper to collect metrics from Prometheus-compatible sources. The scraper sends the collected metrics to Amazon Managed Service for Prometheus workspaces or CloudWatch datasets. You can configure scrapers to collect metrics from Amazon EKS clusters, Amazon MSK clusters, or from VPC-based sources that support DNS-based service discovery. Scrapers are flexible. You can configure a scraper to control which metrics to collect, the frequency of collection, which transformations to apply to the metrics, and more.</p> <p>An IAM role will be created for you that Amazon Managed Service for Prometheus uses to access the metrics in your source. You must configure this role with a policy that allows it to scrape metrics from your source. For Amazon EKS sources, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-eks-setup">Configuring your Amazon EKS cluster</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p> <p>The <code>scrapeConfiguration</code> parameter contains the base-64 encoded YAML configuration for the scraper.</p> <p>When creating a scraper, the service creates a <code>Network Interface</code> in each <b>Availability Zone</b> that are passed into <code>CreateScraper</code> through subnets. These network interfaces are used to connect to your source within the VPC for scraping metrics.</p> <note> <p>For more information about collectors, including what metrics are collected, and how to configure the scraper, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html">Using an Amazon Web Services managed collector</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p> </note>

        Args:
            alias: <p>(optional) An alias to associate with the scraper. This is for your use, and does not need to be unique.</p>
            scrape_configuration: <p>The configuration file to use in the new scraper. For more information, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration">Scraper configuration</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>
            source: <p>The Amazon EKS or Amazon Web Services cluster from which the scraper will collect metrics.</p>
            destination: <p>The destination where the scraper sends the collected metrics. Valid destinations are Amazon Managed Service for Prometheus workspaces and CloudWatch datasets.</p>
            role_configuration: <p>Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.</p>
            client_token: <p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>
            tags: <p>(Optional) The list of tag keys and values to associate with the scraper.</p>
            exporters: <p>The exporter configurations for the scraper. You can configure at most one Amazon OpenSearch Service domain. If you don't specify a value, the scraper is created without an exporter configuration.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateScraper with optional alias input, optional clientToken input, and one set of tags

            >>> await client.create_scraper(alias='alias', scrape_configuration={'configurationBlob': 'blob'}, source={'eksConfiguration': {'clusterArn': 'arn:aws:eks:us-west-2:123456789012:cluster/example', 'securityGroupIds': ['sg-abc123'], 'subnetIds': ['subnet-abc123']}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234'}}, client_token='token', tags={'exampleTag': 'exampleValue'})
            CreateScraper with generic VPC config with mandatory securityGroupIds and subnetIds

            >>> await client.create_scraper(alias='alias', scrape_configuration={'configurationBlob': 'blob'}, source={'vpcConfiguration': {'securityGroupIds': ['sg-abc123'], 'subnetIds': ['subnet-abc123']}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234'}}, client_token='token', tags={'exampleTag': 'exampleValue'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_scraper_request.CreateScraperRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_scraper_response.CreateScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_scraper

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_scraper.async_create_scraper(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.create_scraper_request.CreateScraperRequest = {
            "scrape_configuration": scrape_configuration,
            "source": source,
            "destination": destination,
        }
        if alias is not None:
            input_["alias"] = alias
        if role_configuration is not None:
            input_["role_configuration"] = role_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if exporters is not None:
            input_["exporters"] = exporters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_scraper(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_scraper_response.DescribeScraperResponse":
        """<p>The <code>DescribeScraper</code> operation displays information about an existing scraper.</p>

        Args:
            scraper_id: <p>The ID of the scraper to describe.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeScraper, with no statusReason to report

            >>> await client.describe_scraper(scraper_id='scraper-123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_scraper_request.DescribeScraperRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_scraper_response.DescribeScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_scraper

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_scraper.async_describe_scraper(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_scraper_request.DescribeScraperRequest = {
            "scraper_id": scraper_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_scraper(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional["capo_amp.types.scraper_alias.ScraperAlias"] = None,
        scrape_configuration: Optional[
            "capo_amp.types.scrape_configuration.ScrapeConfiguration"
        ] = None,
        destination: Optional["capo_amp.types.destination.Destination"] = None,
        role_configuration: Optional[
            "capo_amp.types.role_configuration.RoleConfiguration"
        ] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        exporters: Optional["capo_amp.types.exporter_list.ExporterList"] = None,
    ) -> "capo_amp.types.update_scraper_response.UpdateScraperResponse":
        """<p>Updates an existing scraper.</p> <p>You can't use this function to update the source from which the scraper is collecting metrics. To change the source, delete the scraper and create a new one.</p>

        Args:
            scraper_id: <p>The ID of the scraper to update.</p>
            alias: <p>The new alias of the scraper.</p>
            scrape_configuration: <p>Contains the base-64 encoded YAML configuration for the scraper.</p> <note> <p>For more information about configuring a scraper, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html">Using an Amazon Web Services managed collector</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p> </note>
            destination: <p>The new destination where the scraper sends metrics. Valid destinations are Amazon Managed Service for Prometheus workspaces and CloudWatch datasets.</p>
            role_configuration: <p>Use this structure to enable cross-account access, so that you can use a target account to access Prometheus metrics from source accounts.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>
            exporters: <p>The exporter configurations for the scraper. You can configure at most one Amazon OpenSearch Service domain. If you don't specify a value, the existing exporter configuration remains unchanged.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateScraper with all optional parameters

            >>> await client.update_scraper(scraper_id='scraper-123', alias='alias-update', scrape_configuration={'configurationBlob': 'blob-update'}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234-update'}}, client_token='token')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.update_scraper_request.UpdateScraperRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.update_scraper_response.UpdateScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.update_scraper

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.update_scraper.async_update_scraper(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.update_scraper_request.UpdateScraperRequest = {
            "scraper_id": scraper_id
        }
        if alias is not None:
            input_["alias"] = alias
        if scrape_configuration is not None:
            input_["scrape_configuration"] = scrape_configuration
        if destination is not None:
            input_["destination"] = destination
        if role_configuration is not None:
            input_["role_configuration"] = role_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if exporters is not None:
            input_["exporters"] = exporters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_scraper(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.delete_scraper_response.DeleteScraperResponse":
        """<p>The <code>DeleteScraper</code> operation deletes one scraper, and stops any metrics collection that the scraper performs.</p>

        Args:
            scraper_id: <p>The ID of the scraper to delete.</p>
            client_token: <p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteScraper with optional clientToken input

            >>> await client.delete_scraper(scraper_id='scraper-123', client_token='token')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_scraper_request.DeleteScraperRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.delete_scraper_response.DeleteScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.delete_scraper

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_scraper.async_delete_scraper(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_scraper_request.DeleteScraperRequest = {
            "scraper_id": scraper_id
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

    async def list_scrapers(
        self,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        filters: Optional["capo_amp.types.scraper_filters.ScraperFilters"] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_amp.types.list_scrapers_response.ListScrapersResponse":
        """<p>The <code>ListScrapers</code> operation lists all of the scrapers in your account. This includes scrapers being created or deleted. You can optionally filter the returned list.</p>

        Args:
            filters: <p>(Optional) A list of key-value pairs to filter the list of scrapers returned. Keys include <code>status</code>, <code>sourceArn</code>, <code>destinationArn</code>, and <code>alias</code>.</p> <p>Filters on the same key are <code>OR</code>'d together, and filters on different keys are <code>AND</code>'d together. For example, <code>status=ACTIVE&amp;status=CREATING&amp;alias=Test</code>, will return all scrapers that have the alias Test, and are either in status ACTIVE or CREATING.</p> <p>To find all active scrapers that are sending metrics to a specific Amazon Managed Service for Prometheus workspace, you would use the ARN of the workspace in a query:</p> <p> <code>status=ACTIVE&amp;destinationArn=arn:aws:aps:us-east-1:123456789012:workspace/ws-example1-1234-abcd-56ef-123456789012</code> </p> <p>If this is included, it filters the results to only the scrapers that match the filter.</p>
            next_token: <p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>Optional) The maximum number of scrapers to return in one <code>ListScrapers</code> operation. The range is 1-1000.</p> <p>If you omit this parameter, the default of 100 is used.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListScrapers, with a max result of 2, using a pagination token from a previous call to ListScrapers

            >>> await client.list_scrapers(max_results=2, next_token='previouslyGeneratedToken')
            ListScrapers, with filters

            >>> await client.list_scrapers(filters={'status': ['ACTIVE'], 'sourceArn': ['arn:aws:eks:us-west-2:123456789012:cluster/example1'], 'alias': ['alias1']})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.list_scrapers_request.ListScrapersRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.list_scrapers_response.ListScrapersResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_scrapers

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.list_scrapers.async_list_scrapers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.list_scrapers_request.ListScrapersRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_scrapers(
        self,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        filters: Optional["capo_amp.types.scraper_filters.ScraperFilters"] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_amp.types.scraper_summary.ScraperSummary]":
        _token = next_token
        while True:
            _response = await self.list_scrapers(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("scrapers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_scraper_logging_configuration(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        logging_destination: "capo_amp.types.scraper_logging_destination.ScraperLoggingDestination",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        scraper_components: Optional[
            "capo_amp.types.scraper_components.ScraperComponents"
        ] = None,
    ) -> "capo_amp.types.update_scraper_logging_configuration_response.UpdateScraperLoggingConfigurationResponse":
        """<p>Updates the logging configuration for a Amazon Managed Service for Prometheus scraper.</p>

        Args:
            scraper_id: <p>The ID of the scraper whose logging configuration will be updated.</p>
            logging_destination: <p>The destination where scraper logs will be sent.</p>
            scraper_components: <p>The list of scraper components to configure for logging.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.update_scraper_logging_configuration_request.UpdateScraperLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.update_scraper_logging_configuration_response.UpdateScraperLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.update_scraper_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.update_scraper_logging_configuration.async_update_scraper_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.update_scraper_logging_configuration_request.UpdateScraperLoggingConfigurationRequest = {
            "scraper_id": scraper_id,
            "logging_destination": logging_destination,
        }
        if scraper_components is not None:
            input_["scraper_components"] = scraper_components

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_scraper_logging_configuration(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_scraper_logging_configuration_response.DescribeScraperLoggingConfigurationResponse":
        """<p>Describes the logging configuration for a Amazon Managed Service for Prometheus scraper.</p>

        Args:
            scraper_id: <p>The ID of the scraper whose logging configuration will be described.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_scraper_logging_configuration_request.DescribeScraperLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_scraper_logging_configuration_response.DescribeScraperLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_scraper_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_scraper_logging_configuration.async_describe_scraper_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_scraper_logging_configuration_request.DescribeScraperLoggingConfigurationRequest = {
            "scraper_id": scraper_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_scraper_logging_configuration(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes the logging configuration for a Amazon Managed Service for Prometheus scraper.</p>

        Args:
            scraper_id: <p>The ID of the scraper whose logging configuration will be deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is processed exactly once.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_scraper_logging_configuration_request.DeleteScraperLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_scraper_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_scraper_logging_configuration.async_delete_scraper_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_scraper_logging_configuration_request.DeleteScraperLoggingConfigurationRequest = {
            "scraper_id": scraper_id
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

    async def create_workspace(
        self,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_amp.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_amp.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_amp.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a Prometheus workspace. A workspace is a logical space dedicated to the storage and querying of Prometheus metrics. You can have one or more workspaces in each Region in your account.</p>

        Args:
            alias: <p>An alias that you assign to this workspace to help you identify it. It does not need to be unique.</p> <p>Blank spaces at the beginning or end of the alias that you specify will be trimmed from the value used.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>
            tags: <p>The list of tag keys and values to associate with the workspace.</p>
            kms_key_arn: <p>(optional) The ARN for a customer managed KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html">Encryption at rest</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_workspace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_workspace.async_create_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.create_workspace_request.CreateWorkspaceRequest = {}
        if alias is not None:
            input_["alias"] = alias
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_workspace(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_workspace_response.DescribeWorkspaceResponse":
        """<p>Returns information about an existing workspace. </p>

        Args:
            workspace_id: <p>The ID of the workspace to describe.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_workspace_request.DescribeWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_workspace_response.DescribeWorkspaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_workspace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_workspace.async_describe_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_workspace_request.DescribeWorkspaceRequest = {
            "workspace_id": workspace_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workspace_alias(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Updates the alias of an existing workspace. </p>

        Args:
            workspace_id: <p>The ID of the workspace to update.</p>
            alias: <p>The new alias for the workspace. It does not need to be unique.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.update_workspace_alias_request.UpdateWorkspaceAliasRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.update_workspace_alias

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.update_workspace_alias.async_update_workspace_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.update_workspace_alias_request.UpdateWorkspaceAliasRequest = {
            "workspace_id": workspace_id
        }
        if alias is not None:
            input_["alias"] = alias
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

    async def delete_workspace(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes an existing workspace. </p> <note> <p>When you delete a workspace, the data that has been ingested into it is not immediately deleted. It will be permanently deleted within one month.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_workspace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_workspace.async_delete_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_workspace_request.DeleteWorkspaceRequest = {
            "workspace_id": workspace_id
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

    async def list_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_amp.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Lists all of the Amazon Managed Service for Prometheus workspaces in your account. This includes workspaces being created or deleted. </p>

        Args:
            next_token: <p>The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.</p> <p>For example, if your initial request has <code>maxResults</code> of 10, and there are 12 workspaces to return, then your initial request will return 10 and a <code>nextToken</code>. Using the next token in a subsequent call will return the remaining 2 workspaces.</p>
            alias: <p>If this is included, it filters the results to only the workspaces with names that start with the value that you specify here.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>
            max_results: <p>The maximum number of workspaces to return per request. The default is 100.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_workspaces

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.list_workspaces.async_list_workspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.list_workspaces_request.ListWorkspacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if alias is not None:
            input_["alias"] = alias
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_amp.types.workspace_summary.WorkspaceSummary]":
        _token = next_token
        while True:
            _response = await self.list_workspaces(
                config_overrides=config_overrides,
                next_token=_token,
                alias=alias,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workspaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_alert_manager_definition(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        data: "capo_amp.types.alert_manager_definition_data.AlertManagerDefinitionData",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.create_alert_manager_definition_response.CreateAlertManagerDefinitionResponse":
        """<p>The <code>CreateAlertManagerDefinition</code> operation creates the alert manager definition in a workspace. If a workspace already has an alert manager definition, don't use this operation to update it. Instead, use <code>PutAlertManagerDefinition</code>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to add the alert manager definition to.</p>
            data: <p>The alert manager definition to add. A base64-encoded version of the YAML alert manager definition file.</p> <p>For details about the alert manager definition, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html">AlertManagedDefinitionData</a>.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_alert_manager_definition_request.CreateAlertManagerDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_alert_manager_definition_response.CreateAlertManagerDefinitionResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_alert_manager_definition

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_alert_manager_definition.async_create_alert_manager_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.create_alert_manager_definition_request.CreateAlertManagerDefinitionRequest = {
            "workspace_id": workspace_id,
            "data": data,
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

    async def describe_alert_manager_definition(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_alert_manager_definition_response.DescribeAlertManagerDefinitionResponse":
        """<p>Retrieves the full information about the alert manager definition for a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to retrieve the alert manager definition from.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_alert_manager_definition_request.DescribeAlertManagerDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_alert_manager_definition_response.DescribeAlertManagerDefinitionResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_alert_manager_definition

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_alert_manager_definition.async_describe_alert_manager_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_alert_manager_definition_request.DescribeAlertManagerDefinitionRequest = {
            "workspace_id": workspace_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_alert_manager_definition(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        data: "capo_amp.types.alert_manager_definition_data.AlertManagerDefinitionData",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.put_alert_manager_definition_response.PutAlertManagerDefinitionResponse":
        """<p>Updates an existing alert manager definition in a workspace. If the workspace does not already have an alert manager definition, don't use this operation to create it. Instead, use <code>CreateAlertManagerDefinition</code>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to update the alert manager definition in.</p>
            data: <p>The alert manager definition to use. A base64-encoded version of the YAML alert manager definition file.</p> <p>For details about the alert manager definition, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html">AlertManagedDefinitionData</a>.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.put_alert_manager_definition_request.PutAlertManagerDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.put_alert_manager_definition_response.PutAlertManagerDefinitionResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.put_alert_manager_definition

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.put_alert_manager_definition.async_put_alert_manager_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.put_alert_manager_definition_request.PutAlertManagerDefinitionRequest = {
            "workspace_id": workspace_id,
            "data": data,
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

    async def delete_alert_manager_definition(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes the alert manager definition from a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to delete the alert manager definition from.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_alert_manager_definition_request.DeleteAlertManagerDefinitionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_alert_manager_definition

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_alert_manager_definition.async_delete_alert_manager_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_alert_manager_definition_request.DeleteAlertManagerDefinitionRequest = {
            "workspace_id": workspace_id
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

    async def create_anomaly_detector(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        alias: "capo_amp.types.anomaly_detector_alias.AnomalyDetectorAlias",
        configuration: "capo_amp.types.anomaly_detector_configuration.AnomalyDetectorConfiguration",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        evaluation_interval_in_seconds: Optional[
            "capo_amp.types.anomaly_detector_evaluation_interval.AnomalyDetectorEvaluationInterval"
        ] = None,
        missing_data_action: Optional[
            "capo_amp.types.anomaly_detector_missing_data_action.AnomalyDetectorMissingDataAction"
        ] = None,
        labels: Optional[
            "capo_amp.types.prometheus_metric_label_map.PrometheusMetricLabelMap"
        ] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_amp.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_amp.types.create_anomaly_detector_response.CreateAnomalyDetectorResponse"
    ):
        """<p>Creates an anomaly detector within a workspace using the Random Cut Forest algorithm for time-series analysis. The anomaly detector analyzes Amazon Managed Service for Prometheus metrics to identify unusual patterns and behaviors.</p>

        Args:
            workspace_id: <p>The identifier of the workspace where the anomaly detector will be created.</p>
            alias: <p>A user-friendly name for the anomaly detector.</p>
            evaluation_interval_in_seconds: <p>The frequency, in seconds, at which the anomaly detector evaluates metrics. The default value is 60 seconds.</p>
            missing_data_action: <p>Specifies the action to take when data is missing during evaluation.</p>
            configuration: <p>The algorithm configuration for the anomaly detector.</p>
            labels: <p>The Amazon Managed Service for Prometheus metric labels to associate with the anomaly detector.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>The metadata to apply to the anomaly detector to assist with categorization and organization.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_anomaly_detector_request.CreateAnomalyDetectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_anomaly_detector_response.CreateAnomalyDetectorResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_anomaly_detector

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_anomaly_detector.async_create_anomaly_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.create_anomaly_detector_request.CreateAnomalyDetectorRequest = {
            "workspace_id": workspace_id,
            "alias": alias,
            "configuration": configuration,
        }
        if evaluation_interval_in_seconds is not None:
            input_["evaluation_interval_in_seconds"] = evaluation_interval_in_seconds
        if missing_data_action is not None:
            input_["missing_data_action"] = missing_data_action
        if labels is not None:
            input_["labels"] = labels
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

    async def put_anomaly_detector(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        anomaly_detector_id: "capo_amp.types.anomaly_detector_id.AnomalyDetectorId",
        configuration: "capo_amp.types.anomaly_detector_configuration.AnomalyDetectorConfiguration",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        evaluation_interval_in_seconds: Optional[
            "capo_amp.types.anomaly_detector_evaluation_interval.AnomalyDetectorEvaluationInterval"
        ] = None,
        missing_data_action: Optional[
            "capo_amp.types.anomaly_detector_missing_data_action.AnomalyDetectorMissingDataAction"
        ] = None,
        labels: Optional[
            "capo_amp.types.prometheus_metric_label_map.PrometheusMetricLabelMap"
        ] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.put_anomaly_detector_response.PutAnomalyDetectorResponse":
        """<p>When you call <code>PutAnomalyDetector</code>, the operation creates a new anomaly detector if one doesn't exist, or updates an existing one. Each call to this operation triggers a complete retraining of the detector, which includes querying the minimum required samples and backfilling the detector with historical data. This process occurs regardless of whether you're making a minor change like updating the evaluation interval or making more substantial modifications. The operation serves as the single method for creating, updating, and retraining anomaly detectors.</p>

        Args:
            workspace_id: <p>The identifier of the workspace containing the anomaly detector to update.</p>
            anomaly_detector_id: <p>The identifier of the anomaly detector to update.</p>
            evaluation_interval_in_seconds: <p>The frequency, in seconds, at which the anomaly detector evaluates metrics.</p>
            missing_data_action: <p>Specifies the action to take when data is missing during evaluation.</p>
            configuration: <p>The algorithm configuration for the anomaly detector.</p>
            labels: <p>The Amazon Managed Service for Prometheus metric labels to associate with the anomaly detector.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.put_anomaly_detector_request.PutAnomalyDetectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.put_anomaly_detector_response.PutAnomalyDetectorResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.put_anomaly_detector

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.put_anomaly_detector.async_put_anomaly_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.put_anomaly_detector_request.PutAnomalyDetectorRequest = {
            "workspace_id": workspace_id,
            "anomaly_detector_id": anomaly_detector_id,
            "configuration": configuration,
        }
        if evaluation_interval_in_seconds is not None:
            input_["evaluation_interval_in_seconds"] = evaluation_interval_in_seconds
        if missing_data_action is not None:
            input_["missing_data_action"] = missing_data_action
        if labels is not None:
            input_["labels"] = labels
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

    async def describe_anomaly_detector(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        anomaly_detector_id: "capo_amp.types.anomaly_detector_id.AnomalyDetectorId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_anomaly_detector_response.DescribeAnomalyDetectorResponse":
        """<p>Retrieves detailed information about a specific anomaly detector, including its status and configuration.</p>

        Args:
            workspace_id: <p>The identifier of the workspace containing the anomaly detector.</p>
            anomaly_detector_id: <p>The identifier of the anomaly detector to describe.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_anomaly_detector_request.DescribeAnomalyDetectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_anomaly_detector_response.DescribeAnomalyDetectorResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_anomaly_detector

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_anomaly_detector.async_describe_anomaly_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_anomaly_detector_request.DescribeAnomalyDetectorRequest = {
            "workspace_id": workspace_id,
            "anomaly_detector_id": anomaly_detector_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_anomaly_detector(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        anomaly_detector_id: "capo_amp.types.anomaly_detector_id.AnomalyDetectorId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Removes an anomaly detector from a workspace. This operation is idempotent.</p>

        Args:
            workspace_id: <p>The identifier of the workspace containing the anomaly detector to delete.</p>
            anomaly_detector_id: <p>The identifier of the anomaly detector to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_anomaly_detector_request.DeleteAnomalyDetectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_anomaly_detector

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_anomaly_detector.async_delete_anomaly_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_anomaly_detector_request.DeleteAnomalyDetectorRequest = {
            "workspace_id": workspace_id,
            "anomaly_detector_id": anomaly_detector_id,
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

    async def list_anomaly_detectors(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional[
            "capo_amp.types.anomaly_detector_alias.AnomalyDetectorAlias"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_amp.types.list_anomaly_detectors_response.ListAnomalyDetectorsResponse":
        """<p>Returns a paginated list of anomaly detectors for a workspace with optional filtering by alias.</p>

        Args:
            workspace_id: <p>The identifier of the workspace containing the anomaly detectors to list.</p>
            alias: <p>Filters the results to anomaly detectors with the specified alias.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range is 1 to 1000.</p>
            next_token: <p>The pagination token to continue retrieving results.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.list_anomaly_detectors_request.ListAnomalyDetectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.list_anomaly_detectors_response.ListAnomalyDetectorsResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_anomaly_detectors

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.list_anomaly_detectors.async_list_anomaly_detectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.list_anomaly_detectors_request.ListAnomalyDetectorsRequest = {
            "workspace_id": workspace_id
        }
        if alias is not None:
            input_["alias"] = alias
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

    async def iter_list_anomaly_detectors(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional[
            "capo_amp.types.anomaly_detector_alias.AnomalyDetectorAlias"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
    ) -> (
        "AsyncIterator[capo_amp.types.anomaly_detector_summary.AnomalyDetectorSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_anomaly_detectors(
                workspace_id,
                config_overrides=config_overrides,
                alias=alias,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("anomaly_detectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        log_group_arn: "capo_amp.types.log_group_arn.LogGroupArn",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.create_logging_configuration_response.CreateLoggingConfigurationResponse":
        """<p>The <code>CreateLoggingConfiguration</code> operation creates rules and alerting logging configuration for the workspace. Use this operation to set the CloudWatch log group to which the logs will be published to.</p> <note> <p>These logging configurations are only for rules and alerting logs.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to create the logging configuration for.</p>
            log_group_arn: <p>The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_logging_configuration_request.CreateLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_logging_configuration_response.CreateLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_logging_configuration.async_create_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.create_logging_configuration_request.CreateLoggingConfigurationRequest = {
            "workspace_id": workspace_id,
            "log_group_arn": log_group_arn,
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

    async def describe_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_logging_configuration_response.DescribeLoggingConfigurationResponse":
        """<p>Returns complete information about the current rules and alerting logging configuration of the workspace.</p> <note> <p>These logging configurations are only for rules and alerting logs.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to describe the logging configuration for.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_logging_configuration_request.DescribeLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_logging_configuration_response.DescribeLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_logging_configuration.async_describe_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_logging_configuration_request.DescribeLoggingConfigurationRequest = {
            "workspace_id": workspace_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        log_group_arn: "capo_amp.types.log_group_arn.LogGroupArn",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.update_logging_configuration_response.UpdateLoggingConfigurationResponse":
        """<p>Updates the log group ARN or the workspace ID of the current rules and alerting logging configuration.</p> <note> <p>These logging configurations are only for rules and alerting logs.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to update the logging configuration for.</p>
            log_group_arn: <p>The ARN of the CloudWatch log group to which the vended log data will be published.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.update_logging_configuration_request.UpdateLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.update_logging_configuration_response.UpdateLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.update_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.update_logging_configuration.async_update_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.update_logging_configuration_request.UpdateLoggingConfigurationRequest = {
            "workspace_id": workspace_id,
            "log_group_arn": log_group_arn,
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

    async def delete_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes the rules and alerting logging configuration for a workspace.</p> <note> <p>These logging configurations are only for rules and alerting logs.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace containing the logging configuration to delete.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_logging_configuration.async_delete_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest = {
            "workspace_id": workspace_id
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

    async def create_query_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        destinations: "capo_amp.types.logging_destinations.LoggingDestinations",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.create_query_logging_configuration_response.CreateQueryLoggingConfigurationResponse":
        """<p>Creates a query logging configuration for the specified workspace. This operation enables logging of queries that exceed the specified QSP threshold.</p>

        Args:
            workspace_id: <p>The ID of the workspace for which to create the query logging configuration.</p>
            destinations: <p>The destinations where query logs will be sent. Only CloudWatch Logs destination is supported. The list must contain exactly one element.</p>
            client_token: <p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_query_logging_configuration_request.CreateQueryLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_query_logging_configuration_response.CreateQueryLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_query_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_query_logging_configuration.async_create_query_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.create_query_logging_configuration_request.CreateQueryLoggingConfigurationRequest = {
            "workspace_id": workspace_id,
            "destinations": destinations,
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

    async def describe_query_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_query_logging_configuration_response.DescribeQueryLoggingConfigurationResponse":
        """<p>Retrieves the details of the query logging configuration for the specified workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace for which to retrieve the query logging configuration.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_query_logging_configuration_request.DescribeQueryLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_query_logging_configuration_response.DescribeQueryLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_query_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_query_logging_configuration.async_describe_query_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_query_logging_configuration_request.DescribeQueryLoggingConfigurationRequest = {
            "workspace_id": workspace_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_query_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        destinations: "capo_amp.types.logging_destinations.LoggingDestinations",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.update_query_logging_configuration_response.UpdateQueryLoggingConfigurationResponse":
        """<p>Updates the query logging configuration for the specified workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace for which to update the query logging configuration.</p>
            destinations: <p>The destinations where query logs will be sent. Only CloudWatch Logs destination is supported. The list must contain exactly one element.</p>
            client_token: <p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.update_query_logging_configuration_request.UpdateQueryLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.update_query_logging_configuration_response.UpdateQueryLoggingConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.update_query_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.update_query_logging_configuration.async_update_query_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.update_query_logging_configuration_request.UpdateQueryLoggingConfigurationRequest = {
            "workspace_id": workspace_id,
            "destinations": destinations,
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

    async def delete_query_logging_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes the query logging configuration for the specified workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace from which to delete the query logging configuration.</p>
            client_token: <p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_query_logging_configuration_request.DeleteQueryLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_query_logging_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_query_logging_configuration.async_delete_query_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_query_logging_configuration_request.DeleteQueryLoggingConfigurationRequest = {
            "workspace_id": workspace_id
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

    async def create_rule_groups_namespace(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName",
        data: "capo_amp.types.rule_groups_namespace_data.RuleGroupsNamespaceData",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_amp.types.tag_map.TagMap"] = None,
    ) -> "capo_amp.types.create_rule_groups_namespace_response.CreateRuleGroupsNamespaceResponse":
        """<p>The <code>CreateRuleGroupsNamespace</code> operation creates a rule groups namespace within a workspace. A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces.</p> <important> <p>The combined length of a rule group namespace and a rule group name cannot exceed 721 UTF-8 bytes.</p> </important> <p>Use this operation only to create new rule groups namespaces. To update an existing rule groups namespace, use <code>PutRuleGroupsNamespace</code>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to add the rule groups namespace.</p>
            name: <p>The name for the new rule groups namespace.</p>
            data: <p>The rules file to use in the new namespace.</p> <p>Contains the base64-encoded version of the YAML rules file.</p> <p>For details about the rule groups namespace structure, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html">RuleGroupsNamespaceData</a>.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>
            tags: <p>The list of tag keys and values to associate with the rule groups namespace.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_rule_groups_namespace_request.CreateRuleGroupsNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_rule_groups_namespace_response.CreateRuleGroupsNamespaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_rule_groups_namespace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_rule_groups_namespace.async_create_rule_groups_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.create_rule_groups_namespace_request.CreateRuleGroupsNamespaceRequest = {
            "workspace_id": workspace_id,
            "name": name,
            "data": data,
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

    async def describe_rule_groups_namespace(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_rule_groups_namespace_response.DescribeRuleGroupsNamespaceResponse":
        """<p>Returns complete information about one rule groups namespace. To retrieve a list of rule groups namespaces, use <code>ListRuleGroupsNamespaces</code>.</p>

        Args:
            workspace_id: <p>The ID of the workspace containing the rule groups namespace.</p>
            name: <p>The name of the rule groups namespace that you want information for.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_rule_groups_namespace_request.DescribeRuleGroupsNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_rule_groups_namespace_response.DescribeRuleGroupsNamespaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_rule_groups_namespace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_rule_groups_namespace.async_describe_rule_groups_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_rule_groups_namespace_request.DescribeRuleGroupsNamespaceRequest = {
            "workspace_id": workspace_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_rule_groups_namespace(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName",
        data: "capo_amp.types.rule_groups_namespace_data.RuleGroupsNamespaceData",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_amp.types.put_rule_groups_namespace_response.PutRuleGroupsNamespaceResponse":
        """<p>Updates an existing rule groups namespace within a workspace. A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces.</p> <important> <p>The combined length of a rule group namespace and a rule group name cannot exceed 721 UTF-8 bytes.</p> </important> <p>Use this operation only to update existing rule groups namespaces. To create a new rule groups namespace, use <code>CreateRuleGroupsNamespace</code>.</p> <p>You can't use this operation to add tags to an existing rule groups namespace. Instead, use <code>TagResource</code>.</p>

        Args:
            workspace_id: <p>The ID of the workspace where you are updating the rule groups namespace.</p>
            name: <p>The name of the rule groups namespace that you are updating.</p>
            data: <p>The new rules file to use in the namespace. A base64-encoded version of the YAML rule groups file.</p> <p>For details about the rule groups namespace structure, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html">RuleGroupsNamespaceData</a>.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.put_rule_groups_namespace_request.PutRuleGroupsNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.put_rule_groups_namespace_response.PutRuleGroupsNamespaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.put_rule_groups_namespace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.put_rule_groups_namespace.async_put_rule_groups_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.put_rule_groups_namespace_request.PutRuleGroupsNamespaceRequest = {
            "workspace_id": workspace_id,
            "name": name,
            "data": data,
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

    async def delete_rule_groups_namespace(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes one rule groups namespace and its associated rule groups definition.</p>

        Args:
            workspace_id: <p>The ID of the workspace containing the rule groups namespace and definition to delete.</p>
            name: <p>The name of the rule groups namespace to delete.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_rule_groups_namespace_request.DeleteRuleGroupsNamespaceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_rule_groups_namespace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_rule_groups_namespace.async_delete_rule_groups_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_rule_groups_namespace_request.DeleteRuleGroupsNamespaceRequest = {
            "workspace_id": workspace_id,
            "name": name,
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

    async def list_rule_groups_namespaces(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        name: Optional[
            "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
        ] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_amp.types.list_rule_groups_namespaces_response.ListRuleGroupsNamespacesResponse":
        """<p>Returns a list of rule groups namespaces in a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace containing the rule groups namespaces.</p>
            name: <p>Use this parameter to filter the rule groups namespaces that are returned. Only the namespaces with names that begin with the value that you specify are returned.</p>
            next_token: <p>The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.</p> <p>For example, if your initial request has <code>maxResults</code> of 10, and there are 12 rule groups namespaces to return, then your initial request will return 10 and a <code>nextToken</code>. Using the next token in a subsequent call will return the remaining 2 namespaces.</p>
            max_results: <p>The maximum number of results to return. The default is 100.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.list_rule_groups_namespaces_request.ListRuleGroupsNamespacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.list_rule_groups_namespaces_response.ListRuleGroupsNamespacesResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_rule_groups_namespaces

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.list_rule_groups_namespaces.async_list_rule_groups_namespaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.list_rule_groups_namespaces_request.ListRuleGroupsNamespacesRequest = {
            "workspace_id": workspace_id
        }
        if name is not None:
            input_["name"] = name
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

    async def iter_list_rule_groups_namespaces(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        name: Optional[
            "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
        ] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_amp.types.rule_groups_namespace_summary.RuleGroupsNamespaceSummary]":
        _token = next_token
        while True:
            _response = await self.list_rule_groups_namespaces(
                workspace_id,
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("rule_groups_namespaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_workspace_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse":
        """<p>Use this operation to return information about the configuration of a workspace. The configuration details returned include workspace configuration status, label set limits, and retention period.</p>

        Args:
            workspace_id: <p>The ID of the workspace that you want to retrieve information for. To find the IDs of your workspaces, use the <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.htm">ListWorkspaces</a> operation.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_workspace_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_workspace_configuration.async_describe_workspace_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest = {
            "workspace_id": workspace_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workspace_configuration(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        limits_per_label_set: Optional[
            "capo_amp.types.limits_per_label_set_list.LimitsPerLabelSetList"
        ] = None,
        retention_period_in_days: Optional[int] = None,
        out_of_order_time_window_in_seconds: Optional[int] = None,
        rule_query_offset_in_seconds: Optional[int] = None,
    ) -> "capo_amp.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse":
        """<p>Use this operation to create or update the label sets, label set limits, and retention period of a workspace.</p> <p>You must specify at least one of <code>limitsPerLabelSet</code> or <code>retentionPeriodInDays</code> for the request to be valid.</p>

        Args:
            workspace_id: <p>The ID of the workspace that you want to update. To find the IDs of your workspaces, use the <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.htm">ListWorkspaces</a> operation.</p>
            client_token: <p>You can include a token in your operation to make it an idempotent opeartion. </p>
            limits_per_label_set: <p>This is an array of structures, where each structure defines a label set for the workspace, and defines the active time series limit for each of those label sets. Each label name in a label set must be unique.</p>
            retention_period_in_days: <p>Specifies how many days that metrics will be retained in the workspace.</p>
            out_of_order_time_window_in_seconds: <p>Specifies the time window in seconds for accepting out of order samples. Out of order samples older than this window are rejected.</p>
            rule_query_offset_in_seconds: <p>Specifies the duration in seconds to offset rule evaluation queries into the past. This allows ingested samples to be available before rule evaluation.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.update_workspace_configuration

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.update_workspace_configuration.async_update_workspace_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest = {
            "workspace_id": workspace_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if limits_per_label_set is not None:
            input_["limits_per_label_set"] = limits_per_label_set
        if retention_period_in_days is not None:
            input_["retention_period_in_days"] = retention_period_in_days
        if out_of_order_time_window_in_seconds is not None:
            input_["out_of_order_time_window_in_seconds"] = (
                out_of_order_time_window_in_seconds
            )
        if rule_query_offset_in_seconds is not None:
            input_["rule_query_offset_in_seconds"] = rule_query_offset_in_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        policy_document: str,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        revision_id: Optional[str] = None,
    ) -> "capo_amp.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates a resource-based policy for an Amazon Managed Service for Prometheus workspace. Use resource-based policies to grant permissions to other AWS accounts or services to access your workspace.</p> <p>Only Prometheus-compatible APIs can be used for workspace sharing. You can add non-Prometheus-compatible APIs to the policy, but they will be ignored. For more information, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-Prometheus-Compatible-Apis.html">Prometheus-compatible APIs</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p> <p>If your workspace uses customer-managed KMS keys for encryption, you must grant the principals in your resource-based policy access to those KMS keys. You can do this by creating KMS grants. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html">CreateGrant</a> in the <i>AWS Key Management Service API Reference</i> and <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html">Encryption at rest</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p> <p>For more information about working with IAM, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/security_iam_service-with-iam.html">Using Amazon Managed Service for Prometheus with IAM</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to attach the resource-based policy to.</p>
            policy_document: <p>The JSON policy document to use as the resource-based policy. This policy defines the permissions that other AWS accounts or services have to access your workspace.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is safe to retry (idempotent).</p>
            revision_id: <p>The revision ID of the policy to update. Use this parameter to ensure that you are updating the correct version of the policy. If you don't specify a revision ID, the policy is updated regardless of its current revision.</p> <p>For the first <b>PUT</b> request on a workspace that doesn't have an existing resource policy, you can specify <code>NO_POLICY</code> as the revision ID.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "workspace_id": workspace_id,
            "policy_document": policy_document,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_resource_policy(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_resource_policy_response.DescribeResourcePolicyResponse":
        """<p>Returns information about the resource-based policy attached to an Amazon Managed Service for Prometheus workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to describe the resource-based policy for.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_resource_policy_request.DescribeResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_resource_policy_response.DescribeResourcePolicyResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_resource_policy

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_resource_policy.async_describe_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.describe_resource_policy_request.DescribeResourcePolicyRequest = {
            "workspace_id": workspace_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        revision_id: Optional[str] = None,
    ) -> None:
        """<p>Deletes the resource-based policy attached to an Amazon Managed Service for Prometheus workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace from which to delete the resource-based policy.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the request is safe to retry (idempotent).</p>
            revision_id: <p>The revision ID of the policy to delete. Use this parameter to ensure that you are deleting the correct version of the policy.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amp.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "workspace_id": workspace_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if revision_id is not None:
            input_["revision_id"] = revision_id

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
