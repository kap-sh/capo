"""Generated from Smithy shape ``com.amazonaws.ssmincidents#SSMIncidents``."""

import datetime
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ssm_incidents._auth._signers
import capo_ssm_incidents._auth._sigv4
from capo_ssm_incidents._auth._identity import Credentials
from capo_ssm_incidents._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ssm_incidents._auth._zapros_handler import AuthMiddleware
from capo_ssm_incidents._pagination import resolve_path as _resolve_path
from capo_ssm_incidents._services._aws_config import aws_config
from capo_ssm_incidents._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ssm_incidents.types.actions_list
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.batch_get_incident_findings_input
    import capo_ssm_incidents.types.batch_get_incident_findings_output
    import capo_ssm_incidents.types.chat_channel
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.create_replication_set_input
    import capo_ssm_incidents.types.create_replication_set_output
    import capo_ssm_incidents.types.create_response_plan_input
    import capo_ssm_incidents.types.create_response_plan_output
    import capo_ssm_incidents.types.create_timeline_event_input
    import capo_ssm_incidents.types.create_timeline_event_output
    import capo_ssm_incidents.types.dedupe_string
    import capo_ssm_incidents.types.delete_incident_record_input
    import capo_ssm_incidents.types.delete_incident_record_output
    import capo_ssm_incidents.types.delete_replication_set_input
    import capo_ssm_incidents.types.delete_replication_set_output
    import capo_ssm_incidents.types.delete_resource_policy_input
    import capo_ssm_incidents.types.delete_resource_policy_output
    import capo_ssm_incidents.types.delete_response_plan_input
    import capo_ssm_incidents.types.delete_response_plan_output
    import capo_ssm_incidents.types.delete_timeline_event_input
    import capo_ssm_incidents.types.delete_timeline_event_output
    import capo_ssm_incidents.types.engagement_set
    import capo_ssm_incidents.types.event_data
    import capo_ssm_incidents.types.event_reference_list
    import capo_ssm_incidents.types.event_summary
    import capo_ssm_incidents.types.filter_list
    import capo_ssm_incidents.types.finding_id_list
    import capo_ssm_incidents.types.finding_summary
    import capo_ssm_incidents.types.get_incident_record_input
    import capo_ssm_incidents.types.get_incident_record_output
    import capo_ssm_incidents.types.get_replication_set_input
    import capo_ssm_incidents.types.get_replication_set_output
    import capo_ssm_incidents.types.get_resource_policies_input
    import capo_ssm_incidents.types.get_resource_policies_output
    import capo_ssm_incidents.types.get_response_plan_input
    import capo_ssm_incidents.types.get_response_plan_output
    import capo_ssm_incidents.types.get_timeline_event_input
    import capo_ssm_incidents.types.get_timeline_event_output
    import capo_ssm_incidents.types.impact
    import capo_ssm_incidents.types.incident_record_status
    import capo_ssm_incidents.types.incident_record_summary
    import capo_ssm_incidents.types.incident_summary
    import capo_ssm_incidents.types.incident_template
    import capo_ssm_incidents.types.incident_title
    import capo_ssm_incidents.types.integrations
    import capo_ssm_incidents.types.list_incident_findings_input
    import capo_ssm_incidents.types.list_incident_findings_output
    import capo_ssm_incidents.types.list_incident_records_input
    import capo_ssm_incidents.types.list_incident_records_output
    import capo_ssm_incidents.types.list_related_items_input
    import capo_ssm_incidents.types.list_related_items_output
    import capo_ssm_incidents.types.list_replication_sets_input
    import capo_ssm_incidents.types.list_replication_sets_output
    import capo_ssm_incidents.types.list_response_plans_input
    import capo_ssm_incidents.types.list_response_plans_output
    import capo_ssm_incidents.types.list_tags_for_resource_request
    import capo_ssm_incidents.types.list_tags_for_resource_response
    import capo_ssm_incidents.types.list_timeline_events_input
    import capo_ssm_incidents.types.list_timeline_events_output
    import capo_ssm_incidents.types.max_results
    import capo_ssm_incidents.types.next_token
    import capo_ssm_incidents.types.notification_target_set
    import capo_ssm_incidents.types.policy
    import capo_ssm_incidents.types.policy_id
    import capo_ssm_incidents.types.put_resource_policy_input
    import capo_ssm_incidents.types.put_resource_policy_output
    import capo_ssm_incidents.types.region_map_input
    import capo_ssm_incidents.types.related_item
    import capo_ssm_incidents.types.related_item_list
    import capo_ssm_incidents.types.related_items_update
    import capo_ssm_incidents.types.resource_policy
    import capo_ssm_incidents.types.response_plan_display_name
    import capo_ssm_incidents.types.response_plan_name
    import capo_ssm_incidents.types.response_plan_summary
    import capo_ssm_incidents.types.sort_order
    import capo_ssm_incidents.types.start_incident_input
    import capo_ssm_incidents.types.start_incident_output
    import capo_ssm_incidents.types.tag_key_list
    import capo_ssm_incidents.types.tag_map
    import capo_ssm_incidents.types.tag_map_update
    import capo_ssm_incidents.types.tag_resource_request
    import capo_ssm_incidents.types.tag_resource_response
    import capo_ssm_incidents.types.timeline_event_sort
    import capo_ssm_incidents.types.timeline_event_type
    import capo_ssm_incidents.types.trigger_details
    import capo_ssm_incidents.types.untag_resource_request
    import capo_ssm_incidents.types.untag_resource_response
    import capo_ssm_incidents.types.update_action_list
    import capo_ssm_incidents.types.update_deletion_protection_input
    import capo_ssm_incidents.types.update_deletion_protection_output
    import capo_ssm_incidents.types.update_incident_record_input
    import capo_ssm_incidents.types.update_incident_record_output
    import capo_ssm_incidents.types.update_related_items_input
    import capo_ssm_incidents.types.update_related_items_output
    import capo_ssm_incidents.types.update_replication_set_input
    import capo_ssm_incidents.types.update_replication_set_output
    import capo_ssm_incidents.types.update_response_plan_input
    import capo_ssm_incidents.types.update_response_plan_output
    import capo_ssm_incidents.types.update_timeline_event_input
    import capo_ssm_incidents.types.update_timeline_event_output
    import capo_ssm_incidents.types.uuid


class SSMIncidentsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SSMIncidentsClient:
    """A client for the ``SSMIncidents`` service.

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
        self._config = SSMIncidentsClientConfig(
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
        self, config_overrides: Optional[SSMIncidentsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SSMIncidentsClientConfig = config_overrides or {}
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

    def batch_get_incident_findings(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        finding_ids: "capo_ssm_incidents.types.finding_id_list.FindingIdList",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.batch_get_incident_findings_output.BatchGetIncidentFindingsOutput":
        """<p>Retrieves details about all specified findings for an incident, including descriptive details about each finding. A finding represents a recent application environment change made by an CodeDeploy deployment or an CloudFormation stack creation or update that can be investigated as a potential cause of the incident.</p>

        Args:
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident for which you want to view finding details.</p>
            finding_ids: <p>A list of IDs of findings for which you want to view details.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.batch_get_incident_findings_input.BatchGetIncidentFindingsInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.batch_get_incident_findings_output.BatchGetIncidentFindingsOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.batch_get_incident_findings

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.batch_get_incident_findings.batch_get_incident_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.batch_get_incident_findings_input.BatchGetIncidentFindingsInput = {
            "incident_record_arn": incident_record_arn,
            "finding_ids": finding_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_replication_set(
        self,
        regions: "capo_ssm_incidents.types.region_map_input.RegionMapInput",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_ssm_incidents.types.tag_map.TagMap"] = None,
    ) -> "capo_ssm_incidents.types.create_replication_set_output.CreateReplicationSetOutput":
        """<p>A replication set replicates and encrypts your data to the provided Regions with the provided KMS key. </p>

        Args:
            regions: <p>The Regions that Incident Manager replicates your data to. You can have up to three Regions in your replication set.</p>
            client_token: <p>A token that ensures that the operation is called only once with the specified details.</p>
            tags: <p>A list of tags to add to the replication set.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.create_replication_set_input.CreateReplicationSetInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.create_replication_set_output.CreateReplicationSetOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.create_replication_set

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.create_replication_set.create_replication_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.create_replication_set_input.CreateReplicationSetInput = {
            "regions": regions
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

    def create_response_plan(
        self,
        name: "capo_ssm_incidents.types.response_plan_name.ResponsePlanName",
        incident_template: "capo_ssm_incidents.types.incident_template.IncidentTemplate",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
        display_name: Optional[
            "capo_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
        ] = None,
        chat_channel: Optional[
            "capo_ssm_incidents.types.chat_channel.ChatChannel"
        ] = None,
        engagements: Optional[
            "capo_ssm_incidents.types.engagement_set.EngagementSet"
        ] = None,
        actions: Optional["capo_ssm_incidents.types.actions_list.ActionsList"] = None,
        tags: Optional["capo_ssm_incidents.types.tag_map.TagMap"] = None,
        integrations: Optional[
            "capo_ssm_incidents.types.integrations.Integrations"
        ] = None,
    ) -> (
        "capo_ssm_incidents.types.create_response_plan_output.CreateResponsePlanOutput"
    ):
        """<p>Creates a response plan that automates the initial response to incidents. A response plan engages contacts, starts chat channel collaboration, and initiates runbooks at the beginning of an incident.</p>

        Args:
            client_token: <p>A token ensuring that the operation is called only once with the specified details.</p>
            name: <p>The short format name of the response plan. Can't include spaces.</p>
            display_name: <p>The long format of the response plan name. This field can contain spaces.</p>
            incident_template: <p>Details used to create an incident when using this response plan.</p>
            chat_channel: <p>The Chatbot chat channel used for collaboration during an incident.</p>
            engagements: <p>The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.</p>
            actions: <p>The actions that the response plan starts at the beginning of an incident.</p>
            tags: <p>A list of tags that you are adding to the response plan.</p>
            integrations: <p>Information about third-party services integrated into the response plan.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.create_response_plan_input.CreateResponsePlanInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.create_response_plan_output.CreateResponsePlanOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.create_response_plan

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.create_response_plan.create_response_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.create_response_plan_input.CreateResponsePlanInput = {
            "name": name,
            "incident_template": incident_template,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if chat_channel is not None:
            input_["chat_channel"] = chat_channel
        if engagements is not None:
            input_["engagements"] = engagements
        if actions is not None:
            input_["actions"] = actions
        if tags is not None:
            input_["tags"] = tags
        if integrations is not None:
            input_["integrations"] = integrations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_timeline_event(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        event_time: datetime.datetime,
        event_type: "capo_ssm_incidents.types.timeline_event_type.TimelineEventType",
        event_data: "capo_ssm_incidents.types.event_data.EventData",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
        event_references: Optional[
            "capo_ssm_incidents.types.event_reference_list.EventReferenceList"
        ] = None,
    ) -> "capo_ssm_incidents.types.create_timeline_event_output.CreateTimelineEventOutput":
        """<p>Creates a custom timeline event on the incident details page of an incident record. Incident Manager automatically creates timeline events that mark key moments during an incident. You can create custom timeline events to mark important events that Incident Manager can detect automatically.</p>

        Args:
            client_token: <p>A token that ensures that a client calls the action only once with the specified details.</p>
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident record that the action adds the incident to.</p>
            event_time: <p>The timestamp for when the event occurred.</p>
            event_type: <p>The type of event. You can create timeline events of type <code>Custom Event</code> and <code>Note</code>.</p> <p>To make a Note-type event appear on the <i>Incident notes</i> panel in the console, specify <code>eventType</code> as <code>Note</code>and enter the Amazon Resource Name (ARN) of the incident as the value for <code>eventReference</code>.</p>
            event_data: <p>A short description of the event.</p>
            event_references: <p>Adds one or more references to the <code>TimelineEvent</code>. A reference is an Amazon Web Services resource involved or associated with the incident. To specify a reference, enter its Amazon Resource Name (ARN). You can also specify a related item associated with a resource. For example, to specify an Amazon DynamoDB (DynamoDB) table as a resource, use the table's ARN. You can also specify an Amazon CloudWatch metric associated with the DynamoDB table as a related item.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.create_timeline_event_input.CreateTimelineEventInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.create_timeline_event_output.CreateTimelineEventOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.create_timeline_event

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.create_timeline_event.create_timeline_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.create_timeline_event_input.CreateTimelineEventInput = {
            "incident_record_arn": incident_record_arn,
            "event_time": event_time,
            "event_type": event_type,
            "event_data": event_data,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if event_references is not None:
            input_["event_references"] = event_references

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_incident_record(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.delete_incident_record_output.DeleteIncidentRecordOutput":
        """<p>Delete an incident record from Incident Manager. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the incident record you are deleting.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.delete_incident_record_input.DeleteIncidentRecordInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.delete_incident_record_output.DeleteIncidentRecordOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.delete_incident_record

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.delete_incident_record.delete_incident_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.delete_incident_record_input.DeleteIncidentRecordInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_replication_set(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.delete_replication_set_output.DeleteReplicationSetOutput":
        """<p>Deletes all Regions in your replication set. Deleting the replication set deletes all Incident Manager data.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the replication set you're deleting.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.delete_replication_set_input.DeleteReplicationSetInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.delete_replication_set_output.DeleteReplicationSetOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.delete_replication_set

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.delete_replication_set.delete_replication_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.delete_replication_set_input.DeleteReplicationSetInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "capo_ssm_incidents.types.arn.Arn",
        policy_id: "capo_ssm_incidents.types.policy_id.PolicyId",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.delete_resource_policy_output.DeleteResourcePolicyOutput":
        """<p>Deletes the resource policy that Resource Access Manager uses to share your Incident Manager resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you're deleting the policy from.</p>
            policy_id: <p>The ID of the resource policy you're deleting.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.delete_resource_policy_input.DeleteResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.delete_resource_policy_output.DeleteResourcePolicyOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.delete_resource_policy

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.delete_resource_policy_input.DeleteResourcePolicyInput = {
            "resource_arn": resource_arn,
            "policy_id": policy_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_response_plan(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> (
        "capo_ssm_incidents.types.delete_response_plan_output.DeleteResponsePlanOutput"
    ):
        """<p>Deletes the specified response plan. Deleting a response plan stops all linked CloudWatch alarms and EventBridge events from creating an incident with this response plan.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the response plan.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.delete_response_plan_input.DeleteResponsePlanInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.delete_response_plan_output.DeleteResponsePlanOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.delete_response_plan

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.delete_response_plan.delete_response_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.delete_response_plan_input.DeleteResponsePlanInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_timeline_event(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        event_id: "capo_ssm_incidents.types.uuid.UUID",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.delete_timeline_event_output.DeleteTimelineEventOutput":
        """<p>Deletes a timeline event from an incident.</p>

        Args:
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>
            event_id: <p>The ID of the event to update. You can use <code>ListTimelineEvents</code> to find an event's ID.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.delete_timeline_event_input.DeleteTimelineEventInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.delete_timeline_event_output.DeleteTimelineEventOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.delete_timeline_event

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.delete_timeline_event.delete_timeline_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.delete_timeline_event_input.DeleteTimelineEventInput = {
            "incident_record_arn": incident_record_arn,
            "event_id": event_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_incident_record(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.get_incident_record_output.GetIncidentRecordOutput":
        """<p>Returns the details for the specified incident record.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the incident record.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.get_incident_record_input.GetIncidentRecordInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.get_incident_record_output.GetIncidentRecordOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.get_incident_record

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.get_incident_record.get_incident_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.get_incident_record_input.GetIncidentRecordInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_replication_set(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.get_replication_set_output.GetReplicationSetOutput":
        """<p>Retrieve your Incident Manager replication set.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the replication set you want to retrieve.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.get_replication_set_input.GetReplicationSetInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.get_replication_set_output.GetReplicationSetOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.get_replication_set

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.get_replication_set.get_replication_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.get_replication_set_input.GetReplicationSetInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policies(
        self,
        resource_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_incidents.types.get_resource_policies_output.GetResourcePoliciesOutput":
        """<p>Retrieves the resource policies attached to the specified response plan.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the response plan with the attached resource policy. </p>
            max_results: <p>The maximum number of resource policies to display for each page of results.</p>
            next_token: <p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.get_resource_policies_input.GetResourcePoliciesInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.get_resource_policies_output.GetResourcePoliciesOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.get_resource_policies

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.get_resource_policies.get_resource_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.get_resource_policies_input.GetResourcePoliciesInput = {
            "resource_arn": resource_arn
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

    def iter_get_resource_policies(
        self,
        resource_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_ssm_incidents.types.resource_policy.ResourcePolicy]":
        _token = next_token
        while True:
            _response = self.get_resource_policies(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_response_plan(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.get_response_plan_output.GetResponsePlanOutput":
        """<p>Retrieves the details of the specified response plan.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the response plan.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.get_response_plan_input.GetResponsePlanInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.get_response_plan_output.GetResponsePlanOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.get_response_plan

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.get_response_plan.get_response_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.get_response_plan_input.GetResponsePlanInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_timeline_event(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        event_id: "capo_ssm_incidents.types.uuid.UUID",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.get_timeline_event_output.GetTimelineEventOutput":
        """<p>Retrieves a timeline event based on its ID and incident record.</p>

        Args:
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>
            event_id: <p>The ID of the event. You can get an event's ID when you create it, or by using <code>ListTimelineEvents</code>.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.get_timeline_event_input.GetTimelineEventInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.get_timeline_event_output.GetTimelineEventOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.get_timeline_event

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.get_timeline_event.get_timeline_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.get_timeline_event_input.GetTimelineEventInput = {
            "incident_record_arn": incident_record_arn,
            "event_id": event_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_incident_findings(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_incidents.types.list_incident_findings_output.ListIncidentFindingsOutput":
        """<p>Retrieves a list of the IDs of findings, plus their last modified times, that have been identified for a specified incident. A finding represents a recent application environment change made by an CloudFormation stack creation or update or an CodeDeploy deployment that can be investigated as a potential cause of the incident.</p>

        Args:
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident for which you want to view associated findings.</p>
            max_results: <p>The maximum number of findings to retrieve per call.</p>
            next_token: <p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.list_incident_findings_input.ListIncidentFindingsInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.list_incident_findings_output.ListIncidentFindingsOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.list_incident_findings

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.list_incident_findings.list_incident_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.list_incident_findings_input.ListIncidentFindingsInput = {
            "incident_record_arn": incident_record_arn
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

    def iter_list_incident_findings(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_ssm_incidents.types.finding_summary.FindingSummary]":
        _token = next_token
        while True:
            _response = self.list_incident_findings(
                incident_record_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_incident_records(
        self,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        filters: Optional["capo_ssm_incidents.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_incidents.types.list_incident_records_output.ListIncidentRecordsOutput":
        """<p>Lists all incident records in your account. Use this command to retrieve the Amazon Resource Name (ARN) of the incident record you want to update. </p>

        Args:
            filters: <p>Filters the list of incident records you want to search through. You can filter on the following keys:</p> <ul> <li> <p> <code>creationTime</code> </p> </li> <li> <p> <code>impact</code> </p> </li> <li> <p> <code>status</code> </p> </li> <li> <p> <code>createdBy</code> </p> </li> </ul> <p>Note the following when when you use Filters:</p> <ul> <li> <p>If you don't specify a Filter, the response includes all incident records.</p> </li> <li> <p>If you specify more than one filter in a single request, the response returns incident records that match all filters.</p> </li> <li> <p>If you specify a filter with more than one value, the response returns incident records that match any of the values provided.</p> </li> </ul>
            max_results: <p>The maximum number of results per page.</p>
            next_token: <p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.list_incident_records_input.ListIncidentRecordsInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.list_incident_records_output.ListIncidentRecordsOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.list_incident_records

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.list_incident_records.list_incident_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.list_incident_records_input.ListIncidentRecordsInput = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_incident_records(
        self,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        filters: Optional["capo_ssm_incidents.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_ssm_incidents.types.incident_record_summary.IncidentRecordSummary]":
        _token = next_token
        while True:
            _response = self.list_incident_records(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("incident_record_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_related_items(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_incidents.types.list_related_items_output.ListRelatedItemsOutput":
        """<p>List all related items for an incident record.</p>

        Args:
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident record containing the listed related items.</p>
            max_results: <p>The maximum number of related items per page.</p>
            next_token: <p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.list_related_items_input.ListRelatedItemsInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.list_related_items_output.ListRelatedItemsOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.list_related_items

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.list_related_items.list_related_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.list_related_items_input.ListRelatedItemsInput = {
            "incident_record_arn": incident_record_arn
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

    def iter_list_related_items(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_ssm_incidents.types.related_item.RelatedItem]":
        _token = next_token
        while True:
            _response = self.list_related_items(
                incident_record_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("related_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_replication_sets(
        self,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_incidents.types.list_replication_sets_output.ListReplicationSetsOutput":
        """<p>Lists details about the replication set configured in your account. </p>

        Args:
            max_results: <p>The maximum number of results per page. </p>
            next_token: <p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.list_replication_sets_input.ListReplicationSetsInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.list_replication_sets_output.ListReplicationSetsOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.list_replication_sets

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.list_replication_sets.list_replication_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.list_replication_sets_input.ListReplicationSetsInput = {}
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

    def iter_list_replication_sets(
        self,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_ssm_incidents.types.arn.Arn]":
        _token = next_token
        while True:
            _response = self.list_replication_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("replication_set_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_response_plans(
        self,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "capo_ssm_incidents.types.list_response_plans_output.ListResponsePlansOutput":
        """<p>Lists all response plans in your account.</p>

        Args:
            max_results: <p>The maximum number of response plans per page.</p>
            next_token: <p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.list_response_plans_input.ListResponsePlansInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.list_response_plans_output.ListResponsePlansOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.list_response_plans

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.list_response_plans.list_response_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.list_response_plans_input.ListResponsePlansInput = {}
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

    def iter_list_response_plans(
        self,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_ssm_incidents.types.response_plan_summary.ResponsePlanSummary]":
        _token = next_token
        while True:
            _response = self.list_response_plans(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("response_plan_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags that are attached to the specified response plan or incident.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the response plan or incident.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.list_tags_for_resource

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_timeline_events(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        filters: Optional["capo_ssm_incidents.types.filter_list.FilterList"] = None,
        sort_by: Optional[
            "capo_ssm_incidents.types.timeline_event_sort.TimelineEventSort"
        ] = None,
        sort_order: Optional["capo_ssm_incidents.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> (
        "capo_ssm_incidents.types.list_timeline_events_output.ListTimelineEventsOutput"
    ):
        """<p>Lists timeline events for the specified incident record.</p>

        Args:
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>
            filters: <p>Filters the timeline events based on the provided conditional values. You can filter timeline events with the following keys:</p> <ul> <li> <p> <code>eventReference</code> </p> </li> <li> <p> <code>eventTime</code> </p> </li> <li> <p> <code>eventType</code> </p> </li> </ul> <p>Note the following when deciding how to use Filters:</p> <ul> <li> <p>If you don't specify a Filter, the response includes all timeline events.</p> </li> <li> <p>If you specify more than one filter in a single request, the response returns timeline events that match all filters.</p> </li> <li> <p>If you specify a filter with more than one value, the response returns timeline events that match any of the values provided.</p> </li> </ul>
            sort_by: <p>Sort timeline events by the specified key value pair.</p>
            sort_order: <p>Sorts the order of timeline events by the value specified in the <code>sortBy</code> field.</p>
            max_results: <p>The maximum number of results per page.</p>
            next_token: <p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.list_timeline_events_input.ListTimelineEventsInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.list_timeline_events_output.ListTimelineEventsOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.list_timeline_events

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.list_timeline_events.list_timeline_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.list_timeline_events_input.ListTimelineEventsInput = {
            "incident_record_arn": incident_record_arn
        }
        if filters is not None:
            input_["filters"] = filters
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_list_timeline_events(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        filters: Optional["capo_ssm_incidents.types.filter_list.FilterList"] = None,
        sort_by: Optional[
            "capo_ssm_incidents.types.timeline_event_sort.TimelineEventSort"
        ] = None,
        sort_order: Optional["capo_ssm_incidents.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_ssm_incidents.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm_incidents.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_ssm_incidents.types.event_summary.EventSummary]":
        _token = next_token
        while True:
            _response = self.list_timeline_events(
                incident_record_arn,
                config_overrides=config_overrides,
                filters=filters,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("event_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_resource_policy(
        self,
        resource_arn: "capo_ssm_incidents.types.arn.Arn",
        policy: "capo_ssm_incidents.types.policy.Policy",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.put_resource_policy_output.PutResourcePolicyOutput":
        """<p>Adds a resource policy to the specified response plan. The resource policy is used to share the response plan using Resource Access Manager (RAM). For more information about cross-account sharing, see <a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-cross-account-cross-region.html">Cross-Region and cross-account incident management</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the response plan to add the resource policy to.</p>
            policy: <p>Details of the resource policy.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.put_resource_policy_input.PutResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.put_resource_policy_output.PutResourcePolicyOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.put_resource_policy

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.put_resource_policy_input.PutResourcePolicyInput = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_incident(
        self,
        response_plan_arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
        title: Optional["capo_ssm_incidents.types.incident_title.IncidentTitle"] = None,
        impact: Optional["capo_ssm_incidents.types.impact.Impact"] = None,
        trigger_details: Optional[
            "capo_ssm_incidents.types.trigger_details.TriggerDetails"
        ] = None,
        related_items: Optional[
            "capo_ssm_incidents.types.related_item_list.RelatedItemList"
        ] = None,
    ) -> "capo_ssm_incidents.types.start_incident_output.StartIncidentOutput":
        """<p>Used to start an incident from CloudWatch alarms, EventBridge events, or manually. </p>

        Args:
            client_token: <p>A token ensuring that the operation is called only once with the specified details.</p>
            response_plan_arn: <p>The Amazon Resource Name (ARN) of the response plan that pre-defines summary, chat channels, Amazon SNS topics, runbooks, title, and impact of the incident. </p>
            title: <p>Provide a title for the incident. Providing a title overwrites the title provided by the response plan. </p>
            impact: <p>Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>
            trigger_details: <p>Details of what created the incident record in Incident Manager.</p>
            related_items: <p>Add related items to the incident for other responders to use. Related items are Amazon Web Services resources, external links, or files uploaded to an Amazon S3 bucket. </p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.start_incident_input.StartIncidentInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.start_incident_output.StartIncidentOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.start_incident

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.start_incident.start_incident(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.start_incident_input.StartIncidentInput = {
            "response_plan_arn": response_plan_arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if title is not None:
            input_["title"] = title
        if impact is not None:
            input_["impact"] = impact
        if trigger_details is not None:
            input_["trigger_details"] = trigger_details
        if related_items is not None:
            input_["related_items"] = related_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_ssm_incidents.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a response plan.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the response plan you're adding the tags to.</p>
            tags: <p>A list of tags to add to the response plan.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.tag_resource

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_ssm_incidents.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
    ) -> "capo_ssm_incidents.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the response plan you're removing a tag from.</p>
            tag_keys: <p>The name of the tag to remove from the response plan.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.untag_resource

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.untag_resource_request.UntagResourceRequest = {
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

    def update_deletion_protection(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        deletion_protected: bool,
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_ssm_incidents.types.update_deletion_protection_output.UpdateDeletionProtectionOutput":
        """<p>Update deletion protection to either allow or deny deletion of the final Region in a replication set.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the replication set to update.</p>
            deletion_protected: <p>Specifies if deletion protection is turned on or off in your account. </p>
            client_token: <p>A token that ensures that the operation is called only once with the specified details.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.update_deletion_protection_input.UpdateDeletionProtectionInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.update_deletion_protection_output.UpdateDeletionProtectionOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.update_deletion_protection

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.update_deletion_protection.update_deletion_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.update_deletion_protection_input.UpdateDeletionProtectionInput = {
            "arn": arn,
            "deletion_protected": deletion_protected,
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

    def update_incident_record(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
        title: Optional["capo_ssm_incidents.types.incident_title.IncidentTitle"] = None,
        summary: Optional[
            "capo_ssm_incidents.types.incident_summary.IncidentSummary"
        ] = None,
        impact: Optional["capo_ssm_incidents.types.impact.Impact"] = None,
        status: Optional[
            "capo_ssm_incidents.types.incident_record_status.IncidentRecordStatus"
        ] = None,
        chat_channel: Optional[
            "capo_ssm_incidents.types.chat_channel.ChatChannel"
        ] = None,
        notification_targets: Optional[
            "capo_ssm_incidents.types.notification_target_set.NotificationTargetSet"
        ] = None,
    ) -> "capo_ssm_incidents.types.update_incident_record_output.UpdateIncidentRecordOutput":
        """<p>Update the details of an incident record. You can use this operation to update an incident record from the defined chat channel. For more information about using actions in chat channels, see <a href="https://docs.aws.amazon.com/incident-manager/latest/userguide/chat.html#chat-interact">Interacting through chat</a>.</p>

        Args:
            client_token: <p>A token that ensures that a client calls the operation only once with the specified details.</p>
            arn: <p>The Amazon Resource Name (ARN) of the incident record you are updating.</p>
            title: <p>A brief description of the incident.</p>
            summary: <p>A longer description of what occurred during the incident.</p>
            impact: <p>Defines the impact of the incident to customers and applications. If you provide an impact for an incident, it overwrites the impact provided by the response plan.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>
            status: <p>The status of the incident. Possible statuses are <code>Open</code> or <code>Resolved</code>.</p>
            chat_channel: <p>The Chatbot chat channel where responders can collaborate.</p>
            notification_targets: <p>The Amazon SNS targets that Incident Manager notifies when a client updates an incident.</p> <p>Using multiple SNS topics creates redundancy in the event that a Region is down during the incident.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.update_incident_record_input.UpdateIncidentRecordInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.update_incident_record_output.UpdateIncidentRecordOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.update_incident_record

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.update_incident_record.update_incident_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.update_incident_record_input.UpdateIncidentRecordInput = {
            "arn": arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if title is not None:
            input_["title"] = title
        if summary is not None:
            input_["summary"] = summary
        if impact is not None:
            input_["impact"] = impact
        if status is not None:
            input_["status"] = status
        if chat_channel is not None:
            input_["chat_channel"] = chat_channel
        if notification_targets is not None:
            input_["notification_targets"] = notification_targets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_related_items(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        related_items_update: "capo_ssm_incidents.types.related_items_update.RelatedItemsUpdate",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_ssm_incidents.types.update_related_items_output.UpdateRelatedItemsOutput"
    ):
        """<p>Add or remove related items from the related items tab of an incident record.</p>

        Args:
            client_token: <p>A token that ensures that a client calls the operation only once with the specified details.</p>
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident record that contains the related items that you update.</p>
            related_items_update: <p>Details about the item that you are add to, or delete from, an incident.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.update_related_items_input.UpdateRelatedItemsInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.update_related_items_output.UpdateRelatedItemsOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.update_related_items

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.update_related_items.update_related_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.update_related_items_input.UpdateRelatedItemsInput = {
            "incident_record_arn": incident_record_arn,
            "related_items_update": related_items_update,
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

    def update_replication_set(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        actions: "capo_ssm_incidents.types.update_action_list.UpdateActionList",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_ssm_incidents.types.update_replication_set_output.UpdateReplicationSetOutput":
        """<p>Add or delete Regions from your replication set.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the replication set you're updating.</p>
            actions: <p>An action to add or delete a Region.</p>
            client_token: <p>A token that ensures that the operation is called only once with the specified details.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.update_replication_set_input.UpdateReplicationSetInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.update_replication_set_output.UpdateReplicationSetOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.update_replication_set

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.update_replication_set.update_replication_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.update_replication_set_input.UpdateReplicationSetInput = {
            "arn": arn,
            "actions": actions,
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

    def update_response_plan(
        self,
        arn: "capo_ssm_incidents.types.arn.Arn",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
        display_name: Optional[
            "capo_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
        ] = None,
        incident_template_title: Optional[
            "capo_ssm_incidents.types.incident_title.IncidentTitle"
        ] = None,
        incident_template_impact: Optional[
            "capo_ssm_incidents.types.impact.Impact"
        ] = None,
        incident_template_summary: Optional[
            "capo_ssm_incidents.types.incident_summary.IncidentSummary"
        ] = None,
        incident_template_dedupe_string: Optional[
            "capo_ssm_incidents.types.dedupe_string.DedupeString"
        ] = None,
        incident_template_notification_targets: Optional[
            "capo_ssm_incidents.types.notification_target_set.NotificationTargetSet"
        ] = None,
        chat_channel: Optional[
            "capo_ssm_incidents.types.chat_channel.ChatChannel"
        ] = None,
        engagements: Optional[
            "capo_ssm_incidents.types.engagement_set.EngagementSet"
        ] = None,
        actions: Optional["capo_ssm_incidents.types.actions_list.ActionsList"] = None,
        incident_template_tags: Optional[
            "capo_ssm_incidents.types.tag_map_update.TagMapUpdate"
        ] = None,
        integrations: Optional[
            "capo_ssm_incidents.types.integrations.Integrations"
        ] = None,
    ) -> (
        "capo_ssm_incidents.types.update_response_plan_output.UpdateResponsePlanOutput"
    ):
        """<p>Updates the specified response plan.</p>

        Args:
            client_token: <p>A token ensuring that the operation is called only once with the specified details.</p>
            arn: <p>The Amazon Resource Name (ARN) of the response plan.</p>
            display_name: <p>The long format name of the response plan. The display name can't contain spaces.</p>
            incident_template_title: <p>The short format name of the incident. The title can't contain spaces.</p>
            incident_template_impact: <p>Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>
            incident_template_summary: <p>A brief summary of the incident. This typically contains what has happened, what's currently happening, and next steps.</p>
            incident_template_dedupe_string: <p>The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.</p>
            incident_template_notification_targets: <p>The Amazon SNS targets that are notified when updates are made to an incident.</p>
            chat_channel: <p>The Chatbot chat channel used for collaboration during an incident.</p> <p>Use the empty structure to remove the chat channel from the response plan.</p>
            engagements: <p>The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.</p>
            actions: <p>The actions that this response plan takes at the beginning of an incident.</p>
            incident_template_tags: <p>Tags to assign to the template. When the <code>StartIncident</code> API action is called, Incident Manager assigns the tags specified in the template to the incident. To call this action, you must also have permission to call the <code>TagResource</code> API action for the incident record resource.</p>
            integrations: <p>Information about third-party services integrated into the response plan.</p>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.update_response_plan_input.UpdateResponsePlanInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.update_response_plan_output.UpdateResponsePlanOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.update_response_plan

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.update_response_plan.update_response_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.update_response_plan_input.UpdateResponsePlanInput = {
            "arn": arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if incident_template_title is not None:
            input_["incident_template_title"] = incident_template_title
        if incident_template_impact is not None:
            input_["incident_template_impact"] = incident_template_impact
        if incident_template_summary is not None:
            input_["incident_template_summary"] = incident_template_summary
        if incident_template_dedupe_string is not None:
            input_["incident_template_dedupe_string"] = incident_template_dedupe_string
        if incident_template_notification_targets is not None:
            input_["incident_template_notification_targets"] = (
                incident_template_notification_targets
            )
        if chat_channel is not None:
            input_["chat_channel"] = chat_channel
        if engagements is not None:
            input_["engagements"] = engagements
        if actions is not None:
            input_["actions"] = actions
        if incident_template_tags is not None:
            input_["incident_template_tags"] = incident_template_tags
        if integrations is not None:
            input_["integrations"] = integrations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_timeline_event(
        self,
        incident_record_arn: "capo_ssm_incidents.types.arn.Arn",
        event_id: "capo_ssm_incidents.types.uuid.UUID",
        *,
        config_overrides: Optional[SSMIncidentsClientConfig] = None,
        client_token: Optional[
            "capo_ssm_incidents.types.client_token.ClientToken"
        ] = None,
        event_time: Optional[datetime.datetime] = None,
        event_type: Optional[
            "capo_ssm_incidents.types.timeline_event_type.TimelineEventType"
        ] = None,
        event_data: Optional["capo_ssm_incidents.types.event_data.EventData"] = None,
        event_references: Optional[
            "capo_ssm_incidents.types.event_reference_list.EventReferenceList"
        ] = None,
    ) -> "capo_ssm_incidents.types.update_timeline_event_output.UpdateTimelineEventOutput":
        """<p>Updates a timeline event. You can update events of type <code>Custom Event</code>.</p>

        Args:
            client_token: <p>A token that ensures that a client calls the operation only once with the specified details.</p>
            incident_record_arn: <p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>
            event_id: <p>The ID of the event to update. You can use <code>ListTimelineEvents</code> to find an event's ID.</p>
            event_time: <p>The timestamp for when the event occurred.</p>
            event_type: <p>The type of event. You can update events of type <code>Custom Event</code> and <code>Note</code>.</p>
            event_data: <p>A short description of the event.</p>
            event_references: <p>Updates all existing references in a <code>TimelineEvent</code>. A reference is an Amazon Web Services resource involved or associated with the incident. To specify a reference, enter its Amazon Resource Name (ARN). You can also specify a related item associated with that resource. For example, to specify an Amazon DynamoDB (DynamoDB) table as a resource, use its ARN. You can also specify an Amazon CloudWatch metric associated with the DynamoDB table as a related item.</p> <important> <p>This update action overrides all existing references. If you want to keep existing references, you must specify them in the call. If you don't, this action removes any existing references and enters only new references.</p> </important>

        Raises:
            capo_ssm_incidents.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation.</p>
            capo_ssm_incidents.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource causes an inconsistent state.</p>
            capo_ssm_incidents.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_incidents.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which doesn't exist. </p>
            capo_ssm_incidents.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_incidents.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ssm_incidents.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ssm_incidents.types.update_timeline_event_input.UpdateTimelineEventInput]",
        ) -> OperationResponse[
            "capo_ssm_incidents.types.update_timeline_event_output.UpdateTimelineEventOutput"
        ]:
            import capo_ssm_incidents._operations.ssm_incidents.update_timeline_event

            output, http_response = (
                capo_ssm_incidents._operations.ssm_incidents.update_timeline_event.update_timeline_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_incidents.types.update_timeline_event_input.UpdateTimelineEventInput = {
            "incident_record_arn": incident_record_arn,
            "event_id": event_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if event_time is not None:
            input_["event_time"] = event_time
        if event_type is not None:
            input_["event_type"] = event_type
        if event_data is not None:
            input_["event_data"] = event_data
        if event_references is not None:
            input_["event_references"] = event_references

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
