from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_amp._auth._signers
import capo_amp._auth._sigv4
from capo_amp._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_amp.types.create_scraper_request
    import capo_amp.types.create_scraper_response
    import capo_amp.types.delete_scraper_request
    import capo_amp.types.delete_scraper_response
    import capo_amp.types.describe_scraper_request
    import capo_amp.types.describe_scraper_response
    import capo_amp.types.destination
    import capo_amp.types.exporter_list
    import capo_amp.types.idempotency_token
    import capo_amp.types.list_scrapers_request
    import capo_amp.types.list_scrapers_response
    import capo_amp.types.pagination_token
    import capo_amp.types.role_configuration
    import capo_amp.types.scrape_configuration
    import capo_amp.types.scraper_alias
    import capo_amp.types.scraper_filters
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_summary
    import capo_amp.types.source
    import capo_amp.types.tag_map
    import capo_amp.types.update_scraper_request
    import capo_amp.types.update_scraper_response
    from capo_amp._services.amp import ampClient, ampClientConfig
    from capo_amp._services.async_amp import AsyncampClient, AsyncampClientConfig


class Scraper:
    def __init__(self, service: ampClient) -> None:
        self._service = service

    def create(
        self,
        scrape_configuration: "capo_amp.types.scrape_configuration.ScrapeConfiguration",
        source: "capo_amp.types.source.Source",
        destination: "capo_amp.types.destination.Destination",
        *,
        config_overrides: Optional[ampClientConfig] = None,
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

            >>> client.create(alias='alias', scrape_configuration={'configurationBlob': 'blob'}, source={'eksConfiguration': {'clusterArn': 'arn:aws:eks:us-west-2:123456789012:cluster/example', 'securityGroupIds': ['sg-abc123'], 'subnetIds': ['subnet-abc123']}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234'}}, client_token='token', tags={'exampleTag': 'exampleValue'})
            CreateScraper with generic VPC config with mandatory securityGroupIds and subnetIds

            >>> client.create(alias='alias', scrape_configuration={'configurationBlob': 'blob'}, source={'vpcConfiguration': {'securityGroupIds': ['sg-abc123'], 'subnetIds': ['subnet-abc123']}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234'}}, client_token='token', tags={'exampleTag': 'exampleValue'})
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.create_scraper_request.CreateScraperRequest]",
        ) -> OperationResponse[
            "capo_amp.types.create_scraper_response.CreateScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_scraper

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.create_scraper.create_scraper(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[ampClientConfig] = None,
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

            >>> client.read(scraper_id='scraper-123')
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.describe_scraper_request.DescribeScraperRequest]",
        ) -> OperationResponse[
            "capo_amp.types.describe_scraper_response.DescribeScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_scraper

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.describe_scraper.describe_scraper(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.describe_scraper_request.DescribeScraperRequest = {
            "scraper_id": scraper_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[ampClientConfig] = None,
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

            >>> client.update(scraper_id='scraper-123', alias='alias-update', scrape_configuration={'configurationBlob': 'blob-update'}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234-update'}}, client_token='token')
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.update_scraper_request.UpdateScraperRequest]",
        ) -> OperationResponse[
            "capo_amp.types.update_scraper_response.UpdateScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.update_scraper

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.update_scraper.update_scraper(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        scraper_id: "capo_amp.types.scraper_id.ScraperId",
        *,
        config_overrides: Optional[ampClientConfig] = None,
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

            >>> client.delete(scraper_id='scraper-123', client_token='token')
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.delete_scraper_request.DeleteScraperRequest]",
        ) -> OperationResponse[
            "capo_amp.types.delete_scraper_response.DeleteScraperResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.delete_scraper

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.delete_scraper.delete_scraper(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.delete_scraper_request.DeleteScraperRequest = {
            "scraper_id": scraper_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ampClientConfig] = None,
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

            >>> client.list(max_results=2, next_token='previouslyGeneratedToken')
            ListScrapers, with filters

            >>> client.list(filters={'status': ['ACTIVE'], 'sourceArn': ['arn:aws:eks:us-west-2:123456789012:cluster/example1'], 'alias': ['alias1']})
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.list_scrapers_request.ListScrapersRequest]",
        ) -> OperationResponse[
            "capo_amp.types.list_scrapers_response.ListScrapersResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_scrapers

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.list_scrapers.list_scrapers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.list_scrapers_request.ListScrapersRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncScraper:
    def __init__(self, service: AsyncampClient) -> None:
        self._service = service

    async def create(
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

            >>> await client.create(alias='alias', scrape_configuration={'configurationBlob': 'blob'}, source={'eksConfiguration': {'clusterArn': 'arn:aws:eks:us-west-2:123456789012:cluster/example', 'securityGroupIds': ['sg-abc123'], 'subnetIds': ['subnet-abc123']}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234'}}, client_token='token', tags={'exampleTag': 'exampleValue'})
            CreateScraper with generic VPC config with mandatory securityGroupIds and subnetIds

            >>> await client.create(alias='alias', scrape_configuration={'configurationBlob': 'blob'}, source={'vpcConfiguration': {'securityGroupIds': ['sg-abc123'], 'subnetIds': ['subnet-abc123']}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234'}}, client_token='token', tags={'exampleTag': 'exampleValue'})
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def read(
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

            >>> await client.read(scraper_id='scraper-123')
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def update(
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

            >>> await client.update(scraper_id='scraper-123', alias='alias-update', scrape_configuration={'configurationBlob': 'blob-update'}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:aps:us-west-2:123456789012:workspace/ws-ogh2u499-ce12-hg89-v6c7-123412341234-update'}}, client_token='token')
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def delete(
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

            >>> await client.delete(scraper_id='scraper-123', client_token='token')
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def list(
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

            >>> await client.list(max_results=2, next_token='previouslyGeneratedToken')
            ListScrapers, with filters

            >>> await client.list(filters={'status': ['ACTIVE'], 'sourceArn': ['arn:aws:eks:us-west-2:123456789012:cluster/example1'], 'alias': ['alias1']})
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
