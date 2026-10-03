"""Generated from Smithy shape ``com.amazonaws.inspector#InspectorService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_inspector._auth._signers
import capo_inspector._auth._sigv4
from capo_inspector._auth._identity import Credentials
from capo_inspector._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_inspector._auth._zapros_handler import AuthMiddleware
from capo_inspector._pagination import resolve_path as _resolve_path
from capo_inspector._services._aws_config import aws_config
from capo_inspector._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_inspector.types.add_attributes_to_findings_request
    import capo_inspector.types.add_attributes_to_findings_response
    import capo_inspector.types.add_remove_attributes_finding_arn_list
    import capo_inspector.types.agent_filter
    import capo_inspector.types.arn
    import capo_inspector.types.assessment_run_duration
    import capo_inspector.types.assessment_run_filter
    import capo_inspector.types.assessment_run_name
    import capo_inspector.types.assessment_target_filter
    import capo_inspector.types.assessment_target_name
    import capo_inspector.types.assessment_template_filter
    import capo_inspector.types.assessment_template_name
    import capo_inspector.types.assessment_template_rules_package_arn_list
    import capo_inspector.types.batch_describe_arn_list
    import capo_inspector.types.batch_describe_exclusions_arn_list
    import capo_inspector.types.create_assessment_target_request
    import capo_inspector.types.create_assessment_target_response
    import capo_inspector.types.create_assessment_template_request
    import capo_inspector.types.create_assessment_template_response
    import capo_inspector.types.create_exclusions_preview_request
    import capo_inspector.types.create_exclusions_preview_response
    import capo_inspector.types.create_resource_group_request
    import capo_inspector.types.create_resource_group_response
    import capo_inspector.types.delete_assessment_run_request
    import capo_inspector.types.delete_assessment_target_request
    import capo_inspector.types.delete_assessment_template_request
    import capo_inspector.types.describe_assessment_runs_request
    import capo_inspector.types.describe_assessment_runs_response
    import capo_inspector.types.describe_assessment_targets_request
    import capo_inspector.types.describe_assessment_targets_response
    import capo_inspector.types.describe_assessment_templates_request
    import capo_inspector.types.describe_assessment_templates_response
    import capo_inspector.types.describe_cross_account_access_role_response
    import capo_inspector.types.describe_exclusions_request
    import capo_inspector.types.describe_exclusions_response
    import capo_inspector.types.describe_findings_request
    import capo_inspector.types.describe_findings_response
    import capo_inspector.types.describe_resource_groups_request
    import capo_inspector.types.describe_resource_groups_response
    import capo_inspector.types.describe_rules_packages_request
    import capo_inspector.types.describe_rules_packages_response
    import capo_inspector.types.finding_filter
    import capo_inspector.types.get_assessment_report_request
    import capo_inspector.types.get_assessment_report_response
    import capo_inspector.types.get_exclusions_preview_request
    import capo_inspector.types.get_exclusions_preview_response
    import capo_inspector.types.get_telemetry_metadata_request
    import capo_inspector.types.get_telemetry_metadata_response
    import capo_inspector.types.inspector_event
    import capo_inspector.types.list_assessment_run_agents_request
    import capo_inspector.types.list_assessment_run_agents_response
    import capo_inspector.types.list_assessment_runs_request
    import capo_inspector.types.list_assessment_runs_response
    import capo_inspector.types.list_assessment_targets_request
    import capo_inspector.types.list_assessment_targets_response
    import capo_inspector.types.list_assessment_templates_request
    import capo_inspector.types.list_assessment_templates_response
    import capo_inspector.types.list_event_subscriptions_max_results
    import capo_inspector.types.list_event_subscriptions_request
    import capo_inspector.types.list_event_subscriptions_response
    import capo_inspector.types.list_exclusions_request
    import capo_inspector.types.list_exclusions_response
    import capo_inspector.types.list_findings_request
    import capo_inspector.types.list_findings_response
    import capo_inspector.types.list_max_results
    import capo_inspector.types.list_parent_arn_list
    import capo_inspector.types.list_rules_packages_request
    import capo_inspector.types.list_rules_packages_response
    import capo_inspector.types.list_tags_for_resource_request
    import capo_inspector.types.list_tags_for_resource_response
    import capo_inspector.types.locale
    import capo_inspector.types.pagination_token
    import capo_inspector.types.preview_agents_max_results
    import capo_inspector.types.preview_agents_request
    import capo_inspector.types.preview_agents_response
    import capo_inspector.types.register_cross_account_access_role_request
    import capo_inspector.types.remove_attributes_from_findings_request
    import capo_inspector.types.remove_attributes_from_findings_response
    import capo_inspector.types.report_file_format
    import capo_inspector.types.report_type
    import capo_inspector.types.resource_group_tags
    import capo_inspector.types.set_tags_for_resource_request
    import capo_inspector.types.start_assessment_run_request
    import capo_inspector.types.start_assessment_run_response
    import capo_inspector.types.stop_action
    import capo_inspector.types.stop_assessment_run_request
    import capo_inspector.types.subscribe_to_event_request
    import capo_inspector.types.tag_list
    import capo_inspector.types.unsubscribe_from_event_request
    import capo_inspector.types.update_assessment_target_request
    import capo_inspector.types.user_attribute_key_list
    import capo_inspector.types.user_attribute_list
    import capo_inspector.types.uuid


class InspectorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class InspectorClient:
    """A client for the ``Inspector`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = InspectorClientConfig(
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
        self, config_overrides: Optional[InspectorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: InspectorClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def add_attributes_to_findings(
        self,
        finding_arns: "capo_inspector.types.add_remove_attributes_finding_arn_list.AddRemoveAttributesFindingArnList",
        attributes: "capo_inspector.types.user_attribute_list.UserAttributeList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.add_attributes_to_findings_response.AddAttributesToFindingsResponse":
        """<p>Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.</p>

        Args:
            finding_arns: <p>The ARNs that specify the findings that you want to assign attributes to.</p>
            attributes: <p>The array of attributes that you want to assign to specified findings.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Add attributes to findings
            Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.

            >>> client.add_attributes_to_findings(finding_arns=['arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU'], attributes=[{'key': 'Example', 'value': 'example'}])
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.add_attributes_to_findings_request.AddAttributesToFindingsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.add_attributes_to_findings_response.AddAttributesToFindingsResponse"
        ]:
            import capo_inspector._operations.inspector_service.add_attributes_to_findings

            output, http_response = (
                capo_inspector._operations.inspector_service.add_attributes_to_findings.add_attributes_to_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.add_attributes_to_findings_request.AddAttributesToFindingsRequest = {
            "finding_arns": finding_arns,
            "attributes": attributes,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_assessment_target(
        self,
        assessment_target_name: "capo_inspector.types.assessment_target_name.AssessmentTargetName",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        resource_group_arn: Optional["capo_inspector.types.arn.Arn"] = None,
    ) -> "capo_inspector.types.create_assessment_target_response.CreateAssessmentTargetResponse":
        """<p>Creates a new assessment target using the ARN of the resource group that is generated by <a>CreateResourceGroup</a>. If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target. If the <a href="https://docs.aws.amazon.com/inspector/latest/userguide/inspector_slr.html">service-linked role</a> isn’t already registered, this action also creates and registers a service-linked role to grant Amazon Inspector access to AWS Services needed to perform security assessments. You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account. For more information, see <a href="https://docs.aws.amazon.com/inspector/latest/userguide/inspector_applications.html"> Amazon Inspector Assessment Targets</a>.</p>

        Args:
            assessment_target_name: <p>The user-defined name that identifies the assessment target that you want to create. The name must be unique within the AWS account.</p>
            resource_group_arn: <p>The ARN that specifies the resource group that is used to create the assessment target. If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_cross_account_role_exception.InvalidCrossAccountRoleException: <p>Amazon Inspector cannot assume the cross-account role that it needs to list your EC2 instances during the assessment run.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current AWS account limits. The error code describes the limit exceeded.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create assessment target
            Creates a new assessment target using the ARN of the resource group that is generated by CreateResourceGroup. You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account.

            >>> client.create_assessment_target(assessment_target_name='ExampleAssessmentTarget', resource_group_arn='arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.create_assessment_target_request.CreateAssessmentTargetRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.create_assessment_target_response.CreateAssessmentTargetResponse"
        ]:
            import capo_inspector._operations.inspector_service.create_assessment_target

            output, http_response = (
                capo_inspector._operations.inspector_service.create_assessment_target.create_assessment_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.create_assessment_target_request.CreateAssessmentTargetRequest = {
            "assessment_target_name": assessment_target_name
        }
        if resource_group_arn is not None:
            input_["resource_group_arn"] = resource_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_assessment_template(
        self,
        assessment_target_arn: "capo_inspector.types.arn.Arn",
        assessment_template_name: "capo_inspector.types.assessment_template_name.AssessmentTemplateName",
        duration_in_seconds: "capo_inspector.types.assessment_run_duration.AssessmentRunDuration",
        rules_package_arns: "capo_inspector.types.assessment_template_rules_package_arn_list.AssessmentTemplateRulesPackageArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        user_attributes_for_findings: Optional[
            "capo_inspector.types.user_attribute_list.UserAttributeList"
        ] = None,
    ) -> "capo_inspector.types.create_assessment_template_response.CreateAssessmentTemplateResponse":
        """<p>Creates an assessment template for the assessment target that is specified by the ARN of the assessment target. If the <a href="https://docs.aws.amazon.com/inspector/latest/userguide/inspector_slr.html">service-linked role</a> isn’t already registered, this action also creates and registers a service-linked role to grant Amazon Inspector access to AWS Services needed to perform security assessments.</p>

        Args:
            assessment_target_arn: <p>The ARN that specifies the assessment target for which you want to create the assessment template.</p>
            assessment_template_name: <p>The user-defined name that identifies the assessment template that you want to create. You can create several assessment templates for an assessment target. The names of the assessment templates that correspond to a particular assessment target must be unique.</p>
            duration_in_seconds: <p>The duration of the assessment run in seconds.</p>
            rules_package_arns: <p>The ARNs that specify the rules packages that you want to attach to the assessment template.</p>
            user_attributes_for_findings: <p>The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template. An attribute is a key and value pair (an <a>Attribute</a> object). Within an assessment template, each key must be unique.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current AWS account limits. The error code describes the limit exceeded.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create assessment template
            Creates an assessment template for the assessment target that is specified by the ARN of the assessment target.

            >>> client.create_assessment_template(assessment_target_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX', assessment_template_name='ExampleAssessmentTemplate', duration_in_seconds=180, rules_package_arns=['arn:aws:inspector:us-west-2:758058086616:rulespackage/0-11B9DBXp'], user_attributes_for_findings=[{'key': 'Example', 'value': 'example'}])
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.create_assessment_template_request.CreateAssessmentTemplateRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.create_assessment_template_response.CreateAssessmentTemplateResponse"
        ]:
            import capo_inspector._operations.inspector_service.create_assessment_template

            output, http_response = (
                capo_inspector._operations.inspector_service.create_assessment_template.create_assessment_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.create_assessment_template_request.CreateAssessmentTemplateRequest = {
            "assessment_target_arn": assessment_target_arn,
            "assessment_template_name": assessment_template_name,
            "duration_in_seconds": duration_in_seconds,
            "rules_package_arns": rules_package_arns,
        }
        if user_attributes_for_findings is not None:
            input_["user_attributes_for_findings"] = user_attributes_for_findings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_exclusions_preview(
        self,
        assessment_template_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.create_exclusions_preview_response.CreateExclusionsPreviewResponse":
        """<p>Starts the generation of an exclusions preview for the specified assessment template. The exclusions preview lists the potential exclusions (ExclusionPreview) that Inspector can detect before it runs the assessment. </p>

        Args:
            assessment_template_arn: <p>The ARN that specifies the assessment template for which you want to create an exclusions preview.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.preview_generation_in_progress_exception.PreviewGenerationInProgressException: <p>The request is rejected. The specified assessment template is currently generating an exclusions preview.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.create_exclusions_preview_request.CreateExclusionsPreviewRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.create_exclusions_preview_response.CreateExclusionsPreviewResponse"
        ]:
            import capo_inspector._operations.inspector_service.create_exclusions_preview

            output, http_response = (
                capo_inspector._operations.inspector_service.create_exclusions_preview.create_exclusions_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.create_exclusions_preview_request.CreateExclusionsPreviewRequest = {
            "assessment_template_arn": assessment_template_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_resource_group(
        self,
        resource_group_tags: "capo_inspector.types.resource_group_tags.ResourceGroupTags",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.create_resource_group_response.CreateResourceGroupResponse":
        """<p>Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target. For more information, see <a>CreateAssessmentTarget</a>.</p>

        Args:
            resource_group_tags: <p>A collection of keys and an array of possible values, '[{"key":"key1","values":["Value1","Value2"]},{"key":"Key2","values":["Value3"]}]'.</p> <p>For example,'[{"key":"Name","values":["TestEC2Instance"]}]'.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current AWS account limits. The error code describes the limit exceeded.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create resource group
            Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target.

            >>> client.create_resource_group(resource_group_tags=[{'key': 'Name', 'value': 'example'}])
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.create_resource_group_request.CreateResourceGroupRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.create_resource_group_response.CreateResourceGroupResponse"
        ]:
            import capo_inspector._operations.inspector_service.create_resource_group

            output, http_response = (
                capo_inspector._operations.inspector_service.create_resource_group.create_resource_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.create_resource_group_request.CreateResourceGroupRequest = {
            "resource_group_tags": resource_group_tags
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_assessment_run(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> None:
        """<p>Deletes the assessment run that is specified by the ARN of the assessment run.</p>

        Args:
            assessment_run_arn: <p>The ARN that specifies the assessment run that you want to delete.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.assessment_run_in_progress_exception.AssessmentRunInProgressException: <p>You cannot perform a specified action if an assessment run is currently in progress.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete assessment run
            Deletes the assessment run that is specified by the ARN of the assessment run.

            >>> client.delete_assessment_run(assessment_run_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.delete_assessment_run_request.DeleteAssessmentRunRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.delete_assessment_run

            output, http_response = (
                capo_inspector._operations.inspector_service.delete_assessment_run.delete_assessment_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.delete_assessment_run_request.DeleteAssessmentRunRequest = {
            "assessment_run_arn": assessment_run_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_assessment_target(
        self,
        assessment_target_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> None:
        """<p>Deletes the assessment target that is specified by the ARN of the assessment target.</p>

        Args:
            assessment_target_arn: <p>The ARN that specifies the assessment target that you want to delete.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.assessment_run_in_progress_exception.AssessmentRunInProgressException: <p>You cannot perform a specified action if an assessment run is currently in progress.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete assessment target
            Deletes the assessment target that is specified by the ARN of the assessment target.

            >>> client.delete_assessment_target(assessment_target_arn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.delete_assessment_target_request.DeleteAssessmentTargetRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.delete_assessment_target

            output, http_response = (
                capo_inspector._operations.inspector_service.delete_assessment_target.delete_assessment_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.delete_assessment_target_request.DeleteAssessmentTargetRequest = {
            "assessment_target_arn": assessment_target_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_assessment_template(
        self,
        assessment_template_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> None:
        """<p>Deletes the assessment template that is specified by the ARN of the assessment template.</p>

        Args:
            assessment_template_arn: <p>The ARN that specifies the assessment template that you want to delete.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.assessment_run_in_progress_exception.AssessmentRunInProgressException: <p>You cannot perform a specified action if an assessment run is currently in progress.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete assessment template
            Deletes the assessment template that is specified by the ARN of the assessment template.

            >>> client.delete_assessment_template(assessment_template_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.delete_assessment_template_request.DeleteAssessmentTemplateRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.delete_assessment_template

            output, http_response = (
                capo_inspector._operations.inspector_service.delete_assessment_template.delete_assessment_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.delete_assessment_template_request.DeleteAssessmentTemplateRequest = {
            "assessment_template_arn": assessment_template_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_assessment_runs(
        self,
        assessment_run_arns: "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.describe_assessment_runs_response.DescribeAssessmentRunsResponse":
        """<p>Describes the assessment runs that are specified by the ARNs of the assessment runs.</p>

        Args:
            assessment_run_arns: <p>The ARN that specifies the assessment run that you want to describe.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.describe_assessment_runs_request.DescribeAssessmentRunsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_assessment_runs_response.DescribeAssessmentRunsResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_assessment_runs

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_assessment_runs.describe_assessment_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.describe_assessment_runs_request.DescribeAssessmentRunsRequest = {
            "assessment_run_arns": assessment_run_arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_assessment_targets(
        self,
        assessment_target_arns: "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.describe_assessment_targets_response.DescribeAssessmentTargetsResponse":
        """<p>Describes the assessment targets that are specified by the ARNs of the assessment targets.</p>

        Args:
            assessment_target_arns: <p>The ARNs that specifies the assessment targets that you want to describe.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.describe_assessment_targets_request.DescribeAssessmentTargetsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_assessment_targets_response.DescribeAssessmentTargetsResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_assessment_targets

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_assessment_targets.describe_assessment_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.describe_assessment_targets_request.DescribeAssessmentTargetsRequest = {
            "assessment_target_arns": assessment_target_arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_assessment_templates(
        self,
        assessment_template_arns: "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.describe_assessment_templates_response.DescribeAssessmentTemplatesResponse":
        """<p>Describes the assessment templates that are specified by the ARNs of the assessment templates.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.describe_assessment_templates_request.DescribeAssessmentTemplatesRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_assessment_templates_response.DescribeAssessmentTemplatesResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_assessment_templates

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_assessment_templates.describe_assessment_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.describe_assessment_templates_request.DescribeAssessmentTemplatesRequest = {
            "assessment_template_arns": assessment_template_arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cross_account_access_role(
        self, *, config_overrides: Optional[InspectorClientConfig] = None
    ) -> "capo_inspector.types.describe_cross_account_access_role_response.DescribeCrossAccountAccessRoleResponse":
        """<p>Describes the IAM role that enables Amazon Inspector to access your AWS account.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_cross_account_access_role_response.DescribeCrossAccountAccessRoleResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_cross_account_access_role

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_cross_account_access_role.describe_cross_account_access_role(
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

    def describe_exclusions(
        self,
        exclusion_arns: "capo_inspector.types.batch_describe_exclusions_arn_list.BatchDescribeExclusionsArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        locale: Optional["capo_inspector.types.locale.Locale"] = None,
    ) -> "capo_inspector.types.describe_exclusions_response.DescribeExclusionsResponse":
        """<p>Describes the exclusions that are specified by the exclusions' ARNs.</p>

        Args:
            exclusion_arns: <p>The list of ARNs that specify the exclusions that you want to describe.</p>
            locale: <p>The locale into which you want to translate the exclusion's title, description, and recommendation.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.describe_exclusions_request.DescribeExclusionsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_exclusions_response.DescribeExclusionsResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_exclusions

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_exclusions.describe_exclusions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.describe_exclusions_request.DescribeExclusionsRequest = {
            "exclusion_arns": exclusion_arns
        }
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_findings(
        self,
        finding_arns: "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        locale: Optional["capo_inspector.types.locale.Locale"] = None,
    ) -> "capo_inspector.types.describe_findings_response.DescribeFindingsResponse":
        """<p>Describes the findings that are specified by the ARNs of the findings.</p>

        Args:
            finding_arns: <p>The ARN that specifies the finding that you want to describe.</p>
            locale: <p>The locale into which you want to translate a finding description, recommendation, and the short description that identifies the finding.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.describe_findings_request.DescribeFindingsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_findings_response.DescribeFindingsResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_findings

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_findings.describe_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.describe_findings_request.DescribeFindingsRequest = {
            "finding_arns": finding_arns
        }
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_resource_groups(
        self,
        resource_group_arns: "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.describe_resource_groups_response.DescribeResourceGroupsResponse":
        """<p>Describes the resource groups that are specified by the ARNs of the resource groups.</p>

        Args:
            resource_group_arns: <p>The ARN that specifies the resource group that you want to describe.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.describe_resource_groups_request.DescribeResourceGroupsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_resource_groups_response.DescribeResourceGroupsResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_resource_groups

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_resource_groups.describe_resource_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.describe_resource_groups_request.DescribeResourceGroupsRequest = {
            "resource_group_arns": resource_group_arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_rules_packages(
        self,
        rules_package_arns: "capo_inspector.types.batch_describe_arn_list.BatchDescribeArnList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        locale: Optional["capo_inspector.types.locale.Locale"] = None,
    ) -> "capo_inspector.types.describe_rules_packages_response.DescribeRulesPackagesResponse":
        """<p>Describes the rules packages that are specified by the ARNs of the rules packages.</p>

        Args:
            rules_package_arns: <p>The ARN that specifies the rules package that you want to describe.</p>
            locale: <p>The locale that you want to translate a rules package description into.</p>

        Raises:
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe rules packages
            Describes the rules packages that are specified by the ARNs of the rules packages.

            >>> client.describe_rules_packages(rules_package_arns=['arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ'])
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.describe_rules_packages_request.DescribeRulesPackagesRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.describe_rules_packages_response.DescribeRulesPackagesResponse"
        ]:
            import capo_inspector._operations.inspector_service.describe_rules_packages

            output, http_response = (
                capo_inspector._operations.inspector_service.describe_rules_packages.describe_rules_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.describe_rules_packages_request.DescribeRulesPackagesRequest = {
            "rules_package_arns": rules_package_arns
        }
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_assessment_report(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        report_file_format: "capo_inspector.types.report_file_format.ReportFileFormat",
        report_type: "capo_inspector.types.report_type.ReportType",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.get_assessment_report_response.GetAssessmentReportResponse":
        """<p>Produces an assessment report that includes detailed and comprehensive results of a specified assessment run. </p>

        Args:
            assessment_run_arn: <p>The ARN that specifies the assessment run for which you want to generate a report.</p>
            report_file_format: <p>Specifies the file format (html or pdf) of the assessment report that you want to generate.</p>
            report_type: <p>Specifies the type of the assessment report that you want to generate. There are two types of assessment reports: a finding report and a full report. For more information, see <a href="https://docs.aws.amazon.com/inspector/latest/userguide/inspector_reports.html">Assessment Reports</a>. </p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.assessment_run_in_progress_exception.AssessmentRunInProgressException: <p>You cannot perform a specified action if an assessment run is currently in progress.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>Used by the <a>GetAssessmentReport</a> API. The request was rejected because you tried to generate a report for an assessment run that existed before reporting was supported in Amazon Inspector. You can only generate reports for assessment runs that took place or will take place after generating reports in Amazon Inspector became available.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.get_assessment_report_request.GetAssessmentReportRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.get_assessment_report_response.GetAssessmentReportResponse"
        ]:
            import capo_inspector._operations.inspector_service.get_assessment_report

            output, http_response = (
                capo_inspector._operations.inspector_service.get_assessment_report.get_assessment_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.get_assessment_report_request.GetAssessmentReportRequest = {
            "assessment_run_arn": assessment_run_arn,
            "report_file_format": report_file_format,
            "report_type": report_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_exclusions_preview(
        self,
        assessment_template_arn: "capo_inspector.types.arn.Arn",
        preview_token: "capo_inspector.types.uuid.UUID",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
        locale: Optional["capo_inspector.types.locale.Locale"] = None,
    ) -> "capo_inspector.types.get_exclusions_preview_response.GetExclusionsPreviewResponse":
        """<p>Retrieves the exclusions preview (a list of ExclusionPreview objects) specified by the preview token. You can obtain the preview token by running the CreateExclusionsPreview API.</p>

        Args:
            assessment_template_arn: <p>The ARN that specifies the assessment template for which the exclusions preview was requested.</p>
            preview_token: <p>The unique identifier associated of the exclusions preview.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the GetExclusionsPreviewRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.</p>
            locale: <p>The locale into which you want to translate the exclusion's title, description, and recommendation.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.get_exclusions_preview_request.GetExclusionsPreviewRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.get_exclusions_preview_response.GetExclusionsPreviewResponse"
        ]:
            import capo_inspector._operations.inspector_service.get_exclusions_preview

            output, http_response = (
                capo_inspector._operations.inspector_service.get_exclusions_preview.get_exclusions_preview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.get_exclusions_preview_request.GetExclusionsPreviewRequest = {
            "assessment_template_arn": assessment_template_arn,
            "preview_token": preview_token,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_exclusions_preview(
        self,
        assessment_template_arn: "capo_inspector.types.arn.Arn",
        preview_token: "capo_inspector.types.uuid.UUID",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
        locale: Optional["capo_inspector.types.locale.Locale"] = None,
    ) -> "Iterator[capo_inspector.types.get_exclusions_preview_response.GetExclusionsPreviewResponse]":
        _token = next_token
        while True:
            _response = self.get_exclusions_preview(
                assessment_template_arn,
                preview_token,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                locale=locale,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_telemetry_metadata(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.get_telemetry_metadata_response.GetTelemetryMetadataResponse":
        """<p>Information about the data that is collected for the specified assessment run.</p>

        Args:
            assessment_run_arn: <p>The ARN that specifies the assessment run that has the telemetry data that you want to obtain.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get telemetry metadata
            Information about the data that is collected for the specified assessment run.

            >>> client.get_telemetry_metadata(assessment_run_arn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.get_telemetry_metadata_request.GetTelemetryMetadataRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.get_telemetry_metadata_response.GetTelemetryMetadataResponse"
        ]:
            import capo_inspector._operations.inspector_service.get_telemetry_metadata

            output, http_response = (
                capo_inspector._operations.inspector_service.get_telemetry_metadata.get_telemetry_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.get_telemetry_metadata_request.GetTelemetryMetadataRequest = {
            "assessment_run_arn": assessment_run_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_assessment_run_agents(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        filter: Optional["capo_inspector.types.agent_filter.AgentFilter"] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "capo_inspector.types.list_assessment_run_agents_response.ListAssessmentRunAgentsResponse":
        """<p>Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.</p>

        Args:
            assessment_run_arn: <p>The ARN that specifies the assessment run whose agents you want to list.</p>
            filter: <p>You can use this parameter to specify a subset of data to be included in the action's response.</p> <p>For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListAssessmentRunAgents</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List assessment run agents
            Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.

            >>> client.list_assessment_run_agents(assessment_run_arn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE', max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_assessment_run_agents_request.ListAssessmentRunAgentsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_assessment_run_agents_response.ListAssessmentRunAgentsResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_assessment_run_agents

            output, http_response = (
                capo_inspector._operations.inspector_service.list_assessment_run_agents.list_assessment_run_agents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_assessment_run_agents_request.ListAssessmentRunAgentsRequest = {
            "assessment_run_arn": assessment_run_arn
        }
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_assessment_run_agents(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        filter: Optional["capo_inspector.types.agent_filter.AgentFilter"] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.list_assessment_run_agents_response.ListAssessmentRunAgentsResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_run_agents(
                assessment_run_arn,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assessment_runs(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        assessment_template_arns: Optional[
            "capo_inspector.types.list_parent_arn_list.ListParentArnList"
        ] = None,
        filter: Optional[
            "capo_inspector.types.assessment_run_filter.AssessmentRunFilter"
        ] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> (
        "capo_inspector.types.list_assessment_runs_response.ListAssessmentRunsResponse"
    ):
        """<p>Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.</p>

        Args:
            assessment_template_arns: <p>The ARNs that specify the assessment templates whose assessment runs you want to list.</p>
            filter: <p>You can use this parameter to specify a subset of data to be included in the action's response.</p> <p>For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListAssessmentRuns</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List assessment runs
            Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.

            >>> client.list_assessment_runs(assessment_template_arns=['arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw'], max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_assessment_runs_request.ListAssessmentRunsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_assessment_runs_response.ListAssessmentRunsResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_assessment_runs

            output, http_response = (
                capo_inspector._operations.inspector_service.list_assessment_runs.list_assessment_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_assessment_runs_request.ListAssessmentRunsRequest = {}
        if assessment_template_arns is not None:
            input_["assessment_template_arns"] = assessment_template_arns
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_assessment_runs(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        assessment_template_arns: Optional[
            "capo_inspector.types.list_parent_arn_list.ListParentArnList"
        ] = None,
        filter: Optional[
            "capo_inspector.types.assessment_run_filter.AssessmentRunFilter"
        ] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.list_assessment_runs_response.ListAssessmentRunsResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_runs(
                config_overrides=config_overrides,
                assessment_template_arns=assessment_template_arns,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assessment_targets(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        filter: Optional[
            "capo_inspector.types.assessment_target_filter.AssessmentTargetFilter"
        ] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "capo_inspector.types.list_assessment_targets_response.ListAssessmentTargetsResponse":
        """<p>Lists the ARNs of the assessment targets within this AWS account. For more information about assessment targets, see <a href="https://docs.aws.amazon.com/inspector/latest/userguide/inspector_applications.html">Amazon Inspector Assessment Targets</a>.</p>

        Args:
            filter: <p>You can use this parameter to specify a subset of data to be included in the action's response.</p> <p>For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListAssessmentTargets</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List assessment targets
            Lists the ARNs of the assessment targets within this AWS account.

            >>> client.list_assessment_targets(max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_assessment_targets_request.ListAssessmentTargetsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_assessment_targets_response.ListAssessmentTargetsResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_assessment_targets

            output, http_response = (
                capo_inspector._operations.inspector_service.list_assessment_targets.list_assessment_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_assessment_targets_request.ListAssessmentTargetsRequest = {}
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_assessment_targets(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        filter: Optional[
            "capo_inspector.types.assessment_target_filter.AssessmentTargetFilter"
        ] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.list_assessment_targets_response.ListAssessmentTargetsResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_targets(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assessment_templates(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        assessment_target_arns: Optional[
            "capo_inspector.types.list_parent_arn_list.ListParentArnList"
        ] = None,
        filter: Optional[
            "capo_inspector.types.assessment_template_filter.AssessmentTemplateFilter"
        ] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "capo_inspector.types.list_assessment_templates_response.ListAssessmentTemplatesResponse":
        """<p>Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.</p>

        Args:
            assessment_target_arns: <p>A list of ARNs that specifies the assessment targets whose assessment templates you want to list.</p>
            filter: <p>You can use this parameter to specify a subset of data to be included in the action's response.</p> <p>For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListAssessmentTemplates</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List assessment templates
            Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.

            >>> client.list_assessment_templates(assessment_target_arns=['arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq'], max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_assessment_templates_request.ListAssessmentTemplatesRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_assessment_templates_response.ListAssessmentTemplatesResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_assessment_templates

            output, http_response = (
                capo_inspector._operations.inspector_service.list_assessment_templates.list_assessment_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_assessment_templates_request.ListAssessmentTemplatesRequest = {}
        if assessment_target_arns is not None:
            input_["assessment_target_arns"] = assessment_target_arns
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_assessment_templates(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        assessment_target_arns: Optional[
            "capo_inspector.types.list_parent_arn_list.ListParentArnList"
        ] = None,
        filter: Optional[
            "capo_inspector.types.assessment_template_filter.AssessmentTemplateFilter"
        ] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.list_assessment_templates_response.ListAssessmentTemplatesResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_templates(
                config_overrides=config_overrides,
                assessment_target_arns=assessment_target_arns,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_subscriptions(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        resource_arn: Optional["capo_inspector.types.arn.Arn"] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_event_subscriptions_max_results.ListEventSubscriptionsMaxResults"
        ] = None,
    ) -> "capo_inspector.types.list_event_subscriptions_response.ListEventSubscriptionsResponse":
        """<p>Lists all the event subscriptions for the assessment template that is specified by the ARN of the assessment template. For more information, see <a>SubscribeToEvent</a> and <a>UnsubscribeFromEvent</a>.</p>

        Args:
            resource_arn: <p>The ARN of the assessment template for which you want to list the existing event subscriptions.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListEventSubscriptions</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_event_subscriptions_request.ListEventSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_event_subscriptions_response.ListEventSubscriptionsResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_event_subscriptions

            output, http_response = (
                capo_inspector._operations.inspector_service.list_event_subscriptions.list_event_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_event_subscriptions_request.ListEventSubscriptionsRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
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

    def iter_list_event_subscriptions(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        resource_arn: Optional["capo_inspector.types.arn.Arn"] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_event_subscriptions_max_results.ListEventSubscriptionsMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.list_event_subscriptions_response.ListEventSubscriptionsResponse]":
        _token = next_token
        while True:
            _response = self.list_event_subscriptions(
                config_overrides=config_overrides,
                resource_arn=resource_arn,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_exclusions(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "capo_inspector.types.list_exclusions_response.ListExclusionsResponse":
        """<p>List exclusions that are generated by the assessment run.</p>

        Args:
            assessment_run_arn: <p>The ARN of the assessment run that generated the exclusions that you want to list.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListExclusionsRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_exclusions_request.ListExclusionsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_exclusions_response.ListExclusionsResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_exclusions

            output, http_response = (
                capo_inspector._operations.inspector_service.list_exclusions.list_exclusions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_exclusions_request.ListExclusionsRequest = {
            "assessment_run_arn": assessment_run_arn
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

    def iter_list_exclusions(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> (
        "Iterator[capo_inspector.types.list_exclusions_response.ListExclusionsResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_exclusions(
                assessment_run_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_findings(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        assessment_run_arns: Optional[
            "capo_inspector.types.list_parent_arn_list.ListParentArnList"
        ] = None,
        filter: Optional["capo_inspector.types.finding_filter.FindingFilter"] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "capo_inspector.types.list_findings_response.ListFindingsResponse":
        """<p>Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.</p>

        Args:
            assessment_run_arns: <p>The ARNs of the assessment runs that generate the findings that you want to list.</p>
            filter: <p>You can use this parameter to specify a subset of data to be included in the action's response.</p> <p>For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListFindings</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List findings
            Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.

            >>> client.list_findings(assessment_run_arns=['arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE'], max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_findings_request.ListFindingsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_findings_response.ListFindingsResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_findings

            output, http_response = (
                capo_inspector._operations.inspector_service.list_findings.list_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_findings_request.ListFindingsRequest = {}
        if assessment_run_arns is not None:
            input_["assessment_run_arns"] = assessment_run_arns
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_findings(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        assessment_run_arns: Optional[
            "capo_inspector.types.list_parent_arn_list.ListParentArnList"
        ] = None,
        filter: Optional["capo_inspector.types.finding_filter.FindingFilter"] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.list_findings_response.ListFindingsResponse]":
        _token = next_token
        while True:
            _response = self.list_findings(
                config_overrides=config_overrides,
                assessment_run_arns=assessment_run_arns,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_rules_packages(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "capo_inspector.types.list_rules_packages_response.ListRulesPackagesResponse":
        """<p>Lists all available Amazon Inspector rules packages.</p>

        Args:
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListRulesPackages</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List rules packages
            Lists all available Amazon Inspector rules packages.

            >>> client.list_rules_packages(max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_rules_packages_request.ListRulesPackagesRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_rules_packages_response.ListRulesPackagesResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_rules_packages

            output, http_response = (
                capo_inspector._operations.inspector_service.list_rules_packages.list_rules_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_rules_packages_request.ListRulesPackagesRequest = {}
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

    def iter_list_rules_packages(
        self,
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.list_max_results.ListMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.list_rules_packages_response.ListRulesPackagesResponse]":
        _token = next_token
        while True:
            _response = self.list_rules_packages(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with an assessment template.</p>

        Args:
            resource_arn: <p>The ARN that specifies the assessment template whose tags you want to list.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List tags for resource
            Lists all tags associated with an assessment template.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-gcwFliYu')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_inspector._operations.inspector_service.list_tags_for_resource

            output, http_response = (
                capo_inspector._operations.inspector_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def preview_agents(
        self,
        preview_agents_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.preview_agents_max_results.PreviewAgentsMaxResults"
        ] = None,
    ) -> "capo_inspector.types.preview_agents_response.PreviewAgentsResponse":
        """<p>Previews the agents installed on the EC2 instances that are part of the specified assessment target.</p>

        Args:
            preview_agents_arn: <p>The ARN of the assessment target whose agents you want to preview.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>PreviewAgents</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_cross_account_role_exception.InvalidCrossAccountRoleException: <p>Amazon Inspector cannot assume the cross-account role that it needs to list your EC2 instances during the assessment run.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Preview agents
            Previews the agents installed on the EC2 instances that are part of the specified assessment target.

            >>> client.preview_agents(preview_agents_arn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq', max_results=123)
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.preview_agents_request.PreviewAgentsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.preview_agents_response.PreviewAgentsResponse"
        ]:
            import capo_inspector._operations.inspector_service.preview_agents

            output, http_response = (
                capo_inspector._operations.inspector_service.preview_agents.preview_agents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.preview_agents_request.PreviewAgentsRequest = {
            "preview_agents_arn": preview_agents_arn
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

    def iter_preview_agents(
        self,
        preview_agents_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        next_token: Optional[
            "capo_inspector.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_inspector.types.preview_agents_max_results.PreviewAgentsMaxResults"
        ] = None,
    ) -> "Iterator[capo_inspector.types.preview_agents_response.PreviewAgentsResponse]":
        _token = next_token
        while True:
            _response = self.preview_agents(
                preview_agents_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def register_cross_account_access_role(
        self,
        role_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> None:
        """<p>Registers the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments.</p>

        Args:
            role_arn: <p>The ARN of the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments. </p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_cross_account_role_exception.InvalidCrossAccountRoleException: <p>Amazon Inspector cannot assume the cross-account role that it needs to list your EC2 instances during the assessment run.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Register cross account access role
            Registers the IAM role that Amazon Inspector uses to list your EC2 instances at the start of the assessment run or when you call the PreviewAgents action.

            >>> client.register_cross_account_access_role(role_arn='arn:aws:iam::123456789012:role/inspector')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.register_cross_account_access_role_request.RegisterCrossAccountAccessRoleRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.register_cross_account_access_role

            output, http_response = (
                capo_inspector._operations.inspector_service.register_cross_account_access_role.register_cross_account_access_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.register_cross_account_access_role_request.RegisterCrossAccountAccessRoleRequest = {
            "role_arn": role_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_attributes_from_findings(
        self,
        finding_arns: "capo_inspector.types.add_remove_attributes_finding_arn_list.AddRemoveAttributesFindingArnList",
        attribute_keys: "capo_inspector.types.user_attribute_key_list.UserAttributeKeyList",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> "capo_inspector.types.remove_attributes_from_findings_response.RemoveAttributesFromFindingsResponse":
        """<p>Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.</p>

        Args:
            finding_arns: <p>The ARNs that specify the findings that you want to remove attributes from.</p>
            attribute_keys: <p>The array of attribute keys that you want to remove from specified findings.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove attributes from findings
            Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.

            >>> client.remove_attributes_from_findings(finding_arns=['arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU'], attribute_keys=['key=Example,value=example'])
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.remove_attributes_from_findings_request.RemoveAttributesFromFindingsRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.remove_attributes_from_findings_response.RemoveAttributesFromFindingsResponse"
        ]:
            import capo_inspector._operations.inspector_service.remove_attributes_from_findings

            output, http_response = (
                capo_inspector._operations.inspector_service.remove_attributes_from_findings.remove_attributes_from_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.remove_attributes_from_findings_request.RemoveAttributesFromFindingsRequest = {
            "finding_arns": finding_arns,
            "attribute_keys": attribute_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_tags_for_resource(
        self,
        resource_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        tags: Optional["capo_inspector.types.tag_list.TagList"] = None,
    ) -> None:
        """<p>Sets tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template.</p>

        Args:
            resource_arn: <p>The ARN of the assessment template that you want to set tags to.</p>
            tags: <p>A collection of key and value pairs that you want to set to the assessment template.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Set tags for resource
            Sets tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template.

            >>> client.set_tags_for_resource(resource_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0', tags=[{'key': 'Example', 'value': 'example'}])
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.set_tags_for_resource_request.SetTagsForResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.set_tags_for_resource

            output, http_response = (
                capo_inspector._operations.inspector_service.set_tags_for_resource.set_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.set_tags_for_resource_request.SetTagsForResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_assessment_run(
        self,
        assessment_template_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        assessment_run_name: Optional[
            "capo_inspector.types.assessment_run_name.AssessmentRunName"
        ] = None,
    ) -> (
        "capo_inspector.types.start_assessment_run_response.StartAssessmentRunResponse"
    ):
        """<p>Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.</p>

        Args:
            assessment_template_arn: <p>The ARN of the assessment template of the assessment run that you want to start.</p>
            assessment_run_name: <p>You can specify the name for the assessment run. The name must be unique for the assessment template whose ARN is used to start the assessment run.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.agents_already_running_assessment_exception.AgentsAlreadyRunningAssessmentException: <p>You started an assessment run, but one of the instances is already participating in another assessment run.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_cross_account_role_exception.InvalidCrossAccountRoleException: <p>Amazon Inspector cannot assume the cross-account role that it needs to list your EC2 instances during the assessment run.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current AWS account limits. The error code describes the limit exceeded.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Start assessment run
            Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.

            >>> client.start_assessment_run(assessment_template_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T', assessment_run_name='examplerun')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.start_assessment_run_request.StartAssessmentRunRequest]",
        ) -> OperationResponse[
            "capo_inspector.types.start_assessment_run_response.StartAssessmentRunResponse"
        ]:
            import capo_inspector._operations.inspector_service.start_assessment_run

            output, http_response = (
                capo_inspector._operations.inspector_service.start_assessment_run.start_assessment_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.start_assessment_run_request.StartAssessmentRunRequest = {
            "assessment_template_arn": assessment_template_arn
        }
        if assessment_run_name is not None:
            input_["assessment_run_name"] = assessment_run_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_assessment_run(
        self,
        assessment_run_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        stop_action: Optional["capo_inspector.types.stop_action.StopAction"] = None,
    ) -> None:
        """<p>Stops the assessment run that is specified by the ARN of the assessment run.</p>

        Args:
            assessment_run_arn: <p>The ARN of the assessment run that you want to stop.</p>
            stop_action: <p>An input option that can be set to either START_EVALUATION or SKIP_EVALUATION. START_EVALUATION (the default value), stops the AWS agent from collecting data and begins the results evaluation and the findings generation process. SKIP_EVALUATION cancels the assessment run immediately, after which no findings are generated.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Stop assessment run
            Stops the assessment run that is specified by the ARN of the assessment run.

            >>> client.stop_assessment_run(assessment_run_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.stop_assessment_run_request.StopAssessmentRunRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.stop_assessment_run

            output, http_response = (
                capo_inspector._operations.inspector_service.stop_assessment_run.stop_assessment_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.stop_assessment_run_request.StopAssessmentRunRequest = {
            "assessment_run_arn": assessment_run_arn
        }
        if stop_action is not None:
            input_["stop_action"] = stop_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def subscribe_to_event(
        self,
        resource_arn: "capo_inspector.types.arn.Arn",
        event: "capo_inspector.types.inspector_event.InspectorEvent",
        topic_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> None:
        """<p>Enables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.</p>

        Args:
            resource_arn: <p>The ARN of the assessment template that is used during the event for which you want to receive SNS notifications.</p>
            event: <p>The event for which you want to receive SNS notifications.</p>
            topic_arn: <p>The ARN of the SNS topic to which the SNS notifications are sent.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because it attempted to create resources beyond the current AWS account limits. The error code describes the limit exceeded.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Subscribe to event
            Enables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.

            >>> client.subscribe_to_event(resource_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0', event='ASSESSMENT_RUN_COMPLETED', topic_arn='arn:aws:sns:us-west-2:123456789012:exampletopic')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.subscribe_to_event_request.SubscribeToEventRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.subscribe_to_event

            output, http_response = (
                capo_inspector._operations.inspector_service.subscribe_to_event.subscribe_to_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.subscribe_to_event_request.SubscribeToEventRequest = {
            "resource_arn": resource_arn,
            "event": event,
            "topic_arn": topic_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def unsubscribe_from_event(
        self,
        resource_arn: "capo_inspector.types.arn.Arn",
        event: "capo_inspector.types.inspector_event.InspectorEvent",
        topic_arn: "capo_inspector.types.arn.Arn",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
    ) -> None:
        """<p>Disables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.</p>

        Args:
            resource_arn: <p>The ARN of the assessment template that is used during the event for which you want to stop receiving SNS notifications.</p>
            event: <p>The event for which you want to stop receiving SNS notifications.</p>
            topic_arn: <p>The ARN of the SNS topic to which SNS notifications are sent.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Unsubscribe from event
            Disables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.

            >>> client.unsubscribe_from_event(resource_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0', event='ASSESSMENT_RUN_COMPLETED', topic_arn='arn:aws:sns:us-west-2:123456789012:exampletopic')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.unsubscribe_from_event_request.UnsubscribeFromEventRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.unsubscribe_from_event

            output, http_response = (
                capo_inspector._operations.inspector_service.unsubscribe_from_event.unsubscribe_from_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.unsubscribe_from_event_request.UnsubscribeFromEventRequest = {
            "resource_arn": resource_arn,
            "event": event,
            "topic_arn": topic_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_assessment_target(
        self,
        assessment_target_arn: "capo_inspector.types.arn.Arn",
        assessment_target_name: "capo_inspector.types.assessment_target_name.AssessmentTargetName",
        *,
        config_overrides: Optional[InspectorClientConfig] = None,
        resource_group_arn: Optional["capo_inspector.types.arn.Arn"] = None,
    ) -> None:
        """<p>Updates the assessment target that is specified by the ARN of the assessment target.</p> <p>If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p>

        Args:
            assessment_target_arn: <p>The ARN of the assessment target that you want to update.</p>
            assessment_target_name: <p>The name of the assessment target that you want to update.</p>
            resource_group_arn: <p>The ARN of the resource group that is used to specify the new resource group to associate with the assessment target.</p>

        Raises:
            capo_inspector.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to access the requested resource.</p>
            capo_inspector.errors.internal_exception.InternalException: <p>Internal server error.</p>
            capo_inspector.errors.invalid_input_exception.InvalidInputException: <p>The request was rejected because an invalid or out-of-range value was supplied for an input parameter.</p>
            capo_inspector.errors.no_such_entity_exception.NoSuchEntityException: <p>The request was rejected because it referenced an entity that does not exist. The error code describes the entity.</p>
            capo_inspector.errors.service_temporarily_unavailable_exception.ServiceTemporarilyUnavailableException: <p>The serice is temporary unavailable.</p>
            capo_inspector.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update assessment target
            Updates the assessment target that is specified by the ARN of the assessment target.

            >>> client.update_assessment_target(assessment_target_arn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX', assessment_target_name='Example', resource_group_arn='arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-yNbgL5Pt')
        """

        def _handler(
            req: "OperationRequest[capo_inspector.types.update_assessment_target_request.UpdateAssessmentTargetRequest]",
        ) -> OperationResponse[None]:
            import capo_inspector._operations.inspector_service.update_assessment_target

            output, http_response = (
                capo_inspector._operations.inspector_service.update_assessment_target.update_assessment_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector.types.update_assessment_target_request.UpdateAssessmentTargetRequest = {
            "assessment_target_arn": assessment_target_arn,
            "assessment_target_name": assessment_target_name,
        }
        if resource_group_arn is not None:
            input_["resource_group_arn"] = resource_group_arn

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
