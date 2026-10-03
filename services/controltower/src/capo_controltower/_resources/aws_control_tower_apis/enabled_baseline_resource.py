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
    import capo_controltower.types.arn
    import capo_controltower.types.baseline_version
    import capo_controltower.types.disable_baseline_input
    import capo_controltower.types.disable_baseline_output
    import capo_controltower.types.enable_baseline_input
    import capo_controltower.types.enable_baseline_output
    import capo_controltower.types.enabled_baseline_filter
    import capo_controltower.types.enabled_baseline_parameters
    import capo_controltower.types.enabled_baseline_summary
    import capo_controltower.types.get_enabled_baseline_input
    import capo_controltower.types.get_enabled_baseline_output
    import capo_controltower.types.list_enabled_baselines_input
    import capo_controltower.types.list_enabled_baselines_max_results
    import capo_controltower.types.list_enabled_baselines_next_token
    import capo_controltower.types.list_enabled_baselines_output
    import capo_controltower.types.reset_enabled_baseline_input
    import capo_controltower.types.reset_enabled_baseline_output
    import capo_controltower.types.tag_map
    import capo_controltower.types.update_enabled_baseline_input
    import capo_controltower.types.update_enabled_baseline_output
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class EnabledBaselineResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def create(
        self,
        baseline_version: "capo_controltower.types.baseline_version.BaselineVersion",
        baseline_identifier: "capo_controltower.types.arn.Arn",
        target_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
        ] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
    ) -> "capo_controltower.types.enable_baseline_output.EnableBaselineOutput":
        """<p>Enable (apply) a <code>Baseline</code> to a Target. This API starts an asynchronous operation to deploy resources specified by the <code>Baseline</code> to the specified Target. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_version: <p>The specific version to be enabled of the specified baseline.</p>
            parameters: <p>A list of <code>key-value</code> objects that specify enablement parameters, where <code>key</code> is a string and <code>value</code> is a document of any type.</p>
            baseline_identifier: <p>The ARN of the baseline to be enabled.</p>
            target_identifier: <p>The ARN of the target on which the baseline will be enabled. Only OUs are supported as targets.</p>
            tags: <p>Tags associated with input to <code>EnableBaseline</code>.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.enable_baseline_input.EnableBaselineInput]",
        ) -> OperationResponse[
            "capo_controltower.types.enable_baseline_output.EnableBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.enable_baseline

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.enable_baseline.enable_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.enable_baseline_input.EnableBaselineInput = {
            "baseline_version": baseline_version,
            "baseline_identifier": baseline_identifier,
            "target_identifier": target_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters
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
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_enabled_baseline_output.GetEnabledBaselineOutput":
        """<p>Retrieve details of an <code>EnabledBaseline</code> resource by specifying its identifier.</p>

        Args:
            enabled_baseline_identifier: <p>Identifier of the <code>EnabledBaseline</code> resource to be retrieved, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.get_enabled_baseline_input.GetEnabledBaselineInput]",
        ) -> OperationResponse[
            "capo_controltower.types.get_enabled_baseline_output.GetEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_enabled_baseline

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.get_enabled_baseline.get_enabled_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_enabled_baseline_input.GetEnabledBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
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
        baseline_version: "capo_controltower.types.baseline_version.BaselineVersion",
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
        ] = None,
    ) -> "capo_controltower.types.update_enabled_baseline_output.UpdateEnabledBaselineOutput":
        """<p>Updates an <code>EnabledBaseline</code> resource's applied parameters or version. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_version: <p>Specifies the new <code>Baseline</code> version, to which the <code>EnabledBaseline</code> should be updated.</p>
            parameters: <p>Parameters to apply when making an update.</p>
            enabled_baseline_identifier: <p>Specifies the <code>EnabledBaseline</code> resource to be updated.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.update_enabled_baseline_input.UpdateEnabledBaselineInput]",
        ) -> OperationResponse[
            "capo_controltower.types.update_enabled_baseline_output.UpdateEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_enabled_baseline

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.update_enabled_baseline.update_enabled_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.update_enabled_baseline_input.UpdateEnabledBaselineInput = {
            "baseline_version": baseline_version,
            "enabled_baseline_identifier": enabled_baseline_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.disable_baseline_output.DisableBaselineOutput":
        """<p>Disable an <code>EnabledBaseline</code> resource on the specified Target. This API starts an asynchronous operation to remove all resources deployed as part of the baseline enablement. The resource will vary depending on the enabled baseline. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            enabled_baseline_identifier: <p>Identifier of the <code>EnabledBaseline</code> resource to be deactivated, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.disable_baseline_input.DisableBaselineInput]",
        ) -> OperationResponse[
            "capo_controltower.types.disable_baseline_output.DisableBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.disable_baseline

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.disable_baseline.disable_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.disable_baseline_input.DisableBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
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
        filter: Optional[
            "capo_controltower.types.enabled_baseline_filter.EnabledBaselineFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_enabled_baselines_max_results.ListEnabledBaselinesMaxResults"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> "capo_controltower.types.list_enabled_baselines_output.ListEnabledBaselinesOutput":
        """<p>Returns a list of summaries describing <code>EnabledBaseline</code> resources. You can filter the list by the corresponding <code>Baseline</code> or <code>Target</code> of the <code>EnabledBaseline</code> resources. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            filter: <p>A filter applied on the <code>ListEnabledBaseline</code> operation. Allowed filters are <code>baselineIdentifiers</code> and <code>targetIdentifiers</code>. The filter can be applied for either, or both.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>
            include_children: <p>A value that can be set to include the child enabled baselines in responses. The default value is false.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.list_enabled_baselines_input.ListEnabledBaselinesInput]",
        ) -> OperationResponse[
            "capo_controltower.types.list_enabled_baselines_output.ListEnabledBaselinesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_enabled_baselines

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.list_enabled_baselines.list_enabled_baselines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_enabled_baselines_input.ListEnabledBaselinesInput = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_children is not None:
            input_["include_children"] = include_children

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reset_enabled_baseline(
        self,
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.reset_enabled_baseline_output.ResetEnabledBaselineOutput":
        """<p>Re-enables an <code>EnabledBaseline</code> resource. For example, this API can re-apply the existing <code>Baseline</code> after a new member account is moved to the target OU. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            enabled_baseline_identifier: <p>Specifies the ID of the <code>EnabledBaseline</code> resource to be re-enabled, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.reset_enabled_baseline_input.ResetEnabledBaselineInput]",
        ) -> OperationResponse[
            "capo_controltower.types.reset_enabled_baseline_output.ResetEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_enabled_baseline

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.reset_enabled_baseline.reset_enabled_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.reset_enabled_baseline_input.ResetEnabledBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEnabledBaselineResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def create(
        self,
        baseline_version: "capo_controltower.types.baseline_version.BaselineVersion",
        baseline_identifier: "capo_controltower.types.arn.Arn",
        target_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
        ] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
    ) -> "capo_controltower.types.enable_baseline_output.EnableBaselineOutput":
        """<p>Enable (apply) a <code>Baseline</code> to a Target. This API starts an asynchronous operation to deploy resources specified by the <code>Baseline</code> to the specified Target. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_version: <p>The specific version to be enabled of the specified baseline.</p>
            parameters: <p>A list of <code>key-value</code> objects that specify enablement parameters, where <code>key</code> is a string and <code>value</code> is a document of any type.</p>
            baseline_identifier: <p>The ARN of the baseline to be enabled.</p>
            target_identifier: <p>The ARN of the target on which the baseline will be enabled. Only OUs are supported as targets.</p>
            tags: <p>Tags associated with input to <code>EnableBaseline</code>.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.enable_baseline_input.EnableBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.enable_baseline_output.EnableBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.enable_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.enable_baseline.async_enable_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.enable_baseline_input.EnableBaselineInput = {
            "baseline_version": baseline_version,
            "baseline_identifier": baseline_identifier,
            "target_identifier": target_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters
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
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_enabled_baseline_output.GetEnabledBaselineOutput":
        """<p>Retrieve details of an <code>EnabledBaseline</code> resource by specifying its identifier.</p>

        Args:
            enabled_baseline_identifier: <p>Identifier of the <code>EnabledBaseline</code> resource to be retrieved, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_enabled_baseline_input.GetEnabledBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_enabled_baseline_output.GetEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_enabled_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_enabled_baseline.async_get_enabled_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_enabled_baseline_input.GetEnabledBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
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
        baseline_version: "capo_controltower.types.baseline_version.BaselineVersion",
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
        ] = None,
    ) -> "capo_controltower.types.update_enabled_baseline_output.UpdateEnabledBaselineOutput":
        """<p>Updates an <code>EnabledBaseline</code> resource's applied parameters or version. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_version: <p>Specifies the new <code>Baseline</code> version, to which the <code>EnabledBaseline</code> should be updated.</p>
            parameters: <p>Parameters to apply when making an update.</p>
            enabled_baseline_identifier: <p>Specifies the <code>EnabledBaseline</code> resource to be updated.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.update_enabled_baseline_input.UpdateEnabledBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.update_enabled_baseline_output.UpdateEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_enabled_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.update_enabled_baseline.async_update_enabled_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.update_enabled_baseline_input.UpdateEnabledBaselineInput = {
            "baseline_version": baseline_version,
            "enabled_baseline_identifier": enabled_baseline_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.disable_baseline_output.DisableBaselineOutput":
        """<p>Disable an <code>EnabledBaseline</code> resource on the specified Target. This API starts an asynchronous operation to remove all resources deployed as part of the baseline enablement. The resource will vary depending on the enabled baseline. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            enabled_baseline_identifier: <p>Identifier of the <code>EnabledBaseline</code> resource to be deactivated, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.disable_baseline_input.DisableBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.disable_baseline_output.DisableBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.disable_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.disable_baseline.async_disable_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.disable_baseline_input.DisableBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
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
        filter: Optional[
            "capo_controltower.types.enabled_baseline_filter.EnabledBaselineFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_enabled_baselines_max_results.ListEnabledBaselinesMaxResults"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> "capo_controltower.types.list_enabled_baselines_output.ListEnabledBaselinesOutput":
        """<p>Returns a list of summaries describing <code>EnabledBaseline</code> resources. You can filter the list by the corresponding <code>Baseline</code> or <code>Target</code> of the <code>EnabledBaseline</code> resources. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            filter: <p>A filter applied on the <code>ListEnabledBaseline</code> operation. Allowed filters are <code>baselineIdentifiers</code> and <code>targetIdentifiers</code>. The filter can be applied for either, or both.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>
            include_children: <p>A value that can be set to include the child enabled baselines in responses. The default value is false.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_enabled_baselines_input.ListEnabledBaselinesInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_enabled_baselines_output.ListEnabledBaselinesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_enabled_baselines

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_enabled_baselines.async_list_enabled_baselines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_enabled_baselines_input.ListEnabledBaselinesInput = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_children is not None:
            input_["include_children"] = include_children

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_enabled_baseline(
        self,
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.reset_enabled_baseline_output.ResetEnabledBaselineOutput":
        """<p>Re-enables an <code>EnabledBaseline</code> resource. For example, this API can re-apply the existing <code>Baseline</code> after a new member account is moved to the target OU. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            enabled_baseline_identifier: <p>Specifies the ID of the <code>EnabledBaseline</code> resource to be re-enabled, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href="https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.reset_enabled_baseline_input.ResetEnabledBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.reset_enabled_baseline_output.ResetEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_enabled_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.reset_enabled_baseline.async_reset_enabled_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.reset_enabled_baseline_input.ResetEnabledBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
