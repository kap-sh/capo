"""Generated from Smithy shape ``com.amazonaws.mediastore#MediaStore_20170901``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_mediastore._auth._signers
import capo_mediastore._auth._sigv4
from capo_mediastore._auth._identity import Credentials
from capo_mediastore._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediastore._auth._zapros_handler import AuthMiddleware
from capo_mediastore._pagination import resolve_path as _resolve_path
from capo_mediastore._services._aws_config import aaws_config
from capo_mediastore._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_mediastore.types.container_arn
    import capo_mediastore.types.container_list_limit
    import capo_mediastore.types.container_name
    import capo_mediastore.types.container_policy
    import capo_mediastore.types.cors_policy
    import capo_mediastore.types.create_container_input
    import capo_mediastore.types.create_container_output
    import capo_mediastore.types.delete_container_input
    import capo_mediastore.types.delete_container_output
    import capo_mediastore.types.delete_container_policy_input
    import capo_mediastore.types.delete_container_policy_output
    import capo_mediastore.types.delete_cors_policy_input
    import capo_mediastore.types.delete_cors_policy_output
    import capo_mediastore.types.delete_lifecycle_policy_input
    import capo_mediastore.types.delete_lifecycle_policy_output
    import capo_mediastore.types.delete_metric_policy_input
    import capo_mediastore.types.delete_metric_policy_output
    import capo_mediastore.types.describe_container_input
    import capo_mediastore.types.describe_container_output
    import capo_mediastore.types.get_container_policy_input
    import capo_mediastore.types.get_container_policy_output
    import capo_mediastore.types.get_cors_policy_input
    import capo_mediastore.types.get_cors_policy_output
    import capo_mediastore.types.get_lifecycle_policy_input
    import capo_mediastore.types.get_lifecycle_policy_output
    import capo_mediastore.types.get_metric_policy_input
    import capo_mediastore.types.get_metric_policy_output
    import capo_mediastore.types.lifecycle_policy
    import capo_mediastore.types.list_containers_input
    import capo_mediastore.types.list_containers_output
    import capo_mediastore.types.list_tags_for_resource_input
    import capo_mediastore.types.list_tags_for_resource_output
    import capo_mediastore.types.metric_policy
    import capo_mediastore.types.pagination_token
    import capo_mediastore.types.put_container_policy_input
    import capo_mediastore.types.put_container_policy_output
    import capo_mediastore.types.put_cors_policy_input
    import capo_mediastore.types.put_cors_policy_output
    import capo_mediastore.types.put_lifecycle_policy_input
    import capo_mediastore.types.put_lifecycle_policy_output
    import capo_mediastore.types.put_metric_policy_input
    import capo_mediastore.types.put_metric_policy_output
    import capo_mediastore.types.start_access_logging_input
    import capo_mediastore.types.start_access_logging_output
    import capo_mediastore.types.stop_access_logging_input
    import capo_mediastore.types.stop_access_logging_output
    import capo_mediastore.types.tag_key_list
    import capo_mediastore.types.tag_list
    import capo_mediastore.types.tag_resource_input
    import capo_mediastore.types.tag_resource_output
    import capo_mediastore.types.untag_resource_input
    import capo_mediastore.types.untag_resource_output


class AsyncMediaStoreClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMediaStoreClient:
    """A client for the ``MediaStore`` service.

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
        self._config = AsyncMediaStoreClientConfig(
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
        self, config_overrides: Optional[AsyncMediaStoreClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMediaStoreClientConfig = config_overrides or {}
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

    async def create_container(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
        tags: Optional["capo_mediastore.types.tag_list.TagList"] = None,
    ) -> "capo_mediastore.types.create_container_output.CreateContainerOutput":
        """<p>Creates a storage container to hold objects. A container is similar to a bucket in the Amazon S3 service.</p>

        Args:
            container_name: <p>The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named <code>movies</code> in every region, as long as you don’t have an existing container with that name.</p>
            tags: <p>An array of key:value pairs that you define. These values can be anything that you want. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see <a href="https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html">Tagging Resources in MediaStore</a>.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit has been exceeded.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.create_container_input.CreateContainerInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.create_container_output.CreateContainerOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.create_container

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.create_container.async_create_container(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.create_container_input.CreateContainerInput = {
            "container_name": container_name
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

    async def delete_container(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.delete_container_output.DeleteContainerOutput":
        """<p>Deletes the specified container. Before you make a <code>DeleteContainer</code> request, delete any objects in the container or in any folders in the container. You can delete only empty containers. </p>

        Args:
            container_name: <p>The name of the container to delete. </p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.delete_container_input.DeleteContainerInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.delete_container_output.DeleteContainerOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.delete_container

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.delete_container.async_delete_container(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.delete_container_input.DeleteContainerInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_container_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.delete_container_policy_output.DeleteContainerPolicyOutput":
        """<p>Deletes the access policy that is associated with the specified container.</p>

        Args:
            container_name: <p>The name of the container that holds the policy.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.policy_not_found_exception.PolicyNotFoundException: <p>The policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.delete_container_policy_input.DeleteContainerPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.delete_container_policy_output.DeleteContainerPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.delete_container_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.delete_container_policy.async_delete_container_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.delete_container_policy_input.DeleteContainerPolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cors_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.delete_cors_policy_output.DeleteCorsPolicyOutput":
        """<p>Deletes the cross-origin resource sharing (CORS) configuration information that is set for the container.</p> <p>To use this operation, you must have permission to perform the <code>MediaStore:DeleteCorsPolicy</code> action. The container owner has this permission by default and can grant this permission to others.</p>

        Args:
            container_name: <p>The name of the container to remove the policy from.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.cors_policy_not_found_exception.CorsPolicyNotFoundException: <p>The CORS policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.delete_cors_policy_input.DeleteCorsPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.delete_cors_policy_output.DeleteCorsPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.delete_cors_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.delete_cors_policy.async_delete_cors_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.delete_cors_policy_input.DeleteCorsPolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_lifecycle_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.delete_lifecycle_policy_output.DeleteLifecyclePolicyOutput":
        """<p>Removes an object lifecycle policy from a container. It takes up to 20 minutes for the change to take effect.</p>

        Args:
            container_name: <p>The name of the container that holds the object lifecycle policy.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.policy_not_found_exception.PolicyNotFoundException: <p>The policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.delete_lifecycle_policy_input.DeleteLifecyclePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.delete_lifecycle_policy_output.DeleteLifecyclePolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.delete_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.delete_lifecycle_policy.async_delete_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.delete_lifecycle_policy_input.DeleteLifecyclePolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_metric_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.delete_metric_policy_output.DeleteMetricPolicyOutput":
        """<p>Deletes the metric policy that is associated with the specified container. If there is no metric policy associated with the container, MediaStore doesn't send metrics to CloudWatch.</p>

        Args:
            container_name: <p>The name of the container that is associated with the metric policy that you want to delete.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.policy_not_found_exception.PolicyNotFoundException: <p>The policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.delete_metric_policy_input.DeleteMetricPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.delete_metric_policy_output.DeleteMetricPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.delete_metric_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.delete_metric_policy.async_delete_metric_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.delete_metric_policy_input.DeleteMetricPolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_container(
        self,
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
        container_name: Optional[
            "capo_mediastore.types.container_name.ContainerName"
        ] = None,
    ) -> "capo_mediastore.types.describe_container_output.DescribeContainerOutput":
        """<p>Retrieves the properties of the requested container. This request is commonly used to retrieve the endpoint of a container. An endpoint is a value assigned by the service when a new container is created. A container's endpoint does not change after it has been assigned. The <code>DescribeContainer</code> request returns a single <code>Container</code> object based on <code>ContainerName</code>. To return all <code>Container</code> objects that are associated with a specified AWS account, use <a>ListContainers</a>.</p>

        Args:
            container_name: <p>The name of the container to query.</p>

        Raises:
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.describe_container_input.DescribeContainerInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.describe_container_output.DescribeContainerOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.describe_container

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.describe_container.async_describe_container(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.describe_container_input.DescribeContainerInput = {}
        if container_name is not None:
            input_["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.get_container_policy_output.GetContainerPolicyOutput":
        """<p>Retrieves the access policy for the specified container. For information about the data that is included in an access policy, see the <a href="https://aws.amazon.com/documentation/iam/">AWS Identity and Access Management User Guide</a>.</p>

        Args:
            container_name: <p>The name of the container. </p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.policy_not_found_exception.PolicyNotFoundException: <p>The policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.get_container_policy_input.GetContainerPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.get_container_policy_output.GetContainerPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.get_container_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.get_container_policy.async_get_container_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.get_container_policy_input.GetContainerPolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cors_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.get_cors_policy_output.GetCorsPolicyOutput":
        """<p>Returns the cross-origin resource sharing (CORS) configuration information that is set for the container.</p> <p>To use this operation, you must have permission to perform the <code>MediaStore:GetCorsPolicy</code> action. By default, the container owner has this permission and can grant it to others.</p>

        Args:
            container_name: <p>The name of the container that the policy is assigned to.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.cors_policy_not_found_exception.CorsPolicyNotFoundException: <p>The CORS policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.get_cors_policy_input.GetCorsPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.get_cors_policy_output.GetCorsPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.get_cors_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.get_cors_policy.async_get_cors_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.get_cors_policy_input.GetCorsPolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lifecycle_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.get_lifecycle_policy_output.GetLifecyclePolicyOutput":
        """<p>Retrieves the object lifecycle policy that is assigned to a container.</p>

        Args:
            container_name: <p>The name of the container that the object lifecycle policy is assigned to.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.policy_not_found_exception.PolicyNotFoundException: <p>The policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.get_lifecycle_policy_input.GetLifecyclePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.get_lifecycle_policy_output.GetLifecyclePolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.get_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.get_lifecycle_policy.async_get_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.get_lifecycle_policy_input.GetLifecyclePolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_metric_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.get_metric_policy_output.GetMetricPolicyOutput":
        """<p>Returns the metric policy for the specified container. </p>

        Args:
            container_name: <p>The name of the container that is associated with the metric policy.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.policy_not_found_exception.PolicyNotFoundException: <p>The policy that you specified in the request does not exist.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.get_metric_policy_input.GetMetricPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.get_metric_policy_output.GetMetricPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.get_metric_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.get_metric_policy.async_get_metric_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.get_metric_policy_input.GetMetricPolicyInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_containers(
        self,
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
        next_token: Optional[
            "capo_mediastore.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_mediastore.types.container_list_limit.ContainerListLimit"
        ] = None,
    ) -> "capo_mediastore.types.list_containers_output.ListContainersOutput":
        """<p>Lists the properties of all containers in AWS Elemental MediaStore. </p> <p>You can query to receive all the containers in one response. Or you can include the <code>MaxResults</code> parameter to receive a limited number of containers in each response. In this case, the response includes a token. To get the next set of containers, send the command again, this time with the <code>NextToken</code> parameter (with the returned token as its value). The next set of responses appears, with a token if there are still more containers to receive. </p> <p>See also <a>DescribeContainer</a>, which gets the properties of one container. </p>

        Args:
            next_token: <p>Only if you used <code>MaxResults</code> in the first command, enter the token (which was included in the previous response) to obtain the next set of containers. This token is included in a response only if there actually are more containers to list.</p>
            max_results: <p>Enter the maximum number of containers in the response. Use from 1 to 255 characters. </p>

        Raises:
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.list_containers_input.ListContainersInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.list_containers_output.ListContainersOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.list_containers

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.list_containers.async_list_containers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.list_containers_input.ListContainersInput = {}
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

    async def iter_list_containers(
        self,
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
        next_token: Optional[
            "capo_mediastore.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_mediastore.types.container_list_limit.ContainerListLimit"
        ] = None,
    ) -> "AsyncIterator[capo_mediastore.types.list_containers_output.ListContainersOutput]":
        _token = next_token
        while True:
            _response = await self.list_containers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource: "capo_mediastore.types.container_arn.ContainerARN",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> (
        "capo_mediastore.types.list_tags_for_resource_output.ListTagsForResourceOutput"
    ):
        """<p>Returns a list of the tags assigned to the specified container. </p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) for the container.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource": resource
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_container_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        policy: "capo_mediastore.types.container_policy.ContainerPolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.put_container_policy_output.PutContainerPolicyOutput":
        """<p>Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the <a href="https://aws.amazon.com/documentation/iam/">AWS Identity and Access Management User Guide</a>.</p> <p>For this release of the REST API, you can create only one policy for a container. If you enter <code>PutContainerPolicy</code> twice, the second command modifies the existing policy. </p>

        Args:
            container_name: <p>The name of the container.</p>
            policy: <p>The contents of the policy, which includes the following: </p> <ul> <li> <p>One <code>Version</code> tag</p> </li> <li> <p>One <code>Statement</code> tag that contains the standard tags for the policy.</p> </li> </ul>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.put_container_policy_input.PutContainerPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.put_container_policy_output.PutContainerPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.put_container_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.put_container_policy.async_put_container_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.put_container_policy_input.PutContainerPolicyInput = {
            "container_name": container_name,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_cors_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        cors_policy: "capo_mediastore.types.cors_policy.CorsPolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.put_cors_policy_output.PutCorsPolicyOutput":
        """<p>Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser's XMLHttpRequest capability.</p> <p>To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.</p> <p>To learn more about CORS, see <a href="https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html">Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore</a>.</p>

        Args:
            container_name: <p>The name of the container that you want to assign the CORS policy to.</p>
            cors_policy: <p>The CORS policy to apply to the container. </p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.put_cors_policy_input.PutCorsPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.put_cors_policy_output.PutCorsPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.put_cors_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.put_cors_policy.async_put_cors_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.put_cors_policy_input.PutCorsPolicyInput = {
            "container_name": container_name,
            "cors_policy": cors_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_lifecycle_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        lifecycle_policy: "capo_mediastore.types.lifecycle_policy.LifecyclePolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.put_lifecycle_policy_output.PutLifecyclePolicyOutput":
        """<p>Writes an object lifecycle policy to a container. If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect.</p> <p>For information about how to construct an object lifecycle policy, see <a href="https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html">Components of an Object Lifecycle Policy</a>.</p>

        Args:
            container_name: <p>The name of the container that you want to assign the object lifecycle policy to.</p>
            lifecycle_policy: <p>The object lifecycle policy to apply to the container.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.put_lifecycle_policy_input.PutLifecyclePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.put_lifecycle_policy_output.PutLifecyclePolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.put_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.put_lifecycle_policy.async_put_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.put_lifecycle_policy_input.PutLifecyclePolicyInput = {
            "container_name": container_name,
            "lifecycle_policy": lifecycle_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_metric_policy(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        metric_policy: "capo_mediastore.types.metric_policy.MetricPolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.put_metric_policy_output.PutMetricPolicyOutput":
        """<p>The metric policy that you want to add to the container. A metric policy allows AWS Elemental MediaStore to send metrics to Amazon CloudWatch. It takes up to 20 minutes for the new policy to take effect.</p>

        Args:
            container_name: <p>The name of the container that you want to add the metric policy to.</p>
            metric_policy: <p>The metric policy that you want to associate with the container. In the policy, you must indicate whether you want MediaStore to send container-level metrics. You can also include up to five rules to define groups of objects that you want MediaStore to send object-level metrics for. If you include rules in the policy, construct each rule with both of the following:</p> <ul> <li> <p>An object group that defines which objects to include in the group. The definition can be a path or a file name, but it can't have more than 900 characters. Valid characters are: a-z, A-Z, 0-9, _ (underscore), = (equal), : (colon), . (period), - (hyphen), ~ (tilde), / (forward slash), and * (asterisk). Wildcards (*) are acceptable.</p> </li> <li> <p>An object group name that allows you to refer to the object group. The name can't have more than 30 characters. Valid characters are: a-z, A-Z, 0-9, and _ (underscore).</p> </li> </ul>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.put_metric_policy_input.PutMetricPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.put_metric_policy_output.PutMetricPolicyOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.put_metric_policy

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.put_metric_policy.async_put_metric_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.put_metric_policy_input.PutMetricPolicyInput = {
            "container_name": container_name,
            "metric_policy": metric_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_access_logging(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.start_access_logging_output.StartAccessLoggingOutput":
        """<p>Starts access logging on the specified container. When you enable access logging on a container, MediaStore delivers access logs for objects stored in that container to Amazon CloudWatch Logs.</p>

        Args:
            container_name: <p>The name of the container that you want to start access logging on.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.start_access_logging_input.StartAccessLoggingInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.start_access_logging_output.StartAccessLoggingOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.start_access_logging

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.start_access_logging.async_start_access_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.start_access_logging_input.StartAccessLoggingInput = {
            "container_name": container_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_access_logging(
        self,
        container_name: "capo_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.stop_access_logging_output.StopAccessLoggingOutput":
        """<p>Stops access logging on the specified container. When you stop access logging on a container, MediaStore stops sending access logs to Amazon CloudWatch Logs. These access logs are not saved and are not retrievable.</p>

        Args:
            container_name: <p>The name of the container that you want to stop access logging on.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.stop_access_logging_input.StopAccessLoggingInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.stop_access_logging_output.StopAccessLoggingOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.stop_access_logging

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.stop_access_logging.async_stop_access_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.stop_access_logging_input.StopAccessLoggingInput = {
            "container_name": container_name
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
        resource: "capo_mediastore.types.container_arn.ContainerARN",
        tags: "capo_mediastore.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.tag_resource_output.TagResourceOutput":
        """<p>Adds tags to the specified AWS Elemental MediaStore container. Tags are key:value pairs that you can associate with AWS resources. For example, the tag key might be "customer" and the tag value might be "companyA." You can specify one or more tags to add to each container. You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see <a href="https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html">Tagging Resources in MediaStore</a>.</p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) for the container. </p>
            tags: <p>An array of key:value pairs that you want to add to the container. You need to specify only the tags that you want to add or update. For example, suppose a container already has two tags (customer:CompanyA and priority:High). You want to change the priority tag and also add a third tag (type:Contract). For TagResource, you specify the following tags: priority:Medium, type:Contract. The result is that your container has three tags: customer:CompanyA, priority:Medium, and type:Contract.</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.tag_resource

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.tag_resource_input.TagResourceInput = {
            "resource": resource,
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
        resource: "capo_mediastore.types.container_arn.ContainerARN",
        tag_keys: "capo_mediastore.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "capo_mediastore.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from the specified container. You can specify one or more tags to remove. </p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) for the container.</p>
            tag_keys: <p>A comma-separated list of keys for tags that you want to remove from the container. For example, if your container has two tags (customer:CompanyA and priority:High) and you want to remove one of the tags (priority:High), you specify the key for the tag that you want to remove (priority).</p>

        Raises:
            capo_mediastore.errors.container_in_use_exception.ContainerInUseException: <p>The container that you specified in the request already exists or is being updated.</p>
            capo_mediastore.errors.container_not_found_exception.ContainerNotFoundException: <p>The container that you specified in the request does not exist.</p>
            capo_mediastore.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediastore.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_mediastore.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_mediastore._operations.media_store_20170901.untag_resource

            (
                output,
                http_response,
            ) = await capo_mediastore._operations.media_store_20170901.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore.types.untag_resource_input.UntagResourceInput = {
            "resource": resource,
            "tag_keys": tag_keys,
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
