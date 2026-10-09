"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#mediapackagev2``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mediapackagev2._auth._signers
import capo_mediapackagev2._auth._sigv4
from capo_mediapackagev2._auth._identity import Credentials
from capo_mediapackagev2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediapackagev2._auth._zapros_handler import AuthMiddleware
from capo_mediapackagev2._pagination import resolve_path as _resolve_path
from capo_mediapackagev2._resources.mediapackagev2.channel_group_resource import (
    ChannelGroupResource,
)
from capo_mediapackagev2._services._aws_config import aws_config
from capo_mediapackagev2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mediapackagev2.types.cancel_harvest_job_request
    import capo_mediapackagev2.types.cancel_harvest_job_response
    import capo_mediapackagev2.types.cdn_auth_configuration
    import capo_mediapackagev2.types.channel_group_list_configuration
    import capo_mediapackagev2.types.channel_list_configuration
    import capo_mediapackagev2.types.container_type
    import capo_mediapackagev2.types.create_channel_group_request
    import capo_mediapackagev2.types.create_channel_group_response
    import capo_mediapackagev2.types.create_channel_request
    import capo_mediapackagev2.types.create_channel_response
    import capo_mediapackagev2.types.create_dash_manifests
    import capo_mediapackagev2.types.create_harvest_job_request
    import capo_mediapackagev2.types.create_harvest_job_response
    import capo_mediapackagev2.types.create_hls_manifests
    import capo_mediapackagev2.types.create_low_latency_hls_manifests
    import capo_mediapackagev2.types.create_mss_manifests
    import capo_mediapackagev2.types.create_origin_endpoint_request
    import capo_mediapackagev2.types.create_origin_endpoint_response
    import capo_mediapackagev2.types.delete_channel_group_request
    import capo_mediapackagev2.types.delete_channel_group_response
    import capo_mediapackagev2.types.delete_channel_policy_request
    import capo_mediapackagev2.types.delete_channel_policy_response
    import capo_mediapackagev2.types.delete_channel_request
    import capo_mediapackagev2.types.delete_channel_response
    import capo_mediapackagev2.types.delete_origin_endpoint_policy_request
    import capo_mediapackagev2.types.delete_origin_endpoint_policy_response
    import capo_mediapackagev2.types.delete_origin_endpoint_request
    import capo_mediapackagev2.types.delete_origin_endpoint_response
    import capo_mediapackagev2.types.destination
    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.force_endpoint_error_configuration
    import capo_mediapackagev2.types.get_channel_group_request
    import capo_mediapackagev2.types.get_channel_group_response
    import capo_mediapackagev2.types.get_channel_policy_request
    import capo_mediapackagev2.types.get_channel_policy_response
    import capo_mediapackagev2.types.get_channel_request
    import capo_mediapackagev2.types.get_channel_response
    import capo_mediapackagev2.types.get_harvest_job_request
    import capo_mediapackagev2.types.get_harvest_job_response
    import capo_mediapackagev2.types.get_origin_endpoint_policy_request
    import capo_mediapackagev2.types.get_origin_endpoint_policy_response
    import capo_mediapackagev2.types.get_origin_endpoint_request
    import capo_mediapackagev2.types.get_origin_endpoint_response
    import capo_mediapackagev2.types.harvest_job
    import capo_mediapackagev2.types.harvest_job_status
    import capo_mediapackagev2.types.harvested_manifests
    import capo_mediapackagev2.types.harvester_schedule_configuration
    import capo_mediapackagev2.types.idempotency_token
    import capo_mediapackagev2.types.input_switch_configuration
    import capo_mediapackagev2.types.input_type
    import capo_mediapackagev2.types.list_channel_groups_request
    import capo_mediapackagev2.types.list_channel_groups_response
    import capo_mediapackagev2.types.list_channels_request
    import capo_mediapackagev2.types.list_channels_response
    import capo_mediapackagev2.types.list_harvest_jobs_request
    import capo_mediapackagev2.types.list_harvest_jobs_response
    import capo_mediapackagev2.types.list_origin_endpoints_request
    import capo_mediapackagev2.types.list_origin_endpoints_response
    import capo_mediapackagev2.types.list_resource_max_results
    import capo_mediapackagev2.types.list_tags_for_resource_request
    import capo_mediapackagev2.types.list_tags_for_resource_response
    import capo_mediapackagev2.types.multiview_configuration
    import capo_mediapackagev2.types.origin_endpoint_list_configuration
    import capo_mediapackagev2.types.output_header_configuration
    import capo_mediapackagev2.types.output_locking_mode
    import capo_mediapackagev2.types.policy_text
    import capo_mediapackagev2.types.put_channel_policy_request
    import capo_mediapackagev2.types.put_channel_policy_response
    import capo_mediapackagev2.types.put_origin_endpoint_policy_request
    import capo_mediapackagev2.types.put_origin_endpoint_policy_response
    import capo_mediapackagev2.types.reset_channel_state_request
    import capo_mediapackagev2.types.reset_channel_state_response
    import capo_mediapackagev2.types.reset_origin_endpoint_state_request
    import capo_mediapackagev2.types.reset_origin_endpoint_state_response
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.segment
    import capo_mediapackagev2.types.stream_name_output_mode
    import capo_mediapackagev2.types.tag_arn
    import capo_mediapackagev2.types.tag_key_list
    import capo_mediapackagev2.types.tag_map
    import capo_mediapackagev2.types.tag_resource_request
    import capo_mediapackagev2.types.untag_resource_request
    import capo_mediapackagev2.types.update_channel_group_request
    import capo_mediapackagev2.types.update_channel_group_response
    import capo_mediapackagev2.types.update_channel_request
    import capo_mediapackagev2.types.update_channel_response
    import capo_mediapackagev2.types.update_origin_endpoint_request
    import capo_mediapackagev2.types.update_origin_endpoint_response
    import capo_mediapackagev2.types.uri_separator


