from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_gameliftstreams._auth._signers
import capo_gameliftstreams._auth._sigv4
from capo_gameliftstreams._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_gameliftstreams.types.client_token
    import capo_gameliftstreams.types.create_stream_group_input
    import capo_gameliftstreams.types.create_stream_group_output
    import capo_gameliftstreams.types.delete_stream_group_input
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.get_stream_group_input
    import capo_gameliftstreams.types.get_stream_group_output
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.list_stream_groups_input
    import capo_gameliftstreams.types.list_stream_groups_output
    import capo_gameliftstreams.types.location_configurations
    import capo_gameliftstreams.types.max_results
    import capo_gameliftstreams.types.next_token
    import capo_gameliftstreams.types.stream_class
    import capo_gameliftstreams.types.stream_group_summary
    import capo_gameliftstreams.types.tags
    import capo_gameliftstreams.types.update_stream_group_input
    import capo_gameliftstreams.types.update_stream_group_output
    from capo_gameliftstreams._services.async_game_lift_streams import (
        AsyncGameLiftStreamsClient,
        AsyncGameLiftStreamsClientConfig,
    )
    from capo_gameliftstreams._services.game_lift_streams import (
        GameLiftStreamsClient,
        GameLiftStreamsClientConfig,
    )


class StreamGroupResource:
    def __init__(self, service: GameLiftStreamsClient) -> None:
        self._service = service

    def create(
        self,
        description: "capo_gameliftstreams.types.description.Description",
        stream_class: "capo_gameliftstreams.types.stream_class.StreamClass",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
        default_application_identifier: Optional[
            "capo_gameliftstreams.types.identifier.Identifier"
        ] = None,
        location_configurations: Optional[
            "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
        ] = None,
        tags: Optional["capo_gameliftstreams.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_gameliftstreams.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_gameliftstreams.types.create_stream_group_output.CreateStreamGroupOutput"
    ):
        """<p> Stream groups manage how Amazon GameLift Streams allocates resources and handles concurrent streams, allowing you to effectively manage capacity and costs. Within a stream group, you specify an application to stream, streaming locations and their capacity, and the stream class you want to use when streaming applications to your end-users. A stream class defines the hardware configuration of the compute resources that Amazon GameLift Streams will use when streaming, such as the CPU, GPU, and memory. </p> <p> Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available: </p> <ul> <li> <p> <b>Always-on capacity</b>: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle. </p> </li> <li> <p> <b>Maximum capacity</b>: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released. </p> </li> <li> <p> <b>Target-idle capacity</b>: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state. </p> </li> </ul> <p>Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.</p> <p> To adjust the capacity of any <code>ACTIVE</code> stream group, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html">UpdateStreamGroup</a>. </p> <p> If the <code>CreateStreamGroup</code> request is successful, Amazon GameLift Streams assigns a unique ID to the stream group resource and sets the status to <code>ACTIVATING</code>. It can take a few minutes for Amazon GameLift Streams to finish creating the stream group while it searches for unallocated compute resources and provisions them. When complete, the stream group status will be <code>ACTIVE</code> and you can start stream sessions by using <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html">StartStreamSession</a>. To check the stream group's status, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html">GetStreamGroup</a>. </p> <p>Stream groups should be recreated every 3-4 weeks to pick up important service updates and fixes. Stream groups that are older than 180 days can no longer be updated with new application associations. Stream groups expire when they are 365 days old, at which point they can no longer stream sessions. The exact expiration date is indicated by the date value in the <code>ExpiresAt</code> field.</p>

        Args:
            description: <p>A descriptive label for the stream group.</p>
            stream_class: <p>The target stream quality for sessions that are hosted in this stream group. Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available: </p> <p>A stream class can be one of the following:</p> <ul> <li> <p> <b> <code>gen6n_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra_win2022</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium</code> (NVIDIA, medium)</b> Supports applications with moderate 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 4 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small</code> (NVIDIA, small)</b> Supports applications with lightweight 3D scene complexity and low CPU usage. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 1 vCPUs, 4 GB RAM, 2 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 12 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium_win2022</code> (NVIDIA, medium)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small_win2022</code> (NVIDIA, small)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 3 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_ultra</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> </ul>
            default_application_identifier: <p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>If you do not link an application when you create a stream group, you will need to link one later, before you can start streaming, using <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html">AssociateApplications</a>.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            location_configurations: <p> A set of one or more locations and the streaming capacity for each location. </p>
            tags: <p>A list of labels to assign to the new stream group resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html">TagResource</a> to add tags, <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html">UntagResource</a> to remove tags, and <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to view tags on existing resources.</p>
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gameliftstreams.types.create_stream_group_input.CreateStreamGroupInput]",
        ) -> OperationResponse[
            "capo_gameliftstreams.types.create_stream_group_output.CreateStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.create_stream_group

            output, http_response = (
                capo_gameliftstreams._operations.game_lift_streams.create_stream_group.create_stream_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.create_stream_group_input.CreateStreamGroupInput = {
            "description": description,
            "stream_class": stream_class,
        }
        if default_application_identifier is not None:
            input_["default_application_identifier"] = default_application_identifier
        if location_configurations is not None:
            input_["location_configurations"] = location_configurations
        if tags is not None:
            input_["tags"] = tags
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

    def read(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.get_stream_group_output.GetStreamGroupOutput":
        """<p>Retrieves properties for a Amazon GameLift Streams stream group resource. Specify the ID of the stream group that you want to retrieve. If the operation is successful, it returns properties for the requested stream group.</p>

        Args:
            identifier: <p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gameliftstreams.types.get_stream_group_input.GetStreamGroupInput]",
        ) -> OperationResponse[
            "capo_gameliftstreams.types.get_stream_group_output.GetStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.get_stream_group

            output, http_response = (
                capo_gameliftstreams._operations.game_lift_streams.get_stream_group.get_stream_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.get_stream_group_input.GetStreamGroupInput = {
            "identifier": identifier
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
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
        location_configurations: Optional[
            "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
        ] = None,
        description: Optional[
            "capo_gameliftstreams.types.description.Description"
        ] = None,
        default_application_identifier: Optional[
            "capo_gameliftstreams.types.identifier.Identifier"
        ] = None,
    ) -> (
        "capo_gameliftstreams.types.update_stream_group_output.UpdateStreamGroupOutput"
    ):
        """<p> Updates the configuration settings for an Amazon GameLift Streams stream group resource. To update a stream group, it must be in <code>ACTIVE</code> status. You can change the description, the set of locations, and the requested capacity of a stream group per location. If you want to change the stream class, create a new stream group. </p> <p> Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available: </p> <ul> <li> <p> <b>Always-on capacity</b>: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle. </p> </li> <li> <p> <b>Maximum capacity</b>: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released. </p> </li> <li> <p> <b>Target-idle capacity</b>: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state. </p> </li> </ul> <p>Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.</p> <p>To update a stream group, specify the stream group's Amazon Resource Name (ARN) and provide the new values. If the request is successful, Amazon GameLift Streams returns the complete updated metadata for the stream group. Expired stream groups cannot be updated.</p>

        Args:
            identifier: <p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            location_configurations: <p> A set of one or more locations and the streaming capacity for each location. </p>
            description: <p>A descriptive label for the stream group.</p>
            default_application_identifier: <p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>Note that this parameter only sets the default application in a stream group. To associate a new application to an existing stream group, you must use <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html">AssociateApplications</a>.</p> <p>When you switch default applications in a stream group, it can take up to a few hours for the new default application to be pre-cached.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gameliftstreams.types.update_stream_group_input.UpdateStreamGroupInput]",
        ) -> OperationResponse[
            "capo_gameliftstreams.types.update_stream_group_output.UpdateStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.update_stream_group

            output, http_response = (
                capo_gameliftstreams._operations.game_lift_streams.update_stream_group.update_stream_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.update_stream_group_input.UpdateStreamGroupInput = {
            "identifier": identifier
        }
        if location_configurations is not None:
            input_["location_configurations"] = location_configurations
        if description is not None:
            input_["description"] = description
        if default_application_identifier is not None:
            input_["default_application_identifier"] = default_application_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
    ) -> None:
        """<p>Permanently deletes all compute resources and information related to a stream group. To delete a stream group, specify the unique stream group identifier. During the deletion process, the stream group's status is <code>DELETING</code>. This operation stops streams in progress and prevents new streams from starting. As a best practice, before deleting the stream group, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html">ListStreamSessions</a> to check for streams in progress and take action to stop them. When you delete a stream group, any application associations referring to that stream group are automatically removed.</p>

        Args:
            identifier: <p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gameliftstreams.types.delete_stream_group_input.DeleteStreamGroupInput]",
        ) -> OperationResponse[None]:
            import capo_gameliftstreams._operations.game_lift_streams.delete_stream_group

            output, http_response = (
                capo_gameliftstreams._operations.game_lift_streams.delete_stream_group.delete_stream_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.delete_stream_group_input.DeleteStreamGroupInput = {
            "identifier": identifier
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
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_gameliftstreams.types.list_stream_groups_output.ListStreamGroupsOutput":
        """<p>Retrieves a list of all Amazon GameLift Streams stream groups that are associated with the Amazon Web Services account in use. This operation returns stream groups in all statuses, in no particular order. You can paginate the results as needed.</p>

        Args:
            next_token: <p>A token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gameliftstreams.types.list_stream_groups_input.ListStreamGroupsInput]",
        ) -> OperationResponse[
            "capo_gameliftstreams.types.list_stream_groups_output.ListStreamGroupsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.list_stream_groups

            output, http_response = (
                capo_gameliftstreams._operations.game_lift_streams.list_stream_groups.list_stream_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.list_stream_groups_input.ListStreamGroupsInput = {}
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


class AsyncStreamGroupResource:
    def __init__(self, service: AsyncGameLiftStreamsClient) -> None:
        self._service = service

    async def create(
        self,
        description: "capo_gameliftstreams.types.description.Description",
        stream_class: "capo_gameliftstreams.types.stream_class.StreamClass",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        default_application_identifier: Optional[
            "capo_gameliftstreams.types.identifier.Identifier"
        ] = None,
        location_configurations: Optional[
            "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
        ] = None,
        tags: Optional["capo_gameliftstreams.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_gameliftstreams.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_gameliftstreams.types.create_stream_group_output.CreateStreamGroupOutput"
    ):
        """<p> Stream groups manage how Amazon GameLift Streams allocates resources and handles concurrent streams, allowing you to effectively manage capacity and costs. Within a stream group, you specify an application to stream, streaming locations and their capacity, and the stream class you want to use when streaming applications to your end-users. A stream class defines the hardware configuration of the compute resources that Amazon GameLift Streams will use when streaming, such as the CPU, GPU, and memory. </p> <p> Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available: </p> <ul> <li> <p> <b>Always-on capacity</b>: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle. </p> </li> <li> <p> <b>Maximum capacity</b>: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released. </p> </li> <li> <p> <b>Target-idle capacity</b>: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state. </p> </li> </ul> <p>Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.</p> <p> To adjust the capacity of any <code>ACTIVE</code> stream group, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html">UpdateStreamGroup</a>. </p> <p> If the <code>CreateStreamGroup</code> request is successful, Amazon GameLift Streams assigns a unique ID to the stream group resource and sets the status to <code>ACTIVATING</code>. It can take a few minutes for Amazon GameLift Streams to finish creating the stream group while it searches for unallocated compute resources and provisions them. When complete, the stream group status will be <code>ACTIVE</code> and you can start stream sessions by using <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html">StartStreamSession</a>. To check the stream group's status, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html">GetStreamGroup</a>. </p> <p>Stream groups should be recreated every 3-4 weeks to pick up important service updates and fixes. Stream groups that are older than 180 days can no longer be updated with new application associations. Stream groups expire when they are 365 days old, at which point they can no longer stream sessions. The exact expiration date is indicated by the date value in the <code>ExpiresAt</code> field.</p>

        Args:
            description: <p>A descriptive label for the stream group.</p>
            stream_class: <p>The target stream quality for sessions that are hosted in this stream group. Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available: </p> <p>A stream class can be one of the following:</p> <ul> <li> <p> <b> <code>gen6n_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra_win2022</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium</code> (NVIDIA, medium)</b> Supports applications with moderate 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 4 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small</code> (NVIDIA, small)</b> Supports applications with lightweight 3D scene complexity and low CPU usage. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 1 vCPUs, 4 GB RAM, 2 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 12 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium_win2022</code> (NVIDIA, medium)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small_win2022</code> (NVIDIA, small)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 3 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_ultra</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> </ul>
            default_application_identifier: <p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>If you do not link an application when you create a stream group, you will need to link one later, before you can start streaming, using <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html">AssociateApplications</a>.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            location_configurations: <p> A set of one or more locations and the streaming capacity for each location. </p>
            tags: <p>A list of labels to assign to the new stream group resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html">TagResource</a> to add tags, <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html">UntagResource</a> to remove tags, and <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to view tags on existing resources.</p>
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.create_stream_group_input.CreateStreamGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.create_stream_group_output.CreateStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.create_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.create_stream_group.async_create_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.create_stream_group_input.CreateStreamGroupInput = {
            "description": description,
            "stream_class": stream_class,
        }
        if default_application_identifier is not None:
            input_["default_application_identifier"] = default_application_identifier
        if location_configurations is not None:
            input_["location_configurations"] = location_configurations
        if tags is not None:
            input_["tags"] = tags
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

    async def read(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.get_stream_group_output.GetStreamGroupOutput":
        """<p>Retrieves properties for a Amazon GameLift Streams stream group resource. Specify the ID of the stream group that you want to retrieve. If the operation is successful, it returns properties for the requested stream group.</p>

        Args:
            identifier: <p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.get_stream_group_input.GetStreamGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.get_stream_group_output.GetStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.get_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.get_stream_group.async_get_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.get_stream_group_input.GetStreamGroupInput = {
            "identifier": identifier
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
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        location_configurations: Optional[
            "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
        ] = None,
        description: Optional[
            "capo_gameliftstreams.types.description.Description"
        ] = None,
        default_application_identifier: Optional[
            "capo_gameliftstreams.types.identifier.Identifier"
        ] = None,
    ) -> (
        "capo_gameliftstreams.types.update_stream_group_output.UpdateStreamGroupOutput"
    ):
        """<p> Updates the configuration settings for an Amazon GameLift Streams stream group resource. To update a stream group, it must be in <code>ACTIVE</code> status. You can change the description, the set of locations, and the requested capacity of a stream group per location. If you want to change the stream class, create a new stream group. </p> <p> Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available: </p> <ul> <li> <p> <b>Always-on capacity</b>: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle. </p> </li> <li> <p> <b>Maximum capacity</b>: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released. </p> </li> <li> <p> <b>Target-idle capacity</b>: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state. </p> </li> </ul> <p>Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.</p> <p>To update a stream group, specify the stream group's Amazon Resource Name (ARN) and provide the new values. If the request is successful, Amazon GameLift Streams returns the complete updated metadata for the stream group. Expired stream groups cannot be updated.</p>

        Args:
            identifier: <p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            location_configurations: <p> A set of one or more locations and the streaming capacity for each location. </p>
            description: <p>A descriptive label for the stream group.</p>
            default_application_identifier: <p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>Note that this parameter only sets the default application in a stream group. To associate a new application to an existing stream group, you must use <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html">AssociateApplications</a>.</p> <p>When you switch default applications in a stream group, it can take up to a few hours for the new default application to be pre-cached.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.update_stream_group_input.UpdateStreamGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.update_stream_group_output.UpdateStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.update_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.update_stream_group.async_update_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.update_stream_group_input.UpdateStreamGroupInput = {
            "identifier": identifier
        }
        if location_configurations is not None:
            input_["location_configurations"] = location_configurations
        if description is not None:
            input_["description"] = description
        if default_application_identifier is not None:
            input_["default_application_identifier"] = default_application_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> None:
        """<p>Permanently deletes all compute resources and information related to a stream group. To delete a stream group, specify the unique stream group identifier. During the deletion process, the stream group's status is <code>DELETING</code>. This operation stops streams in progress and prevents new streams from starting. As a best practice, before deleting the stream group, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html">ListStreamSessions</a> to check for streams in progress and take action to stop them. When you delete a stream group, any application associations referring to that stream group are automatically removed.</p>

        Args:
            identifier: <p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.delete_stream_group_input.DeleteStreamGroupInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_gameliftstreams._operations.game_lift_streams.delete_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.delete_stream_group.async_delete_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.delete_stream_group_input.DeleteStreamGroupInput = {
            "identifier": identifier
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
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_gameliftstreams.types.list_stream_groups_output.ListStreamGroupsOutput":
        """<p>Retrieves a list of all Amazon GameLift Streams stream groups that are associated with the Amazon Web Services account in use. This operation returns stream groups in all statuses, in no particular order. You can paginate the results as needed.</p>

        Args:
            next_token: <p>A token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.list_stream_groups_input.ListStreamGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.list_stream_groups_output.ListStreamGroupsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.list_stream_groups

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.list_stream_groups.async_list_stream_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.list_stream_groups_input.ListStreamGroupsInput = {}
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
