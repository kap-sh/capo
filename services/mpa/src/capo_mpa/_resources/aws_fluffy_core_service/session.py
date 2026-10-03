from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_mpa._auth._signers
import capo_mpa._auth._sigv4
from capo_mpa._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.cancel_session_request
    import capo_mpa.types.cancel_session_response
    import capo_mpa.types.filters
    import capo_mpa.types.get_session_request
    import capo_mpa.types.get_session_response
    import capo_mpa.types.list_sessions_request
    import capo_mpa.types.list_sessions_response
    import capo_mpa.types.list_sessions_response_session
    import capo_mpa.types.max_results
    import capo_mpa.types.session_arn
    import capo_mpa.types.token
    from capo_mpa._services.async_mpa import AsyncMPAClient, AsyncMPAClientConfig
    from capo_mpa._services.mpa import MPAClient, MPAClientConfig


class Session:
    def __init__(self, service: MPAClient) -> None:
        self._service = service

    def read(
        self,
        session_arn: "capo_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.get_session_response.GetSessionResponse":
        """<p>Returns details for an approval session. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.get_session_response.GetSessionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_session

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.get_session_request.GetSessionRequest = {
            "session_arn": session_arn
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
        session_arn: "capo_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.cancel_session_response.CancelSessionResponse":
        """<p>Cancels an approval session. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.cancel_session_request.CancelSessionRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.cancel_session_response.CancelSessionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.cancel_session

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.cancel_session.cancel_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.cancel_session_request.CancelSessionRequest = {
            "session_arn": session_arn
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
        approval_team_arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
        filters: Optional["capo_mpa.types.filters.Filters"] = None,
    ) -> "capo_mpa.types.list_sessions_response.ListSessionsResponse":
        """<p>Returns a list of approval sessions. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            approval_team_arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            filters: <p>An array of <code>Filter</code> objects. Contains the filter to apply when listing sessions.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_sessions

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.list_sessions_request.ListSessionsRequest = {
            "approval_team_arn": approval_team_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSession:
    def __init__(self, service: AsyncMPAClient) -> None:
        self._service = service

    async def read(
        self,
        session_arn: "capo_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.get_session_response.GetSessionResponse":
        """<p>Returns details for an approval session. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.get_session_response.GetSessionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_session

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.get_session_request.GetSessionRequest = {
            "session_arn": session_arn
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
        session_arn: "capo_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "capo_mpa.types.cancel_session_response.CancelSessionResponse":
        """<p>Cancels an approval session. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.conflict_exception.ConflictException: <p>The request cannot be completed because it conflicts with the current state of a resource.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.cancel_session_request.CancelSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.cancel_session_response.CancelSessionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.cancel_session

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.cancel_session.async_cancel_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.cancel_session_request.CancelSessionRequest = {
            "session_arn": session_arn
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
        approval_team_arn: "capo_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
        filters: Optional["capo_mpa.types.filters.Filters"] = None,
    ) -> "capo_mpa.types.list_sessions_response.ListSessionsResponse":
        """<p>Returns a list of approval sessions. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            approval_team_arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            filters: <p>An array of <code>Filter</code> objects. Contains the filter to apply when listing sessions.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mpa.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mpa.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_sessions

            (
                output,
                http_response,
            ) = await capo_mpa._operations.aws_fluffy_core_service.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mpa.types.list_sessions_request.ListSessionsRequest = {
            "approval_team_arn": approval_team_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
