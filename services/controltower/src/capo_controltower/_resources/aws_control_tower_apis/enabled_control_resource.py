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
    import capo_controltower.types.control_identifier
    import capo_controltower.types.enable_control_input
    import capo_controltower.types.enable_control_output
    import capo_controltower.types.enabled_control_filter
    import capo_controltower.types.enabled_control_parameters
    import capo_controltower.types.enabled_control_summary
    import capo_controltower.types.get_enabled_control_input
    import capo_controltower.types.get_enabled_control_output
    import capo_controltower.types.list_enabled_controls_input
    import capo_controltower.types.list_enabled_controls_output
    import capo_controltower.types.max_results
    import capo_controltower.types.reset_enabled_control_input
    import capo_controltower.types.reset_enabled_control_output
    import capo_controltower.types.tag_map
    import capo_controltower.types.target_identifier
    import capo_controltower.types.update_enabled_control_input
    import capo_controltower.types.update_enabled_control_output
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class EnabledControlResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def create(
        self,
        control_identifier: "capo_controltower.types.control_identifier.ControlIdentifier",
        target_identifier: "capo_controltower.types.target_identifier.TargetIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_control_parameters.EnabledControlParameters"
        ] = None,
    ) -> "capo_controltower.types.enable_control_output.EnableControlOutput":
        """<p>This API call activates a control. It starts an asynchronous operation that creates Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>
            tags: <p>Tags to be applied to the <code>EnabledControl</code> resource.</p>
            parameters: <p>A list of input parameter values, which are specified to configure the control when you enable it.</p>

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
            req: "OperationRequest[capo_controltower.types.enable_control_input.EnableControlInput]",
        ) -> OperationResponse[
            "capo_controltower.types.enable_control_output.EnableControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.enable_control

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.enable_control.enable_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.enable_control_input.EnableControlInput = {
            "control_identifier": control_identifier,
            "target_identifier": target_identifier,
        }
        if tags is not None:
            input_["tags"] = tags
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_enabled_control_output.GetEnabledControlOutput":
        """<p>Retrieves details about an enabled control. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            enabled_control_identifier: <p>The <code>controlIdentifier</code> of the enabled control.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.get_enabled_control_input.GetEnabledControlInput]",
        ) -> OperationResponse[
            "capo_controltower.types.get_enabled_control_output.GetEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_enabled_control

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.get_enabled_control.get_enabled_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_enabled_control_input.GetEnabledControlInput = {
            "enabled_control_identifier": enabled_control_identifier
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
        parameters: "capo_controltower.types.enabled_control_parameters.EnabledControlParameters",
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput":
        """<p> Updates the configuration of an already enabled control.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of SUCCEEDED, supply parameters that are different from the currently configured parameters. Otherwise, Amazon Web Services Control Tower will not accept the request.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of FAILED, Amazon Web Services Control Tower updates the control to match any valid parameters that you supply.</p> <p>If the <code>DriftSummary</code> status for the control shows as <code>DRIFTED</code>, you cannot call this API. Instead, you can update the control by calling the <code>ResetEnabledControl</code> API. Alternatively, you can call <code>DisableControl</code> and then call <code>EnableControl</code> again. Also, you can run an extending governance operation to repair drift. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>. </p>

        Args:
            parameters: <p>A key/value pair, where <code>Key</code> is of type <code>String</code> and <code>Value</code> is of type <code>Document</code>.</p>
            enabled_control_identifier: <p> The ARN of the enabled control that will be updated. </p>

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
            req: "OperationRequest[capo_controltower.types.update_enabled_control_input.UpdateEnabledControlInput]",
        ) -> OperationResponse[
            "capo_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_enabled_control

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.update_enabled_control.update_enabled_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.update_enabled_control_input.UpdateEnabledControlInput = {
            "parameters": parameters,
            "enabled_control_identifier": enabled_control_identifier,
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
        target_identifier: Optional[
            "capo_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_controltower.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_controltower.types.enabled_control_filter.EnabledControlFilter"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> (
        "capo_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
    ):
        """<p>Lists the controls enabled by Amazon Web Services Control Tower on the specified organizational unit and the accounts it contains. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            target_identifier: <p>The ARN of the target. The value depends on the target type:</p> <ul> <li> <p>Organizational unit (OU) – Specify the ARN of the OU.</p> </li> <li> <p>Account – Specify the ARN of the account.</p> </li> </ul> <p>For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>
            filter: <p>An input filter for the <code>ListEnabledControls</code> API that lets you select the types of control operations to view.</p>
            include_children: <p>Specifies whether to include enabled controls from child organizational units and child accounts in the response.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.list_enabled_controls_input.ListEnabledControlsInput]",
        ) -> OperationResponse[
            "capo_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_enabled_controls

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.list_enabled_controls.list_enabled_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_enabled_controls_input.ListEnabledControlsInput = {}
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if include_children is not None:
            input_["include_children"] = include_children

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reset_enabled_control(
        self,
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> (
        "capo_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
    ):
        """<p>Resets an enabled control. Does not work for controls implemented with SCPs.</p>

        Args:
            enabled_control_identifier: <p>The ARN of the enabled control to be reset.</p>

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
            req: "OperationRequest[capo_controltower.types.reset_enabled_control_input.ResetEnabledControlInput]",
        ) -> OperationResponse[
            "capo_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_enabled_control

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.reset_enabled_control.reset_enabled_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.reset_enabled_control_input.ResetEnabledControlInput = {
            "enabled_control_identifier": enabled_control_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEnabledControlResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def create(
        self,
        control_identifier: "capo_controltower.types.control_identifier.ControlIdentifier",
        target_identifier: "capo_controltower.types.target_identifier.TargetIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_control_parameters.EnabledControlParameters"
        ] = None,
    ) -> "capo_controltower.types.enable_control_output.EnableControlOutput":
        """<p>This API call activates a control. It starts an asynchronous operation that creates Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>
            tags: <p>Tags to be applied to the <code>EnabledControl</code> resource.</p>
            parameters: <p>A list of input parameter values, which are specified to configure the control when you enable it.</p>

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
            req: "AsyncOperationRequest[capo_controltower.types.enable_control_input.EnableControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.enable_control_output.EnableControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.enable_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.enable_control.async_enable_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.enable_control_input.EnableControlInput = {
            "control_identifier": control_identifier,
            "target_identifier": target_identifier,
        }
        if tags is not None:
            input_["tags"] = tags
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_enabled_control_output.GetEnabledControlOutput":
        """<p>Retrieves details about an enabled control. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            enabled_control_identifier: <p>The <code>controlIdentifier</code> of the enabled control.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_enabled_control_input.GetEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_enabled_control_output.GetEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_enabled_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_enabled_control.async_get_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_enabled_control_input.GetEnabledControlInput = {
            "enabled_control_identifier": enabled_control_identifier
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
        parameters: "capo_controltower.types.enabled_control_parameters.EnabledControlParameters",
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput":
        """<p> Updates the configuration of an already enabled control.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of SUCCEEDED, supply parameters that are different from the currently configured parameters. Otherwise, Amazon Web Services Control Tower will not accept the request.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of FAILED, Amazon Web Services Control Tower updates the control to match any valid parameters that you supply.</p> <p>If the <code>DriftSummary</code> status for the control shows as <code>DRIFTED</code>, you cannot call this API. Instead, you can update the control by calling the <code>ResetEnabledControl</code> API. Alternatively, you can call <code>DisableControl</code> and then call <code>EnableControl</code> again. Also, you can run an extending governance operation to repair drift. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>. </p>

        Args:
            parameters: <p>A key/value pair, where <code>Key</code> is of type <code>String</code> and <code>Value</code> is of type <code>Document</code>.</p>
            enabled_control_identifier: <p> The ARN of the enabled control that will be updated. </p>

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
            req: "AsyncOperationRequest[capo_controltower.types.update_enabled_control_input.UpdateEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_enabled_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.update_enabled_control.async_update_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.update_enabled_control_input.UpdateEnabledControlInput = {
            "parameters": parameters,
            "enabled_control_identifier": enabled_control_identifier,
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
        target_identifier: Optional[
            "capo_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_controltower.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_controltower.types.enabled_control_filter.EnabledControlFilter"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> (
        "capo_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
    ):
        """<p>Lists the controls enabled by Amazon Web Services Control Tower on the specified organizational unit and the accounts it contains. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            target_identifier: <p>The ARN of the target. The value depends on the target type:</p> <ul> <li> <p>Organizational unit (OU) – Specify the ARN of the OU.</p> </li> <li> <p>Account – Specify the ARN of the account.</p> </li> </ul> <p>For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>
            filter: <p>An input filter for the <code>ListEnabledControls</code> API that lets you select the types of control operations to view.</p>
            include_children: <p>Specifies whether to include enabled controls from child organizational units and child accounts in the response.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_enabled_controls_input.ListEnabledControlsInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_enabled_controls

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_enabled_controls.async_list_enabled_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_enabled_controls_input.ListEnabledControlsInput = {}
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if include_children is not None:
            input_["include_children"] = include_children

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_enabled_control(
        self,
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> (
        "capo_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
    ):
        """<p>Resets an enabled control. Does not work for controls implemented with SCPs.</p>

        Args:
            enabled_control_identifier: <p>The ARN of the enabled control to be reset.</p>

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
            req: "AsyncOperationRequest[capo_controltower.types.reset_enabled_control_input.ResetEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_enabled_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.reset_enabled_control.async_reset_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.reset_enabled_control_input.ResetEnabledControlInput = {
            "enabled_control_identifier": enabled_control_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
