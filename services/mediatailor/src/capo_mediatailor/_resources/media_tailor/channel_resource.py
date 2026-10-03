from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_mediatailor._auth._signers
import capo_mediatailor._auth._sigv4
from capo_mediatailor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.audiences
    import capo_mediatailor.types.channel
    import capo_mediatailor.types.configure_logs_for_channel_request
    import capo_mediatailor.types.configure_logs_for_channel_response
    import capo_mediatailor.types.create_channel_request
    import capo_mediatailor.types.create_channel_response
    import capo_mediatailor.types.delete_channel_request
    import capo_mediatailor.types.delete_channel_response
    import capo_mediatailor.types.describe_channel_request
    import capo_mediatailor.types.describe_channel_response
    import capo_mediatailor.types.get_channel_schedule_request
    import capo_mediatailor.types.get_channel_schedule_response
    import capo_mediatailor.types.list_channels_request
    import capo_mediatailor.types.list_channels_response
    import capo_mediatailor.types.log_types
    import capo_mediatailor.types.max_results
    import capo_mediatailor.types.playback_mode
    import capo_mediatailor.types.request_outputs
    import capo_mediatailor.types.schedule_entry
    import capo_mediatailor.types.slate_source
    import capo_mediatailor.types.start_channel_request
    import capo_mediatailor.types.start_channel_response
    import capo_mediatailor.types.stop_channel_request
    import capo_mediatailor.types.stop_channel_response
    import capo_mediatailor.types.tier
    import capo_mediatailor.types.time_shift_configuration
    import capo_mediatailor.types.update_channel_request
    import capo_mediatailor.types.update_channel_response
    from capo_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from capo_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class ChannelResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        playback_mode: "capo_mediatailor.types.playback_mode.PlaybackMode",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
        tier: Optional["capo_mediatailor.types.tier.Tier"] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            playback_mode: <p>The type of playback mode to use for this channel.</p> <p> <code>LINEAR</code> - The programs in the schedule play once back-to-back in the schedule.</p> <p> <code>LOOP</code> - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.</p>
            tags: <p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            tier: <p>The tier of the channel.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_channel_request.CreateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
            "playback_mode": playback_mode,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if tags is not None:
            input_["tags"] = tags
        if tier is not None:
            input_["tier"] = tier
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_channel_response.DescribeChannelResponse":
        """<p>Describes a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_channel_request.DescribeChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_channel_request.DescribeChannelRequest = {
            "channel_name": channel_name
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
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.update_channel_response.UpdateChannelResponse":
        """<p>Updates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_channel_request.UpdateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_channel_response.DeleteChannelResponse":
        """<p>Deletes a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_channel_request.DeleteChannelRequest = {
            "channel_name": channel_name
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
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_channels_response.ListChannelsResponse":
        """<p>Retrieves information about the channels that are associated with the current AWS account.</p>

        Args:
            max_results: <p>The maximum number of channels that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channels, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListChannels</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_channels

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_channels_request.ListChannelsRequest = {}
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

    def configure_logs_for_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        log_types: "capo_mediatailor.types.log_types.LogTypes",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.configure_logs_for_channel_response.ConfigureLogsForChannelResponse":
        """<p>Configures Amazon CloudWatch log settings for a channel.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            log_types: <p>The types of logs to collect.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.configure_logs_for_channel_request.ConfigureLogsForChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.configure_logs_for_channel_response.ConfigureLogsForChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.configure_logs_for_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.configure_logs_for_channel.configure_logs_for_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.configure_logs_for_channel_request.ConfigureLogsForChannelRequest = {
            "channel_name": channel_name,
            "log_types": log_types,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        playback_mode: "capo_mediatailor.types.playback_mode.PlaybackMode",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
        tier: Optional["capo_mediatailor.types.tier.Tier"] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            playback_mode: <p>The type of playback mode to use for this channel.</p> <p> <code>LINEAR</code> - The programs in the schedule play once back-to-back in the schedule.</p> <p> <code>LOOP</code> - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.</p>
            tags: <p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            tier: <p>The tier of the channel.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_channel_request.CreateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
            "playback_mode": playback_mode,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if tags is not None:
            input_["tags"] = tags
        if tier is not None:
            input_["tier"] = tier
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_schedule(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        duration_minutes: Optional["capo_mediatailor.types.__string.__string"] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        audience: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.get_channel_schedule_response.GetChannelScheduleResponse":
        """<p>Retrieves information about your channel's schedule.</p>

        Args:
            channel_name: <p>The name of the channel associated with this Channel Schedule.</p>
            duration_minutes: <p>The duration in minutes of the channel schedule.</p>
            max_results: <p>The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channel schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p>
            next_token: <p>(Optional) If the playback configuration has more than <code>MaxResults</code> channel schedules, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>GetChannelScheduleRequest</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more channel schedules to get.</p>
            audience: <p>The single audience for GetChannelScheduleRequest.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_channel_schedule_request.GetChannelScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_channel_schedule_response.GetChannelScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_channel_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_channel_schedule.get_channel_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_channel_schedule_request.GetChannelScheduleRequest = {
            "channel_name": channel_name
        }
        if duration_minutes is not None:
            input_["duration_minutes"] = duration_minutes
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if audience is not None:
            input_["audience"] = audience

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.start_channel_response.StartChannelResponse":
        """<p>Starts a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.start_channel_request.StartChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.start_channel_response.StartChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.start_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.start_channel.start_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.start_channel_request.StartChannelRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.stop_channel_response.StopChannelResponse":
        """<p>Stops a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.stop_channel_request.StopChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.stop_channel_response.StopChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.stop_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.stop_channel.stop_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.stop_channel_request.StopChannelRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncChannelResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        playback_mode: "capo_mediatailor.types.playback_mode.PlaybackMode",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
        tier: Optional["capo_mediatailor.types.tier.Tier"] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            playback_mode: <p>The type of playback mode to use for this channel.</p> <p> <code>LINEAR</code> - The programs in the schedule play once back-to-back in the schedule.</p> <p> <code>LOOP</code> - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.</p>
            tags: <p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            tier: <p>The tier of the channel.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.create_channel_request.CreateChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.create_channel.async_create_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_channel_request.CreateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
            "playback_mode": playback_mode,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if tags is not None:
            input_["tags"] = tags
        if tier is not None:
            input_["tier"] = tier
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_channel_response.DescribeChannelResponse":
        """<p>Describes a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.describe_channel_request.DescribeChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.describe_channel.async_describe_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_channel_request.DescribeChannelRequest = {
            "channel_name": channel_name
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
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.update_channel_response.UpdateChannelResponse":
        """<p>Updates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.update_channel_request.UpdateChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.update_channel.async_update_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_channel_request.UpdateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_channel_response.DeleteChannelResponse":
        """<p>Deletes a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.delete_channel_request.DeleteChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.delete_channel.async_delete_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_channel_request.DeleteChannelRequest = {
            "channel_name": channel_name
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
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_channels_response.ListChannelsResponse":
        """<p>Retrieves information about the channels that are associated with the current AWS account.</p>

        Args:
            max_results: <p>The maximum number of channels that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channels, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListChannels</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.list_channels_request.ListChannelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_channels

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.list_channels.async_list_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_channels_request.ListChannelsRequest = {}
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

    async def configure_logs_for_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        log_types: "capo_mediatailor.types.log_types.LogTypes",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.configure_logs_for_channel_response.ConfigureLogsForChannelResponse":
        """<p>Configures Amazon CloudWatch log settings for a channel.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            log_types: <p>The types of logs to collect.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.configure_logs_for_channel_request.ConfigureLogsForChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.configure_logs_for_channel_response.ConfigureLogsForChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.configure_logs_for_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.configure_logs_for_channel.async_configure_logs_for_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.configure_logs_for_channel_request.ConfigureLogsForChannelRequest = {
            "channel_name": channel_name,
            "log_types": log_types,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        playback_mode: "capo_mediatailor.types.playback_mode.PlaybackMode",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
        tier: Optional["capo_mediatailor.types.tier.Tier"] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            playback_mode: <p>The type of playback mode to use for this channel.</p> <p> <code>LINEAR</code> - The programs in the schedule play once back-to-back in the schedule.</p> <p> <code>LOOP</code> - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.</p>
            tags: <p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            tier: <p>The tier of the channel.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.create_channel_request.CreateChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.create_channel.async_create_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_channel_request.CreateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
            "playback_mode": playback_mode,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if tags is not None:
            input_["tags"] = tags
        if tier is not None:
            input_["tier"] = tier
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_channel_schedule(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        duration_minutes: Optional["capo_mediatailor.types.__string.__string"] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        audience: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.get_channel_schedule_response.GetChannelScheduleResponse":
        """<p>Retrieves information about your channel's schedule.</p>

        Args:
            channel_name: <p>The name of the channel associated with this Channel Schedule.</p>
            duration_minutes: <p>The duration in minutes of the channel schedule.</p>
            max_results: <p>The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channel schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p>
            next_token: <p>(Optional) If the playback configuration has more than <code>MaxResults</code> channel schedules, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>GetChannelScheduleRequest</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more channel schedules to get.</p>
            audience: <p>The single audience for GetChannelScheduleRequest.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.get_channel_schedule_request.GetChannelScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.get_channel_schedule_response.GetChannelScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_channel_schedule

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.get_channel_schedule.async_get_channel_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_channel_schedule_request.GetChannelScheduleRequest = {
            "channel_name": channel_name
        }
        if duration_minutes is not None:
            input_["duration_minutes"] = duration_minutes
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if audience is not None:
            input_["audience"] = audience

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.start_channel_response.StartChannelResponse":
        """<p>Starts a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.start_channel_request.StartChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.start_channel_response.StartChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.start_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.start_channel.async_start_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.start_channel_request.StartChannelRequest = {
            "channel_name": channel_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.stop_channel_response.StopChannelResponse":
        """<p>Stops a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.stop_channel_request.StopChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.stop_channel_response.StopChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.stop_channel

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.stop_channel.async_stop_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.stop_channel_request.StopChannelRequest = {
            "channel_name": channel_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
