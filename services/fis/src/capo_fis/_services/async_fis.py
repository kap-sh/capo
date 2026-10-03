"""Generated from Smithy shape ``com.amazonaws.fis#FaultInjectionSimulator``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_fis._auth._signers
import capo_fis._auth._sigv4
from capo_fis._auth._identity import Credentials
from capo_fis._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_fis._auth._zapros_handler import AuthMiddleware
from capo_fis._pagination import resolve_path as _resolve_path
from capo_fis._services._aws_config import aaws_config
from capo_fis._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_fis.types.action_id
    import capo_fis.types.action_summary
    import capo_fis.types.client_token
    import capo_fis.types.create_experiment_template_action_input_map
    import capo_fis.types.create_experiment_template_experiment_options_input
    import capo_fis.types.create_experiment_template_log_configuration_input
    import capo_fis.types.create_experiment_template_report_configuration_input
    import capo_fis.types.create_experiment_template_request
    import capo_fis.types.create_experiment_template_response
    import capo_fis.types.create_experiment_template_stop_condition_input_list
    import capo_fis.types.create_experiment_template_target_input_map
    import capo_fis.types.create_target_account_configuration_request
    import capo_fis.types.create_target_account_configuration_response
    import capo_fis.types.delete_experiment_template_request
    import capo_fis.types.delete_experiment_template_response
    import capo_fis.types.delete_target_account_configuration_request
    import capo_fis.types.delete_target_account_configuration_response
    import capo_fis.types.experiment_id
    import capo_fis.types.experiment_summary
    import capo_fis.types.experiment_template_description
    import capo_fis.types.experiment_template_id
    import capo_fis.types.experiment_template_summary
    import capo_fis.types.get_action_request
    import capo_fis.types.get_action_response
    import capo_fis.types.get_experiment_request
    import capo_fis.types.get_experiment_response
    import capo_fis.types.get_experiment_target_account_configuration_request
    import capo_fis.types.get_experiment_target_account_configuration_response
    import capo_fis.types.get_experiment_template_request
    import capo_fis.types.get_experiment_template_response
    import capo_fis.types.get_safety_lever_request
    import capo_fis.types.get_safety_lever_response
    import capo_fis.types.get_target_account_configuration_request
    import capo_fis.types.get_target_account_configuration_response
    import capo_fis.types.get_target_resource_type_request
    import capo_fis.types.get_target_resource_type_response
    import capo_fis.types.list_actions_max_results
    import capo_fis.types.list_actions_request
    import capo_fis.types.list_actions_response
    import capo_fis.types.list_experiment_resolved_targets_max_results
    import capo_fis.types.list_experiment_resolved_targets_request
    import capo_fis.types.list_experiment_resolved_targets_response
    import capo_fis.types.list_experiment_target_account_configurations_request
    import capo_fis.types.list_experiment_target_account_configurations_response
    import capo_fis.types.list_experiment_templates_max_results
    import capo_fis.types.list_experiment_templates_request
    import capo_fis.types.list_experiment_templates_response
    import capo_fis.types.list_experiments_max_results
    import capo_fis.types.list_experiments_request
    import capo_fis.types.list_experiments_response
    import capo_fis.types.list_tags_for_resource_request
    import capo_fis.types.list_tags_for_resource_response
    import capo_fis.types.list_target_account_configurations_max_results
    import capo_fis.types.list_target_account_configurations_request
    import capo_fis.types.list_target_account_configurations_response
    import capo_fis.types.list_target_resource_types_max_results
    import capo_fis.types.list_target_resource_types_request
    import capo_fis.types.list_target_resource_types_response
    import capo_fis.types.next_token
    import capo_fis.types.resolved_target
    import capo_fis.types.resource_arn
    import capo_fis.types.role_arn
    import capo_fis.types.safety_lever_id
    import capo_fis.types.start_experiment_experiment_options_input
    import capo_fis.types.start_experiment_request
    import capo_fis.types.start_experiment_response
    import capo_fis.types.stop_experiment_request
    import capo_fis.types.stop_experiment_response
    import capo_fis.types.tag_key_list
    import capo_fis.types.tag_map
    import capo_fis.types.tag_resource_request
    import capo_fis.types.tag_resource_response
    import capo_fis.types.target_account_configuration_description
    import capo_fis.types.target_account_configuration_summary
    import capo_fis.types.target_account_id
    import capo_fis.types.target_name
    import capo_fis.types.target_resource_type_id
    import capo_fis.types.target_resource_type_summary
    import capo_fis.types.untag_resource_request
    import capo_fis.types.untag_resource_response
    import capo_fis.types.update_experiment_template_action_input_map
    import capo_fis.types.update_experiment_template_experiment_options_input
    import capo_fis.types.update_experiment_template_log_configuration_input
    import capo_fis.types.update_experiment_template_report_configuration_input
    import capo_fis.types.update_experiment_template_request
    import capo_fis.types.update_experiment_template_response
    import capo_fis.types.update_experiment_template_stop_condition_input_list
    import capo_fis.types.update_experiment_template_target_input_map
    import capo_fis.types.update_safety_lever_state_input
    import capo_fis.types.update_safety_lever_state_request
    import capo_fis.types.update_safety_lever_state_response
    import capo_fis.types.update_target_account_configuration_request
    import capo_fis.types.update_target_account_configuration_response


class AsyncfisClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncfisClient:
    """A client for the ``fis`` service.

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
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncfisClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncfisClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncfisClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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
        )
        return interceptors_, options_

    async def create_experiment_template(
        self,
        client_token: "capo_fis.types.client_token.ClientToken",
        description: "capo_fis.types.experiment_template_description.ExperimentTemplateDescription",
        stop_conditions: "capo_fis.types.create_experiment_template_stop_condition_input_list.CreateExperimentTemplateStopConditionInputList",
        actions: "capo_fis.types.create_experiment_template_action_input_map.CreateExperimentTemplateActionInputMap",
        role_arn: "capo_fis.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        targets: Optional[
            "capo_fis.types.create_experiment_template_target_input_map.CreateExperimentTemplateTargetInputMap"
        ] = None,
        tags: Optional["capo_fis.types.tag_map.TagMap"] = None,
        log_configuration: Optional[
            "capo_fis.types.create_experiment_template_log_configuration_input.CreateExperimentTemplateLogConfigurationInput"
        ] = None,
        experiment_options: Optional[
            "capo_fis.types.create_experiment_template_experiment_options_input.CreateExperimentTemplateExperimentOptionsInput"
        ] = None,
        experiment_report_configuration: Optional[
            "capo_fis.types.create_experiment_template_report_configuration_input.CreateExperimentTemplateReportConfigurationInput"
        ] = None,
    ) -> "capo_fis.types.create_experiment_template_response.CreateExperimentTemplateResponse":
        """<p>Creates an experiment template. </p> <p>An experiment template includes the following components:</p> <ul> <li> <p> <b>Targets</b>: A target can be a specific resource in your Amazon Web Services environment, or one or more resources that match criteria that you specify, for example, resources that have specific tags.</p> </li> <li> <p> <b>Actions</b>: The actions to carry out on the target. You can specify multiple actions, the duration of each action, and when to start each action during an experiment.</p> </li> <li> <p> <b>Stop conditions</b>: If a stop condition is triggered while an experiment is running, the experiment is automatically stopped. You can define a stop condition as a CloudWatch alarm.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html">experiment templates</a> in the <i>Fault Injection Service User Guide</i>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            description: <p>A description for the experiment template.</p>
            stop_conditions: <p>The stop conditions.</p>
            targets: <p>The targets for the experiment.</p>
            actions: <p>The actions for the experiment.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf.</p>
            tags: <p>The tags to apply to the experiment template.</p>
            log_configuration: <p>The configuration for experiment logging.</p>
            experiment_options: <p>The experiment options for the experiment template.</p>
            experiment_report_configuration: <p>The experiment report configuration for the experiment template.</p>

        Raises:
            capo_fis.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict.</p>
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.create_experiment_template_request.CreateExperimentTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.create_experiment_template_response.CreateExperimentTemplateResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.create_experiment_template

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.create_experiment_template.async_create_experiment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.create_experiment_template_request.CreateExperimentTemplateRequest = {
            "client_token": client_token,
            "description": description,
            "stop_conditions": stop_conditions,
            "actions": actions,
            "role_arn": role_arn,
        }
        if targets is not None:
            input_["targets"] = targets
        if tags is not None:
            input_["tags"] = tags
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if experiment_options is not None:
            input_["experiment_options"] = experiment_options
        if experiment_report_configuration is not None:
            input_["experiment_report_configuration"] = experiment_report_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_target_account_configuration(
        self,
        experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        account_id: "capo_fis.types.target_account_id.TargetAccountId",
        role_arn: "capo_fis.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        client_token: Optional["capo_fis.types.client_token.ClientToken"] = None,
        description: Optional[
            "capo_fis.types.target_account_configuration_description.TargetAccountConfigurationDescription"
        ] = None,
    ) -> "capo_fis.types.create_target_account_configuration_response.CreateTargetAccountConfigurationResponse":
        """<p>Creates a target account configuration for the experiment template. A target account configuration is required when <code>accountTargeting</code> of <code>experimentOptions</code> is set to <code>multi-account</code>. For more information, see <a href="https://docs.aws.amazon.com/fis/latest/userguide/experiment-options.html">experiment options</a> in the <i>Fault Injection Service User Guide</i>. </p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            experiment_template_id: <p>The experiment template ID.</p>
            account_id: <p>The Amazon Web Services account ID of the target account.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role for the target account.</p>
            description: <p>The description of the target account.</p>

        Raises:
            capo_fis.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict.</p>
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.create_target_account_configuration_request.CreateTargetAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.create_target_account_configuration_response.CreateTargetAccountConfigurationResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.create_target_account_configuration

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.create_target_account_configuration.async_create_target_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.create_target_account_configuration_request.CreateTargetAccountConfigurationRequest = {
            "experiment_template_id": experiment_template_id,
            "account_id": account_id,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_experiment_template(
        self,
        id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.delete_experiment_template_response.DeleteExperimentTemplateResponse":
        """<p>Deletes the specified experiment template.</p>

        Args:
            id: <p>The ID of the experiment template.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.delete_experiment_template_request.DeleteExperimentTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.delete_experiment_template_response.DeleteExperimentTemplateResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.delete_experiment_template

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.delete_experiment_template.async_delete_experiment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.delete_experiment_template_request.DeleteExperimentTemplateRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_target_account_configuration(
        self,
        experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        account_id: "capo_fis.types.target_account_id.TargetAccountId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.delete_target_account_configuration_response.DeleteTargetAccountConfigurationResponse":
        """<p>Deletes the specified target account configuration of the experiment template.</p>

        Args:
            experiment_template_id: <p>The ID of the experiment template.</p>
            account_id: <p>The Amazon Web Services account ID of the target account.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.delete_target_account_configuration_request.DeleteTargetAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.delete_target_account_configuration_response.DeleteTargetAccountConfigurationResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.delete_target_account_configuration

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.delete_target_account_configuration.async_delete_target_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.delete_target_account_configuration_request.DeleteTargetAccountConfigurationRequest = {
            "experiment_template_id": experiment_template_id,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_action(
        self,
        id: "capo_fis.types.action_id.ActionId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.get_action_response.GetActionResponse":
        """<p>Gets information about the specified FIS action.</p>

        Args:
            id: <p>The ID of the action.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.get_action_request.GetActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.get_action_response.GetActionResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.get_action

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.get_action.async_get_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.get_action_request.GetActionRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_experiment(
        self,
        id: "capo_fis.types.experiment_id.ExperimentId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.get_experiment_response.GetExperimentResponse":
        """<p>Gets information about the specified experiment.</p>

        Args:
            id: <p>The ID of the experiment.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.get_experiment_request.GetExperimentRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.get_experiment_response.GetExperimentResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.get_experiment

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.get_experiment.async_get_experiment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.get_experiment_request.GetExperimentRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_experiment_target_account_configuration(
        self,
        experiment_id: "capo_fis.types.experiment_id.ExperimentId",
        account_id: "capo_fis.types.target_account_id.TargetAccountId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.get_experiment_target_account_configuration_response.GetExperimentTargetAccountConfigurationResponse":
        """<p>Gets information about the specified target account configuration of the experiment.</p>

        Args:
            experiment_id: <p>The ID of the experiment.</p>
            account_id: <p>The Amazon Web Services account ID of the target account.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.get_experiment_target_account_configuration_request.GetExperimentTargetAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.get_experiment_target_account_configuration_response.GetExperimentTargetAccountConfigurationResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.get_experiment_target_account_configuration

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.get_experiment_target_account_configuration.async_get_experiment_target_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.get_experiment_target_account_configuration_request.GetExperimentTargetAccountConfigurationRequest = {
            "experiment_id": experiment_id,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_experiment_template(
        self,
        id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> (
        "capo_fis.types.get_experiment_template_response.GetExperimentTemplateResponse"
    ):
        """<p>Gets information about the specified experiment template.</p>

        Args:
            id: <p>The ID of the experiment template.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.get_experiment_template_request.GetExperimentTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.get_experiment_template_response.GetExperimentTemplateResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.get_experiment_template

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.get_experiment_template.async_get_experiment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.get_experiment_template_request.GetExperimentTemplateRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_safety_lever(
        self,
        id: "capo_fis.types.safety_lever_id.SafetyLeverId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.get_safety_lever_response.GetSafetyLeverResponse":
        """<p> Gets information about the specified safety lever. </p>

        Args:
            id: <p> The ID of the safety lever. </p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.get_safety_lever_request.GetSafetyLeverRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.get_safety_lever_response.GetSafetyLeverResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.get_safety_lever

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.get_safety_lever.async_get_safety_lever(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.get_safety_lever_request.GetSafetyLeverRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_target_account_configuration(
        self,
        experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        account_id: "capo_fis.types.target_account_id.TargetAccountId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.get_target_account_configuration_response.GetTargetAccountConfigurationResponse":
        """<p>Gets information about the specified target account configuration of the experiment template.</p>

        Args:
            experiment_template_id: <p>The ID of the experiment template.</p>
            account_id: <p>The Amazon Web Services account ID of the target account.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.get_target_account_configuration_request.GetTargetAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.get_target_account_configuration_response.GetTargetAccountConfigurationResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.get_target_account_configuration

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.get_target_account_configuration.async_get_target_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.get_target_account_configuration_request.GetTargetAccountConfigurationRequest = {
            "experiment_template_id": experiment_template_id,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_target_resource_type(
        self,
        resource_type: "capo_fis.types.target_resource_type_id.TargetResourceTypeId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> (
        "capo_fis.types.get_target_resource_type_response.GetTargetResourceTypeResponse"
    ):
        """<p>Gets information about the specified resource type.</p>

        Args:
            resource_type: <p>The resource type.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.get_target_resource_type_request.GetTargetResourceTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.get_target_resource_type_response.GetTargetResourceTypeResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.get_target_resource_type

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.get_target_resource_type.async_get_target_resource_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.get_target_resource_type_request.GetTargetResourceTypeRequest = {
            "resource_type": resource_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_actions(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_actions_max_results.ListActionsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "capo_fis.types.list_actions_response.ListActionsResponse":
        """<p>Lists the available FIS actions.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_actions_request.ListActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_actions_response.ListActionsResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_actions

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_actions.async_list_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_actions_request.ListActionsRequest = {}
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

    async def iter_list_actions(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_actions_max_results.ListActionsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_fis.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_actions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_experiment_resolved_targets(
        self,
        experiment_id: "capo_fis.types.experiment_id.ExperimentId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_experiment_resolved_targets_max_results.ListExperimentResolvedTargetsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
        target_name: Optional["capo_fis.types.target_name.TargetName"] = None,
    ) -> "capo_fis.types.list_experiment_resolved_targets_response.ListExperimentResolvedTargetsResponse":
        """<p>Lists the resolved targets information of the specified experiment.</p>

        Args:
            experiment_id: <p>The ID of the experiment.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>
            target_name: <p>The name of the target.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_experiment_resolved_targets_request.ListExperimentResolvedTargetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_experiment_resolved_targets_response.ListExperimentResolvedTargetsResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_experiment_resolved_targets

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_experiment_resolved_targets.async_list_experiment_resolved_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_experiment_resolved_targets_request.ListExperimentResolvedTargetsRequest = {
            "experiment_id": experiment_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if target_name is not None:
            input_["target_name"] = target_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_experiment_resolved_targets(
        self,
        experiment_id: "capo_fis.types.experiment_id.ExperimentId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_experiment_resolved_targets_max_results.ListExperimentResolvedTargetsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
        target_name: Optional["capo_fis.types.target_name.TargetName"] = None,
    ) -> "AsyncIterator[capo_fis.types.resolved_target.ResolvedTarget]":
        _token = next_token
        while True:
            _response = await self.list_experiment_resolved_targets(
                experiment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                target_name=target_name,
            )
            _page = _resolve_path(_response, ("resolved_targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_experiments(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_experiments_max_results.ListExperimentsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
        experiment_template_id: Optional[
            "capo_fis.types.experiment_template_id.ExperimentTemplateId"
        ] = None,
    ) -> "capo_fis.types.list_experiments_response.ListExperimentsResponse":
        """<p>Lists your experiments.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next page of results.</p>
            experiment_template_id: <p>The ID of the experiment template.</p>

        Raises:
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_experiments_request.ListExperimentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_experiments_response.ListExperimentsResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_experiments

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_experiments.async_list_experiments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_experiments_request.ListExperimentsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if experiment_template_id is not None:
            input_["experiment_template_id"] = experiment_template_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_experiments(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_experiments_max_results.ListExperimentsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
        experiment_template_id: Optional[
            "capo_fis.types.experiment_template_id.ExperimentTemplateId"
        ] = None,
    ) -> "AsyncIterator[capo_fis.types.experiment_summary.ExperimentSummary]":
        _token = next_token
        while True:
            _response = await self.list_experiments(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                experiment_template_id=experiment_template_id,
            )
            _page = _resolve_path(_response, ("experiments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_experiment_target_account_configurations(
        self,
        experiment_id: "capo_fis.types.experiment_id.ExperimentId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "capo_fis.types.list_experiment_target_account_configurations_response.ListExperimentTargetAccountConfigurationsResponse":
        """<p>Lists the target account configurations of the specified experiment.</p>

        Args:
            experiment_id: <p>The ID of the experiment.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_experiment_target_account_configurations_request.ListExperimentTargetAccountConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_experiment_target_account_configurations_response.ListExperimentTargetAccountConfigurationsResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_experiment_target_account_configurations

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_experiment_target_account_configurations.async_list_experiment_target_account_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_experiment_target_account_configurations_request.ListExperimentTargetAccountConfigurationsRequest = {
            "experiment_id": experiment_id
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_experiment_templates(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_experiment_templates_max_results.ListExperimentTemplatesMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "capo_fis.types.list_experiment_templates_response.ListExperimentTemplatesResponse":
        """<p>Lists your experiment templates.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_experiment_templates_request.ListExperimentTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_experiment_templates_response.ListExperimentTemplatesResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_experiment_templates

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_experiment_templates.async_list_experiment_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_experiment_templates_request.ListExperimentTemplatesRequest = {}
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

    async def iter_list_experiment_templates(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_experiment_templates_max_results.ListExperimentTemplatesMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_fis.types.experiment_template_summary.ExperimentTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_experiment_templates(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("experiment_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_fis.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_target_account_configurations(
        self,
        experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_target_account_configurations_max_results.ListTargetAccountConfigurationsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "capo_fis.types.list_target_account_configurations_response.ListTargetAccountConfigurationsResponse":
        """<p>Lists the target account configurations of the specified experiment template.</p>

        Args:
            experiment_template_id: <p>The ID of the experiment template.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_target_account_configurations_request.ListTargetAccountConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_target_account_configurations_response.ListTargetAccountConfigurationsResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_target_account_configurations

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_target_account_configurations.async_list_target_account_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_target_account_configurations_request.ListTargetAccountConfigurationsRequest = {
            "experiment_template_id": experiment_template_id
        }
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

    async def iter_list_target_account_configurations(
        self,
        experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_target_account_configurations_max_results.ListTargetAccountConfigurationsMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_fis.types.target_account_configuration_summary.TargetAccountConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_target_account_configurations(
                experiment_template_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("target_account_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_target_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_target_resource_types_max_results.ListTargetResourceTypesMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "capo_fis.types.list_target_resource_types_response.ListTargetResourceTypesResponse":
        """<p>Lists the target resource types.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.list_target_resource_types_request.ListTargetResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.list_target_resource_types_response.ListTargetResourceTypesResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.list_target_resource_types

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.list_target_resource_types.async_list_target_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.list_target_resource_types_request.ListTargetResourceTypesRequest = {}
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

    async def iter_list_target_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        max_results: Optional[
            "capo_fis.types.list_target_resource_types_max_results.ListTargetResourceTypesMaxResults"
        ] = None,
        next_token: Optional["capo_fis.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_fis.types.target_resource_type_summary.TargetResourceTypeSummary]":
        _token = next_token
        while True:
            _response = await self.list_target_resource_types(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("target_resource_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_experiment(
        self,
        client_token: "capo_fis.types.client_token.ClientToken",
        experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        experiment_options: Optional[
            "capo_fis.types.start_experiment_experiment_options_input.StartExperimentExperimentOptionsInput"
        ] = None,
        tags: Optional["capo_fis.types.tag_map.TagMap"] = None,
    ) -> "capo_fis.types.start_experiment_response.StartExperimentResponse":
        """<p>Starts running an experiment from the specified experiment template.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            experiment_template_id: <p>The ID of the experiment template.</p>
            experiment_options: <p>The experiment options for running the experiment.</p>
            tags: <p>The tags to apply to the experiment.</p>

        Raises:
            capo_fis.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict.</p>
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.start_experiment_request.StartExperimentRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.start_experiment_response.StartExperimentResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.start_experiment

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.start_experiment.async_start_experiment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.start_experiment_request.StartExperimentRequest = {
            "client_token": client_token,
            "experiment_template_id": experiment_template_id,
        }
        if experiment_options is not None:
            input_["experiment_options"] = experiment_options
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_experiment(
        self,
        id: "capo_fis.types.experiment_id.ExperimentId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.stop_experiment_response.StopExperimentResponse":
        """<p>Stops the specified experiment.</p>

        Args:
            id: <p>The ID of the experiment.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.stop_experiment_request.StopExperimentRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.stop_experiment_response.StopExperimentResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.stop_experiment

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.stop_experiment.async_stop_experiment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.stop_experiment_request.StopExperimentRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_fis.types.resource_arn.ResourceArn",
        tags: "capo_fis.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.tag_resource_response.TagResourceResponse":
        """<p>Applies the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags for the resource.</p>

        Raises:
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.tag_resource

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_fis.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        tag_keys: Optional["capo_fis.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_fis.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys to remove.</p>

        Raises:
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.untag_resource

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_experiment_template(
        self,
        id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        description: Optional[
            "capo_fis.types.experiment_template_description.ExperimentTemplateDescription"
        ] = None,
        stop_conditions: Optional[
            "capo_fis.types.update_experiment_template_stop_condition_input_list.UpdateExperimentTemplateStopConditionInputList"
        ] = None,
        targets: Optional[
            "capo_fis.types.update_experiment_template_target_input_map.UpdateExperimentTemplateTargetInputMap"
        ] = None,
        actions: Optional[
            "capo_fis.types.update_experiment_template_action_input_map.UpdateExperimentTemplateActionInputMap"
        ] = None,
        role_arn: Optional["capo_fis.types.role_arn.RoleArn"] = None,
        log_configuration: Optional[
            "capo_fis.types.update_experiment_template_log_configuration_input.UpdateExperimentTemplateLogConfigurationInput"
        ] = None,
        experiment_options: Optional[
            "capo_fis.types.update_experiment_template_experiment_options_input.UpdateExperimentTemplateExperimentOptionsInput"
        ] = None,
        experiment_report_configuration: Optional[
            "capo_fis.types.update_experiment_template_report_configuration_input.UpdateExperimentTemplateReportConfigurationInput"
        ] = None,
    ) -> "capo_fis.types.update_experiment_template_response.UpdateExperimentTemplateResponse":
        """<p>Updates the specified experiment template.</p>

        Args:
            id: <p>The ID of the experiment template.</p>
            description: <p>A description for the template.</p>
            stop_conditions: <p>The stop conditions for the experiment.</p>
            targets: <p>The targets for the experiment.</p>
            actions: <p>The actions for the experiment.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf.</p>
            log_configuration: <p>The configuration for experiment logging.</p>
            experiment_options: <p>The experiment options for the experiment template.</p>
            experiment_report_configuration: <p>The experiment report configuration for the experiment template.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.update_experiment_template_request.UpdateExperimentTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.update_experiment_template_response.UpdateExperimentTemplateResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.update_experiment_template

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.update_experiment_template.async_update_experiment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.update_experiment_template_request.UpdateExperimentTemplateRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if stop_conditions is not None:
            input_["stop_conditions"] = stop_conditions
        if targets is not None:
            input_["targets"] = targets
        if actions is not None:
            input_["actions"] = actions
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if experiment_options is not None:
            input_["experiment_options"] = experiment_options
        if experiment_report_configuration is not None:
            input_["experiment_report_configuration"] = experiment_report_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_safety_lever_state(
        self,
        id: "capo_fis.types.safety_lever_id.SafetyLeverId",
        state: "capo_fis.types.update_safety_lever_state_input.UpdateSafetyLeverStateInput",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
    ) -> "capo_fis.types.update_safety_lever_state_response.UpdateSafetyLeverStateResponse":
        """<p> Updates the specified safety lever state. </p>

        Args:
            id: <p> The ID of the safety lever. </p>
            state: <p> The state of the safety lever. </p>

        Raises:
            capo_fis.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict.</p>
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.update_safety_lever_state_request.UpdateSafetyLeverStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.update_safety_lever_state_response.UpdateSafetyLeverStateResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.update_safety_lever_state

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.update_safety_lever_state.async_update_safety_lever_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.update_safety_lever_state_request.UpdateSafetyLeverStateRequest = {
            "id": id,
            "state": state,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_target_account_configuration(
        self,
        experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId",
        account_id: "capo_fis.types.target_account_id.TargetAccountId",
        *,
        config_overrides: Optional[AsyncfisClientConfig] = None,
        role_arn: Optional["capo_fis.types.role_arn.RoleArn"] = None,
        description: Optional[
            "capo_fis.types.target_account_configuration_description.TargetAccountConfigurationDescription"
        ] = None,
    ) -> "capo_fis.types.update_target_account_configuration_response.UpdateTargetAccountConfigurationResponse":
        """<p>Updates the target account configuration for the specified experiment template.</p>

        Args:
            experiment_template_id: <p>The ID of the experiment template.</p>
            account_id: <p>The Amazon Web Services account ID of the target account.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role for the target account.</p>
            description: <p>The description of the target account.</p>

        Raises:
            capo_fis.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_fis.errors.validation_exception.ValidationException: <p>The specified input is not valid, or fails to satisfy the constraints for the request.</p>
            capo_fis.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_fis.types.update_target_account_configuration_request.UpdateTargetAccountConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_fis.types.update_target_account_configuration_response.UpdateTargetAccountConfigurationResponse"
        ]:
            import capo_fis._operations.fault_injection_simulator.update_target_account_configuration

            (
                output,
                http_response,
            ) = await capo_fis._operations.fault_injection_simulator.update_target_account_configuration.async_update_target_account_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_fis.types.update_target_account_configuration_request.UpdateTargetAccountConfigurationRequest = {
            "experiment_template_id": experiment_template_id,
            "account_id": account_id,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
