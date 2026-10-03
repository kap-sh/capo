from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_launch_wizard._auth._signers
import capo_launch_wizard._auth._sigv4
from capo_launch_wizard._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_launch_wizard.types.get_workload_input
    import capo_launch_wizard.types.get_workload_output
    import capo_launch_wizard.types.list_workloads_input
    import capo_launch_wizard.types.list_workloads_output
    import capo_launch_wizard.types.max_workload_results
    import capo_launch_wizard.types.next_token
    import capo_launch_wizard.types.workload_data_summary
    import capo_launch_wizard.types.workload_name
    from capo_launch_wizard._services.async_launch_wizard import (
        AsyncLaunchWizardClient,
        AsyncLaunchWizardClientConfig,
    )
    from capo_launch_wizard._services.launch_wizard import (
        LaunchWizardClient,
        LaunchWizardClientConfig,
    )


class Workload:
    def __init__(self, service: LaunchWizardClient) -> None:
        self._service = service

    def read(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.get_workload_output.GetWorkloadOutput":
        """<p>Returns information about a workload.</p>

        Args:
            workload_name: <p>The name of the workload.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get details about a specific workload.

            >>> client.read(workload_name='SAP')
        """

        def _handler(
            req: "OperationRequest[capo_launch_wizard.types.get_workload_input.GetWorkloadInput]",
        ) -> OperationResponse[
            "capo_launch_wizard.types.get_workload_output.GetWorkloadOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.get_workload

            output, http_response = (
                capo_launch_wizard._operations.launch_wizard.get_workload.get_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_launch_wizard.types.get_workload_input.GetWorkloadInput = {
            "workload_name": workload_name
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
        config_overrides: Optional[LaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "capo_launch_wizard.types.list_workloads_output.ListWorkloadsOutput":
        """<p>Lists the available workload names. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html">ListWorkloadDeploymentPatterns</a> operation to discover the available deployment patterns for a given workload.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all available workloads supported by AWS Launch Wizard.

            >>> client.list()
        """

        def _handler(
            req: "OperationRequest[capo_launch_wizard.types.list_workloads_input.ListWorkloadsInput]",
        ) -> OperationResponse[
            "capo_launch_wizard.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_workloads

            output, http_response = (
                capo_launch_wizard._operations.launch_wizard.list_workloads.list_workloads(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_workloads_input.ListWorkloadsInput = {}
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


class AsyncWorkload:
    def __init__(self, service: AsyncLaunchWizardClient) -> None:
        self._service = service

    async def read(
        self,
        workload_name: "capo_launch_wizard.types.workload_name.WorkloadName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.get_workload_output.GetWorkloadOutput":
        """<p>Returns information about a workload.</p>

        Args:
            workload_name: <p>The name of the workload.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get details about a specific workload.

            >>> await client.read(workload_name='SAP')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.get_workload_input.GetWorkloadInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.get_workload_output.GetWorkloadOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.get_workload

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.get_workload.async_get_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_launch_wizard.types.get_workload_input.GetWorkloadInput = {
            "workload_name": workload_name
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
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "capo_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["capo_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "capo_launch_wizard.types.list_workloads_output.ListWorkloadsOutput":
        """<p>Lists the available workload names. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html">ListWorkloadDeploymentPatterns</a> operation to discover the available deployment patterns for a given workload.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href="https://repost.aws/">re:Post</a>.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all available workloads supported by AWS Launch Wizard.

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_launch_wizard.types.list_workloads_input.ListWorkloadsInput]",
        ) -> AsyncOperationResponse[
            "capo_launch_wizard.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_workloads

            (
                output,
                http_response,
            ) = await capo_launch_wizard._operations.launch_wizard.list_workloads.async_list_workloads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_workloads_input.ListWorkloadsInput = {}
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