class MediaPackageV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MediaPackageV2Client:
    """A client for the ``MediaPackageV2`` service.

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
        self._config = MediaPackageV2ClientConfig(
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
        self.channel_group_resource = ChannelGroupResource(self)

    def operation_options(
        self, config_overrides: Optional[MediaPackageV2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaPackageV2ClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_mediapackagev2.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch resource that you want to view tags for.</p>

        Raises:
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all tags for a resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:mediapackagev2:us-west-2:123456789012:channelGroup/exampleChannelGroup/channel/exampleChannel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.list_tags_for_resource

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_mediapackagev2.types.tag_arn.TagArn",
        tags: "capo_mediapackagev2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> None:
        """<p>Assigns one of more tags (key-value pairs) to the specified MediaPackage resource.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values. You can use the TagResource operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p>

        Args:
            resource_arn: <p>The ARN of the MediaPackage resource that you're adding tags to.</p>
            tags: <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.</p>

        Raises:
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Add tags to a resource

            >>> client.tag_resource(resource_arn='arn:aws:mediapackagev2:us-west-2:123456789012:channelGroup/exampleChannelGroup/channel/exampleChannel', tags={'key3': 'value3', 'key4': 'value4'})
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediapackagev2._operations.mediapackagev2.tag_resource

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_mediapackagev2.types.tag_arn.TagArn",
        tag_keys: "capo_mediapackagev2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the MediaPackage resource that you're removing tags from.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove tags from a resource

            >>> client.untag_resource(resource_arn='arn:aws:mediapackagev2:us-west-2:123456789012:channelGroup/exampleChannelGroup/channel/exampleChannel', tag_keys=['key3', 'key4'])
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediapackagev2._operations.mediapackagev2.untag_resource

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.untag_resource_request.UntagResourceRequest = {
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

    def create_channel_group(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        client_token: Optional[
            "capo_mediapackagev2.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_mediapackagev2.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_mediapackagev2.types.tag_map.TagMap"] = None,
    ) -> "capo_mediapackagev2.types.create_channel_group_response.CreateChannelGroupResponse":
        """<p>Create a channel group to group your channels and origin endpoints. A channel group is the top-level resource that consists of channels and origin endpoints that are associated with it and that provides predictable URLs for stream delivery. All channels and origin endpoints within the channel group are guaranteed to share the DNS. You can create only one channel group with each request. </p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. You can't use spaces in the name. You can't change the name after you create the channel group.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            description: <p>Enter any descriptive text that helps you to identify the channel group.</p>
            tags: <p>A comma-separated list of tag key:value pairs that you define. For example:</p> <p> <code>"Key1": "Value1",</code> </p> <p> <code>"Key2": "Value2"</code> </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creating a Channel Group

            >>> client.create_channel_group(channel_group_name='exampleChannelGroup', description='Description for exampleChannelGroup', tags={'key1': 'value1', 'key2': 'value2'})
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.create_channel_group_request.CreateChannelGroupRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.create_channel_group_response.CreateChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.create_channel_group

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.create_channel_group.create_channel_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.create_channel_group_request.CreateChannelGroupRequest = {
            "channel_group_name": channel_group_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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

    def get_channel_group(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.get_channel_group_response.GetChannelGroupResponse":
        """<p>Retrieves the specified channel group that's configured in AWS Elemental MediaPackage.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Getting a Channel Group

            >>> client.get_channel_group(channel_group_name='exampleChannelGroup')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.get_channel_group_request.GetChannelGroupRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.get_channel_group_response.GetChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.get_channel_group

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.get_channel_group.get_channel_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.get_channel_group_request.GetChannelGroupRequest = {
            "channel_group_name": channel_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel_group(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        e_tag: Optional["capo_mediapackagev2.types.entity_tag.EntityTag"] = None,
        description: Optional[
            "capo_mediapackagev2.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_mediapackagev2.types.update_channel_group_response.UpdateChannelGroupResponse":
        """<p>Update the specified channel group. You can edit the description on a channel group for easier identification later from the AWS Elemental MediaPackage console. You can't edit the name of the channel group.</p> <p>Any edits you make that impact the video output may not be reflected for a few minutes.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            e_tag: <p>The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.</p>
            description: <p>Any descriptive information that you want to add to the channel group for future identification purposes.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updating a Channel Group

            >>> client.update_channel_group(channel_group_name='exampleChannelGroup', description='Updated description for exampleChannelGroup')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.update_channel_group_request.UpdateChannelGroupRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.update_channel_group_response.UpdateChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.update_channel_group

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.update_channel_group.update_channel_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.update_channel_group_request.UpdateChannelGroupRequest = {
            "channel_group_name": channel_group_name
        }
        if e_tag is not None:
            input_["e_tag"] = e_tag
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_group(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.delete_channel_group_response.DeleteChannelGroupResponse":
        """<p>Delete a channel group. You must delete the channel group's channels and origin endpoints before you can delete the channel group. If you delete a channel group, you'll lose access to the egress domain and will have to create a new channel group to replace it.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deleting a Channel Group

            >>> client.delete_channel_group(channel_group_name='exampleChannelGroup')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.delete_channel_group_request.DeleteChannelGroupRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.delete_channel_group_response.DeleteChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.delete_channel_group

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.delete_channel_group.delete_channel_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.delete_channel_group_request.DeleteChannelGroupRequest = {
            "channel_group_name": channel_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_channel_groups(
        self,
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediapackagev2.types.list_channel_groups_response.ListChannelGroupsResponse":
        """<p>Retrieves all channel groups that are configured in Elemental MediaPackage.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing all Channel Groups

            >>> client.list_channel_groups()
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.list_channel_groups_request.ListChannelGroupsRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.list_channel_groups_response.ListChannelGroupsResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.list_channel_groups

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.list_channel_groups.list_channel_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.list_channel_groups_request.ListChannelGroupsRequest = {}
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

    def iter_list_channel_groups(
        self,
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediapackagev2.types.channel_group_list_configuration.ChannelGroupListConfiguration]":
        _token = next_token
        while True:
            _response = self.list_channel_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_channel(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        client_token: Optional[
            "capo_mediapackagev2.types.idempotency_token.IdempotencyToken"
        ] = None,
        input_type: Optional["capo_mediapackagev2.types.input_type.InputType"] = None,
        description: Optional[
            "capo_mediapackagev2.types.resource_description.ResourceDescription"
        ] = None,
        input_switch_configuration: Optional[
            "capo_mediapackagev2.types.input_switch_configuration.InputSwitchConfiguration"
        ] = None,
        output_header_configuration: Optional[
            "capo_mediapackagev2.types.output_header_configuration.OutputHeaderConfiguration"
        ] = None,
        multiview_configuration: Optional[
            "capo_mediapackagev2.types.multiview_configuration.MultiviewConfiguration"
        ] = None,
        output_locking_mode: Optional[
            "capo_mediapackagev2.types.output_locking_mode.OutputLockingMode"
        ] = None,
        tags: Optional["capo_mediapackagev2.types.tag_map.TagMap"] = None,
    ) -> "capo_mediapackagev2.types.create_channel_response.CreateChannelResponse":
        """<p>Create a channel to start receiving content streams. The channel represents the input to MediaPackage for incoming live content from an encoder such as AWS Elemental MediaLive. The channel receives content, and after packaging it, outputs it through an origin endpoint to downstream devices (such as video players or CDNs) that request the content. You can create only one channel with each request. We recommend that you spread out channels between channel groups, such as putting redundant channels in the same AWS Region in different channel groups.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. You can't change the name after you create the channel.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            input_type: <p>The input type is an immutable field. It defines whether the channel allows CMAF ingest, HLS ingest, or server-side multiview output. Multiview channels receive no ingest of their own. If unprovided, the value defaults to HLS.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>HLS</code> - The HLS streaming specification (which defines M3U8 manifests and TS segments).</p> </li> <li> <p> <code>CMAF</code> - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).</p> </li> <li> <p> <code>MULTIVIEW</code> – Server-side multiview. The channel receives no ingest of its own. Instead, it composites video from the source channels in its <code>MultiviewConfiguration</code> into a single tiled output stream.</p> </li> </ul>
            description: <p>Enter any descriptive text that helps you to identify the channel.</p>
            input_switch_configuration: <p>The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>
            output_header_configuration: <p>The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>
            multiview_configuration: <p>The multiview configuration for the channel. This setting is required when <code>InputType</code> is <code>MULTIVIEW</code>, and can't be set for any other input type.</p>
            output_locking_mode: <p>The output locking mode for the channel. This setting is only valid when <code>InputType</code> is <code>CMAF</code>. This value is immutable after channel creation. If you don't specify a value, the default is <code>EPOCH_LOCKED</code>.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>EPOCH_LOCKED</code> - The channel uses epoch-locked behavior with deterministic sequence numbering and fixed segment boundaries aligned to epoch time. This mode supports cross-region synchronization and failover.</p> </li> <li> <p> <code>NON_EPOCH_LOCKED</code> - The channel uses non-epoch-locked behavior with duration-based segment combining and monotonically increasing sequence numbers starting from 0. This mode does not support cross-region synchronization or failover.</p> </li> </ul>
            tags: <p>A comma-separated list of tag key:value pairs that you define. For example:</p> <p> <code>"Key1": "Value1",</code> </p> <p> <code>"Key2": "Value2"</code> </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creating a Channel

            >>> client.create_channel(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', input_type='HLS', description='Description for exampleChannel', tags={'key1': 'value1', 'key2': 'value2'})
            Creating a CMAF Channel with non-epoch-locked output locking mode

            >>> client.create_channel(channel_group_name='exampleChannelGroup', channel_name='exampleCmafChannel', input_type='CMAF', output_locking_mode='NON_EPOCH_LOCKED', description='Non-epoch-locked CMAF channel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.create_channel

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.create_channel_request.CreateChannelRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if input_type is not None:
            input_["input_type"] = input_type
        if description is not None:
            input_["description"] = description
        if input_switch_configuration is not None:
            input_["input_switch_configuration"] = input_switch_configuration
        if output_header_configuration is not None:
            input_["output_header_configuration"] = output_header_configuration
        if multiview_configuration is not None:
            input_["multiview_configuration"] = multiview_configuration
        if output_locking_mode is not None:
            input_["output_locking_mode"] = output_locking_mode
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.get_channel_response.GetChannelResponse":
        """<p>Retrieves the specified channel that's configured in AWS Elemental MediaPackage.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Getting a Channel

            >>> client.get_channel(channel_group_name='exampleChannelGroup', channel_name='exampleChannel')
            Getting a CMAF Channel with non-epoch-locked output locking mode

            >>> client.get_channel(channel_group_name='exampleChannelGroup', channel_name='exampleCmafChannel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.get_channel_request.GetChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.get_channel_response.GetChannelResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.get_channel

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.get_channel.get_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.get_channel_request.GetChannelRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        e_tag: Optional["capo_mediapackagev2.types.entity_tag.EntityTag"] = None,
        description: Optional[
            "capo_mediapackagev2.types.resource_description.ResourceDescription"
        ] = None,
        input_switch_configuration: Optional[
            "capo_mediapackagev2.types.input_switch_configuration.InputSwitchConfiguration"
        ] = None,
        output_header_configuration: Optional[
            "capo_mediapackagev2.types.output_header_configuration.OutputHeaderConfiguration"
        ] = None,
        multiview_configuration: Optional[
            "capo_mediapackagev2.types.multiview_configuration.MultiviewConfiguration"
        ] = None,
    ) -> "capo_mediapackagev2.types.update_channel_response.UpdateChannelResponse":
        """<p>Update the specified channel. You can edit if MediaPackage sends ingest or egress access logs to the CloudWatch log group, if content will be encrypted, the description on a channel, and your channel's policy settings. You can't edit the name of the channel or CloudFront distribution details.</p> <p>Any edits you make that impact the video output may not be reflected for a few minutes.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            e_tag: <p>The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.</p>
            description: <p>Any descriptive information that you want to add to the channel for future identification purposes.</p>
            input_switch_configuration: <p>The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>
            output_header_configuration: <p>The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>
            multiview_configuration: <p>The multiview configuration for the channel. This setting is required when the channel's <code>InputType</code> is <code>MULTIVIEW</code>, and can't be set for any other input type. Because <code>InputType</code> is immutable, you can change a multiview channel's sources and layouts. You can't add or remove the multiview configuration itself.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updating a Channel

            >>> client.update_channel(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', description='Updated description for exampleChannel')
            Updating a CMAF Channel with non-epoch-locked output locking mode

            >>> client.update_channel(channel_group_name='exampleChannelGroup', channel_name='exampleCmafChannel', description='Updated non-epoch-locked CMAF channel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.update_channel

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.update_channel_request.UpdateChannelRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }
        if e_tag is not None:
            input_["e_tag"] = e_tag
        if description is not None:
            input_["description"] = description
        if input_switch_configuration is not None:
            input_["input_switch_configuration"] = input_switch_configuration
        if output_header_configuration is not None:
            input_["output_header_configuration"] = output_header_configuration
        if multiview_configuration is not None:
            input_["multiview_configuration"] = multiview_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.delete_channel_response.DeleteChannelResponse":
        """<p>Delete a channel to stop AWS Elemental MediaPackage from receiving further content. You must delete the channel's origin endpoints before you can delete the channel.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deleting a Channel

            >>> client.delete_channel(channel_group_name='exampleChannelGroup', channel_name='exampleChannel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.delete_channel

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.delete_channel_request.DeleteChannelRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_channels(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediapackagev2.types.list_channels_response.ListChannelsResponse":
        """<p>Retrieves all channels in a specific channel group that are configured in AWS Elemental MediaPackage.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing all Channels

            >>> client.list_channels(channel_group_name='exampleChannelGroup')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.list_channels

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.list_channels_request.ListChannelsRequest = {
            "channel_group_name": channel_group_name
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

    def iter_list_channels(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediapackagev2.types.channel_list_configuration.ChannelListConfiguration]":
        _token = next_token
        while True:
            _response = self.list_channels(
                channel_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def reset_channel_state(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.reset_channel_state_response.ResetChannelStateResponse":
        """<p>Resetting the channel can help to clear errors from misconfigurations in the encoder. A reset refreshes the ingest stream and removes previous content. </p> <p> Be sure to stop the encoder before you reset the channel, and wait at least 30 seconds before you restart the encoder. </p>

        Args:
            channel_group_name: <p>The name of the channel group that contains the channel that you are resetting.</p>
            channel_name: <p>The name of the channel that you are resetting.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Reset a Channel

            >>> client.reset_channel_state(channel_group_name='exampleChannelGroup', channel_name='exampleChannel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.reset_channel_state_request.ResetChannelStateRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.reset_channel_state_response.ResetChannelStateResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.reset_channel_state

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.reset_channel_state.reset_channel_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.reset_channel_state_request.ResetChannelStateRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_channel_policy(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        policy: "capo_mediapackagev2.types.policy_text.PolicyText",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> (
        "capo_mediapackagev2.types.put_channel_policy_response.PutChannelPolicyResponse"
    ):
        """<p>Attaches an IAM policy to the specified channel. With policies, you can specify who has access to AWS resources and what actions they can perform on those resources. You can attach only one policy with each request.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            policy: <p>The policy to attach to the specified channel.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creating a Channel Policy

            >>> client.put_channel_policy(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', policy='{...}')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.put_channel_policy_request.PutChannelPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.put_channel_policy_response.PutChannelPolicyResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.put_channel_policy

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.put_channel_policy.put_channel_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.put_channel_policy_request.PutChannelPolicyRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_policy(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> (
        "capo_mediapackagev2.types.get_channel_policy_response.GetChannelPolicyResponse"
    ):
        """<p>Retrieves the specified channel policy that's configured in AWS Elemental MediaPackage. With policies, you can specify who has access to AWS resources and what actions they can perform on those resources.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Getting a Channel Policy

            >>> client.get_channel_policy(channel_group_name='exampleChannelGroup', channel_name='exampleChannel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.get_channel_policy_request.GetChannelPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.get_channel_policy_response.GetChannelPolicyResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.get_channel_policy

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.get_channel_policy.get_channel_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.get_channel_policy_request.GetChannelPolicyRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_policy(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.delete_channel_policy_response.DeleteChannelPolicyResponse":
        """<p>Delete a channel policy.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deleting a Channel Policy

            >>> client.delete_channel_policy(channel_group_name='exampleChannelGroup', channel_name='exampleChannel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.delete_channel_policy_request.DeleteChannelPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.delete_channel_policy_response.DeleteChannelPolicyResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.delete_channel_policy

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.delete_channel_policy.delete_channel_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.delete_channel_policy_request.DeleteChannelPolicyRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_origin_endpoint(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        container_type: "capo_mediapackagev2.types.container_type.ContainerType",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        segment: Optional["capo_mediapackagev2.types.segment.Segment"] = None,
        client_token: Optional[
            "capo_mediapackagev2.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_mediapackagev2.types.resource_description.ResourceDescription"
        ] = None,
        startover_window_seconds: Optional[int] = None,
        hls_manifests: Optional[
            "capo_mediapackagev2.types.create_hls_manifests.CreateHlsManifests"
        ] = None,
        low_latency_hls_manifests: Optional[
            "capo_mediapackagev2.types.create_low_latency_hls_manifests.CreateLowLatencyHlsManifests"
        ] = None,
        dash_manifests: Optional[
            "capo_mediapackagev2.types.create_dash_manifests.CreateDashManifests"
        ] = None,
        mss_manifests: Optional[
            "capo_mediapackagev2.types.create_mss_manifests.CreateMssManifests"
        ] = None,
        force_endpoint_error_configuration: Optional[
            "capo_mediapackagev2.types.force_endpoint_error_configuration.ForceEndpointErrorConfiguration"
        ] = None,
        uri_separator: Optional[
            "capo_mediapackagev2.types.uri_separator.UriSeparator"
        ] = None,
        stream_name_output_mode: Optional[
            "capo_mediapackagev2.types.stream_name_output_mode.StreamNameOutputMode"
        ] = None,
        tags: Optional["capo_mediapackagev2.types.tag_map.TagMap"] = None,
    ) -> "capo_mediapackagev2.types.create_origin_endpoint_response.CreateOriginEndpointResponse":
        """<p>The endpoint is attached to a channel, and represents the output of the live content. You can associate multiple endpoints to a single channel. Each endpoint gives players and downstream CDNs (such as Amazon CloudFront) access to the content for playback. Content can't be served from a channel until it has an endpoint. You can create only one endpoint with each request. </p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            origin_endpoint_name: <p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and must be unique for your account in the AWS Region and channel. You can't use spaces in the name. You can't change the name after you create the endpoint.</p>
            container_type: <p>The type of container to attach to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. You can't change the container type after you create the endpoint.</p>
            segment: <p>The segment configuration, including the segment name, duration, and other configuration values.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            description: <p>Enter any descriptive text that helps you to identify the origin endpoint.</p>
            startover_window_seconds: <p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p>
            hls_manifests: <p>An HTTP live streaming (HLS) manifest configuration.</p>
            low_latency_hls_manifests: <p>A low-latency HLS manifest configuration.</p>
            dash_manifests: <p>A DASH manifest configuration.</p>
            mss_manifests: <p>A list of Microsoft Smooth Streaming (MSS) manifest configurations for the origin endpoint. You can configure multiple MSS manifests to provide different streaming experiences or to support different client requirements.</p>
            force_endpoint_error_configuration: <p>The failover settings for the endpoint.</p>
            uri_separator: <p>The separator character to use in generated URIs for this origin endpoint. This setting applies to all manifest types on the endpoint. If you don't specify a value, the default is <code>UNDERSCORE</code>.</p>
            stream_name_output_mode: <p>The output mode for stream names in egress manifests. This setting is valid only when the associated channel's <code>InputType</code> is <code>HLS</code>. You can't change the stream name output mode after you create the endpoint.</p> <p> <code>INDEX</code> uses numeric indices for stream names (for example, 1, 2, 3). <code>PASSTHROUGH_NAME</code> uses the stream names from the input manifest. If you don't specify a value, the default is <code>INDEX</code>.</p>
            tags: <p>A comma-separated list of tag key:value pairs that you define. For example:</p> <p> <code>"Key1": "Value1",</code> </p> <p> <code>"Key2": "Value2"</code> </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creating an OriginEndpoint with container type TS, and encryption enabled

            >>> client.create_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointTS', container_type='TS', description='Description for exampleOriginEndpointTS', startover_window_seconds=300, force_endpoint_error_configuration={'EndpointErrorConditions': ['STALE_MANIFEST', 'INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT']}, uri_separator='UNDERSCORE', stream_name_output_mode='INDEX', segment={'SegmentDurationSeconds': 6, 'SegmentName': 'segmentName', 'TsUseAudioRenditionGroup': True, 'IncludeIframeOnlyStreams': True, 'TsIncludeDvbSubtitles': True, 'Scte': {'ScteFilter': ['SPLICE_INSERT', 'BREAK']}, 'Encryption': {'ConstantInitializationVector': 'A382A901F3C1F7718512266CFFBB0B7E', 'EncryptionMethod': {'TsEncryptionMethod': 'AES_128'}, 'KeyRotationIntervalSeconds': 300, 'SpekeKeyProvider': {'EncryptionContractConfiguration': {'PresetSpeke20Audio': 'SHARED', 'PresetSpeke20Video': 'SHARED'}, 'ResourceId': 'ResourceId', 'DrmSystems': ['CLEAR_KEY_AES_128'], 'RoleArn': 'arn:aws:iam::123456789012:role/empRole', 'Url': 'https://foo.com', 'CertificateArn': 'arn:aws:acm:us-west-2:123456789012:certificate/0c6a65f1-7bd3-48ac-be17-f38675def22e'}}}, hls_manifests=[{'ManifestName': 'exampleManifest1', 'ChildManifestName': 'exampleChildManifest1', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60, 'UriPathType': 'ROOT'}, {'ManifestName': 'exampleManifest2', 'ChildManifestName': 'exampleManifest2', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60, 'UriPathType': 'ROOT'}], low_latency_hls_manifests=[{'ManifestName': 'exampleLLManifest1', 'ChildManifestName': 'exampleLLChildManifest1', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60}, {'ManifestName': 'exampleLLManifest2', 'ChildManifestName': 'exampleLLManifest2', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60}], tags={'key1': 'value1', 'key2': 'value2'})
            Creating an OriginEndpoint with container type CMAF, and encryption enabled

            >>> client.create_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointCMAF', container_type='CMAF', startover_window_seconds=300, force_endpoint_error_configuration={'EndpointErrorConditions': ['STALE_MANIFEST', 'INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT']}, uri_separator='UNDERSCORE', segment={'SegmentDurationSeconds': 6, 'SegmentName': 'segmentName', 'IncludeIframeOnlyStreams': True, 'Scte': {'ScteFilter': ['SPLICE_INSERT', 'BREAK']}, 'Encryption': {'ConstantInitializationVector': 'A382A901F3C1F7718512266CFFBB0B9F', 'EncryptionMethod': {'CmafEncryptionMethod': 'CBCS'}, 'KeyRotationIntervalSeconds': 300, 'SpekeKeyProvider': {'EncryptionContractConfiguration': {'PresetSpeke20Audio': 'PRESET_AUDIO_1', 'PresetSpeke20Video': 'PRESET_VIDEO_1'}, 'ResourceId': 'ResourceId', 'DrmSystems': ['PLAYREADY', 'WIDEVINE'], 'RoleArn': 'arn:aws:iam::123456789012:role/empRole', 'Url': 'https://foo.com', 'CertificateArn': 'arn:aws:acm:us-west-2:123456789012:certificate/0c6a65f1-7bd3-48ac-be17-f38675def22e'}}, 'OutputTimestampMode': 'REBASED_TO_CHANNEL_START'}, hls_manifests=[{'ManifestName': 'exampleManifest1', 'ChildManifestName': 'exampleChildManifest1', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60}, {'ManifestName': 'exampleManifest2', 'ChildManifestName': 'exampleManifest2', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60}], low_latency_hls_manifests=[{'ManifestName': 'exampleLLManifest1', 'ChildManifestName': 'exampleLLChildManifest1', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60}, {'ManifestName': 'exampleLLManifest2', 'ChildManifestName': 'exampleLLManifest2', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60}], dash_manifests=[{'ManifestName': 'exampleDashManifest1', 'ManifestWindowSeconds': 300, 'MinUpdatePeriodSeconds': 5, 'MinBufferTimeSeconds': 30, 'SuggestedPresentationDelaySeconds': 2, 'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE', 'PeriodTriggers': ['AVAILS'], 'ScteDash': {'AdMarkerDash': 'XML'}, 'DrmSignaling': 'INDIVIDUAL', 'UtcTiming': {'TimingMode': 'HTTP_HEAD', 'TimingSource': 'example'}, 'Profiles': ['DVB_DASH'], 'BaseUrls': [{'Url': 'http://example.com/', 'ServiceLocation': 'A', 'DvbPriority': 1, 'DvbWeight': 3}], 'ProgramInformation': {'Title': 'exampleTitle', 'Source': 'exampleSource', 'Copyright': '(c) Example. All rights reserved', 'LanguageCode': 'en', 'MoreInformationUrl': 'https://example.com/more-information'}, 'DvbSettings': {'FontDownload': {'Url': 'https://example.com/fonts/SubtitleDisplay.woff', 'MimeType': 'application/font', 'FontFamily': 'SubtitleDisplay'}, 'ErrorMetrics': [{'ReportingUrl': 'https://example.com/dvb-errors/errors', 'Probability': 500}]}, 'Compactness': 'STANDARD'}, {'ManifestName': 'exampleDashManifest2', 'ManifestWindowSeconds': 60, 'MinUpdatePeriodSeconds': 3, 'MinBufferTimeSeconds': 9, 'SuggestedPresentationDelaySeconds': 12, 'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE', 'PeriodTriggers': ['AVAILS', 'DRM_KEY_ROTATION', 'SOURCE_CHANGES', 'SOURCE_DISRUPTIONS'], 'ScteDash': {'AdMarkerDash': 'XML'}, 'DrmSignaling': 'INDIVIDUAL', 'UtcTiming': {'TimingMode': 'HTTP_HEAD', 'TimingSource': 'example'}, 'Profiles': ['DVB_DASH'], 'BaseUrls': [{'Url': 'http://example2.com/', 'ServiceLocation': 'B', 'DvbPriority': 2, 'DvbWeight': 2}], 'ProgramInformation': {'Title': 'exampleTitle2', 'Source': 'exampleSource2', 'Copyright': '(c) Example. All rights reserved', 'LanguageCode': 'en', 'MoreInformationUrl': 'https://example2.com/more-information'}, 'DvbSettings': {'FontDownload': {'Url': 'https://example.com/fonts/SubtitleDisplay.woff', 'MimeType': 'application/font', 'FontFamily': 'SubtitleDisplay'}, 'ErrorMetrics': [{'ReportingUrl': 'https://example2.com/dvb-errors/errors', 'Probability': 600}]}, 'Compactness': 'STANDARD', 'AvailabilityStartTimeConfiguration': {'FixedAvailabilityStartTime': '2026-04-17T23:00:00.00Z'}}], tags={'key1': 'value1', 'key2': 'value2'})
            Creating an OriginEndpoint with container type ISM, and encryption enabled

            >>> client.create_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointISM', container_type='ISM', description='Description for exampleOriginEndpointISM', startover_window_seconds=300, force_endpoint_error_configuration={'EndpointErrorConditions': ['STALE_MANIFEST', 'INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT']}, uri_separator='UNDERSCORE', segment={'SegmentDurationSeconds': 2, 'SegmentName': 'segmentName', 'Encryption': {'EncryptionMethod': {'IsmEncryptionMethod': 'CENC'}, 'SpekeKeyProvider': {'EncryptionContractConfiguration': {'PresetSpeke20Audio': 'SHARED', 'PresetSpeke20Video': 'SHARED'}, 'ResourceId': 'ResourceId', 'DrmSystems': ['PLAYREADY'], 'RoleArn': 'arn:aws:iam::123456789012:role/empRole', 'Url': 'https://speke-key-provider.example.com'}}}, mss_manifests=[{'ManifestName': 'exampleMssManifest1', 'ManifestWindowSeconds': 60, 'ManifestLayout': 'FULL'}], tags={'key1': 'value1', 'key2': 'value2'})
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.create_origin_endpoint_request.CreateOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.create_origin_endpoint_response.CreateOriginEndpointResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.create_origin_endpoint

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.create_origin_endpoint.create_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.create_origin_endpoint_request.CreateOriginEndpointRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
            "container_type": container_type,
        }
        if segment is not None:
            input_["segment"] = segment
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if startover_window_seconds is not None:
            input_["startover_window_seconds"] = startover_window_seconds
        if hls_manifests is not None:
            input_["hls_manifests"] = hls_manifests
        if low_latency_hls_manifests is not None:
            input_["low_latency_hls_manifests"] = low_latency_hls_manifests
        if dash_manifests is not None:
            input_["dash_manifests"] = dash_manifests
        if mss_manifests is not None:
            input_["mss_manifests"] = mss_manifests
        if force_endpoint_error_configuration is not None:
            input_["force_endpoint_error_configuration"] = (
                force_endpoint_error_configuration
            )
        if uri_separator is not None:
            input_["uri_separator"] = uri_separator
        if stream_name_output_mode is not None:
            input_["stream_name_output_mode"] = stream_name_output_mode
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_origin_endpoint(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.get_origin_endpoint_response.GetOriginEndpointResponse":
        """<p>Retrieves the specified origin endpoint that's configured in AWS Elemental MediaPackage to obtain its playback URL and to view the packaging settings that it's currently using.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            origin_endpoint_name: <p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Getting an OriginEndpoint

            >>> client.get_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointTS')
            Getting an OriginEndpoint with ISM container

            >>> client.get_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointISM')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.get_origin_endpoint_request.GetOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.get_origin_endpoint_response.GetOriginEndpointResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.get_origin_endpoint

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.get_origin_endpoint.get_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.get_origin_endpoint_request.GetOriginEndpointRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_origin_endpoint(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        container_type: "capo_mediapackagev2.types.container_type.ContainerType",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        segment: Optional["capo_mediapackagev2.types.segment.Segment"] = None,
        description: Optional[
            "capo_mediapackagev2.types.resource_description.ResourceDescription"
        ] = None,
        startover_window_seconds: Optional[int] = None,
        hls_manifests: Optional[
            "capo_mediapackagev2.types.create_hls_manifests.CreateHlsManifests"
        ] = None,
        low_latency_hls_manifests: Optional[
            "capo_mediapackagev2.types.create_low_latency_hls_manifests.CreateLowLatencyHlsManifests"
        ] = None,
        dash_manifests: Optional[
            "capo_mediapackagev2.types.create_dash_manifests.CreateDashManifests"
        ] = None,
        mss_manifests: Optional[
            "capo_mediapackagev2.types.create_mss_manifests.CreateMssManifests"
        ] = None,
        force_endpoint_error_configuration: Optional[
            "capo_mediapackagev2.types.force_endpoint_error_configuration.ForceEndpointErrorConfiguration"
        ] = None,
        uri_separator: Optional[
            "capo_mediapackagev2.types.uri_separator.UriSeparator"
        ] = None,
        stream_name_output_mode: Optional[
            "capo_mediapackagev2.types.stream_name_output_mode.StreamNameOutputMode"
        ] = None,
        e_tag: Optional["capo_mediapackagev2.types.entity_tag.EntityTag"] = None,
    ) -> "capo_mediapackagev2.types.update_origin_endpoint_response.UpdateOriginEndpointResponse":
        """<p>Update the specified origin endpoint. Edit the packaging preferences on an endpoint to optimize the viewing experience. You can't edit the name of the endpoint.</p> <p>Any edits you make that impact the video output may not be reflected for a few minutes.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            origin_endpoint_name: <p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>
            container_type: <p>The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. </p>
            segment: <p>The segment configuration, including the segment name, duration, and other configuration values.</p>
            description: <p>Any descriptive information that you want to add to the origin endpoint for future identification purposes.</p>
            startover_window_seconds: <p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p>
            hls_manifests: <p>An HTTP live streaming (HLS) manifest configuration.</p>
            low_latency_hls_manifests: <p>A low-latency HLS manifest configuration.</p>
            dash_manifests: <p>A DASH manifest configuration.</p>
            mss_manifests: <p>A list of Microsoft Smooth Streaming (MSS) manifest configurations to update for the origin endpoint. This replaces the existing MSS manifest configurations.</p>
            force_endpoint_error_configuration: <p>The failover settings for the endpoint.</p>
            uri_separator: <p>The separator character to use in generated URIs for this origin endpoint. This setting applies to all manifest types on the endpoint. If you don't specify a value in the update request, the current value is preserved.</p>
            stream_name_output_mode: <p>The output mode for stream names in egress manifests. If you provide a value, it must match the current value. You can't change the stream name output mode after you create the endpoint.</p>
            e_tag: <p>The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updating an OriginEndpoint

            >>> client.update_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointTS', container_type='TS', description='Updated description for exampleOriginEndpointTS', startover_window_seconds=600, force_endpoint_error_configuration={'EndpointErrorConditions': ['STALE_MANIFEST', 'INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT']}, uri_separator='HYPHEN', segment={'SegmentDurationSeconds': 7, 'SegmentName': 'segmentName2', 'TsUseAudioRenditionGroup': True, 'IncludeIframeOnlyStreams': False, 'TsIncludeDvbSubtitles': False, 'Scte': {'ScteFilter': ['SPLICE_INSERT']}, 'Encryption': {'ConstantInitializationVector': 'A382A901F3C1F7718512266CFFBB0B7E', 'EncryptionMethod': {'TsEncryptionMethod': 'AES_128'}, 'KeyRotationIntervalSeconds': 300, 'SpekeKeyProvider': {'EncryptionContractConfiguration': {'PresetSpeke20Audio': 'SHARED', 'PresetSpeke20Video': 'SHARED'}, 'ResourceId': 'ResourceId', 'DrmSystems': ['CLEAR_KEY_AES_128'], 'RoleArn': 'arn:aws:iam::123456789012:role/empRole', 'Url': 'https://foo.com', 'CertificateArn': 'arn:aws:acm:us-west-2:123456789012:certificate/0c6a65f1-7bd3-48ac-be17-f38675def22e'}}}, hls_manifests=[{'ManifestName': 'exampleManifest1', 'ChildManifestName': 'exampleChildManifest1', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60, 'UriPathType': 'LEAF'}, {'ManifestName': 'exampleManifest2', 'ChildManifestName': 'exampleManifest2', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60, 'UriPathType': 'LEAF'}], low_latency_hls_manifests=[{'ManifestName': 'exampleLLManifest1', 'ChildManifestName': 'exampleLLChildManifest1', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60, 'UriPathType': 'ROOT'}, {'ManifestName': 'exampleLLManifest2', 'ChildManifestName': 'exampleLLManifest2', 'ScteHls': {'AdMarkerHls': 'DATERANGE'}, 'ManifestWindowSeconds': 30, 'ProgramDateTimeIntervalSeconds': 60, 'UriPathType': 'ROOT'}])
            Updating an OriginEndpoint with ISM container

            >>> client.update_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointISM', container_type='ISM', description='Updated description for exampleOriginEndpointISM', startover_window_seconds=600, force_endpoint_error_configuration={'EndpointErrorConditions': ['STALE_MANIFEST', 'INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT']}, uri_separator='HYPHEN', segment={'SegmentDurationSeconds': 2, 'SegmentName': 'segmentName2', 'Encryption': {'EncryptionMethod': {'IsmEncryptionMethod': 'CENC'}, 'SpekeKeyProvider': {'EncryptionContractConfiguration': {'PresetSpeke20Audio': 'SHARED', 'PresetSpeke20Video': 'SHARED'}, 'ResourceId': 'ResourceId', 'DrmSystems': ['PLAYREADY'], 'RoleArn': 'arn:aws:iam::123456789012:role/empRole', 'Url': 'https://speke-key-provider.example.com'}}}, mss_manifests=[{'ManifestName': 'exampleMssManifest1', 'ManifestWindowSeconds': 60, 'ManifestLayout': 'FULL'}, {'ManifestName': 'exampleMssManifest2', 'ManifestWindowSeconds': 30, 'ManifestLayout': 'COMPACT'}])
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.update_origin_endpoint_request.UpdateOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.update_origin_endpoint_response.UpdateOriginEndpointResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.update_origin_endpoint

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.update_origin_endpoint.update_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.update_origin_endpoint_request.UpdateOriginEndpointRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
            "container_type": container_type,
        }
        if segment is not None:
            input_["segment"] = segment
        if description is not None:
            input_["description"] = description
        if startover_window_seconds is not None:
            input_["startover_window_seconds"] = startover_window_seconds
        if hls_manifests is not None:
            input_["hls_manifests"] = hls_manifests
        if low_latency_hls_manifests is not None:
            input_["low_latency_hls_manifests"] = low_latency_hls_manifests
        if dash_manifests is not None:
            input_["dash_manifests"] = dash_manifests
        if mss_manifests is not None:
            input_["mss_manifests"] = mss_manifests
        if force_endpoint_error_configuration is not None:
            input_["force_endpoint_error_configuration"] = (
                force_endpoint_error_configuration
            )
        if uri_separator is not None:
            input_["uri_separator"] = uri_separator
        if stream_name_output_mode is not None:
            input_["stream_name_output_mode"] = stream_name_output_mode
        if e_tag is not None:
            input_["e_tag"] = e_tag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_origin_endpoint(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.delete_origin_endpoint_response.DeleteOriginEndpointResponse":
        """<p>Origin endpoints can serve content until they're deleted. Delete the endpoint if it should no longer respond to playback requests. You must delete all endpoints from a channel before you can delete the channel.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            origin_endpoint_name: <p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deleting an OriginEndpoint

            >>> client.delete_origin_endpoint(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpointTS')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.delete_origin_endpoint_request.DeleteOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.delete_origin_endpoint_response.DeleteOriginEndpointResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.delete_origin_endpoint

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.delete_origin_endpoint.delete_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.delete_origin_endpoint_request.DeleteOriginEndpointRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_origin_endpoints(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediapackagev2.types.list_origin_endpoints_response.ListOriginEndpointsResponse":
        """<p>Retrieves all origin endpoints in a specific channel that are configured in AWS Elemental MediaPackage.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing all OriginEndpoints

            >>> client.list_origin_endpoints(channel_group_name='exampleChannelGroup', channel_name='exampleChannel')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.list_origin_endpoints_request.ListOriginEndpointsRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.list_origin_endpoints_response.ListOriginEndpointsResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.list_origin_endpoints

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.list_origin_endpoints.list_origin_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.list_origin_endpoints_request.ListOriginEndpointsRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
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

    def iter_list_origin_endpoints(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediapackagev2.types.origin_endpoint_list_configuration.OriginEndpointListConfiguration]":
        _token = next_token
        while True:
            _response = self.list_origin_endpoints(
                channel_group_name,
                channel_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def reset_origin_endpoint_state(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.reset_origin_endpoint_state_response.ResetOriginEndpointStateResponse":
        """<p>Resetting the origin endpoint can help to resolve unexpected behavior and other content packaging issues. It also helps to preserve special events when you don't want the previous content to be available for viewing. A reset clears out all previous content from the origin endpoint.</p> <p>MediaPackage might return old content from this endpoint in the first 30 seconds after the endpoint reset. For best results, when possible, wait 30 seconds from endpoint reset to send playback requests to this endpoint. </p>

        Args:
            channel_group_name: <p>The name of the channel group that contains the channel with the origin endpoint that you are resetting.</p>
            channel_name: <p>The name of the channel with the origin endpoint that you are resetting.</p>
            origin_endpoint_name: <p>The name of the origin endpoint that you are resetting.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Reset an OriginEndpoint

            >>> client.reset_origin_endpoint_state(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpoint')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.reset_origin_endpoint_state_request.ResetOriginEndpointStateRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.reset_origin_endpoint_state_response.ResetOriginEndpointStateResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.reset_origin_endpoint_state

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.reset_origin_endpoint_state.reset_origin_endpoint_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.reset_origin_endpoint_state_request.ResetOriginEndpointStateRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_origin_endpoint_policy(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        policy: "capo_mediapackagev2.types.policy_text.PolicyText",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        cdn_auth_configuration: Optional[
            "capo_mediapackagev2.types.cdn_auth_configuration.CdnAuthConfiguration"
        ] = None,
    ) -> "capo_mediapackagev2.types.put_origin_endpoint_policy_response.PutOriginEndpointPolicyResponse":
        """<p>Attaches an IAM policy to the specified origin endpoint. You can attach only one policy with each request.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            origin_endpoint_name: <p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>
            policy: <p>The policy to attach to the specified origin endpoint.</p>
            cdn_auth_configuration: <p>The settings for using authorization headers between the MediaPackage endpoint and your CDN. </p> <p>For information about CDN authorization, see <a href="https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth.html">CDN authorization in Elemental MediaPackage</a> in the MediaPackage user guide. </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creating an Origin Endpoint Policy

            >>> client.put_origin_endpoint_policy(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpoint', policy='{...}')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.put_origin_endpoint_policy_request.PutOriginEndpointPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.put_origin_endpoint_policy_response.PutOriginEndpointPolicyResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.put_origin_endpoint_policy

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.put_origin_endpoint_policy.put_origin_endpoint_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.put_origin_endpoint_policy_request.PutOriginEndpointPolicyRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
            "policy": policy,
        }
        if cdn_auth_configuration is not None:
            input_["cdn_auth_configuration"] = cdn_auth_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_origin_endpoint_policy(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.get_origin_endpoint_policy_response.GetOriginEndpointPolicyResponse":
        """<p>Retrieves the specified origin endpoint policy that's configured in AWS Elemental MediaPackage.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            origin_endpoint_name: <p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Getting an Origin Endpoint Policy

            >>> client.get_origin_endpoint_policy(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpoint')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.get_origin_endpoint_policy_request.GetOriginEndpointPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.get_origin_endpoint_policy_response.GetOriginEndpointPolicyResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.get_origin_endpoint_policy

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.get_origin_endpoint_policy.get_origin_endpoint_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.get_origin_endpoint_policy_request.GetOriginEndpointPolicyRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_origin_endpoint_policy(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.delete_origin_endpoint_policy_response.DeleteOriginEndpointPolicyResponse":
        """<p>Delete an origin endpoint policy.</p>

        Args:
            channel_group_name: <p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>
            channel_name: <p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>
            origin_endpoint_name: <p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deleting an Origin Endpoint Policy

            >>> client.delete_origin_endpoint_policy(channel_group_name='exampleChannelGroup', channel_name='exampleChannel', origin_endpoint_name='exampleOriginEndpoint')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.delete_origin_endpoint_policy_request.DeleteOriginEndpointPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.delete_origin_endpoint_policy_response.DeleteOriginEndpointPolicyResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.delete_origin_endpoint_policy

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.delete_origin_endpoint_policy.delete_origin_endpoint_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.delete_origin_endpoint_policy_request.DeleteOriginEndpointPolicyRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_harvest_job(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        harvested_manifests: "capo_mediapackagev2.types.harvested_manifests.HarvestedManifests",
        schedule_configuration: "capo_mediapackagev2.types.harvester_schedule_configuration.HarvesterScheduleConfiguration",
        destination: "capo_mediapackagev2.types.destination.Destination",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        description: Optional[
            "capo_mediapackagev2.types.resource_description.ResourceDescription"
        ] = None,
        client_token: Optional[
            "capo_mediapackagev2.types.idempotency_token.IdempotencyToken"
        ] = None,
        harvest_job_name: Optional[
            "capo_mediapackagev2.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_mediapackagev2.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_mediapackagev2.types.create_harvest_job_response.CreateHarvestJobResponse"
    ):
        """<p>Creates a new harvest job to export content from a MediaPackage v2 channel to an S3 bucket.</p>

        Args:
            channel_group_name: <p>The name of the channel group containing the channel from which to harvest content.</p>
            channel_name: <p>The name of the channel from which to harvest content.</p>
            origin_endpoint_name: <p>The name of the origin endpoint from which to harvest content.</p>
            description: <p>An optional description for the harvest job.</p>
            harvested_manifests: <p>A list of manifests to be harvested.</p>
            schedule_configuration: <p>The configuration for when the harvest job should run, including start and end times.</p>
            destination: <p>The S3 destination where the harvested content will be placed.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            harvest_job_name: <p>A name for the harvest job. This name must be unique within the channel.</p>
            tags: <p>A collection of tags associated with the harvest job.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creating a Harvest Job

            >>> client.create_harvest_job(channel_group_name='exampleChannelGroup', channel_name='exampleChannelName', origin_endpoint_name='exampleOriginEndpointName', description='Example HarvestJob description', harvested_manifests={'HlsManifests': [{'ManifestName': 'HlsManifest'}], 'DashManifests': [{'ManifestName': 'DashManifest'}], 'LowLatencyHlsManifests': [{'ManifestName': 'LowLatencyHlsManifest'}]}, schedule_configuration={'StartTime': '2024-05-28T06:00:00.00Z', 'EndTime': '2024-05-28T12:00:00.00Z'}, destination={'S3Destination': {'BucketName': 'harvestJobS3DestinationBucket', 'DestinationPath': 'manifests'}})
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.create_harvest_job_request.CreateHarvestJobRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.create_harvest_job_response.CreateHarvestJobResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.create_harvest_job

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.create_harvest_job.create_harvest_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.create_harvest_job_request.CreateHarvestJobRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
            "harvested_manifests": harvested_manifests,
            "schedule_configuration": schedule_configuration,
            "destination": destination,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if harvest_job_name is not None:
            input_["harvest_job_name"] = harvest_job_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_harvest_job(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        harvest_job_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
    ) -> "capo_mediapackagev2.types.get_harvest_job_response.GetHarvestJobResponse":
        """<p>Retrieves the details of a specific harvest job.</p>

        Args:
            channel_group_name: <p>The name of the channel group containing the channel associated with the harvest job.</p>
            channel_name: <p>The name of the channel associated with the harvest job.</p>
            origin_endpoint_name: <p>The name of the origin endpoint associated with the harvest job.</p>
            harvest_job_name: <p>The name of the harvest job to retrieve.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Getting a Harvest Job

            >>> client.get_harvest_job(channel_group_name='exampleChannelGroup', channel_name='exampleChannelName', origin_endpoint_name='exampleOriginEndpointName', harvest_job_name='HarvestJobName')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.get_harvest_job_request.GetHarvestJobRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.get_harvest_job_response.GetHarvestJobResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.get_harvest_job

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.get_harvest_job.get_harvest_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.get_harvest_job_request.GetHarvestJobRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
            "harvest_job_name": harvest_job_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_harvest_job(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        channel_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        harvest_job_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        e_tag: Optional["capo_mediapackagev2.types.entity_tag.EntityTag"] = None,
    ) -> (
        "capo_mediapackagev2.types.cancel_harvest_job_response.CancelHarvestJobResponse"
    ):
        """<p>Cancels an in-progress harvest job.</p>

        Args:
            channel_group_name: <p>The name of the channel group containing the channel from which the harvest job is running.</p>
            channel_name: <p>The name of the channel from which the harvest job is running.</p>
            origin_endpoint_name: <p>The name of the origin endpoint that the harvest job is harvesting from. This cannot be changed after the harvest job is submitted.</p>
            harvest_job_name: <p>The name of the harvest job to cancel. This name must be unique within the channel and cannot be changed after the harvest job is submitted.</p>
            e_tag: <p>The current Entity Tag (ETag) associated with the harvest job. Used for concurrency control.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a Harvest Job

            >>> client.cancel_harvest_job(channel_group_name='exampleChannelGroup', channel_name='exampleChannelName', origin_endpoint_name='exampleOriginEndpointName', harvest_job_name='HarvestJobName')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.cancel_harvest_job_request.CancelHarvestJobRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.cancel_harvest_job_response.CancelHarvestJobResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.cancel_harvest_job

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.cancel_harvest_job.cancel_harvest_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.cancel_harvest_job_request.CancelHarvestJobRequest = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
            "harvest_job_name": harvest_job_name,
        }
        if e_tag is not None:
            input_["e_tag"] = e_tag

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_harvest_jobs(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        channel_name: Optional[
            "capo_mediapackagev2.types.resource_name.ResourceName"
        ] = None,
        origin_endpoint_name: Optional[
            "capo_mediapackagev2.types.resource_name.ResourceName"
        ] = None,
        status: Optional[
            "capo_mediapackagev2.types.harvest_job_status.HarvestJobStatus"
        ] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediapackagev2.types.list_harvest_jobs_response.ListHarvestJobsResponse":
        """<p>Retrieves a list of harvest jobs that match the specified criteria.</p>

        Args:
            channel_group_name: <p>The name of the channel group to filter the harvest jobs by. If specified, only harvest jobs associated with channels in this group will be returned.</p>
            channel_name: <p>The name of the channel to filter the harvest jobs by. If specified, only harvest jobs associated with this channel will be returned.</p>
            origin_endpoint_name: <p>The name of the origin endpoint to filter the harvest jobs by. If specified, only harvest jobs associated with this origin endpoint will be returned.</p>
            status: <p>The status to filter the harvest jobs by. If specified, only harvest jobs with this status will be returned.</p>
            max_results: <p>The maximum number of harvest jobs to return in a single request. If not specified, a default value will be used.</p>
            next_token: <p>A token used for pagination. Provide this value in subsequent requests to retrieve the next set of results.</p>

        Raises:
            capo_mediapackagev2.errors.access_denied_exception.AccessDeniedException: <p>Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.</p>
            capo_mediapackagev2.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_mediapackagev2.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            capo_mediapackagev2.errors.throttling_exception.ThrottlingException: <p>The request throughput limit was exceeded.</p>
            capo_mediapackagev2.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service.</p>
            capo_mediapackagev2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListHarvestJobs: Specify ChannelGroup only

            >>> client.list_harvest_jobs(channel_group_name='exampleChannelGroup')
            ListHarvestJobs: Specify ChannelGroup, Channel only

            >>> client.list_harvest_jobs(channel_group_name='exampleChannelGroup', channel_name='exampleChannelName')
            ListHarvestJobs: Specify ChannelGroup, Channel, OriginEndpoint

            >>> client.list_harvest_jobs(channel_group_name='exampleChannelGroup', channel_name='exampleChannelName', origin_endpoint_name='exampleOriginEndpointName')
            ListHarvestJobs: Specify ChannelGroup, Channel, OriginEndpoint + Status filter

            >>> client.list_harvest_jobs(channel_group_name='exampleChannelGroup', channel_name='exampleChannelName', origin_endpoint_name='exampleOriginEndpointName', status='QUEUED')
            ListHarvestJobs: Empty response

            >>> client.list_harvest_jobs(channel_group_name='exampleChannelGroup', channel_name='exampleChannelName', origin_endpoint_name='exampleOriginEndpointName')
        """

        def _handler(
            req: "OperationRequest[capo_mediapackagev2.types.list_harvest_jobs_request.ListHarvestJobsRequest]",
        ) -> OperationResponse[
            "capo_mediapackagev2.types.list_harvest_jobs_response.ListHarvestJobsResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.list_harvest_jobs

            output, http_response = (
                capo_mediapackagev2._operations.mediapackagev2.list_harvest_jobs.list_harvest_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.list_harvest_jobs_request.ListHarvestJobsRequest = {
            "channel_group_name": channel_group_name
        }
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if origin_endpoint_name is not None:
            input_["origin_endpoint_name"] = origin_endpoint_name
        if status is not None:
            input_["status"] = status
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

    def iter_list_harvest_jobs(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[MediaPackageV2ClientConfig] = None,
        channel_name: Optional[
            "capo_mediapackagev2.types.resource_name.ResourceName"
        ] = None,
        origin_endpoint_name: Optional[
            "capo_mediapackagev2.types.resource_name.ResourceName"
        ] = None,
        status: Optional[
            "capo_mediapackagev2.types.harvest_job_status.HarvestJobStatus"
        ] = None,
        max_results: Optional[
            "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_mediapackagev2.types.harvest_job.HarvestJob]":
        _token = next_token
        while True:
            _response = self.list_harvest_jobs(
                channel_group_name,
                config_overrides=config_overrides,
                channel_name=channel_name,
                origin_endpoint_name=origin_endpoint_name,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
