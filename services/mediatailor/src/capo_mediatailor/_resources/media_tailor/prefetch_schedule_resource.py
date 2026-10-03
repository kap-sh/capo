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
    import capo_mediatailor.types.__integer_min1_max100
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.create_prefetch_schedule_request
    import capo_mediatailor.types.create_prefetch_schedule_response
    import capo_mediatailor.types.delete_prefetch_schedule_request
    import capo_mediatailor.types.delete_prefetch_schedule_response
    import capo_mediatailor.types.get_prefetch_schedule_request
    import capo_mediatailor.types.get_prefetch_schedule_response
    import capo_mediatailor.types.list_prefetch_schedule_type
    import capo_mediatailor.types.list_prefetch_schedules_request
    import capo_mediatailor.types.list_prefetch_schedules_response
    import capo_mediatailor.types.prefetch_consumption
    import capo_mediatailor.types.prefetch_retrieval
    import capo_mediatailor.types.prefetch_schedule
    import capo_mediatailor.types.prefetch_schedule_type
    import capo_mediatailor.types.recurring_prefetch_configuration
    from capo_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from capo_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class PrefetchScheduleResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        consumption: Optional[
            "capo_mediatailor.types.prefetch_consumption.PrefetchConsumption"
        ] = None,
        retrieval: Optional[
            "capo_mediatailor.types.prefetch_retrieval.PrefetchRetrieval"
        ] = None,
        recurring_prefetch_configuration: Optional[
            "capo_mediatailor.types.recurring_prefetch_configuration.RecurringPrefetchConfiguration"
        ] = None,
        schedule_type: Optional[
            "capo_mediatailor.types.prefetch_schedule_type.PrefetchScheduleType"
        ] = None,
        stream_id: Optional["capo_mediatailor.types.__string.__string"] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_prefetch_schedule_response.CreatePrefetchScheduleResponse":
        """<p>Creates a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            consumption: <p>The configuration settings for how and when MediaTailor consumes prefetched ads from the ad decision server for single prefetch schedules. Each consumption configuration contains an end time and an optional start time that define the <i>consumption window</i>. Prefetch schedules automatically expire no earlier than seven days after the end time.</p>
            name: <p>The name to assign to the schedule request.</p>
            playback_configuration_name: <p>The name to assign to the playback configuration.</p>
            retrieval: <p>The configuration settings for retrieval of prefetched ads from the ad decision server. Only one set of prefetched ads will be retrieved and subsequently consumed for each ad break.</p>
            recurring_prefetch_configuration: <p>The configuration that defines how and when MediaTailor performs ad prefetching in a live event.</p>
            schedule_type: <p>The frequency that MediaTailor creates prefetch schedules. <code>SINGLE</code> indicates that this schedule applies to one ad break. <code>RECURRING</code> indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.</p> <p>For more information about the prefetch types and when you might use each, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Prefetching ads in Elemental MediaTailor.</a> </p>
            stream_id: <p>An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration. If <code>StreamId</code> is specified, MediaTailor returns all of the prefetch schedules with an exact match on <code>StreamId</code>. If not specified, MediaTailor returns all of the prefetch schedules for the playback configuration, regardless of <code>StreamId</code>.</p>
            tags: <p>The tags to assign to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_prefetch_schedule_request.CreatePrefetchScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_prefetch_schedule_response.CreatePrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_prefetch_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_prefetch_schedule.create_prefetch_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_prefetch_schedule_request.CreatePrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }
        if consumption is not None:
            input_["consumption"] = consumption
        if retrieval is not None:
            input_["retrieval"] = retrieval
        if recurring_prefetch_configuration is not None:
            input_["recurring_prefetch_configuration"] = (
                recurring_prefetch_configuration
            )
        if schedule_type is not None:
            input_["schedule_type"] = schedule_type
        if stream_id is not None:
            input_["stream_id"] = stream_id
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
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_prefetch_schedule_response.GetPrefetchScheduleResponse":
        """<p>Retrieves a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            name: <p>The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.</p>
            playback_configuration_name: <p>Returns information about the prefetch schedule for a specific playback configuration. If you call <code>GetPrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_prefetch_schedule_request.GetPrefetchScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_prefetch_schedule_response.GetPrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_prefetch_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_prefetch_schedule.get_prefetch_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_prefetch_schedule_request.GetPrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_prefetch_schedule_response.DeletePrefetchScheduleResponse":
        """<p>Deletes a prefetch schedule for a specific playback configuration. If you call <code>DeletePrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            name: <p>The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.</p>
            playback_configuration_name: <p>The name of the playback configuration for this prefetch schedule.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_prefetch_schedule_request.DeletePrefetchScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_prefetch_schedule_response.DeletePrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_prefetch_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_prefetch_schedule.delete_prefetch_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_prefetch_schedule_request.DeletePrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
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
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional[
            "capo_mediatailor.types.__integer_min1_max100.__integerMin1Max100"
        ] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        schedule_type: Optional[
            "capo_mediatailor.types.list_prefetch_schedule_type.ListPrefetchScheduleType"
        ] = None,
        stream_id: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_prefetch_schedules_response.ListPrefetchSchedulesResponse":
        """<p>Lists the prefetch schedules for a playback configuration.</p>

        Args:
            max_results: <p>The maximum number of prefetch schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> prefetch schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListPrefetchSchedules</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            playback_configuration_name: <p>Retrieves the prefetch schedule(s) for a specific playback configuration.</p>
            schedule_type: <p>The type of prefetch schedules that you want to list. <code>SINGLE</code> indicates that you want to list the configured single prefetch schedules. <code>RECURRING</code> indicates that you want to list the configured recurring prefetch schedules. <code>ALL</code> indicates that you want to list all configured prefetch schedules.</p>
            stream_id: <p>An optional filtering parameter whereby MediaTailor filters the prefetch schedules to include only specific streams.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_prefetch_schedules_request.ListPrefetchSchedulesRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_prefetch_schedules_response.ListPrefetchSchedulesResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_prefetch_schedules

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_prefetch_schedules.list_prefetch_schedules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_prefetch_schedules_request.ListPrefetchSchedulesRequest = {
            "playback_configuration_name": playback_configuration_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if schedule_type is not None:
            input_["schedule_type"] = schedule_type
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPrefetchScheduleResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        consumption: Optional[
            "capo_mediatailor.types.prefetch_consumption.PrefetchConsumption"
        ] = None,
        retrieval: Optional[
            "capo_mediatailor.types.prefetch_retrieval.PrefetchRetrieval"
        ] = None,
        recurring_prefetch_configuration: Optional[
            "capo_mediatailor.types.recurring_prefetch_configuration.RecurringPrefetchConfiguration"
        ] = None,
        schedule_type: Optional[
            "capo_mediatailor.types.prefetch_schedule_type.PrefetchScheduleType"
        ] = None,
        stream_id: Optional["capo_mediatailor.types.__string.__string"] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_prefetch_schedule_response.CreatePrefetchScheduleResponse":
        """<p>Creates a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            consumption: <p>The configuration settings for how and when MediaTailor consumes prefetched ads from the ad decision server for single prefetch schedules. Each consumption configuration contains an end time and an optional start time that define the <i>consumption window</i>. Prefetch schedules automatically expire no earlier than seven days after the end time.</p>
            name: <p>The name to assign to the schedule request.</p>
            playback_configuration_name: <p>The name to assign to the playback configuration.</p>
            retrieval: <p>The configuration settings for retrieval of prefetched ads from the ad decision server. Only one set of prefetched ads will be retrieved and subsequently consumed for each ad break.</p>
            recurring_prefetch_configuration: <p>The configuration that defines how and when MediaTailor performs ad prefetching in a live event.</p>
            schedule_type: <p>The frequency that MediaTailor creates prefetch schedules. <code>SINGLE</code> indicates that this schedule applies to one ad break. <code>RECURRING</code> indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.</p> <p>For more information about the prefetch types and when you might use each, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Prefetching ads in Elemental MediaTailor.</a> </p>
            stream_id: <p>An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration. If <code>StreamId</code> is specified, MediaTailor returns all of the prefetch schedules with an exact match on <code>StreamId</code>. If not specified, MediaTailor returns all of the prefetch schedules for the playback configuration, regardless of <code>StreamId</code>.</p>
            tags: <p>The tags to assign to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.create_prefetch_schedule_request.CreatePrefetchScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.create_prefetch_schedule_response.CreatePrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_prefetch_schedule

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.create_prefetch_schedule.async_create_prefetch_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_prefetch_schedule_request.CreatePrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }
        if consumption is not None:
            input_["consumption"] = consumption
        if retrieval is not None:
            input_["retrieval"] = retrieval
        if recurring_prefetch_configuration is not None:
            input_["recurring_prefetch_configuration"] = (
                recurring_prefetch_configuration
            )
        if schedule_type is not None:
            input_["schedule_type"] = schedule_type
        if stream_id is not None:
            input_["stream_id"] = stream_id
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
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_prefetch_schedule_response.GetPrefetchScheduleResponse":
        """<p>Retrieves a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            name: <p>The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.</p>
            playback_configuration_name: <p>Returns information about the prefetch schedule for a specific playback configuration. If you call <code>GetPrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.get_prefetch_schedule_request.GetPrefetchScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.get_prefetch_schedule_response.GetPrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_prefetch_schedule

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.get_prefetch_schedule.async_get_prefetch_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_prefetch_schedule_request.GetPrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_prefetch_schedule_response.DeletePrefetchScheduleResponse":
        """<p>Deletes a prefetch schedule for a specific playback configuration. If you call <code>DeletePrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            name: <p>The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.</p>
            playback_configuration_name: <p>The name of the playback configuration for this prefetch schedule.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.delete_prefetch_schedule_request.DeletePrefetchScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.delete_prefetch_schedule_response.DeletePrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_prefetch_schedule

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.delete_prefetch_schedule.async_delete_prefetch_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_prefetch_schedule_request.DeletePrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
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
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        max_results: Optional[
            "capo_mediatailor.types.__integer_min1_max100.__integerMin1Max100"
        ] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        schedule_type: Optional[
            "capo_mediatailor.types.list_prefetch_schedule_type.ListPrefetchScheduleType"
        ] = None,
        stream_id: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_prefetch_schedules_response.ListPrefetchSchedulesResponse":
        """<p>Lists the prefetch schedules for a playback configuration.</p>

        Args:
            max_results: <p>The maximum number of prefetch schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> prefetch schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListPrefetchSchedules</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            playback_configuration_name: <p>Retrieves the prefetch schedule(s) for a specific playback configuration.</p>
            schedule_type: <p>The type of prefetch schedules that you want to list. <code>SINGLE</code> indicates that you want to list the configured single prefetch schedules. <code>RECURRING</code> indicates that you want to list the configured recurring prefetch schedules. <code>ALL</code> indicates that you want to list all configured prefetch schedules.</p>
            stream_id: <p>An optional filtering parameter whereby MediaTailor filters the prefetch schedules to include only specific streams.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.list_prefetch_schedules_request.ListPrefetchSchedulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.list_prefetch_schedules_response.ListPrefetchSchedulesResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_prefetch_schedules

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.list_prefetch_schedules.async_list_prefetch_schedules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_prefetch_schedules_request.ListPrefetchSchedulesRequest = {
            "playback_configuration_name": playback_configuration_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if schedule_type is not None:
            input_["schedule_type"] = schedule_type
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
