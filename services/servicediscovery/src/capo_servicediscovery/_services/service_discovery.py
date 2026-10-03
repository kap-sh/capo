"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Route53AutoNaming_v20170314``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_servicediscovery._auth._signers
import capo_servicediscovery._auth._sigv4
from capo_servicediscovery._auth._identity import Credentials
from capo_servicediscovery._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_servicediscovery._auth._zapros_handler import AuthMiddleware
from capo_servicediscovery._pagination import resolve_path as _resolve_path
from capo_servicediscovery._services._aws_config import aws_config
from capo_servicediscovery._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_servicediscovery.types.amazon_resource_name
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.attributes
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.create_http_namespace_request
    import capo_servicediscovery.types.create_http_namespace_response
    import capo_servicediscovery.types.create_private_dns_namespace_request
    import capo_servicediscovery.types.create_private_dns_namespace_response
    import capo_servicediscovery.types.create_public_dns_namespace_request
    import capo_servicediscovery.types.create_public_dns_namespace_response
    import capo_servicediscovery.types.create_service_request
    import capo_servicediscovery.types.create_service_response
    import capo_servicediscovery.types.custom_health_status
    import capo_servicediscovery.types.delete_namespace_request
    import capo_servicediscovery.types.delete_namespace_response
    import capo_servicediscovery.types.delete_service_attributes_request
    import capo_servicediscovery.types.delete_service_attributes_response
    import capo_servicediscovery.types.delete_service_request
    import capo_servicediscovery.types.delete_service_response
    import capo_servicediscovery.types.deregister_instance_request
    import capo_servicediscovery.types.deregister_instance_response
    import capo_servicediscovery.types.discover_instances_request
    import capo_servicediscovery.types.discover_instances_response
    import capo_servicediscovery.types.discover_instances_revision_request
    import capo_servicediscovery.types.discover_instances_revision_response
    import capo_servicediscovery.types.discover_max_results
    import capo_servicediscovery.types.dns_config
    import capo_servicediscovery.types.get_instance_request
    import capo_servicediscovery.types.get_instance_response
    import capo_servicediscovery.types.get_instances_health_status_request
    import capo_servicediscovery.types.get_instances_health_status_response
    import capo_servicediscovery.types.get_namespace_request
    import capo_servicediscovery.types.get_namespace_response
    import capo_servicediscovery.types.get_operation_request
    import capo_servicediscovery.types.get_operation_response
    import capo_servicediscovery.types.get_service_attributes_request
    import capo_servicediscovery.types.get_service_attributes_response
    import capo_servicediscovery.types.get_service_request
    import capo_servicediscovery.types.get_service_response
    import capo_servicediscovery.types.health_check_config
    import capo_servicediscovery.types.health_check_custom_config
    import capo_servicediscovery.types.health_status_filter
    import capo_servicediscovery.types.http_namespace_change
    import capo_servicediscovery.types.instance_id
    import capo_servicediscovery.types.instance_id_list
    import capo_servicediscovery.types.list_instances_request
    import capo_servicediscovery.types.list_instances_response
    import capo_servicediscovery.types.list_namespaces_request
    import capo_servicediscovery.types.list_namespaces_response
    import capo_servicediscovery.types.list_operations_request
    import capo_servicediscovery.types.list_operations_response
    import capo_servicediscovery.types.list_services_request
    import capo_servicediscovery.types.list_services_response
    import capo_servicediscovery.types.list_tags_for_resource_request
    import capo_servicediscovery.types.list_tags_for_resource_response
    import capo_servicediscovery.types.max_results
    import capo_servicediscovery.types.namespace_filters
    import capo_servicediscovery.types.namespace_name
    import capo_servicediscovery.types.namespace_name_http
    import capo_servicediscovery.types.namespace_name_private
    import capo_servicediscovery.types.namespace_name_public
    import capo_servicediscovery.types.next_token
    import capo_servicediscovery.types.operation_filters
    import capo_servicediscovery.types.operation_id
    import capo_servicediscovery.types.private_dns_namespace_change
    import capo_servicediscovery.types.private_dns_namespace_properties
    import capo_servicediscovery.types.public_dns_namespace_change
    import capo_servicediscovery.types.public_dns_namespace_properties
    import capo_servicediscovery.types.register_instance_request
    import capo_servicediscovery.types.register_instance_response
    import capo_servicediscovery.types.resource_description
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.service_attribute_key_list
    import capo_servicediscovery.types.service_attributes_map
    import capo_servicediscovery.types.service_change
    import capo_servicediscovery.types.service_filters
    import capo_servicediscovery.types.service_name
    import capo_servicediscovery.types.service_type_option
    import capo_servicediscovery.types.tag_key_list
    import capo_servicediscovery.types.tag_list
    import capo_servicediscovery.types.tag_resource_request
    import capo_servicediscovery.types.tag_resource_response
    import capo_servicediscovery.types.untag_resource_request
    import capo_servicediscovery.types.untag_resource_response
    import capo_servicediscovery.types.update_http_namespace_request
    import capo_servicediscovery.types.update_http_namespace_response
    import capo_servicediscovery.types.update_instance_custom_health_status_request
    import capo_servicediscovery.types.update_private_dns_namespace_request
    import capo_servicediscovery.types.update_private_dns_namespace_response
    import capo_servicediscovery.types.update_public_dns_namespace_request
    import capo_servicediscovery.types.update_public_dns_namespace_response
    import capo_servicediscovery.types.update_service_attributes_request
    import capo_servicediscovery.types.update_service_attributes_response
    import capo_servicediscovery.types.update_service_request
    import capo_servicediscovery.types.update_service_response


class ServiceDiscoveryClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ServiceDiscoveryClient:
    """A client for the ``ServiceDiscovery`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = ServiceDiscoveryClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[ServiceDiscoveryClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ServiceDiscoveryClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_http_namespace(
        self,
        name: "capo_servicediscovery.types.namespace_name_http.NamespaceNameHttp",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        creator_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
        description: Optional[
            "capo_servicediscovery.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_servicediscovery.types.tag_list.TagList"] = None,
    ) -> "capo_servicediscovery.types.create_http_namespace_response.CreateHttpNamespaceResponse":
        """<p>Creates an HTTP namespace. Service instances registered using an HTTP namespace can be discovered using a <code>DiscoverInstances</code> request but can't be discovered using DNS.</p> <p>For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html">Cloud Map quotas</a> in the <i>Cloud Map Developer Guide</i>.</p>

        Args:
            name: <p>The name that you want to assign to this namespace.</p>
            creator_request_id: <p>A unique string that identifies the request and that allows failed <code>CreateHttpNamespace</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/time stamp).</p>
            description: <p>A description for the namespace.</p>
            tags: <p>The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_already_exists.NamespaceAlreadyExists: <p>The namespace that you're trying to create already exists.</p>
            capo_servicediscovery.errors.resource_limit_exceeded.ResourceLimitExceeded: <p>The resource can't be created because you've reached the quota on the number of resources.</p>
            capo_servicediscovery.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateHttpNamespace example
            This example creates an HTTP namespace.

            >>> client.create_http_namespace(creator_request_id='example-creator-request-id-0001', name='example-http.com', description='Example.com AWS Cloud Map HTTP Namespace')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.create_http_namespace_request.CreateHttpNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.create_http_namespace_response.CreateHttpNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.create_http_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.create_http_namespace.create_http_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.create_http_namespace_request.CreateHttpNamespaceRequest = {
            "name": name
        }
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_private_dns_namespace(
        self,
        name: "capo_servicediscovery.types.namespace_name_private.NamespaceNamePrivate",
        vpc: "capo_servicediscovery.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        creator_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
        description: Optional[
            "capo_servicediscovery.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_servicediscovery.types.tag_list.TagList"] = None,
        properties: Optional[
            "capo_servicediscovery.types.private_dns_namespace_properties.PrivateDnsNamespaceProperties"
        ] = None,
    ) -> "capo_servicediscovery.types.create_private_dns_namespace_response.CreatePrivateDnsNamespaceResponse":
        """<p>Creates a private namespace based on DNS, which is visible only inside a specified Amazon VPC. The namespace defines your service naming scheme. For example, if you name your namespace <code>example.com</code> and name your service <code>backend</code>, the resulting DNS name for the service is <code>backend.example.com</code>. Service instances that are registered using a private DNS namespace can be discovered using either a <code>DiscoverInstances</code> request or using DNS. For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html">Cloud Map quotas</a> in the <i>Cloud Map Developer Guide</i>.</p>

        Args:
            name: <p>The name that you want to assign to this namespace. When you create a private DNS namespace, Cloud Map automatically creates an Amazon Route 53 private hosted zone that has the same name as the namespace.</p>
            creator_request_id: <p>A unique string that identifies the request and that allows failed <code>CreatePrivateDnsNamespace</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/timestamp).</p>
            description: <p>A description for the namespace.</p>
            vpc: <p>The ID of the Amazon VPC that you want to associate the namespace with.</p>
            tags: <p>The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>
            properties: <p>Properties for the private DNS namespace.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_already_exists.NamespaceAlreadyExists: <p>The namespace that you're trying to create already exists.</p>
            capo_servicediscovery.errors.resource_limit_exceeded.ResourceLimitExceeded: <p>The resource can't be created because you've reached the quota on the number of resources.</p>
            capo_servicediscovery.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: Create private DNS namespace
            Example: Create private DNS namespace

            >>> client.create_private_dns_namespace(name='example.com', vpc='vpc-1c56417b', creator_request_id='eedd6892-50f3-41b2-8af9-611d6e1d1a8c')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.create_private_dns_namespace_request.CreatePrivateDnsNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.create_private_dns_namespace_response.CreatePrivateDnsNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.create_private_dns_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.create_private_dns_namespace.create_private_dns_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.create_private_dns_namespace_request.CreatePrivateDnsNamespaceRequest = {
            "name": name,
            "vpc": vpc,
        }
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if properties is not None:
            input_["properties"] = properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_public_dns_namespace(
        self,
        name: "capo_servicediscovery.types.namespace_name_public.NamespaceNamePublic",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        creator_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
        description: Optional[
            "capo_servicediscovery.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_servicediscovery.types.tag_list.TagList"] = None,
        properties: Optional[
            "capo_servicediscovery.types.public_dns_namespace_properties.PublicDnsNamespaceProperties"
        ] = None,
    ) -> "capo_servicediscovery.types.create_public_dns_namespace_response.CreatePublicDnsNamespaceResponse":
        """<p>Creates a public namespace based on DNS, which is visible on the internet. The namespace defines your service naming scheme. For example, if you name your namespace <code>example.com</code> and name your service <code>backend</code>, the resulting DNS name for the service is <code>backend.example.com</code>. You can discover instances that were registered with a public DNS namespace by using either a <code>DiscoverInstances</code> request or using DNS. For the current quota on the number of namespaces that you can create using the same Amazon Web Services account, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html">Cloud Map quotas</a> in the <i>Cloud Map Developer Guide</i>.</p> <important> <p>The <code>CreatePublicDnsNamespace</code> API operation is not supported in the Amazon Web Services GovCloud (US) Regions.</p> </important>

        Args:
            name: <p>The name that you want to assign to this namespace.</p> <note> <p>Do not include sensitive information in the name. The name is publicly available using DNS queries.</p> </note>
            creator_request_id: <p>A unique string that identifies the request and that allows failed <code>CreatePublicDnsNamespace</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/timestamp).</p>
            description: <p>A description for the namespace.</p>
            tags: <p>The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>
            properties: <p>Properties for the public DNS namespace.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_already_exists.NamespaceAlreadyExists: <p>The namespace that you're trying to create already exists.</p>
            capo_servicediscovery.errors.resource_limit_exceeded.ResourceLimitExceeded: <p>The resource can't be created because you've reached the quota on the number of resources.</p>
            capo_servicediscovery.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreatePublicDnsNamespace example
            This example creates a public namespace based on DNS.

            >>> client.create_public_dns_namespace(creator_request_id='example-creator-request-id-0003', name='example-public-dns.com', description='Example.com AWS Cloud Map Public DNS Namespace')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.create_public_dns_namespace_request.CreatePublicDnsNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.create_public_dns_namespace_response.CreatePublicDnsNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.create_public_dns_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.create_public_dns_namespace.create_public_dns_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.create_public_dns_namespace_request.CreatePublicDnsNamespaceRequest = {
            "name": name
        }
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if properties is not None:
            input_["properties"] = properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_service(
        self,
        name: "capo_servicediscovery.types.service_name.ServiceName",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        namespace_id: Optional["capo_servicediscovery.types.arn.Arn"] = None,
        creator_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
        description: Optional[
            "capo_servicediscovery.types.resource_description.ResourceDescription"
        ] = None,
        dns_config: Optional["capo_servicediscovery.types.dns_config.DnsConfig"] = None,
        health_check_config: Optional[
            "capo_servicediscovery.types.health_check_config.HealthCheckConfig"
        ] = None,
        health_check_custom_config: Optional[
            "capo_servicediscovery.types.health_check_custom_config.HealthCheckCustomConfig"
        ] = None,
        tags: Optional["capo_servicediscovery.types.tag_list.TagList"] = None,
        type: Optional[
            "capo_servicediscovery.types.service_type_option.ServiceTypeOption"
        ] = None,
    ) -> "capo_servicediscovery.types.create_service_response.CreateServiceResponse":
        """<p>Creates a service. This action defines the configuration for the following entities:</p> <ul> <li> <p>For public and private DNS namespaces, one of the following combinations of DNS records in Amazon Route 53:</p> <ul> <li> <p> <code>A</code> </p> </li> <li> <p> <code>AAAA</code> </p> </li> <li> <p> <code>A</code> and <code>AAAA</code> </p> </li> <li> <p> <code>SRV</code> </p> </li> <li> <p> <code>CNAME</code> </p> </li> </ul> </li> <li> <p>Optionally, a health check</p> </li> </ul> <p>After you create the service, you can submit a <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html">RegisterInstance</a> request, and Cloud Map uses the values in the configuration to create the specified entities.</p> <p>For the current quota on the number of instances that you can register using the same namespace and using the same service, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html">Cloud Map quotas</a> in the <i>Cloud Map Developer Guide</i>.</p>

        Args:
            name: <p>The name that you want to assign to the service.</p> <note> <p>Do not include sensitive information in the name if the namespace is discoverable by public DNS queries.</p> </note> <p>If you want Cloud Map to create an <code>SRV</code> record when you register an instance and you're using a system that requires a specific <code>SRV</code> format, such as <a href="http://www.haproxy.org/">HAProxy</a>, specify the following for <code>Name</code>:</p> <ul> <li> <p>Start the name with an underscore (_), such as <code>_exampleservice</code>.</p> </li> <li> <p>End the name with <i>._protocol</i>, such as <code>._tcp</code>.</p> </li> </ul> <p>When you register an instance, Cloud Map creates an <code>SRV</code> record and assigns a name to the record by concatenating the service name and the namespace name (for example,</p> <p> <code>_exampleservice._tcp.example.com</code>).</p> <note> <p>For services that are accessible by DNS queries, you can't create multiple services with names that differ only by case (such as EXAMPLE and example). Otherwise, these services have the same DNS name and can't be distinguished. However, if you use a namespace that's only accessible by API calls, then you can create services that with names that differ only by case.</p> </note>
            namespace_id: <p>The ID or Amazon Resource Name (ARN) of the namespace that you want to use to create the service. For namespaces shared with your Amazon Web Services account, specify the namespace ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            creator_request_id: <p>A unique string that identifies the request and that allows failed <code>CreateService</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/timestamp).</p>
            description: <p>A description for the service.</p>
            dns_config: <p>A complex type that contains information about the Amazon Route 53 records that you want Cloud Map to create when you register an instance. </p>
            health_check_config: <p> <i>Public DNS and HTTP namespaces only.</i> A complex type that contains settings for an optional Route 53 health check. If you specify settings for a health check, Cloud Map associates the health check with all the Route 53 DNS records that you specify in <code>DnsConfig</code>.</p> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important> <p>For information about the charges for health checks, see <a href="http://aws.amazon.com/cloud-map/pricing/">Cloud Map Pricing</a>.</p>
            health_check_custom_config: <p>A complex type that contains information about an optional custom health check.</p> <important> <p>If you specify a health check configuration, you can specify either <code>HealthCheckCustomConfig</code> or <code>HealthCheckConfig</code> but not both.</p> </important> <p>You can't add, update, or delete a <code>HealthCheckCustomConfig</code> configuration from an existing service.</p>
            tags: <p>The tags to add to the service. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>
            type: <p>If present, specifies that the service instances are only discoverable using the <code>DiscoverInstances</code> API operation. No DNS records is registered for the service instances. The only valid value is <code>HTTP</code>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.resource_limit_exceeded.ResourceLimitExceeded: <p>The resource can't be created because you've reached the quota on the number of resources.</p>
            capo_servicediscovery.errors.service_already_exists.ServiceAlreadyExists: <p>The service can't be created because a service with the same name already exists.</p>
            capo_servicediscovery.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: Create service
            Example: Create service

            >>> client.create_service(name='myservice', namespace_id='ns-ylexjili4cdxy3xm', dns_config={'NamespaceId': 'ns-ylexjili4cdxy3xm', 'RoutingPolicy': 'MULTIVALUE', 'DnsRecords': [{'Type': 'A', 'TTL': 60}]}, creator_request_id='567c1193-6b00-4308-bd57-ad38a8822d25')
            Create service using namespace ARN
            Namespace sharee creates a service using a namespace ARN instead of namespace ID, useful when working with shared namespaces.

            >>> client.create_service(name='example-service', namespace_id='arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678', description='Example service using namespace ARN', dns_config={'DnsRecords': [{'Type': 'A', 'TTL': 300}], 'RoutingPolicy': 'MULTIVALUE'})
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.create_service

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.create_service_request.CreateServiceRequest = {
            "name": name
        }
        if namespace_id is not None:
            input_["namespace_id"] = namespace_id
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id
        if description is not None:
            input_["description"] = description
        if dns_config is not None:
            input_["dns_config"] = dns_config
        if health_check_config is not None:
            input_["health_check_config"] = health_check_config
        if health_check_custom_config is not None:
            input_["health_check_custom_config"] = health_check_custom_config
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_namespace(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> (
        "capo_servicediscovery.types.delete_namespace_response.DeleteNamespaceResponse"
    ):
        """<p>Deletes a namespace from the current account. If the namespace still contains one or more services, the request fails.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the namespace that you want to delete.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.resource_in_use.ResourceInUse: <p>The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: Delete namespace
            Example: Delete namespace

            >>> client.delete_namespace(id='ns-ylexjili4cdxy3xm')
            Delete namespace using namespace ARN
            Deletes a namespace using a namespace ARN instead of namespace ID, useful when working with shared namespaces.

            >>> client.delete_namespace(id='arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.delete_namespace_response.DeleteNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.delete_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.delete_namespace.delete_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.delete_namespace_request.DeleteNamespaceRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a specified service and all associated service attributes. If the service still contains one or more registered instances, the request fails.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the service that you want to delete. If the namespace associated with the service is shared with your Amazon Web Services account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.resource_in_use.ResourceInUse: <p>The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: Delete service
            Example: Delete service

            >>> client.delete_service(id='srv-p5zdwlg5uvvzjita')
            Delete service using service ARN
            Deletes a service using a service ARN instead of service ID, useful when working with shared namespaces.

            >>> client.delete_service(id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.delete_service

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.delete_service_request.DeleteServiceRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_attributes(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        attributes: "capo_servicediscovery.types.service_attribute_key_list.ServiceAttributeKeyList",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.delete_service_attributes_response.DeleteServiceAttributesResponse":
        """<p>Deletes specific attributes associated with a service.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service from which the attributes will be deleted. For services created in a namespace shared with your Amazon Web Services account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            attributes: <p>A list of keys corresponding to each attribute that you want to delete.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteServiceAttributes example
            Example: Delete service attribute by providing attribute key and service ID

            >>> client.delete_service_attributes(attributes=['port'], service_id='srv-e4anhexample0004')
            Delete service attributes using service ARN
            Deletes service attributes using a service ARN instead of service ID, useful for cross-account scenarios or when working with shared namespaces.

            >>> client.delete_service_attributes(service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678', attributes=['Port'])
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.delete_service_attributes_request.DeleteServiceAttributesRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.delete_service_attributes_response.DeleteServiceAttributesResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.delete_service_attributes

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.delete_service_attributes.delete_service_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.delete_service_attributes_request.DeleteServiceAttributesRequest = {
            "service_id": service_id,
            "attributes": attributes,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_instance(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        instance_id: "capo_servicediscovery.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.deregister_instance_response.DeregisterInstanceResponse":
        """<p>Deletes the Amazon Route 53 DNS records and health check, if any, that Cloud Map created for the specified instance.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. If the namespace associated with the service is shared with your account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            instance_id: <p>The value that you specified for <code>Id</code> in the <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html">RegisterInstance</a> request.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.instance_not_found.InstanceNotFound: <p>No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.resource_in_use.ResourceInUse: <p>The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: Deregister a service instance
            Example: Deregister a service instance

            >>> client.deregister_instance(service_id='srv-p5zdwlg5uvvzjita', instance_id='myservice-53')
            Deregister instance using service ARN
            Deregisters an instance using a service ARN instead of service ID, useful when working with shared namespaces.

            >>> client.deregister_instance(instance_id='i-abcd1234xmpl5678', service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.deregister_instance_request.DeregisterInstanceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.deregister_instance_response.DeregisterInstanceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.deregister_instance

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.deregister_instance.deregister_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.deregister_instance_request.DeregisterInstanceRequest = {
            "service_id": service_id,
            "instance_id": instance_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def discover_instances(
        self,
        namespace_name: "capo_servicediscovery.types.namespace_name.NamespaceName",
        service_name: "capo_servicediscovery.types.service_name.ServiceName",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        max_results: Optional[
            "capo_servicediscovery.types.discover_max_results.DiscoverMaxResults"
        ] = None,
        query_parameters: Optional[
            "capo_servicediscovery.types.attributes.Attributes"
        ] = None,
        optional_parameters: Optional[
            "capo_servicediscovery.types.attributes.Attributes"
        ] = None,
        health_status: Optional[
            "capo_servicediscovery.types.health_status_filter.HealthStatusFilter"
        ] = None,
        owner_account: Optional[
            "capo_servicediscovery.types.aws_account_id.AWSAccountId"
        ] = None,
    ) -> "capo_servicediscovery.types.discover_instances_response.DiscoverInstancesResponse":
        """<p>Discovers registered instances for a specified namespace and service. You can use <code>DiscoverInstances</code> to discover instances for any type of namespace. <code>DiscoverInstances</code> returns a randomized list of instances allowing customers to distribute traffic evenly across instances. For public and private DNS namespaces, you can also use DNS queries to discover instances.</p>

        Args:
            namespace_name: <p>The <code>HttpName</code> name of the namespace. The <code>HttpName</code> is found in the <code>HttpProperties</code> member of the <code>Properties</code> member of the namespace. In most cases, <code>Name</code> and <code>HttpName</code> match. However, if you reuse <code>Name</code> for namespace creation, a generated hash is added to <code>HttpName</code> to distinguish the two.</p>
            service_name: <p>The name of the service that you specified when you registered the instance.</p>
            max_results: <p>The maximum number of instances that you want Cloud Map to return in the response to a <code>DiscoverInstances</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 instances.</p>
            query_parameters: <p>Filters to scope the results based on custom attributes for the instance (for example, <code>{version=v1, az=1a}</code>). Only instances that match all the specified key-value pairs are returned.</p>
            optional_parameters: <p>Opportunistic filters to scope the results based on custom attributes. If there are instances that match both the filters specified in both the <code>QueryParameters</code> parameter and this parameter, all of these instances are returned. Otherwise, the filters are ignored, and only instances that match the filters that are specified in the <code>QueryParameters</code> parameter are returned.</p>
            health_status: <p>The health status of the instances that you want to discover. This parameter is ignored for services that don't have a health check configured, and all instances are returned.</p> <dl> <dt>HEALTHY</dt> <dd> <p>Returns healthy instances.</p> </dd> <dt>UNHEALTHY</dt> <dd> <p>Returns unhealthy instances.</p> </dd> <dt>ALL</dt> <dd> <p>Returns all instances.</p> </dd> <dt>HEALTHY_OR_ELSE_ALL</dt> <dd> <p>Returns healthy instances, unless none are reporting a healthy state. In that case, return all instances. This is also called failing open.</p> </dd> </dl>
            owner_account: <p>The ID of the Amazon Web Services account that owns the namespace associated with the instance, as specified in the namespace <code>ResourceOwner</code> field. For instances associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.request_limit_exceeded.RequestLimitExceeded: <p>The operation can't be completed because you've reached the quota for the number of requests. For more information, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/throttling.html">Cloud Map API request throttling quota</a> in the <i>Cloud Map Developer Guide</i>.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Discover instances using owner account
            Discovers instances in a shared namespace by specifying the OwnerAccount parameter, useful when working with shared namespaces.

            >>> client.discover_instances(namespace_name='example-shared-namespace', service_name='shared-namespace-service', owner_account='123456789012')
            Example: Discover registered instances
            Example: Discover registered instances

            >>> client.discover_instances(namespace_name='example.com', service_name='myservice', max_results=10, health_status='ALL')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.discover_instances_request.DiscoverInstancesRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.discover_instances_response.DiscoverInstancesResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.discover_instances

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.discover_instances.discover_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.discover_instances_request.DiscoverInstancesRequest = {
            "namespace_name": namespace_name,
            "service_name": service_name,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if query_parameters is not None:
            input_["query_parameters"] = query_parameters
        if optional_parameters is not None:
            input_["optional_parameters"] = optional_parameters
        if health_status is not None:
            input_["health_status"] = health_status
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def discover_instances_revision(
        self,
        namespace_name: "capo_servicediscovery.types.namespace_name.NamespaceName",
        service_name: "capo_servicediscovery.types.service_name.ServiceName",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        owner_account: Optional[
            "capo_servicediscovery.types.aws_account_id.AWSAccountId"
        ] = None,
    ) -> "capo_servicediscovery.types.discover_instances_revision_response.DiscoverInstancesRevisionResponse":
        """<p>Discovers the increasing revision associated with an instance.</p>

        Args:
            namespace_name: <p>The <code>HttpName</code> name of the namespace. The <code>HttpName</code> is found in the <code>HttpProperties</code> member of the <code>Properties</code> member of the namespace.</p>
            service_name: <p>The name of the service that you specified when you registered the instance.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the namespace associated with the instance, as specified in the namespace <code>ResourceOwner</code> field. For instances associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.request_limit_exceeded.RequestLimitExceeded: <p>The operation can't be completed because you've reached the quota for the number of requests. For more information, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/throttling.html">Cloud Map API request throttling quota</a> in the <i>Cloud Map Developer Guide</i>.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Discover instances revision using owner account
            Discovers the instances revision in a shared namespace by specifying the OwnerAccount parameter, useful when working with shared namespaces.

            >>> client.discover_instances_revision(namespace_name='example-shared-namespace', service_name='shared-service', owner_account='123456789012')
            To discover the revision for a registered instance
            The following example discovers the revision ID for a registered instance.

            >>> client.discover_instances_revision(namespace_name='example-namespace', service_name='example-service')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.discover_instances_revision_request.DiscoverInstancesRevisionRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.discover_instances_revision_response.DiscoverInstancesRevisionResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.discover_instances_revision

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.discover_instances_revision.discover_instances_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.discover_instances_revision_request.DiscoverInstancesRevisionRequest = {
            "namespace_name": namespace_name,
            "service_name": service_name,
        }
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_instance(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        instance_id: "capo_servicediscovery.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.get_instance_response.GetInstanceResponse":
        """<p>Gets information about a specified instance.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            instance_id: <p>The ID of the instance that you want to get information about.</p>

        Raises:
            capo_servicediscovery.errors.instance_not_found.InstanceNotFound: <p>No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetInstance example
            This example gets information about a specified instance.

            >>> client.get_instance(instance_id='i-abcd1234', service_id='srv-e4anhexample0004')
            Get instance details using service ARN for shared namespace
            This example gets information about an instance using a service ARN instead of service ID. This is useful for listing instances associated with shared namespaces.

            >>> client.get_instance(instance_id='i-abcd1234', service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.get_instance_request.GetInstanceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.get_instance_response.GetInstanceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.get_instance

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.get_instance.get_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.get_instance_request.GetInstanceRequest = {
            "service_id": service_id,
            "instance_id": instance_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_instances_health_status(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        instances: Optional[
            "capo_servicediscovery.types.instance_id_list.InstanceIdList"
        ] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
    ) -> "capo_servicediscovery.types.get_instances_health_status_response.GetInstancesHealthStatusResponse":
        """<p>Gets the current health status (<code>Healthy</code>, <code>Unhealthy</code>, or <code>Unknown</code>) of one or more instances that are associated with a specified service.</p> <note> <p>There's a brief delay between when you register an instance and when the health status for the instance is available. </p> </note>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that the instance is associated with. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            instances: <p>An array that contains the IDs of all the instances that you want to get the health status for.</p> <p>If you omit <code>Instances</code>, Cloud Map returns the health status for all the instances that are associated with the specified service.</p> <note> <p>To get the IDs for the instances that you've registered by using a specified service, submit a <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html">ListInstances</a> request.</p> </note>
            max_results: <p>The maximum number of instances that you want Cloud Map to return in the response to a <code>GetInstancesHealthStatus</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 instances.</p>
            next_token: <p>For the first <code>GetInstancesHealthStatus</code> request, omit this value.</p> <p>If more than <code>MaxResults</code> instances match the specified criteria, you can submit another <code>GetInstancesHealthStatus</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p>

        Raises:
            capo_servicediscovery.errors.instance_not_found.InstanceNotFound: <p>No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetInstancesHealthStatus example
            This example gets the current health status of one or more instances that are associate with a specified service.

            >>> client.get_instances_health_status(service_id='srv-e4anhexample0004')
            Get instances health status using service ARN for shared namespace
            This example gets the current health status of instances using a service ARN instead of service ID. This is useful for checking health status of instances associated with shared namespaces.

            >>> client.get_instances_health_status(service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.get_instances_health_status_request.GetInstancesHealthStatusRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.get_instances_health_status_response.GetInstancesHealthStatusResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.get_instances_health_status

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.get_instances_health_status.get_instances_health_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.get_instances_health_status_request.GetInstancesHealthStatusRequest = {
            "service_id": service_id
        }
        if instances is not None:
            input_["instances"] = instances
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

    def iter_get_instances_health_status(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        instances: Optional[
            "capo_servicediscovery.types.instance_id_list.InstanceIdList"
        ] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_servicediscovery.types.get_instances_health_status_response.GetInstancesHealthStatusResponse]":
        _token = next_token
        while True:
            _response = self.get_instances_health_status(
                service_id,
                config_overrides=config_overrides,
                instances=instances,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_namespace(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.get_namespace_response.GetNamespaceResponse":
        """<p>Gets information about a namespace.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the namespace that you want to get information about. For namespaces shared with your Amazon Web Services account, specify the namespace ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i> </p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.get_namespace_request.GetNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.get_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.get_namespace.get_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.get_namespace_request.GetNamespaceRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_operation(
        self,
        operation_id: "capo_servicediscovery.types.operation_id.OperationId",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        owner_account: Optional[
            "capo_servicediscovery.types.aws_account_id.AWSAccountId"
        ] = None,
    ) -> "capo_servicediscovery.types.get_operation_response.GetOperationResponse":
        """<p>Gets information about any operation that returns an operation ID in the response, such as a <code>CreateHttpNamespace</code> request.</p> <note> <p>To get a list of operations that match specified criteria, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html">ListOperations</a>.</p> </note>

        Args:
            operation_id: <p>The ID of the operation that you want to get more information about.</p>
            owner_account: <p>The ID of the Amazon Web Services account that owns the namespace associated with the operation, as specified in the namespace <code>ResourceOwner</code> field. For operations associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.operation_not_found.OperationNotFound: <p>No operation exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: Get operation result
            Example: Get operation result

            >>> client.get_operation(operation_id='gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9302yzd')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.get_operation_request.GetOperationRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.get_operation_response.GetOperationResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.get_operation

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.get_operation.get_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.get_operation_request.GetOperationRequest = {
            "operation_id": operation_id
        }
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.get_service_response.GetServiceResponse":
        """<p>Gets the settings for a specified service.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the service that you want to get settings for. For services created by consumers in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get service using service ARN
            Gets service settings using a service ARN instead of service ID, useful when working with shared namespaces. Shows a service created by a sharee (111122223333) in a namespace owned by another account (123456789012).

            >>> client.get_service(id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.get_service_request.GetServiceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.get_service_response.GetServiceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.get_service

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.get_service_request.GetServiceRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service_attributes(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.get_service_attributes_response.GetServiceAttributesResponse":
        """<p>Returns the attributes associated with a specified service.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that you want to get attributes for. For services created in a namespace shared with your Amazon Web Services account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get service attributes using service ARN
            Gets service attributes using a service ARN instead of service ID, useful when working with shared namespaces. Shows attributes for a service created by a sharee in a namespace owned by another account.

            >>> client.get_service_attributes(service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678')
            GetServiceAttributes Example
            This example gets the attributes for a specified service.

            >>> client.get_service_attributes(service_id='srv-e4anhexample0004')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.get_service_attributes_request.GetServiceAttributesRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.get_service_attributes_response.GetServiceAttributesResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.get_service_attributes

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.get_service_attributes.get_service_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.get_service_attributes_request.GetServiceAttributesRequest = {
            "service_id": service_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_instances(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_servicediscovery.types.list_instances_response.ListInstancesResponse":
        """<p>Lists summary information about the instances that you registered by using a specified service.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that you want to list instances for. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            next_token: <p>For the first <code>ListInstances</code> request, omit this value.</p> <p>If more than <code>MaxResults</code> instances match the specified criteria, you can submit another <code>ListInstances</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p>
            max_results: <p>The maximum number of instances that you want Cloud Map to return in the response to a <code>ListInstances</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 instances.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: List service instances
            Example: List service instances

            >>> client.list_instances(service_id='srv-qzpwvt2tfqcegapy')
            List instances using service ARN for shared namespace
            This example lists instances using a service ARN instead of service ID. This is useful for listing instances associated with shared namespaces.

            >>> client.list_instances(service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.list_instances_request.ListInstancesRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.list_instances_response.ListInstancesResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.list_instances

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.list_instances.list_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.list_instances_request.ListInstancesRequest = {
            "service_id": service_id
        }
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

    def iter_list_instances(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_servicediscovery.types.list_instances_response.ListInstancesResponse]":
        _token = next_token
        while True:
            _response = self.list_instances(
                service_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_namespaces(
        self,
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_servicediscovery.types.namespace_filters.NamespaceFilters"
        ] = None,
    ) -> "capo_servicediscovery.types.list_namespaces_response.ListNamespacesResponse":
        """<p>Lists summary information about the namespaces that were created by the current Amazon Web Services account and shared with the current Amazon Web Services account.</p>

        Args:
            next_token: <p>For the first <code>ListNamespaces</code> request, omit this value.</p> <p>If the response contains <code>NextToken</code>, submit another <code>ListNamespaces</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> namespaces and then filters them based on the specified criteria. It's possible that no namespaces in the first <code>MaxResults</code> namespaces matched the specified criteria but that subsequent groups of <code>MaxResults</code> namespaces do contain namespaces that match the criteria.</p> </note>
            max_results: <p>The maximum number of namespaces that you want Cloud Map to return in the response to a <code>ListNamespaces</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 namespaces.</p>
            filters: <p>A complex type that contains specifications for the namespaces that you want to list.</p> <p>If you specify more than one filter, a namespace must match all filters to be returned by <code>ListNamespaces</code>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: List namespaces
            Example: List namespaces

            >>> client.list_namespaces()
            List namespaces filtered by resource owner
            This example shows how to list namespaces that are shared with you from other AWS accounts using the RESOURCE_OWNER filter.

            >>> client.list_namespaces(filters=[{'Name': 'RESOURCE_OWNER', 'Values': ['OTHER_ACCOUNTS']}])
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.list_namespaces

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.list_namespaces.list_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.list_namespaces_request.ListNamespacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_namespaces(
        self,
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_servicediscovery.types.namespace_filters.NamespaceFilters"
        ] = None,
    ) -> "Iterator[capo_servicediscovery.types.list_namespaces_response.ListNamespacesResponse]":
        _token = next_token
        while True:
            _response = self.list_namespaces(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_operations(
        self,
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_servicediscovery.types.operation_filters.OperationFilters"
        ] = None,
    ) -> "capo_servicediscovery.types.list_operations_response.ListOperationsResponse":
        """<p>Lists operations that match the criteria that you specify.</p>

        Args:
            next_token: <p>For the first <code>ListOperations</code> request, omit this value.</p> <p>If the response contains <code>NextToken</code>, submit another <code>ListOperations</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> operations and then filters them based on the specified criteria. It's possible that no operations in the first <code>MaxResults</code> operations matched the specified criteria but that subsequent groups of <code>MaxResults</code> operations do contain operations that match the criteria.</p> </note>
            max_results: <p>The maximum number of items that you want Cloud Map to return in the response to a <code>ListOperations</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 operations.</p>
            filters: <p>A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.</p> <p>If you specify more than one filter, an operation must match all filters to be returned by <code>ListOperations</code>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListOperations Example
            This example gets the operations that have a STATUS of either PENDING or SUCCESS.

            >>> client.list_operations(filters=[{'Name': 'STATUS', 'Condition': 'IN', 'Values': ['PENDING', 'SUCCESS']}])
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.list_operations_request.ListOperationsRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.list_operations_response.ListOperationsResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.list_operations

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.list_operations.list_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.list_operations_request.ListOperationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_operations(
        self,
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_servicediscovery.types.operation_filters.OperationFilters"
        ] = None,
    ) -> "Iterator[capo_servicediscovery.types.list_operations_response.ListOperationsResponse]":
        _token = next_token
        while True:
            _response = self.list_operations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services(
        self,
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_servicediscovery.types.service_filters.ServiceFilters"
        ] = None,
    ) -> "capo_servicediscovery.types.list_services_response.ListServicesResponse":
        """<p>Lists summary information for all the services that are associated with one or more namespaces.</p>

        Args:
            next_token: <p>For the first <code>ListServices</code> request, omit this value.</p> <p>If the response contains <code>NextToken</code>, submit another <code>ListServices</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> services and then filters them based on the specified criteria. It's possible that no services in the first <code>MaxResults</code> services matched the specified criteria but that subsequent groups of <code>MaxResults</code> services do contain services that match the criteria.</p> </note>
            max_results: <p>The maximum number of services that you want Cloud Map to return in the response to a <code>ListServices</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 services.</p>
            filters: <p>A complex type that contains specifications for the namespaces that you want to list services for. </p> <p>If you specify more than one filter, an operation must match all filters to be returned by <code>ListServices</code>.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: List services
            Example: List services

            >>> client.list_services()
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.list_services_response.ListServicesResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.list_services

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.list_services_request.ListServicesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_services(
        self,
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        next_token: Optional["capo_servicediscovery.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_servicediscovery.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_servicediscovery.types.service_filters.ServiceFilters"
        ] = None,
    ) -> "Iterator[capo_servicediscovery.types.list_services_response.ListServicesResponse]":
        _token = next_token
        while True:
            _response = self.list_services(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_servicediscovery.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to retrieve tags for.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation can't be completed because the resource was not found.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListTagsForResource example
            This example lists the tags of a resource.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:servicediscovery:us-east-1:123456789012:namespace/ns-ylexjili4cdxy3xm')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.list_tags_for_resource

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_instance(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        instance_id: "capo_servicediscovery.types.instance_id.InstanceId",
        attributes: "capo_servicediscovery.types.attributes.Attributes",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        creator_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_servicediscovery.types.register_instance_response.RegisterInstanceResponse":
        """<p>Creates or updates one or more records and, optionally, creates a health check based on the settings in a specified service. When you submit a <code>RegisterInstance</code> request, the following occurs:</p> <ul> <li> <p>For each DNS record that you define in the service that's specified by <code>ServiceId</code>, a record is created or updated in the hosted zone that's associated with the corresponding namespace.</p> </li> <li> <p>If the service includes <code>HealthCheckConfig</code>, a health check is created based on the settings in the health check configuration.</p> </li> <li> <p>The health check, if any, is associated with each of the new or updated records.</p> </li> </ul> <important> <p>One <code>RegisterInstance</code> request must complete before you can submit another request and specify the same service ID and instance ID.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html">CreateService</a>.</p> <p>When Cloud Map receives a DNS query for the specified DNS name, it returns the applicable value:</p> <ul> <li> <p> <b>If the health check is healthy</b>: returns all the records</p> </li> <li> <p> <b>If the health check is unhealthy</b>: returns the applicable value for the last healthy instance</p> </li> <li> <p> <b>If you didn't specify a health check configuration</b>: returns all the records</p> </li> </ul> <p>For the current quota on the number of instances that you can register using the same namespace and using the same service, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/cloud-map-limits.html">Cloud Map quotas</a> in the <i>Cloud Map Developer Guide</i>.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that you want to use for settings for the instance. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            instance_id: <p>An identifier that you want to associate with the instance. Note the following:</p> <ul> <li> <p>If the service that's specified by <code>ServiceId</code> includes settings for an <code>SRV</code> record, the value of <code>InstanceId</code> is automatically included as part of the value for the <code>SRV</code> record. For more information, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsRecord.html#cloudmap-Type-DnsRecord-Type">DnsRecord > Type</a>.</p> </li> <li> <p>You can use this value to update an existing instance.</p> </li> <li> <p>To register a new instance, you must specify a value that's unique among instances that you register by using the same service. </p> </li> <li> <p>If you specify an existing <code>InstanceId</code> and <code>ServiceId</code>, Cloud Map updates the existing DNS records, if any. If there's also an existing health check, Cloud Map deletes the old health check and creates a new one. </p> <note> <p>The health check isn't deleted immediately, so it will still appear for a while if you submit a <code>ListHealthChecks</code> request, for example.</p> </note> </li> </ul> <note> <p>Do not include sensitive information in <code>InstanceId</code> if the namespace is discoverable by public DNS queries and any <code>Type</code> member of <code>DnsRecord</code> for the service contains <code>SRV</code> because the <code>InstanceId</code> is discoverable by public DNS queries.</p> </note>
            creator_request_id: <p>A unique string that identifies the request and that allows failed <code>RegisterInstance</code> requests to be retried without the risk of executing the operation twice. You must use a unique <code>CreatorRequestId</code> string every time you submit a <code>RegisterInstance</code> request if you're registering additional instances for the same namespace and service. <code>CreatorRequestId</code> can be any unique string (for example, a date/time stamp).</p>
            attributes: <p>A string map that contains the following information for the service that you specify in <code>ServiceId</code>:</p> <ul> <li> <p>The attributes that apply to the records that are defined in the service. </p> </li> <li> <p>For each attribute, the applicable value.</p> </li> </ul> <important> <p>Do not include sensitive information in the attributes if the namespace is discoverable by public DNS queries.</p> </important> <p>The following are the supported attribute keys.</p> <dl> <dt>AWS_ALIAS_DNS_NAME</dt> <dd> <p>If you want Cloud Map to create an Amazon Route 53 alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that's associated with the load balancer. For information about how to get the DNS name, see "DNSName" in the topic <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html">AliasTarget</a> in the <i>Route 53 API Reference</i>.</p> <p>Note the following:</p> <ul> <li> <p>The configuration for the service that's specified by <code>ServiceId</code> must include settings for an <code>A</code> record, an <code>AAAA</code> record, or both.</p> </li> <li> <p>In the service that's specified by <code>ServiceId</code>, the value of <code>RoutingPolicy</code> must be <code>WEIGHTED</code>.</p> </li> <li> <p>If the service that's specified by <code>ServiceId</code> includes <code>HealthCheckConfig</code> settings, Cloud Map will create the Route 53 health check, but it doesn't associate the health check with the alias record.</p> </li> <li> <p>Cloud Map currently doesn't support creating alias records that route traffic to Amazon Web Services resources other than Elastic Load Balancing load balancers.</p> </li> <li> <p>If you specify a value for <code>AWS_ALIAS_DNS_NAME</code>, don't specify values for any of the <code>AWS_INSTANCE</code> attributes.</p> </li> <li> <p>The <code>AWS_ALIAS_DNS_NAME</code> is not supported in the GovCloud (US) Regions.</p> </li> </ul> </dd> <dt>AWS_EC2_INSTANCE_ID</dt> <dd> <p> <i>HTTP namespaces only.</i> The Amazon EC2 instance ID for the instance. If the <code>AWS_EC2_INSTANCE_ID</code> attribute is specified, then the only other attribute that can be specified is <code>AWS_INIT_HEALTH_STATUS</code>. When the <code>AWS_EC2_INSTANCE_ID</code> attribute is specified, then the <code>AWS_INSTANCE_IPV4</code> attribute will be filled out with the primary private IPv4 address.</p> </dd> <dt>AWS_INIT_HEALTH_STATUS</dt> <dd> <p>If the service configuration includes <code>HealthCheckCustomConfig</code>, you can optionally use <code>AWS_INIT_HEALTH_STATUS</code> to specify the initial status of the custom health check, <code>HEALTHY</code> or <code>UNHEALTHY</code>. If you don't specify a value for <code>AWS_INIT_HEALTH_STATUS</code>, the initial status is <code>HEALTHY</code>.</p> </dd> <dt>AWS_INSTANCE_CNAME</dt> <dd> <p>If the service configuration includes a <code>CNAME</code> record, the domain name that you want Route 53 to return in response to DNS queries (for example, <code>example.com</code>).</p> <p>This value is required if the service specified by <code>ServiceId</code> includes settings for an <code>CNAME</code> record.</p> </dd> <dt>AWS_INSTANCE_IPV4</dt> <dd> <p>If the service configuration includes an <code>A</code> record, the IPv4 address that you want Route 53 to return in response to DNS queries (for example, <code>192.0.2.44</code>).</p> <p>This value is required if the service specified by <code>ServiceId</code> includes settings for an <code>A</code> record. If the service includes settings for an <code>SRV</code> record, you must specify a value for <code>AWS_INSTANCE_IPV4</code>, <code>AWS_INSTANCE_IPV6</code>, or both.</p> </dd> <dt>AWS_INSTANCE_IPV6</dt> <dd> <p>If the service configuration includes an <code>AAAA</code> record, the IPv6 address that you want Route 53 to return in response to DNS queries (for example, <code>2001:0db8:85a3:0000:0000:abcd:0001:2345</code>).</p> <p>This value is required if the service specified by <code>ServiceId</code> includes settings for an <code>AAAA</code> record. If the service includes settings for an <code>SRV</code> record, you must specify a value for <code>AWS_INSTANCE_IPV4</code>, <code>AWS_INSTANCE_IPV6</code>, or both.</p> </dd> <dt>AWS_INSTANCE_PORT</dt> <dd> <p>If the service includes an <code>SRV</code> record, the value that you want Route 53 to return for the port.</p> <p>If the service includes <code>HealthCheckConfig</code>, the port on the endpoint that you want Route 53 to send requests to. </p> <p>This value is required if you specified settings for an <code>SRV</code> record or a Route 53 health check when you created the service.</p> </dd> <dt>Custom attributes</dt> <dd> <p>You can add up to 30 custom attributes. For each key-value pair, the maximum length of the attribute name is 255 characters, and the maximum length of the attribute value is 1,024 characters. The total size of all provided attributes (sum of all keys and values) must not exceed 5,000 characters.</p> </dd> </dl>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.resource_in_use.ResourceInUse: <p>The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.</p>
            capo_servicediscovery.errors.resource_limit_exceeded.ResourceLimitExceeded: <p>The resource can't be created because you've reached the quota on the number of resources.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example: Register Instance
            Example: Register Instance

            >>> client.register_instance(service_id='srv-p5zdwlg5uvvzjita', instance_id='myservice-53', attributes={'AWS_INSTANCE_IPV4': '172.2.1.3', 'AWS_INSTANCE_PORT': '808'}, creator_request_id='7a48a98a-72e6-4849-bfa7-1a458e030d7b')
            Register instance using service ARN
            Registers an instance using a service ARN instead of service ID, useful when working with shared namespaces. Shows registering an instance to a service created by a sharee in a namespace owned by another account.

            >>> client.register_instance(instance_id='i-abcd1234xmpl5678', service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678', attributes={'AWS_INSTANCE_IPV4': '192.0.2.44', 'AWS_INSTANCE_PORT': '80'})
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.register_instance_request.RegisterInstanceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.register_instance_response.RegisterInstanceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.register_instance

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.register_instance.register_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.register_instance_request.RegisterInstanceRequest = {
            "service_id": service_id,
            "instance_id": instance_id,
            "attributes": attributes,
        }
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_servicediscovery.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_servicediscovery.types.tag_list.TagList",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to retrieve tags for.</p>
            tags: <p>The tags to add to the specified resource. Specifying the tag key is required. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation can't be completed because the resource was not found.</p>
            capo_servicediscovery.errors.too_many_tags_exception.TooManyTagsException: <p>The list of tags on the resource is over the quota. The maximum number of tags that can be applied to a resource is 50.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            TagResource example
            This example adds "Department" and "Project" tags to a resource.

            >>> client.tag_resource(resource_arn='arn:aws:servicediscovery:us-east-1:123456789012:namespace/ns-ylexjili4cdxy3xm', tags=[{'Key': 'Department', 'Value': 'Engineering'}, {'Key': 'Project', 'Value': 'Zeta'}])
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.tag_resource

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_servicediscovery.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_servicediscovery.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to retrieve tags for.</p>
            tag_keys: <p>The tag keys to remove from the specified resource.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation can't be completed because the resource was not found.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UntagResource example
            This example removes the "Department" and "Project" tags from a resource.

            >>> client.untag_resource(resource_arn='arn:aws:servicediscovery:us-east-1:123456789012:namespace/ns-ylexjili4cdxy3xm', tag_keys=['Project', 'Department'])
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.untag_resource

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_http_namespace(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        namespace: "capo_servicediscovery.types.http_namespace_change.HttpNamespaceChange",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        updater_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse":
        """<p>Updates an HTTP namespace.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the namespace that you want to update.</p>
            updater_request_id: <p>A unique string that identifies the request and that allows failed <code>UpdateHttpNamespace</code> requests to be retried without the risk of running the operation twice. <code>UpdaterRequestId</code> can be any unique string (for example, a date/timestamp).</p>
            namespace: <p>Updated properties for the the HTTP namespace.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.resource_in_use.ResourceInUse: <p>The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a HTTP namespace
            The following example updates the description of a HTTP namespace.

            >>> client.update_http_namespace(id='ns-vh4nbmEXAMPLE', namespace={'Description': 'The updated namespace description.'})
            Update HTTP namespace using namespace ARN for shared namespace
            This example updates an HTTP namespace using a namespace ARN instead of namespace ID.

            >>> client.update_http_namespace(id='arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-vh4nbmexample', namespace={'Description': 'Updated description for shared HTTP namespace.'})
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.update_http_namespace_request.UpdateHttpNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.update_http_namespace_response.UpdateHttpNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.update_http_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.update_http_namespace.update_http_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.update_http_namespace_request.UpdateHttpNamespaceRequest = {
            "id": id,
            "namespace": namespace,
        }
        if updater_request_id is None:
            updater_request_id = str(uuid.uuid4())
        input_["updater_request_id"] = updater_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_instance_custom_health_status(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        instance_id: "capo_servicediscovery.types.resource_id.ResourceId",
        status: "capo_servicediscovery.types.custom_health_status.CustomHealthStatus",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> None:
        """<p>Submits a request to change the health status of a custom health check to healthy or unhealthy.</p> <p>You can use <code>UpdateInstanceCustomHealthStatus</code> to change the status only for custom health checks, which you define using <code>HealthCheckCustomConfig</code> when you create a service. You can't use it to change the status for Route 53 health checks, which you define using <code>HealthCheckConfig</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html">HealthCheckCustomConfig</a>.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that includes the configuration for the custom health check that you want to change the status for. For services created in a shared namespace, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>
            instance_id: <p>The ID of the instance that you want to change the health status for.</p>
            status: <p>The new status of the instance, <code>HEALTHY</code> or <code>UNHEALTHY</code>.</p>

        Raises:
            capo_servicediscovery.errors.custom_health_not_found.CustomHealthNotFound: <p>The health check for the instance that's specified by <code>ServiceId</code> and <code>InstanceId</code> isn't a custom health check. </p>
            capo_servicediscovery.errors.instance_not_found.InstanceNotFound: <p>No instance exists with the specified ID, or the instance was recently registered, and information about the instance hasn't propagated yet.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update instance custom health status using service ARN
            Updates instance custom health status using a service ARN instead of service ID, useful when working with shared namespaces.

            >>> client.update_instance_custom_health_status(instance_id='i-abcd1234xmpl5678', service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678', status='HEALTHY')
            UpdateInstanceCustomHealthStatus Example
            This example submits a request to change the health status of an instance associated with a service with a custom health check to HEALTHY.

            >>> client.update_instance_custom_health_status(instance_id='i-abcd1234', service_id='srv-e4anhexample0004', status='HEALTHY')
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.update_instance_custom_health_status_request.UpdateInstanceCustomHealthStatusRequest]",
        ) -> OperationResponse[None]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.update_instance_custom_health_status

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.update_instance_custom_health_status.update_instance_custom_health_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.update_instance_custom_health_status_request.UpdateInstanceCustomHealthStatusRequest = {
            "service_id": service_id,
            "instance_id": instance_id,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_private_dns_namespace(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        namespace: "capo_servicediscovery.types.private_dns_namespace_change.PrivateDnsNamespaceChange",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        updater_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_servicediscovery.types.update_private_dns_namespace_response.UpdatePrivateDnsNamespaceResponse":
        """<p>Updates a private DNS namespace.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the namespace that you want to update.</p>
            updater_request_id: <p>A unique string that identifies the request and that allows failed <code>UpdatePrivateDnsNamespace</code> requests to be retried without the risk of running the operation twice. <code>UpdaterRequestId</code> can be any unique string (for example, a date/timestamp).</p>
            namespace: <p>Updated properties for the private DNS namespace.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.resource_in_use.ResourceInUse: <p>The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a private DNS namespace
            The following example updates the description of a private DNS namespace.

            >>> client.update_private_dns_namespace(id='ns-bk3aEXAMPLE', updater_request_id='', namespace={'Description': 'The updated namespace description.'})
            Update private DNS namespace using namespace ARN for shared namespace
            This example updates a private DNS namespace using a namespace ARN instead of namespace ID.

            >>> client.update_private_dns_namespace(id='arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-bk3aexample', namespace={'Description': 'Updated description for shared private DNS namespace.'})
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.update_private_dns_namespace_request.UpdatePrivateDnsNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.update_private_dns_namespace_response.UpdatePrivateDnsNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.update_private_dns_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.update_private_dns_namespace.update_private_dns_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.update_private_dns_namespace_request.UpdatePrivateDnsNamespaceRequest = {
            "id": id,
            "namespace": namespace,
        }
        if updater_request_id is None:
            updater_request_id = str(uuid.uuid4())
        input_["updater_request_id"] = updater_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_public_dns_namespace(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        namespace: "capo_servicediscovery.types.public_dns_namespace_change.PublicDnsNamespaceChange",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
        updater_request_id: Optional[
            "capo_servicediscovery.types.resource_id.ResourceId"
        ] = None,
    ) -> "capo_servicediscovery.types.update_public_dns_namespace_response.UpdatePublicDnsNamespaceResponse":
        """<p>Updates a public DNS namespace.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the namespace being updated.</p>
            updater_request_id: <p>A unique string that identifies the request and that allows failed <code>UpdatePublicDnsNamespace</code> requests to be retried without the risk of running the operation twice. <code>UpdaterRequestId</code> can be any unique string (for example, a date/timestamp).</p>
            namespace: <p>Updated properties for the public DNS namespace.</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.namespace_not_found.NamespaceNotFound: <p>No namespace exists with the specified ID.</p>
            capo_servicediscovery.errors.resource_in_use.ResourceInUse: <p>The specified resource can't be deleted because it contains other resources. For example, you can't delete a service that contains any instances.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a public DNS namespace
            The following example updates the description of a public DNS namespace.

            >>> client.update_public_dns_namespace(id='ns-bk3aEXAMPLE', updater_request_id='', namespace={'Description': 'The updated namespace description.'})
            Update public DNS namespace using namespace ARN for shared namespace
            This example updates a public DNS namespace using a namespace ARN instead of namespace ID.

            >>> client.update_public_dns_namespace(id='arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-bk3aexample', namespace={'Description': 'Updated description for shared public DNS namespace.'})
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.update_public_dns_namespace_request.UpdatePublicDnsNamespaceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.update_public_dns_namespace_response.UpdatePublicDnsNamespaceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.update_public_dns_namespace

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.update_public_dns_namespace.update_public_dns_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.update_public_dns_namespace_request.UpdatePublicDnsNamespaceRequest = {
            "id": id,
            "namespace": namespace,
        }
        if updater_request_id is None:
            updater_request_id = str(uuid.uuid4())
        input_["updater_request_id"] = updater_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service(
        self,
        id: "capo_servicediscovery.types.arn.Arn",
        service: "capo_servicediscovery.types.service_change.ServiceChange",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.update_service_response.UpdateServiceResponse":
        """<p>Submits a request to perform the following operations:</p> <ul> <li> <p>Update the TTL setting for existing <code>DnsRecords</code> configurations</p> </li> <li> <p>Add, update, or delete <code>HealthCheckConfig</code> for a specified service</p> <note> <p>You can't add, update, or delete a <code>HealthCheckCustomConfig</code> configuration.</p> </note> </li> </ul> <p>For public and private DNS namespaces, note the following:</p> <ul> <li> <p>If you omit any existing <code>DnsRecords</code> or <code>HealthCheckConfig</code> configurations from an <code>UpdateService</code> request, the configurations are deleted from the service.</p> </li> <li> <p>If you omit an existing <code>HealthCheckCustomConfig</code> configuration from an <code>UpdateService</code> request, the configuration isn't deleted from the service.</p> </li> </ul> <note> <p>You can't call <code>UpdateService</code> and update settings in the following scenarios:</p> <ul> <li> <p>When the service is associated with an HTTP namespace</p> </li> <li> <p>When the service is associated with a shared namespace and contains instances that were registered by Amazon Web Services accounts other than the account making the <code>UpdateService</code> call</p> </li> </ul> </note> <p>When you update settings for a service, Cloud Map also updates the corresponding settings in all the records and health checks that were created by using the specified service.</p>

        Args:
            id: <p>The ID or Amazon Resource Name (ARN) of the service that you want to update. If the namespace associated with the service is shared with your Amazon Web Services account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i> </p>
            service: <p>A complex type that contains the new settings for the service. You can specify a maximum of 30 attributes (key-value pairs).</p>

        Raises:
            capo_servicediscovery.errors.duplicate_request.DuplicateRequest: <p>The operation is already in progress.</p>
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateService Example
            This example submits a request to replace the DnsConfig and HealthCheckConfig settings of a specified service.

            >>> client.update_service(id='srv-e4anhexample0004', service={'HealthCheckConfig': {'Type': 'HTTP', 'ResourcePath': '/', 'FailureThreshold': 2}, 'DnsConfig': {'DnsRecords': [{'Type': 'A', 'TTL': 60}]}})
            Update service using service ARN for shared namespace
            This example updates a service using a service ARN instead of service ID. This is useful for updating services associated with shared namespaces.

            >>> client.update_service(id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004', service={'Description': 'Updated service description for shared namespace'})
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.update_service

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.update_service_request.UpdateServiceRequest = {
            "id": id,
            "service": service,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_attributes(
        self,
        service_id: "capo_servicediscovery.types.arn.Arn",
        attributes: "capo_servicediscovery.types.service_attributes_map.ServiceAttributesMap",
        *,
        config_overrides: Optional[ServiceDiscoveryClientConfig] = None,
    ) -> "capo_servicediscovery.types.update_service_attributes_response.UpdateServiceAttributesResponse":
        """<p>Submits a request to update a specified service to add service-level attributes.</p>

        Args:
            service_id: <p>The ID or Amazon Resource Name (ARN) of the service that you want to update. For services created in a namespace shared with your Amazon Web Services account, specify the service ARN.</p>
            attributes: <p>A string map that contains attribute key-value pairs.</p>

        Raises:
            capo_servicediscovery.errors.invalid_input.InvalidInput: <p>One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.</p>
            capo_servicediscovery.errors.service_attributes_limit_exceeded_exception.ServiceAttributesLimitExceededException: <p>The attribute can't be added to the service because you've exceeded the quota for the number of attributes you can add to a service.</p>
            capo_servicediscovery.errors.service_not_found.ServiceNotFound: <p>No service exists with the specified ID.</p>
            capo_servicediscovery.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update service attributes using service ARN
            Updates service attributes using a service ARN instead of service ID, useful when working with shared namespaces.

            >>> client.update_service_attributes(service_id='arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678', attributes={'Port': '8080', 'Protocol': 'HTTP'})
            UpdateServiceAttributes Example
            This example submits a request to update the specified service to add a port attribute with the value 80.

            >>> client.update_service_attributes(service_id='srv-e4anhexample0004', attributes={'port': '80'})
        """

        def _handler(
            req: "OperationRequest[capo_servicediscovery.types.update_service_attributes_request.UpdateServiceAttributesRequest]",
        ) -> OperationResponse[
            "capo_servicediscovery.types.update_service_attributes_response.UpdateServiceAttributesResponse"
        ]:
            import capo_servicediscovery._operations.route53_auto_naming_v20170314.update_service_attributes

            output, http_response = (
                capo_servicediscovery._operations.route53_auto_naming_v20170314.update_service_attributes.update_service_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_servicediscovery.types.update_service_attributes_request.UpdateServiceAttributesRequest = {
            "service_id": service_id,
            "attributes": attributes,
        }

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
