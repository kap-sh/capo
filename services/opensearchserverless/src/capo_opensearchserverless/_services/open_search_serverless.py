"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#OpenSearchServerless``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_opensearchserverless._auth._signers
import capo_opensearchserverless._auth._sigv4
from capo_opensearchserverless._auth._identity import Credentials
from capo_opensearchserverless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_opensearchserverless._auth._zapros_handler import AuthMiddleware
from capo_opensearchserverless._pagination import resolve_path as _resolve_path
from capo_opensearchserverless._resources.open_search_serverless.access_policy import (
    AccessPolicy,
)
from capo_opensearchserverless._resources.open_search_serverless.collection import (
    Collection,
)
from capo_opensearchserverless._resources.open_search_serverless.collection_group import (
    CollectionGroup,
)
from capo_opensearchserverless._resources.open_search_serverless.index import Index
from capo_opensearchserverless._resources.open_search_serverless.lifecycle_policy import (
    LifecyclePolicy,
)
from capo_opensearchserverless._resources.open_search_serverless.security_config import (
    SecurityConfig,
)
from capo_opensearchserverless._resources.open_search_serverless.security_policy import (
    SecurityPolicy,
)
from capo_opensearchserverless._resources.open_search_serverless.vpc_endpoint import (
    VpcEndpoint,
)
from capo_opensearchserverless._services._aws_config import aws_config
from capo_opensearchserverless._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_opensearchserverless.types.access_policy_type
    import capo_opensearchserverless.types.arn
    import capo_opensearchserverless.types.batch_get_collection_group_request
    import capo_opensearchserverless.types.batch_get_collection_group_response
    import capo_opensearchserverless.types.batch_get_collection_request
    import capo_opensearchserverless.types.batch_get_collection_response
    import capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_request
    import capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_response
    import capo_opensearchserverless.types.batch_get_lifecycle_policy_request
    import capo_opensearchserverless.types.batch_get_lifecycle_policy_response
    import capo_opensearchserverless.types.batch_get_vpc_endpoint_request
    import capo_opensearchserverless.types.batch_get_vpc_endpoint_response
    import capo_opensearchserverless.types.capacity_limits
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_filters
    import capo_opensearchserverless.types.collection_group_capacity_limits
    import capo_opensearchserverless.types.collection_group_id
    import capo_opensearchserverless.types.collection_group_ids
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.collection_group_names
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.collection_ids
    import capo_opensearchserverless.types.collection_name
    import capo_opensearchserverless.types.collection_names
    import capo_opensearchserverless.types.collection_type
    import capo_opensearchserverless.types.config_description
    import capo_opensearchserverless.types.config_name
    import capo_opensearchserverless.types.create_access_policy_request
    import capo_opensearchserverless.types.create_access_policy_response
    import capo_opensearchserverless.types.create_collection_group_request
    import capo_opensearchserverless.types.create_collection_group_response
    import capo_opensearchserverless.types.create_collection_request
    import capo_opensearchserverless.types.create_collection_response
    import capo_opensearchserverless.types.create_iam_identity_center_config_options
    import capo_opensearchserverless.types.create_index_request
    import capo_opensearchserverless.types.create_index_response
    import capo_opensearchserverless.types.create_lifecycle_policy_request
    import capo_opensearchserverless.types.create_lifecycle_policy_response
    import capo_opensearchserverless.types.create_security_config_request
    import capo_opensearchserverless.types.create_security_config_response
    import capo_opensearchserverless.types.create_security_policy_request
    import capo_opensearchserverless.types.create_security_policy_response
    import capo_opensearchserverless.types.create_vpc_endpoint_request
    import capo_opensearchserverless.types.create_vpc_endpoint_response
    import capo_opensearchserverless.types.delete_access_policy_request
    import capo_opensearchserverless.types.delete_access_policy_response
    import capo_opensearchserverless.types.delete_collection_group_request
    import capo_opensearchserverless.types.delete_collection_group_response
    import capo_opensearchserverless.types.delete_collection_request
    import capo_opensearchserverless.types.delete_collection_response
    import capo_opensearchserverless.types.delete_index_request
    import capo_opensearchserverless.types.delete_index_response
    import capo_opensearchserverless.types.delete_lifecycle_policy_request
    import capo_opensearchserverless.types.delete_lifecycle_policy_response
    import capo_opensearchserverless.types.delete_security_config_request
    import capo_opensearchserverless.types.delete_security_config_response
    import capo_opensearchserverless.types.delete_security_policy_request
    import capo_opensearchserverless.types.delete_security_policy_response
    import capo_opensearchserverless.types.delete_vpc_endpoint_request
    import capo_opensearchserverless.types.delete_vpc_endpoint_response
    import capo_opensearchserverless.types.deletion_protection
    import capo_opensearchserverless.types.encryption_config
    import capo_opensearchserverless.types.get_access_policy_request
    import capo_opensearchserverless.types.get_access_policy_response
    import capo_opensearchserverless.types.get_account_settings_request
    import capo_opensearchserverless.types.get_account_settings_response
    import capo_opensearchserverless.types.get_index_request
    import capo_opensearchserverless.types.get_index_response
    import capo_opensearchserverless.types.get_policies_stats_request
    import capo_opensearchserverless.types.get_policies_stats_response
    import capo_opensearchserverless.types.get_security_config_request
    import capo_opensearchserverless.types.get_security_config_response
    import capo_opensearchserverless.types.get_security_policy_request
    import capo_opensearchserverless.types.get_security_policy_response
    import capo_opensearchserverless.types.iam_federation_config_options
    import capo_opensearchserverless.types.index_name
    import capo_opensearchserverless.types.index_schema
    import capo_opensearchserverless.types.lifecycle_policy_identifiers
    import capo_opensearchserverless.types.lifecycle_policy_resource_identifiers
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.lifecycle_resource_filter
    import capo_opensearchserverless.types.list_access_policies_request
    import capo_opensearchserverless.types.list_access_policies_response
    import capo_opensearchserverless.types.list_collection_groups_request
    import capo_opensearchserverless.types.list_collection_groups_response
    import capo_opensearchserverless.types.list_collections_request
    import capo_opensearchserverless.types.list_collections_response
    import capo_opensearchserverless.types.list_lifecycle_policies_request
    import capo_opensearchserverless.types.list_lifecycle_policies_response
    import capo_opensearchserverless.types.list_security_configs_request
    import capo_opensearchserverless.types.list_security_configs_response
    import capo_opensearchserverless.types.list_security_policies_request
    import capo_opensearchserverless.types.list_security_policies_response
    import capo_opensearchserverless.types.list_tags_for_resource_request
    import capo_opensearchserverless.types.list_tags_for_resource_response
    import capo_opensearchserverless.types.list_vpc_endpoints_request
    import capo_opensearchserverless.types.list_vpc_endpoints_response
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_document
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.policy_version
    import capo_opensearchserverless.types.resource_filter
    import capo_opensearchserverless.types.saml_config_options
    import capo_opensearchserverless.types.security_config_id
    import capo_opensearchserverless.types.security_config_type
    import capo_opensearchserverless.types.security_group_ids
    import capo_opensearchserverless.types.security_policy_type
    import capo_opensearchserverless.types.serverless_generation
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.subnet_ids
    import capo_opensearchserverless.types.tag_keys
    import capo_opensearchserverless.types.tag_resource_request
    import capo_opensearchserverless.types.tag_resource_response
    import capo_opensearchserverless.types.tags
    import capo_opensearchserverless.types.untag_resource_request
    import capo_opensearchserverless.types.untag_resource_response
    import capo_opensearchserverless.types.update_access_policy_request
    import capo_opensearchserverless.types.update_access_policy_response
    import capo_opensearchserverless.types.update_account_settings_request
    import capo_opensearchserverless.types.update_account_settings_response
    import capo_opensearchserverless.types.update_collection_group_request
    import capo_opensearchserverless.types.update_collection_group_response
    import capo_opensearchserverless.types.update_collection_request
    import capo_opensearchserverless.types.update_collection_response
    import capo_opensearchserverless.types.update_iam_identity_center_config_options
    import capo_opensearchserverless.types.update_index_request
    import capo_opensearchserverless.types.update_index_response
    import capo_opensearchserverless.types.update_lifecycle_policy_request
    import capo_opensearchserverless.types.update_lifecycle_policy_response
    import capo_opensearchserverless.types.update_security_config_request
    import capo_opensearchserverless.types.update_security_config_response
    import capo_opensearchserverless.types.update_security_policy_request
    import capo_opensearchserverless.types.update_security_policy_response
    import capo_opensearchserverless.types.update_vpc_endpoint_request
    import capo_opensearchserverless.types.update_vpc_endpoint_response
    import capo_opensearchserverless.types.vector_options
    import capo_opensearchserverless.types.vpc_endpoint_filters
    import capo_opensearchserverless.types.vpc_endpoint_id
    import capo_opensearchserverless.types.vpc_endpoint_ids
    import capo_opensearchserverless.types.vpc_endpoint_name
    import capo_opensearchserverless.types.vpc_id


class OpenSearchServerlessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class OpenSearchServerlessClient:
    """A client for the ``OpenSearchServerless`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = OpenSearchServerlessClientConfig(
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
        self.access_policy = AccessPolicy(self)
        self.collection = Collection(self)
        self.collection_group = CollectionGroup(self)
        self.index = Index(self)
        self.lifecycle_policy = LifecyclePolicy(self)
        self.security_config = SecurityConfig(self)
        self.security_policy = SecurityPolicy(self)
        self.vpc_endpoint = VpcEndpoint(self)

    def operation_options(
        self, config_overrides: Optional[OpenSearchServerlessClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: OpenSearchServerlessClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def batch_get_collection(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        ids: Optional[
            "capo_opensearchserverless.types.collection_ids.CollectionIds"
        ] = None,
        names: Optional[
            "capo_opensearchserverless.types.collection_names.CollectionNames"
        ] = None,
    ) -> "capo_opensearchserverless.types.batch_get_collection_response.BatchGetCollectionResponse":
        """<p>Returns attributes for one or more collections, including the collection endpoint, the OpenSearch Dashboards endpoint, and FIPS-compliant endpoints. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            ids: <p>A list of collection IDs. You can't provide names and IDs in the same request. The ID is part of the collection endpoint. You can also retrieve it using the <a href="https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html">ListCollections</a> API.</p>
            names: <p>A list of collection names. You can't provide names and IDs in the same request.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.batch_get_collection_request.BatchGetCollectionRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.batch_get_collection_response.BatchGetCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_collection

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.batch_get_collection.batch_get_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_collection_request.BatchGetCollectionRequest = {}
        if ids is not None:
            input_["ids"] = ids
        if names is not None:
            input_["names"] = names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_collection_group(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        ids: Optional[
            "capo_opensearchserverless.types.collection_group_ids.CollectionGroupIds"
        ] = None,
        names: Optional[
            "capo_opensearchserverless.types.collection_group_names.CollectionGroupNames"
        ] = None,
    ) -> "capo_opensearchserverless.types.batch_get_collection_group_response.BatchGetCollectionGroupResponse":
        """<p>Returns attributes for one or more collection groups, including capacity limits and the number of collections in each group. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            ids: <p>A list of collection group IDs. You can't provide names and IDs in the same request.</p>
            names: <p>A list of collection group names. You can't provide names and IDs in the same request.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.batch_get_collection_group_request.BatchGetCollectionGroupRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.batch_get_collection_group_response.BatchGetCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_collection_group

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.batch_get_collection_group.batch_get_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_collection_group_request.BatchGetCollectionGroupRequest = {}
        if ids is not None:
            input_["ids"] = ids
        if names is not None:
            input_["names"] = names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_effective_lifecycle_policy(
        self,
        resource_identifiers: "capo_opensearchserverless.types.lifecycle_policy_resource_identifiers.LifecyclePolicyResourceIdentifiers",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_response.BatchGetEffectiveLifecyclePolicyResponse":
        """<p>Returns a list of successful and failed retrievals for the OpenSearch Serverless indexes. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list">Viewing data lifecycle policies</a>.</p>

        Args:
            resource_identifiers: <p>The unique identifiers of policy types and resource names.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_request.BatchGetEffectiveLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_response.BatchGetEffectiveLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_effective_lifecycle_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.batch_get_effective_lifecycle_policy.batch_get_effective_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_request.BatchGetEffectiveLifecyclePolicyRequest = {
            "resource_identifiers": resource_identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_lifecycle_policy(
        self,
        identifiers: "capo_opensearchserverless.types.lifecycle_policy_identifiers.LifecyclePolicyIdentifiers",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.batch_get_lifecycle_policy_response.BatchGetLifecyclePolicyResponse":
        """<p>Returns one or more configured OpenSearch Serverless lifecycle policies. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list">Viewing data lifecycle policies</a>.</p>

        Args:
            identifiers: <p>The unique identifiers of policy types and policy names.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.batch_get_lifecycle_policy_request.BatchGetLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.batch_get_lifecycle_policy_response.BatchGetLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_lifecycle_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.batch_get_lifecycle_policy.batch_get_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_lifecycle_policy_request.BatchGetLifecyclePolicyRequest = {
            "identifiers": identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_vpc_endpoint(
        self,
        ids: "capo_opensearchserverless.types.vpc_endpoint_ids.VpcEndpointIds",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.batch_get_vpc_endpoint_response.BatchGetVpcEndpointResponse":
        """<p>Returns attributes for one or more VPC endpoints associated with the current account. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            ids: <p>A list of VPC endpoint identifiers.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.batch_get_vpc_endpoint_request.BatchGetVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.batch_get_vpc_endpoint_response.BatchGetVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_vpc_endpoint

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.batch_get_vpc_endpoint.batch_get_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_vpc_endpoint_request.BatchGetVpcEndpointRequest = {
            "ids": ids
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_lifecycle_policy(
        self,
        type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy: "capo_opensearchserverless.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse":
        """<p>Creates a lifecyle policy to be applied to OpenSearch Serverless indexes. Lifecycle policies define the number of days or hours to retain the data on an OpenSearch Serverless index. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-create">Creating data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            name: <p>The name of the lifecycle policy.</p>
            description: <p>A description of the lifecycle policy.</p>
            policy: <p>The JSON policy document to use as the content for the lifecycle policy.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_lifecycle_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_lifecycle_policy.create_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest = {
            "type": type,
            "name": name,
            "policy": policy,
        }
        if description is not None:
            input_["description"] = description
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

    def create_security_policy(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy: "capo_opensearchserverless.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_security_policy_response.CreateSecurityPolicyResponse":
        """<p>Creates a security policy to be used by one or more OpenSearch Serverless collections. Security policies provide access to a collection and its OpenSearch Dashboards endpoint from public networks or specific VPC endpoints. They also allow you to secure a collection with a KMS encryption key. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html">Network access for Amazon OpenSearch Serverless</a> and <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the policy.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_security_policy_request.CreateSecurityPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_security_policy_response.CreateSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_security_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_security_policy.create_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_security_policy_request.CreateSecurityPolicyRequest = {
            "type": type,
            "name": name,
            "policy": policy,
        }
        if description is not None:
            input_["description"] = description
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

    def get_account_settings(
        self, *, config_overrides: Optional[OpenSearchServerlessClientConfig] = None
    ) -> "capo_opensearchserverless.types.get_account_settings_response.GetAccountSettingsResponse":
        """<p>Returns account-level settings related to OpenSearch Serverless.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_account_settings

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_account_settings_request.GetAccountSettingsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policies_stats(
        self, *, config_overrides: Optional[OpenSearchServerlessClientConfig] = None
    ) -> "capo_opensearchserverless.types.get_policies_stats_response.GetPoliciesStatsResponse":
        """<p>Returns statistical information about your OpenSearch Serverless access policies, security configurations, and security policies.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_policies_stats_request.GetPoliciesStatsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_policies_stats_response.GetPoliciesStatsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_policies_stats

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_policies_stats.get_policies_stats(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_policies_stats_request.GetPoliciesStatsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_opensearchserverless.types.arn.Arn",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the tags for an OpenSearch Serverless resource. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_tags_for_resource

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_opensearchserverless.types.arn.Arn",
        tags: "capo_opensearchserverless.types.tags.Tags",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.tag_resource_response.TagResourceResponse":
        """<p>Associates tags with an OpenSearch Serverless resource. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>
            tags: <p>A list of tags (key-value pairs) to add to the resource. All tag keys in the request must be unique.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.tag_resource

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_opensearchserverless.types.arn.Arn",
        tag_keys: "capo_opensearchserverless.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> (
        "capo_opensearchserverless.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Removes a tag or set of tags from an OpenSearch Serverless resource. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>
            tag_keys: <p>The tag or set of tags to remove from the resource. All tag keys in the request must be unique.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.untag_resource

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.untag_resource_request.UntagResourceRequest = {
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

    def update_account_settings(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.capacity_limits.CapacityLimits"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_account_settings_response.UpdateAccountSettingsResponse":
        """<p>Update the OpenSearch Serverless settings for the current Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html">Managing capacity limits for Amazon OpenSearch Serverless</a>.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_account_settings_request.UpdateAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_account_settings_response.UpdateAccountSettingsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_account_settings

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_account_settings.update_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_account_settings_request.UpdateAccountSettingsRequest = {}
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vpc_endpoint(
        self,
        id: "capo_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        add_subnet_ids: Optional[
            "capo_opensearchserverless.types.subnet_ids.SubnetIds"
        ] = None,
        remove_subnet_ids: Optional[
            "capo_opensearchserverless.types.subnet_ids.SubnetIds"
        ] = None,
        add_security_group_ids: Optional[
            "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        remove_security_group_ids: Optional[
            "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse":
        """<p>Updates an OpenSearch Serverless-managed interface endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The unique identifier of the interface endpoint to update.</p>
            add_subnet_ids: <p>The ID of one or more subnets to add to the endpoint.</p>
            remove_subnet_ids: <p>The unique identifiers of the subnets to remove from the endpoint.</p>
            add_security_group_ids: <p>The unique identifiers of the security groups to add to the endpoint. Security groups define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            remove_security_group_ids: <p>The unique identifiers of the security groups to remove from the endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_vpc_endpoint

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_vpc_endpoint.update_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest = {
            "id": id
        }
        if add_subnet_ids is not None:
            input_["add_subnet_ids"] = add_subnet_ids
        if remove_subnet_ids is not None:
            input_["remove_subnet_ids"] = remove_subnet_ids
        if add_security_group_ids is not None:
            input_["add_security_group_ids"] = add_security_group_ids
        if remove_security_group_ids is not None:
            input_["remove_security_group_ids"] = remove_security_group_ids
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

    def create_access_policy(
        self,
        type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy: "capo_opensearchserverless.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_access_policy_response.CreateAccessPolicyResponse":
        """<p>Creates a data access policy for OpenSearch Serverless. Access policies limit access to collections and the resources within them, and allow a user to access that data irrespective of the access mechanism or network source. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_access_policy_request.CreateAccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_access_policy_response.CreateAccessPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_access_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_access_policy.create_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_access_policy_request.CreateAccessPolicyRequest = {
            "type": type,
            "name": name,
            "policy": policy,
        }
        if description is not None:
            input_["description"] = description
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

    def get_access_policy(
        self,
        type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_access_policy_response.GetAccessPolicyResponse":
        """<p>Returns an OpenSearch Serverless access policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>Tye type of policy. Currently, the only supported value is <code>data</code>.</p>
            name: <p>The name of the access policy.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_access_policy_request.GetAccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_access_policy_response.GetAccessPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_access_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_access_policy.get_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_access_policy_request.GetAccessPolicyRequest = {
            "type": type,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_access_policy(
        self,
        type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        policy: Optional[
            "capo_opensearchserverless.types.policy_document.PolicyDocument"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_access_policy_response.UpdateAccessPolicyResponse":
        """<p>Updates an OpenSearch Serverless access policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_access_policy_request.UpdateAccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_access_policy_response.UpdateAccessPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_access_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_access_policy.update_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_access_policy_request.UpdateAccessPolicyRequest = {
            "type": type,
            "name": name,
            "policy_version": policy_version,
        }
        if description is not None:
            input_["description"] = description
        if policy is not None:
            input_["policy"] = policy
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

    def delete_access_policy(
        self,
        type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_access_policy_response.DeleteAccessPolicyResponse":
        """<p>Deletes an OpenSearch Serverless access policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_access_policy_request.DeleteAccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_access_policy_response.DeleteAccessPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_access_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_access_policy.delete_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_access_policy_request.DeleteAccessPolicyRequest = {
            "type": type,
            "name": name,
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

    def list_access_policies(
        self,
        type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "capo_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_access_policies_response.ListAccessPoliciesResponse":
        """<p>Returns information about a list of OpenSearch Serverless access policies.</p>

        Args:
            type: <p>The type of access policy.</p>
            resource: <p>Resource filters (can be collections or indexes) that policies can apply to.</p>
            next_token: <p>If your initial <code>ListAccessPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListAccessPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_access_policies_request.ListAccessPoliciesRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_access_policies_response.ListAccessPoliciesResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_access_policies

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_access_policies.list_access_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_access_policies_request.ListAccessPoliciesRequest = {
            "type": type
        }
        if resource is not None:
            input_["resource"] = resource
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

    def iter_list_access_policies(
        self,
        type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "capo_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_opensearchserverless.types.list_access_policies_response.ListAccessPoliciesResponse]":
        _token = next_token
        while True:
            _response = self.list_access_policies(
                type,
                config_overrides=config_overrides,
                resource=resource,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_collection(
        self,
        name: "capo_opensearchserverless.types.collection_name.CollectionName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        type: Optional[
            "capo_opensearchserverless.types.collection_type.CollectionType"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        standby_replicas: Optional[
            "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
        ] = None,
        vector_options: Optional[
            "capo_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        collection_group_name: Optional[
            "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
        ] = None,
        encryption_config: Optional[
            "capo_opensearchserverless.types.encryption_config.EncryptionConfig"
        ] = None,
        deletion_protection: Optional[
            "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_collection_response.CreateCollectionResponse":
        """<p>Creates a new OpenSearch Serverless collection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            name: <p>Name of the collection.</p>
            type: <p>The type of collection.</p>
            description: <p>Description of the collection.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            collection_group_name: <p>The name of the collection group to associate with the collection.</p>
            encryption_config: <p>Encryption settings for the collection.</p>
            deletion_protection: <p>Indicates whether to enable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.ocu_limit_exceeded_exception.OcuLimitExceededException: <p>Thrown when the collection you're attempting to create results in a number of search or indexing OCUs that exceeds the account limit. </p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_collection_request.CreateCollectionRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_collection_response.CreateCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_collection

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_collection.create_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_collection_request.CreateCollectionRequest = {
            "name": name
        }
        if type is not None:
            input_["type"] = type
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if standby_replicas is not None:
            input_["standby_replicas"] = standby_replicas
        if vector_options is not None:
            input_["vector_options"] = vector_options
        if collection_group_name is not None:
            input_["collection_group_name"] = collection_group_name
        if encryption_config is not None:
            input_["encryption_config"] = encryption_config
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
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

    def update_collection(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        vector_options: Optional[
            "capo_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        deletion_protection: Optional[
            "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_collection_response.UpdateCollectionResponse":
        """<p>Updates an OpenSearch Serverless collection.</p>

        Args:
            id: <p>The unique identifier of the collection.</p>
            description: <p>A description of the collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            deletion_protection: <p>Indicates whether to enable or disable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_collection_request.UpdateCollectionRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_collection_response.UpdateCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_collection

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_collection.update_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_collection_request.UpdateCollectionRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if vector_options is not None:
            input_["vector_options"] = vector_options
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
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

    def delete_collection(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse":
        """<p>Deletes an OpenSearch Serverless collection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection. For example, <code>1iu5usc406kd</code>. The ID is part of the collection endpoint. You can also retrieve it using the <a href="https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html">ListCollections</a> API.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_collection

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_collection.delete_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest = {
            "id": id
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

    def list_collections(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        collection_filters: Optional[
            "capo_opensearchserverless.types.collection_filters.CollectionFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_collections_response.ListCollectionsResponse":
        """<p>Lists all OpenSearch Serverless collections. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p> <note> <p>Make sure to include an empty request body {} if you don't include any collection filters in the request.</p> </note>

        Args:
            collection_filters: <p> A list of filter names and values that you can use for requests.</p>
            next_token: <p>If your initial <code>ListCollections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollections</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_collections_request.ListCollectionsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_collections_response.ListCollectionsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_collections

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_collections.list_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_collections_request.ListCollectionsRequest = {}
        if collection_filters is not None:
            input_["collection_filters"] = collection_filters
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

    def iter_list_collections(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        collection_filters: Optional[
            "capo_opensearchserverless.types.collection_filters.CollectionFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_opensearchserverless.types.list_collections_response.ListCollectionsResponse]":
        _token = next_token
        while True:
            _response = self.list_collections(
                config_overrides=config_overrides,
                collection_filters=collection_filters,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_collection_group(
        self,
        name: "capo_opensearchserverless.types.collection_group_name.CollectionGroupName",
        standby_replicas: "capo_opensearchserverless.types.standby_replicas.StandbyReplicas",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        generation: Optional[
            "capo_opensearchserverless.types.serverless_generation.ServerlessGeneration"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse":
        """<p>Creates a collection group within OpenSearch Serverless. Collection groups let you manage OpenSearch Compute Units (OCUs) at a group level, with multiple collections sharing the group's capacity limits.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html">Managing collection groups</a>.</p>

        Args:
            name: <p>The name of the collection group.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection group.</p>
            description: <p>A description of the collection group.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>
            capacity_limits: <p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>
            generation: <p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_collection_group

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_collection_group.create_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest = {
            "name": name,
            "standby_replicas": standby_replicas,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
        if generation is not None:
            input_["generation"] = generation
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

    def update_collection_group(
        self,
        id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse":
        """<p>Updates the description and capacity limits of a collection group.</p>

        Args:
            id: <p>The unique identifier of the collection group to update.</p>
            description: <p>A new description for the collection group.</p>
            capacity_limits: <p>Updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_collection_group

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_collection_group.update_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
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

    def delete_collection_group(
        self,
        id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse":
        """<p>Deletes a collection group. You can only delete empty collection groups that contain no collections. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection group to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_collection_group

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_collection_group.delete_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest = {
            "id": id
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

    def list_collection_groups(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse":
        """<p>Returns a list of collection groups. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            next_token: <p>If your initial <code>ListCollectionGroups</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollectionGroups</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_collection_groups

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_collection_groups.list_collection_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest = {}
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

    def iter_list_collection_groups(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse]":
        _token = next_token
        while True:
            _response = self.list_collection_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_index(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        index_schema: Optional[
            "capo_opensearchserverless.types.index_schema.IndexSchema"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_index_response.CreateIndexResponse":
        """<p>Creates an index within an OpenSearch Serverless collection. Unlike other OpenSearch indexes, indexes created by this API are automatically configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a> in the <i>OpenSearch User Guide</i>.</p>

        Args:
            id: <p>The unique identifier of the collection in which to create the index.</p>
            index_name: <p>The name of the index to create. Index names must be lowercase and can't begin with underscores (_) or hyphens (-).</p>
            index_schema: <p>The JSON schema definition for the index, including field mappings and settings.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_index_request.CreateIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_index_response.CreateIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_index.create_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_index_request.CreateIndexRequest = {
            "id": id,
            "index_name": index_name,
        }
        if index_schema is not None:
            input_["index_schema"] = index_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_index(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_index_response.GetIndexResponse":
        """<p>Retrieves information about an index in an OpenSearch Serverless collection, including its schema definition. The index might be configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index.</p>
            index_name: <p>The name of the index to retrieve information about.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_index_request.GetIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_index_response.GetIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_index.get_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_index_request.GetIndexRequest = {
            "id": id,
            "index_name": index_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_index(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        index_schema: Optional[
            "capo_opensearchserverless.types.index_schema.IndexSchema"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_index_response.UpdateIndexResponse":
        """<p>Updates an existing index in an OpenSearch Serverless collection. This operation allows you to modify the index schema, including adding new fields or changing field mappings. You can also enable automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index to update.</p>
            index_name: <p>The name of the index to update.</p>
            index_schema: <p>The updated JSON schema definition for the index, including field mappings and settings. </p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_index_request.UpdateIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_index_response.UpdateIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_index.update_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_index_request.UpdateIndexRequest = {
            "id": id,
            "index_name": index_name,
        }
        if index_schema is not None:
            input_["index_schema"] = index_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_index(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.delete_index_response.DeleteIndexResponse":
        """<p>Deletes an index from an OpenSearch Serverless collection. Be aware that the index might be configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index to delete.</p>
            index_name: <p>The name of the index to delete.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_index_request.DeleteIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_index_response.DeleteIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_index.delete_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_index_request.DeleteIndexRequest = {
            "id": id,
            "index_name": index_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_lifecycle_policy(
        self,
        type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        policy: Optional[
            "capo_opensearchserverless.types.policy_document.PolicyDocument"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse":
        """<p>Updates an OpenSearch Serverless access policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-update">Updating data lifecycle policies</a>.</p>

        Args:
            type: <p> The type of lifecycle policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the lifecycle policy.</p>
            policy: <p>The JSON policy document to use as the content for the lifecycle policy.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_lifecycle_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_lifecycle_policy.update_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest = {
            "type": type,
            "name": name,
            "policy_version": policy_version,
        }
        if description is not None:
            input_["description"] = description
        if policy is not None:
            input_["policy"] = policy
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

    def delete_lifecycle_policy(
        self,
        type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse":
        """<p>Deletes an OpenSearch Serverless lifecycle policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-delete">Deleting data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_lifecycle_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_lifecycle_policy.delete_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest = {
            "type": type,
            "name": name,
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

    def list_lifecycle_policies(
        self,
        type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resources: Optional[
            "capo_opensearchserverless.types.lifecycle_resource_filter.LifecycleResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse":
        """<p>Returns a list of OpenSearch Serverless lifecycle policies. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list">Viewing data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            resources: <p>Resource filters that policies can apply to. Currently, the only supported resource type is <code>index</code>.</p>
            next_token: <p>If your initial <code>ListLifecyclePolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListLifecyclePolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use use <code>nextToken</code> to get the next page of results. The default is 10.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_lifecycle_policies

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_lifecycle_policies.list_lifecycle_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest = {
            "type": type
        }
        if resources is not None:
            input_["resources"] = resources
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

    def iter_list_lifecycle_policies(
        self,
        type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resources: Optional[
            "capo_opensearchserverless.types.lifecycle_resource_filter.LifecycleResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_opensearchserverless.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse]":
        _token = next_token
        while True:
            _response = self.list_lifecycle_policies(
                type,
                config_overrides=config_overrides,
                resources=resources,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_security_config(
        self,
        type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType",
        name: "capo_opensearchserverless.types.config_name.ConfigName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options: Optional[
            "capo_opensearchserverless.types.create_iam_identity_center_config_options.CreateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse":
        """<p>Specifies a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            name: <p>The name of the security configuration.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>Describes SAML options in the form of a key-value map. This field is required if you specify <code>SAML</code> for the <code>type</code> parameter.</p>
            iam_identity_center_options: <p>Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify <code>iamidentitycenter</code> for the <code>type</code> parameter.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map. This field is required if you specify <code>iamFederation</code> for the <code>type</code> parameter.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_security_config.create_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest = {
            "type": type,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if saml_options is not None:
            input_["saml_options"] = saml_options
        if iam_identity_center_options is not None:
            input_["iam_identity_center_options"] = iam_identity_center_options
        if iam_federation_options is not None:
            input_["iam_federation_options"] = iam_federation_options
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

    def get_security_config(
        self,
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse":
        """<p>Returns information about an OpenSearch Serverless security configuration. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The unique identifier of the security configuration.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_security_config.get_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_security_config(
        self,
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        config_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "capo_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options_updates: Optional[
            "capo_opensearchserverless.types.update_iam_identity_center_config_options.UpdateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "capo_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse":
        """<p>Updates a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            config_version: <p>The version of the security configuration to be updated. You can find the most recent version of a security configuration using the <code>GetSecurityPolicy</code> command.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>SAML options in in the form of a key-value map.</p>
            iam_identity_center_options_updates: <p>Describes IAM Identity Center options in the form of a key-value map.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_security_config.update_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest = {
            "id": id,
            "config_version": config_version,
        }
        if description is not None:
            input_["description"] = description
        if saml_options is not None:
            input_["saml_options"] = saml_options
        if iam_identity_center_options_updates is not None:
            input_["iam_identity_center_options_updates"] = (
                iam_identity_center_options_updates
            )
        if iam_federation_options is not None:
            input_["iam_federation_options"] = iam_federation_options
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

    def delete_security_config(
        self,
        id: "capo_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse":
        """<p>Deletes a security configuration for OpenSearch Serverless. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_security_config

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_security_config.delete_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest = {
            "id": id
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

    def list_security_configs(
        self,
        type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse":
        """<p>Returns information about configured OpenSearch Serverless security configurations. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            next_token: <p>If your initial <code>ListSecurityConfigs</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityConfigs</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_security_configs

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_security_configs.list_security_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest = {
            "type": type
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

    def iter_list_security_configs(
        self,
        type: "capo_opensearchserverless.types.security_config_type.SecurityConfigType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse]":
        _token = next_token
        while True:
            _response = self.list_security_configs(
                type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_security_policy(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse":
        """<p>Returns information about a configured OpenSearch Serverless security policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html">Network access for Amazon OpenSearch Serverless</a> and <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the security policy.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_security_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_security_policy.get_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest = {
            "type": type,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_security_policy(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        policy: Optional[
            "capo_opensearchserverless.types.policy_document.PolicyDocument"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse":
        """<p>Updates an OpenSearch Serverless security policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html">Network access for Amazon OpenSearch Serverless</a> and <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of access policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_security_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_security_policy.update_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest = {
            "type": type,
            "name": name,
            "policy_version": policy_version,
        }
        if description is not None:
            input_["description"] = description
        if policy is not None:
            input_["policy"] = policy
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

    def delete_security_policy(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse":
        """<p>Deletes an OpenSearch Serverless security policy.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_security_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_security_policy.delete_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest = {
            "type": type,
            "name": name,
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

    def list_security_policies(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "capo_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse":
        """<p>Returns information about configured OpenSearch Serverless security policies.</p>

        Args:
            type: <p>The type of policy.</p>
            resource: <p>Resource filters (can be collection or indexes) that policies can apply to. </p>
            next_token: <p>If your initial <code>ListSecurityPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_security_policies

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_security_policies.list_security_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest = {
            "type": type
        }
        if resource is not None:
            input_["resource"] = resource
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

    def iter_list_security_policies(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "capo_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse]":
        _token = next_token
        while True:
            _response = self.list_security_policies(
                type,
                config_overrides=config_overrides,
                resource=resource,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_vpc_endpoint(
        self,
        name: "capo_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName",
        vpc_id: "capo_opensearchserverless.types.vpc_id.VpcId",
        subnet_ids: "capo_opensearchserverless.types.subnet_ids.SubnetIds",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        security_group_ids: Optional[
            "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an OpenSearch Serverless-managed interface VPC endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            name: <p>The name of the interface endpoint.</p>
            vpc_id: <p>The ID of the VPC from which you'll access OpenSearch Serverless.</p>
            subnet_ids: <p>The ID of one or more subnets from which you'll access OpenSearch Serverless.</p>
            security_group_ids: <p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint.create_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {
            "name": name,
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
        }
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
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

    def delete_vpc_endpoint(
        self,
        id: "capo_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an OpenSearch Serverless-managed interface endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The VPC endpoint identifier.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint.delete_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {
            "id": id
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

    def list_vpc_endpoints(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        vpc_endpoint_filters: Optional[
            "capo_opensearchserverless.types.vpc_endpoint_filters.VpcEndpointFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            vpc_endpoint_filters: <p>Filter the results according to the current status of the VPC endpoint. Possible statuses are <code>CREATING</code>, <code>DELETING</code>, <code>UPDATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            next_token: <p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints.list_vpc_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}
        if vpc_endpoint_filters is not None:
            input_["vpc_endpoint_filters"] = vpc_endpoint_filters
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

    def iter_list_vpc_endpoints(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        vpc_endpoint_filters: Optional[
            "capo_opensearchserverless.types.vpc_endpoint_filters.VpcEndpointFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse]":
        _token = next_token
        while True:
            _response = self.list_vpc_endpoints(
                config_overrides=config_overrides,
                vpc_endpoint_filters=vpc_endpoint_filters,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
