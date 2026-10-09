"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AwsResilienceHub``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_resiliencehub._auth._signers
import capo_resiliencehub._auth._sigv4
from capo_resiliencehub._auth._identity import Credentials
from capo_resiliencehub._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_resiliencehub._auth._zapros_handler import AuthMiddleware
from capo_resiliencehub._pagination import resolve_path as _resolve_path
from capo_resiliencehub._services._aws_config import aws_config
from capo_resiliencehub._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_resiliencehub.types.accept_grouping_recommendation_entries
    import capo_resiliencehub.types.accept_resource_grouping_recommendations_request
    import capo_resiliencehub.types.accept_resource_grouping_recommendations_response
    import capo_resiliencehub.types.add_draft_app_version_resource_mappings_request
    import capo_resiliencehub.types.add_draft_app_version_resource_mappings_response
    import capo_resiliencehub.types.additional_info_map
    import capo_resiliencehub.types.app_assessment_schedule_type
    import capo_resiliencehub.types.app_component_name_list
    import capo_resiliencehub.types.app_template_body
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.arn_list
    import capo_resiliencehub.types.assessment_invoker
    import capo_resiliencehub.types.assessment_status_list
    import capo_resiliencehub.types.aws_region
    import capo_resiliencehub.types.batch_update_recommendation_status_request
    import capo_resiliencehub.types.batch_update_recommendation_status_response
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.client_token
    import capo_resiliencehub.types.compliance_status
    import capo_resiliencehub.types.condition_list
    import capo_resiliencehub.types.create_app_request
    import capo_resiliencehub.types.create_app_response
    import capo_resiliencehub.types.create_app_version_app_component_request
    import capo_resiliencehub.types.create_app_version_app_component_response
    import capo_resiliencehub.types.create_app_version_resource_request
    import capo_resiliencehub.types.create_app_version_resource_response
    import capo_resiliencehub.types.create_recommendation_template_request
    import capo_resiliencehub.types.create_recommendation_template_response
    import capo_resiliencehub.types.create_resiliency_policy_request
    import capo_resiliencehub.types.create_resiliency_policy_response
    import capo_resiliencehub.types.customer_id
    import capo_resiliencehub.types.data_location_constraint
    import capo_resiliencehub.types.delete_app_assessment_request
    import capo_resiliencehub.types.delete_app_assessment_response
    import capo_resiliencehub.types.delete_app_input_source_request
    import capo_resiliencehub.types.delete_app_input_source_response
    import capo_resiliencehub.types.delete_app_request
    import capo_resiliencehub.types.delete_app_response
    import capo_resiliencehub.types.delete_app_version_app_component_request
    import capo_resiliencehub.types.delete_app_version_app_component_response
    import capo_resiliencehub.types.delete_app_version_resource_request
    import capo_resiliencehub.types.delete_app_version_resource_response
    import capo_resiliencehub.types.delete_recommendation_template_request
    import capo_resiliencehub.types.delete_recommendation_template_response
    import capo_resiliencehub.types.delete_resiliency_policy_request
    import capo_resiliencehub.types.delete_resiliency_policy_response
    import capo_resiliencehub.types.describe_app_assessment_request
    import capo_resiliencehub.types.describe_app_assessment_response
    import capo_resiliencehub.types.describe_app_request
    import capo_resiliencehub.types.describe_app_response
    import capo_resiliencehub.types.describe_app_version_app_component_request
    import capo_resiliencehub.types.describe_app_version_app_component_response
    import capo_resiliencehub.types.describe_app_version_request
    import capo_resiliencehub.types.describe_app_version_resource_request
    import capo_resiliencehub.types.describe_app_version_resource_response
    import capo_resiliencehub.types.describe_app_version_resources_resolution_status_request
    import capo_resiliencehub.types.describe_app_version_resources_resolution_status_response
    import capo_resiliencehub.types.describe_app_version_response
    import capo_resiliencehub.types.describe_app_version_template_request
    import capo_resiliencehub.types.describe_app_version_template_response
    import capo_resiliencehub.types.describe_draft_app_version_resources_import_status_request
    import capo_resiliencehub.types.describe_draft_app_version_resources_import_status_response
    import capo_resiliencehub.types.describe_metrics_export_request
    import capo_resiliencehub.types.describe_metrics_export_response
    import capo_resiliencehub.types.describe_resiliency_policy_request
    import capo_resiliencehub.types.describe_resiliency_policy_response
    import capo_resiliencehub.types.describe_resource_grouping_recommendation_task_request
    import capo_resiliencehub.types.describe_resource_grouping_recommendation_task_response
    import capo_resiliencehub.types.disruption_policy
    import capo_resiliencehub.types.eks_source_cluster_namespace
    import capo_resiliencehub.types.eks_source_list
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.entity_name_list
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.event_subscription_list
    import capo_resiliencehub.types.field_list
    import capo_resiliencehub.types.grouping_recommendation
    import capo_resiliencehub.types.import_resources_to_draft_app_version_request
    import capo_resiliencehub.types.import_resources_to_draft_app_version_response
    import capo_resiliencehub.types.list_alarm_recommendations_request
    import capo_resiliencehub.types.list_alarm_recommendations_response
    import capo_resiliencehub.types.list_app_assessment_compliance_drifts_request
    import capo_resiliencehub.types.list_app_assessment_compliance_drifts_response
    import capo_resiliencehub.types.list_app_assessment_resource_drifts_request
    import capo_resiliencehub.types.list_app_assessment_resource_drifts_response
    import capo_resiliencehub.types.list_app_assessments_request
    import capo_resiliencehub.types.list_app_assessments_response
    import capo_resiliencehub.types.list_app_component_compliances_request
    import capo_resiliencehub.types.list_app_component_compliances_response
    import capo_resiliencehub.types.list_app_component_recommendations_request
    import capo_resiliencehub.types.list_app_component_recommendations_response
    import capo_resiliencehub.types.list_app_input_sources_request
    import capo_resiliencehub.types.list_app_input_sources_response
    import capo_resiliencehub.types.list_app_version_app_components_request
    import capo_resiliencehub.types.list_app_version_app_components_response
    import capo_resiliencehub.types.list_app_version_resource_mappings_request
    import capo_resiliencehub.types.list_app_version_resource_mappings_response
    import capo_resiliencehub.types.list_app_version_resources_request
    import capo_resiliencehub.types.list_app_version_resources_response
    import capo_resiliencehub.types.list_app_versions_request
    import capo_resiliencehub.types.list_app_versions_response
    import capo_resiliencehub.types.list_apps_request
    import capo_resiliencehub.types.list_apps_response
    import capo_resiliencehub.types.list_metrics_request
    import capo_resiliencehub.types.list_metrics_response
    import capo_resiliencehub.types.list_recommendation_templates_request
    import capo_resiliencehub.types.list_recommendation_templates_response
    import capo_resiliencehub.types.list_resiliency_policies_request
    import capo_resiliencehub.types.list_resiliency_policies_response
    import capo_resiliencehub.types.list_resource_grouping_recommendations_request
    import capo_resiliencehub.types.list_resource_grouping_recommendations_response
    import capo_resiliencehub.types.list_sop_recommendations_request
    import capo_resiliencehub.types.list_sop_recommendations_response
    import capo_resiliencehub.types.list_suggested_resiliency_policies_request
    import capo_resiliencehub.types.list_suggested_resiliency_policies_response
    import capo_resiliencehub.types.list_tags_for_resource_request
    import capo_resiliencehub.types.list_tags_for_resource_response
    import capo_resiliencehub.types.list_test_recommendations_request
    import capo_resiliencehub.types.list_test_recommendations_response
    import capo_resiliencehub.types.list_unsupported_app_version_resources_request
    import capo_resiliencehub.types.list_unsupported_app_version_resources_response
    import capo_resiliencehub.types.logical_resource_id
    import capo_resiliencehub.types.max_results
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.permission_model
    import capo_resiliencehub.types.publish_app_version_request
    import capo_resiliencehub.types.publish_app_version_response
    import capo_resiliencehub.types.put_draft_app_version_template_request
    import capo_resiliencehub.types.put_draft_app_version_template_response
    import capo_resiliencehub.types.recommendation_id_list
    import capo_resiliencehub.types.recommendation_template_status_list
    import capo_resiliencehub.types.reject_grouping_recommendation_entries
    import capo_resiliencehub.types.reject_resource_grouping_recommendations_request
    import capo_resiliencehub.types.reject_resource_grouping_recommendations_response
    import capo_resiliencehub.types.remove_draft_app_version_resource_mappings_request
    import capo_resiliencehub.types.remove_draft_app_version_resource_mappings_response
    import capo_resiliencehub.types.render_recommendation_type_list
    import capo_resiliencehub.types.resiliency_policy_tier
    import capo_resiliencehub.types.resolve_app_version_resources_request
    import capo_resiliencehub.types.resolve_app_version_resources_response
    import capo_resiliencehub.types.resource_drift
    import capo_resiliencehub.types.resource_import_strategy_type
    import capo_resiliencehub.types.resource_mapping_list
    import capo_resiliencehub.types.row
    import capo_resiliencehub.types.sort_list
    import capo_resiliencehub.types.start_app_assessment_request
    import capo_resiliencehub.types.start_app_assessment_response
    import capo_resiliencehub.types.start_metrics_export_request
    import capo_resiliencehub.types.start_metrics_export_response
    import capo_resiliencehub.types.start_resource_grouping_recommendation_task_request
    import capo_resiliencehub.types.start_resource_grouping_recommendation_task_response
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.string255_list
    import capo_resiliencehub.types.string2048
    import capo_resiliencehub.types.tag_key_list
    import capo_resiliencehub.types.tag_map
    import capo_resiliencehub.types.tag_resource_request
    import capo_resiliencehub.types.tag_resource_response
    import capo_resiliencehub.types.template_format
    import capo_resiliencehub.types.terraform_source
    import capo_resiliencehub.types.terraform_source_list
    import capo_resiliencehub.types.time_stamp
    import capo_resiliencehub.types.untag_resource_request
    import capo_resiliencehub.types.untag_resource_response
    import capo_resiliencehub.types.update_app_request
    import capo_resiliencehub.types.update_app_response
    import capo_resiliencehub.types.update_app_version_app_component_request
    import capo_resiliencehub.types.update_app_version_app_component_response
    import capo_resiliencehub.types.update_app_version_request
    import capo_resiliencehub.types.update_app_version_resource_request
    import capo_resiliencehub.types.update_app_version_resource_response
    import capo_resiliencehub.types.update_app_version_response
    import capo_resiliencehub.types.update_recommendation_status_request_entries
    import capo_resiliencehub.types.update_resiliency_policy_request
    import capo_resiliencehub.types.update_resiliency_policy_response


class resiliencehubClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class resiliencehubClient:
    """A client for the ``resiliencehub`` service.

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
        self._config = resiliencehubClientConfig(
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
        self, config_overrides: Optional[resiliencehubClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: resiliencehubClientConfig = config_overrides or {}
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

    def accept_resource_grouping_recommendations(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        entries: "capo_resiliencehub.types.accept_grouping_recommendation_entries.AcceptGroupingRecommendationEntries",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.accept_resource_grouping_recommendations_response.AcceptResourceGroupingRecommendationsResponse":
        """<p>Accepts the resource grouping recommendations suggested by Resilience Hub for your application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            entries: <p>List of resource grouping recommendations you want to include in your application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.accept_resource_grouping_recommendations_request.AcceptResourceGroupingRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.accept_resource_grouping_recommendations_response.AcceptResourceGroupingRecommendationsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.accept_resource_grouping_recommendations

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.accept_resource_grouping_recommendations.accept_resource_grouping_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.accept_resource_grouping_recommendations_request.AcceptResourceGroupingRecommendationsRequest = {
            "app_arn": app_arn,
            "entries": entries,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_draft_app_version_resource_mappings(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        resource_mappings: "capo_resiliencehub.types.resource_mapping_list.ResourceMappingList",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.add_draft_app_version_resource_mappings_response.AddDraftAppVersionResourceMappingsResponse":
        """<p>Adds the source of resource-maps to the draft version of an application. During assessment, Resilience Hub will use these resource-maps to resolve the latest physical ID for each resource in the application template. For more information about different types of resources supported by Resilience Hub and how to add them in your application, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/how-app-manage.html">Step 2: How is your application managed?</a> in the Resilience Hub User Guide.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            resource_mappings: <p>Mappings used to map logical resources from the template to physical resources. You can use the mapping type <code>CFN_STACK</code> if the application template uses a logical stack name. Or you can map individual resources by using the mapping type <code>RESOURCE</code>. We recommend using the mapping type <code>CFN_STACK</code> if the application is backed by a CloudFormation stack.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.add_draft_app_version_resource_mappings_request.AddDraftAppVersionResourceMappingsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.add_draft_app_version_resource_mappings_response.AddDraftAppVersionResourceMappingsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.add_draft_app_version_resource_mappings

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.add_draft_app_version_resource_mappings.add_draft_app_version_resource_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.add_draft_app_version_resource_mappings_request.AddDraftAppVersionResourceMappingsRequest = {
            "app_arn": app_arn,
            "resource_mappings": resource_mappings,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_recommendation_status(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        request_entries: "capo_resiliencehub.types.update_recommendation_status_request_entries.UpdateRecommendationStatusRequestEntries",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.batch_update_recommendation_status_response.BatchUpdateRecommendationStatusResponse":
        """<p>Enables you to include or exclude one or more operational recommendations.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            request_entries: <p>Defines the list of operational recommendations that need to be included or excluded.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.batch_update_recommendation_status_request.BatchUpdateRecommendationStatusRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.batch_update_recommendation_status_response.BatchUpdateRecommendationStatusResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.batch_update_recommendation_status

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.batch_update_recommendation_status.batch_update_recommendation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.batch_update_recommendation_status_request.BatchUpdateRecommendationStatusRequest = {
            "app_arn": app_arn,
            "request_entries": request_entries,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_app(
        self,
        name: "capo_resiliencehub.types.entity_name.EntityName",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        description: Optional[
            "capo_resiliencehub.types.entity_description.EntityDescription"
        ] = None,
        policy_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        tags: Optional["capo_resiliencehub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
        assessment_schedule: Optional[
            "capo_resiliencehub.types.app_assessment_schedule_type.AppAssessmentScheduleType"
        ] = None,
        permission_model: Optional[
            "capo_resiliencehub.types.permission_model.PermissionModel"
        ] = None,
        event_subscriptions: Optional[
            "capo_resiliencehub.types.event_subscription_list.EventSubscriptionList"
        ] = None,
        aws_application_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
    ) -> "capo_resiliencehub.types.create_app_response.CreateAppResponse":
        """<p>Creates an Resilience Hub application. An Resilience Hub application is a collection of Amazon Web Services resources structured to prevent and recover Amazon Web Services application disruptions. To describe a Resilience Hub application, you provide an application name, resources from one or more CloudFormation stacks, Resource Groups, Terraform state files, AppRegistry applications, and an appropriate resiliency policy. In addition, you can also add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters as optional resources. For more information about the number of resources supported per application, see <a href="https://docs.aws.amazon.com/general/latest/gr/resiliencehub.html#limits_resiliencehub">Service quotas</a>.</p> <p>After you create an Resilience Hub application, you publish it so that you can run a resiliency assessment on it. You can then use recommendations from the assessment to improve resiliency by running another assessment, comparing results, and then iterating the process until you achieve your goals for recovery time objective (RTO) and recovery point objective (RPO).</p>

        Args:
            name: <p>Name of the application.</p>
            description: <p>The optional description for an app.</p>
            policy_arn: <p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            tags: <p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>
            assessment_schedule: <p> Assessment execution schedule with 'Daily' or 'Disabled' values. </p>
            permission_model: <p>Defines the roles and credentials that Resilience Hub would use while creating the application, importing its resources, and running an assessment.</p>
            event_subscriptions: <p>The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports only <b>Drift detected</b> and <b>Scheduled assessment failure</b> events notification.</p>
            aws_application_arn: <p>Amazon Resource Name (ARN) of Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.create_app_request.CreateAppRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.create_app_response.CreateAppResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.create_app

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.create_app.create_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.create_app_request.CreateAppRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if assessment_schedule is not None:
            input_["assessment_schedule"] = assessment_schedule
        if permission_model is not None:
            input_["permission_model"] = permission_model
        if event_subscriptions is not None:
            input_["event_subscriptions"] = event_subscriptions
        if aws_application_arn is not None:
            input_["aws_application_arn"] = aws_application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_app_version_app_component(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        name: "capo_resiliencehub.types.string255.String255",
        type: "capo_resiliencehub.types.string255.String255",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        id: Optional["capo_resiliencehub.types.string255.String255"] = None,
        additional_info: Optional[
            "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
        ] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.create_app_version_app_component_response.CreateAppVersionAppComponentResponse":
        """<p>Creates a new Application Component in the Resilience Hub application.</p> <note> <p>This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the <code>PublishAppVersion</code> API.</p> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            id: <p>Identifier of the Application Component.</p>
            name: <p>Name of the Application Component.</p>
            type: <p>Type of Application Component. For more information about the types of Application Component, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html">Grouping resources in an AppComponent</a>.</p>
            additional_info: <p>Currently, there is no supported additional information for Application Components.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.create_app_version_app_component_request.CreateAppVersionAppComponentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.create_app_version_app_component_response.CreateAppVersionAppComponentResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.create_app_version_app_component

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.create_app_version_app_component.create_app_version_app_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.create_app_version_app_component_request.CreateAppVersionAppComponentRequest = {
            "app_arn": app_arn,
            "name": name,
            "type": type,
        }
        if id is not None:
            input_["id"] = id
        if additional_info is not None:
            input_["additional_info"] = additional_info
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

    def create_app_version_resource(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        logical_resource_id: "capo_resiliencehub.types.logical_resource_id.LogicalResourceId",
        physical_resource_id: "capo_resiliencehub.types.string2048.String2048",
        resource_type: "capo_resiliencehub.types.string255.String255",
        app_components: "capo_resiliencehub.types.app_component_name_list.AppComponentNameList",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resource_name: Optional[
            "capo_resiliencehub.types.entity_name.EntityName"
        ] = None,
        aws_region: Optional["capo_resiliencehub.types.aws_region.AwsRegion"] = None,
        aws_account_id: Optional[
            "capo_resiliencehub.types.customer_id.CustomerId"
        ] = None,
        additional_info: Optional[
            "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
        ] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.create_app_version_resource_response.CreateAppVersionResourceResponse":
        """<p>Adds a resource to the Resilience Hub application and assigns it to the specified Application Components. If you specify a new Application Component, Resilience Hub will automatically create the Application Component.</p> <note> <ul> <li> <p>This action has no effect outside Resilience Hub.</p> </li> <li> <p>This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the <code>PublishAppVersion</code> API.</p> </li> <li> <p>To update application version with new <code>physicalResourceID</code>, you must call <code>ResolveAppVersionResources</code> API.</p> </li> </ul> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            resource_name: <p>Name of the resource.</p>
            logical_resource_id: <p>Logical identifier of the resource.</p>
            physical_resource_id: <p>Physical identifier of the resource.</p>
            aws_region: <p>Amazon Web Services region that owns the physical resource.</p>
            aws_account_id: <p>Amazon Web Services account that owns the physical resource.</p>
            resource_type: <p>Type of resource.</p>
            app_components: <p>List of Application Components that this resource belongs to. If an Application Component is not part of the Resilience Hub application, it will be added.</p>
            additional_info: <p>Currently, there is no supported additional information for resources.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.create_app_version_resource_request.CreateAppVersionResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.create_app_version_resource_response.CreateAppVersionResourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.create_app_version_resource

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.create_app_version_resource.create_app_version_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.create_app_version_resource_request.CreateAppVersionResourceRequest = {
            "app_arn": app_arn,
            "logical_resource_id": logical_resource_id,
            "physical_resource_id": physical_resource_id,
            "resource_type": resource_type,
            "app_components": app_components,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if additional_info is not None:
            input_["additional_info"] = additional_info
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

    def create_recommendation_template(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        name: "capo_resiliencehub.types.entity_name.EntityName",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        recommendation_ids: Optional[
            "capo_resiliencehub.types.recommendation_id_list.RecommendationIdList"
        ] = None,
        format: Optional[
            "capo_resiliencehub.types.template_format.TemplateFormat"
        ] = None,
        recommendation_types: Optional[
            "capo_resiliencehub.types.render_recommendation_type_list.RenderRecommendationTypeList"
        ] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_resiliencehub.types.tag_map.TagMap"] = None,
        bucket_name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
    ) -> "capo_resiliencehub.types.create_recommendation_template_response.CreateRecommendationTemplateResponse":
        """<p>Creates a new recommendation template for the Resilience Hub application.</p>

        Args:
            recommendation_ids: <p>Identifiers for the recommendations used to create a recommendation template.</p>
            format: <p>The format for the recommendation template.</p> <dl> <dt>CfnJson</dt> <dd> <p>The template is CloudFormation JSON.</p> </dd> <dt>CfnYaml</dt> <dd> <p>The template is CloudFormation YAML.</p> </dd> </dl>
            recommendation_types: <p>An array of strings that specify the recommendation template type or types.</p> <dl> <dt>Alarm</dt> <dd> <p>The template is an <a>AlarmRecommendation</a> template.</p> </dd> <dt>Sop</dt> <dd> <p>The template is a <a>SopRecommendation</a> template.</p> </dd> <dt>Test</dt> <dd> <p>The template is a <a>TestRecommendation</a> template.</p> </dd> </dl>
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            name: <p>The name for the recommendation template.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>
            tags: <p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>
            bucket_name: <p>The name of the Amazon S3 bucket that will contain the recommendation template.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.create_recommendation_template_request.CreateRecommendationTemplateRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.create_recommendation_template_response.CreateRecommendationTemplateResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.create_recommendation_template

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.create_recommendation_template.create_recommendation_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.create_recommendation_template_request.CreateRecommendationTemplateRequest = {
            "assessment_arn": assessment_arn,
            "name": name,
        }
        if recommendation_ids is not None:
            input_["recommendation_ids"] = recommendation_ids
        if format is not None:
            input_["format"] = format
        if recommendation_types is not None:
            input_["recommendation_types"] = recommendation_types
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if bucket_name is not None:
            input_["bucket_name"] = bucket_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_resiliency_policy(
        self,
        policy_name: "capo_resiliencehub.types.entity_name.EntityName",
        tier: "capo_resiliencehub.types.resiliency_policy_tier.ResiliencyPolicyTier",
        policy: "capo_resiliencehub.types.disruption_policy.DisruptionPolicy",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        policy_description: Optional[
            "capo_resiliencehub.types.entity_description.EntityDescription"
        ] = None,
        data_location_constraint: Optional[
            "capo_resiliencehub.types.data_location_constraint.DataLocationConstraint"
        ] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_resiliencehub.types.tag_map.TagMap"] = None,
    ) -> "capo_resiliencehub.types.create_resiliency_policy_response.CreateResiliencyPolicyResponse":
        """<p>Creates a resiliency policy for an application.</p> <note> <p>Resilience Hub allows you to provide a value of zero for <code>rtoInSecs</code> and <code>rpoInSecs</code> of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for <code>rtoInSecs</code> and <code>rpoInSecs</code>, the estimated workload RTO and estimated workload RPO result will be near zero and the <b>Compliance status</b> for your application will be set to <b>Policy breached</b>.</p> </note>

        Args:
            policy_name: <p>Name of the resiliency policy.</p>
            policy_description: <p>Description of the resiliency policy.</p>
            data_location_constraint: <p>Specifies a high-level geographical location constraint for where your resilience policy data can be stored.</p>
            tier: <p>The tier for this resiliency policy, ranging from the highest severity (<code>MissionCritical</code>) to lowest (<code>NonCritical</code>).</p>
            policy: <p>The type of resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>
            tags: <p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.create_resiliency_policy_request.CreateResiliencyPolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.create_resiliency_policy_response.CreateResiliencyPolicyResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.create_resiliency_policy

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.create_resiliency_policy.create_resiliency_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.create_resiliency_policy_request.CreateResiliencyPolicyRequest = {
            "policy_name": policy_name,
            "tier": tier,
            "policy": policy,
        }
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if data_location_constraint is not None:
            input_["data_location_constraint"] = data_location_constraint
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_app(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        force_delete: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.delete_app_response.DeleteAppResponse":
        """<p>Deletes an Resilience Hub application. This is a destructive action that can't be undone.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            force_delete: <p>A boolean option to force the deletion of an Resilience Hub application. </p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.delete_app_request.DeleteAppRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.delete_app_response.DeleteAppResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.delete_app

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.delete_app.delete_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.delete_app_request.DeleteAppRequest = {
            "app_arn": app_arn
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete
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

    def delete_app_assessment(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.delete_app_assessment_response.DeleteAppAssessmentResponse":
        """<p>Deletes an Resilience Hub application assessment. This is a destructive action that can't be undone.</p>

        Args:
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.delete_app_assessment_request.DeleteAppAssessmentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.delete_app_assessment_response.DeleteAppAssessmentResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.delete_app_assessment

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.delete_app_assessment.delete_app_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.delete_app_assessment_request.DeleteAppAssessmentRequest = {
            "assessment_arn": assessment_arn
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

    def delete_app_input_source(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        source_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        terraform_source: Optional[
            "capo_resiliencehub.types.terraform_source.TerraformSource"
        ] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
        eks_source_cluster_namespace: Optional[
            "capo_resiliencehub.types.eks_source_cluster_namespace.EksSourceClusterNamespace"
        ] = None,
    ) -> "capo_resiliencehub.types.delete_app_input_source_response.DeleteAppInputSourceResponse":
        """<p>Deletes the input source and all of its imported resources from the Resilience Hub application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            source_arn: <p>The Amazon Resource Name (ARN) of the imported resource you want to remove from the Resilience Hub application. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            terraform_source: <p>The imported Terraform s3 state ﬁle you want to remove from the Resilience Hub application.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>
            eks_source_cluster_namespace: <p>The namespace on your Amazon Elastic Kubernetes Service cluster that you want to delete from the Resilience Hub application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.delete_app_input_source_request.DeleteAppInputSourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.delete_app_input_source_response.DeleteAppInputSourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.delete_app_input_source

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.delete_app_input_source.delete_app_input_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.delete_app_input_source_request.DeleteAppInputSourceRequest = {
            "app_arn": app_arn
        }
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if terraform_source is not None:
            input_["terraform_source"] = terraform_source
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if eks_source_cluster_namespace is not None:
            input_["eks_source_cluster_namespace"] = eks_source_cluster_namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_app_version_app_component(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        id: "capo_resiliencehub.types.string255.String255",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.delete_app_version_app_component_response.DeleteAppVersionAppComponentResponse":
        """<p>Deletes an Application Component from the Resilience Hub application.</p> <note> <ul> <li> <p>This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the <code>PublishAppVersion</code> API.</p> </li> <li> <p>You will not be able to delete an Application Component if it has resources associated with it.</p> </li> </ul> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            id: <p>Identifier of the Application Component.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.delete_app_version_app_component_request.DeleteAppVersionAppComponentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.delete_app_version_app_component_response.DeleteAppVersionAppComponentResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.delete_app_version_app_component

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.delete_app_version_app_component.delete_app_version_app_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.delete_app_version_app_component_request.DeleteAppVersionAppComponentRequest = {
            "app_arn": app_arn,
            "id": id,
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

    def delete_app_version_resource(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resource_name: Optional[
            "capo_resiliencehub.types.entity_name.EntityName"
        ] = None,
        logical_resource_id: Optional[
            "capo_resiliencehub.types.logical_resource_id.LogicalResourceId"
        ] = None,
        physical_resource_id: Optional[
            "capo_resiliencehub.types.string2048.String2048"
        ] = None,
        aws_region: Optional["capo_resiliencehub.types.aws_region.AwsRegion"] = None,
        aws_account_id: Optional[
            "capo_resiliencehub.types.customer_id.CustomerId"
        ] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.delete_app_version_resource_response.DeleteAppVersionResourceResponse":
        """<p>Deletes a resource from the Resilience Hub application.</p> <note> <ul> <li> <p>You can only delete a manually added resource. To exclude non-manually added resources, use the <code>UpdateAppVersionResource</code> API.</p> </li> <li> <p>This action has no effect outside Resilience Hub.</p> </li> <li> <p>This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the <code>PublishAppVersion</code> API.</p> </li> </ul> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            resource_name: <p>Name of the resource.</p>
            logical_resource_id: <p>Logical identifier of the resource.</p>
            physical_resource_id: <p>Physical identifier of the resource.</p>
            aws_region: <p>Amazon Web Services region that owns the physical resource.</p>
            aws_account_id: <p>Amazon Web Services account that owns the physical resource.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.delete_app_version_resource_request.DeleteAppVersionResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.delete_app_version_resource_response.DeleteAppVersionResourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.delete_app_version_resource

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.delete_app_version_resource.delete_app_version_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.delete_app_version_resource_request.DeleteAppVersionResourceRequest = {
            "app_arn": app_arn
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id
        if physical_resource_id is not None:
            input_["physical_resource_id"] = physical_resource_id
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
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

    def delete_recommendation_template(
        self,
        recommendation_template_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.delete_recommendation_template_response.DeleteRecommendationTemplateResponse":
        """<p>Deletes a recommendation template. This is a destructive action that can't be undone.</p>

        Args:
            recommendation_template_arn: <p>The Amazon Resource Name (ARN) for a recommendation template.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.delete_recommendation_template_request.DeleteRecommendationTemplateRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.delete_recommendation_template_response.DeleteRecommendationTemplateResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.delete_recommendation_template

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.delete_recommendation_template.delete_recommendation_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.delete_recommendation_template_request.DeleteRecommendationTemplateRequest = {
            "recommendation_template_arn": recommendation_template_arn
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

    def delete_resiliency_policy(
        self,
        policy_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.delete_resiliency_policy_response.DeleteResiliencyPolicyResponse":
        """<p>Deletes a resiliency policy. This is a destructive action that can't be undone.</p>

        Args:
            policy_arn: <p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.delete_resiliency_policy_request.DeleteResiliencyPolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.delete_resiliency_policy_response.DeleteResiliencyPolicyResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.delete_resiliency_policy

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.delete_resiliency_policy.delete_resiliency_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.delete_resiliency_policy_request.DeleteResiliencyPolicyRequest = {
            "policy_arn": policy_arn
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

    def describe_app(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_app_response.DescribeAppResponse":
        """<p>Describes an Resilience Hub application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_app_request.DescribeAppRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_app_response.DescribeAppResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_app

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_app.describe_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_app_request.DescribeAppRequest = {
            "app_arn": app_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_app_assessment(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_app_assessment_response.DescribeAppAssessmentResponse":
        """<p>Describes an assessment for an Resilience Hub application.</p>

        Args:
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_app_assessment_request.DescribeAppAssessmentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_app_assessment_response.DescribeAppAssessmentResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_app_assessment

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_app_assessment.describe_app_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_app_assessment_request.DescribeAppAssessmentRequest = {
            "assessment_arn": assessment_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_app_version(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_app_version_response.DescribeAppVersionResponse":
        """<p>Describes the Resilience Hub application version.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>Resilience Hub application version.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_app_version_request.DescribeAppVersionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_app_version_response.DescribeAppVersionResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_app_version

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_app_version.describe_app_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_app_version_request.DescribeAppVersionRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_app_version_app_component(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        id: "capo_resiliencehub.types.string255.String255",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_app_version_app_component_response.DescribeAppVersionAppComponentResponse":
        """<p>Describes an Application Component in the Resilience Hub application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>Resilience Hub application version.</p>
            id: <p>Identifier of the Application Component.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_app_version_app_component_request.DescribeAppVersionAppComponentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_app_version_app_component_response.DescribeAppVersionAppComponentResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_app_component

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_app_component.describe_app_version_app_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_app_version_app_component_request.DescribeAppVersionAppComponentRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_app_version_resource(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resource_name: Optional[
            "capo_resiliencehub.types.entity_name.EntityName"
        ] = None,
        logical_resource_id: Optional[
            "capo_resiliencehub.types.logical_resource_id.LogicalResourceId"
        ] = None,
        physical_resource_id: Optional[
            "capo_resiliencehub.types.string2048.String2048"
        ] = None,
        aws_region: Optional["capo_resiliencehub.types.aws_region.AwsRegion"] = None,
        aws_account_id: Optional[
            "capo_resiliencehub.types.customer_id.CustomerId"
        ] = None,
    ) -> "capo_resiliencehub.types.describe_app_version_resource_response.DescribeAppVersionResourceResponse":
        """<p>Describes a resource of the Resilience Hub application.</p> <note> <p>This API accepts only one of the following parameters to describe the resource:</p> <ul> <li> <p> <code>resourceName</code> </p> </li> <li> <p> <code>logicalResourceId</code> </p> </li> <li> <p> <code>physicalResourceId</code> (Along with <code>physicalResourceId</code>, you can also provide <code>awsAccountId</code>, and <code>awsRegion</code>)</p> </li> </ul> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>Resilience Hub application version.</p>
            resource_name: <p>Name of the resource.</p>
            logical_resource_id: <p>Logical identifier of the resource.</p>
            physical_resource_id: <p>Physical identifier of the resource.</p>
            aws_region: <p>Amazon Web Services region that owns the physical resource.</p>
            aws_account_id: <p>Amazon Web Services account that owns the physical resource.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_app_version_resource_request.DescribeAppVersionResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_app_version_resource_response.DescribeAppVersionResourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_resource

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_resource.describe_app_version_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_app_version_resource_request.DescribeAppVersionResourceRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id
        if physical_resource_id is not None:
            input_["physical_resource_id"] = physical_resource_id
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_app_version_resources_resolution_status(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resolution_id: Optional["capo_resiliencehub.types.string255.String255"] = None,
    ) -> "capo_resiliencehub.types.describe_app_version_resources_resolution_status_response.DescribeAppVersionResourcesResolutionStatusResponse":
        """<p>Returns the resolution status for the specified resolution identifier for an application version. If <code>resolutionId</code> is not specified, the current resolution status is returned.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>The version of the application.</p>
            resolution_id: <p>The identifier for a specific resolution.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_app_version_resources_resolution_status_request.DescribeAppVersionResourcesResolutionStatusRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_app_version_resources_resolution_status_response.DescribeAppVersionResourcesResolutionStatusResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_resources_resolution_status

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_resources_resolution_status.describe_app_version_resources_resolution_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_app_version_resources_resolution_status_request.DescribeAppVersionResourcesResolutionStatusRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
        }
        if resolution_id is not None:
            input_["resolution_id"] = resolution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_app_version_template(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_app_version_template_response.DescribeAppVersionTemplateResponse":
        """<p>Describes details about an Resilience Hub application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>The version of the application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_app_version_template_request.DescribeAppVersionTemplateRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_app_version_template_response.DescribeAppVersionTemplateResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_template

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_app_version_template.describe_app_version_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_app_version_template_request.DescribeAppVersionTemplateRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_draft_app_version_resources_import_status(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_draft_app_version_resources_import_status_response.DescribeDraftAppVersionResourcesImportStatusResponse":
        """<p>Describes the status of importing resources to an application version.</p> <note> <p>If you get a 404 error with <code>ResourceImportStatusNotFoundAppMetadataException</code>, you must call <code>importResourcesToDraftAppVersion</code> after creating the application and before calling <code>describeDraftAppVersionResourcesImportStatus</code> to obtain the status.</p> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_draft_app_version_resources_import_status_request.DescribeDraftAppVersionResourcesImportStatusRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_draft_app_version_resources_import_status_response.DescribeDraftAppVersionResourcesImportStatusResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_draft_app_version_resources_import_status

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_draft_app_version_resources_import_status.describe_draft_app_version_resources_import_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_draft_app_version_resources_import_status_request.DescribeDraftAppVersionResourcesImportStatusRequest = {
            "app_arn": app_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_metrics_export(
        self,
        metrics_export_id: "capo_resiliencehub.types.string255.String255",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_metrics_export_response.DescribeMetricsExportResponse":
        """<p>Describes the metrics of the application configuration being exported.</p>

        Args:
            metrics_export_id: <p>Identifier of the metrics export task.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_metrics_export_request.DescribeMetricsExportRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_metrics_export_response.DescribeMetricsExportResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_metrics_export

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_metrics_export.describe_metrics_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_metrics_export_request.DescribeMetricsExportRequest = {
            "metrics_export_id": metrics_export_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_resiliency_policy(
        self,
        policy_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.describe_resiliency_policy_response.DescribeResiliencyPolicyResponse":
        """<p>Describes a specified resiliency policy for an Resilience Hub application. The returned policy object includes creation time, data location constraints, the Amazon Resource Name (ARN) for the policy, tags, tier, and more.</p>

        Args:
            policy_arn: <p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_resiliency_policy_request.DescribeResiliencyPolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_resiliency_policy_response.DescribeResiliencyPolicyResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_resiliency_policy

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_resiliency_policy.describe_resiliency_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_resiliency_policy_request.DescribeResiliencyPolicyRequest = {
            "policy_arn": policy_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_resource_grouping_recommendation_task(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        grouping_id: Optional["capo_resiliencehub.types.string255.String255"] = None,
    ) -> "capo_resiliencehub.types.describe_resource_grouping_recommendation_task_response.DescribeResourceGroupingRecommendationTaskResponse":
        """<p>Describes the resource grouping recommendation tasks run by Resilience Hub for your application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            grouping_id: <p>Identifier of the grouping recommendation task.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.describe_resource_grouping_recommendation_task_request.DescribeResourceGroupingRecommendationTaskRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.describe_resource_grouping_recommendation_task_response.DescribeResourceGroupingRecommendationTaskResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.describe_resource_grouping_recommendation_task

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.describe_resource_grouping_recommendation_task.describe_resource_grouping_recommendation_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.describe_resource_grouping_recommendation_task_request.DescribeResourceGroupingRecommendationTaskRequest = {
            "app_arn": app_arn
        }
        if grouping_id is not None:
            input_["grouping_id"] = grouping_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_resources_to_draft_app_version(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        source_arns: Optional["capo_resiliencehub.types.arn_list.ArnList"] = None,
        terraform_sources: Optional[
            "capo_resiliencehub.types.terraform_source_list.TerraformSourceList"
        ] = None,
        import_strategy: Optional[
            "capo_resiliencehub.types.resource_import_strategy_type.ResourceImportStrategyType"
        ] = None,
        eks_sources: Optional[
            "capo_resiliencehub.types.eks_source_list.EksSourceList"
        ] = None,
    ) -> "capo_resiliencehub.types.import_resources_to_draft_app_version_response.ImportResourcesToDraftAppVersionResponse":
        """<p>Imports resources to Resilience Hub application draft version from different input sources. For more information about the input sources supported by Resilience Hub, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html">Discover the structure and describe your Resilience Hub application</a>.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            source_arns: <p>The Amazon Resource Names (ARNs) for the resources.</p>
            terraform_sources: <p> A list of terraform file s3 URLs you need to import. </p>
            import_strategy: <p>The import strategy you would like to set to import resources into Resilience Hub application.</p>
            eks_sources: <p>The input sources of the Amazon Elastic Kubernetes Service resources you need to import.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.import_resources_to_draft_app_version_request.ImportResourcesToDraftAppVersionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.import_resources_to_draft_app_version_response.ImportResourcesToDraftAppVersionResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.import_resources_to_draft_app_version

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.import_resources_to_draft_app_version.import_resources_to_draft_app_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.import_resources_to_draft_app_version_request.ImportResourcesToDraftAppVersionRequest = {
            "app_arn": app_arn
        }
        if source_arns is not None:
            input_["source_arns"] = source_arns
        if terraform_sources is not None:
            input_["terraform_sources"] = terraform_sources
        if import_strategy is not None:
            input_["import_strategy"] = import_strategy
        if eks_sources is not None:
            input_["eks_sources"] = eks_sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_alarm_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_alarm_recommendations_response.ListAlarmRecommendationsResponse":
        """<p>Lists the alarm recommendations for an Resilience Hub application.</p>

        Args:
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_alarm_recommendations_request.ListAlarmRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_alarm_recommendations_response.ListAlarmRecommendationsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_alarm_recommendations

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_alarm_recommendations.list_alarm_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_alarm_recommendations_request.ListAlarmRecommendationsRequest = {
            "assessment_arn": assessment_arn
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

    def iter_list_alarm_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_alarm_recommendations_response.ListAlarmRecommendationsResponse]":
        _token = next_token
        while True:
            _response = self.list_alarm_recommendations(
                assessment_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_assessment_compliance_drifts(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_assessment_compliance_drifts_response.ListAppAssessmentComplianceDriftsResponse":
        """<p>List of compliance drifts that were detected while running an assessment.</p>

        Args:
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of compliance drifts requested.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_assessment_compliance_drifts_request.ListAppAssessmentComplianceDriftsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_assessment_compliance_drifts_response.ListAppAssessmentComplianceDriftsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_assessment_compliance_drifts

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_assessment_compliance_drifts.list_app_assessment_compliance_drifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_assessment_compliance_drifts_request.ListAppAssessmentComplianceDriftsRequest = {
            "assessment_arn": assessment_arn
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

    def iter_list_app_assessment_compliance_drifts(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_assessment_compliance_drifts_response.ListAppAssessmentComplianceDriftsResponse]":
        _token = next_token
        while True:
            _response = self.list_app_assessment_compliance_drifts(
                assessment_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_assessment_resource_drifts(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_assessment_resource_drifts_response.ListAppAssessmentResourceDriftsResponse":
        """<p>List of resource drifts that were detected while running an assessment.</p>

        Args:
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of drift results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_assessment_resource_drifts_request.ListAppAssessmentResourceDriftsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_assessment_resource_drifts_response.ListAppAssessmentResourceDriftsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_assessment_resource_drifts

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_assessment_resource_drifts.list_app_assessment_resource_drifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_assessment_resource_drifts_request.ListAppAssessmentResourceDriftsRequest = {
            "assessment_arn": assessment_arn
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

    def iter_list_app_assessment_resource_drifts(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.resource_drift.ResourceDrift]":
        _token = next_token
        while True:
            _response = self.list_app_assessment_resource_drifts(
                assessment_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resource_drifts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_assessments(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        app_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        assessment_name: Optional[
            "capo_resiliencehub.types.entity_name.EntityName"
        ] = None,
        assessment_status: Optional[
            "capo_resiliencehub.types.assessment_status_list.AssessmentStatusList"
        ] = None,
        compliance_status: Optional[
            "capo_resiliencehub.types.compliance_status.ComplianceStatus"
        ] = None,
        invoker: Optional[
            "capo_resiliencehub.types.assessment_invoker.AssessmentInvoker"
        ] = None,
        reverse_order: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_assessments_response.ListAppAssessmentsResponse":
        """<p>Lists the assessments for an Resilience Hub application. You can use request parameters to refine the results for the response object.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            assessment_name: <p>The name for the assessment.</p>
            assessment_status: <p>The current status of the assessment for the resiliency policy.</p>
            compliance_status: <p>The current status of compliance for the resiliency policy.</p>
            invoker: <p>Specifies the entity that invoked a specific assessment, either a <code>User</code> or the <code>System</code>.</p>
            reverse_order: <p>The default is to sort by ascending <b>startTime</b>. To sort by descending <b>startTime</b>, set reverseOrder to <code>true</code>.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_assessments_request.ListAppAssessmentsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_assessments_response.ListAppAssessmentsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_assessments

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_assessments.list_app_assessments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_assessments_request.ListAppAssessmentsRequest = {}
        if app_arn is not None:
            input_["app_arn"] = app_arn
        if assessment_name is not None:
            input_["assessment_name"] = assessment_name
        if assessment_status is not None:
            input_["assessment_status"] = assessment_status
        if compliance_status is not None:
            input_["compliance_status"] = compliance_status
        if invoker is not None:
            input_["invoker"] = invoker
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
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

    def iter_list_app_assessments(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        app_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        assessment_name: Optional[
            "capo_resiliencehub.types.entity_name.EntityName"
        ] = None,
        assessment_status: Optional[
            "capo_resiliencehub.types.assessment_status_list.AssessmentStatusList"
        ] = None,
        compliance_status: Optional[
            "capo_resiliencehub.types.compliance_status.ComplianceStatus"
        ] = None,
        invoker: Optional[
            "capo_resiliencehub.types.assessment_invoker.AssessmentInvoker"
        ] = None,
        reverse_order: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_assessments_response.ListAppAssessmentsResponse]":
        _token = next_token
        while True:
            _response = self.list_app_assessments(
                config_overrides=config_overrides,
                app_arn=app_arn,
                assessment_name=assessment_name,
                assessment_status=assessment_status,
                compliance_status=compliance_status,
                invoker=invoker,
                reverse_order=reverse_order,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_component_compliances(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_component_compliances_response.ListAppComponentCompliancesResponse":
        """<p>Lists the compliances for an Resilience Hub Application Component.</p>

        Args:
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_component_compliances_request.ListAppComponentCompliancesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_component_compliances_response.ListAppComponentCompliancesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_component_compliances

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_component_compliances.list_app_component_compliances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_component_compliances_request.ListAppComponentCompliancesRequest = {
            "assessment_arn": assessment_arn
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

    def iter_list_app_component_compliances(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_component_compliances_response.ListAppComponentCompliancesResponse]":
        _token = next_token
        while True:
            _response = self.list_app_component_compliances(
                assessment_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_component_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_component_recommendations_response.ListAppComponentRecommendationsResponse":
        """<p>Lists the recommendations for an Resilience Hub Application Component.</p>

        Args:
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_component_recommendations_request.ListAppComponentRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_component_recommendations_response.ListAppComponentRecommendationsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_component_recommendations

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_component_recommendations.list_app_component_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_component_recommendations_request.ListAppComponentRecommendationsRequest = {
            "assessment_arn": assessment_arn
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

    def iter_list_app_component_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_component_recommendations_response.ListAppComponentRecommendationsResponse]":
        _token = next_token
        while True:
            _response = self.list_app_component_recommendations(
                assessment_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_input_sources(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_input_sources_response.ListAppInputSourcesResponse":
        """<p>Lists all the input sources of the Resilience Hub application. For more information about the input sources supported by Resilience Hub, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html">Discover the structure and describe your Resilience Hub application</a>.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>Resilience Hub application version.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of input sources to be displayed per Resilience Hub application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_input_sources_request.ListAppInputSourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_input_sources_response.ListAppInputSourcesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_input_sources

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_input_sources.list_app_input_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_input_sources_request.ListAppInputSourcesRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
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

    def iter_list_app_input_sources(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_input_sources_response.ListAppInputSourcesResponse]":
        _token = next_token
        while True:
            _response = self.list_app_input_sources(
                app_arn,
                app_version,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_apps(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
        name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        app_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        from_last_assessment_time: Optional[
            "capo_resiliencehub.types.time_stamp.TimeStamp"
        ] = None,
        to_last_assessment_time: Optional[
            "capo_resiliencehub.types.time_stamp.TimeStamp"
        ] = None,
        reverse_order: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        aws_application_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
    ) -> "capo_resiliencehub.types.list_apps_response.ListAppsResponse":
        """<p>Lists your Resilience Hub applications.</p> <note> <p>You can filter applications using only one filter at a time or without using any filter. If you try to filter applications using multiple filters, you will get the following error:</p> <p> <code>An error occurred (ValidationException) when calling the ListApps operation: Only one filter is supported for this operation.</code> </p> </note>

        Args:
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            name: <p>The name for the one of the listed applications.</p>
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            from_last_assessment_time: <p>Lower limit of the range that is used to filter applications based on their last assessment times.</p>
            to_last_assessment_time: <p>Upper limit of the range that is used to filter the applications based on their last assessment times.</p>
            reverse_order: <p>The application list is sorted based on the values of <code>lastAppComplianceEvaluationTime</code> field. By default, application list is sorted in ascending order. To sort the application list in descending order, set this field to <code>True</code>.</p>
            aws_application_arn: <p>Amazon Resource Name (ARN) of Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_apps_request.ListAppsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_apps_response.ListAppsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_apps

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_apps.list_apps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_apps_request.ListAppsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if name is not None:
            input_["name"] = name
        if app_arn is not None:
            input_["app_arn"] = app_arn
        if from_last_assessment_time is not None:
            input_["from_last_assessment_time"] = from_last_assessment_time
        if to_last_assessment_time is not None:
            input_["to_last_assessment_time"] = to_last_assessment_time
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if aws_application_arn is not None:
            input_["aws_application_arn"] = aws_application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_apps(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
        name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        app_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        from_last_assessment_time: Optional[
            "capo_resiliencehub.types.time_stamp.TimeStamp"
        ] = None,
        to_last_assessment_time: Optional[
            "capo_resiliencehub.types.time_stamp.TimeStamp"
        ] = None,
        reverse_order: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        aws_application_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_apps_response.ListAppsResponse]":
        _token = next_token
        while True:
            _response = self.list_apps(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                name=name,
                app_arn=app_arn,
                from_last_assessment_time=from_last_assessment_time,
                to_last_assessment_time=to_last_assessment_time,
                reverse_order=reverse_order,
                aws_application_arn=aws_application_arn,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_version_app_components(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_version_app_components_response.ListAppVersionAppComponentsResponse":
        """<p>Lists all the Application Components in the Resilience Hub application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>Version of the Application Component.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of Application Components to be displayed per Resilience Hub application version.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_version_app_components_request.ListAppVersionAppComponentsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_version_app_components_response.ListAppVersionAppComponentsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_version_app_components

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_version_app_components.list_app_version_app_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_version_app_components_request.ListAppVersionAppComponentsRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
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

    def iter_list_app_version_app_components(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_version_app_components_response.ListAppVersionAppComponentsResponse]":
        _token = next_token
        while True:
            _response = self.list_app_version_app_components(
                app_arn,
                app_version,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_version_resource_mappings(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_version_resource_mappings_response.ListAppVersionResourceMappingsResponse":
        """<p>Lists how the resources in an application version are mapped/sourced from. Mappings can be physical resource identifiers, CloudFormation stacks, resource-groups, or an application registry app.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>The version of the application.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_version_resource_mappings_request.ListAppVersionResourceMappingsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_version_resource_mappings_response.ListAppVersionResourceMappingsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_version_resource_mappings

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_version_resource_mappings.list_app_version_resource_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_version_resource_mappings_request.ListAppVersionResourceMappingsRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
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

    def iter_list_app_version_resource_mappings(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_version_resource_mappings_response.ListAppVersionResourceMappingsResponse]":
        _token = next_token
        while True:
            _response = self.list_app_version_resource_mappings(
                app_arn,
                app_version,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_version_resources(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resolution_id: Optional["capo_resiliencehub.types.string255.String255"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_app_version_resources_response.ListAppVersionResourcesResponse":
        """<p>Lists all the resources in an Resilience Hub application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>The version of the application.</p>
            resolution_id: <p>The identifier for a specific resolution.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_version_resources_request.ListAppVersionResourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_version_resources_response.ListAppVersionResourcesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_version_resources

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_version_resources.list_app_version_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_version_resources_request.ListAppVersionResourcesRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
        }
        if resolution_id is not None:
            input_["resolution_id"] = resolution_id
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

    def iter_list_app_version_resources(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resolution_id: Optional["capo_resiliencehub.types.string255.String255"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_version_resources_response.ListAppVersionResourcesResponse]":
        _token = next_token
        while True:
            _response = self.list_app_version_resources(
                app_arn,
                app_version,
                config_overrides=config_overrides,
                resolution_id=resolution_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_app_versions(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
        start_time: Optional["capo_resiliencehub.types.time_stamp.TimeStamp"] = None,
        end_time: Optional["capo_resiliencehub.types.time_stamp.TimeStamp"] = None,
    ) -> "capo_resiliencehub.types.list_app_versions_response.ListAppVersionsResponse":
        """<p>Lists the different versions for the Resilience Hub applications.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            start_time: <p>Lower limit of the time range to filter the application versions.</p>
            end_time: <p>Upper limit of the time range to filter the application versions.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_app_versions_request.ListAppVersionsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_app_versions_response.ListAppVersionsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_app_versions

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_app_versions.list_app_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_app_versions_request.ListAppVersionsRequest = {
            "app_arn": app_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_app_versions(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
        start_time: Optional["capo_resiliencehub.types.time_stamp.TimeStamp"] = None,
        end_time: Optional["capo_resiliencehub.types.time_stamp.TimeStamp"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_app_versions_response.ListAppVersionsResponse]":
        _token = next_token
        while True:
            _response = self.list_app_versions(
                app_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                start_time=start_time,
                end_time=end_time,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_metrics(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
        fields: Optional["capo_resiliencehub.types.field_list.FieldList"] = None,
        data_source: Optional["capo_resiliencehub.types.string255.String255"] = None,
        conditions: Optional[
            "capo_resiliencehub.types.condition_list.ConditionList"
        ] = None,
        sorts: Optional["capo_resiliencehub.types.sort_list.SortList"] = None,
    ) -> "capo_resiliencehub.types.list_metrics_response.ListMetricsResponse":
        """<p>Lists the metrics that can be exported.</p>

        Args:
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            fields: <p>Indicates the list of fields in the data source.</p>
            data_source: <p>Indicates the data source of the metrics.</p>
            conditions: <p>Indicates the list of all the conditions that were applied on the metrics.</p>
            sorts: <p>(Optional) Indicates the order in which you want to sort the fields in the metrics. By default, the fields are sorted in the ascending order.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_metrics_request.ListMetricsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_metrics_response.ListMetricsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_metrics

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_metrics.list_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_metrics_request.ListMetricsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if fields is not None:
            input_["fields"] = fields
        if data_source is not None:
            input_["data_source"] = data_source
        if conditions is not None:
            input_["conditions"] = conditions
        if sorts is not None:
            input_["sorts"] = sorts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_metrics(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
        fields: Optional["capo_resiliencehub.types.field_list.FieldList"] = None,
        data_source: Optional["capo_resiliencehub.types.string255.String255"] = None,
        conditions: Optional[
            "capo_resiliencehub.types.condition_list.ConditionList"
        ] = None,
        sorts: Optional["capo_resiliencehub.types.sort_list.SortList"] = None,
    ) -> "Iterator[capo_resiliencehub.types.row.Row]":
        _token = next_token
        while True:
            _response = self.list_metrics(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                fields=fields,
                data_source=data_source,
                conditions=conditions,
                sorts=sorts,
            )
            _page = _resolve_path(_response, ("rows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommendation_templates(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        assessment_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        reverse_order: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        status: Optional[
            "capo_resiliencehub.types.recommendation_template_status_list.RecommendationTemplateStatusList"
        ] = None,
        recommendation_template_arn: Optional[
            "capo_resiliencehub.types.arn.Arn"
        ] = None,
        name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_recommendation_templates_response.ListRecommendationTemplatesResponse":
        """<p>Lists the recommendation templates for the Resilience Hub applications.</p>

        Args:
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            reverse_order: <p>The default is to sort by ascending <b>startTime</b>. To sort by descending <b>startTime</b>, set reverseOrder to <code>true</code>.</p>
            status: <p>Status of the action.</p>
            recommendation_template_arn: <p>The Amazon Resource Name (ARN) for a recommendation template.</p>
            name: <p>The name for one of the listed recommendation templates.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_recommendation_templates_request.ListRecommendationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_recommendation_templates_response.ListRecommendationTemplatesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_recommendation_templates

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_recommendation_templates.list_recommendation_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_recommendation_templates_request.ListRecommendationTemplatesRequest = {}
        if assessment_arn is not None:
            input_["assessment_arn"] = assessment_arn
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if status is not None:
            input_["status"] = status
        if recommendation_template_arn is not None:
            input_["recommendation_template_arn"] = recommendation_template_arn
        if name is not None:
            input_["name"] = name
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

    def iter_list_recommendation_templates(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        assessment_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        reverse_order: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        status: Optional[
            "capo_resiliencehub.types.recommendation_template_status_list.RecommendationTemplateStatusList"
        ] = None,
        recommendation_template_arn: Optional[
            "capo_resiliencehub.types.arn.Arn"
        ] = None,
        name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_recommendation_templates_response.ListRecommendationTemplatesResponse]":
        _token = next_token
        while True:
            _response = self.list_recommendation_templates(
                config_overrides=config_overrides,
                assessment_arn=assessment_arn,
                reverse_order=reverse_order,
                status=status,
                recommendation_template_arn=recommendation_template_arn,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resiliency_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        policy_name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_resiliency_policies_response.ListResiliencyPoliciesResponse":
        """<p>Lists the resiliency policies for the Resilience Hub applications.</p>

        Args:
            policy_name: <p>Name of the resiliency policy.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_resiliency_policies_request.ListResiliencyPoliciesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_resiliency_policies_response.ListResiliencyPoliciesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_resiliency_policies

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_resiliency_policies.list_resiliency_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_resiliency_policies_request.ListResiliencyPoliciesRequest = {}
        if policy_name is not None:
            input_["policy_name"] = policy_name
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

    def iter_list_resiliency_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        policy_name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_resiliency_policies_response.ListResiliencyPoliciesResponse]":
        _token = next_token
        while True:
            _response = self.list_resiliency_policies(
                config_overrides=config_overrides,
                policy_name=policy_name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_grouping_recommendations(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        app_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_resource_grouping_recommendations_response.ListResourceGroupingRecommendationsResponse":
        """<p>Lists the resource grouping recommendations suggested by Resilience Hub for your application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of grouping recommendations to be displayed per Resilience Hub application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_resource_grouping_recommendations_request.ListResourceGroupingRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_resource_grouping_recommendations_response.ListResourceGroupingRecommendationsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_resource_grouping_recommendations

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_resource_grouping_recommendations.list_resource_grouping_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_resource_grouping_recommendations_request.ListResourceGroupingRecommendationsRequest = {}
        if app_arn is not None:
            input_["app_arn"] = app_arn
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

    def iter_list_resource_grouping_recommendations(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        app_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.grouping_recommendation.GroupingRecommendation]":
        _token = next_token
        while True:
            _response = self.list_resource_grouping_recommendations(
                config_overrides=config_overrides,
                app_arn=app_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("grouping_recommendations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sop_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_sop_recommendations_response.ListSopRecommendationsResponse":
        """<p>Lists the standard operating procedure (SOP) recommendations for the Resilience Hub applications.</p>

        Args:
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_sop_recommendations_request.ListSopRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_sop_recommendations_response.ListSopRecommendationsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_sop_recommendations

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_sop_recommendations.list_sop_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_sop_recommendations_request.ListSopRecommendationsRequest = {
            "assessment_arn": assessment_arn
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

    def iter_list_sop_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_sop_recommendations_response.ListSopRecommendationsResponse]":
        _token = next_token
        while True:
            _response = self.list_sop_recommendations(
                assessment_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_suggested_resiliency_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_suggested_resiliency_policies_response.ListSuggestedResiliencyPoliciesResponse":
        """<p>Lists the suggested resiliency policies for the Resilience Hub applications.</p>

        Args:
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_suggested_resiliency_policies_request.ListSuggestedResiliencyPoliciesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_suggested_resiliency_policies_response.ListSuggestedResiliencyPoliciesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_suggested_resiliency_policies

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_suggested_resiliency_policies.list_suggested_resiliency_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_suggested_resiliency_policies_request.ListSuggestedResiliencyPoliciesRequest = {}
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

    def iter_list_suggested_resiliency_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_suggested_resiliency_policies_response.ListSuggestedResiliencyPoliciesResponse]":
        _token = next_token
        while True:
            _response = self.list_suggested_resiliency_policies(
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
        resource_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for your resources in your Resilience Hub applications.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a specific resource in your Resilience Hub application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_tags_for_resource

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_test_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_test_recommendations_response.ListTestRecommendationsResponse":
        """<p>Lists the test recommendations for the Resilience Hub application.</p>

        Args:
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            assessment_arn: <p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_test_recommendations_request.ListTestRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_test_recommendations_response.ListTestRecommendationsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_test_recommendations

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_test_recommendations.list_test_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_test_recommendations_request.ListTestRecommendationsRequest = {
            "assessment_arn": assessment_arn
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

    def iter_list_test_recommendations(
        self,
        assessment_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_test_recommendations_response.ListTestRecommendationsResponse]":
        _token = next_token
        while True:
            _response = self.list_test_recommendations(
                assessment_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_unsupported_app_version_resources(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resolution_id: Optional["capo_resiliencehub.types.string255.String255"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "capo_resiliencehub.types.list_unsupported_app_version_resources_response.ListUnsupportedAppVersionResourcesResponse":
        """<p>Lists the resources that are not currently supported in Resilience Hub. An unsupported resource is a resource that exists in the object that was used to create an app, but is not supported by Resilience Hub.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>The version of the application.</p>
            resolution_id: <p>The identifier for a specific resolution.</p>
            next_token: <p>Null, or the token from a previous call to get the next set of results.</p>
            max_results: <p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.list_unsupported_app_version_resources_request.ListUnsupportedAppVersionResourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.list_unsupported_app_version_resources_response.ListUnsupportedAppVersionResourcesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.list_unsupported_app_version_resources

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.list_unsupported_app_version_resources.list_unsupported_app_version_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.list_unsupported_app_version_resources_request.ListUnsupportedAppVersionResourcesRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
        }
        if resolution_id is not None:
            input_["resolution_id"] = resolution_id
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

    def iter_list_unsupported_app_version_resources(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resolution_id: Optional["capo_resiliencehub.types.string255.String255"] = None,
        next_token: Optional["capo_resiliencehub.types.next_token.NextToken"] = None,
        max_results: Optional["capo_resiliencehub.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_resiliencehub.types.list_unsupported_app_version_resources_response.ListUnsupportedAppVersionResourcesResponse]":
        _token = next_token
        while True:
            _response = self.list_unsupported_app_version_resources(
                app_arn,
                app_version,
                config_overrides=config_overrides,
                resolution_id=resolution_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def publish_app_version(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        version_name: Optional[
            "capo_resiliencehub.types.entity_version.EntityVersion"
        ] = None,
    ) -> "capo_resiliencehub.types.publish_app_version_response.PublishAppVersionResponse":
        """<p>Publishes a new version of a specific Resilience Hub application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            version_name: <p>Name of the application version.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.publish_app_version_request.PublishAppVersionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.publish_app_version_response.PublishAppVersionResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.publish_app_version

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.publish_app_version.publish_app_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.publish_app_version_request.PublishAppVersionRequest = {
            "app_arn": app_arn
        }
        if version_name is not None:
            input_["version_name"] = version_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_draft_app_version_template(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_template_body: "capo_resiliencehub.types.app_template_body.AppTemplateBody",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.put_draft_app_version_template_response.PutDraftAppVersionTemplateResponse":
        """<p>Adds or updates the app template for an Resilience Hub application draft version.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_template_body: <p>A JSON string that provides information about your application structure. To learn more about the <code>appTemplateBody</code> template, see the sample template provided in the <i>Examples</i> section.</p> <p>The <code>appTemplateBody</code> JSON string has the following structure:</p> <ul> <li> <p> <b> <code>resources</code> </b> </p> <p>The list of logical resources that must be included in the Resilience Hub application.</p> <p>Type: Array</p> <note> <p>Don't add the resources that you want to exclude.</p> </note> <p>Each <code>resources</code> array item includes the following fields:</p> <ul> <li> <p> <i> <code>logicalResourceId</code> </i> </p> <p>Logical identifier of the resource.</p> <p>Type: Object</p> <p>Each <code>logicalResourceId</code> object includes the following fields:</p> <ul> <li> <p> <code>identifier</code> </p> <p>Identifier of the resource.</p> <p>Type: String</p> </li> <li> <p> <code>logicalStackName</code> </p> <p>The name of the CloudFormation stack this resource belongs to.</p> <p>Type: String</p> </li> <li> <p> <code>resourceGroupName</code> </p> <p>The name of the resource group this resource belongs to.</p> <p>Type: String</p> </li> <li> <p> <code>terraformSourceName</code> </p> <p>The name of the Terraform S3 state file this resource belongs to.</p> <p>Type: String</p> </li> <li> <p> <code>eksSourceName</code> </p> <p>Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.</p> <note> <p>This parameter accepts values in "eks-cluster/namespace" format.</p> </note> <p>Type: String</p> </li> </ul> </li> <li> <p> <i> <code>type</code> </i> </p> <p>The type of resource.</p> <p>Type: string</p> </li> <li> <p> <i> <code>name</code> </i> </p> <p>The name of the resource.</p> <p>Type: String</p> </li> <li> <p> <code>additionalInfo</code> </p> <p>Additional configuration parameters for an Resilience Hub application. If you want to implement <code>additionalInfo</code> through the Resilience Hub console rather than using an API call, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html">Configure the application configuration parameters</a>.</p> <note> <p>Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.</p> <p>Key: <code>"failover-regions"</code> </p> <p>Value: <code>"[{"region":"&lt;REGION&gt;", "accounts":[{"id":"&lt;ACCOUNT_ID&gt;"}]}]"</code> </p> </note> </li> </ul> </li> <li> <p> <b> <code>appComponents</code> </b> </p> <p>List of Application Components that this resource belongs to. If an Application Component is not part of the Resilience Hub application, it will be added.</p> <p>Type: Array</p> <p>Each <code>appComponents</code> array item includes the following fields:</p> <ul> <li> <p> <code>name</code> </p> <p>Name of the Application Component.</p> <p>Type: String</p> </li> <li> <p> <code>type</code> </p> <p>Type of Application Component. For more information about the types of Application Component, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html">Grouping resources in an AppComponent</a>.</p> <p>Type: String</p> </li> <li> <p> <code>resourceNames</code> </p> <p>The list of included resources that are assigned to the Application Component.</p> <p>Type: Array of strings</p> </li> <li> <p> <code>additionalInfo</code> </p> <p>Additional configuration parameters for an Resilience Hub application. If you want to implement <code>additionalInfo</code> through the Resilience Hub console rather than using an API call, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html">Configure the application configuration parameters</a>.</p> <note> <p>Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.</p> <p>Key: <code>"failover-regions"</code> </p> <p>Value: <code>"[{"region":"&lt;REGION&gt;", "accounts":[{"id":"&lt;ACCOUNT_ID&gt;"}]}]"</code> </p> </note> </li> </ul> </li> <li> <p> <b> <code>excludedResources</code> </b> </p> <p>The list of logical resource identifiers to be excluded from the application.</p> <p>Type: Array</p> <note> <p>Don't add the resources that you want to include.</p> </note> <p>Each <code>excludedResources</code> array item includes the following fields:</p> <ul> <li> <p> <i> <code>logicalResourceIds</code> </i> </p> <p>Logical identifier of the resource.</p> <p>Type: Object</p> <note> <p>You can configure only one of the following fields:</p> <ul> <li> <p> <code>logicalStackName</code> </p> </li> <li> <p> <code>resourceGroupName</code> </p> </li> <li> <p> <code>terraformSourceName</code> </p> </li> <li> <p> <code>eksSourceName</code> </p> </li> </ul> </note> <p>Each <code>logicalResourceIds</code> object includes the following fields:</p> <ul> <li> <p> <code>identifier</code> </p> <p>Identifier of the resource.</p> <p>Type: String</p> </li> <li> <p> <code>logicalStackName</code> </p> <p>The name of the CloudFormation stack this resource belongs to.</p> <p>Type: String</p> </li> <li> <p> <code>resourceGroupName</code> </p> <p>The name of the resource group this resource belongs to.</p> <p>Type: String</p> </li> <li> <p> <code>terraformSourceName</code> </p> <p>The name of the Terraform S3 state file this resource belongs to.</p> <p>Type: String</p> </li> <li> <p> <code>eksSourceName</code> </p> <p>Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.</p> <note> <p>This parameter accepts values in "eks-cluster/namespace" format.</p> </note> <p>Type: String</p> </li> </ul> </li> </ul> </li> <li> <p> <b> <code>version</code> </b> </p> <p>Resilience Hub application version.</p> </li> <li> <p> <code>additionalInfo</code> </p> <p>Additional configuration parameters for an Resilience Hub application. If you want to implement <code>additionalInfo</code> through the Resilience Hub console rather than using an API call, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html">Configure the application configuration parameters</a>.</p> <note> <p>Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.</p> <p>Key: <code>"failover-regions"</code> </p> <p>Value: <code>"[{"region":"&lt;REGION&gt;", "accounts":[{"id":"&lt;ACCOUNT_ID&gt;"}]}]"</code> </p> </note> </li> </ul>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.put_draft_app_version_template_request.PutDraftAppVersionTemplateRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.put_draft_app_version_template_response.PutDraftAppVersionTemplateResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.put_draft_app_version_template

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.put_draft_app_version_template.put_draft_app_version_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.put_draft_app_version_template_request.PutDraftAppVersionTemplateRequest = {
            "app_arn": app_arn,
            "app_template_body": app_template_body,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_resource_grouping_recommendations(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        entries: "capo_resiliencehub.types.reject_grouping_recommendation_entries.RejectGroupingRecommendationEntries",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.reject_resource_grouping_recommendations_response.RejectResourceGroupingRecommendationsResponse":
        """<p>Rejects resource grouping recommendations.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            entries: <p>List of resource grouping recommendations you have selected to exclude from your application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.reject_resource_grouping_recommendations_request.RejectResourceGroupingRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.reject_resource_grouping_recommendations_response.RejectResourceGroupingRecommendationsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.reject_resource_grouping_recommendations

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.reject_resource_grouping_recommendations.reject_resource_grouping_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.reject_resource_grouping_recommendations_request.RejectResourceGroupingRecommendationsRequest = {
            "app_arn": app_arn,
            "entries": entries,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_draft_app_version_resource_mappings(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resource_names: Optional[
            "capo_resiliencehub.types.entity_name_list.EntityNameList"
        ] = None,
        logical_stack_names: Optional[
            "capo_resiliencehub.types.string255_list.String255List"
        ] = None,
        app_registry_app_names: Optional[
            "capo_resiliencehub.types.entity_name_list.EntityNameList"
        ] = None,
        resource_group_names: Optional[
            "capo_resiliencehub.types.entity_name_list.EntityNameList"
        ] = None,
        terraform_source_names: Optional[
            "capo_resiliencehub.types.string255_list.String255List"
        ] = None,
        eks_source_names: Optional[
            "capo_resiliencehub.types.string255_list.String255List"
        ] = None,
    ) -> "capo_resiliencehub.types.remove_draft_app_version_resource_mappings_response.RemoveDraftAppVersionResourceMappingsResponse":
        """<p>Removes resource mappings from a draft application version.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            resource_names: <p>The names of the resources you want to remove from the resource mappings.</p>
            logical_stack_names: <p>The names of the CloudFormation stacks you want to remove from the resource mappings.</p>
            app_registry_app_names: <p>The names of the registered applications you want to remove from the resource mappings.</p>
            resource_group_names: <p>The names of the resource groups you want to remove from the resource mappings.</p>
            terraform_source_names: <p>The names of the Terraform sources you want to remove from the resource mappings.</p>
            eks_source_names: <p>The names of the Amazon Elastic Kubernetes Service clusters and namespaces you want to remove from the resource mappings.</p> <note> <p>This parameter accepts values in "eks-cluster/namespace" format.</p> </note>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.remove_draft_app_version_resource_mappings_request.RemoveDraftAppVersionResourceMappingsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.remove_draft_app_version_resource_mappings_response.RemoveDraftAppVersionResourceMappingsResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.remove_draft_app_version_resource_mappings

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.remove_draft_app_version_resource_mappings.remove_draft_app_version_resource_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.remove_draft_app_version_resource_mappings_request.RemoveDraftAppVersionResourceMappingsRequest = {
            "app_arn": app_arn
        }
        if resource_names is not None:
            input_["resource_names"] = resource_names
        if logical_stack_names is not None:
            input_["logical_stack_names"] = logical_stack_names
        if app_registry_app_names is not None:
            input_["app_registry_app_names"] = app_registry_app_names
        if resource_group_names is not None:
            input_["resource_group_names"] = resource_group_names
        if terraform_source_names is not None:
            input_["terraform_source_names"] = terraform_source_names
        if eks_source_names is not None:
            input_["eks_source_names"] = eks_source_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resolve_app_version_resources(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.resolve_app_version_resources_response.ResolveAppVersionResourcesResponse":
        """<p>Resolves the resources for an application version.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>The version of the application.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.resolve_app_version_resources_request.ResolveAppVersionResourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.resolve_app_version_resources_response.ResolveAppVersionResourcesResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.resolve_app_version_resources

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.resolve_app_version_resources.resolve_app_version_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.resolve_app_version_resources_request.ResolveAppVersionResourcesRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_app_assessment(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        app_version: "capo_resiliencehub.types.entity_version.EntityVersion",
        assessment_name: "capo_resiliencehub.types.entity_name.EntityName",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_resiliencehub.types.tag_map.TagMap"] = None,
    ) -> "capo_resiliencehub.types.start_app_assessment_response.StartAppAssessmentResponse":
        """<p>Creates a new application assessment for an application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            app_version: <p>The version of the application.</p>
            assessment_name: <p>The name for the assessment.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>
            tags: <p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.start_app_assessment_request.StartAppAssessmentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.start_app_assessment_response.StartAppAssessmentResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.start_app_assessment

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.start_app_assessment.start_app_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.start_app_assessment_request.StartAppAssessmentRequest = {
            "app_arn": app_arn,
            "app_version": app_version,
            "assessment_name": assessment_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_metrics_export(
        self,
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        bucket_name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        client_token: Optional[
            "capo_resiliencehub.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehub.types.start_metrics_export_response.StartMetricsExportResponse":
        """<p>Initiates the export task of metrics.</p>

        Args:
            bucket_name: <p>(Optional) Specifies the name of the Amazon Simple Storage Service bucket where the exported metrics will be stored.</p>
            client_token: <p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.start_metrics_export_request.StartMetricsExportRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.start_metrics_export_response.StartMetricsExportResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.start_metrics_export

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.start_metrics_export.start_metrics_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.start_metrics_export_request.StartMetricsExportRequest = {}
        if bucket_name is not None:
            input_["bucket_name"] = bucket_name
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

    def start_resource_grouping_recommendation_task(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.start_resource_grouping_recommendation_task_response.StartResourceGroupingRecommendationTaskResponse":
        """<p>Starts grouping recommendation task.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.start_resource_grouping_recommendation_task_request.StartResourceGroupingRecommendationTaskRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.start_resource_grouping_recommendation_task_response.StartResourceGroupingRecommendationTaskResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.start_resource_grouping_recommendation_task

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.start_resource_grouping_recommendation_task.start_resource_grouping_recommendation_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.start_resource_grouping_recommendation_task_request.StartResourceGroupingRecommendationTaskRequest = {
            "app_arn": app_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_resiliencehub.types.arn.Arn",
        tags: "capo_resiliencehub.types.tag_map.TagMap",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.tag_resource_response.TagResourceResponse":
        """<p>Applies one or more tags to a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource. </p>
            tags: <p>The tags to assign to the resource. Each tag consists of a key/value pair.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.tag_resource

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_resiliencehub.types.arn.Arn",
        tag_keys: "capo_resiliencehub.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
    ) -> "capo_resiliencehub.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource. </p>
            tag_keys: <p>The keys of the tags you want to remove.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.untag_resource

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.untag_resource_request.UntagResourceRequest = {
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

    def update_app(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        description: Optional[
            "capo_resiliencehub.types.entity_description.EntityDescription"
        ] = None,
        policy_arn: Optional["capo_resiliencehub.types.arn.Arn"] = None,
        clear_resiliency_policy_arn: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
        assessment_schedule: Optional[
            "capo_resiliencehub.types.app_assessment_schedule_type.AppAssessmentScheduleType"
        ] = None,
        permission_model: Optional[
            "capo_resiliencehub.types.permission_model.PermissionModel"
        ] = None,
        event_subscriptions: Optional[
            "capo_resiliencehub.types.event_subscription_list.EventSubscriptionList"
        ] = None,
    ) -> "capo_resiliencehub.types.update_app_response.UpdateAppResponse":
        """<p>Updates an application.</p>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            description: <p>The optional description for an app.</p>
            policy_arn: <p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            clear_resiliency_policy_arn: <p>Specifies if the resiliency policy ARN should be cleared.</p>
            assessment_schedule: <p> Assessment execution schedule with 'Daily' or 'Disabled' values. </p>
            permission_model: <p>Defines the roles and credentials that Resilience Hub would use while creating an application, importing its resources, and running an assessment.</p>
            event_subscriptions: <p>The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for <b>Drift detected</b> and <b>Scheduled assessment failure</b> events.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.update_app_request.UpdateAppRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.update_app_response.UpdateAppResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.update_app

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.update_app.update_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.update_app_request.UpdateAppRequest = {
            "app_arn": app_arn
        }
        if description is not None:
            input_["description"] = description
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
        if clear_resiliency_policy_arn is not None:
            input_["clear_resiliency_policy_arn"] = clear_resiliency_policy_arn
        if assessment_schedule is not None:
            input_["assessment_schedule"] = assessment_schedule
        if permission_model is not None:
            input_["permission_model"] = permission_model
        if event_subscriptions is not None:
            input_["event_subscriptions"] = event_subscriptions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_app_version(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        additional_info: Optional[
            "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
        ] = None,
    ) -> (
        "capo_resiliencehub.types.update_app_version_response.UpdateAppVersionResponse"
    ):
        """<p>Updates the Resilience Hub application version.</p> <note> <p>This API updates the Resilience Hub application draft version. To use this information for running resiliency assessments, you must publish the Resilience Hub application using the <code>PublishAppVersion</code> API.</p> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            additional_info: <p>Additional configuration parameters for an Resilience Hub application. If you want to implement <code>additionalInfo</code> through the Resilience Hub console rather than using an API call, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html">Configure the application configuration parameters</a>.</p> <note> <p>Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.</p> <p>Key: <code>"failover-regions"</code> </p> <p>Value: <code>"[{"region":"&lt;REGION&gt;", "accounts":[{"id":"&lt;ACCOUNT_ID&gt;"}]}]"</code> </p> </note>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.update_app_version_request.UpdateAppVersionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.update_app_version_response.UpdateAppVersionResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.update_app_version

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.update_app_version.update_app_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.update_app_version_request.UpdateAppVersionRequest = {
            "app_arn": app_arn
        }
        if additional_info is not None:
            input_["additional_info"] = additional_info

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_app_version_app_component(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        id: "capo_resiliencehub.types.string255.String255",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        name: Optional["capo_resiliencehub.types.string255.String255"] = None,
        type: Optional["capo_resiliencehub.types.string255.String255"] = None,
        additional_info: Optional[
            "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
        ] = None,
    ) -> "capo_resiliencehub.types.update_app_version_app_component_response.UpdateAppVersionAppComponentResponse":
        """<p>Updates an existing Application Component in the Resilience Hub application.</p> <note> <p>This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the <code>PublishAppVersion</code> API.</p> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            id: <p>Identifier of the Application Component.</p>
            name: <p>Name of the Application Component.</p>
            type: <p>Type of Application Component. For more information about the types of Application Component, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html">Grouping resources in an AppComponent</a>.</p>
            additional_info: <p>Currently, there is no supported additional information for Application Components.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.update_app_version_app_component_request.UpdateAppVersionAppComponentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.update_app_version_app_component_response.UpdateAppVersionAppComponentResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.update_app_version_app_component

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.update_app_version_app_component.update_app_version_app_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.update_app_version_app_component_request.UpdateAppVersionAppComponentRequest = {
            "app_arn": app_arn,
            "id": id,
        }
        if name is not None:
            input_["name"] = name
        if type is not None:
            input_["type"] = type
        if additional_info is not None:
            input_["additional_info"] = additional_info

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_app_version_resource(
        self,
        app_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        resource_name: Optional[
            "capo_resiliencehub.types.entity_name.EntityName"
        ] = None,
        logical_resource_id: Optional[
            "capo_resiliencehub.types.logical_resource_id.LogicalResourceId"
        ] = None,
        physical_resource_id: Optional[
            "capo_resiliencehub.types.string2048.String2048"
        ] = None,
        aws_region: Optional["capo_resiliencehub.types.aws_region.AwsRegion"] = None,
        aws_account_id: Optional[
            "capo_resiliencehub.types.customer_id.CustomerId"
        ] = None,
        resource_type: Optional["capo_resiliencehub.types.string255.String255"] = None,
        app_components: Optional[
            "capo_resiliencehub.types.app_component_name_list.AppComponentNameList"
        ] = None,
        additional_info: Optional[
            "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
        ] = None,
        excluded: Optional[
            "capo_resiliencehub.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_resiliencehub.types.update_app_version_resource_response.UpdateAppVersionResourceResponse":
        """<p>Updates the resource details in the Resilience Hub application.</p> <note> <ul> <li> <p>This action has no effect outside Resilience Hub.</p> </li> <li> <p>This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the <code>PublishAppVersion</code> API.</p> </li> <li> <p>To update application version with new <code>physicalResourceID</code>, you must call <code>ResolveAppVersionResources</code> API.</p> </li> </ul> </note>

        Args:
            app_arn: <p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            resource_name: <p>Name of the resource.</p>
            logical_resource_id: <p>Logical identifier of the resource.</p>
            physical_resource_id: <p>Physical identifier of the resource.</p>
            aws_region: <p>Amazon Web Services region that owns the physical resource.</p>
            aws_account_id: <p>Amazon Web Services account that owns the physical resource.</p>
            resource_type: <p>Type of resource.</p>
            app_components: <p>List of Application Components that this resource belongs to. If an Application Component is not part of the Resilience Hub application, it will be added.</p>
            additional_info: <p>Currently, there is no supported additional information for resources.</p>
            excluded: <p>Indicates if a resource is excluded from an Resilience Hub application.</p> <note> <p>You can exclude only imported resources from an Resilience Hub application.</p> </note>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.update_app_version_resource_request.UpdateAppVersionResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.update_app_version_resource_response.UpdateAppVersionResourceResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.update_app_version_resource

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.update_app_version_resource.update_app_version_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.update_app_version_resource_request.UpdateAppVersionResourceRequest = {
            "app_arn": app_arn
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id
        if physical_resource_id is not None:
            input_["physical_resource_id"] = physical_resource_id
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if app_components is not None:
            input_["app_components"] = app_components
        if additional_info is not None:
            input_["additional_info"] = additional_info
        if excluded is not None:
            input_["excluded"] = excluded

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resiliency_policy(
        self,
        policy_arn: "capo_resiliencehub.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubClientConfig] = None,
        policy_name: Optional["capo_resiliencehub.types.entity_name.EntityName"] = None,
        policy_description: Optional[
            "capo_resiliencehub.types.entity_description.EntityDescription"
        ] = None,
        data_location_constraint: Optional[
            "capo_resiliencehub.types.data_location_constraint.DataLocationConstraint"
        ] = None,
        tier: Optional[
            "capo_resiliencehub.types.resiliency_policy_tier.ResiliencyPolicyTier"
        ] = None,
        policy: Optional[
            "capo_resiliencehub.types.disruption_policy.DisruptionPolicy"
        ] = None,
    ) -> "capo_resiliencehub.types.update_resiliency_policy_response.UpdateResiliencyPolicyResponse":
        """<p>Updates a resiliency policy.</p> <note> <p>Resilience Hub allows you to provide a value of zero for <code>rtoInSecs</code> and <code>rpoInSecs</code> of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for <code>rtoInSecs</code> and <code>rpoInSecs</code>, the estimated workload RTO and estimated workload RPO result will be near zero and the <b>Compliance status</b> for your application will be set to <b>Policy breached</b>.</p> </note>

        Args:
            policy_arn: <p>Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:resiliency-policy/<code>policy-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>
            policy_name: <p>Name of the resiliency policy.</p>
            policy_description: <p>Description of the resiliency policy.</p>
            data_location_constraint: <p>Specifies a high-level geographical location constraint for where your resilience policy data can be stored.</p>
            tier: <p>The tier for this resiliency policy, ranging from the highest severity (<code>MissionCritical</code>) to lowest (<code>NonCritical</code>).</p>
            policy: <p>Resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.</p>

        Raises:
            capo_resiliencehub.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.</p>
            capo_resiliencehub.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_resiliencehub.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Resilience Hub service.</p>
            capo_resiliencehub.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception occurs when the specified resource could not be found.</p>
            capo_resiliencehub.errors.throttling_exception.ThrottlingException: <p>This exception occurs when you have exceeded the limit on the number of requests per second.</p>
            capo_resiliencehub.errors.validation_exception.ValidationException: <p>This exception occurs when a request is not valid.</p>
            capo_resiliencehub.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehub.types.update_resiliency_policy_request.UpdateResiliencyPolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehub.types.update_resiliency_policy_response.UpdateResiliencyPolicyResponse"
        ]:
            import capo_resiliencehub._operations.aws_resilience_hub.update_resiliency_policy

            output, http_response = (
                capo_resiliencehub._operations.aws_resilience_hub.update_resiliency_policy.update_resiliency_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehub.types.update_resiliency_policy_request.UpdateResiliencyPolicyRequest = {
            "policy_arn": policy_arn
        }
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if data_location_constraint is not None:
            input_["data_location_constraint"] = data_location_constraint
        if tier is not None:
            input_["tier"] = tier
        if policy is not None:
            input_["policy"] = policy

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
