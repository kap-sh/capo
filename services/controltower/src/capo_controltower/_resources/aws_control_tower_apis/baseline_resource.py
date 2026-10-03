from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_controltower._auth._signers
import capo_controltower._auth._sigv4
from capo_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_controltower.types.baseline_arn
    import capo_controltower.types.baseline_summary
    import capo_controltower.types.get_baseline_input
    import capo_controltower.types.get_baseline_output
    import capo_controltower.types.list_baselines_input
    import capo_controltower.types.list_baselines_max_results
    import capo_controltower.types.list_baselines_output
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class BaselineResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        baseline_identifier: "capo_controltower.types.baseline_arn.BaselineArn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_baseline_output.GetBaselineOutput":
        """<p>Retrieve details about an existing <code>Baseline</code> resource by specifying its identifier. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_identifier: <p>The ARN of the <code>Baseline</code> resource to be retrieved.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.get_baseline_input.GetBaselineInput]",
        ) -> OperationResponse[
            "capo_controltower.types.get_baseline_output.GetBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_baseline

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.get_baseline.get_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_baseline_input.GetBaselineInput = {
            "baseline_identifier": baseline_identifier
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
        config_overrides: Optional[ControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_baselines_max_results.ListBaselinesMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_baselines_output.ListBaselinesOutput":
        """<p>Returns a summary list of all available baselines. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.list_baselines_input.ListBaselinesInput]",
        ) -> OperationResponse[
            "capo_controltower.types.list_baselines_output.ListBaselinesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_baselines

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.list_baselines.list_baselines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_baselines_input.ListBaselinesInput = {}
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


class AsyncBaselineResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        baseline_identifier: "capo_controltower.types.baseline_arn.BaselineArn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_baseline_output.GetBaselineOutput":
        """<p>Retrieve details about an existing <code>Baseline</code> resource by specifying its identifier. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_identifier: <p>The ARN of the <code>Baseline</code> resource to be retrieved.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_baseline_input.GetBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_baseline_output.GetBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_baseline.async_get_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_baseline_input.GetBaselineInput = {
            "baseline_identifier": baseline_identifier
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
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_baselines_max_results.ListBaselinesMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_baselines_output.ListBaselinesOutput":
        """<p>Returns a summary list of all available baselines. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_baselines_input.ListBaselinesInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_baselines_output.ListBaselinesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_baselines

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_baselines.async_list_baselines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_baselines_input.ListBaselinesInput = {}
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
