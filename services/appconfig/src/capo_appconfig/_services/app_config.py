"""Generated from Smithy shape ``com.amazonaws.appconfig#AmazonAppConfig``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_appconfig._auth._signers
import capo_appconfig._auth._sigv4
from capo_appconfig._auth._identity import Credentials
from capo_appconfig._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_appconfig._auth._zapros_handler import AuthMiddleware
from capo_appconfig._pagination import resolve_path as _resolve_path
from capo_appconfig._services._aws_config import aws_config
from capo_appconfig._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_appconfig.types.account_settings
    import capo_appconfig.types.actions_map
    import capo_appconfig.types.application
    import capo_appconfig.types.applications
    import capo_appconfig.types.arn
    import capo_appconfig.types.blob
    import capo_appconfig.types.boolean
    import capo_appconfig.types.configuration
    import capo_appconfig.types.configuration_profile
    import capo_appconfig.types.configuration_profile_summary
    import capo_appconfig.types.configuration_profile_type
    import capo_appconfig.types.configuration_profiles
    import capo_appconfig.types.create_application_request
    import capo_appconfig.types.create_configuration_profile_request
    import capo_appconfig.types.create_deployment_strategy_request
    import capo_appconfig.types.create_environment_request
    import capo_appconfig.types.create_experiment_definition_request
    import capo_appconfig.types.create_extension_association_request
    import capo_appconfig.types.create_extension_request
    import capo_appconfig.types.create_hosted_configuration_version_request
    import capo_appconfig.types.delete_application_request
    import capo_appconfig.types.delete_configuration_profile_request
    import capo_appconfig.types.delete_deployment_strategy_request
    import capo_appconfig.types.delete_environment_request
    import capo_appconfig.types.delete_experiment_definition_request
    import capo_appconfig.types.delete_extension_association_request
    import capo_appconfig.types.delete_extension_request
    import capo_appconfig.types.delete_hosted_configuration_version_request
    import capo_appconfig.types.delete_type
    import capo_appconfig.types.deletion_protection_check
    import capo_appconfig.types.deletion_protection_settings
    import capo_appconfig.types.deployment
    import capo_appconfig.types.deployment_parameters
    import capo_appconfig.types.deployment_strategies
    import capo_appconfig.types.deployment_strategy
    import capo_appconfig.types.deployment_strategy_id
    import capo_appconfig.types.deployment_summary
    import capo_appconfig.types.deployments
    import capo_appconfig.types.description
    import capo_appconfig.types.dynamic_parameter_map
    import capo_appconfig.types.environment
    import capo_appconfig.types.environments
    import capo_appconfig.types.experiment_definition
    import capo_appconfig.types.experiment_definition_status
    import capo_appconfig.types.experiment_definition_summary
    import capo_appconfig.types.experiment_definitions
    import capo_appconfig.types.experiment_run
    import capo_appconfig.types.experiment_run_event
    import capo_appconfig.types.experiment_run_events
    import capo_appconfig.types.experiment_run_result
    import capo_appconfig.types.experiment_run_status
    import capo_appconfig.types.experiment_run_summary
    import capo_appconfig.types.experiment_runs
    import capo_appconfig.types.extension
    import capo_appconfig.types.extension_association
    import capo_appconfig.types.extension_association_summary
    import capo_appconfig.types.extension_associations
    import capo_appconfig.types.extension_or_parameter_name
    import capo_appconfig.types.extension_summary
    import capo_appconfig.types.extensions
    import capo_appconfig.types.flag_key
    import capo_appconfig.types.get_application_request
    import capo_appconfig.types.get_configuration_profile_request
    import capo_appconfig.types.get_configuration_request
    import capo_appconfig.types.get_deployment_request
    import capo_appconfig.types.get_deployment_strategy_request
    import capo_appconfig.types.get_environment_request
    import capo_appconfig.types.get_experiment_definition_request
    import capo_appconfig.types.get_experiment_run_request
    import capo_appconfig.types.get_extension_association_request
    import capo_appconfig.types.get_extension_request
    import capo_appconfig.types.get_hosted_configuration_version_request
    import capo_appconfig.types.growth_factor
    import capo_appconfig.types.growth_type
    import capo_appconfig.types.hosted_configuration_version
    import capo_appconfig.types.hosted_configuration_version_summary
    import capo_appconfig.types.hosted_configuration_versions
    import capo_appconfig.types.id
    import capo_appconfig.types.identifier
    import capo_appconfig.types.integer
    import capo_appconfig.types.kms_key_identifier
    import capo_appconfig.types.kms_key_identifier_or_empty
    import capo_appconfig.types.list_applications_request
    import capo_appconfig.types.list_configuration_profiles_request
    import capo_appconfig.types.list_deployment_strategies_request
    import capo_appconfig.types.list_deployments_request
    import capo_appconfig.types.list_environments_request
    import capo_appconfig.types.list_experiment_definitions_request
    import capo_appconfig.types.list_experiment_run_events_request
    import capo_appconfig.types.list_experiment_runs_request
    import capo_appconfig.types.list_extension_associations_request
    import capo_appconfig.types.list_extensions_request
    import capo_appconfig.types.list_hosted_configuration_versions_request
    import capo_appconfig.types.list_tags_for_resource_request
    import capo_appconfig.types.long_name
    import capo_appconfig.types.max_results
    import capo_appconfig.types.minutes_between0_and24_hours
    import capo_appconfig.types.monitor_list
    import capo_appconfig.types.name
    import capo_appconfig.types.name_with_reserved_aws_prefix
    import capo_appconfig.types.next_token
    import capo_appconfig.types.nullable_percentage
    import capo_appconfig.types.parameter_map
    import capo_appconfig.types.parameter_value_map
    import capo_appconfig.types.positive_integer
    import capo_appconfig.types.query_name
    import capo_appconfig.types.replicate_to
    import capo_appconfig.types.resource_tags
    import capo_appconfig.types.role_arn
    import capo_appconfig.types.rule
    import capo_appconfig.types.start_deployment_request
    import capo_appconfig.types.start_experiment_run_request
    import capo_appconfig.types.stop_deployment_request
    import capo_appconfig.types.stop_experiment_run_request
    import capo_appconfig.types.string_with_length_between1_and64
    import capo_appconfig.types.string_with_length_between1_and255
    import capo_appconfig.types.tag_key_list
    import capo_appconfig.types.tag_map
    import capo_appconfig.types.tag_resource_request
    import capo_appconfig.types.treatment_input
    import capo_appconfig.types.treatment_input_list
    import capo_appconfig.types.treatment_overrides
    import capo_appconfig.types.untag_resource_request
    import capo_appconfig.types.update_account_settings_request
    import capo_appconfig.types.update_application_request
    import capo_appconfig.types.update_configuration_profile_request
    import capo_appconfig.types.update_deployment_strategy_request
    import capo_appconfig.types.update_environment_request
    import capo_appconfig.types.update_experiment_definition_request
    import capo_appconfig.types.update_experiment_run_request
    import capo_appconfig.types.update_extension_association_request
    import capo_appconfig.types.update_extension_request
    import capo_appconfig.types.uri
    import capo_appconfig.types.validate_configuration_request
    import capo_appconfig.types.validator_list
    import capo_appconfig.types.vended_metrics_settings
    import capo_appconfig.types.version
    import capo_appconfig.types.version_label


class AppConfigClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AppConfigClient:
    """A client for the ``AppConfig`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AppConfigClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AppConfigClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AppConfigClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def create_application(
        self,
        name: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
    ) -> "capo_appconfig.types.application.Application":
        """<p>Creates an application. In AppConfig, an application is simply an organizational construct like a folder. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users.</p>

        Args:
            name: <p>A name for the application.</p>
            description: <p>A description of the application.</p>
            tags: <p>Metadata to assign to the application. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an application
            The following create-application example creates an application in AWS AppConfig.

            >>> client.create_application(name='example-application', description='An application used for creating an example.')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse["capo_appconfig.types.application.Application"]:
            import capo_appconfig._operations.amazon_app_config.create_application

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_application_request.CreateApplicationRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_configuration_profile(
        self,
        application_id: "capo_appconfig.types.name.Name",
        name: "capo_appconfig.types.long_name.LongName",
        location_uri: "capo_appconfig.types.uri.Uri",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        retrieval_role_arn: Optional["capo_appconfig.types.role_arn.RoleArn"] = None,
        validators: Optional[
            "capo_appconfig.types.validator_list.ValidatorList"
        ] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
        type: Optional[
            "capo_appconfig.types.configuration_profile_type.ConfigurationProfileType"
        ] = None,
        kms_key_identifier: Optional[
            "capo_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
    ) -> "capo_appconfig.types.configuration_profile.ConfigurationProfile":
        """<p>Creates a configuration profile, which is information that enables AppConfig to access the configuration source. Valid configuration sources include the following:</p> <ul> <li> <p>Configuration data in YAML, JSON, and other formats stored in the AppConfig hosted configuration store</p> </li> <li> <p>Configuration data stored as objects in an Amazon Simple Storage Service (Amazon S3) bucket</p> </li> <li> <p>Pipelines stored in CodePipeline</p> </li> <li> <p>Secrets stored in Secrets Manager</p> </li> <li> <p>Standard and secure string parameters stored in Amazon Web Services Systems Manager Parameter Store</p> </li> <li> <p>Configuration data in SSM documents stored in the Systems Manager document store</p> </li> </ul> <p>A configuration profile includes the following information:</p> <ul> <li> <p>The URI location of the configuration data.</p> </li> <li> <p>The Identity and Access Management (IAM) role that provides access to the configuration data.</p> </li> <li> <p>A validator for the configuration data. Available validators include either a JSON Schema or an Amazon Web Services Lambda function.</p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html">Create a Configuration and a Configuration Profile</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            application_id: <p>The application ID.</p>
            name: <p>A name for the configuration profile.</p>
            description: <p>A description of the configuration profile.</p>
            location_uri: <p>A URI to locate the configuration. You can specify the following:</p> <ul> <li> <p>For the AppConfig hosted configuration store and for feature flags, specify <code>hosted</code>.</p> </li> <li> <p>For an Amazon Web Services Systems Manager Parameter Store parameter, specify either the parameter name in the format <code>ssm-parameter://<parameter name></code> or the ARN.</p> </li> <li> <p>For an Amazon Web Services CodePipeline pipeline, specify the URI in the following format: <code>codepipeline</code>://<pipeline name>.</p> </li> <li> <p>For an Secrets Manager secret, specify the URI in the following format: <code>secretsmanager</code>://<secret name>.</p> </li> <li> <p>For an Amazon S3 object, specify the URI in the following format: <code>s3://<bucket>/<objectKey> </code>. Here is an example: <code>s3://amzn-s3-demo-bucket/my-app/us-east-1/my-config.json</code> </p> </li> <li> <p>For an SSM document, specify either the document name in the format <code>ssm-document://<document name></code> or the Amazon Resource Name (ARN).</p> </li> </ul>
            retrieval_role_arn: <p>The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.</p> <important> <p>A retrieval role ARN is not required for configurations stored in CodePipeline or the AppConfig hosted configuration store. It is required for all other sources that store your configuration. </p> </important>
            validators: <p>A list of methods for validating the configuration.</p>
            tags: <p>Metadata to assign to the configuration profile. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>
            type: <p>The type of configurations contained in the profile. AppConfig supports <code>feature flags</code> and <code>freeform</code> configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for <code>Type</code>:</p> <p> <code>AWS.AppConfig.FeatureFlags</code> </p> <p> <code>AWS.Freeform</code> </p>
            kms_key_identifier: <p>The identifier for an Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. The identifier can be an KMS key ID, alias, or the Amazon Resource Name (ARN) of the key ID or alias. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a configuration profile
            The following create-configuration-profile example creates a configuration profile using a configuration stored in Parameter Store, a capability of Systems Manager.

            >>> client.create_configuration_profile(application_id='339ohji', name='Example-Configuration-Profile', location_uri='ssm-parameter://Example-Parameter', retrieval_role_arn='arn:aws:iam::111122223333:role/Example-App-Config-Role')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_configuration_profile_request.CreateConfigurationProfileRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.configuration_profile.ConfigurationProfile"
        ]:
            import capo_appconfig._operations.amazon_app_config.create_configuration_profile

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_configuration_profile.create_configuration_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_configuration_profile_request.CreateConfigurationProfileRequest = {
            "application_id": application_id,
            "name": name,
            "location_uri": location_uri,
        }
        if description is not None:
            input_["description"] = description
        if retrieval_role_arn is not None:
            input_["retrieval_role_arn"] = retrieval_role_arn
        if validators is not None:
            input_["validators"] = validators
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment_strategy(
        self,
        name: "capo_appconfig.types.name.Name",
        deployment_duration_in_minutes: "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours",
        growth_factor: "capo_appconfig.types.growth_factor.GrowthFactor",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        final_bake_time_in_minutes: Optional[
            "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
        ] = None,
        growth_type: Optional["capo_appconfig.types.growth_type.GrowthType"] = None,
        replicate_to: Optional["capo_appconfig.types.replicate_to.ReplicateTo"] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
    ) -> "capo_appconfig.types.deployment_strategy.DeploymentStrategy":
        """<p>Creates a deployment strategy that defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.</p>

        Args:
            name: <p>A name for the deployment strategy.</p>
            description: <p>A description of the deployment strategy.</p>
            deployment_duration_in_minutes: <p>Total amount of time for a deployment to last.</p> <note> <p>AppConfig Agent supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html#appconfig-entity-based-gradual-deployments">Using AppConfig Agent for user-based or entity-based gradual deployments</a> </p> </note>
            final_bake_time_in_minutes: <p>Specifies the amount of time AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AppConfig rolls back the deployment. You must configure permissions for AppConfig to roll back based on CloudWatch alarms. For more information, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html">Configuring permissions for rollback based on Amazon CloudWatch alarms</a> in the <i>AppConfig User Guide</i>.</p>
            growth_factor: <p>The percentage of targets to receive a deployed configuration during each interval.</p>
            growth_type: <p>The algorithm used to define how percentage grows over time. AppConfig supports the following growth types:</p> <p> <b>Linear</b>: For this type, AppConfig processes the deployment by dividing the total number of targets by the value specified for <code>Step percentage</code>. For example, a linear deployment that uses a <code>Step percentage</code> of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.</p> <p> <b>Exponential</b>: For this type, AppConfig processes the deployment exponentially using the following formula: <code>G*(2^N)</code>. In this formula, <code>G</code> is the growth factor specified by the user and <code>N</code> is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:</p> <p> <code>2*(2^0)</code> </p> <p> <code>2*(2^1)</code> </p> <p> <code>2*(2^2)</code> </p> <p>Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.</p>
            replicate_to: <p>Save the deployment strategy to a Systems Manager (SSM) document.</p>
            tags: <p>Metadata to assign to the deployment strategy. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a deployment strategy
            The following create-deployment-strategy example creates a deployment strategy called Example-Deployment that takes 15 minutes and deploys the configuration to 25% of the application at a time. The strategy is also copied to an SSM Document.

            >>> client.create_deployment_strategy(name='Example-Deployment', deployment_duration_in_minutes=15, growth_factor=25, replicate_to='SSM_DOCUMENT')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_deployment_strategy_request.CreateDeploymentStrategyRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.deployment_strategy.DeploymentStrategy"
        ]:
            import capo_appconfig._operations.amazon_app_config.create_deployment_strategy

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_deployment_strategy.create_deployment_strategy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_deployment_strategy_request.CreateDeploymentStrategyRequest = {
            "name": name,
            "deployment_duration_in_minutes": deployment_duration_in_minutes,
            "growth_factor": growth_factor,
        }
        if description is not None:
            input_["description"] = description
        if final_bake_time_in_minutes is not None:
            input_["final_bake_time_in_minutes"] = final_bake_time_in_minutes
        if growth_type is not None:
            input_["growth_type"] = growth_type
        if replicate_to is not None:
            input_["replicate_to"] = replicate_to
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_environment(
        self,
        application_id: "capo_appconfig.types.name.Name",
        name: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        monitors: Optional["capo_appconfig.types.monitor_list.MonitorList"] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
    ) -> "capo_appconfig.types.environment.Environment":
        """<p>Creates an environment. For each application, you define one or more environments. An environment is a deployment group of AppConfig targets, such as applications in a <code>Beta</code> or <code>Production</code> environment. You can also define environments for application subcomponents such as the <code>Web</code>, <code>Mobile</code> and <code>Back-end</code> components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.</p>

        Args:
            application_id: <p>The application ID.</p>
            name: <p>A name for the environment.</p>
            description: <p>A description of the environment.</p>
            monitors: <p>Amazon CloudWatch alarms to monitor during the deployment process.</p>
            tags: <p>Metadata to assign to the environment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an environment
            The following create-environment example creates an AWS AppConfig environment named Example-Environment using the application you created using create-application

            >>> client.create_environment(application_id='339ohji', name='Example-Environment')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse["capo_appconfig.types.environment.Environment"]:
            import capo_appconfig._operations.amazon_app_config.create_environment

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_environment_request.CreateEnvironmentRequest = {
            "application_id": application_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if monitors is not None:
            input_["monitors"] = monitors
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_experiment_definition(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        name: "capo_appconfig.types.name_with_reserved_aws_prefix.NameWithReservedAwsPrefix",
        configuration_profile_identifier: "capo_appconfig.types.identifier.Identifier",
        environment_identifier: "capo_appconfig.types.identifier.Identifier",
        flag_key: "capo_appconfig.types.flag_key.FlagKey",
        treatments: "capo_appconfig.types.treatment_input_list.TreatmentInputList",
        control: "capo_appconfig.types.treatment_input.TreatmentInput",
        audience_rule: "capo_appconfig.types.rule.Rule",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        hypothesis: Optional["capo_appconfig.types.description.Description"] = None,
        audience_description: Optional[
            "capo_appconfig.types.description.Description"
        ] = None,
        launch_criteria: Optional[
            "capo_appconfig.types.description.Description"
        ] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
    ) -> "capo_appconfig.types.experiment_definition.ExperimentDefinition":
        """<p>Creates an experiment definition in AppConfig. An experiment definition describes the purpose, scope, and operational configuration of an experiment, including the target audience, feature flag, and treatment configurations.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            name: <p>A name for the experiment definition.</p>
            configuration_profile_identifier: <p>The configuration profile ID or name that stores the feature flag.</p>
            environment_identifier: <p>The environment ID or name where the experiment will run.</p>
            flag_key: <p>The key of the existing feature flag to use with the experiment.</p>
            treatments: <p>A list of treatments to evaluate during the experiment. Each treatment defines a distinct variation compared to the control.</p>
            control: <p>The control treatment that represents the baseline experience for comparison.</p>
            audience_rule: <p>A rule that defines which users are eligible to be assigned to treatments during the experiment.</p>
            hypothesis: <p>A description of the goal or hypothesis the experiment is designed to validate.</p>
            audience_description: <p>A description of the intended audience for the experiment.</p>
            launch_criteria: <p>Information about the conditions under which you would launch the winning treatment.</p>
            tags: <p>The tags to assign to the experiment definition. Tags help organize and categorize your AppConfig resources.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an experiment definition
            The following CreateExperimentDefinition example creates an experiment definition that tests a feature flag with a 50/50 traffic split.

            >>> client.create_experiment_definition(application_identifier='339ohji', configuration_profile_identifier='ur8hx2f', environment_identifier='54j1r29', name='Example-Experiment-Definition', flag_key='my-feature-flag', treatments=[{'Weight': 50, 'FlagValue': {'Enabled': True}}], control={'Weight': 50, 'FlagValue': {'Enabled': False}}, audience_rule='(eq $country "US")')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_experiment_definition_request.CreateExperimentDefinitionRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.experiment_definition.ExperimentDefinition"
        ]:
            import capo_appconfig._operations.amazon_app_config.create_experiment_definition

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_experiment_definition.create_experiment_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_experiment_definition_request.CreateExperimentDefinitionRequest = {
            "application_identifier": application_identifier,
            "name": name,
            "configuration_profile_identifier": configuration_profile_identifier,
            "environment_identifier": environment_identifier,
            "flag_key": flag_key,
            "treatments": treatments,
            "control": control,
            "audience_rule": audience_rule,
        }
        if hypothesis is not None:
            input_["hypothesis"] = hypothesis
        if audience_description is not None:
            input_["audience_description"] = audience_description
        if launch_criteria is not None:
            input_["launch_criteria"] = launch_criteria
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_extension(
        self,
        name: "capo_appconfig.types.extension_or_parameter_name.ExtensionOrParameterName",
        actions: "capo_appconfig.types.actions_map.ActionsMap",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        parameters: Optional["capo_appconfig.types.parameter_map.ParameterMap"] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
        latest_version_number: Optional["capo_appconfig.types.integer.Integer"] = None,
    ) -> "capo_appconfig.types.extension.Extension":
        """<p>Creates an AppConfig extension. An extension augments your ability to inject logic or behavior at different points during the AppConfig workflow of creating or deploying a configuration.</p> <p>You can create your own extensions or use the Amazon Web Services authored extensions provided by AppConfig. For an AppConfig extension that uses Lambda, you must create a Lambda function to perform any computation and processing defined in the extension. If you plan to create custom versions of the Amazon Web Services authored notification extensions, you only need to specify an Amazon Resource Name (ARN) in the <code>Uri</code> field for the new extension version.</p> <ul> <li> <p>For a custom EventBridge notification extension, enter the ARN of the EventBridge default events in the <code>Uri</code> field.</p> </li> <li> <p>For a custom Amazon SNS notification extension, enter the ARN of an Amazon SNS topic in the <code>Uri</code> field.</p> </li> <li> <p>For a custom Amazon SQS notification extension, enter the ARN of an Amazon SQS message queue in the <code>Uri</code> field. </p> </li> </ul> <p>For more information about extensions, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">Extending workflows</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            name: <p>A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.</p>
            description: <p>Information about the extension.</p>
            actions: <p>The actions defined in the extension.</p>
            parameters: <p>The parameters accepted by the extension. You specify parameter values when you associate the extension to an AppConfig resource by using the <code>CreateExtensionAssociation</code> API action. For Lambda extension actions, these parameters are included in the Lambda request object.</p>
            tags: <p>Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. </p>
            latest_version_number: <p>You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_extension_request.CreateExtensionRequest]",
        ) -> OperationResponse["capo_appconfig.types.extension.Extension"]:
            import capo_appconfig._operations.amazon_app_config.create_extension

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_extension.create_extension(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_extension_request.CreateExtensionRequest = {
            "name": name,
            "actions": actions,
        }
        if description is not None:
            input_["description"] = description
        if parameters is not None:
            input_["parameters"] = parameters
        if tags is not None:
            input_["tags"] = tags
        if latest_version_number is not None:
            input_["latest_version_number"] = latest_version_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_extension_association(
        self,
        extension_identifier: "capo_appconfig.types.identifier.Identifier",
        resource_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        extension_version_number: Optional[
            "capo_appconfig.types.integer.Integer"
        ] = None,
        parameters: Optional[
            "capo_appconfig.types.parameter_value_map.ParameterValueMap"
        ] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
    ) -> "capo_appconfig.types.extension_association.ExtensionAssociation":
        """<p>When you create an extension or configure an Amazon Web Services authored extension, you associate the extension with an AppConfig application, environment, or configuration profile. For example, you can choose to run the <code>AppConfig deployment events to Amazon SNS</code> Amazon Web Services authored extension and receive notifications on an Amazon SNS topic anytime a configuration deployment is started for a specific application. Defining which extension to associate with an AppConfig resource is called an <i>extension association</i>. An extension association is a specified relationship between an extension and an AppConfig resource, such as an application or a configuration profile. For more information about extensions and associations, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">Extending workflows</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            extension_identifier: <p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>
            extension_version_number: <p>The version number of the extension. If not specified, AppConfig uses the maximum version of the extension.</p>
            resource_identifier: <p>The ARN of an application, configuration profile, or environment.</p>
            parameters: <p>The parameter names and values defined in the extensions. Extension parameters marked <code>Required</code> must be entered for this field.</p>
            tags: <p>Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. </p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_extension_association_request.CreateExtensionAssociationRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.extension_association.ExtensionAssociation"
        ]:
            import capo_appconfig._operations.amazon_app_config.create_extension_association

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_extension_association.create_extension_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_extension_association_request.CreateExtensionAssociationRequest = {
            "extension_identifier": extension_identifier,
            "resource_identifier": resource_identifier,
        }
        if extension_version_number is not None:
            input_["extension_version_number"] = extension_version_number
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

    def create_hosted_configuration_version(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        content: "capo_appconfig.types.blob.Blob",
        content_type: "capo_appconfig.types.string_with_length_between1_and255.StringWithLengthBetween1And255",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        latest_version_number: Optional["capo_appconfig.types.integer.Integer"] = None,
        version_label: Optional[
            "capo_appconfig.types.version_label.VersionLabel"
        ] = None,
    ) -> "capo_appconfig.types.hosted_configuration_version.HostedConfigurationVersion":
        """<p>Creates a new configuration in the AppConfig hosted configuration store. If you're creating a feature flag, we recommend you familiarize yourself with the JSON schema for feature flag data. For more information, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-type-reference-feature-flags.html">Type reference for AWS.AppConfig.FeatureFlags</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            application_id: <p>The application ID.</p>
            configuration_profile_id: <p>The configuration profile ID.</p>
            description: <p>A description of the configuration.</p> <note> <p>Due to HTTP limitations, this field only supports ASCII characters.</p> </note>
            content: <p>The configuration data, as bytes.</p> <note> <p>AppConfig accepts any type of data, including text formats like JSON or TOML, or binary formats like protocol buffers or compressed data.</p> </note>
            content_type: <p>A standard MIME type describing the format of the configuration content. For more information, see <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17">Content-Type</a>.</p>
            latest_version_number: <p>An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.</p>
            version_label: <p>An optional, user-defined label for the AppConfig hosted configuration version. This value must contain at least one non-numeric character. For example, "v2.2.0".</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.payload_too_large_exception.PayloadTooLargeException: <p>The configuration size is too large.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one more AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:</p> <p>Applications: 100 max</p> <p>To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig">Service quotas for AppConfig</a> in the Amazon Web Services General Reference.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a hosted configuration version
            The following create-hosted-configuration-version example creates a new configuration in the AWS AppConfig configuration store.

            >>> client.create_hosted_configuration_version(application_id='339ohji', configuration_profile_id='ur8hx2f', content='eyAiTmFtZSI6ICJFeGFtcGxlQXBwbGljYXRpb24iLCAiSWQiOiBFeGFtcGxlSUQsICJSYW5rIjogNyB9', content_type='text', latest_version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.create_hosted_configuration_version_request.CreateHostedConfigurationVersionRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.hosted_configuration_version.HostedConfigurationVersion"
        ]:
            import capo_appconfig._operations.amazon_app_config.create_hosted_configuration_version

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.create_hosted_configuration_version.create_hosted_configuration_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.create_hosted_configuration_version_request.CreateHostedConfigurationVersionRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "content": content,
            "content_type": content_type,
        }
        if description is not None:
            input_["description"] = description
        if latest_version_number is not None:
            input_["latest_version_number"] = latest_version_number
        if version_label is not None:
            input_["version_label"] = version_label

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> None:
        """<p>Deletes an application.</p>

        Args:
            application_id: <p>The ID of the application to delete.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an application
            The following delete-application example deletes the specified application.


            >>> client.delete_application(application_id='339ohji')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_application

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_configuration_profile(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        deletion_protection_check: Optional[
            "capo_appconfig.types.deletion_protection_check.DeletionProtectionCheck"
        ] = None,
    ) -> None:
        """<p>Deletes a configuration profile.</p> <p>To prevent users from unintentionally deleting actively-used configuration profiles, enable <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/deletion-protection.html">deletion protection</a>.</p>

        Args:
            application_id: <p>The application ID that includes the configuration profile you want to delete.</p>
            configuration_profile_id: <p>The ID of the configuration profile you want to delete.</p>
            deletion_protection_check: <p>A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile if your application has called either <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html">GetLatestConfiguration</a> or for the configuration profile during the specified interval. </p> <p>This parameter supports the following values:</p> <ul> <li> <p> <code>BYPASS</code>: Instructs AppConfig to bypass the deletion protection check and delete a configuration profile even if deletion protection would have otherwise prevented it.</p> </li> <li> <p> <code>APPLY</code>: Instructs the deletion protection check to run, even if deletion protection is disabled at the account level. <code>APPLY</code> also forces the deletion protection check to run against resources created in the past hour, which are normally excluded from deletion protection checks. </p> </li> <li> <p> <code>ACCOUNT_DEFAULT</code>: The default setting, which instructs AppConfig to implement the deletion protection value specified in the <code>UpdateAccountSettings</code> API.</p> </li> </ul>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a configuration profile
            The following delete-configuration-profile example deletes the specified configuration profile.

            >>> client.delete_configuration_profile(application_id='339ohji', configuration_profile_id='ur8hx2f')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_configuration_profile_request.DeleteConfigurationProfileRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_configuration_profile

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_configuration_profile.delete_configuration_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_configuration_profile_request.DeleteConfigurationProfileRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
        }
        if deletion_protection_check is not None:
            input_["deletion_protection_check"] = deletion_protection_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_deployment_strategy(
        self,
        deployment_strategy_id: "capo_appconfig.types.deployment_strategy_id.DeploymentStrategyId",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> None:
        """<p>Deletes a deployment strategy.</p>

        Args:
            deployment_strategy_id: <p>The ID of the deployment strategy you want to delete.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a deployment strategy
            The following delete-deployment-strategy example deletes the specified deployment strategy.

            >>> client.delete_deployment_strategy(deployment_strategy_id='1225qzk')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_deployment_strategy_request.DeleteDeploymentStrategyRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_deployment_strategy

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_deployment_strategy.delete_deployment_strategy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_deployment_strategy_request.DeleteDeploymentStrategyRequest = {
            "deployment_strategy_id": deployment_strategy_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment(
        self,
        environment_id: "capo_appconfig.types.name.Name",
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        deletion_protection_check: Optional[
            "capo_appconfig.types.deletion_protection_check.DeletionProtectionCheck"
        ] = None,
    ) -> None:
        """<p>Deletes an environment.</p> <p>To prevent users from unintentionally deleting actively-used environments, enable <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/deletion-protection.html">deletion protection</a>.</p>

        Args:
            environment_id: <p>The ID of the environment that you want to delete.</p>
            application_id: <p>The application ID that includes the environment that you want to delete.</p>
            deletion_protection_check: <p>A parameter to configure deletion protection. Deletion protection prevents a user from deleting an environment if your application called either <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html">GetLatestConfiguration</a> or in the environment during the specified interval. </p> <p>This parameter supports the following values:</p> <ul> <li> <p> <code>BYPASS</code>: Instructs AppConfig to bypass the deletion protection check and delete a configuration profile even if deletion protection would have otherwise prevented it. </p> </li> <li> <p> <code>APPLY</code>: Instructs the deletion protection check to run, even if deletion protection is disabled at the account level. <code>APPLY</code> also forces the deletion protection check to run against resources created in the past hour, which are normally excluded from deletion protection checks.</p> </li> <li> <p> <code>ACCOUNT_DEFAULT</code>: The default setting, which instructs AppConfig to implement the deletion protection value specified in the <code>UpdateAccountSettings</code> API.</p> </li> </ul>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an environment
            The following delete-environment example deletes the specified application environment.

            >>> client.delete_environment(application_id='339ohji', environment_id='54j1r29')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_environment

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_environment_request.DeleteEnvironmentRequest = {
            "environment_id": environment_id,
            "application_id": application_id,
        }
        if deletion_protection_check is not None:
            input_["deletion_protection_check"] = deletion_protection_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_experiment_definition(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        delete_type: Optional["capo_appconfig.types.delete_type.DeleteType"] = None,
    ) -> None:
        """<p>Deletes an experiment definition. You can archive the definition to hide it from the active list while preserving it for future reference, or permanently delete it along with all associated run history.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            delete_type: <p>The type of deletion to perform. Valid values include archive (hide but preserve) and permanent (delete permanently).</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an experiment definition
            The following DeleteExperimentDefinition example archives (soft-deletes) the specified experiment definition.

            >>> client.delete_experiment_definition(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_experiment_definition_request.DeleteExperimentDefinitionRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_experiment_definition

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_experiment_definition.delete_experiment_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_experiment_definition_request.DeleteExperimentDefinitionRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
        }
        if delete_type is not None:
            input_["delete_type"] = delete_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_extension(
        self,
        extension_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        version_number: Optional["capo_appconfig.types.integer.Integer"] = None,
    ) -> None:
        """<p>Deletes an AppConfig extension. You must delete all associations to an extension before you delete the extension.</p>

        Args:
            extension_identifier: <p>The name, ID, or Amazon Resource Name (ARN) of the extension you want to delete.</p>
            version_number: <p>A specific version of an extension to delete. If omitted, the highest version is deleted.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_extension_request.DeleteExtensionRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_extension

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_extension.delete_extension(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_extension_request.DeleteExtensionRequest = {
            "extension_identifier": extension_identifier
        }
        if version_number is not None:
            input_["version_number"] = version_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_extension_association(
        self,
        extension_association_id: "capo_appconfig.types.id.Id",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> None:
        """<p>Deletes an extension association. This action doesn't delete extensions defined in the association.</p>

        Args:
            extension_association_id: <p>The ID of the extension association to delete.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_extension_association_request.DeleteExtensionAssociationRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_extension_association

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_extension_association.delete_extension_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_extension_association_request.DeleteExtensionAssociationRequest = {
            "extension_association_id": extension_association_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_hosted_configuration_version(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        version_number: "capo_appconfig.types.integer.Integer",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> None:
        """<p>Deletes a version of a configuration from the AppConfig hosted configuration store.</p>

        Args:
            application_id: <p>The application ID.</p>
            configuration_profile_id: <p>The configuration profile ID.</p>
            version_number: <p>The versions number to delete.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a hosted configuration version
            The following delete-hosted-configuration-version example deletes a configuration version hosted in the AWS AppConfig configuration store.

            >>> client.delete_hosted_configuration_version(application_id='339ohji', configuration_profile_id='ur8hx2f', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.delete_hosted_configuration_version_request.DeleteHostedConfigurationVersionRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.delete_hosted_configuration_version

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.delete_hosted_configuration_version.delete_hosted_configuration_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.delete_hosted_configuration_version_request.DeleteHostedConfigurationVersionRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_settings(
        self, *, config_overrides: Optional[AppConfigClientConfig] = None
    ) -> "capo_appconfig.types.account_settings.AccountSettings":
        """<p>Returns information about the status of the <code>DeletionProtection</code> parameter.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse["capo_appconfig.types.account_settings.AccountSettings"]:
            import capo_appconfig._operations.amazon_app_config.get_account_settings

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_account_settings.get_account_settings(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application(
        self,
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.application.Application":
        """<p>Retrieves information about an application.</p>

        Args:
            application_id: <p>The ID of the application you want to get.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list details of an application
            The following get-application example lists the details of the specified application.

            >>> client.get_application(application_id='339ohji')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse["capo_appconfig.types.application.Application"]:
            import capo_appconfig._operations.amazon_app_config.get_application

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_configuration(
        self,
        application: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64",
        environment: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64",
        configuration: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64",
        client_id: "capo_appconfig.types.string_with_length_between1_and64.StringWithLengthBetween1And64",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        client_configuration_version: Optional[
            "capo_appconfig.types.version.Version"
        ] = None,
    ) -> "capo_appconfig.types.configuration.Configuration":
        """<p>(Deprecated) Retrieves the latest deployed configuration.</p> <important> <p>Note the following important information.</p> <ul> <li> <p>This API action is deprecated. Calls to receive configuration data should use the <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html">StartConfigurationSession</a> and <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html">GetLatestConfiguration</a> APIs instead. </p> </li> <li> <p> <a>GetConfiguration</a> is a priced call. For more information, see <a href="https://aws.amazon.com/systems-manager/pricing/">Pricing</a>.</p> </li> </ul> </important>

        Args:
            application: <p>The application to get. Specify either the application name or the application ID.</p>
            environment: <p>The environment to get. Specify either the environment name or the environment ID.</p>
            configuration: <p>The configuration to get. Specify either the configuration name or the configuration ID.</p>
            client_id: <p>The clientId parameter in the following command is a unique, user-specified ID to identify the client for the configuration. This ID enables AppConfig to deploy the configuration in intervals, as defined in the deployment strategy. </p>
            client_configuration_version: <p>The configuration version returned in the most recent <a>GetConfiguration</a> response.</p> <important> <p>AppConfig uses the value of the <code>ClientConfigurationVersion</code> parameter to identify the configuration version on your clients. If you don’t send <code>ClientConfigurationVersion</code> with each call to <a>GetConfiguration</a>, your clients receive the current configuration. You are charged each time your clients receive a configuration.</p> <p>To avoid excess charges, we recommend you use the <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/StartConfigurationSession.html">StartConfigurationSession</a> and <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/GetLatestConfiguration.html">GetLatestConfiguration</a> APIs, which track the client configuration version on your behalf. If you choose to continue using <a>GetConfiguration</a>, we recommend that you include the <code>ClientConfigurationVersion</code> value with every call to <a>GetConfiguration</a>. The value to use for <code>ClientConfigurationVersion</code> comes from the <code>ConfigurationVersion</code> attribute returned by <a>GetConfiguration</a> when there is new or updated data, and should be saved for subsequent calls to <a>GetConfiguration</a>.</p> </important> <p>For more information about working with configurations, see <a href="http://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html">Retrieving feature flags and configuration data in AppConfig</a> in the <i>AppConfig User Guide</i>.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve configuration details
            The following get-configuration example returns the configuration details of the example application. On subsequent calls to get-configuration, use the client-configuration-version parameter to only update the configuration of your application if the version has changed. Only updating the configuration when the version has changed avoids excess charges incurred by calling get-configuration.

            >>> client.get_configuration(application='example-application', environment='Example-Environment', configuration='Example-Configuration-Profile', client_id='example-id')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_configuration_request.GetConfigurationRequest]",
        ) -> OperationResponse["capo_appconfig.types.configuration.Configuration"]:
            import capo_appconfig._operations.amazon_app_config.get_configuration

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_configuration.get_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_configuration_request.GetConfigurationRequest = {
            "application": application,
            "environment": environment,
            "configuration": configuration,
            "client_id": client_id,
        }
        if client_configuration_version is not None:
            input_["client_configuration_version"] = client_configuration_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_configuration_profile(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.configuration_profile.ConfigurationProfile":
        """<p>Retrieves information about a configuration profile.</p>

        Args:
            application_id: <p>The ID of the application that includes the configuration profile you want to get.</p>
            configuration_profile_id: <p>The ID of the configuration profile that you want to get.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve configuration profile details
            The following get-configuration-profile example returns the details of the specified configuration profile.

            >>> client.get_configuration_profile(application_id='339ohji', configuration_profile_id='ur8hx2f')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_configuration_profile_request.GetConfigurationProfileRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.configuration_profile.ConfigurationProfile"
        ]:
            import capo_appconfig._operations.amazon_app_config.get_configuration_profile

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_configuration_profile.get_configuration_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_configuration_profile_request.GetConfigurationProfileRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment(
        self,
        application_id: "capo_appconfig.types.name.Name",
        environment_id: "capo_appconfig.types.name.Name",
        deployment_number: "capo_appconfig.types.integer.Integer",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.deployment.Deployment":
        """<p>Retrieves information about a configuration deployment.</p>

        Args:
            application_id: <p>The ID of the application that includes the deployment you want to get. </p>
            environment_id: <p>The ID of the environment that includes the deployment you want to get. </p>
            deployment_number: <p>The sequence number of the deployment.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_deployment_request.GetDeploymentRequest]",
        ) -> OperationResponse["capo_appconfig.types.deployment.Deployment"]:
            import capo_appconfig._operations.amazon_app_config.get_deployment

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_deployment_request.GetDeploymentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
            "deployment_number": deployment_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment_strategy(
        self,
        deployment_strategy_id: "capo_appconfig.types.deployment_strategy_id.DeploymentStrategyId",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.deployment_strategy.DeploymentStrategy":
        """<p>Retrieves information about a deployment strategy. A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.</p>

        Args:
            deployment_strategy_id: <p>The ID of the deployment strategy to get.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve details of a deployment strategy
            The following get-deployment-strategy example lists the details of the specified deployment strategy.

            >>> client.get_deployment_strategy(deployment_strategy_id='1225qzk')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_deployment_strategy_request.GetDeploymentStrategyRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.deployment_strategy.DeploymentStrategy"
        ]:
            import capo_appconfig._operations.amazon_app_config.get_deployment_strategy

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_deployment_strategy.get_deployment_strategy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_deployment_strategy_request.GetDeploymentStrategyRequest = {
            "deployment_strategy_id": deployment_strategy_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_environment(
        self,
        application_id: "capo_appconfig.types.name.Name",
        environment_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.environment.Environment":
        """<p>Retrieves information about an environment. An environment is a deployment group of AppConfig applications, such as applications in a <code>Production</code> environment or in an <code>EU_Region</code> environment. Each configuration deployment targets an environment. You can enable one or more Amazon CloudWatch alarms for an environment. If an alarm is triggered during a deployment, AppConfig roles back the configuration.</p>

        Args:
            application_id: <p>The ID of the application that includes the environment you want to get.</p>
            environment_id: <p>The ID of the environment that you want to get.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve environment details
            The following get-environment example returns the details and state of the specified environment.

            >>> client.get_environment(application_id='339ohji', environment_id='54j1r29')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse["capo_appconfig.types.environment.Environment"]:
            import capo_appconfig._operations.amazon_app_config.get_environment

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_environment_request.GetEnvironmentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_experiment_definition(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.experiment_definition.ExperimentDefinition":
        """<p>Retrieves information about an experiment definition.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get an experiment definition
            The following GetExperimentDefinition example retrieves the details of an experiment definition.

            >>> client.get_experiment_definition(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_experiment_definition_request.GetExperimentDefinitionRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.experiment_definition.ExperimentDefinition"
        ]:
            import capo_appconfig._operations.amazon_app_config.get_experiment_definition

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_experiment_definition.get_experiment_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_experiment_definition_request.GetExperimentDefinitionRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_experiment_run(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        run: "capo_appconfig.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.experiment_run.ExperimentRun":
        """<p>Retrieves information about an experiment run, including its status, start time, and exposure settings.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            run: <p>The run number to retrieve.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get an experiment run
            The following GetExperimentRun example retrieves the details of an experiment run.

            >>> client.get_experiment_run(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k', run=1)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_experiment_run_request.GetExperimentRunRequest]",
        ) -> OperationResponse["capo_appconfig.types.experiment_run.ExperimentRun"]:
            import capo_appconfig._operations.amazon_app_config.get_experiment_run

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_experiment_run.get_experiment_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_experiment_run_request.GetExperimentRunRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
            "run": run,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_extension(
        self,
        extension_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        version_number: Optional["capo_appconfig.types.integer.Integer"] = None,
    ) -> "capo_appconfig.types.extension.Extension":
        """<p>Returns information about an AppConfig extension.</p>

        Args:
            extension_identifier: <p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>
            version_number: <p>The extension version number. If no version number was defined, AppConfig uses the highest version.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_extension_request.GetExtensionRequest]",
        ) -> OperationResponse["capo_appconfig.types.extension.Extension"]:
            import capo_appconfig._operations.amazon_app_config.get_extension

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_extension.get_extension(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_extension_request.GetExtensionRequest = {
            "extension_identifier": extension_identifier
        }
        if version_number is not None:
            input_["version_number"] = version_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_extension_association(
        self,
        extension_association_id: "capo_appconfig.types.id.Id",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.extension_association.ExtensionAssociation":
        """<p>Returns information about an AppConfig extension association. For more information about extensions and associations, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">Extending workflows</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            extension_association_id: <p>The extension association ID to get.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_extension_association_request.GetExtensionAssociationRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.extension_association.ExtensionAssociation"
        ]:
            import capo_appconfig._operations.amazon_app_config.get_extension_association

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_extension_association.get_extension_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_extension_association_request.GetExtensionAssociationRequest = {
            "extension_association_id": extension_association_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hosted_configuration_version(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        version_number: "capo_appconfig.types.integer.Integer",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.hosted_configuration_version.HostedConfigurationVersion":
        """<p>Retrieves information about a specific configuration version.</p>

        Args:
            application_id: <p>The application ID.</p>
            configuration_profile_id: <p>The configuration profile ID.</p>
            version_number: <p>The version.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve hosted configuration details
            The following get-hosted-configuration-version example retrieves the configuration details of the AWS AppConfig hosted configuration.

            >>> client.get_hosted_configuration_version(application_id='339ohji', configuration_profile_id='ur8hx2f', version_number=1)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.get_hosted_configuration_version_request.GetHostedConfigurationVersionRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.hosted_configuration_version.HostedConfigurationVersion"
        ]:
            import capo_appconfig._operations.amazon_app_config.get_hosted_configuration_version

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.get_hosted_configuration_version.get_hosted_configuration_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.get_hosted_configuration_version_request.GetHostedConfigurationVersionRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "version_number": version_number,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_applications(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "capo_appconfig.types.applications.Applications":
        """<p>Lists all applications in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Next token is a pagination token generated by AppConfig to describe what page the previous List call ended on. For the first List request, the nextToken should not be set. On subsequent calls, the nextToken parameter should be set to the previous responses nextToken value. Use this token to get the next set of results. </p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the available applications
            The following list-applications example lists the available applications in your AWS account.

            >>> client.list_applications()
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse["capo_appconfig.types.applications.Applications"]:
            import capo_appconfig._operations.amazon_app_config.list_applications

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_applications_request.ListApplicationsRequest = {}
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

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_appconfig.types.application.Application]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_configuration_profiles(
        self,
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        type: Optional[
            "capo_appconfig.types.configuration_profile_type.ConfigurationProfileType"
        ] = None,
    ) -> "capo_appconfig.types.configuration_profiles.ConfigurationProfiles":
        """<p>Lists the configuration profiles for an application.</p>

        Args:
            application_id: <p>The application ID.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>
            type: <p>A filter based on the type of configurations that the configuration profile contains. A configuration can be a feature flag or a freeform configuration.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the available configuration profiles
            The following list-configuration-profiles example lists the available configuration profiles for the specified application.

            >>> client.list_configuration_profiles(application_id='339ohji')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_configuration_profiles_request.ListConfigurationProfilesRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.configuration_profiles.ConfigurationProfiles"
        ]:
            import capo_appconfig._operations.amazon_app_config.list_configuration_profiles

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_configuration_profiles.list_configuration_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_configuration_profiles_request.ListConfigurationProfilesRequest = {
            "application_id": application_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_configuration_profiles(
        self,
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        type: Optional[
            "capo_appconfig.types.configuration_profile_type.ConfigurationProfileType"
        ] = None,
    ) -> "Iterator[capo_appconfig.types.configuration_profile_summary.ConfigurationProfileSummary]":
        _token = next_token
        while True:
            _response = self.list_configuration_profiles(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                type=type,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployments(
        self,
        application_id: "capo_appconfig.types.name.Name",
        environment_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "capo_appconfig.types.deployments.Deployments":
        """<p>Lists the deployments for an environment in descending deployment number order.</p>

        Args:
            application_id: <p>The application ID.</p>
            environment_id: <p>The environment ID.</p>
            max_results: <p>The maximum number of items that may be returned for this call. If there are items that have not yet been returned, the response will include a non-null <code>NextToken</code> that you can provide in a subsequent call to get the next set of results.</p>
            next_token: <p>The token returned by a prior call to this operation indicating the next set of results to be returned. If not specified, the operation will return the first set of results.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_deployments_request.ListDeploymentsRequest]",
        ) -> OperationResponse["capo_appconfig.types.deployments.Deployments"]:
            import capo_appconfig._operations.amazon_app_config.list_deployments

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_deployments_request.ListDeploymentsRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
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

    def iter_list_deployments(
        self,
        application_id: "capo_appconfig.types.name.Name",
        environment_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_appconfig.types.deployment_summary.DeploymentSummary]":
        _token = next_token
        while True:
            _response = self.list_deployments(
                application_id,
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_deployment_strategies(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "capo_appconfig.types.deployment_strategies.DeploymentStrategies":
        """<p>Lists deployment strategies.</p>

        Args:
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the available deployment strategies
            The following list-deployment-strategies example lists the available deployment strategies in your AWS account.

            >>> client.list_deployment_strategies()
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_deployment_strategies_request.ListDeploymentStrategiesRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.deployment_strategies.DeploymentStrategies"
        ]:
            import capo_appconfig._operations.amazon_app_config.list_deployment_strategies

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_deployment_strategies.list_deployment_strategies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_deployment_strategies_request.ListDeploymentStrategiesRequest = {}
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

    def iter_list_deployment_strategies(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_appconfig.types.deployment_strategy.DeploymentStrategy]":
        _token = next_token
        while True:
            _response = self.list_deployment_strategies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_environments(
        self,
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "capo_appconfig.types.environments.Environments":
        """<p>Lists the environments for an application.</p>

        Args:
            application_id: <p>The application ID.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the available environments
            The following list-environments example lists the available environments in your AWS account for the specified application.

            >>> client.list_environments(application_id='339ohji')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse["capo_appconfig.types.environments.Environments"]:
            import capo_appconfig._operations.amazon_app_config.list_environments

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_environments_request.ListEnvironmentsRequest = {
            "application_id": application_id
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

    def iter_list_environments(
        self,
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_appconfig.types.environment.Environment]":
        _token = next_token
        while True:
            _response = self.list_environments(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_experiment_definitions(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        application_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        configuration_profile_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        environment_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        status: Optional[
            "capo_appconfig.types.experiment_definition_status.ExperimentDefinitionStatus"
        ] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "capo_appconfig.types.experiment_definitions.ExperimentDefinitions":
        """<p>Lists the experiment definitions for an account. You can filter results by application, configuration profile, environment, or status.</p>

        Args:
            application_identifier: <p>The application ID or name to filter results.</p>
            configuration_profile_identifier: <p>The configuration profile ID or name to filter results.</p>
            environment_identifier: <p>The environment ID or name to filter results.</p>
            status: <p>A filter for the experiment definition status.</p>
            max_results: <p>The maximum number of items to return for this call.</p>
            next_token: <p>A token to start the list from a previously truncated response.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list experiment definitions
            The following ListExperimentDefinitions example lists the experiment definitions for an application.

            >>> client.list_experiment_definitions(application_identifier='339ohji')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_experiment_definitions_request.ListExperimentDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.experiment_definitions.ExperimentDefinitions"
        ]:
            import capo_appconfig._operations.amazon_app_config.list_experiment_definitions

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_experiment_definitions.list_experiment_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_experiment_definitions_request.ListExperimentDefinitionsRequest = {}
        if application_identifier is not None:
            input_["application_identifier"] = application_identifier
        if configuration_profile_identifier is not None:
            input_["configuration_profile_identifier"] = (
                configuration_profile_identifier
            )
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if status is not None:
            input_["status"] = status
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

    def iter_list_experiment_definitions(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        application_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        configuration_profile_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        environment_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        status: Optional[
            "capo_appconfig.types.experiment_definition_status.ExperimentDefinitionStatus"
        ] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_appconfig.types.experiment_definition_summary.ExperimentDefinitionSummary]":
        _token = next_token
        while True:
            _response = self.list_experiment_definitions(
                config_overrides=config_overrides,
                application_identifier=application_identifier,
                configuration_profile_identifier=configuration_profile_identifier,
                environment_identifier=environment_identifier,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_experiment_run_events(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        run: "capo_appconfig.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "capo_appconfig.types.experiment_run_events.ExperimentRunEvents":
        """<p>Lists the events for a specified experiment run. Events provide a timeline of actions and state changes that occurred during the run.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            run: <p>The run number.</p>
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>A token to start the list from a previously truncated response.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list experiment run events
            The following ListExperimentRunEvents example lists the events for an experiment run.

            >>> client.list_experiment_run_events(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k', run=1)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_experiment_run_events_request.ListExperimentRunEventsRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.experiment_run_events.ExperimentRunEvents"
        ]:
            import capo_appconfig._operations.amazon_app_config.list_experiment_run_events

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_experiment_run_events.list_experiment_run_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_experiment_run_events_request.ListExperimentRunEventsRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
            "run": run,
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

    def iter_list_experiment_run_events(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        run: "capo_appconfig.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_appconfig.types.experiment_run_event.ExperimentRunEvent]":
        _token = next_token
        while True:
            _response = self.list_experiment_run_events(
                application_identifier,
                experiment_definition_identifier,
                run,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_experiment_runs(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        status: Optional[
            "capo_appconfig.types.experiment_run_status.ExperimentRunStatus"
        ] = None,
    ) -> "capo_appconfig.types.experiment_runs.ExperimentRuns":
        """<p>Lists the experiment runs for a specified experiment definition. You can filter by status.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>A token to start the list from a previously truncated response.</p>
            status: <p>A filter for the experiment run status.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list experiment runs
            The following ListExperimentRuns example lists the experiment runs for an experiment definition.

            >>> client.list_experiment_runs(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_experiment_runs_request.ListExperimentRunsRequest]",
        ) -> OperationResponse["capo_appconfig.types.experiment_runs.ExperimentRuns"]:
            import capo_appconfig._operations.amazon_app_config.list_experiment_runs

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_experiment_runs.list_experiment_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_experiment_runs_request.ListExperimentRunsRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_experiment_runs(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        status: Optional[
            "capo_appconfig.types.experiment_run_status.ExperimentRunStatus"
        ] = None,
    ) -> "Iterator[capo_appconfig.types.experiment_run_summary.ExperimentRunSummary]":
        _token = next_token
        while True:
            _response = self.list_experiment_runs(
                application_identifier,
                experiment_definition_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_extension_associations(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        resource_identifier: Optional["capo_appconfig.types.arn.Arn"] = None,
        extension_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        extension_version_number: Optional[
            "capo_appconfig.types.integer.Integer"
        ] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "capo_appconfig.types.extension_associations.ExtensionAssociations":
        """<p>Lists all AppConfig extension associations in the account. For more information about extensions and associations, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">Extending workflows</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            resource_identifier: <p>The ARN of an application, configuration profile, or environment.</p>
            extension_identifier: <p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>
            extension_version_number: <p>The version number for the extension defined in the association.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results or pass null to get the first set of results. </p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_extension_associations_request.ListExtensionAssociationsRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.extension_associations.ExtensionAssociations"
        ]:
            import capo_appconfig._operations.amazon_app_config.list_extension_associations

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_extension_associations.list_extension_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_extension_associations_request.ListExtensionAssociationsRequest = {}
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if extension_identifier is not None:
            input_["extension_identifier"] = extension_identifier
        if extension_version_number is not None:
            input_["extension_version_number"] = extension_version_number
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

    def iter_list_extension_associations(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        resource_identifier: Optional["capo_appconfig.types.arn.Arn"] = None,
        extension_identifier: Optional[
            "capo_appconfig.types.identifier.Identifier"
        ] = None,
        extension_version_number: Optional[
            "capo_appconfig.types.integer.Integer"
        ] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_appconfig.types.extension_association_summary.ExtensionAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_extension_associations(
                config_overrides=config_overrides,
                resource_identifier=resource_identifier,
                extension_identifier=extension_identifier,
                extension_version_number=extension_version_number,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_extensions(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        name: Optional["capo_appconfig.types.query_name.QueryName"] = None,
    ) -> "capo_appconfig.types.extensions.Extensions":
        """<p>Lists all custom and Amazon Web Services authored AppConfig extensions in the account. For more information about extensions, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">Extending workflows</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            name: <p>The extension name.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_extensions_request.ListExtensionsRequest]",
        ) -> OperationResponse["capo_appconfig.types.extensions.Extensions"]:
            import capo_appconfig._operations.amazon_app_config.list_extensions

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_extensions.list_extensions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_extensions_request.ListExtensionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_extensions(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        name: Optional["capo_appconfig.types.query_name.QueryName"] = None,
    ) -> "Iterator[capo_appconfig.types.extension_summary.ExtensionSummary]":
        _token = next_token
        while True:
            _response = self.list_extensions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_hosted_configuration_versions(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        version_label: Optional["capo_appconfig.types.query_name.QueryName"] = None,
    ) -> (
        "capo_appconfig.types.hosted_configuration_versions.HostedConfigurationVersions"
    ):
        """<p>Lists configurations stored in the AppConfig hosted configuration store by version. </p>

        Args:
            application_id: <p>The application ID.</p>
            configuration_profile_id: <p>The configuration profile ID.</p>
            max_results: <p>The maximum number of items to return for this call. If <code>MaxResults</code> is not provided in the call, AppConfig returns the maximum of 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            version_label: <p>An optional filter that can be used to specify the version label of an AppConfig hosted configuration version. This parameter supports filtering by prefix using a wildcard, for example "v2*". If you don't specify an asterisk at the end of the value, only an exact match is returned.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the available hosted configuration versions
            The following list-hosted-configuration-versions example lists the configurations versions hosted in the AWS AppConfig hosted configuration store for the specified application and configuration profile.

            >>> client.list_hosted_configuration_versions(application_id='339ohji', configuration_profile_id='ur8hx2f')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_hosted_configuration_versions_request.ListHostedConfigurationVersionsRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.hosted_configuration_versions.HostedConfigurationVersions"
        ]:
            import capo_appconfig._operations.amazon_app_config.list_hosted_configuration_versions

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_hosted_configuration_versions.list_hosted_configuration_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_hosted_configuration_versions_request.ListHostedConfigurationVersionsRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if version_label is not None:
            input_["version_label"] = version_label

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_hosted_configuration_versions(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        max_results: Optional["capo_appconfig.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_appconfig.types.next_token.NextToken"] = None,
        version_label: Optional["capo_appconfig.types.query_name.QueryName"] = None,
    ) -> "Iterator[capo_appconfig.types.hosted_configuration_version_summary.HostedConfigurationVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_hosted_configuration_versions(
                application_id,
                configuration_profile_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                version_label=version_label,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_appconfig.types.arn.Arn",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> "capo_appconfig.types.resource_tags.ResourceTags":
        """<p>Retrieves the list of key-value tags assigned to the resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the tags of an application
            The following list-tags-for-resource example lists the tags of a specified application.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:appconfig:us-east-1:111122223333:application/339ohji')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse["capo_appconfig.types.resource_tags.ResourceTags"]:
            import capo_appconfig._operations.amazon_app_config.list_tags_for_resource

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_deployment(
        self,
        application_id: "capo_appconfig.types.name.Name",
        environment_id: "capo_appconfig.types.name.Name",
        deployment_strategy_id: "capo_appconfig.types.deployment_strategy_id.DeploymentStrategyId",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        configuration_version: "capo_appconfig.types.version.Version",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
        kms_key_identifier: Optional[
            "capo_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
        dynamic_extension_parameters: Optional[
            "capo_appconfig.types.dynamic_parameter_map.DynamicParameterMap"
        ] = None,
        latest_deployment_number: Optional[
            "capo_appconfig.types.integer.Integer"
        ] = None,
    ) -> "capo_appconfig.types.deployment.Deployment":
        """<p>Starts a deployment.</p> <note> <p>AppConfig Agent supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html#appconfig-entity-based-gradual-deployments">Using AppConfig Agent for user-based or entity-based gradual deployments</a> </p> </note>

        Args:
            application_id: <p>The application ID.</p>
            environment_id: <p>The environment ID.</p>
            deployment_strategy_id: <p>The deployment strategy ID.</p>
            configuration_profile_id: <p>The configuration profile ID.</p>
            configuration_version: <p>The configuration version to deploy. If deploying an AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.</p>
            description: <p>A description of the deployment.</p>
            tags: <p>Metadata to assign to the deployment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>
            kms_key_identifier: <p>The KMS key identifier (key ID, key alias, or key ARN). AppConfig uses this ID to encrypt the configuration data using a customer managed key. </p>
            dynamic_extension_parameters: <p>A map of dynamic extension parameter names to values to pass to associated extensions with <code>PRE_START_DEPLOYMENT</code> actions.</p>
            latest_deployment_number: <p>The number of the latest deployment. Use this value to ensure that the deployment starts from the expected state and to prevent conflicting updates.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.start_deployment_request.StartDeploymentRequest]",
        ) -> OperationResponse["capo_appconfig.types.deployment.Deployment"]:
            import capo_appconfig._operations.amazon_app_config.start_deployment

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.start_deployment.start_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.start_deployment_request.StartDeploymentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
            "deployment_strategy_id": deployment_strategy_id,
            "configuration_profile_id": configuration_profile_id,
            "configuration_version": configuration_version,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if dynamic_extension_parameters is not None:
            input_["dynamic_extension_parameters"] = dynamic_extension_parameters
        if latest_deployment_number is not None:
            input_["latest_deployment_number"] = latest_deployment_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_experiment_run(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        exposure_percentage: Optional[
            "capo_appconfig.types.nullable_percentage.NullablePercentage"
        ] = None,
        treatment_overrides: Optional[
            "capo_appconfig.types.treatment_overrides.TreatmentOverrides"
        ] = None,
        tags: Optional["capo_appconfig.types.tag_map.TagMap"] = None,
        deployment_parameters: Optional[
            "capo_appconfig.types.deployment_parameters.DeploymentParameters"
        ] = None,
    ) -> "capo_appconfig.types.experiment_run.ExperimentRun":
        """<p>Starts an experiment run for the specified experiment definition. An experiment run delivers treatments to the target audience and collects metrics. You can start multiple experiment runs from the same experiment definition.</p> <note> <p>Billing for this experiment begins when you call this operation and continues until the experiment is stopped. For pricing details, see <a href="https://aws.amazon.com/systems-manager/pricing/">AppConfig pricing</a>.</p> </note>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            description: <p>A description of this experiment run.</p>
            exposure_percentage: <p>The percentage of the target audience to expose to treatments. Set to 0 to validate the experiment before exposing production users.</p>
            treatment_overrides: <p>Treatment assignment overrides that assign specific entity IDs to treatments directly, bypassing random assignment.</p>
            tags: <p>The tags to assign to the experiment run.</p>
            deployment_parameters: <p>The deployment parameters for the experiment run, including a KMS key identifier for encryption.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start an experiment run
            The following StartExperimentRun example starts an experiment run with 50% audience exposure.

            >>> client.start_experiment_run(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k', exposure_percentage=50.0)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.start_experiment_run_request.StartExperimentRunRequest]",
        ) -> OperationResponse["capo_appconfig.types.experiment_run.ExperimentRun"]:
            import capo_appconfig._operations.amazon_app_config.start_experiment_run

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.start_experiment_run.start_experiment_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.start_experiment_run_request.StartExperimentRunRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
        }
        if description is not None:
            input_["description"] = description
        if exposure_percentage is not None:
            input_["exposure_percentage"] = exposure_percentage
        if treatment_overrides is not None:
            input_["treatment_overrides"] = treatment_overrides
        if tags is not None:
            input_["tags"] = tags
        if deployment_parameters is not None:
            input_["deployment_parameters"] = deployment_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_deployment(
        self,
        application_id: "capo_appconfig.types.name.Name",
        environment_id: "capo_appconfig.types.name.Name",
        deployment_number: "capo_appconfig.types.integer.Integer",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        allow_revert: Optional["capo_appconfig.types.boolean.Boolean"] = None,
    ) -> "capo_appconfig.types.deployment.Deployment":
        """<p>Stops a deployment. This API action works only on deployments that have a status of <code>DEPLOYING</code>, unless an <code>AllowRevert</code> parameter is supplied. If the <code>AllowRevert</code> parameter is supplied, the status of an in-progress deployment will be <code>ROLLED_BACK</code>. The status of a completed deployment will be <code>REVERTED</code>. AppConfig only allows a revert within 72 hours of deployment completion.</p>

        Args:
            application_id: <p>The application ID.</p>
            environment_id: <p>The environment ID.</p>
            deployment_number: <p>The sequence number of the deployment.</p>
            allow_revert: <p>A Boolean that enables AppConfig to rollback a <code>COMPLETED</code> deployment to the previous configuration version. This action moves the deployment to a status of <code>REVERTED</code>.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop configuration deployment
            The following stop-deployment example stops the deployment of an application configuration to the specified environment.

            >>> client.stop_deployment(application_id='339ohji', environment_id='54j1r29', deployment_number=2)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.stop_deployment_request.StopDeploymentRequest]",
        ) -> OperationResponse["capo_appconfig.types.deployment.Deployment"]:
            import capo_appconfig._operations.amazon_app_config.stop_deployment

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.stop_deployment.stop_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.stop_deployment_request.StopDeploymentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
            "deployment_number": deployment_number,
        }
        if allow_revert is not None:
            input_["allow_revert"] = allow_revert

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_experiment_run(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        run: "capo_appconfig.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        result: Optional[
            "capo_appconfig.types.experiment_run_result.ExperimentRunResult"
        ] = None,
        deployment_parameters: Optional[
            "capo_appconfig.types.deployment_parameters.DeploymentParameters"
        ] = None,
    ) -> "capo_appconfig.types.experiment_run.ExperimentRun":
        """<p>Stops a running experiment. Stopping an experiment run ends audience exposure and returns users to the currently deployed feature flag configuration.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            run: <p>The run number to stop.</p>
            result: <p>The result of the experiment run, including an executive summary and reasons for or against launching.</p>
            deployment_parameters: <p>The deployment parameters for the stop operation.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop an experiment run
            The following StopExperimentRun example stops a running experiment and records the result.

            >>> client.stop_experiment_run(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k', run=1, result={'ExecutiveSummary': 't1 wins with 16% lift in conversion', 'ReasonsToLaunch': 'Significant improvement in key metric'})
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.stop_experiment_run_request.StopExperimentRunRequest]",
        ) -> OperationResponse["capo_appconfig.types.experiment_run.ExperimentRun"]:
            import capo_appconfig._operations.amazon_app_config.stop_experiment_run

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.stop_experiment_run.stop_experiment_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.stop_experiment_run_request.StopExperimentRunRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
            "run": run,
        }
        if result is not None:
            input_["result"] = result
        if deployment_parameters is not None:
            input_["deployment_parameters"] = deployment_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_appconfig.types.arn.Arn",
        tags: "capo_appconfig.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> None:
        """<p>Assigns metadata to an AppConfig resource. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which to retrieve tags.</p>
            tags: <p>The key-value string map. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To tag an application
            The following tag-resource example tags an application resource.

            >>> client.tag_resource(resource_arn='arn:aws:appconfig:us-east-1:111122223333:application/339ohji', tags={'group1': '1'})
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.tag_resource

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.tag_resource_request.TagResourceRequest = {
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

    def untag_resource(
        self,
        resource_arn: "capo_appconfig.types.arn.Arn",
        tag_keys: "capo_appconfig.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> None:
        """<p>Deletes a tag key and value from an AppConfig resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which to remove tags.</p>
            tag_keys: <p>The tag keys to delete.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove a tag from an application
            The following untag-resource example removes the group1 tag from the specified application.

            >>> client.untag_resource(resource_arn='arn:aws:appconfig:us-east-1:111122223333:application/339ohji', tag_keys=['group1'])
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.untag_resource

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.untag_resource_request.UntagResourceRequest = {
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

    def update_account_settings(
        self,
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        deletion_protection: Optional[
            "capo_appconfig.types.deletion_protection_settings.DeletionProtectionSettings"
        ] = None,
        vended_metrics: Optional[
            "capo_appconfig.types.vended_metrics_settings.VendedMetricsSettings"
        ] = None,
    ) -> "capo_appconfig.types.account_settings.AccountSettings":
        """<p>Updates the value of the <code>DeletionProtection</code> parameter.</p>

        Args:
            deletion_protection: <p>A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile or an environment if AppConfig has called either <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html">GetLatestConfiguration</a> or for the configuration profile or from the environment during the specified interval. The default interval for <code>ProtectionPeriodInMinutes</code> is 60.</p>
            vended_metrics: <p>The configuration for vended metrics in the account.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_account_settings_request.UpdateAccountSettingsRequest]",
        ) -> OperationResponse["capo_appconfig.types.account_settings.AccountSettings"]:
            import capo_appconfig._operations.amazon_app_config.update_account_settings

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_account_settings.update_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_account_settings_request.UpdateAccountSettingsRequest = {}
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if vended_metrics is not None:
            input_["vended_metrics"] = vended_metrics

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application(
        self,
        application_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        name: Optional["capo_appconfig.types.name.Name"] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
    ) -> "capo_appconfig.types.application.Application":
        """<p>Updates an application.</p>

        Args:
            application_id: <p>The application ID.</p>
            name: <p>The name of the application.</p>
            description: <p>A description of the application.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an application
            The following update-application example updates the name of the specified application.

            >>> client.update_application(application_id='339ohji', name='Example-Application', description='')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse["capo_appconfig.types.application.Application"]:
            import capo_appconfig._operations.amazon_app_config.update_application

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_configuration_profile(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        name: Optional["capo_appconfig.types.long_name.LongName"] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        retrieval_role_arn: Optional["capo_appconfig.types.role_arn.RoleArn"] = None,
        validators: Optional[
            "capo_appconfig.types.validator_list.ValidatorList"
        ] = None,
        kms_key_identifier: Optional[
            "capo_appconfig.types.kms_key_identifier_or_empty.KmsKeyIdentifierOrEmpty"
        ] = None,
    ) -> "capo_appconfig.types.configuration_profile.ConfigurationProfile":
        """<p>Updates a configuration profile.</p>

        Args:
            application_id: <p>The application ID.</p>
            configuration_profile_id: <p>The ID of the configuration profile.</p>
            name: <p>The name of the configuration profile.</p>
            description: <p>A description of the configuration profile.</p>
            retrieval_role_arn: <p>The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.</p> <important> <p>A retrieval role ARN is not required for configurations stored in CodePipeline or the AppConfig hosted configuration store. It is required for all other sources that store your configuration. </p> </important>
            validators: <p>A list of methods for validating the configuration.</p>
            kms_key_identifier: <p>The identifier for a Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. The identifier can be an KMS key ID, alias, or the Amazon Resource Name (ARN) of the key ID or alias. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a configuration profile
            The following update-configuration-profile example updates the description of the specified configuration profile.

            >>> client.update_configuration_profile(application_id='339ohji', configuration_profile_id='ur8hx2f', description='Configuration profile used for examples.')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_configuration_profile_request.UpdateConfigurationProfileRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.configuration_profile.ConfigurationProfile"
        ]:
            import capo_appconfig._operations.amazon_app_config.update_configuration_profile

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_configuration_profile.update_configuration_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_configuration_profile_request.UpdateConfigurationProfileRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if retrieval_role_arn is not None:
            input_["retrieval_role_arn"] = retrieval_role_arn
        if validators is not None:
            input_["validators"] = validators
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_deployment_strategy(
        self,
        deployment_strategy_id: "capo_appconfig.types.deployment_strategy_id.DeploymentStrategyId",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        deployment_duration_in_minutes: Optional[
            "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
        ] = None,
        final_bake_time_in_minutes: Optional[
            "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
        ] = None,
        growth_factor: Optional[
            "capo_appconfig.types.growth_factor.GrowthFactor"
        ] = None,
        growth_type: Optional["capo_appconfig.types.growth_type.GrowthType"] = None,
    ) -> "capo_appconfig.types.deployment_strategy.DeploymentStrategy":
        """<p>Updates a deployment strategy.</p>

        Args:
            deployment_strategy_id: <p>The deployment strategy ID.</p>
            description: <p>A description of the deployment strategy.</p>
            deployment_duration_in_minutes: <p>Total amount of time for a deployment to last.</p>
            final_bake_time_in_minutes: <p>The amount of time that AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.</p>
            growth_factor: <p>The percentage of targets to receive a deployed configuration during each interval.</p>
            growth_type: <p>The algorithm used to define how percentage grows over time. AppConfig supports the following growth types:</p> <p> <b>Linear</b>: For this type, AppConfig processes the deployment by increments of the growth factor evenly distributed over the deployment time. For example, a linear deployment that uses a growth factor of 20 initially makes the configuration available to 20 percent of the targets. After 1/5th of the deployment time has passed, the system updates the percentage to 40 percent. This continues until 100% of the targets are set to receive the deployed configuration.</p> <p> <b>Exponential</b>: For this type, AppConfig processes the deployment exponentially using the following formula: <code>G*(2^N)</code>. In this formula, <code>G</code> is the growth factor specified by the user and <code>N</code> is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:</p> <p> <code>2*(2^0)</code> </p> <p> <code>2*(2^1)</code> </p> <p> <code>2*(2^2)</code> </p> <p>Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a deployment strategy
            The following update-deployment-strategy example updates final bake time to 20 minutes in the specified deployment strategy. ::


            >>> client.update_deployment_strategy(deployment_strategy_id='1225qzk', final_bake_time_in_minutes=20)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_deployment_strategy_request.UpdateDeploymentStrategyRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.deployment_strategy.DeploymentStrategy"
        ]:
            import capo_appconfig._operations.amazon_app_config.update_deployment_strategy

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_deployment_strategy.update_deployment_strategy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_deployment_strategy_request.UpdateDeploymentStrategyRequest = {
            "deployment_strategy_id": deployment_strategy_id
        }
        if description is not None:
            input_["description"] = description
        if deployment_duration_in_minutes is not None:
            input_["deployment_duration_in_minutes"] = deployment_duration_in_minutes
        if final_bake_time_in_minutes is not None:
            input_["final_bake_time_in_minutes"] = final_bake_time_in_minutes
        if growth_factor is not None:
            input_["growth_factor"] = growth_factor
        if growth_type is not None:
            input_["growth_type"] = growth_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_environment(
        self,
        application_id: "capo_appconfig.types.name.Name",
        environment_id: "capo_appconfig.types.name.Name",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        name: Optional["capo_appconfig.types.name.Name"] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        monitors: Optional["capo_appconfig.types.monitor_list.MonitorList"] = None,
    ) -> "capo_appconfig.types.environment.Environment":
        """<p>Updates an environment.</p>

        Args:
            application_id: <p>The application ID.</p>
            environment_id: <p>The environment ID.</p>
            name: <p>The name of the environment.</p>
            description: <p>A description of the environment.</p>
            monitors: <p>Amazon CloudWatch alarms to monitor during the deployment process.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an environment
            The following update-environment example updates an environment's description.

            >>> client.update_environment(application_id='339ohji', environment_id='54j1r29', description='An environment for examples.')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> OperationResponse["capo_appconfig.types.environment.Environment"]:
            import capo_appconfig._operations.amazon_app_config.update_environment

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_environment_request.UpdateEnvironmentRequest = {
            "application_id": application_id,
            "environment_id": environment_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if monitors is not None:
            input_["monitors"] = monitors

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_experiment_definition(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        treatments: Optional[
            "capo_appconfig.types.treatment_input_list.TreatmentInputList"
        ] = None,
        control: Optional["capo_appconfig.types.treatment_input.TreatmentInput"] = None,
        hypothesis: Optional["capo_appconfig.types.description.Description"] = None,
        audience_rule: Optional["capo_appconfig.types.rule.Rule"] = None,
        audience_description: Optional[
            "capo_appconfig.types.description.Description"
        ] = None,
        launch_criteria: Optional[
            "capo_appconfig.types.description.Description"
        ] = None,
    ) -> "capo_appconfig.types.experiment_definition.ExperimentDefinition":
        """<p>Updates an experiment definition. You can update treatments, the control, audience rules, and other properties. You cannot update an experiment definition while an experiment run is active.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            treatments: <p>The updated list of treatments to evaluate during the experiment. Each treatment defines a distinct variation compared to the control.</p>
            control: <p>An updated control treatment.</p>
            hypothesis: <p>An updated hypothesis.</p>
            audience_rule: <p>An updated audience rule.</p>
            audience_description: <p>An updated audience description.</p>
            launch_criteria: <p>Updated launch criteria.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an experiment definition
            The following UpdateExperimentDefinition example updates the hypothesis and audience rule of an experiment definition.

            >>> client.update_experiment_definition(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k', hypothesis='Enabling the feature will increase conversion by 10%', audience_rule='(eq $country "US")')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_experiment_definition_request.UpdateExperimentDefinitionRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.experiment_definition.ExperimentDefinition"
        ]:
            import capo_appconfig._operations.amazon_app_config.update_experiment_definition

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_experiment_definition.update_experiment_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_experiment_definition_request.UpdateExperimentDefinitionRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
        }
        if treatments is not None:
            input_["treatments"] = treatments
        if control is not None:
            input_["control"] = control
        if hypothesis is not None:
            input_["hypothesis"] = hypothesis
        if audience_rule is not None:
            input_["audience_rule"] = audience_rule
        if audience_description is not None:
            input_["audience_description"] = audience_description
        if launch_criteria is not None:
            input_["launch_criteria"] = launch_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_experiment_run(
        self,
        application_identifier: "capo_appconfig.types.identifier.Identifier",
        experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier",
        run: "capo_appconfig.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        exposure_percentage: Optional[
            "capo_appconfig.types.nullable_percentage.NullablePercentage"
        ] = None,
        treatment_overrides: Optional[
            "capo_appconfig.types.treatment_overrides.TreatmentOverrides"
        ] = None,
        deployment_parameters: Optional[
            "capo_appconfig.types.deployment_parameters.DeploymentParameters"
        ] = None,
    ) -> "capo_appconfig.types.experiment_run.ExperimentRun":
        """<p>Updates a running experiment. Use this operation to increase audience exposure, modify treatment assignment overrides, or update the description of an active experiment run. Audience exposure can only be increased, not decreased.</p>

        Args:
            application_identifier: <p>The application ID or name.</p>
            experiment_definition_identifier: <p>The experiment definition ID or name.</p>
            run: <p>The run number to update.</p>
            description: <p>An updated description for the experiment run.</p>
            exposure_percentage: <p>The new exposure percentage. This value can only be increased from the current setting.</p>
            treatment_overrides: <p>The updated treatment assignment overrides that assign specific entity IDs to treatments, bypassing random assignment.</p>
            deployment_parameters: <p>The updated deployment parameters for the experiment run.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an experiment run
            The following UpdateExperimentRun example increases the exposure percentage of a running experiment.

            >>> client.update_experiment_run(application_identifier='339ohji', experiment_definition_identifier='bsxyd7k', run=1, exposure_percentage=75.0)
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_experiment_run_request.UpdateExperimentRunRequest]",
        ) -> OperationResponse["capo_appconfig.types.experiment_run.ExperimentRun"]:
            import capo_appconfig._operations.amazon_app_config.update_experiment_run

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_experiment_run.update_experiment_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_experiment_run_request.UpdateExperimentRunRequest = {
            "application_identifier": application_identifier,
            "experiment_definition_identifier": experiment_definition_identifier,
            "run": run,
        }
        if description is not None:
            input_["description"] = description
        if exposure_percentage is not None:
            input_["exposure_percentage"] = exposure_percentage
        if treatment_overrides is not None:
            input_["treatment_overrides"] = treatment_overrides
        if deployment_parameters is not None:
            input_["deployment_parameters"] = deployment_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_extension(
        self,
        extension_identifier: "capo_appconfig.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        description: Optional["capo_appconfig.types.description.Description"] = None,
        actions: Optional["capo_appconfig.types.actions_map.ActionsMap"] = None,
        parameters: Optional["capo_appconfig.types.parameter_map.ParameterMap"] = None,
        version_number: Optional["capo_appconfig.types.integer.Integer"] = None,
    ) -> "capo_appconfig.types.extension.Extension":
        """<p>Updates an AppConfig extension. For more information about extensions, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">Extending workflows</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            extension_identifier: <p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>
            description: <p>Information about the extension.</p>
            actions: <p>The actions defined in the extension.</p>
            parameters: <p>One or more parameters for the actions called by the extension.</p>
            version_number: <p>The extension version number.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_extension_request.UpdateExtensionRequest]",
        ) -> OperationResponse["capo_appconfig.types.extension.Extension"]:
            import capo_appconfig._operations.amazon_app_config.update_extension

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_extension.update_extension(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_extension_request.UpdateExtensionRequest = {
            "extension_identifier": extension_identifier
        }
        if description is not None:
            input_["description"] = description
        if actions is not None:
            input_["actions"] = actions
        if parameters is not None:
            input_["parameters"] = parameters
        if version_number is not None:
            input_["version_number"] = version_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_extension_association(
        self,
        extension_association_id: "capo_appconfig.types.id.Id",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
        parameters: Optional[
            "capo_appconfig.types.parameter_value_map.ParameterValueMap"
        ] = None,
    ) -> "capo_appconfig.types.extension_association.ExtensionAssociation":
        """<p>Updates an association. For more information about extensions and associations, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html">Extending workflows</a> in the <i>AppConfig User Guide</i>.</p>

        Args:
            extension_association_id: <p>The system-generated ID for the association.</p>
            parameters: <p>The parameter names and values defined in the extension.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.update_extension_association_request.UpdateExtensionAssociationRequest]",
        ) -> OperationResponse[
            "capo_appconfig.types.extension_association.ExtensionAssociation"
        ]:
            import capo_appconfig._operations.amazon_app_config.update_extension_association

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.update_extension_association.update_extension_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.update_extension_association_request.UpdateExtensionAssociationRequest = {
            "extension_association_id": extension_association_id
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

    def validate_configuration(
        self,
        application_id: "capo_appconfig.types.name.Name",
        configuration_profile_id: "capo_appconfig.types.long_name.LongName",
        configuration_version: "capo_appconfig.types.version.Version",
        *,
        config_overrides: Optional[AppConfigClientConfig] = None,
    ) -> None:
        """<p>Uses the validators in a configuration profile to validate a configuration.</p>

        Args:
            application_id: <p>The application ID.</p>
            configuration_profile_id: <p>The configuration profile ID.</p>
            configuration_version: <p>The version of the configuration to validate.</p>

        Raises:
            capo_appconfig.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_appconfig.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the AppConfig service.</p>
            capo_appconfig.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfig.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To validate a configuration
            The following validate-configuration example uses the validators in a configuration profile to validate a configuration.

            >>> client.validate_configuration(application_id='abc1234', configuration_profile_id='ur8hx2f', configuration_version='1')
        """

        def _handler(
            req: "OperationRequest[capo_appconfig.types.validate_configuration_request.ValidateConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_appconfig._operations.amazon_app_config.validate_configuration

            output, http_response = (
                capo_appconfig._operations.amazon_app_config.validate_configuration.validate_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfig.types.validate_configuration_request.ValidateConfigurationRequest = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "configuration_version": configuration_version,
        }

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
