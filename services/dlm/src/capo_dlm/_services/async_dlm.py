"""Generated from Smithy shape ``com.amazonaws.dlm#dlm_20180112``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_dlm._auth._signers
import capo_dlm._auth._sigv4
from capo_dlm._auth._identity import Credentials
from capo_dlm._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_dlm._auth._zapros_handler import AuthMiddleware
from capo_dlm._services._aws_config import aaws_config
from capo_dlm._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_dlm.types.copy_tags_nullable
    import capo_dlm.types.create_interval
    import capo_dlm.types.create_lifecycle_policy_request
    import capo_dlm.types.create_lifecycle_policy_response
    import capo_dlm.types.cross_region_copy_target_list
    import capo_dlm.types.default_policies_type_values
    import capo_dlm.types.default_policy_type_values
    import capo_dlm.types.delete_lifecycle_policy_request
    import capo_dlm.types.delete_lifecycle_policy_response
    import capo_dlm.types.exclusions
    import capo_dlm.types.execution_role_arn
    import capo_dlm.types.extend_deletion
    import capo_dlm.types.get_lifecycle_policies_request
    import capo_dlm.types.get_lifecycle_policies_response
    import capo_dlm.types.get_lifecycle_policy_request
    import capo_dlm.types.get_lifecycle_policy_response
    import capo_dlm.types.gettable_policy_state_values
    import capo_dlm.types.list_tags_for_resource_request
    import capo_dlm.types.list_tags_for_resource_response
    import capo_dlm.types.policy_arn
    import capo_dlm.types.policy_description
    import capo_dlm.types.policy_details
    import capo_dlm.types.policy_id
    import capo_dlm.types.policy_id_list
    import capo_dlm.types.resource_type_values_list
    import capo_dlm.types.retain_interval
    import capo_dlm.types.settable_policy_state_values
    import capo_dlm.types.tag_key_list
    import capo_dlm.types.tag_map
    import capo_dlm.types.tag_resource_request
    import capo_dlm.types.tag_resource_response
    import capo_dlm.types.tags_to_add_filter_list
    import capo_dlm.types.target_tags_filter_list
    import capo_dlm.types.untag_resource_request
    import capo_dlm.types.untag_resource_response
    import capo_dlm.types.update_lifecycle_policy_request
    import capo_dlm.types.update_lifecycle_policy_response


class AsyncDLMClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDLMClient:
    """A client for the ``DLM`` service.

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
        self._config = AsyncDLMClientConfig(
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
        self, config_overrides: Optional[AsyncDLMClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDLMClientConfig = config_overrides or {}
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

    async def create_lifecycle_policy(
        self,
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
        execution_role_arn: Optional[
            "capo_dlm.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
        description: Optional[
            "capo_dlm.types.policy_description.PolicyDescription"
        ] = None,
        state: Optional[
            "capo_dlm.types.settable_policy_state_values.SettablePolicyStateValues"
        ] = None,
        policy_details: Optional["capo_dlm.types.policy_details.PolicyDetails"] = None,
        tags: Optional["capo_dlm.types.tag_map.TagMap"] = None,
        default_policy: Optional[
            "capo_dlm.types.default_policy_type_values.DefaultPolicyTypeValues"
        ] = None,
        create_interval: Optional[
            "capo_dlm.types.create_interval.CreateInterval"
        ] = None,
        retain_interval: Optional[
            "capo_dlm.types.retain_interval.RetainInterval"
        ] = None,
        copy_tags: Optional[
            "capo_dlm.types.copy_tags_nullable.CopyTagsNullable"
        ] = None,
        extend_deletion: Optional[
            "capo_dlm.types.extend_deletion.ExtendDeletion"
        ] = None,
        cross_region_copy_targets: Optional[
            "capo_dlm.types.cross_region_copy_target_list.CrossRegionCopyTargetList"
        ] = None,
        exclusions: Optional["capo_dlm.types.exclusions.Exclusions"] = None,
    ) -> (
        "capo_dlm.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse"
    ):
        """<p>Creates an Amazon Data Lifecycle Manager lifecycle policy. Amazon Data Lifecycle Manager supports the following policy types:</p> <ul> <li> <p>Custom EBS snapshot policy</p> </li> <li> <p>Custom EBS-backed AMI policy</p> </li> <li> <p>Cross-account copy event policy</p> </li> <li> <p>Default policy for EBS snapshots</p> </li> <li> <p>Default policy for EBS-backed AMIs</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/policy-differences.html"> Default policies vs custom policies</a>.</p> <important> <p>If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.</p> </important>

        Args:
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.</p>
            description: <p>A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.</p>
            state: <p>The activation state of the lifecycle policy after creation.</p>
            policy_details: <p>The configuration details of the lifecycle policy.</p> <important> <p>If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.</p> </important>
            tags: <p>The tags to apply to the lifecycle policy during creation.</p>
            default_policy: <p> <b>[Default policies only]</b> Specify the type of default policy to create.</p> <ul> <li> <p>To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify <code>VOLUME</code>.</p> </li> <li> <p>To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify <code>INSTANCE</code>.</p> </li> </ul>
            create_interval: <p> <b>[Default policies only]</b> Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.</p> <p>Default: 1</p>
            retain_interval: <p> <b>[Default policies only]</b> Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.</p> <p>Default: 7</p>
            copy_tags: <p> <b>[Default policies only]</b> Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is <code>false</code>.</p> <p>Default: false</p>
            extend_deletion: <p> <b>[Default policies only]</b> Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.</p> <p>By default (<b>ExtendDeletion=false</b>):</p> <ul> <li> <p>If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify <code>true</code>.</p> </li> <li> <p>If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify <code>true</code>.</p> </li> </ul> <p>If you enable extended deletion (<b>ExtendDeletion=true</b>), you override both default behaviors simultaneously.</p> <p>If you do not specify a value, the default is <code>false</code>.</p> <p>Default: false</p>
            cross_region_copy_targets: <p> <b>[Default policies only]</b> Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.</p>
            exclusions: <p> <b>[Default policies only]</b> Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.</p>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.invalid_request_exception.InvalidRequestException: <p>Bad request. The request is missing required parameters or has invalid parameters.</p>
            capo_dlm.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because a limit was exceeded.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.create_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.create_lifecycle_policy.async_create_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest = {}
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if description is not None:
            input_["description"] = description
        if state is not None:
            input_["state"] = state
        if policy_details is not None:
            input_["policy_details"] = policy_details
        if tags is not None:
            input_["tags"] = tags
        if default_policy is not None:
            input_["default_policy"] = default_policy
        if create_interval is not None:
            input_["create_interval"] = create_interval
        if retain_interval is not None:
            input_["retain_interval"] = retain_interval
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if extend_deletion is not None:
            input_["extend_deletion"] = extend_deletion
        if cross_region_copy_targets is not None:
            input_["cross_region_copy_targets"] = cross_region_copy_targets
        if exclusions is not None:
            input_["exclusions"] = exclusions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_lifecycle_policy(
        self,
        policy_id: "capo_dlm.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
    ) -> (
        "capo_dlm.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
    ):
        """<p>Deletes the specified lifecycle policy and halts the automated operations that the policy specified.</p> <p>For more information about deleting a policy, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-modify-delete.html#delete">Delete lifecycle policies</a>.</p>

        Args:
            policy_id: <p>The identifier of the lifecycle policy.</p>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because a limit was exceeded.</p>
            capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource was not found.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.delete_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.delete_lifecycle_policy.async_delete_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest = {
            "policy_id": policy_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lifecycle_policies(
        self,
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
        policy_ids: Optional["capo_dlm.types.policy_id_list.PolicyIdList"] = None,
        state: Optional[
            "capo_dlm.types.gettable_policy_state_values.GettablePolicyStateValues"
        ] = None,
        resource_types: Optional[
            "capo_dlm.types.resource_type_values_list.ResourceTypeValuesList"
        ] = None,
        target_tags: Optional[
            "capo_dlm.types.target_tags_filter_list.TargetTagsFilterList"
        ] = None,
        tags_to_add: Optional[
            "capo_dlm.types.tags_to_add_filter_list.TagsToAddFilterList"
        ] = None,
        default_policy_type: Optional[
            "capo_dlm.types.default_policies_type_values.DefaultPoliciesTypeValues"
        ] = None,
    ) -> "capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse":
        """<p>Gets summary information about all or the specified data lifecycle policies.</p> <p>To get complete information about a policy, use <a href="https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicy.html">GetLifecyclePolicy</a>.</p>

        Args:
            policy_ids: <p>The identifiers of the data lifecycle policies.</p>
            state: <p>The activation state.</p>
            resource_types: <p>The resource type.</p>
            target_tags: <p>The target tag for a policy.</p> <p>Tags are strings in the format <code>key=value</code>.</p>
            tags_to_add: <p>The tags to add to objects created by the policy.</p> <p>Tags are strings in the format <code>key=value</code>.</p> <p>These user-defined tags are added in addition to the Amazon Web Services-added lifecycle tags.</p>
            default_policy_type: <p> <b>[Default policies only]</b> Specifies the type of default policy to get. Specify one of the following:</p> <ul> <li> <p> <code>VOLUME</code> - To get only the default policy for EBS snapshots</p> </li> <li> <p> <code>INSTANCE</code> - To get only the default policy for EBS-backed AMIs</p> </li> <li> <p> <code>ALL</code> - To get all default policies</p> </li> </ul>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.invalid_request_exception.InvalidRequestException: <p>Bad request. The request is missing required parameters or has invalid parameters.</p>
            capo_dlm.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because a limit was exceeded.</p>
            capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource was not found.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.get_lifecycle_policies_request.GetLifecyclePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.get_lifecycle_policies_response.GetLifecyclePoliciesResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.get_lifecycle_policies

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.get_lifecycle_policies.async_get_lifecycle_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.get_lifecycle_policies_request.GetLifecyclePoliciesRequest = {}
        if policy_ids is not None:
            input_["policy_ids"] = policy_ids
        if state is not None:
            input_["state"] = state
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if target_tags is not None:
            input_["target_tags"] = target_tags
        if tags_to_add is not None:
            input_["tags_to_add"] = tags_to_add
        if default_policy_type is not None:
            input_["default_policy_type"] = default_policy_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lifecycle_policy(
        self,
        policy_id: "capo_dlm.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
    ) -> "capo_dlm.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse":
        """<p>Gets detailed information about the specified lifecycle policy.</p>

        Args:
            policy_id: <p>The identifier of the lifecycle policy.</p>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because a limit was exceeded.</p>
            capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource was not found.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.get_lifecycle_policy_response.GetLifecyclePolicyResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.get_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.get_lifecycle_policy.async_get_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.get_lifecycle_policy_request.GetLifecyclePolicyRequest = {
            "policy_id": policy_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_dlm.types.policy_arn.PolicyArn",
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
    ) -> "capo_dlm.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.invalid_request_exception.InvalidRequestException: <p>Bad request. The request is missing required parameters or has invalid parameters.</p>
            capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource was not found.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_dlm.types.policy_arn.PolicyArn",
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
        tags: Optional["capo_dlm.types.tag_map.TagMap"] = None,
    ) -> "capo_dlm.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>One or more tags.</p>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.invalid_request_exception.InvalidRequestException: <p>Bad request. The request is missing required parameters or has invalid parameters.</p>
            capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource was not found.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.tag_resource

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_dlm.types.policy_arn.PolicyArn",
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
        tag_keys: Optional["capo_dlm.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_dlm.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.invalid_request_exception.InvalidRequestException: <p>Bad request. The request is missing required parameters or has invalid parameters.</p>
            capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource was not found.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.untag_resource

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_lifecycle_policy(
        self,
        policy_id: "capo_dlm.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[AsyncDLMClientConfig] = None,
        execution_role_arn: Optional[
            "capo_dlm.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
        state: Optional[
            "capo_dlm.types.settable_policy_state_values.SettablePolicyStateValues"
        ] = None,
        description: Optional[
            "capo_dlm.types.policy_description.PolicyDescription"
        ] = None,
        policy_details: Optional["capo_dlm.types.policy_details.PolicyDetails"] = None,
        create_interval: Optional[
            "capo_dlm.types.create_interval.CreateInterval"
        ] = None,
        retain_interval: Optional[
            "capo_dlm.types.retain_interval.RetainInterval"
        ] = None,
        copy_tags: Optional[
            "capo_dlm.types.copy_tags_nullable.CopyTagsNullable"
        ] = None,
        extend_deletion: Optional[
            "capo_dlm.types.extend_deletion.ExtendDeletion"
        ] = None,
        cross_region_copy_targets: Optional[
            "capo_dlm.types.cross_region_copy_target_list.CrossRegionCopyTargetList"
        ] = None,
        exclusions: Optional["capo_dlm.types.exclusions.Exclusions"] = None,
    ) -> (
        "capo_dlm.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse"
    ):
        """<p>Updates the specified lifecycle policy.</p> <p>For more information about updating a policy, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-modify-delete.html#modify">Modify lifecycle policies</a>.</p>

        Args:
            policy_id: <p>The identifier of the lifecycle policy.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.</p>
            state: <p>The desired activation state of the lifecycle policy after creation.</p>
            description: <p>A description of the lifecycle policy.</p>
            policy_details: <p>The configuration of the lifecycle policy. You cannot update the policy type or the resource type.</p>
            create_interval: <p> <b>[Default policies only]</b> Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days.</p>
            retain_interval: <p> <b>[Default policies only]</b> Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time.</p>
            copy_tags: <p> <b>[Default policies only]</b> Indicates whether the policy should copy tags from the source resource to the snapshot or AMI.</p>
            extend_deletion: <p> <b>[Default policies only]</b> Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.</p> <p>By default (<b>ExtendDeletion=false</b>):</p> <ul> <li> <p>If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify <code>true</code>.</p> </li> <li> <p>If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify <code>true</code>.</p> </li> </ul> <p>If you enable extended deletion (<b>ExtendDeletion=true</b>), you override both default behaviors simultaneously.</p> <p>Default: false</p>
            cross_region_copy_targets: <p> <b>[Default policies only]</b> Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.</p>
            exclusions: <p> <b>[Default policies only]</b> Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.</p>

        Raises:
            capo_dlm.errors.internal_server_exception.InternalServerException: <p>The service failed in an unexpected way.</p>
            capo_dlm.errors.invalid_request_exception.InvalidRequestException: <p>Bad request. The request is missing required parameters or has invalid parameters.</p>
            capo_dlm.errors.limit_exceeded_exception.LimitExceededException: <p>The request failed because a limit was exceeded.</p>
            capo_dlm.errors.resource_not_found_exception.ResourceNotFoundException: <p>A requested resource was not found.</p>
            capo_dlm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dlm.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_dlm.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse"
        ]:
            import capo_dlm._operations.dlm_20180112.update_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_dlm._operations.dlm_20180112.update_lifecycle_policy.async_update_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dlm.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest = {
            "policy_id": policy_id
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if state is not None:
            input_["state"] = state
        if description is not None:
            input_["description"] = description
        if policy_details is not None:
            input_["policy_details"] = policy_details
        if create_interval is not None:
            input_["create_interval"] = create_interval
        if retain_interval is not None:
            input_["retain_interval"] = retain_interval
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if extend_deletion is not None:
            input_["extend_deletion"] = extend_deletion
        if cross_region_copy_targets is not None:
            input_["cross_region_copy_targets"] = cross_region_copy_targets
        if exclusions is not None:
            input_["exclusions"] = exclusions

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
