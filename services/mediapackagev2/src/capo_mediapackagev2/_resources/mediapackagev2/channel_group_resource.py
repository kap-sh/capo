from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_mediapackagev2._auth._signers
import capo_mediapackagev2._auth._sigv4
from capo_mediapackagev2._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mediapackagev2.types.channel_group_list_configuration
    import capo_mediapackagev2.types.create_channel_group_request
    import capo_mediapackagev2.types.create_channel_group_response
    import capo_mediapackagev2.types.delete_channel_group_request
    import capo_mediapackagev2.types.delete_channel_group_response
    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.get_channel_group_request
    import capo_mediapackagev2.types.get_channel_group_response
    import capo_mediapackagev2.types.idempotency_token
    import capo_mediapackagev2.types.list_channel_groups_request
    import capo_mediapackagev2.types.list_channel_groups_response
    import capo_mediapackagev2.types.list_resource_max_results
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.tag_map
    import capo_mediapackagev2.types.update_channel_group_request
    import capo_mediapackagev2.types.update_channel_group_response
    from capo_mediapackagev2._services.async_media_package_v2 import (
        AsyncMediaPackageV2Client,
        AsyncMediaPackageV2ClientConfig,
    )
    from capo_mediapackagev2._services.media_package_v2 import (
        MediaPackageV2Client,
        MediaPackageV2ClientConfig,
    )


class ChannelGroupResource:
    def __init__(self, service: MediaPackageV2Client) -> None:
        self._service = service

    def put(
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

            >>> client.put(channel_group_name='exampleChannelGroup', description='Description for exampleChannelGroup', tags={'key1': 'value1', 'key2': 'value2'})
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
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

            >>> client.read(channel_group_name='exampleChannelGroup')
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def update(
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

            >>> client.update(channel_group_name='exampleChannelGroup', description='Updated description for exampleChannelGroup')
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

            >>> client.delete(channel_group_name='exampleChannelGroup')
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def list(
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

            >>> client.list()
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncChannelGroupResource:
    def __init__(self, service: AsyncMediaPackageV2Client) -> None:
        self._service = service

    async def put(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncMediaPackageV2ClientConfig] = None,
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

            >>> await client.put(channel_group_name='exampleChannelGroup', description='Description for exampleChannelGroup', tags={'key1': 'value1', 'key2': 'value2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackagev2.types.create_channel_group_request.CreateChannelGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackagev2.types.create_channel_group_response.CreateChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.create_channel_group

            (
                output,
                http_response,
            ) = await capo_mediapackagev2._operations.mediapackagev2.create_channel_group.async_create_channel_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncMediaPackageV2ClientConfig] = None,
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

            >>> await client.read(channel_group_name='exampleChannelGroup')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackagev2.types.get_channel_group_request.GetChannelGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackagev2.types.get_channel_group_response.GetChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.get_channel_group

            (
                output,
                http_response,
            ) = await capo_mediapackagev2._operations.mediapackagev2.get_channel_group.async_get_channel_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.get_channel_group_request.GetChannelGroupRequest = {
            "channel_group_name": channel_group_name
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
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncMediaPackageV2ClientConfig] = None,
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

            >>> await client.update(channel_group_name='exampleChannelGroup', description='Updated description for exampleChannelGroup')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackagev2.types.update_channel_group_request.UpdateChannelGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackagev2.types.update_channel_group_response.UpdateChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.update_channel_group

            (
                output,
                http_response,
            ) = await capo_mediapackagev2._operations.mediapackagev2.update_channel_group.async_update_channel_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.update_channel_group_request.UpdateChannelGroupRequest = {
            "channel_group_name": channel_group_name
        }
        if e_tag is not None:
            input_["e_tag"] = e_tag
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncMediaPackageV2ClientConfig] = None,
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

            >>> await client.delete(channel_group_name='exampleChannelGroup')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackagev2.types.delete_channel_group_request.DeleteChannelGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackagev2.types.delete_channel_group_response.DeleteChannelGroupResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.delete_channel_group

            (
                output,
                http_response,
            ) = await capo_mediapackagev2._operations.mediapackagev2.delete_channel_group.async_delete_channel_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.delete_channel_group_request.DeleteChannelGroupRequest = {
            "channel_group_name": channel_group_name
        }

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
        config_overrides: Optional[AsyncMediaPackageV2ClientConfig] = None,
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

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackagev2.types.list_channel_groups_request.ListChannelGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackagev2.types.list_channel_groups_response.ListChannelGroupsResponse"
        ]:
            import capo_mediapackagev2._operations.mediapackagev2.list_channel_groups

            (
                output,
                http_response,
            ) = await capo_mediapackagev2._operations.mediapackagev2.list_channel_groups.async_list_channel_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediapackagev2.types.list_channel_groups_request.ListChannelGroupsRequest = {}
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
