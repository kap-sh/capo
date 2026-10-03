"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AmazonElasticsearchService2015``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_elasticsearch_service._auth._signers
import capo_elasticsearch_service._auth._sigv4
from capo_elasticsearch_service._auth._identity import Credentials
from capo_elasticsearch_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_elasticsearch_service._auth._zapros_handler import AuthMiddleware
from capo_elasticsearch_service._pagination import resolve_path as _resolve_path
from capo_elasticsearch_service._services._aws_config import aws_config
from capo_elasticsearch_service._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_request
    import capo_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_response
    import capo_elasticsearch_service.types.add_tags_request
    import capo_elasticsearch_service.types.advanced_options
    import capo_elasticsearch_service.types.advanced_security_options_input
    import capo_elasticsearch_service.types.arn
    import capo_elasticsearch_service.types.associate_package_request
    import capo_elasticsearch_service.types.associate_package_response
    import capo_elasticsearch_service.types.authorize_vpc_endpoint_access_request
    import capo_elasticsearch_service.types.authorize_vpc_endpoint_access_response
    import capo_elasticsearch_service.types.auto_tune_options
    import capo_elasticsearch_service.types.auto_tune_options_input
    import capo_elasticsearch_service.types.automated_snapshot_pause_request_options
    import capo_elasticsearch_service.types.aws_account
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.cancel_domain_config_change_request
    import capo_elasticsearch_service.types.cancel_domain_config_change_response
    import capo_elasticsearch_service.types.cancel_elasticsearch_service_software_update_request
    import capo_elasticsearch_service.types.cancel_elasticsearch_service_software_update_response
    import capo_elasticsearch_service.types.client_token
    import capo_elasticsearch_service.types.cognito_options
    import capo_elasticsearch_service.types.commit_message
    import capo_elasticsearch_service.types.connection_alias
    import capo_elasticsearch_service.types.create_elasticsearch_domain_request
    import capo_elasticsearch_service.types.create_elasticsearch_domain_response
    import capo_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_request
    import capo_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_response
    import capo_elasticsearch_service.types.create_package_request
    import capo_elasticsearch_service.types.create_package_response
    import capo_elasticsearch_service.types.create_vpc_endpoint_request
    import capo_elasticsearch_service.types.create_vpc_endpoint_response
    import capo_elasticsearch_service.types.cross_cluster_search_connection_id
    import capo_elasticsearch_service.types.delete_elasticsearch_domain_request
    import capo_elasticsearch_service.types.delete_elasticsearch_domain_response
    import capo_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_request
    import capo_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_response
    import capo_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_request
    import capo_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_response
    import capo_elasticsearch_service.types.delete_package_request
    import capo_elasticsearch_service.types.delete_package_response
    import capo_elasticsearch_service.types.delete_vpc_endpoint_request
    import capo_elasticsearch_service.types.delete_vpc_endpoint_response
    import capo_elasticsearch_service.types.deployment_strategy_options
    import capo_elasticsearch_service.types.describe_domain_auto_tunes_request
    import capo_elasticsearch_service.types.describe_domain_auto_tunes_response
    import capo_elasticsearch_service.types.describe_domain_change_progress_request
    import capo_elasticsearch_service.types.describe_domain_change_progress_response
    import capo_elasticsearch_service.types.describe_elasticsearch_domain_config_request
    import capo_elasticsearch_service.types.describe_elasticsearch_domain_config_response
    import capo_elasticsearch_service.types.describe_elasticsearch_domain_request
    import capo_elasticsearch_service.types.describe_elasticsearch_domain_response
    import capo_elasticsearch_service.types.describe_elasticsearch_domains_request
    import capo_elasticsearch_service.types.describe_elasticsearch_domains_response
    import capo_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_request
    import capo_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_response
    import capo_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_request
    import capo_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_response
    import capo_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_request
    import capo_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_response
    import capo_elasticsearch_service.types.describe_packages_filter_list
    import capo_elasticsearch_service.types.describe_packages_request
    import capo_elasticsearch_service.types.describe_packages_response
    import capo_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_request
    import capo_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_response
    import capo_elasticsearch_service.types.describe_reserved_elasticsearch_instances_request
    import capo_elasticsearch_service.types.describe_reserved_elasticsearch_instances_response
    import capo_elasticsearch_service.types.describe_vpc_endpoints_request
    import capo_elasticsearch_service.types.describe_vpc_endpoints_response
    import capo_elasticsearch_service.types.dissociate_package_request
    import capo_elasticsearch_service.types.dissociate_package_response
    import capo_elasticsearch_service.types.domain_arn
    import capo_elasticsearch_service.types.domain_endpoint_options
    import capo_elasticsearch_service.types.domain_engine_mode
    import capo_elasticsearch_service.types.domain_information
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.domain_name_list
    import capo_elasticsearch_service.types.domain_use_case
    import capo_elasticsearch_service.types.dry_run
    import capo_elasticsearch_service.types.ebs_options
    import capo_elasticsearch_service.types.elasticsearch_cluster_config
    import capo_elasticsearch_service.types.elasticsearch_version_string
    import capo_elasticsearch_service.types.encryption_at_rest_options
    import capo_elasticsearch_service.types.engine_type
    import capo_elasticsearch_service.types.es_partition_instance_type
    import capo_elasticsearch_service.types.filter_list
    import capo_elasticsearch_service.types.get_compatible_elasticsearch_versions_request
    import capo_elasticsearch_service.types.get_compatible_elasticsearch_versions_response
    import capo_elasticsearch_service.types.get_package_version_history_request
    import capo_elasticsearch_service.types.get_package_version_history_response
    import capo_elasticsearch_service.types.get_upgrade_history_request
    import capo_elasticsearch_service.types.get_upgrade_history_response
    import capo_elasticsearch_service.types.get_upgrade_status_request
    import capo_elasticsearch_service.types.get_upgrade_status_response
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.instance_count
    import capo_elasticsearch_service.types.list_domain_names_request
    import capo_elasticsearch_service.types.list_domain_names_response
    import capo_elasticsearch_service.types.list_domains_for_package_request
    import capo_elasticsearch_service.types.list_domains_for_package_response
    import capo_elasticsearch_service.types.list_elasticsearch_instance_types_request
    import capo_elasticsearch_service.types.list_elasticsearch_instance_types_response
    import capo_elasticsearch_service.types.list_elasticsearch_versions_request
    import capo_elasticsearch_service.types.list_elasticsearch_versions_response
    import capo_elasticsearch_service.types.list_packages_for_domain_request
    import capo_elasticsearch_service.types.list_packages_for_domain_response
    import capo_elasticsearch_service.types.list_tags_request
    import capo_elasticsearch_service.types.list_tags_response
    import capo_elasticsearch_service.types.list_vpc_endpoint_access_request
    import capo_elasticsearch_service.types.list_vpc_endpoint_access_response
    import capo_elasticsearch_service.types.list_vpc_endpoints_for_domain_request
    import capo_elasticsearch_service.types.list_vpc_endpoints_for_domain_response
    import capo_elasticsearch_service.types.list_vpc_endpoints_request
    import capo_elasticsearch_service.types.list_vpc_endpoints_response
    import capo_elasticsearch_service.types.log_publishing_options
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token
    import capo_elasticsearch_service.types.node_to_node_encryption_options
    import capo_elasticsearch_service.types.package_description
    import capo_elasticsearch_service.types.package_id
    import capo_elasticsearch_service.types.package_name
    import capo_elasticsearch_service.types.package_source
    import capo_elasticsearch_service.types.package_type
    import capo_elasticsearch_service.types.policy_document
    import capo_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_request
    import capo_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_response
    import capo_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_request
    import capo_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_response
    import capo_elasticsearch_service.types.remove_tags_request
    import capo_elasticsearch_service.types.reservation_token
    import capo_elasticsearch_service.types.revoke_vpc_endpoint_access_request
    import capo_elasticsearch_service.types.revoke_vpc_endpoint_access_response
    import capo_elasticsearch_service.types.snapshot_options
    import capo_elasticsearch_service.types.start_elasticsearch_service_software_update_request
    import capo_elasticsearch_service.types.start_elasticsearch_service_software_update_response
    import capo_elasticsearch_service.types.string_list
    import capo_elasticsearch_service.types.tag_list
    import capo_elasticsearch_service.types.update_elasticsearch_domain_config_request
    import capo_elasticsearch_service.types.update_elasticsearch_domain_config_response
    import capo_elasticsearch_service.types.update_package_request
    import capo_elasticsearch_service.types.update_package_response
    import capo_elasticsearch_service.types.update_vpc_endpoint_request
    import capo_elasticsearch_service.types.update_vpc_endpoint_response
    import capo_elasticsearch_service.types.upgrade_elasticsearch_domain_request
    import capo_elasticsearch_service.types.upgrade_elasticsearch_domain_response
    import capo_elasticsearch_service.types.vpc_endpoint_id
    import capo_elasticsearch_service.types.vpc_endpoint_id_list
    import capo_elasticsearch_service.types.vpc_options


class ElasticsearchServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ElasticsearchServiceClient:
    """A client for the ``ElasticsearchService`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = ElasticsearchServiceClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[ElasticsearchServiceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ElasticsearchServiceClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def accept_inbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "capo_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_response.AcceptInboundCrossClusterSearchConnectionResponse":
        """<p>Allows the destination domain owner to accept an inbound cross-cluster search connection request.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the inbound connection that you want to accept.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_request.AcceptInboundCrossClusterSearchConnectionRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_response.AcceptInboundCrossClusterSearchConnectionResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.accept_inbound_cross_cluster_search_connection

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.accept_inbound_cross_cluster_search_connection.accept_inbound_cross_cluster_search_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_request.AcceptInboundCrossClusterSearchConnectionRequest = {
            "cross_cluster_search_connection_id": cross_cluster_search_connection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_tags(
        self,
        arn: "capo_elasticsearch_service.types.arn.ARN",
        tag_list: "capo_elasticsearch_service.types.tag_list.TagList",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> None:
        """<p>Attaches tags to an existing Elasticsearch domain. Tags are a set of case-sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-awsresorcetagging" target="_blank"> Tagging Amazon Elasticsearch Service Domains for more information.</a></p>

        Args:
            arn: <p> Specify the <code>ARN</code> for which you want to add the tags.</p>
            tag_list: <p> List of <code>Tag</code> that need to be added for the Elasticsearch domain. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.add_tags_request.AddTagsRequest]",
        ) -> OperationResponse[None]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.add_tags

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.add_tags.add_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.add_tags_request.AddTagsRequest = {
            "arn": arn,
            "tag_list": tag_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_package(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.associate_package_response.AssociatePackageResponse":
        """<p>Associates a package with an Amazon ES domain.</p>

        Args:
            package_id: <p>Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.</p>
            domain_name: <p>Name of the domain that you want to associate the package with.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use. Returns HTTP status code 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.associate_package_request.AssociatePackageRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.associate_package_response.AssociatePackageResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.associate_package

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.associate_package.associate_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.associate_package_request.AssociatePackageRequest = {
            "package_id": package_id,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def authorize_vpc_endpoint_access(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        account: "capo_elasticsearch_service.types.aws_account.AWSAccount",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse":
        """<p>Provides access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to provide access to.</p>
            account: <p>The account ID to grant access to.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.authorize_vpc_endpoint_access

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.authorize_vpc_endpoint_access.authorize_vpc_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest = {
            "domain_name": domain_name,
            "account": account,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_domain_config_change(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        dry_run: Optional["capo_elasticsearch_service.types.dry_run.DryRun"] = None,
    ) -> "capo_elasticsearch_service.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse":
        """<p>Cancels a pending configuration change on an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain configuration request to cancel.</p>
            dry_run: <p>When set to <b>True</b>, returns the list of change IDs and properties that will be cancelled without actually cancelling the change.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_domain_config_change

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_domain_config_change.cancel_domain_config_change(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest = {
            "domain_name": domain_name
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_elasticsearch_service_software_update(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.cancel_elasticsearch_service_software_update_response.CancelElasticsearchServiceSoftwareUpdateResponse":
        """<p>Cancels a scheduled service software update for an Amazon ES domain. You can only perform this operation before the <code>AutomatedUpdateDate</code> and when the <code>UpdateStatus</code> is in the <code>PENDING_UPDATE</code> state.</p>

        Args:
            domain_name: <p>The name of the domain that you want to stop the latest service software update on.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.cancel_elasticsearch_service_software_update_request.CancelElasticsearchServiceSoftwareUpdateRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.cancel_elasticsearch_service_software_update_response.CancelElasticsearchServiceSoftwareUpdateResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_elasticsearch_service_software_update

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_elasticsearch_service_software_update.cancel_elasticsearch_service_software_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.cancel_elasticsearch_service_software_update_request.CancelElasticsearchServiceSoftwareUpdateRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_elasticsearch_domain(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        elasticsearch_version: Optional[
            "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
        ] = None,
        elasticsearch_cluster_config: Optional[
            "capo_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
        ] = None,
        ebs_options: Optional[
            "capo_elasticsearch_service.types.ebs_options.EBSOptions"
        ] = None,
        access_policies: Optional[
            "capo_elasticsearch_service.types.policy_document.PolicyDocument"
        ] = None,
        snapshot_options: Optional[
            "capo_elasticsearch_service.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional[
            "capo_elasticsearch_service.types.vpc_options.VPCOptions"
        ] = None,
        cognito_options: Optional[
            "capo_elasticsearch_service.types.cognito_options.CognitoOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "capo_elasticsearch_service.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        node_to_node_encryption_options: Optional[
            "capo_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        advanced_options: Optional[
            "capo_elasticsearch_service.types.advanced_options.AdvancedOptions"
        ] = None,
        log_publishing_options: Optional[
            "capo_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "capo_elasticsearch_service.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        advanced_security_options: Optional[
            "capo_elasticsearch_service.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        auto_tune_options: Optional[
            "capo_elasticsearch_service.types.auto_tune_options_input.AutoTuneOptionsInput"
        ] = None,
        tag_list: Optional["capo_elasticsearch_service.types.tag_list.TagList"] = None,
        deployment_strategy_options: Optional[
            "capo_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "capo_elasticsearch_service.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
        use_case: Optional[
            "capo_elasticsearch_service.types.domain_use_case.DomainUseCase"
        ] = None,
        engine_mode: Optional[
            "capo_elasticsearch_service.types.domain_engine_mode.DomainEngineMode"
        ] = None,
    ) -> "capo_elasticsearch_service.types.create_elasticsearch_domain_response.CreateElasticsearchDomainResponse":
        """<p>Creates a new Elasticsearch domain. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains" target="_blank">Creating Elasticsearch Domains</a> in the <i>Amazon Elasticsearch Service Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain that you are creating. Domain names are unique across the domains owned by an account within an AWS region. Domain names must start with a lowercase letter and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).</p>
            elasticsearch_version: <p>String of format X.Y to specify version for the Elasticsearch domain eg. "1.5" or "2.3". For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains" target="_blank">Creating Elasticsearch Domains</a> in the <i>Amazon Elasticsearch Service Developer Guide</i>.</p>
            elasticsearch_cluster_config: <p>Configuration options for an Elasticsearch domain. Specifies the instance type and number of instances in the domain cluster. </p>
            ebs_options: <p>Options to enable, disable and specify the type and size of EBS storage volumes. </p>
            access_policies: <p> IAM access policy as a JSON-formatted string.</p>
            snapshot_options: <p>Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours. </p>
            vpc_options: <p>Options to specify the subnets and security groups for VPC endpoint. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc" target="_blank">Creating a VPC</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i></p>
            cognito_options: <p>Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html" target="_blank">Amazon Cognito Authentication for Kibana</a>.</p>
            encryption_at_rest_options: <p>Specifies the Encryption At Rest Options.</p>
            node_to_node_encryption_options: <p>Specifies the NodeToNodeEncryptionOptions.</p>
            advanced_options: <p> Option to allow references to indices in an HTTP request body. Must be <code>false</code> when configuring access to individual sub-resources. By default, the value is <code>true</code>. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options" target="_blank">Configuration Advanced Options</a> for more information.</p>
            log_publishing_options: <p>Map of <code>LogType</code> and <code>LogPublishingOption</code>, each containing options to publish a given type of Elasticsearch log.</p>
            domain_endpoint_options: <p>Options to specify configuration that will be applied to the domain endpoint.</p>
            advanced_security_options: <p>Specifies advanced security options.</p>
            auto_tune_options: <p>Specifies Auto-Tune options.</p>
            tag_list: <p>A list of <code>Tag</code> added during domain creation.</p>
            deployment_strategy_options: <p>Specifies the deployment strategy options.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
            use_case: <p>The primary use case for the domain. For valid values, see <code>DomainUseCase</code>.</p>
            engine_mode: <p>The engine mode for the domain. For valid values and requirements, see <code>DomainEngineMode</code>.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access sub-resource that is either invalid or not supported. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.create_elasticsearch_domain_request.CreateElasticsearchDomainRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.create_elasticsearch_domain_response.CreateElasticsearchDomainResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_elasticsearch_domain

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_elasticsearch_domain.create_elasticsearch_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.create_elasticsearch_domain_request.CreateElasticsearchDomainRequest = {
            "domain_name": domain_name
        }
        if elasticsearch_version is not None:
            input_["elasticsearch_version"] = elasticsearch_version
        if elasticsearch_cluster_config is not None:
            input_["elasticsearch_cluster_config"] = elasticsearch_cluster_config
        if ebs_options is not None:
            input_["ebs_options"] = ebs_options
        if access_policies is not None:
            input_["access_policies"] = access_policies
        if snapshot_options is not None:
            input_["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if cognito_options is not None:
            input_["cognito_options"] = cognito_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if node_to_node_encryption_options is not None:
            input_["node_to_node_encryption_options"] = node_to_node_encryption_options
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if domain_endpoint_options is not None:
            input_["domain_endpoint_options"] = domain_endpoint_options
        if advanced_security_options is not None:
            input_["advanced_security_options"] = advanced_security_options
        if auto_tune_options is not None:
            input_["auto_tune_options"] = auto_tune_options
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if deployment_strategy_options is not None:
            input_["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input_["automated_snapshot_pause_options"] = (
                automated_snapshot_pause_options
            )
        if use_case is not None:
            input_["use_case"] = use_case
        if engine_mode is not None:
            input_["engine_mode"] = engine_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_outbound_cross_cluster_search_connection(
        self,
        source_domain_info: "capo_elasticsearch_service.types.domain_information.DomainInformation",
        destination_domain_info: "capo_elasticsearch_service.types.domain_information.DomainInformation",
        connection_alias: "capo_elasticsearch_service.types.connection_alias.ConnectionAlias",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_response.CreateOutboundCrossClusterSearchConnectionResponse":
        """<p>Creates a new cross-cluster search connection from a source domain to a destination domain.</p>

        Args:
            source_domain_info: <p>Specifies the <code><a>DomainInformation</a></code> for the source Elasticsearch domain.</p>
            destination_domain_info: <p>Specifies the <code><a>DomainInformation</a></code> for the destination Elasticsearch domain.</p>
            connection_alias: <p>Specifies the connection alias that will be used by the customer for this connection.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_request.CreateOutboundCrossClusterSearchConnectionRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_response.CreateOutboundCrossClusterSearchConnectionResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_outbound_cross_cluster_search_connection

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_outbound_cross_cluster_search_connection.create_outbound_cross_cluster_search_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_request.CreateOutboundCrossClusterSearchConnectionRequest = {
            "source_domain_info": source_domain_info,
            "destination_domain_info": destination_domain_info,
            "connection_alias": connection_alias,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_package(
        self,
        package_name: "capo_elasticsearch_service.types.package_name.PackageName",
        package_type: "capo_elasticsearch_service.types.package_type.PackageType",
        package_source: "capo_elasticsearch_service.types.package_source.PackageSource",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        package_description: Optional[
            "capo_elasticsearch_service.types.package_description.PackageDescription"
        ] = None,
    ) -> (
        "capo_elasticsearch_service.types.create_package_response.CreatePackageResponse"
    ):
        """<p>Create a package for use with Amazon ES domains.</p>

        Args:
            package_name: <p>Unique identifier for the package.</p>
            package_type: <p>Type of package. Currently supports only TXT-DICTIONARY.</p>
            package_description: <p>Description of the package.</p>
            package_source: <p>The customer S3 location <code>PackageSource</code> for importing the package.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access sub-resource that is either invalid or not supported. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.create_package_request.CreatePackageRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.create_package_response.CreatePackageResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_package

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_package.create_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.create_package_request.CreatePackageRequest = {
            "package_name": package_name,
            "package_type": package_type,
            "package_source": package_source,
        }
        if package_description is not None:
            input_["package_description"] = package_description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_endpoint(
        self,
        domain_arn: "capo_elasticsearch_service.types.domain_arn.DomainArn",
        vpc_options: "capo_elasticsearch_service.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        client_token: Optional[
            "capo_elasticsearch_service.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an Amazon OpenSearch Service-managed VPC endpoint.</p>

        Args:
            domain_arn: <p>The Amazon Resource Name (ARN) of the domain to grant access to.</p>
            vpc_options: <p>Options to specify the subnets and security groups for the endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use. Returns HTTP status code 409.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_vpc_endpoint

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_vpc_endpoint.create_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {
            "domain_arn": domain_arn,
            "vpc_options": vpc_options,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_elasticsearch_domain(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.delete_elasticsearch_domain_response.DeleteElasticsearchDomainResponse":
        """<p>Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.</p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain that you want to permanently delete.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.delete_elasticsearch_domain_request.DeleteElasticsearchDomainRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.delete_elasticsearch_domain_response.DeleteElasticsearchDomainResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_domain

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_domain.delete_elasticsearch_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.delete_elasticsearch_domain_request.DeleteElasticsearchDomainRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_elasticsearch_service_role(
        self, *, config_overrides: Optional[ElasticsearchServiceClientConfig] = None
    ) -> None:
        """<p>Deletes the service-linked role that Elasticsearch Service uses to manage and maintain VPC domains. Role deletion will fail if any existing VPC domains use the role. You must delete any such Elasticsearch domains before deleting the role. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-enabling-slr" target="_blank">Deleting Elasticsearch Service Role</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i>.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(req: "OperationRequest[None]") -> OperationResponse[None]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_service_role

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_service_role.delete_elasticsearch_service_role(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_inbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "capo_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_response.DeleteInboundCrossClusterSearchConnectionResponse":
        """<p>Allows the destination domain owner to delete an existing inbound cross-cluster search connection.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the inbound connection that you want to permanently delete.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_request.DeleteInboundCrossClusterSearchConnectionRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_response.DeleteInboundCrossClusterSearchConnectionResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_inbound_cross_cluster_search_connection

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_inbound_cross_cluster_search_connection.delete_inbound_cross_cluster_search_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_request.DeleteInboundCrossClusterSearchConnectionRequest = {
            "cross_cluster_search_connection_id": cross_cluster_search_connection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_outbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "capo_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_response.DeleteOutboundCrossClusterSearchConnectionResponse":
        """<p>Allows the source domain owner to delete an existing outbound cross-cluster search connection.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the outbound connection that you want to permanently delete.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_request.DeleteOutboundCrossClusterSearchConnectionRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_response.DeleteOutboundCrossClusterSearchConnectionResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_outbound_cross_cluster_search_connection

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_outbound_cross_cluster_search_connection.delete_outbound_cross_cluster_search_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_request.DeleteOutboundCrossClusterSearchConnectionRequest = {
            "cross_cluster_search_connection_id": cross_cluster_search_connection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_package(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> (
        "capo_elasticsearch_service.types.delete_package_response.DeletePackageResponse"
    ):
        """<p>Delete the package.</p>

        Args:
            package_id: <p>Internal ID of the package that you want to delete. Use <code>DescribePackages</code> to find this value.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use. Returns HTTP status code 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.delete_package_request.DeletePackageRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.delete_package_response.DeletePackageResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_package

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_package.delete_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.delete_package_request.DeletePackageRequest = {
            "package_id": package_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_endpoint(
        self,
        vpc_endpoint_id: "capo_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>The unique identifier of the endpoint to be deleted.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_vpc_endpoint

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_vpc_endpoint.delete_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {
            "vpc_endpoint_id": vpc_endpoint_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_domain_auto_tunes(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse":
        """<p>Provides scheduled Auto-Tune action details for the Elasticsearch domain, such as Auto-Tune action type, description, severity, and scheduled date.</p>

        Args:
            domain_name: <p>Specifies the domain name for which you want Auto-Tune action details.</p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p>NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_auto_tunes

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_auto_tunes.describe_domain_auto_tunes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_domain_auto_tunes(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse]":
        _token = next_token
        while True:
            _response = self.describe_domain_auto_tunes(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_domain_change_progress(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        change_id: Optional["capo_elasticsearch_service.types.guid.GUID"] = None,
    ) -> "capo_elasticsearch_service.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse":
        """<p>Returns information about the current blue/green deployment happening on a domain, including a change ID, status, and progress stages.</p>

        Args:
            domain_name: <p>The domain you want to get the progress information about.</p>
            change_id: <p>The specific change ID for which you want to get progress information. This is an optional parameter. If omitted, the service returns information about the most recent configuration change. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_change_progress

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_change_progress.describe_domain_change_progress(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest = {
            "domain_name": domain_name
        }
        if change_id is not None:
            input_["change_id"] = change_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_elasticsearch_domain(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.describe_elasticsearch_domain_response.DescribeElasticsearchDomainResponse":
        """<p>Returns domain configuration information about the specified Elasticsearch domain, including the domain ID, domain endpoint, and domain ARN.</p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain for which you want information.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_elasticsearch_domain_request.DescribeElasticsearchDomainRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_elasticsearch_domain_response.DescribeElasticsearchDomainResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain.describe_elasticsearch_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_elasticsearch_domain_request.DescribeElasticsearchDomainRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_elasticsearch_domain_config(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.describe_elasticsearch_domain_config_response.DescribeElasticsearchDomainConfigResponse":
        """<p>Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.</p>

        Args:
            domain_name: <p>The Elasticsearch domain that you want to get information about.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_elasticsearch_domain_config_request.DescribeElasticsearchDomainConfigRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_elasticsearch_domain_config_response.DescribeElasticsearchDomainConfigResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain_config

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain_config.describe_elasticsearch_domain_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_elasticsearch_domain_config_request.DescribeElasticsearchDomainConfigRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_elasticsearch_domains(
        self,
        domain_names: "capo_elasticsearch_service.types.domain_name_list.DomainNameList",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.describe_elasticsearch_domains_response.DescribeElasticsearchDomainsResponse":
        """<p>Returns domain configuration information about the specified Elasticsearch domains, including the domain ID, domain endpoint, and domain ARN.</p>

        Args:
            domain_names: <p>The Elasticsearch domains for which you want information.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_elasticsearch_domains_request.DescribeElasticsearchDomainsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_elasticsearch_domains_response.DescribeElasticsearchDomainsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domains

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domains.describe_elasticsearch_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_elasticsearch_domains_request.DescribeElasticsearchDomainsRequest = {
            "domain_names": domain_names
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_elasticsearch_instance_type_limits(
        self,
        instance_type: "capo_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType",
        elasticsearch_version: "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        domain_name: Optional[
            "capo_elasticsearch_service.types.domain_name.DomainName"
        ] = None,
    ) -> "capo_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_response.DescribeElasticsearchInstanceTypeLimitsResponse":
        """<p> Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the <code> <a>DomainName</a> </code> to know what Limits are supported for modifying. </p>

        Args:
            domain_name: <p> DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch <code> <a>Limits</a> </code> for existing domain. </p>
            instance_type: <p> The instance type for an Elasticsearch cluster for which Elasticsearch <code> <a>Limits</a> </code> are needed. </p>
            elasticsearch_version: <p> Version of Elasticsearch for which <code> <a>Limits</a> </code> are needed. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access sub-resource that is either invalid or not supported. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_request.DescribeElasticsearchInstanceTypeLimitsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_response.DescribeElasticsearchInstanceTypeLimitsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_instance_type_limits

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_instance_type_limits.describe_elasticsearch_instance_type_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_request.DescribeElasticsearchInstanceTypeLimitsRequest = {
            "instance_type": instance_type,
            "elasticsearch_version": elasticsearch_version,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_inbound_cross_cluster_search_connections(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "capo_elasticsearch_service.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_response.DescribeInboundCrossClusterSearchConnectionsResponse":
        """<p>Lists all the inbound cross-cluster search connections for a destination domain.</p>

        Args:
            filters: <p> A list of filters used to match properties for inbound cross-cluster search connection. Available <code><a>Filter</a></code> names for this operation are: <ul> <li>cross-cluster-search-connection-id</li> <li>source-domain-info.domain-name</li> <li>source-domain-info.owner-id</li> <li>source-domain-info.region</li> <li>destination-domain-info.domain-name</li> </ul> </p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p> NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>The request processing has failed because of invalid pagination token provided by customer. Returns an HTTP status code of 400. </p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_request.DescribeInboundCrossClusterSearchConnectionsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_response.DescribeInboundCrossClusterSearchConnectionsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_inbound_cross_cluster_search_connections

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_inbound_cross_cluster_search_connections.describe_inbound_cross_cluster_search_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_request.DescribeInboundCrossClusterSearchConnectionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_inbound_cross_cluster_search_connections(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "capo_elasticsearch_service.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_response.DescribeInboundCrossClusterSearchConnectionsResponse]":
        _token = next_token
        while True:
            _response = self.describe_inbound_cross_cluster_search_connections(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_outbound_cross_cluster_search_connections(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "capo_elasticsearch_service.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_response.DescribeOutboundCrossClusterSearchConnectionsResponse":
        """<p>Lists all the outbound cross-cluster search connections for a source domain.</p>

        Args:
            filters: <p> A list of filters used to match properties for outbound cross-cluster search connection. Available <code><a>Filter</a></code> names for this operation are: <ul> <li>cross-cluster-search-connection-id</li> <li>destination-domain-info.domain-name</li> <li>destination-domain-info.owner-id</li> <li>destination-domain-info.region</li> <li>source-domain-info.domain-name</li> </ul> </p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p> NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.invalid_pagination_token_exception.InvalidPaginationTokenException: <p>The request processing has failed because of invalid pagination token provided by customer. Returns an HTTP status code of 400. </p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_request.DescribeOutboundCrossClusterSearchConnectionsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_response.DescribeOutboundCrossClusterSearchConnectionsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_outbound_cross_cluster_search_connections

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_outbound_cross_cluster_search_connections.describe_outbound_cross_cluster_search_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_request.DescribeOutboundCrossClusterSearchConnectionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_outbound_cross_cluster_search_connections(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "capo_elasticsearch_service.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_response.DescribeOutboundCrossClusterSearchConnectionsResponse]":
        _token = next_token
        while True:
            _response = self.describe_outbound_cross_cluster_search_connections(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_packages(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "capo_elasticsearch_service.types.describe_packages_filter_list.DescribePackagesFilterList"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.describe_packages_response.DescribePackagesResponse":
        """<p>Describes all packages available to Amazon ES. Includes options for filtering, limiting the number of results, and pagination.</p>

        Args:
            filters: <p>Only returns packages that match the <code>DescribePackagesFilterList</code> values.</p>
            max_results: <p>Limits results to a maximum number of packages.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_packages_request.DescribePackagesRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_packages_response.DescribePackagesResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_packages

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_packages.describe_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_packages_request.DescribePackagesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_packages(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "capo_elasticsearch_service.types.describe_packages_filter_list.DescribePackagesFilterList"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.describe_packages_response.DescribePackagesResponse]":
        _token = next_token
        while True:
            _response = self.describe_packages(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_reserved_elasticsearch_instance_offerings(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        reserved_elasticsearch_instance_offering_id: Optional[
            "capo_elasticsearch_service.types.guid.GUID"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_response.DescribeReservedElasticsearchInstanceOfferingsResponse":
        """<p>Lists available reserved Elasticsearch instance offerings.</p>

        Args:
            reserved_elasticsearch_instance_offering_id: <p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_request.DescribeReservedElasticsearchInstanceOfferingsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_response.DescribeReservedElasticsearchInstanceOfferingsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instance_offerings

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instance_offerings.describe_reserved_elasticsearch_instance_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_request.DescribeReservedElasticsearchInstanceOfferingsRequest = {}
        if reserved_elasticsearch_instance_offering_id is not None:
            input_["reserved_elasticsearch_instance_offering_id"] = (
                reserved_elasticsearch_instance_offering_id
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_reserved_elasticsearch_instance_offerings(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        reserved_elasticsearch_instance_offering_id: Optional[
            "capo_elasticsearch_service.types.guid.GUID"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_response.DescribeReservedElasticsearchInstanceOfferingsResponse]":
        _token = next_token
        while True:
            _response = self.describe_reserved_elasticsearch_instance_offerings(
                config_overrides=config_overrides,
                reserved_elasticsearch_instance_offering_id=reserved_elasticsearch_instance_offering_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_reserved_elasticsearch_instances(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        reserved_elasticsearch_instance_id: Optional[
            "capo_elasticsearch_service.types.guid.GUID"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.describe_reserved_elasticsearch_instances_response.DescribeReservedElasticsearchInstancesResponse":
        """<p>Returns information about reserved Elasticsearch instances for this account.</p>

        Args:
            reserved_elasticsearch_instance_id: <p>The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID.</p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_reserved_elasticsearch_instances_request.DescribeReservedElasticsearchInstancesRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_reserved_elasticsearch_instances_response.DescribeReservedElasticsearchInstancesResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instances

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instances.describe_reserved_elasticsearch_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_reserved_elasticsearch_instances_request.DescribeReservedElasticsearchInstancesRequest = {}
        if reserved_elasticsearch_instance_id is not None:
            input_["reserved_elasticsearch_instance_id"] = (
                reserved_elasticsearch_instance_id
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_reserved_elasticsearch_instances(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        reserved_elasticsearch_instance_id: Optional[
            "capo_elasticsearch_service.types.guid.GUID"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.describe_reserved_elasticsearch_instances_response.DescribeReservedElasticsearchInstancesResponse]":
        _token = next_token
        while True:
            _response = self.describe_reserved_elasticsearch_instances(
                config_overrides=config_overrides,
                reserved_elasticsearch_instance_id=reserved_elasticsearch_instance_id,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_vpc_endpoints(
        self,
        vpc_endpoint_ids: "capo_elasticsearch_service.types.vpc_endpoint_id_list.VpcEndpointIdList",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse":
        """<p>Describes one or more Amazon OpenSearch Service-managed VPC endpoints.</p>

        Args:
            vpc_endpoint_ids: <p>The unique identifiers of the endpoints to get information about.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_vpc_endpoints

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_vpc_endpoints.describe_vpc_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest = {
            "vpc_endpoint_ids": vpc_endpoint_ids
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def dissociate_package(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.dissociate_package_response.DissociatePackageResponse":
        """<p>Dissociates a package from the Amazon ES domain.</p>

        Args:
            package_id: <p>Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.</p>
            domain_name: <p>Name of the domain that you want to associate the package with.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use. Returns HTTP status code 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.dissociate_package_request.DissociatePackageRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.dissociate_package_response.DissociatePackageResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.dissociate_package

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.dissociate_package.dissociate_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.dissociate_package_request.DissociatePackageRequest = {
            "package_id": package_id,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compatible_elasticsearch_versions(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        domain_name: Optional[
            "capo_elasticsearch_service.types.domain_name.DomainName"
        ] = None,
    ) -> "capo_elasticsearch_service.types.get_compatible_elasticsearch_versions_response.GetCompatibleElasticsearchVersionsResponse":
        """<p> Returns a list of upgrade compatible Elastisearch versions. You can optionally pass a <code> <a>DomainName</a> </code> to get all upgrade compatible Elasticsearch versions for that specific domain. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.get_compatible_elasticsearch_versions_request.GetCompatibleElasticsearchVersionsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.get_compatible_elasticsearch_versions_response.GetCompatibleElasticsearchVersionsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_compatible_elasticsearch_versions

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_compatible_elasticsearch_versions.get_compatible_elasticsearch_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.get_compatible_elasticsearch_versions_request.GetCompatibleElasticsearchVersionsRequest = {}
        if domain_name is not None:
            input_["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_package_version_history(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.get_package_version_history_response.GetPackageVersionHistoryResponse":
        """<p>Returns a list of versions of the package, along with their creation time and commit message.</p>

        Args:
            package_id: <p>Returns an audit history of versions of the package.</p>
            max_results: <p>Limits results to a maximum number of versions.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.get_package_version_history_request.GetPackageVersionHistoryRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.get_package_version_history_response.GetPackageVersionHistoryResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_package_version_history

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_package_version_history.get_package_version_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.get_package_version_history_request.GetPackageVersionHistoryRequest = {
            "package_id": package_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_package_version_history(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.get_package_version_history_response.GetPackageVersionHistoryResponse]":
        _token = next_token
        while True:
            _response = self.get_package_version_history(
                package_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_upgrade_history(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.get_upgrade_history_response.GetUpgradeHistoryResponse":
        """<p>Retrieves the complete history of the last 10 upgrades that were performed on the domain.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.get_upgrade_history_request.GetUpgradeHistoryRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.get_upgrade_history_response.GetUpgradeHistoryResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_history

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_history.get_upgrade_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.get_upgrade_history_request.GetUpgradeHistoryRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_upgrade_history(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.get_upgrade_history_response.GetUpgradeHistoryResponse]":
        _token = next_token
        while True:
            _response = self.get_upgrade_history(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_upgrade_status(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.get_upgrade_status_response.GetUpgradeStatusResponse":
        """<p>Retrieves the latest status of the last upgrade or upgrade eligibility check that was performed on the domain.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.get_upgrade_status_request.GetUpgradeStatusRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.get_upgrade_status_response.GetUpgradeStatusResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_status

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_status.get_upgrade_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.get_upgrade_status_request.GetUpgradeStatusRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_domain_names(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        engine_type: Optional[
            "capo_elasticsearch_service.types.engine_type.EngineType"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_domain_names_response.ListDomainNamesResponse":
        """<p>Returns the name of all Elasticsearch domains owned by the current user's account. </p>

        Args:
            engine_type: <p> Optional parameter to filter the output by domain engine type. Acceptable values are 'Elasticsearch' and 'OpenSearch'. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_domain_names_request.ListDomainNamesRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_domain_names_response.ListDomainNamesResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domain_names

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domain_names.list_domain_names(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_domain_names_request.ListDomainNamesRequest = {}
        if engine_type is not None:
            input_["engine_type"] = engine_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_domains_for_package(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_domains_for_package_response.ListDomainsForPackageResponse":
        """<p>Lists all Amazon ES domains associated with the package.</p>

        Args:
            package_id: <p>The package for which to list domains.</p>
            max_results: <p>Limits results to a maximum number of domains.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_domains_for_package_request.ListDomainsForPackageRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_domains_for_package_response.ListDomainsForPackageResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domains_for_package

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domains_for_package.list_domains_for_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_domains_for_package_request.ListDomainsForPackageRequest = {
            "package_id": package_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_domains_for_package(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.list_domains_for_package_response.ListDomainsForPackageResponse]":
        _token = next_token
        while True:
            _response = self.list_domains_for_package(
                package_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_elasticsearch_instance_types(
        self,
        elasticsearch_version: "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        domain_name: Optional[
            "capo_elasticsearch_service.types.domain_name.DomainName"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_elasticsearch_instance_types_response.ListElasticsearchInstanceTypesResponse":
        """<p>List all Elasticsearch instance types that are supported for given ElasticsearchVersion</p>

        Args:
            elasticsearch_version: <p>Version of Elasticsearch for which list of supported elasticsearch instance types are needed. </p>
            domain_name: <p>DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain. </p>
            max_results: <p> Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored. </p>
            next_token: <p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_elasticsearch_instance_types_request.ListElasticsearchInstanceTypesRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_elasticsearch_instance_types_response.ListElasticsearchInstanceTypesResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_instance_types

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_instance_types.list_elasticsearch_instance_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_elasticsearch_instance_types_request.ListElasticsearchInstanceTypesRequest = {
            "elasticsearch_version": elasticsearch_version
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_elasticsearch_instance_types(
        self,
        elasticsearch_version: "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        domain_name: Optional[
            "capo_elasticsearch_service.types.domain_name.DomainName"
        ] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.list_elasticsearch_instance_types_response.ListElasticsearchInstanceTypesResponse]":
        _token = next_token
        while True:
            _response = self.list_elasticsearch_instance_types(
                elasticsearch_version,
                config_overrides=config_overrides,
                domain_name=domain_name,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_elasticsearch_versions(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_elasticsearch_versions_response.ListElasticsearchVersionsResponse":
        """<p>List all supported Elasticsearch versions</p>

        Args:
            max_results: <p> Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_elasticsearch_versions_request.ListElasticsearchVersionsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_elasticsearch_versions_response.ListElasticsearchVersionsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_versions

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_versions.list_elasticsearch_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_elasticsearch_versions_request.ListElasticsearchVersionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_elasticsearch_versions(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.list_elasticsearch_versions_response.ListElasticsearchVersionsResponse]":
        _token = next_token
        while True:
            _response = self.list_elasticsearch_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_packages_for_domain(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_packages_for_domain_response.ListPackagesForDomainResponse":
        """<p>Lists all packages associated with the Amazon ES domain.</p>

        Args:
            domain_name: <p>The name of the domain for which you want to list associated packages.</p>
            max_results: <p>Limits results to a maximum number of packages.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_packages_for_domain_request.ListPackagesForDomainRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_packages_for_domain_response.ListPackagesForDomainResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_packages_for_domain

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_packages_for_domain.list_packages_for_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_packages_for_domain_request.ListPackagesForDomainRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_packages_for_domain(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "capo_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_elasticsearch_service.types.list_packages_for_domain_response.ListPackagesForDomainResponse]":
        _token = next_token
        while True:
            _response = self.list_packages_for_domain(
                domain_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags(
        self,
        arn: "capo_elasticsearch_service.types.arn.ARN",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.list_tags_response.ListTagsResponse":
        """<p>Returns all tags for the given Elasticsearch domain.</p>

        Args:
            arn: <p> Specify the <code>ARN</code> for the Elasticsearch domain to which the tags are attached that you want to view.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_tags_request.ListTagsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_tags_response.ListTagsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_tags

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_tags.list_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_tags_request.ListTagsRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vpc_endpoint_access(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse":
        """<p>Retrieves information about each principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to retrieve access information for.</p>
            next_token: <p>Provides an identifier to allow retrieval of paginated results.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoint_access

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoint_access.list_vpc_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest = {
            "domain_name": domain_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vpc_endpoints(
        self,
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current account and Region.</p>

        Args:
            next_token: <p>Identifier to allow retrieval of paginated results.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints.list_vpc_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vpc_endpoints_for_domain(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        next_token: Optional[
            "capo_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_elasticsearch_service.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse":
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain.</p>

        Args:
            domain_name: <p>Name of the ElasticSearch domain whose VPC endpoints are to be listed.</p>
            next_token: <p>Provides an identifier to allow retrieval of paginated results.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints_for_domain

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints_for_domain.list_vpc_endpoints_for_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest = {
            "domain_name": domain_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def purchase_reserved_elasticsearch_instance_offering(
        self,
        reserved_elasticsearch_instance_offering_id: "capo_elasticsearch_service.types.guid.GUID",
        reservation_name: "capo_elasticsearch_service.types.reservation_token.ReservationToken",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        instance_count: Optional[
            "capo_elasticsearch_service.types.instance_count.InstanceCount"
        ] = None,
    ) -> "capo_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_response.PurchaseReservedElasticsearchInstanceOfferingResponse":
        """<p>Allows you to purchase reserved Elasticsearch instances.</p>

        Args:
            reserved_elasticsearch_instance_offering_id: <p>The ID of the reserved Elasticsearch instance offering to purchase.</p>
            reservation_name: <p>A customer-specified identifier to track this reservation.</p>
            instance_count: <p>The number of Elasticsearch instances to reserve.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_request.PurchaseReservedElasticsearchInstanceOfferingRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_response.PurchaseReservedElasticsearchInstanceOfferingResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.purchase_reserved_elasticsearch_instance_offering

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.purchase_reserved_elasticsearch_instance_offering.purchase_reserved_elasticsearch_instance_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_request.PurchaseReservedElasticsearchInstanceOfferingRequest = {
            "reserved_elasticsearch_instance_offering_id": reserved_elasticsearch_instance_offering_id,
            "reservation_name": reservation_name,
        }
        if instance_count is not None:
            input_["instance_count"] = instance_count

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_inbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "capo_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_response.RejectInboundCrossClusterSearchConnectionResponse":
        """<p>Allows the destination domain owner to reject an inbound cross-cluster search connection request.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the inbound connection that you want to reject.</p>

        Raises:
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_request.RejectInboundCrossClusterSearchConnectionRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_response.RejectInboundCrossClusterSearchConnectionResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.reject_inbound_cross_cluster_search_connection

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.reject_inbound_cross_cluster_search_connection.reject_inbound_cross_cluster_search_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_request.RejectInboundCrossClusterSearchConnectionRequest = {
            "cross_cluster_search_connection_id": cross_cluster_search_connection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags(
        self,
        arn: "capo_elasticsearch_service.types.arn.ARN",
        tag_keys: "capo_elasticsearch_service.types.string_list.StringList",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> None:
        """<p>Removes the specified set of tags from the specified Elasticsearch domain.</p>

        Args:
            arn: <p>Specifies the <code>ARN</code> for the Elasticsearch domain from which you want to delete the specified tags.</p>
            tag_keys: <p>Specifies the <code>TagKey</code> list which you want to remove from the Elasticsearch domain.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.remove_tags_request.RemoveTagsRequest]",
        ) -> OperationResponse[None]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.remove_tags

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.remove_tags.remove_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.remove_tags_request.RemoveTagsRequest = {
            "arn": arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def revoke_vpc_endpoint_access(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        account: "capo_elasticsearch_service.types.aws_account.AWSAccount",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse":
        """<p>Revokes access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain.</p>
            account: <p>The account ID to revoke access from.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.revoke_vpc_endpoint_access

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.revoke_vpc_endpoint_access.revoke_vpc_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest = {
            "domain_name": domain_name,
            "account": account,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_elasticsearch_service_software_update(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.start_elasticsearch_service_software_update_response.StartElasticsearchServiceSoftwareUpdateResponse":
        """<p>Schedules a service software update for an Amazon ES domain.</p>

        Args:
            domain_name: <p>The name of the domain that you want to update to the latest service software.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.start_elasticsearch_service_software_update_request.StartElasticsearchServiceSoftwareUpdateRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.start_elasticsearch_service_software_update_response.StartElasticsearchServiceSoftwareUpdateResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.start_elasticsearch_service_software_update

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.start_elasticsearch_service_software_update.start_elasticsearch_service_software_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.start_elasticsearch_service_software_update_request.StartElasticsearchServiceSoftwareUpdateRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_elasticsearch_domain_config(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        elasticsearch_cluster_config: Optional[
            "capo_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
        ] = None,
        ebs_options: Optional[
            "capo_elasticsearch_service.types.ebs_options.EBSOptions"
        ] = None,
        snapshot_options: Optional[
            "capo_elasticsearch_service.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional[
            "capo_elasticsearch_service.types.vpc_options.VPCOptions"
        ] = None,
        cognito_options: Optional[
            "capo_elasticsearch_service.types.cognito_options.CognitoOptions"
        ] = None,
        advanced_options: Optional[
            "capo_elasticsearch_service.types.advanced_options.AdvancedOptions"
        ] = None,
        access_policies: Optional[
            "capo_elasticsearch_service.types.policy_document.PolicyDocument"
        ] = None,
        log_publishing_options: Optional[
            "capo_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "capo_elasticsearch_service.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        advanced_security_options: Optional[
            "capo_elasticsearch_service.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        node_to_node_encryption_options: Optional[
            "capo_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "capo_elasticsearch_service.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        auto_tune_options: Optional[
            "capo_elasticsearch_service.types.auto_tune_options.AutoTuneOptions"
        ] = None,
        dry_run: Optional["capo_elasticsearch_service.types.dry_run.DryRun"] = None,
        deployment_strategy_options: Optional[
            "capo_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "capo_elasticsearch_service.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
        use_case: Optional[
            "capo_elasticsearch_service.types.domain_use_case.DomainUseCase"
        ] = None,
        engine_mode: Optional[
            "capo_elasticsearch_service.types.domain_engine_mode.DomainEngineMode"
        ] = None,
    ) -> "capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse":
        """<p>Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances. </p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain that you are updating. </p>
            elasticsearch_cluster_config: <p>The type and number of instances to instantiate for the domain cluster.</p>
            ebs_options: <p>Specify the type and size of the EBS volume that you want to use. </p>
            snapshot_options: <p>Option to set the time, in UTC format, for the daily automated snapshot. Default value is <code>0</code> hours. </p>
            vpc_options: <p>Options to specify the subnets and security groups for VPC endpoint. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc" target="_blank">Creating a VPC</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i></p>
            cognito_options: <p>Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html" target="_blank">Amazon Cognito Authentication for Kibana</a>.</p>
            advanced_options: <p>Modifies the advanced option to allow references to indices in an HTTP request body. Must be <code>false</code> when configuring access to individual sub-resources. By default, the value is <code>true</code>. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options" target="_blank">Configuration Advanced Options</a> for more information.</p>
            access_policies: <p>IAM access policy as a JSON-formatted string.</p>
            log_publishing_options: <p>Map of <code>LogType</code> and <code>LogPublishingOption</code>, each containing options to publish a given type of Elasticsearch log.</p>
            domain_endpoint_options: <p>Options to specify configuration that will be applied to the domain endpoint.</p>
            advanced_security_options: <p>Specifies advanced security options.</p>
            node_to_node_encryption_options: <p>Specifies the NodeToNodeEncryptionOptions.</p>
            encryption_at_rest_options: <p>Specifies the Encryption At Rest Options.</p>
            auto_tune_options: <p>Specifies Auto-Tune options.</p>
            dry_run: <p> This flag, when set to True, specifies whether the <code>UpdateElasticsearchDomain</code> request should return the results of validation checks without actually applying the change. This flag, when set to True, specifies the deployment mechanism through which the update shall be applied on the domain. This will not actually perform the Update. </p>
            deployment_strategy_options: <p>Specifies the deployment strategy options.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
            use_case: <p>The primary use case for the domain. For valid values, see <code>DomainUseCase</code>.</p>
            engine_mode: <p>The engine mode for the domain. For valid values and requirements, see <code>DomainEngineMode</code>.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.invalid_type_exception.InvalidTypeException: <p>An exception for trying to create or access sub-resource that is either invalid or not supported. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.update_elasticsearch_domain_config_request.UpdateElasticsearchDomainConfigRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_elasticsearch_domain_config

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_elasticsearch_domain_config.update_elasticsearch_domain_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.update_elasticsearch_domain_config_request.UpdateElasticsearchDomainConfigRequest = {
            "domain_name": domain_name
        }
        if elasticsearch_cluster_config is not None:
            input_["elasticsearch_cluster_config"] = elasticsearch_cluster_config
        if ebs_options is not None:
            input_["ebs_options"] = ebs_options
        if snapshot_options is not None:
            input_["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if cognito_options is not None:
            input_["cognito_options"] = cognito_options
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options
        if access_policies is not None:
            input_["access_policies"] = access_policies
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if domain_endpoint_options is not None:
            input_["domain_endpoint_options"] = domain_endpoint_options
        if advanced_security_options is not None:
            input_["advanced_security_options"] = advanced_security_options
        if node_to_node_encryption_options is not None:
            input_["node_to_node_encryption_options"] = node_to_node_encryption_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if auto_tune_options is not None:
            input_["auto_tune_options"] = auto_tune_options
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if deployment_strategy_options is not None:
            input_["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input_["automated_snapshot_pause_options"] = (
                automated_snapshot_pause_options
            )
        if use_case is not None:
            input_["use_case"] = use_case
        if engine_mode is not None:
            input_["engine_mode"] = engine_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_package(
        self,
        package_id: "capo_elasticsearch_service.types.package_id.PackageID",
        package_source: "capo_elasticsearch_service.types.package_source.PackageSource",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        package_description: Optional[
            "capo_elasticsearch_service.types.package_description.PackageDescription"
        ] = None,
        commit_message: Optional[
            "capo_elasticsearch_service.types.commit_message.CommitMessage"
        ] = None,
    ) -> (
        "capo_elasticsearch_service.types.update_package_response.UpdatePackageResponse"
    ):
        """<p>Updates a package for use with Amazon ES domains.</p>

        Args:
            package_id: <p>Unique identifier for the package.</p>
            package_description: <p>New description of the package.</p>
            commit_message: <p>An info message for the new version which will be shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>

        Raises:
            capo_elasticsearch_service.errors.access_denied_exception.AccessDeniedException: <p>An error occurred because user does not have permissions to access the resource. Returns HTTP status code 403.</p>
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.limit_exceeded_exception.LimitExceededException: <p>An exception for trying to create more than allowed resources or sub-resources. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.update_package_request.UpdatePackageRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.update_package_response.UpdatePackageResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_package

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_package.update_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.update_package_request.UpdatePackageRequest = {
            "package_id": package_id,
            "package_source": package_source,
        }
        if package_description is not None:
            input_["package_description"] = package_description
        if commit_message is not None:
            input_["commit_message"] = commit_message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vpc_endpoint(
        self,
        vpc_endpoint_id: "capo_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId",
        vpc_options: "capo_elasticsearch_service.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
    ) -> "capo_elasticsearch_service.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse":
        """<p>Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>Unique identifier of the VPC endpoint to be updated.</p>
            vpc_options: <p>The security groups and/or subnets to add, remove, or modify.</p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.conflict_exception.ConflictException: <p>An error occurred because the client attempts to remove a resource that is currently in use. Returns HTTP status code 409.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_vpc_endpoint

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_vpc_endpoint.update_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest = {
            "vpc_endpoint_id": vpc_endpoint_id,
            "vpc_options": vpc_options,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def upgrade_elasticsearch_domain(
        self,
        domain_name: "capo_elasticsearch_service.types.domain_name.DomainName",
        target_version: "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString",
        *,
        config_overrides: Optional[ElasticsearchServiceClientConfig] = None,
        perform_check_only: Optional[
            "capo_elasticsearch_service.types.boolean.Boolean"
        ] = None,
    ) -> "capo_elasticsearch_service.types.upgrade_elasticsearch_domain_response.UpgradeElasticsearchDomainResponse":
        """<p>Allows you to either upgrade your domain or perform an Upgrade eligibility check to a compatible Elasticsearch version.</p>

        Args:
            target_version: <p>The version of Elasticsearch that you intend to upgrade the domain to.</p>
            perform_check_only: <p> This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade. </p>

        Raises:
            capo_elasticsearch_service.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_elasticsearch_service.errors.disabled_operation_exception.DisabledOperationException: <p>An error occured because the client wanted to access a not supported operation. Gives http status code of 409.</p>
            capo_elasticsearch_service.errors.internal_exception.InternalException: <p>The request processing has failed because of an unknown error, exception or failure (the failure is internal to the service) . Gives http status code of 500.</p>
            capo_elasticsearch_service.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>An exception for creating a resource that already exists. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.resource_not_found_exception.ResourceNotFoundException: <p>An exception for accessing or deleting a resource that does not exist. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.validation_exception.ValidationException: <p>An exception for missing / invalid input fields. Gives http status code of 400.</p>
            capo_elasticsearch_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_elasticsearch_service.types.upgrade_elasticsearch_domain_request.UpgradeElasticsearchDomainRequest]",
        ) -> OperationResponse[
            "capo_elasticsearch_service.types.upgrade_elasticsearch_domain_response.UpgradeElasticsearchDomainResponse"
        ]:
            import capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.upgrade_elasticsearch_domain

            output, http_response = (
                capo_elasticsearch_service._operations.amazon_elasticsearch_service2015.upgrade_elasticsearch_domain.upgrade_elasticsearch_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_elasticsearch_service.types.upgrade_elasticsearch_domain_request.UpgradeElasticsearchDomainRequest = {
            "domain_name": domain_name,
            "target_version": target_version,
        }
        if perform_check_only is not None:
            input_["perform_check_only"] = perform_check_only

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
