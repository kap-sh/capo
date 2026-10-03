"""Generated from Smithy shape ``com.amazonaws.sfn#AWSStepFunctions``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sfn._auth._signers
import capo_sfn._auth._sigv4
from capo_sfn._auth._identity import Credentials
from capo_sfn._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sfn._auth._zapros_handler import AuthMiddleware
from capo_sfn._pagination import resolve_path as _resolve_path
from capo_sfn._services._aws_config import aws_config
from capo_sfn._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_sfn.types.activity_list_item
    import capo_sfn.types.alias_description
    import capo_sfn.types.arn
    import capo_sfn.types.character_restricted_name
    import capo_sfn.types.client_token
    import capo_sfn.types.create_activity_input
    import capo_sfn.types.create_activity_output
    import capo_sfn.types.create_state_machine_alias_input
    import capo_sfn.types.create_state_machine_alias_output
    import capo_sfn.types.create_state_machine_input
    import capo_sfn.types.create_state_machine_output
    import capo_sfn.types.definition
    import capo_sfn.types.delete_activity_input
    import capo_sfn.types.delete_activity_output
    import capo_sfn.types.delete_state_machine_alias_input
    import capo_sfn.types.delete_state_machine_alias_output
    import capo_sfn.types.delete_state_machine_input
    import capo_sfn.types.delete_state_machine_output
    import capo_sfn.types.delete_state_machine_version_input
    import capo_sfn.types.delete_state_machine_version_output
    import capo_sfn.types.describe_activity_input
    import capo_sfn.types.describe_activity_output
    import capo_sfn.types.describe_execution_input
    import capo_sfn.types.describe_execution_output
    import capo_sfn.types.describe_map_run_input
    import capo_sfn.types.describe_map_run_output
    import capo_sfn.types.describe_state_machine_alias_input
    import capo_sfn.types.describe_state_machine_alias_output
    import capo_sfn.types.describe_state_machine_for_execution_input
    import capo_sfn.types.describe_state_machine_for_execution_output
    import capo_sfn.types.describe_state_machine_input
    import capo_sfn.types.describe_state_machine_output
    import capo_sfn.types.encryption_configuration
    import capo_sfn.types.execution_list_item
    import capo_sfn.types.execution_redrive_filter
    import capo_sfn.types.execution_status
    import capo_sfn.types.get_activity_task_input
    import capo_sfn.types.get_activity_task_output
    import capo_sfn.types.get_execution_history_input
    import capo_sfn.types.get_execution_history_output
    import capo_sfn.types.history_event
    import capo_sfn.types.include_execution_data_get_execution_history
    import capo_sfn.types.included_data
    import capo_sfn.types.inspection_level
    import capo_sfn.types.list_activities_input
    import capo_sfn.types.list_activities_output
    import capo_sfn.types.list_executions_input
    import capo_sfn.types.list_executions_output
    import capo_sfn.types.list_executions_page_token
    import capo_sfn.types.list_map_runs_input
    import capo_sfn.types.list_map_runs_output
    import capo_sfn.types.list_state_machine_aliases_input
    import capo_sfn.types.list_state_machine_aliases_output
    import capo_sfn.types.list_state_machine_versions_input
    import capo_sfn.types.list_state_machine_versions_output
    import capo_sfn.types.list_state_machines_input
    import capo_sfn.types.list_state_machines_output
    import capo_sfn.types.list_tags_for_resource_input
    import capo_sfn.types.list_tags_for_resource_output
    import capo_sfn.types.logging_configuration
    import capo_sfn.types.long_arn
    import capo_sfn.types.map_run_list_item
    import capo_sfn.types.max_concurrency
    import capo_sfn.types.mock_input
    import capo_sfn.types.name
    import capo_sfn.types.page_size
    import capo_sfn.types.page_token
    import capo_sfn.types.publish
    import capo_sfn.types.publish_state_machine_version_input
    import capo_sfn.types.publish_state_machine_version_output
    import capo_sfn.types.redrive_execution_input
    import capo_sfn.types.redrive_execution_output
    import capo_sfn.types.reveal_secrets
    import capo_sfn.types.reverse_order
    import capo_sfn.types.revision_id
    import capo_sfn.types.routing_configuration_list
    import capo_sfn.types.send_task_failure_input
    import capo_sfn.types.send_task_failure_output
    import capo_sfn.types.send_task_heartbeat_input
    import capo_sfn.types.send_task_heartbeat_output
    import capo_sfn.types.send_task_success_input
    import capo_sfn.types.send_task_success_output
    import capo_sfn.types.sensitive_cause
    import capo_sfn.types.sensitive_data
    import capo_sfn.types.sensitive_error
    import capo_sfn.types.start_execution_input
    import capo_sfn.types.start_execution_output
    import capo_sfn.types.start_sync_execution_input
    import capo_sfn.types.start_sync_execution_output
    import capo_sfn.types.state_machine_list_item
    import capo_sfn.types.state_machine_type
    import capo_sfn.types.stop_execution_input
    import capo_sfn.types.stop_execution_output
    import capo_sfn.types.tag_key_list
    import capo_sfn.types.tag_list
    import capo_sfn.types.tag_resource_input
    import capo_sfn.types.tag_resource_output
    import capo_sfn.types.task_token
    import capo_sfn.types.test_state_configuration
    import capo_sfn.types.test_state_input
    import capo_sfn.types.test_state_output
    import capo_sfn.types.test_state_state_name
    import capo_sfn.types.tolerated_failure_count
    import capo_sfn.types.tolerated_failure_percentage
    import capo_sfn.types.trace_header
    import capo_sfn.types.tracing_configuration
    import capo_sfn.types.untag_resource_input
    import capo_sfn.types.untag_resource_output
    import capo_sfn.types.update_map_run_input
    import capo_sfn.types.update_map_run_output
    import capo_sfn.types.update_state_machine_alias_input
    import capo_sfn.types.update_state_machine_alias_output
    import capo_sfn.types.update_state_machine_input
    import capo_sfn.types.update_state_machine_output
    import capo_sfn.types.validate_state_machine_definition_input
    import capo_sfn.types.validate_state_machine_definition_max_result
    import capo_sfn.types.validate_state_machine_definition_output
    import capo_sfn.types.validate_state_machine_definition_severity
    import capo_sfn.types.version_description


class SFNClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SFNClient:
    """A client for the ``SFN`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = SFNClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SFNClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SFNClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_activity(
        self,
        name: "capo_sfn.types.name.Name",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        tags: Optional["capo_sfn.types.tag_list.TagList"] = None,
        encryption_configuration: Optional[
            "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_sfn.types.create_activity_output.CreateActivityOutput":
        r"""<p>Creates an activity. An activity is a task that you write in any programming language and host on any machine that has access to Step Functions. Activities must poll Step Functions using the <code>GetActivityTask</code> API action and respond using <code>SendTask*</code> API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note> <note> <p> <code>CreateActivity</code> is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. <code>CreateActivity</code>'s idempotency check is based on the activity <code>name</code>. If a following request has different <code>tags</code> values, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, <code>tags</code> will not be updated, even if they are different.</p> </note>

        Args:
            name: <p>The name of the activity to create. This name must be unique for your Amazon Web Services account and region.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>
            tags: <p>The list of tags to add to a resource.</p> <p>An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>, and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html">Controlling Access Using IAM Tags</a>.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>
            encryption_configuration: <p>Settings to configure server-side encryption.</p>

        Raises:
            capo_sfn.errors.activity_already_exists.ActivityAlreadyExists: <p>Activity already exists. <code>EncryptionConfiguration</code> may not be updated.</p>
            capo_sfn.errors.activity_limit_exceeded.ActivityLimitExceeded: <p>The maximum number of activities has been reached. Existing activities must be deleted before a new activity can be created.</p>
            capo_sfn.errors.invalid_encryption_configuration.InvalidEncryptionConfiguration: <p>Received when <code>encryptionConfiguration</code> is specified but various conditions exist which make the configuration invalid. For example, if <code>type</code> is set to <code>CUSTOMER_MANAGED_KMS_KEY</code>, but <code>kmsKeyId</code> is null, or <code>kmsDataKeyReusePeriodSeconds</code> is not between 60 and 900, or the KMS key is not symmetric or inactive.</p>
            capo_sfn.errors.invalid_name.InvalidName: <p>The provided name is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.too_many_tags.TooManyTags: <p>You've exceeded the number of tags allowed for a resource. See the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/limits.html"> Limits Topic</a> in the Step Functions Developer Guide.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.create_activity_input.CreateActivityInput]",
        ) -> OperationResponse[
            "capo_sfn.types.create_activity_output.CreateActivityOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.create_activity

            output, http_response = (
                capo_sfn._operations.aws_step_functions.create_activity.create_activity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.create_activity_input.CreateActivityInput = {
            "name": name
        }
        if tags is not None:
            input_["tags"] = tags
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_state_machine(
        self,
        name: "capo_sfn.types.name.Name",
        definition: "capo_sfn.types.definition.Definition",
        role_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        type: Optional["capo_sfn.types.state_machine_type.StateMachineType"] = None,
        logging_configuration: Optional[
            "capo_sfn.types.logging_configuration.LoggingConfiguration"
        ] = None,
        tags: Optional["capo_sfn.types.tag_list.TagList"] = None,
        tracing_configuration: Optional[
            "capo_sfn.types.tracing_configuration.TracingConfiguration"
        ] = None,
        publish: Optional["capo_sfn.types.publish.Publish"] = None,
        version_description: Optional[
            "capo_sfn.types.version_description.VersionDescription"
        ] = None,
        encryption_configuration: Optional[
            "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_sfn.types.create_state_machine_output.CreateStateMachineOutput":
        r"""<p>Creates a state machine. A state machine consists of a collection of states that can do work (<code>Task</code> states), determine to which states to transition next (<code>Choice</code> states), stop an execution with an error (<code>Fail</code> states), and so on. State machines are specified using a JSON-based, structured language. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a> in the Step Functions User Guide.</p> <p>If you set the <code>publish</code> parameter of this API action to <code>true</code>, it publishes version <code>1</code> as the first revision of the state machine.</p> <p> For additional control over security, you can encrypt your data using a <b>customer-managed key</b> for Step Functions state machines. You can configure a symmetric KMS key and data key reuse period when creating or updating a <b>State Machine</b>. The execution history and state machine definition will be encrypted with the key applied to the State Machine. </p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note> <note> <p> <code>CreateStateMachine</code> is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. <code>CreateStateMachine</code>'s idempotency check is based on the state machine <code>name</code>, <code>definition</code>, <code>type</code>, <code>LoggingConfiguration</code>, <code>TracingConfiguration</code>, and <code>EncryptionConfiguration</code> The check is also based on the <code>publish</code> and <code>versionDescription</code> parameters. If a following request has a different <code>roleArn</code> or <code>tags</code>, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, <code>roleArn</code> and <code>tags</code> will not be updated, even if they are different.</p> </note>

        Args:
            name: <p>The name of the state machine. </p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>
            definition: <p>The Amazon States Language definition of the state machine. See <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to use for this state machine.</p>
            type: <p>Determines whether a Standard or Express state machine is created. The default is <code>STANDARD</code>. You cannot update the <code>type</code> of a state machine once it has been created.</p>
            logging_configuration: <p>Defines what execution history events are logged and where they are logged.</p> <note> <p>By default, the <code>level</code> is set to <code>OFF</code>. For more information see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html">Log Levels</a> in the Step Functions User Guide.</p> </note>
            tags: <p>Tags to be added when creating a state machine.</p> <p>An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>, and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html">Controlling Access Using IAM Tags</a>.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>
            tracing_configuration: <p>Selects whether X-Ray tracing is enabled.</p>
            publish: <p>Set to <code>true</code> to publish the first version of the state machine during creation. The default is <code>false</code>.</p>
            version_description: <p>Sets description about the state machine version. You can only set the description if the <code>publish</code> parameter is set to <code>true</code>. Otherwise, if you set <code>versionDescription</code>, but <code>publish</code> to <code>false</code>, this API action throws <code>ValidationException</code>.</p>
            encryption_configuration: <p>Settings to configure server-side encryption.</p>

        Raises:
            capo_sfn.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for <a>DeleteStateMachineVersion</a>, <a>PublishStateMachineVersion</a>, or <a>UpdateStateMachine</a> with the <code>publish</code> parameter set to <code>true</code>.</p> <p>HTTP Status Code: 409</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_definition.InvalidDefinition: <p>The provided Amazon States Language definition is not valid.</p>
            capo_sfn.errors.invalid_encryption_configuration.InvalidEncryptionConfiguration: <p>Received when <code>encryptionConfiguration</code> is specified but various conditions exist which make the configuration invalid. For example, if <code>type</code> is set to <code>CUSTOMER_MANAGED_KMS_KEY</code>, but <code>kmsKeyId</code> is null, or <code>kmsDataKeyReusePeriodSeconds</code> is not between 60 and 900, or the KMS key is not symmetric or inactive.</p>
            capo_sfn.errors.invalid_logging_configuration.InvalidLoggingConfiguration: <p>Configuration is not valid.</p>
            capo_sfn.errors.invalid_name.InvalidName: <p>The provided name is not valid.</p>
            capo_sfn.errors.invalid_tracing_configuration.InvalidTracingConfiguration: <p>Your <code>tracingConfiguration</code> key does not match, or <code>enabled</code> has not been set to <code>true</code> or <code>false</code>.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.state_machine_already_exists.StateMachineAlreadyExists: <p>A state machine with the same name but a different definition or role ARN already exists.</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.state_machine_limit_exceeded.StateMachineLimitExceeded: <p>The maximum number of state machines has been reached. Existing state machines must be deleted before a new state machine can be created.</p>
            capo_sfn.errors.state_machine_type_not_supported.StateMachineTypeNotSupported: <p>State machine type is not supported.</p>
            capo_sfn.errors.too_many_tags.TooManyTags: <p>You've exceeded the number of tags allowed for a resource. See the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/limits.html"> Limits Topic</a> in the Step Functions Developer Guide.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.create_state_machine_input.CreateStateMachineInput]",
        ) -> OperationResponse[
            "capo_sfn.types.create_state_machine_output.CreateStateMachineOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.create_state_machine

            output, http_response = (
                capo_sfn._operations.aws_step_functions.create_state_machine.create_state_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.create_state_machine_input.CreateStateMachineInput = {
            "name": name,
            "definition": definition,
            "role_arn": role_arn,
        }
        if type is not None:
            input_["type"] = type
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if tags is not None:
            input_["tags"] = tags
        if tracing_configuration is not None:
            input_["tracing_configuration"] = tracing_configuration
        if publish is not None:
            input_["publish"] = publish
        if version_description is not None:
            input_["version_description"] = version_description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_state_machine_alias(
        self,
        name: "capo_sfn.types.character_restricted_name.CharacterRestrictedName",
        routing_configuration: "capo_sfn.types.routing_configuration_list.RoutingConfigurationList",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        description: Optional[
            "capo_sfn.types.alias_description.AliasDescription"
        ] = None,
    ) -> (
        "capo_sfn.types.create_state_machine_alias_output.CreateStateMachineAliasOutput"
    ):
        """<p>Creates an <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a> for a state machine that points to one or two <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">versions</a> of the same state machine. You can set your application to call <a>StartExecution</a> with an alias and update the version the alias uses without changing the client's code.</p> <p>You can also map an alias to split <a>StartExecution</a> requests between two versions of a state machine. To do this, add a second <code>RoutingConfig</code> object in the <code>routingConfiguration</code> parameter. You must also specify the percentage of execution run requests each version should receive in both <code>RoutingConfig</code> objects. Step Functions randomly chooses which version runs a given execution based on the percentage you specify.</p> <p>To create an alias that points to a single version, specify a single <code>RoutingConfig</code> object with a <code>weight</code> set to 100.</p> <p>You can create up to 100 aliases for each state machine. You must delete unused aliases using the <a>DeleteStateMachineAlias</a> API action.</p> <p> <code>CreateStateMachineAlias</code> is an idempotent API. Step Functions bases the idempotency check on the <code>stateMachineArn</code>, <code>description</code>, <code>name</code>, and <code>routingConfiguration</code> parameters. Requests that contain the same values for these parameters return a successful idempotent response without creating a duplicate resource.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>DescribeStateMachineAlias</a> </p> </li> <li> <p> <a>ListStateMachineAliases</a> </p> </li> <li> <p> <a>UpdateStateMachineAlias</a> </p> </li> <li> <p> <a>DeleteStateMachineAlias</a> </p> </li> </ul>

        Args:
            description: <p>A description for the state machine alias.</p>
            name: <p>The name of the state machine alias.</p> <p>To avoid conflict with version ARNs, don't use an integer in the name of the alias.</p>
            routing_configuration: <p>The routing configuration of a state machine alias. The routing configuration shifts execution traffic between two state machine versions. <code>routingConfiguration</code> contains an array of <code>RoutingConfig</code> objects that specify up to two state machine versions. Step Functions then randomly choses which version to run an execution with based on the weight assigned to each <code>RoutingConfig</code>.</p>

        Raises:
            capo_sfn.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for <a>DeleteStateMachineVersion</a>, <a>PublishStateMachineVersion</a>, or <a>UpdateStateMachine</a> with the <code>publish</code> parameter set to <code>true</code>.</p> <p>HTTP Status Code: 409</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_name.InvalidName: <p>The provided name is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p> <p>HTTP Status Code: 402</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.create_state_machine_alias_input.CreateStateMachineAliasInput]",
        ) -> OperationResponse[
            "capo_sfn.types.create_state_machine_alias_output.CreateStateMachineAliasOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.create_state_machine_alias

            output, http_response = (
                capo_sfn._operations.aws_step_functions.create_state_machine_alias.create_state_machine_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.create_state_machine_alias_input.CreateStateMachineAliasInput = {
            "name": name,
            "routing_configuration": routing_configuration,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_activity(
        self,
        activity_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.delete_activity_output.DeleteActivityOutput":
        """<p>Deletes an activity.</p>

        Args:
            activity_arn: <p>The Amazon Resource Name (ARN) of the activity to delete.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.delete_activity_input.DeleteActivityInput]",
        ) -> OperationResponse[
            "capo_sfn.types.delete_activity_output.DeleteActivityOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.delete_activity

            output, http_response = (
                capo_sfn._operations.aws_step_functions.delete_activity.delete_activity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.delete_activity_input.DeleteActivityInput = {
            "activity_arn": activity_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_state_machine(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.delete_state_machine_output.DeleteStateMachineOutput":
        """<p>Deletes a state machine. This is an asynchronous operation. It sets the state machine's status to <code>DELETING</code> and begins the deletion process. A state machine is deleted only when all its executions are completed. On the next state transition, the state machine's executions are terminated.</p> <p>A qualified state machine ARN can either refer to a <i>Distributed Map state</i> defined within a state machine, a version ARN, or an alias ARN.</p> <p>The following are some examples of qualified and unqualified state machine ARNs:</p> <ul> <li> <p>The following qualified state machine ARN refers to a <i>Distributed Map state</i> with a label <code>mapStateLabel</code> in a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel</code> </p> <note> <p>If you provide a qualified state machine ARN that refers to a <i>Distributed Map state</i>, the request fails with <code>ValidationException</code>.</p> </note> </li> <li> <p>The following unqualified state machine ARN refers to a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:partition:states:region:account-id:stateMachine:myStateMachine</code> </p> </li> </ul> <p>This API action also deletes all <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">versions</a> and <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">aliases</a> associated with a state machine.</p> <note> <p>For <code>EXPRESS</code> state machines, the deletion happens eventually (usually in less than a minute). Running executions may emit logs after <code>DeleteStateMachine</code> API is called.</p> </note>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine to delete.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.delete_state_machine_input.DeleteStateMachineInput]",
        ) -> OperationResponse[
            "capo_sfn.types.delete_state_machine_output.DeleteStateMachineOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.delete_state_machine

            output, http_response = (
                capo_sfn._operations.aws_step_functions.delete_state_machine.delete_state_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.delete_state_machine_input.DeleteStateMachineInput = {
            "state_machine_arn": state_machine_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_state_machine_alias(
        self,
        state_machine_alias_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> (
        "capo_sfn.types.delete_state_machine_alias_output.DeleteStateMachineAliasOutput"
    ):
        """<p>Deletes a state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a>.</p> <p>After you delete a state machine alias, you can't use it to start executions. When you delete a state machine alias, Step Functions doesn't delete the state machine versions that alias references.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>CreateStateMachineAlias</a> </p> </li> <li> <p> <a>DescribeStateMachineAlias</a> </p> </li> <li> <p> <a>ListStateMachineAliases</a> </p> </li> <li> <p> <a>UpdateStateMachineAlias</a> </p> </li> </ul>

        Args:
            state_machine_alias_arn: <p>The Amazon Resource Name (ARN) of the state machine alias to delete.</p>

        Raises:
            capo_sfn.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for <a>DeleteStateMachineVersion</a>, <a>PublishStateMachineVersion</a>, or <a>UpdateStateMachine</a> with the <code>publish</code> parameter set to <code>true</code>.</p> <p>HTTP Status Code: 409</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.delete_state_machine_alias_input.DeleteStateMachineAliasInput]",
        ) -> OperationResponse[
            "capo_sfn.types.delete_state_machine_alias_output.DeleteStateMachineAliasOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.delete_state_machine_alias

            output, http_response = (
                capo_sfn._operations.aws_step_functions.delete_state_machine_alias.delete_state_machine_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.delete_state_machine_alias_input.DeleteStateMachineAliasInput = {
            "state_machine_alias_arn": state_machine_alias_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_state_machine_version(
        self,
        state_machine_version_arn: "capo_sfn.types.long_arn.LongArn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.delete_state_machine_version_output.DeleteStateMachineVersionOutput":
        """<p>Deletes a state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>. After you delete a version, you can't call <a>StartExecution</a> using that version's ARN or use the version with a state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a>.</p> <note> <p>Deleting a state machine version won't terminate its in-progress executions.</p> </note> <note> <p>You can't delete a state machine version currently referenced by one or more aliases. Before you delete a version, you must either delete the aliases or update them to point to another state machine version.</p> </note> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>PublishStateMachineVersion</a> </p> </li> <li> <p> <a>ListStateMachineVersions</a> </p> </li> </ul>

        Args:
            state_machine_version_arn: <p>The Amazon Resource Name (ARN) of the state machine version to delete.</p>

        Raises:
            capo_sfn.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for <a>DeleteStateMachineVersion</a>, <a>PublishStateMachineVersion</a>, or <a>UpdateStateMachine</a> with the <code>publish</code> parameter set to <code>true</code>.</p> <p>HTTP Status Code: 409</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.delete_state_machine_version_input.DeleteStateMachineVersionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.delete_state_machine_version_output.DeleteStateMachineVersionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.delete_state_machine_version

            output, http_response = (
                capo_sfn._operations.aws_step_functions.delete_state_machine_version.delete_state_machine_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.delete_state_machine_version_input.DeleteStateMachineVersionInput = {
            "state_machine_version_arn": state_machine_version_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_activity(
        self,
        activity_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.describe_activity_output.DescribeActivityOutput":
        """<p>Describes an activity.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note>

        Args:
            activity_arn: <p>The Amazon Resource Name (ARN) of the activity to describe.</p>

        Raises:
            capo_sfn.errors.activity_does_not_exist.ActivityDoesNotExist: <p>The specified activity does not exist.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.describe_activity_input.DescribeActivityInput]",
        ) -> OperationResponse[
            "capo_sfn.types.describe_activity_output.DescribeActivityOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.describe_activity

            output, http_response = (
                capo_sfn._operations.aws_step_functions.describe_activity.describe_activity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.describe_activity_input.DescribeActivityInput = {
            "activity_arn": activity_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_execution(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        included_data: Optional["capo_sfn.types.included_data.IncludedData"] = None,
    ) -> "capo_sfn.types.describe_execution_output.DescribeExecutionOutput":
        """<p>Provides information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata. If you've <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html">redriven</a> an execution, you can use this API action to return information about the redrives of that execution. In addition, you can use this API action to return the Map Run Amazon Resource Name (ARN) if the execution was dispatched by a Map Run.</p> <p>If you specify a version or alias ARN when you call the <a>StartExecution</a> API action, <code>DescribeExecution</code> returns that ARN.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note> <p>Executions of an <code>EXPRESS</code> state machine aren't supported by <code>DescribeExecution</code> unless a Map Run dispatched them.</p>

        Args:
            execution_arn: <p>The Amazon Resource Name (ARN) of the execution to describe.</p>
            included_data: <p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call DescribeStateMachine API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p>

        Raises:
            capo_sfn.errors.execution_does_not_exist.ExecutionDoesNotExist: <p>The specified execution does not exist.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.describe_execution_input.DescribeExecutionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.describe_execution_output.DescribeExecutionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.describe_execution

            output, http_response = (
                capo_sfn._operations.aws_step_functions.describe_execution.describe_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.describe_execution_input.DescribeExecutionInput = {
            "execution_arn": execution_arn
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_map_run(
        self,
        map_run_arn: "capo_sfn.types.long_arn.LongArn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.describe_map_run_output.DescribeMapRunOutput":
        """<p>Provides information about a Map Run's configuration, progress, and results. If you've <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html">redriven</a> a Map Run, this API action also returns information about the redrives of that Map Run. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html">Examining Map Run</a> in the <i>Step Functions Developer Guide</i>.</p>

        Args:
            map_run_arn: <p>The Amazon Resource Name (ARN) that identifies a Map Run.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.describe_map_run_input.DescribeMapRunInput]",
        ) -> OperationResponse[
            "capo_sfn.types.describe_map_run_output.DescribeMapRunOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.describe_map_run

            output, http_response = (
                capo_sfn._operations.aws_step_functions.describe_map_run.describe_map_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.describe_map_run_input.DescribeMapRunInput = {
            "map_run_arn": map_run_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_state_machine(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        included_data: Optional["capo_sfn.types.included_data.IncludedData"] = None,
    ) -> "capo_sfn.types.describe_state_machine_output.DescribeStateMachineOutput":
        """<p>Provides information about a state machine's definition, its IAM role Amazon Resource Name (ARN), and configuration.</p> <p>A qualified state machine ARN can either refer to a <i>Distributed Map state</i> defined within a state machine, a version ARN, or an alias ARN.</p> <p>The following are some examples of qualified and unqualified state machine ARNs:</p> <ul> <li> <p>The following qualified state machine ARN refers to a <i>Distributed Map state</i> with a label <code>mapStateLabel</code> in a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel</code> </p> <note> <p>If you provide a qualified state machine ARN that refers to a <i>Distributed Map state</i>, the request fails with <code>ValidationException</code>.</p> </note> </li> <li> <p>The following qualified state machine ARN refers to an alias named <code>PROD</code>.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD></code> </p> <note> <p>If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.</p> </note> </li> <li> <p>The following unqualified state machine ARN refers to a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine></code> </p> </li> </ul> <p>This API action returns the details for a state machine version if the <code>stateMachineArn</code> you specify is a state machine version ARN.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine for which you want the information.</p> <p>If you specify a state machine version ARN, this API returns details about that version. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, <code>stateMachineARN:1</code>.</p>
            included_data: <p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call the API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p> <note> <p> When calling a labelled ARN for an encrypted state machine, the <code>includedData = METADATA_ONLY</code> parameter will not apply because Step Functions needs to decrypt the entire state machine definition to get the Distributed Map state’s definition. In this case, the API caller needs to have <code>kms:Decrypt</code> permission. </p> </note>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist: <p>The specified state machine does not exist.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.describe_state_machine_input.DescribeStateMachineInput]",
        ) -> OperationResponse[
            "capo_sfn.types.describe_state_machine_output.DescribeStateMachineOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.describe_state_machine

            output, http_response = (
                capo_sfn._operations.aws_step_functions.describe_state_machine.describe_state_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.describe_state_machine_input.DescribeStateMachineInput = {
            "state_machine_arn": state_machine_arn
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_state_machine_alias(
        self,
        state_machine_alias_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.describe_state_machine_alias_output.DescribeStateMachineAliasOutput":
        """<p>Returns details about a state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>CreateStateMachineAlias</a> </p> </li> <li> <p> <a>ListStateMachineAliases</a> </p> </li> <li> <p> <a>UpdateStateMachineAlias</a> </p> </li> <li> <p> <a>DeleteStateMachineAlias</a> </p> </li> </ul>

        Args:
            state_machine_alias_arn: <p>The Amazon Resource Name (ARN) of the state machine alias.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.describe_state_machine_alias_input.DescribeStateMachineAliasInput]",
        ) -> OperationResponse[
            "capo_sfn.types.describe_state_machine_alias_output.DescribeStateMachineAliasOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.describe_state_machine_alias

            output, http_response = (
                capo_sfn._operations.aws_step_functions.describe_state_machine_alias.describe_state_machine_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.describe_state_machine_alias_input.DescribeStateMachineAliasInput = {
            "state_machine_alias_arn": state_machine_alias_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_state_machine_for_execution(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        included_data: Optional["capo_sfn.types.included_data.IncludedData"] = None,
    ) -> "capo_sfn.types.describe_state_machine_for_execution_output.DescribeStateMachineForExecutionOutput":
        """<p>Provides information about a state machine's definition, its execution role ARN, and configuration. If a Map Run dispatched the execution, this action returns the Map Run Amazon Resource Name (ARN) in the response. The state machine returned is the state machine associated with the Map Run.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note> <p>This API action is not supported by <code>EXPRESS</code> state machines.</p>

        Args:
            execution_arn: <p>The Amazon Resource Name (ARN) of the execution you want state machine information for.</p>
            included_data: <p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call the API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p>

        Raises:
            capo_sfn.errors.execution_does_not_exist.ExecutionDoesNotExist: <p>The specified execution does not exist.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.describe_state_machine_for_execution_input.DescribeStateMachineForExecutionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.describe_state_machine_for_execution_output.DescribeStateMachineForExecutionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.describe_state_machine_for_execution

            output, http_response = (
                capo_sfn._operations.aws_step_functions.describe_state_machine_for_execution.describe_state_machine_for_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.describe_state_machine_for_execution_input.DescribeStateMachineForExecutionInput = {
            "execution_arn": execution_arn
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_activity_task(
        self,
        activity_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        worker_name: Optional["capo_sfn.types.name.Name"] = None,
    ) -> "capo_sfn.types.get_activity_task_output.GetActivityTaskOutput":
        """<p>Used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available (i.e. an execution of a task of this type is needed.) The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns a <code>taskToken</code> with a null string.</p> <important> <p>Workers should set their client side socket timeout to at least 65 seconds (5 seconds higher than the maximum time the service may hold the poll request).</p> <p>Polling with <code>GetActivityTask</code> can cause latency in some implementations. See <a href="https://docs.aws.amazon.com/step-functions/latest/dg/bp-activity-pollers.html">Avoid Latency When Polling for Activity Tasks</a> in the Step Functions Developer Guide.</p> </important>

        Args:
            activity_arn: <p>The Amazon Resource Name (ARN) of the activity to retrieve tasks from (assigned when you create the task using <a>CreateActivity</a>.)</p>
            worker_name: <p>You can provide an arbitrary name in order to identify the worker that the task is assigned to. This name is used when it is logged in the execution history.</p>

        Raises:
            capo_sfn.errors.activity_does_not_exist.ActivityDoesNotExist: <p>The specified activity does not exist.</p>
            capo_sfn.errors.activity_worker_limit_exceeded.ActivityWorkerLimitExceeded: <p>The maximum number of workers concurrently polling for activity tasks has been reached.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.get_activity_task_input.GetActivityTaskInput]",
        ) -> OperationResponse[
            "capo_sfn.types.get_activity_task_output.GetActivityTaskOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.get_activity_task

            output, http_response = (
                capo_sfn._operations.aws_step_functions.get_activity_task.get_activity_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.get_activity_task_input.GetActivityTaskInput = {
            "activity_arn": activity_arn
        }
        if worker_name is not None:
            input_["worker_name"] = worker_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_execution_history(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_sfn.types.reverse_order.ReverseOrder"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
        include_execution_data: Optional[
            "capo_sfn.types.include_execution_data_get_execution_history.IncludeExecutionDataGetExecutionHistory"
        ] = None,
    ) -> "capo_sfn.types.get_execution_history_output.GetExecutionHistoryOutput":
        """<p>Returns the history of the specified execution as a list of events. By default, the results are returned in ascending order of the <code>timeStamp</code> of the events. Use the <code>reverseOrder</code> parameter to get the latest events first.</p> <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p> <p>This API action is not supported by <code>EXPRESS</code> state machines.</p>

        Args:
            execution_arn: <p>The Amazon Resource Name (ARN) of the execution.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            reverse_order: <p>Lists events in descending order of their <code>timeStamp</code>.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            include_execution_data: <p>You can select whether execution data (input or output of a history event) is returned. The default is <code>true</code>.</p>

        Raises:
            capo_sfn.errors.execution_does_not_exist.ExecutionDoesNotExist: <p>The specified execution does not exist.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.get_execution_history_input.GetExecutionHistoryInput]",
        ) -> OperationResponse[
            "capo_sfn.types.get_execution_history_output.GetExecutionHistoryOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.get_execution_history

            output, http_response = (
                capo_sfn._operations.aws_step_functions.get_execution_history.get_execution_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.get_execution_history_input.GetExecutionHistoryInput = {
            "execution_arn": execution_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if next_token is not None:
            input_["next_token"] = next_token
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_execution_history(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_sfn.types.reverse_order.ReverseOrder"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
        include_execution_data: Optional[
            "capo_sfn.types.include_execution_data_get_execution_history.IncludeExecutionDataGetExecutionHistory"
        ] = None,
    ) -> "Iterator[capo_sfn.types.history_event.HistoryEvent]":
        _token = next_token
        while True:
            _response = self.get_execution_history(
                execution_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                reverse_order=reverse_order,
                next_token=_token,
                include_execution_data=include_execution_data,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_activities(
        self,
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
    ) -> "capo_sfn.types.list_activities_output.ListActivitiesOutput":
        """<p>Lists the existing activities.</p> <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>

        Raises:
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.list_activities_input.ListActivitiesInput]",
        ) -> OperationResponse[
            "capo_sfn.types.list_activities_output.ListActivitiesOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.list_activities

            output, http_response = (
                capo_sfn._operations.aws_step_functions.list_activities.list_activities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.list_activities_input.ListActivitiesInput = {}
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

    def iter_list_activities(
        self,
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
    ) -> "Iterator[capo_sfn.types.activity_list_item.ActivityListItem]":
        _token = next_token
        while True:
            _response = self.list_activities(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_executions(
        self,
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        state_machine_arn: Optional["capo_sfn.types.arn.Arn"] = None,
        status_filter: Optional[
            "capo_sfn.types.execution_status.ExecutionStatus"
        ] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_sfn.types.list_executions_page_token.ListExecutionsPageToken"
        ] = None,
        map_run_arn: Optional["capo_sfn.types.long_arn.LongArn"] = None,
        redrive_filter: Optional[
            "capo_sfn.types.execution_redrive_filter.ExecutionRedriveFilter"
        ] = None,
    ) -> "capo_sfn.types.list_executions_output.ListExecutionsOutput":
        """<p>Lists all executions of a state machine or a Map Run. You can list all executions related to a state machine by specifying a state machine Amazon Resource Name (ARN), or those related to a Map Run by specifying a Map Run ARN. Using this API action, you can also list all <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html">redriven</a> executions.</p> <p>You can also provide a state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a> ARN or <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a> ARN to list the executions associated with a specific alias or version.</p> <p>Results are sorted by time, with the most recent execution first. Running executions are sorted by their <code>startDate</code> or <code>redriveDate</code>, and other executions are sorted by their <code>stopDate</code>.</p> <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note> <p>This API action is not supported by <code>EXPRESS</code> state machines. However, you may list <code>EXPRESS</code> children started by a map run using the <code>mapRunArn</code> parameter.</p>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine whose executions is listed.</p> <p>You can specify either a <code>mapRunArn</code> or a <code>stateMachineArn</code>, but not both.</p> <p>You can also return a list of executions associated with a specific <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a> or <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>, by specifying an alias ARN or a version ARN in the <code>stateMachineArn</code> parameter.</p>
            status_filter: <p>If specified, only list the executions whose current execution status matches the given filter.</p> <p>If you provide a <code>PENDING_REDRIVE</code> statusFilter, you must specify <code>mapRunArn</code>. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html#redrive-child-workflow-behavior">Child workflow execution redrive behaviour</a> in the <i>Step Functions Developer Guide</i>. </p> <p>If you provide a stateMachineArn and a <code>PENDING_REDRIVE</code> statusFilter, the API returns a validation exception.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            map_run_arn: <p>The Amazon Resource Name (ARN) of the Map Run that started the child workflow executions. If the <code>mapRunArn</code> field is specified, a list of all of the child workflow executions started by a Map Run is returned. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html">Examining Map Run</a> in the <i>Step Functions Developer Guide</i>.</p> <p>You can specify either a <code>mapRunArn</code> or a <code>stateMachineArn</code>, but not both.</p>
            redrive_filter: <p>Sets a filter to list executions based on whether or not they have been redriven.</p> <p>For a Distributed Map, <code>redriveFilter</code> sets a filter to list child workflow executions based on whether or not they have been redriven.</p> <p>If you do not provide a <code>redriveFilter</code>, Step Functions returns a list of both redriven and non-redriven executions.</p> <p>If you provide a state machine ARN in <code>redriveFilter</code>, the API returns a validation exception.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist: <p>The specified state machine does not exist.</p>
            capo_sfn.errors.state_machine_type_not_supported.StateMachineTypeNotSupported: <p>State machine type is not supported.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.list_executions_input.ListExecutionsInput]",
        ) -> OperationResponse[
            "capo_sfn.types.list_executions_output.ListExecutionsOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.list_executions

            output, http_response = (
                capo_sfn._operations.aws_step_functions.list_executions.list_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.list_executions_input.ListExecutionsInput = {}
        if state_machine_arn is not None:
            input_["state_machine_arn"] = state_machine_arn
        if status_filter is not None:
            input_["status_filter"] = status_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if map_run_arn is not None:
            input_["map_run_arn"] = map_run_arn
        if redrive_filter is not None:
            input_["redrive_filter"] = redrive_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_executions(
        self,
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        state_machine_arn: Optional["capo_sfn.types.arn.Arn"] = None,
        status_filter: Optional[
            "capo_sfn.types.execution_status.ExecutionStatus"
        ] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_sfn.types.list_executions_page_token.ListExecutionsPageToken"
        ] = None,
        map_run_arn: Optional["capo_sfn.types.long_arn.LongArn"] = None,
        redrive_filter: Optional[
            "capo_sfn.types.execution_redrive_filter.ExecutionRedriveFilter"
        ] = None,
    ) -> "Iterator[capo_sfn.types.execution_list_item.ExecutionListItem]":
        _token = next_token
        while True:
            _response = self.list_executions(
                config_overrides=config_overrides,
                state_machine_arn=state_machine_arn,
                status_filter=status_filter,
                max_results=max_results,
                next_token=_token,
                map_run_arn=map_run_arn,
                redrive_filter=redrive_filter,
            )
            _page = _resolve_path(_response, ("executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_map_runs(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
    ) -> "capo_sfn.types.list_map_runs_output.ListMapRunsOutput":
        """<p>Lists all Map Runs that were started by a given state machine execution. Use this API action to obtain Map Run ARNs, and then call <code>DescribeMapRun</code> to obtain more information, if needed.</p>

        Args:
            execution_arn: <p>The Amazon Resource Name (ARN) of the execution for which the Map Runs must be listed.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>

        Raises:
            capo_sfn.errors.execution_does_not_exist.ExecutionDoesNotExist: <p>The specified execution does not exist.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.list_map_runs_input.ListMapRunsInput]",
        ) -> OperationResponse["capo_sfn.types.list_map_runs_output.ListMapRunsOutput"]:
            import capo_sfn._operations.aws_step_functions.list_map_runs

            output, http_response = (
                capo_sfn._operations.aws_step_functions.list_map_runs.list_map_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.list_map_runs_input.ListMapRunsInput = {
            "execution_arn": execution_arn
        }
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

    def iter_list_map_runs(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
    ) -> "Iterator[capo_sfn.types.map_run_list_item.MapRunListItem]":
        _token = next_token
        while True:
            _response = self.list_map_runs(
                execution_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("map_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_state_machine_aliases(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
    ) -> (
        "capo_sfn.types.list_state_machine_aliases_output.ListStateMachineAliasesOutput"
    ):
        """<p>Lists <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">aliases</a> for a specified state machine ARN. Results are sorted by time, with the most recently created aliases listed first. </p> <p>To list aliases that reference a state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>, you can specify the version ARN in the <code>stateMachineArn</code> parameter.</p> <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>CreateStateMachineAlias</a> </p> </li> <li> <p> <a>DescribeStateMachineAlias</a> </p> </li> <li> <p> <a>UpdateStateMachineAlias</a> </p> </li> <li> <p> <a>DeleteStateMachineAlias</a> </p> </li> </ul>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine for which you want to list aliases.</p> <p>If you specify a state machine version ARN, this API returns a list of aliases for that version.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist: <p>The specified state machine does not exist.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.list_state_machine_aliases_input.ListStateMachineAliasesInput]",
        ) -> OperationResponse[
            "capo_sfn.types.list_state_machine_aliases_output.ListStateMachineAliasesOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.list_state_machine_aliases

            output, http_response = (
                capo_sfn._operations.aws_step_functions.list_state_machine_aliases.list_state_machine_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.list_state_machine_aliases_input.ListStateMachineAliasesInput = {
            "state_machine_arn": state_machine_arn
        }
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

    def list_state_machines(
        self,
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
    ) -> "capo_sfn.types.list_state_machines_output.ListStateMachinesOutput":
        """<p>Lists the existing state machines.</p> <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.</p> </note>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>

        Raises:
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.list_state_machines_input.ListStateMachinesInput]",
        ) -> OperationResponse[
            "capo_sfn.types.list_state_machines_output.ListStateMachinesOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.list_state_machines

            output, http_response = (
                capo_sfn._operations.aws_step_functions.list_state_machines.list_state_machines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.list_state_machines_input.ListStateMachinesInput = {}
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

    def iter_list_state_machines(
        self,
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
    ) -> "Iterator[capo_sfn.types.state_machine_list_item.StateMachineListItem]":
        _token = next_token
        while True:
            _response = self.list_state_machines(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("state_machines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_state_machine_versions(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        next_token: Optional["capo_sfn.types.page_token.PageToken"] = None,
        max_results: Optional["capo_sfn.types.page_size.PageSize"] = None,
    ) -> "capo_sfn.types.list_state_machine_versions_output.ListStateMachineVersionsOutput":
        """<p>Lists <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">versions</a> for the specified state machine Amazon Resource Name (ARN).</p> <p>The results are sorted in descending order of the version creation time.</p> <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>PublishStateMachineVersion</a> </p> </li> <li> <p> <a>DeleteStateMachineVersion</a> </p> </li> </ul>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.list_state_machine_versions_input.ListStateMachineVersionsInput]",
        ) -> OperationResponse[
            "capo_sfn.types.list_state_machine_versions_output.ListStateMachineVersionsOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.list_state_machine_versions

            output, http_response = (
                capo_sfn._operations.aws_step_functions.list_state_machine_versions.list_state_machine_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.list_state_machine_versions_input.ListStateMachineVersionsInput = {
            "state_machine_arn": state_machine_arn
        }
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List tags for a given resource.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the Step Functions state machine or activity.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_sfn.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.list_tags_for_resource

            output, http_response = (
                capo_sfn._operations.aws_step_functions.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_state_machine_version(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        revision_id: Optional["capo_sfn.types.revision_id.RevisionId"] = None,
        description: Optional[
            "capo_sfn.types.version_description.VersionDescription"
        ] = None,
    ) -> "capo_sfn.types.publish_state_machine_version_output.PublishStateMachineVersionOutput":
        """<p>Creates a <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a> from the current revision of a state machine. Use versions to create immutable snapshots of your state machine. You can start executions from versions either directly or with an alias. To create an alias, use <a>CreateStateMachineAlias</a>.</p> <p>You can publish up to 1000 versions for each state machine. You must manually delete unused versions using the <a>DeleteStateMachineVersion</a> API action.</p> <p> <code>PublishStateMachineVersion</code> is an idempotent API. It doesn't create a duplicate state machine version if it already exists for the current revision. Step Functions bases <code>PublishStateMachineVersion</code>'s idempotency check on the <code>stateMachineArn</code>, <code>name</code>, and <code>revisionId</code> parameters. Requests with the same parameters return a successful idempotent response. If you don't specify a <code>revisionId</code>, Step Functions checks for a previously published version of the state machine's current revision.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>DeleteStateMachineVersion</a> </p> </li> <li> <p> <a>ListStateMachineVersions</a> </p> </li> </ul>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine.</p>
            revision_id: <p>Only publish the state machine version if the current state machine's revision ID matches the specified ID.</p> <p>Use this option to avoid publishing a version if the state machine changed since you last updated it. If the specified revision ID doesn't match the state machine's current revision ID, the API returns <code>ConflictException</code>.</p> <note> <p>To specify an initial revision ID for a state machine with no revision ID assigned, specify the string <code>INITIAL</code> for the <code>revisionId</code> parameter. For example, you can specify a <code>revisionID</code> of <code>INITIAL</code> when you create a state machine using the <a>CreateStateMachine</a> API action.</p> </note>
            description: <p>An optional description of the state machine version.</p>

        Raises:
            capo_sfn.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for <a>DeleteStateMachineVersion</a>, <a>PublishStateMachineVersion</a>, or <a>UpdateStateMachine</a> with the <code>publish</code> parameter set to <code>true</code>.</p> <p>HTTP Status Code: 409</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p> <p>HTTP Status Code: 402</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist: <p>The specified state machine does not exist.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.publish_state_machine_version_input.PublishStateMachineVersionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.publish_state_machine_version_output.PublishStateMachineVersionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.publish_state_machine_version

            output, http_response = (
                capo_sfn._operations.aws_step_functions.publish_state_machine_version.publish_state_machine_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.publish_state_machine_version_input.PublishStateMachineVersionInput = {
            "state_machine_arn": state_machine_arn
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def redrive_execution(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        client_token: Optional["capo_sfn.types.client_token.ClientToken"] = None,
    ) -> "capo_sfn.types.redrive_execution_output.RedriveExecutionOutput":
        """<p>Restarts unsuccessful executions of Standard workflows that didn't complete successfully in the last 14 days. These include failed, aborted, or timed out executions. When you <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html">redrive</a> an execution, it continues the failed execution from the unsuccessful step and uses the same input. Step Functions preserves the results and execution history of the successful steps, and doesn't rerun these steps when you redrive an execution. Redriven executions use the same state machine definition and execution ARN as the original execution attempt.</p> <p>For workflows that include an <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html">Inline Map</a> or <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html">Parallel</a> state, <code>RedriveExecution</code> API action reschedules and redrives only the iterations and branches that failed or aborted.</p> <p>To redrive a workflow that includes a Distributed Map state whose Map Run failed, you must redrive the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/use-dist-map-orchestrate-large-scale-parallel-workloads.html#dist-map-orchestrate-parallel-workloads-key-terms">parent workflow</a>. The parent workflow redrives all the unsuccessful states, including a failed Map Run. If a Map Run was not started in the original execution attempt, the redriven parent workflow starts the Map Run.</p> <note> <p>This API action is not supported by <code>EXPRESS</code> state machines.</p> <p>However, you can restart the unsuccessful executions of Express child workflows in a Distributed Map by redriving its Map Run. When you redrive a Map Run, the Express child workflows are rerun using the <a>StartExecution</a> API action. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html">Redriving Map Runs</a>.</p> </note> <p>You can redrive executions if your original execution meets the following conditions:</p> <ul> <li> <p>The execution status isn't <code>SUCCEEDED</code>.</p> </li> <li> <p>Your workflow execution has not exceeded the redrivable period of 14 days. Redrivable period refers to the time during which you can redrive a given execution. This period starts from the day a state machine completes its execution.</p> </li> <li> <p>The workflow execution has not exceeded the maximum open time of one year. For more information about state machine quotas, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/limits-overview.html#service-limits-state-machine-executions">Quotas related to state machine executions</a>.</p> </li> <li> <p>The execution event history count is less than 24,999. Redriven executions append their event history to the existing event history. Make sure your workflow execution contains less than 24,999 events to accommodate the <code>ExecutionRedriven</code> history event and at least one other history event.</p> </li> </ul>

        Args:
            execution_arn: <p>The Amazon Resource Name (ARN) of the execution to be redriven.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The API will return idempotent responses for the last 10 client tokens used to successfully redrive the execution. These client tokens are valid for up to 15 minutes after they are first used.</p>

        Raises:
            capo_sfn.errors.execution_does_not_exist.ExecutionDoesNotExist: <p>The specified execution does not exist.</p>
            capo_sfn.errors.execution_limit_exceeded.ExecutionLimitExceeded: <p>The maximum number of running executions has been reached. Running executions must end or be stopped before a new execution can be started.</p>
            capo_sfn.errors.execution_not_redrivable.ExecutionNotRedrivable: <p>The execution Amazon Resource Name (ARN) that you specified for <code>executionArn</code> cannot be redriven.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.redrive_execution_input.RedriveExecutionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.redrive_execution_output.RedriveExecutionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.redrive_execution

            output, http_response = (
                capo_sfn._operations.aws_step_functions.redrive_execution.redrive_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.redrive_execution_input.RedriveExecutionInput = {
            "execution_arn": execution_arn
        }
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

    def send_task_failure(
        self,
        task_token: "capo_sfn.types.task_token.TaskToken",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        error: Optional["capo_sfn.types.sensitive_error.SensitiveError"] = None,
        cause: Optional["capo_sfn.types.sensitive_cause.SensitiveCause"] = None,
    ) -> "capo_sfn.types.send_task_failure_output.SendTaskFailureOutput":
        """<p>Used by activity workers, Task states using the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token">callback</a> pattern, and optionally Task states using the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync">job run</a> pattern to report that the task identified by the <code>taskToken</code> failed.</p> <p>For an execution with encryption enabled, Step Functions will encrypt the error and cause fields using the KMS key for the execution role.</p> <p>A caller can mark a task as fail without using any KMS permissions in the execution role if the caller provides a null value for both <code>error</code> and <code>cause</code> fields because no data needs to be encrypted.</p>

        Args:
            task_token: <p>The token that represents this task. Task tokens are generated by Step Functions when tasks are assigned to a worker, or in the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/input-output-contextobject.html">context object</a> when a workflow enters a task state. See <a>GetActivityTaskOutput$taskToken</a>.</p>
            error: <p>The error code of the failure.</p>
            cause: <p>A more detailed explanation of the cause of the failure.</p>

        Raises:
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.task_does_not_exist.TaskDoesNotExist: <p>The activity does not exist.</p>
            capo_sfn.errors.task_timed_out.TaskTimedOut: <p>The task token has either expired or the task associated with the token has already been closed.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.send_task_failure_input.SendTaskFailureInput]",
        ) -> OperationResponse[
            "capo_sfn.types.send_task_failure_output.SendTaskFailureOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.send_task_failure

            output, http_response = (
                capo_sfn._operations.aws_step_functions.send_task_failure.send_task_failure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.send_task_failure_input.SendTaskFailureInput = {
            "task_token": task_token
        }
        if error is not None:
            input_["error"] = error
        if cause is not None:
            input_["cause"] = cause

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_task_heartbeat(
        self,
        task_token: "capo_sfn.types.task_token.TaskToken",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.send_task_heartbeat_output.SendTaskHeartbeatOutput":
        """<p>Used by activity workers and Task states using the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token">callback</a> pattern, and optionally Task states using the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync">job run</a> pattern to report to Step Functions that the task represented by the specified <code>taskToken</code> is still making progress. This action resets the <code>Heartbeat</code> clock. The <code>Heartbeat</code> threshold is specified in the state machine's Amazon States Language definition (<code>HeartbeatSeconds</code>). This action does not in itself create an event in the execution history. However, if the task times out, the execution history contains an <code>ActivityTimedOut</code> entry for activities, or a <code>TaskTimedOut</code> entry for tasks using the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync">job run</a> or <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token">callback</a> pattern.</p> <note> <p>The <code>Timeout</code> of a task, defined in the state machine's Amazon States Language definition, is its maximum allowed duration, regardless of the number of <a>SendTaskHeartbeat</a> requests received. Use <code>HeartbeatSeconds</code> to configure the timeout interval for heartbeats.</p> </note>

        Args:
            task_token: <p>The token that represents this task. Task tokens are generated by Step Functions when tasks are assigned to a worker, or in the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/input-output-contextobject.html">context object</a> when a workflow enters a task state. See <a>GetActivityTaskOutput$taskToken</a>.</p>

        Raises:
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.task_does_not_exist.TaskDoesNotExist: <p>The activity does not exist.</p>
            capo_sfn.errors.task_timed_out.TaskTimedOut: <p>The task token has either expired or the task associated with the token has already been closed.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.send_task_heartbeat_input.SendTaskHeartbeatInput]",
        ) -> OperationResponse[
            "capo_sfn.types.send_task_heartbeat_output.SendTaskHeartbeatOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.send_task_heartbeat

            output, http_response = (
                capo_sfn._operations.aws_step_functions.send_task_heartbeat.send_task_heartbeat(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.send_task_heartbeat_input.SendTaskHeartbeatInput = {
            "task_token": task_token
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_task_success(
        self,
        task_token: "capo_sfn.types.task_token.TaskToken",
        output: "capo_sfn.types.sensitive_data.SensitiveData",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.send_task_success_output.SendTaskSuccessOutput":
        """<p>Used by activity workers, Task states using the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token">callback</a> pattern, and optionally Task states using the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync">job run</a> pattern to report that the task identified by the <code>taskToken</code> completed successfully.</p>

        Args:
            task_token: <p>The token that represents this task. Task tokens are generated by Step Functions when tasks are assigned to a worker, or in the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/input-output-contextobject.html">context object</a> when a workflow enters a task state. See <a>GetActivityTaskOutput$taskToken</a>.</p>
            output: <p>The JSON output of the task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>

        Raises:
            capo_sfn.errors.invalid_output.InvalidOutput: <p>The provided JSON output data is not valid.</p>
            capo_sfn.errors.invalid_token.InvalidToken: <p>The provided token is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.task_does_not_exist.TaskDoesNotExist: <p>The activity does not exist.</p>
            capo_sfn.errors.task_timed_out.TaskTimedOut: <p>The task token has either expired or the task associated with the token has already been closed.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.send_task_success_input.SendTaskSuccessInput]",
        ) -> OperationResponse[
            "capo_sfn.types.send_task_success_output.SendTaskSuccessOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.send_task_success

            output, http_response = (
                capo_sfn._operations.aws_step_functions.send_task_success.send_task_success(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.send_task_success_input.SendTaskSuccessInput = {
            "task_token": task_token,
            "output": output,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_execution(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        name: Optional["capo_sfn.types.name.Name"] = None,
        input: Optional["capo_sfn.types.sensitive_data.SensitiveData"] = None,
        trace_header: Optional["capo_sfn.types.trace_header.TraceHeader"] = None,
    ) -> "capo_sfn.types.start_execution_output.StartExecutionOutput":
        r"""<p>Starts a state machine execution.</p> <p>A qualified state machine ARN can either refer to a <i>Distributed Map state</i> defined within a state machine, a version ARN, or an alias ARN.</p> <p>The following are some examples of qualified and unqualified state machine ARNs:</p> <ul> <li> <p>The following qualified state machine ARN refers to a <i>Distributed Map state</i> with a label <code>mapStateLabel</code> in a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel</code> </p> <note> <p>If you provide a qualified state machine ARN that refers to a <i>Distributed Map state</i>, the request fails with <code>ValidationException</code>.</p> </note> </li> <li> <p>The following qualified state machine ARN refers to an alias named <code>PROD</code>.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD></code> </p> <note> <p>If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.</p> </note> </li> <li> <p>The following unqualified state machine ARN refers to a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine></code> </p> </li> </ul> <p>If you start an execution with an unqualified state machine ARN, Step Functions uses the latest revision of the state machine for the execution.</p> <p>To start executions of a state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>, call <code>StartExecution</code> and provide the version ARN or the ARN of an <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a> that points to the version.</p> <note> <p> <code>StartExecution</code> is idempotent for <code>STANDARD</code> workflows. For a <code>STANDARD</code> workflow, if you call <code>StartExecution</code> with the same name and input as a running execution, the call succeeds and return the same response as the original request. If the execution is closed or if the input is different, it returns a <code>400 ExecutionAlreadyExists</code> error. You can reuse the name 90 days after it closes. </p> <p> <code>StartExecution</code> isn't idempotent for <code>EXPRESS</code> workflows. </p> </note>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine to execute.</p> <p>The <code>stateMachineArn</code> parameter accepts one of the following inputs:</p> <ul> <li> <p> <b>An unqualified state machine ARN</b> – Refers to a state machine ARN that isn't qualified with a version or alias ARN. The following is an example of an unqualified state machine ARN.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine></code> </p> <p>Step Functions doesn't associate state machine executions that you start with an unqualified ARN with a version. This is true even if that version uses the same revision that the execution used.</p> </li> <li> <p> <b>A state machine version ARN</b> – Refers to a version ARN, which is a combination of state machine ARN and the version number separated by a colon (:). The following is an example of the ARN for version 10. </p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine>:10</code> </p> <p>Step Functions doesn't associate executions that you start with a version ARN with any aliases that point to that version.</p> </li> <li> <p> <b>A state machine alias ARN</b> – Refers to an alias ARN, which is a combination of state machine ARN and the alias name separated by a colon (:). The following is an example of the ARN for an alias named <code>PROD</code>.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD></code> </p> <p>Step Functions associates executions that you start with an alias ARN with that alias and the state machine version used for that execution.</p> </li> </ul>
            name: <p>Optional name of the execution. For STANDARD workflows, this name must be unique for your Amazon Web Services account, region, and state machine. If a previous execution with the same name exists, you can reuse the name 90 days after it closes. For EXPRESS workflows, execution names can be reused immediately. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/limits.html#service-limits-state-machine-executions"> Limits Related to State Machine Executions</a> in the <i>Step Functions Developer Guide</i>.</p> <p>If you don't provide a name for the execution, Step Functions automatically generates a universally unique identifier (UUID) as the execution name.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>
            input: <p>The string that contains the JSON input data for the execution, for example:</p> <p> <code>"{\"first_name\" : \"Alejandro\"}"</code> </p> <note> <p>If you don't include any JSON input data, you still must include the two braces, for example: <code>"{}"</code> </p> </note> <p>Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>
            trace_header: <p>Passes the X-Ray trace header. The trace header can also be passed in the request payload.</p> <note> <p> For X-Ray traces, all Amazon Web Services services use the <code>X-Amzn-Trace-Id</code> header from the HTTP request. Using the header is the preferred mechanism to identify a trace. <code>StartExecution</code> and <code>StartSyncExecution</code> API operations can also use <code>traceHeader</code> from the body of the request payload. If <b>both</b> sources are provided, Step Functions will use the <b>header value</b> (preferred) over the value in the request body. </p> </note>

        Raises:
            capo_sfn.errors.execution_already_exists.ExecutionAlreadyExists: <p>The execution has the same <code>name</code> as another execution (but a different <code>input</code>).</p> <note> <p>Executions with the same <code>name</code> and <code>input</code> are considered idempotent.</p> </note>
            capo_sfn.errors.execution_limit_exceeded.ExecutionLimitExceeded: <p>The maximum number of running executions has been reached. Running executions must end or be stopped before a new execution can be started.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_execution_input.InvalidExecutionInput: <p>The provided JSON input data is not valid.</p>
            capo_sfn.errors.invalid_name.InvalidName: <p>The provided name is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist: <p>The specified state machine does not exist.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.start_execution_input.StartExecutionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.start_execution_output.StartExecutionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.start_execution

            output, http_response = (
                capo_sfn._operations.aws_step_functions.start_execution.start_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.start_execution_input.StartExecutionInput = {
            "state_machine_arn": state_machine_arn
        }
        if name is not None:
            input_["name"] = name
        if input is not None:
            input_["input"] = input
        if trace_header is not None:
            input_["trace_header"] = trace_header

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_sync_execution(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        name: Optional["capo_sfn.types.name.Name"] = None,
        input: Optional["capo_sfn.types.sensitive_data.SensitiveData"] = None,
        trace_header: Optional["capo_sfn.types.trace_header.TraceHeader"] = None,
        included_data: Optional["capo_sfn.types.included_data.IncludedData"] = None,
    ) -> "capo_sfn.types.start_sync_execution_output.StartSyncExecutionOutput":
        r"""<p>Starts a Synchronous Express state machine execution. <code>StartSyncExecution</code> is not available for <code>STANDARD</code> workflows.</p> <note> <p> <code>StartSyncExecution</code> will return a <code>200 OK</code> response, even if your execution fails, because the status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your execution from running, such as permissions errors, limit errors, or issues with your state machine code and configuration. </p> </note>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine to execute.</p>
            name: <p>The name of the execution.</p>
            input: <p>The string that contains the JSON input data for the execution, for example:</p> <p> <code>"{\"first_name\" : \"Alejandro\"}"</code> </p> <note> <p>If you don't include any JSON input data, you still must include the two braces, for example: <code>"{}"</code> </p> </note> <p>Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>
            trace_header: <p>Passes the X-Ray trace header. The trace header can also be passed in the request payload.</p> <note> <p> For X-Ray traces, all Amazon Web Services services use the <code>X-Amzn-Trace-Id</code> header from the HTTP request. Using the header is the preferred mechanism to identify a trace. <code>StartExecution</code> and <code>StartSyncExecution</code> API operations can also use <code>traceHeader</code> from the body of the request payload. If <b>both</b> sources are provided, Step Functions will use the <b>header value</b> (preferred) over the value in the request body. </p> </note>
            included_data: <p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call the API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_execution_input.InvalidExecutionInput: <p>The provided JSON input data is not valid.</p>
            capo_sfn.errors.invalid_name.InvalidName: <p>The provided name is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist: <p>The specified state machine does not exist.</p>
            capo_sfn.errors.state_machine_type_not_supported.StateMachineTypeNotSupported: <p>State machine type is not supported.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.start_sync_execution_input.StartSyncExecutionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.start_sync_execution_output.StartSyncExecutionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.start_sync_execution

            output, http_response = (
                capo_sfn._operations.aws_step_functions.start_sync_execution.start_sync_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.start_sync_execution_input.StartSyncExecutionInput = {
            "state_machine_arn": state_machine_arn
        }
        if name is not None:
            input_["name"] = name
        if input is not None:
            input_["input"] = input
        if trace_header is not None:
            input_["trace_header"] = trace_header
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_execution(
        self,
        execution_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        error: Optional["capo_sfn.types.sensitive_error.SensitiveError"] = None,
        cause: Optional["capo_sfn.types.sensitive_cause.SensitiveCause"] = None,
    ) -> "capo_sfn.types.stop_execution_output.StopExecutionOutput":
        """<p>Stops an execution.</p> <p>This API action is not supported by <code>EXPRESS</code> state machines.</p> <p>For an execution with encryption enabled, Step Functions will encrypt the error and cause fields using the KMS key for the execution role.</p> <p>A caller can stop an execution without using any KMS permissions in the execution role if the caller provides a null value for both <code>error</code> and <code>cause</code> fields because no data needs to be encrypted.</p>

        Args:
            execution_arn: <p>The Amazon Resource Name (ARN) of the execution to stop.</p>
            error: <p>The error code of the failure.</p>
            cause: <p>A more detailed explanation of the cause of the failure.</p>

        Raises:
            capo_sfn.errors.execution_does_not_exist.ExecutionDoesNotExist: <p>The specified execution does not exist.</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException: <p>The KMS key is not in valid state, for example: Disabled or Deleted.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.stop_execution_input.StopExecutionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.stop_execution_output.StopExecutionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.stop_execution

            output, http_response = (
                capo_sfn._operations.aws_step_functions.stop_execution.stop_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.stop_execution_input.StopExecutionInput = {
            "execution_arn": execution_arn
        }
        if error is not None:
            input_["error"] = error
        if cause is not None:
            input_["cause"] = cause

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_sfn.types.arn.Arn",
        tags: "capo_sfn.types.tag_list.TagList",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.tag_resource_output.TagResourceOutput":
        """<p>Add a tag to a Step Functions resource.</p> <p>An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>, and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html">Controlling Access Using IAM Tags</a>.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the Step Functions state machine or activity.</p>
            tags: <p>The list of tags to add to a resource.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.too_many_tags.TooManyTags: <p>You've exceeded the number of tags allowed for a resource. See the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/limits.html"> Limits Topic</a> in the Step Functions Developer Guide.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse["capo_sfn.types.tag_resource_output.TagResourceOutput"]:
            import capo_sfn._operations.aws_step_functions.tag_resource

            output, http_response = (
                capo_sfn._operations.aws_step_functions.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_state(
        self,
        definition: "capo_sfn.types.definition.Definition",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        role_arn: Optional["capo_sfn.types.arn.Arn"] = None,
        input: Optional["capo_sfn.types.sensitive_data.SensitiveData"] = None,
        inspection_level: Optional[
            "capo_sfn.types.inspection_level.InspectionLevel"
        ] = None,
        reveal_secrets: Optional["capo_sfn.types.reveal_secrets.RevealSecrets"] = None,
        variables: Optional["capo_sfn.types.sensitive_data.SensitiveData"] = None,
        state_name: Optional[
            "capo_sfn.types.test_state_state_name.TestStateStateName"
        ] = None,
        mock: Optional["capo_sfn.types.mock_input.MockInput"] = None,
        context: Optional["capo_sfn.types.sensitive_data.SensitiveData"] = None,
        state_configuration: Optional[
            "capo_sfn.types.test_state_configuration.TestStateConfiguration"
        ] = None,
    ) -> "capo_sfn.types.test_state_output.TestStateOutput":
        """<p>Accepts the definition of a single state and executes it. You can test a state without creating a state machine or updating an existing state machine. Using this API, you can test the following:</p> <ul> <li> <p>A state's <a href="https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-input-output-dataflow">input and output processing</a> data flow</p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-services.html">Amazon Web Services service integration</a> request and response</p> </li> <li> <p>An <a href="https://docs.aws.amazon.com/step-functions/latest/dg/call-https-apis.html">HTTP Task</a> request and response</p> </li> </ul> <p>You can call this API on only one state at a time. The states that you can test include the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html#task-types">All Task types</a> except <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html">Activity</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-pass-state.html">Pass</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-wait-state.html">Wait</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-choice-state.html">Choice</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-succeed-state.html">Succeed</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-fail-state.html">Fail</a> </p> </li> </ul> <p>The <code>TestState</code> API assumes an IAM role which must contain the required IAM permissions for the resources your state is accessing. For information about the permissions a state might need, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions">IAM permissions to test a state</a>.</p> <p>The <code>TestState</code> API can run for up to five minutes. If the execution of a state exceeds this duration, it fails with the <code>States.Timeout</code> error.</p> <p> <code>TestState</code> only supports the following when a mock is specified: <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html">Activity tasks</a>, <code>.sync</code> or <code>.waitForTaskToken</code> <a href="https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html">service integration patterns</a>, <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html">Parallel</a>, or <a href="https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html">Map</a> states.</p>

        Args:
            definition: <p>The <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a> (ASL) definition of the state or state machine.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the execution role with the required IAM permissions for the state.</p>
            input: <p>A string that contains the JSON input data for the state.</p>
            inspection_level: <p>Determines the values to return when a state is tested. You can specify one of the following types:</p> <ul> <li> <p> <code>INFO</code>: Shows the final state output. By default, Step Functions sets <code>inspectionLevel</code> to <code>INFO</code> if you don't specify a level.</p> </li> <li> <p> <code>DEBUG</code>: Shows the final state output along with the input and output data processing result.</p> </li> <li> <p> <code>TRACE</code>: Shows the HTTP request and response for an HTTP Task. This level also shows the final state output along with the input and output data processing result.</p> </li> </ul> <p>Each of these levels also provide information about the status of the state execution and the next state to transition to.</p>
            reveal_secrets: <p>Specifies whether or not to include secret information in the test result. For HTTP Tasks, a secret includes the data that an EventBridge connection adds to modify the HTTP request headers, query parameters, and body. Step Functions doesn't omit any information included in the state definition or the HTTP response.</p> <p>If you set <code>revealSecrets</code> to <code>true</code>, you must make sure that the IAM user that calls the <code>TestState</code> API has permission for the <code>states:RevealSecrets</code> action. For an example of IAM policy that sets the <code>states:RevealSecrets</code> permission, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions">IAM permissions to test a state</a>. Without this permission, Step Functions throws an access denied error.</p> <p>By default, <code>revealSecrets</code> is set to <code>false</code>.</p>
            variables: <p>JSON object literal that sets variables used in the state under test. Object keys are the variable names and values are the variable values.</p>
            state_name: <p>Denotes the particular state within a state machine definition to be tested. If this field is specified, the <code>definition</code> must contain a fully-formed state machine definition.</p>
            mock: <p>Defines a mocked result or error for the state under test.</p> <p>A mock can only be specified for Task, Map, or Parallel states. If it is specified for another state type, an exception will be thrown.</p>
            context: <p>A JSON string representing a valid Context object for the state under test. This field may only be specified if a mock is specified in the same request.</p>
            state_configuration: <p>Contains configurations for the state under test.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_definition.InvalidDefinition: <p>The provided Amazon States Language definition is not valid.</p>
            capo_sfn.errors.invalid_execution_input.InvalidExecutionInput: <p>The provided JSON input data is not valid.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.test_state_input.TestStateInput]",
        ) -> OperationResponse["capo_sfn.types.test_state_output.TestStateOutput"]:
            import capo_sfn._operations.aws_step_functions.test_state

            output, http_response = (
                capo_sfn._operations.aws_step_functions.test_state.test_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.test_state_input.TestStateInput = {
            "definition": definition
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if input is not None:
            input_["input"] = input
        if inspection_level is not None:
            input_["inspection_level"] = inspection_level
        if reveal_secrets is not None:
            input_["reveal_secrets"] = reveal_secrets
        if variables is not None:
            input_["variables"] = variables
        if state_name is not None:
            input_["state_name"] = state_name
        if mock is not None:
            input_["mock"] = mock
        if context is not None:
            input_["context"] = context
        if state_configuration is not None:
            input_["state_configuration"] = state_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_sfn.types.arn.Arn",
        tag_keys: "capo_sfn.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
    ) -> "capo_sfn.types.untag_resource_output.UntagResourceOutput":
        """<p>Remove a tag from a Step Functions resource</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the Step Functions state machine or activity.</p>
            tag_keys: <p>The list of tags to remove from the resource.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_sfn.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.untag_resource

            output, http_response = (
                capo_sfn._operations.aws_step_functions.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_map_run(
        self,
        map_run_arn: "capo_sfn.types.long_arn.LongArn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        max_concurrency: Optional[
            "capo_sfn.types.max_concurrency.MaxConcurrency"
        ] = None,
        tolerated_failure_percentage: Optional[
            "capo_sfn.types.tolerated_failure_percentage.ToleratedFailurePercentage"
        ] = None,
        tolerated_failure_count: Optional[
            "capo_sfn.types.tolerated_failure_count.ToleratedFailureCount"
        ] = None,
    ) -> "capo_sfn.types.update_map_run_output.UpdateMapRunOutput":
        """<p>Updates an in-progress Map Run's configuration to include changes to the settings that control maximum concurrency and Map Run failure.</p>

        Args:
            map_run_arn: <p>The Amazon Resource Name (ARN) of a Map Run.</p>
            max_concurrency: <p>The maximum number of child workflow executions that can be specified to run in parallel for the Map Run at the same time.</p>
            tolerated_failure_percentage: <p>The maximum percentage of failed items before the Map Run fails.</p>
            tolerated_failure_count: <p>The maximum number of failed items before the Map Run fails.</p>

        Raises:
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.update_map_run_input.UpdateMapRunInput]",
        ) -> OperationResponse[
            "capo_sfn.types.update_map_run_output.UpdateMapRunOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.update_map_run

            output, http_response = (
                capo_sfn._operations.aws_step_functions.update_map_run.update_map_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.update_map_run_input.UpdateMapRunInput = {
            "map_run_arn": map_run_arn
        }
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if tolerated_failure_percentage is not None:
            input_["tolerated_failure_percentage"] = tolerated_failure_percentage
        if tolerated_failure_count is not None:
            input_["tolerated_failure_count"] = tolerated_failure_count

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_state_machine(
        self,
        state_machine_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        definition: Optional["capo_sfn.types.definition.Definition"] = None,
        role_arn: Optional["capo_sfn.types.arn.Arn"] = None,
        logging_configuration: Optional[
            "capo_sfn.types.logging_configuration.LoggingConfiguration"
        ] = None,
        tracing_configuration: Optional[
            "capo_sfn.types.tracing_configuration.TracingConfiguration"
        ] = None,
        publish: Optional["capo_sfn.types.publish.Publish"] = None,
        version_description: Optional[
            "capo_sfn.types.version_description.VersionDescription"
        ] = None,
        encryption_configuration: Optional[
            "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_sfn.types.update_state_machine_output.UpdateStateMachineOutput":
        """<p>Updates an existing state machine by modifying its <code>definition</code>, <code>roleArn</code>, <code>loggingConfiguration</code>, or <code>EncryptionConfiguration</code>. Running executions will continue to use the previous <code>definition</code> and <code>roleArn</code>. You must include at least one of <code>definition</code> or <code>roleArn</code> or you will receive a <code>MissingRequiredParameter</code> error.</p> <p>A qualified state machine ARN refers to a <i>Distributed Map state</i> defined within a state machine. For example, the qualified state machine ARN <code>arn:partition:states:region:account-id:stateMachine:stateMachineName/mapStateLabel</code> refers to a <i>Distributed Map state</i> with a label <code>mapStateLabel</code> in the state machine named <code>stateMachineName</code>.</p> <p>A qualified state machine ARN can either refer to a <i>Distributed Map state</i> defined within a state machine, a version ARN, or an alias ARN.</p> <p>The following are some examples of qualified and unqualified state machine ARNs:</p> <ul> <li> <p>The following qualified state machine ARN refers to a <i>Distributed Map state</i> with a label <code>mapStateLabel</code> in a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:partition:states:region:account-id:stateMachine:myStateMachine/mapStateLabel</code> </p> <note> <p>If you provide a qualified state machine ARN that refers to a <i>Distributed Map state</i>, the request fails with <code>ValidationException</code>.</p> </note> </li> <li> <p>The following qualified state machine ARN refers to an alias named <code>PROD</code>.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine:PROD></code> </p> <note> <p>If you provide a qualified state machine ARN that refers to a version ARN or an alias ARN, the request starts execution for that version or alias.</p> </note> </li> <li> <p>The following unqualified state machine ARN refers to a state machine named <code>myStateMachine</code>.</p> <p> <code>arn:<partition>:states:<region>:<account-id>:stateMachine:<myStateMachine></code> </p> </li> </ul> <p>After you update your state machine, you can set the <code>publish</code> parameter to <code>true</code> in the same action to publish a new <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>. This way, you can opt-in to strict versioning of your state machine.</p> <note> <p>Step Functions assigns monotonically increasing integers for state machine versions, starting at version number 1.</p> </note> <note> <p>All <code>StartExecution</code> calls within a few seconds use the updated <code>definition</code> and <code>roleArn</code>. Executions started immediately after you call <code>UpdateStateMachine</code> may use the previous state machine <code>definition</code> and <code>roleArn</code>. </p> </note>

        Args:
            state_machine_arn: <p>The Amazon Resource Name (ARN) of the state machine.</p>
            definition: <p>The Amazon States Language definition of the state machine. See <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role of the state machine.</p>
            logging_configuration: <p>Use the <code>LoggingConfiguration</code> data type to set CloudWatch Logs options.</p>
            tracing_configuration: <p>Selects whether X-Ray tracing is enabled.</p>
            publish: <p>Specifies whether the state machine version is published. The default is <code>false</code>. To publish a version after updating the state machine, set <code>publish</code> to <code>true</code>.</p>
            version_description: <p>An optional description of the state machine version to publish.</p> <p>You can only specify the <code>versionDescription</code> parameter if you've set <code>publish</code> to <code>true</code>.</p>
            encryption_configuration: <p>Settings to configure server-side encryption. </p>

        Raises:
            capo_sfn.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for <a>DeleteStateMachineVersion</a>, <a>PublishStateMachineVersion</a>, or <a>UpdateStateMachine</a> with the <code>publish</code> parameter set to <code>true</code>.</p> <p>HTTP Status Code: 409</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.invalid_definition.InvalidDefinition: <p>The provided Amazon States Language definition is not valid.</p>
            capo_sfn.errors.invalid_encryption_configuration.InvalidEncryptionConfiguration: <p>Received when <code>encryptionConfiguration</code> is specified but various conditions exist which make the configuration invalid. For example, if <code>type</code> is set to <code>CUSTOMER_MANAGED_KMS_KEY</code>, but <code>kmsKeyId</code> is null, or <code>kmsDataKeyReusePeriodSeconds</code> is not between 60 and 900, or the KMS key is not symmetric or inactive.</p>
            capo_sfn.errors.invalid_logging_configuration.InvalidLoggingConfiguration: <p>Configuration is not valid.</p>
            capo_sfn.errors.invalid_tracing_configuration.InvalidTracingConfiguration: <p>Your <code>tracingConfiguration</code> key does not match, or <code>enabled</code> has not been set to <code>true</code> or <code>false</code>.</p>
            capo_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException: <p>Either your KMS key policy or API caller does not have the required permissions.</p>
            capo_sfn.errors.kms_throttling_exception.KmsThrottlingException: <p>Received when KMS returns <code>ThrottlingException</code> for a KMS call that Step Functions makes on behalf of the caller.</p>
            capo_sfn.errors.missing_required_parameter.MissingRequiredParameter: <p>Request is missing a required parameter. This error occurs if both <code>definition</code> and <code>roleArn</code> are not specified.</p>
            capo_sfn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p> <p>HTTP Status Code: 402</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist: <p>The specified state machine does not exist.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.update_state_machine_input.UpdateStateMachineInput]",
        ) -> OperationResponse[
            "capo_sfn.types.update_state_machine_output.UpdateStateMachineOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.update_state_machine

            output, http_response = (
                capo_sfn._operations.aws_step_functions.update_state_machine.update_state_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.update_state_machine_input.UpdateStateMachineInput = {
            "state_machine_arn": state_machine_arn
        }
        if definition is not None:
            input_["definition"] = definition
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if tracing_configuration is not None:
            input_["tracing_configuration"] = tracing_configuration
        if publish is not None:
            input_["publish"] = publish
        if version_description is not None:
            input_["version_description"] = version_description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_state_machine_alias(
        self,
        state_machine_alias_arn: "capo_sfn.types.arn.Arn",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        description: Optional[
            "capo_sfn.types.alias_description.AliasDescription"
        ] = None,
        routing_configuration: Optional[
            "capo_sfn.types.routing_configuration_list.RoutingConfigurationList"
        ] = None,
    ) -> (
        "capo_sfn.types.update_state_machine_alias_output.UpdateStateMachineAliasOutput"
    ):
        """<p>Updates the configuration of an existing state machine <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a> by modifying its <code>description</code> or <code>routingConfiguration</code>.</p> <p>You must specify at least one of the <code>description</code> or <code>routingConfiguration</code> parameters to update a state machine alias.</p> <note> <p> <code>UpdateStateMachineAlias</code> is an idempotent API. Step Functions bases the idempotency check on the <code>stateMachineAliasArn</code>, <code>description</code>, and <code>routingConfiguration</code> parameters. Requests with the same parameters return an idempotent response.</p> </note> <note> <p>This operation is eventually consistent. All <a>StartExecution</a> requests made within a few seconds use the latest alias configuration. Executions started immediately after calling <code>UpdateStateMachineAlias</code> may use the previous routing configuration.</p> </note> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a>CreateStateMachineAlias</a> </p> </li> <li> <p> <a>DescribeStateMachineAlias</a> </p> </li> <li> <p> <a>ListStateMachineAliases</a> </p> </li> <li> <p> <a>DeleteStateMachineAlias</a> </p> </li> </ul>

        Args:
            state_machine_alias_arn: <p>The Amazon Resource Name (ARN) of the state machine alias.</p>
            description: <p>A description of the state machine alias.</p>
            routing_configuration: <p>The routing configuration of the state machine alias.</p> <p>An array of <code>RoutingConfig</code> objects that specifies up to two state machine versions that the alias starts executions for.</p>

        Raises:
            capo_sfn.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state. This error occurs when there're concurrent requests for <a>DeleteStateMachineVersion</a>, <a>PublishStateMachineVersion</a>, or <a>UpdateStateMachine</a> with the <code>publish</code> parameter set to <code>true</code>.</p> <p>HTTP Status Code: 409</p>
            capo_sfn.errors.invalid_arn.InvalidArn: <p>The provided Amazon Resource Name (ARN) is not valid.</p>
            capo_sfn.errors.resource_not_found.ResourceNotFound: <p>Could not find the referenced resource.</p>
            capo_sfn.errors.state_machine_deleting.StateMachineDeleting: <p>The specified state machine is being deleted.</p>
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.update_state_machine_alias_input.UpdateStateMachineAliasInput]",
        ) -> OperationResponse[
            "capo_sfn.types.update_state_machine_alias_output.UpdateStateMachineAliasOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.update_state_machine_alias

            output, http_response = (
                capo_sfn._operations.aws_step_functions.update_state_machine_alias.update_state_machine_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.update_state_machine_alias_input.UpdateStateMachineAliasInput = {
            "state_machine_alias_arn": state_machine_alias_arn
        }
        if description is not None:
            input_["description"] = description
        if routing_configuration is not None:
            input_["routing_configuration"] = routing_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_state_machine_definition(
        self,
        definition: "capo_sfn.types.definition.Definition",
        *,
        config_overrides: Optional[SFNClientConfig] = None,
        type: Optional["capo_sfn.types.state_machine_type.StateMachineType"] = None,
        severity: Optional[
            "capo_sfn.types.validate_state_machine_definition_severity.ValidateStateMachineDefinitionSeverity"
        ] = None,
        max_results: Optional[
            "capo_sfn.types.validate_state_machine_definition_max_result.ValidateStateMachineDefinitionMaxResult"
        ] = None,
    ) -> "capo_sfn.types.validate_state_machine_definition_output.ValidateStateMachineDefinitionOutput":
        """<p>Validates the syntax of a state machine definition specified in <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a> (ASL), a JSON-based, structured language.</p> <p>You can validate that a state machine definition is correct without creating a state machine resource.</p> <p>Suggested uses for <code>ValidateStateMachineDefinition</code>:</p> <ul> <li> <p>Integrate automated checks into your code review or Continuous Integration (CI) process to check state machine definitions before starting deployments.</p> </li> <li> <p>Run validation from a Git pre-commit hook to verify the definition before committing to your source repository.</p> </li> </ul> <p>Validation will look for problems in your state machine definition and return a <b>result</b> and a list of <b>diagnostic elements</b>.</p> <p>The <b>result</b> value will be <code>OK</code> when your workflow definition can be successfully created or updated. Note the result can be <code>OK</code> even when diagnostic warnings are present in the response. The <b>result</b> value will be <code>FAIL</code> when the workflow definition contains errors that would prevent you from creating or updating your state machine. </p> <p>The list of <a href="https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinitionDiagnostic.html">ValidateStateMachineDefinitionDiagnostic</a> data elements can contain zero or more <b>WARNING</b> and/or <b>ERROR</b> elements.</p> <note> <p>The <b>ValidateStateMachineDefinition API</b> might add new diagnostics in the future, adjust diagnostic codes, or change the message wording. Your automated processes should only rely on the value of the <b>result</b> field value (OK, FAIL). Do <b>not</b> rely on the exact order, count, or wording of diagnostic messages.</p> </note>

        Args:
            definition: <p>The Amazon States Language definition of the state machine. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a> (ASL).</p>
            type: <p>The target type of state machine for this definition. The default is <code>STANDARD</code>.</p>
            severity: <p>Minimum level of diagnostics to return. <code>ERROR</code> returns only <code>ERROR</code> diagnostics, whereas <code>WARNING</code> returns both <code>WARNING</code> and <code>ERROR</code> diagnostics. The default is <code>ERROR</code>. </p>
            max_results: <p>The maximum number of diagnostics that are returned per call. The default and maximum value is 100. Setting the value to 0 will also use the default of 100.</p> <p>If the number of diagnostics returned in the response exceeds <code>maxResults</code>, the value of the <code>truncated</code> field in the response will be set to <code>true</code>.</p>

        Raises:
            capo_sfn.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sfn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sfn.types.validate_state_machine_definition_input.ValidateStateMachineDefinitionInput]",
        ) -> OperationResponse[
            "capo_sfn.types.validate_state_machine_definition_output.ValidateStateMachineDefinitionOutput"
        ]:
            import capo_sfn._operations.aws_step_functions.validate_state_machine_definition

            output, http_response = (
                capo_sfn._operations.aws_step_functions.validate_state_machine_definition.validate_state_machine_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sfn.types.validate_state_machine_definition_input.ValidateStateMachineDefinitionInput = {
            "definition": definition
        }
        if type is not None:
            input_["type"] = type
        if severity is not None:
            input_["severity"] = severity
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
