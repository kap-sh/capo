"""Generated from Smithy shape ``com.amazonaws.pinpoint#Pinpoint``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_pinpoint._auth._signers
import capo_pinpoint._auth._sigv4
from capo_pinpoint._auth._identity import Credentials
from capo_pinpoint._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pinpoint._auth._zapros_handler import AuthMiddleware
from capo_pinpoint._services._aws_config import aws_config
from capo_pinpoint._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.__timestamp_iso8601
    import capo_pinpoint.types.adm_channel_request
    import capo_pinpoint.types.apns_channel_request
    import capo_pinpoint.types.apns_sandbox_channel_request
    import capo_pinpoint.types.apns_voip_channel_request
    import capo_pinpoint.types.apns_voip_sandbox_channel_request
    import capo_pinpoint.types.baidu_channel_request
    import capo_pinpoint.types.create_app_request
    import capo_pinpoint.types.create_app_response
    import capo_pinpoint.types.create_application_request
    import capo_pinpoint.types.create_campaign_request
    import capo_pinpoint.types.create_campaign_response
    import capo_pinpoint.types.create_email_template_request
    import capo_pinpoint.types.create_email_template_response
    import capo_pinpoint.types.create_export_job_request
    import capo_pinpoint.types.create_export_job_response
    import capo_pinpoint.types.create_import_job_request
    import capo_pinpoint.types.create_import_job_response
    import capo_pinpoint.types.create_in_app_template_request
    import capo_pinpoint.types.create_in_app_template_response
    import capo_pinpoint.types.create_journey_request
    import capo_pinpoint.types.create_journey_response
    import capo_pinpoint.types.create_push_template_request
    import capo_pinpoint.types.create_push_template_response
    import capo_pinpoint.types.create_recommender_configuration_request
    import capo_pinpoint.types.create_recommender_configuration_response
    import capo_pinpoint.types.create_recommender_configuration_shape
    import capo_pinpoint.types.create_segment_request
    import capo_pinpoint.types.create_segment_response
    import capo_pinpoint.types.create_sms_template_request
    import capo_pinpoint.types.create_sms_template_response
    import capo_pinpoint.types.create_voice_template_request
    import capo_pinpoint.types.create_voice_template_response
    import capo_pinpoint.types.delete_adm_channel_request
    import capo_pinpoint.types.delete_adm_channel_response
    import capo_pinpoint.types.delete_apns_channel_request
    import capo_pinpoint.types.delete_apns_channel_response
    import capo_pinpoint.types.delete_apns_sandbox_channel_request
    import capo_pinpoint.types.delete_apns_sandbox_channel_response
    import capo_pinpoint.types.delete_apns_voip_channel_request
    import capo_pinpoint.types.delete_apns_voip_channel_response
    import capo_pinpoint.types.delete_apns_voip_sandbox_channel_request
    import capo_pinpoint.types.delete_apns_voip_sandbox_channel_response
    import capo_pinpoint.types.delete_app_request
    import capo_pinpoint.types.delete_app_response
    import capo_pinpoint.types.delete_baidu_channel_request
    import capo_pinpoint.types.delete_baidu_channel_response
    import capo_pinpoint.types.delete_campaign_request
    import capo_pinpoint.types.delete_campaign_response
    import capo_pinpoint.types.delete_email_channel_request
    import capo_pinpoint.types.delete_email_channel_response
    import capo_pinpoint.types.delete_email_template_request
    import capo_pinpoint.types.delete_email_template_response
    import capo_pinpoint.types.delete_endpoint_request
    import capo_pinpoint.types.delete_endpoint_response
    import capo_pinpoint.types.delete_event_stream_request
    import capo_pinpoint.types.delete_event_stream_response
    import capo_pinpoint.types.delete_gcm_channel_request
    import capo_pinpoint.types.delete_gcm_channel_response
    import capo_pinpoint.types.delete_in_app_template_request
    import capo_pinpoint.types.delete_in_app_template_response
    import capo_pinpoint.types.delete_journey_request
    import capo_pinpoint.types.delete_journey_response
    import capo_pinpoint.types.delete_push_template_request
    import capo_pinpoint.types.delete_push_template_response
    import capo_pinpoint.types.delete_recommender_configuration_request
    import capo_pinpoint.types.delete_recommender_configuration_response
    import capo_pinpoint.types.delete_segment_request
    import capo_pinpoint.types.delete_segment_response
    import capo_pinpoint.types.delete_sms_channel_request
    import capo_pinpoint.types.delete_sms_channel_response
    import capo_pinpoint.types.delete_sms_template_request
    import capo_pinpoint.types.delete_sms_template_response
    import capo_pinpoint.types.delete_user_endpoints_request
    import capo_pinpoint.types.delete_user_endpoints_response
    import capo_pinpoint.types.delete_voice_channel_request
    import capo_pinpoint.types.delete_voice_channel_response
    import capo_pinpoint.types.delete_voice_template_request
    import capo_pinpoint.types.delete_voice_template_response
    import capo_pinpoint.types.email_channel_request
    import capo_pinpoint.types.email_template_request
    import capo_pinpoint.types.endpoint_batch_request
    import capo_pinpoint.types.endpoint_request
    import capo_pinpoint.types.events_request
    import capo_pinpoint.types.export_job_request
    import capo_pinpoint.types.gcm_channel_request
    import capo_pinpoint.types.get_adm_channel_request
    import capo_pinpoint.types.get_adm_channel_response
    import capo_pinpoint.types.get_apns_channel_request
    import capo_pinpoint.types.get_apns_channel_response
    import capo_pinpoint.types.get_apns_sandbox_channel_request
    import capo_pinpoint.types.get_apns_sandbox_channel_response
    import capo_pinpoint.types.get_apns_voip_channel_request
    import capo_pinpoint.types.get_apns_voip_channel_response
    import capo_pinpoint.types.get_apns_voip_sandbox_channel_request
    import capo_pinpoint.types.get_apns_voip_sandbox_channel_response
    import capo_pinpoint.types.get_app_request
    import capo_pinpoint.types.get_app_response
    import capo_pinpoint.types.get_application_date_range_kpi_request
    import capo_pinpoint.types.get_application_date_range_kpi_response
    import capo_pinpoint.types.get_application_settings_request
    import capo_pinpoint.types.get_application_settings_response
    import capo_pinpoint.types.get_apps_request
    import capo_pinpoint.types.get_apps_response
    import capo_pinpoint.types.get_baidu_channel_request
    import capo_pinpoint.types.get_baidu_channel_response
    import capo_pinpoint.types.get_campaign_activities_request
    import capo_pinpoint.types.get_campaign_activities_response
    import capo_pinpoint.types.get_campaign_date_range_kpi_request
    import capo_pinpoint.types.get_campaign_date_range_kpi_response
    import capo_pinpoint.types.get_campaign_request
    import capo_pinpoint.types.get_campaign_response
    import capo_pinpoint.types.get_campaign_version_request
    import capo_pinpoint.types.get_campaign_version_response
    import capo_pinpoint.types.get_campaign_versions_request
    import capo_pinpoint.types.get_campaign_versions_response
    import capo_pinpoint.types.get_campaigns_request
    import capo_pinpoint.types.get_campaigns_response
    import capo_pinpoint.types.get_channels_request
    import capo_pinpoint.types.get_channels_response
    import capo_pinpoint.types.get_email_channel_request
    import capo_pinpoint.types.get_email_channel_response
    import capo_pinpoint.types.get_email_template_request
    import capo_pinpoint.types.get_email_template_response
    import capo_pinpoint.types.get_endpoint_request
    import capo_pinpoint.types.get_endpoint_response
    import capo_pinpoint.types.get_event_stream_request
    import capo_pinpoint.types.get_event_stream_response
    import capo_pinpoint.types.get_export_job_request
    import capo_pinpoint.types.get_export_job_response
    import capo_pinpoint.types.get_export_jobs_request
    import capo_pinpoint.types.get_export_jobs_response
    import capo_pinpoint.types.get_gcm_channel_request
    import capo_pinpoint.types.get_gcm_channel_response
    import capo_pinpoint.types.get_import_job_request
    import capo_pinpoint.types.get_import_job_response
    import capo_pinpoint.types.get_import_jobs_request
    import capo_pinpoint.types.get_import_jobs_response
    import capo_pinpoint.types.get_in_app_messages_request
    import capo_pinpoint.types.get_in_app_messages_response
    import capo_pinpoint.types.get_in_app_template_request
    import capo_pinpoint.types.get_in_app_template_response
    import capo_pinpoint.types.get_journey_date_range_kpi_request
    import capo_pinpoint.types.get_journey_date_range_kpi_response
    import capo_pinpoint.types.get_journey_execution_activity_metrics_request
    import capo_pinpoint.types.get_journey_execution_activity_metrics_response
    import capo_pinpoint.types.get_journey_execution_metrics_request
    import capo_pinpoint.types.get_journey_execution_metrics_response
    import capo_pinpoint.types.get_journey_request
    import capo_pinpoint.types.get_journey_response
    import capo_pinpoint.types.get_journey_run_execution_activity_metrics_request
    import capo_pinpoint.types.get_journey_run_execution_activity_metrics_response
    import capo_pinpoint.types.get_journey_run_execution_metrics_request
    import capo_pinpoint.types.get_journey_run_execution_metrics_response
    import capo_pinpoint.types.get_journey_runs_request
    import capo_pinpoint.types.get_journey_runs_response
    import capo_pinpoint.types.get_push_template_request
    import capo_pinpoint.types.get_push_template_response
    import capo_pinpoint.types.get_recommender_configuration_request
    import capo_pinpoint.types.get_recommender_configuration_response
    import capo_pinpoint.types.get_recommender_configurations_request
    import capo_pinpoint.types.get_recommender_configurations_response
    import capo_pinpoint.types.get_segment_export_jobs_request
    import capo_pinpoint.types.get_segment_export_jobs_response
    import capo_pinpoint.types.get_segment_import_jobs_request
    import capo_pinpoint.types.get_segment_import_jobs_response
    import capo_pinpoint.types.get_segment_request
    import capo_pinpoint.types.get_segment_response
    import capo_pinpoint.types.get_segment_version_request
    import capo_pinpoint.types.get_segment_version_response
    import capo_pinpoint.types.get_segment_versions_request
    import capo_pinpoint.types.get_segment_versions_response
    import capo_pinpoint.types.get_segments_request
    import capo_pinpoint.types.get_segments_response
    import capo_pinpoint.types.get_sms_channel_request
    import capo_pinpoint.types.get_sms_channel_response
    import capo_pinpoint.types.get_sms_template_request
    import capo_pinpoint.types.get_sms_template_response
    import capo_pinpoint.types.get_user_endpoints_request
    import capo_pinpoint.types.get_user_endpoints_response
    import capo_pinpoint.types.get_voice_channel_request
    import capo_pinpoint.types.get_voice_channel_response
    import capo_pinpoint.types.get_voice_template_request
    import capo_pinpoint.types.get_voice_template_response
    import capo_pinpoint.types.import_job_request
    import capo_pinpoint.types.in_app_template_request
    import capo_pinpoint.types.journey_state_request
    import capo_pinpoint.types.list_journeys_request
    import capo_pinpoint.types.list_journeys_response
    import capo_pinpoint.types.list_of__string
    import capo_pinpoint.types.list_tags_for_resource_request
    import capo_pinpoint.types.list_tags_for_resource_response
    import capo_pinpoint.types.list_template_versions_request
    import capo_pinpoint.types.list_template_versions_response
    import capo_pinpoint.types.list_templates_request
    import capo_pinpoint.types.list_templates_response
    import capo_pinpoint.types.message_request
    import capo_pinpoint.types.number_validate_request
    import capo_pinpoint.types.phone_number_validate_request
    import capo_pinpoint.types.phone_number_validate_response
    import capo_pinpoint.types.push_notification_template_request
    import capo_pinpoint.types.put_event_stream_request
    import capo_pinpoint.types.put_event_stream_response
    import capo_pinpoint.types.put_events_request
    import capo_pinpoint.types.put_events_response
    import capo_pinpoint.types.remove_attributes_request
    import capo_pinpoint.types.remove_attributes_response
    import capo_pinpoint.types.send_messages_request
    import capo_pinpoint.types.send_messages_response
    import capo_pinpoint.types.send_otp_message_request
    import capo_pinpoint.types.send_otp_message_request_parameters
    import capo_pinpoint.types.send_otp_message_response
    import capo_pinpoint.types.send_users_message_request
    import capo_pinpoint.types.send_users_messages_request
    import capo_pinpoint.types.send_users_messages_response
    import capo_pinpoint.types.sms_channel_request
    import capo_pinpoint.types.sms_template_request
    import capo_pinpoint.types.tag_resource_request
    import capo_pinpoint.types.tags_model
    import capo_pinpoint.types.template_active_version_request
    import capo_pinpoint.types.untag_resource_request
    import capo_pinpoint.types.update_adm_channel_request
    import capo_pinpoint.types.update_adm_channel_response
    import capo_pinpoint.types.update_apns_channel_request
    import capo_pinpoint.types.update_apns_channel_response
    import capo_pinpoint.types.update_apns_sandbox_channel_request
    import capo_pinpoint.types.update_apns_sandbox_channel_response
    import capo_pinpoint.types.update_apns_voip_channel_request
    import capo_pinpoint.types.update_apns_voip_channel_response
    import capo_pinpoint.types.update_apns_voip_sandbox_channel_request
    import capo_pinpoint.types.update_apns_voip_sandbox_channel_response
    import capo_pinpoint.types.update_application_settings_request
    import capo_pinpoint.types.update_application_settings_response
    import capo_pinpoint.types.update_attributes_request
    import capo_pinpoint.types.update_baidu_channel_request
    import capo_pinpoint.types.update_baidu_channel_response
    import capo_pinpoint.types.update_campaign_request
    import capo_pinpoint.types.update_campaign_response
    import capo_pinpoint.types.update_email_channel_request
    import capo_pinpoint.types.update_email_channel_response
    import capo_pinpoint.types.update_email_template_request
    import capo_pinpoint.types.update_email_template_response
    import capo_pinpoint.types.update_endpoint_request
    import capo_pinpoint.types.update_endpoint_response
    import capo_pinpoint.types.update_endpoints_batch_request
    import capo_pinpoint.types.update_endpoints_batch_response
    import capo_pinpoint.types.update_gcm_channel_request
    import capo_pinpoint.types.update_gcm_channel_response
    import capo_pinpoint.types.update_in_app_template_request
    import capo_pinpoint.types.update_in_app_template_response
    import capo_pinpoint.types.update_journey_request
    import capo_pinpoint.types.update_journey_response
    import capo_pinpoint.types.update_journey_state_request
    import capo_pinpoint.types.update_journey_state_response
    import capo_pinpoint.types.update_push_template_request
    import capo_pinpoint.types.update_push_template_response
    import capo_pinpoint.types.update_recommender_configuration_request
    import capo_pinpoint.types.update_recommender_configuration_response
    import capo_pinpoint.types.update_recommender_configuration_shape
    import capo_pinpoint.types.update_segment_request
    import capo_pinpoint.types.update_segment_response
    import capo_pinpoint.types.update_sms_channel_request
    import capo_pinpoint.types.update_sms_channel_response
    import capo_pinpoint.types.update_sms_template_request
    import capo_pinpoint.types.update_sms_template_response
    import capo_pinpoint.types.update_template_active_version_request
    import capo_pinpoint.types.update_template_active_version_response
    import capo_pinpoint.types.update_voice_channel_request
    import capo_pinpoint.types.update_voice_channel_response
    import capo_pinpoint.types.update_voice_template_request
    import capo_pinpoint.types.update_voice_template_response
    import capo_pinpoint.types.verify_otp_message_request
    import capo_pinpoint.types.verify_otp_message_request_parameters
    import capo_pinpoint.types.verify_otp_message_response
    import capo_pinpoint.types.voice_channel_request
    import capo_pinpoint.types.voice_template_request
    import capo_pinpoint.types.write_application_settings_request
    import capo_pinpoint.types.write_campaign_request
    import capo_pinpoint.types.write_event_stream
    import capo_pinpoint.types.write_journey_request
    import capo_pinpoint.types.write_segment_request


class PinpointClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class PinpointClient:
    """A client for the ``Pinpoint`` service.

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
        self._config = PinpointClientConfig(
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
        self, config_overrides: Optional[PinpointClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PinpointClientConfig = config_overrides or {}
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

    def create_app(
        self,
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        create_application_request: Optional[
            "capo_pinpoint.types.create_application_request.CreateApplicationRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_app_response.CreateAppResponse":
        """<p>Creates an application.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_app_request.CreateAppRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_app_response.CreateAppResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_app

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_app.create_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_app_request.CreateAppRequest = {}
        if create_application_request is not None:
            input_["create_application_request"] = create_application_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_campaign(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_campaign_request: Optional[
            "capo_pinpoint.types.write_campaign_request.WriteCampaignRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_campaign_response.CreateCampaignResponse":
        """<p>Creates a new campaign for an application or updates the settings of an existing campaign for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_campaign_request.CreateCampaignRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_campaign

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_campaign.create_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_campaign_request.CreateCampaignRequest = {
            "application_id": application_id
        }
        if write_campaign_request is not None:
            input_["write_campaign_request"] = write_campaign_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_email_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        email_template_request: Optional[
            "capo_pinpoint.types.email_template_request.EmailTemplateRequest"
        ] = None,
    ) -> (
        "capo_pinpoint.types.create_email_template_response.CreateEmailTemplateResponse"
    ):
        """<p>Creates a message template for messages that are sent through the email channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_email_template_request.CreateEmailTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_email_template_response.CreateEmailTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_email_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_email_template.create_email_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_email_template_request.CreateEmailTemplateRequest = {
            "template_name": template_name
        }
        if email_template_request is not None:
            input_["email_template_request"] = email_template_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_export_job(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        export_job_request: Optional[
            "capo_pinpoint.types.export_job_request.ExportJobRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_export_job_response.CreateExportJobResponse":
        """<p>Creates an export job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_export_job_request.CreateExportJobRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_export_job_response.CreateExportJobResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_export_job

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_export_job.create_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_export_job_request.CreateExportJobRequest = {
            "application_id": application_id
        }
        if export_job_request is not None:
            input_["export_job_request"] = export_job_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_import_job(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        import_job_request: Optional[
            "capo_pinpoint.types.import_job_request.ImportJobRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_import_job_response.CreateImportJobResponse":
        """<p>Creates an import job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_import_job_request.CreateImportJobRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_import_job_response.CreateImportJobResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_import_job

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_import_job.create_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_import_job_request.CreateImportJobRequest = {
            "application_id": application_id
        }
        if import_job_request is not None:
            input_["import_job_request"] = import_job_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_in_app_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        in_app_template_request: Optional[
            "capo_pinpoint.types.in_app_template_request.InAppTemplateRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_in_app_template_response.CreateInAppTemplateResponse":
        """<p>Creates a new message template for messages using the in-app message channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_in_app_template_request.CreateInAppTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_in_app_template_response.CreateInAppTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_in_app_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_in_app_template.create_in_app_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_in_app_template_request.CreateInAppTemplateRequest = {
            "template_name": template_name
        }
        if in_app_template_request is not None:
            input_["in_app_template_request"] = in_app_template_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_journey(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_journey_request: Optional[
            "capo_pinpoint.types.write_journey_request.WriteJourneyRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_journey_response.CreateJourneyResponse":
        """<p>Creates a journey for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_journey_request.CreateJourneyRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_journey_response.CreateJourneyResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_journey

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_journey.create_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_journey_request.CreateJourneyRequest = {
            "application_id": application_id
        }
        if write_journey_request is not None:
            input_["write_journey_request"] = write_journey_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_push_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        push_notification_template_request: Optional[
            "capo_pinpoint.types.push_notification_template_request.PushNotificationTemplateRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_push_template_response.CreatePushTemplateResponse":
        """<p>Creates a message template for messages that are sent through a push notification channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_push_template_request.CreatePushTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_push_template_response.CreatePushTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_push_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_push_template.create_push_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_push_template_request.CreatePushTemplateRequest = {
            "template_name": template_name
        }
        if push_notification_template_request is not None:
            input_["push_notification_template_request"] = (
                push_notification_template_request
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_recommender_configuration(
        self,
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        create_recommender_configuration: Optional[
            "capo_pinpoint.types.create_recommender_configuration_shape.CreateRecommenderConfigurationShape"
        ] = None,
    ) -> "capo_pinpoint.types.create_recommender_configuration_response.CreateRecommenderConfigurationResponse":
        """<p>Creates an Amazon Pinpoint configuration for a recommender model.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_recommender_configuration_request.CreateRecommenderConfigurationRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_recommender_configuration_response.CreateRecommenderConfigurationResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_recommender_configuration

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_recommender_configuration.create_recommender_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_recommender_configuration_request.CreateRecommenderConfigurationRequest = {}
        if create_recommender_configuration is not None:
            input_["create_recommender_configuration"] = (
                create_recommender_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_segment(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_segment_request: Optional[
            "capo_pinpoint.types.write_segment_request.WriteSegmentRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_segment_response.CreateSegmentResponse":
        """<p>Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_segment_request.CreateSegmentRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_segment_response.CreateSegmentResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_segment

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_segment.create_segment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_segment_request.CreateSegmentRequest = {
            "application_id": application_id
        }
        if write_segment_request is not None:
            input_["write_segment_request"] = write_segment_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sms_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        sms_template_request: Optional[
            "capo_pinpoint.types.sms_template_request.SMSTemplateRequest"
        ] = None,
    ) -> "capo_pinpoint.types.create_sms_template_response.CreateSmsTemplateResponse":
        """<p>Creates a message template for messages that are sent through the SMS channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_sms_template_request.CreateSmsTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_sms_template_response.CreateSmsTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_sms_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_sms_template.create_sms_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_sms_template_request.CreateSmsTemplateRequest = {
            "template_name": template_name
        }
        if sms_template_request is not None:
            input_["sms_template_request"] = sms_template_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_voice_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        voice_template_request: Optional[
            "capo_pinpoint.types.voice_template_request.VoiceTemplateRequest"
        ] = None,
    ) -> (
        "capo_pinpoint.types.create_voice_template_response.CreateVoiceTemplateResponse"
    ):
        """<p>Creates a message template for messages that are sent through the voice channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.create_voice_template_request.CreateVoiceTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.create_voice_template_response.CreateVoiceTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.create_voice_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.create_voice_template.create_voice_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.create_voice_template_request.CreateVoiceTemplateRequest = {
            "template_name": template_name
        }
        if voice_template_request is not None:
            input_["voice_template_request"] = voice_template_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_adm_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_adm_channel_response.DeleteAdmChannelResponse":
        """<p>Disables the ADM channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_adm_channel_request.DeleteAdmChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_adm_channel_response.DeleteAdmChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_adm_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_adm_channel.delete_adm_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_adm_channel_request.DeleteAdmChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_apns_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_apns_channel_response.DeleteApnsChannelResponse":
        """<p>Disables the APNs channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_apns_channel_request.DeleteApnsChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_apns_channel_response.DeleteApnsChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_apns_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_apns_channel.delete_apns_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_apns_channel_request.DeleteApnsChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_apns_sandbox_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_apns_sandbox_channel_response.DeleteApnsSandboxChannelResponse":
        """<p>Disables the APNs sandbox channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_apns_sandbox_channel_request.DeleteApnsSandboxChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_apns_sandbox_channel_response.DeleteApnsSandboxChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_apns_sandbox_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_apns_sandbox_channel.delete_apns_sandbox_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_apns_sandbox_channel_request.DeleteApnsSandboxChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_apns_voip_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_apns_voip_channel_response.DeleteApnsVoipChannelResponse":
        """<p>Disables the APNs VoIP channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_apns_voip_channel_request.DeleteApnsVoipChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_apns_voip_channel_response.DeleteApnsVoipChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_apns_voip_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_apns_voip_channel.delete_apns_voip_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_apns_voip_channel_request.DeleteApnsVoipChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_apns_voip_sandbox_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_apns_voip_sandbox_channel_response.DeleteApnsVoipSandboxChannelResponse":
        """<p>Disables the APNs VoIP sandbox channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_apns_voip_sandbox_channel_request.DeleteApnsVoipSandboxChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_apns_voip_sandbox_channel_response.DeleteApnsVoipSandboxChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_apns_voip_sandbox_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_apns_voip_sandbox_channel.delete_apns_voip_sandbox_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_apns_voip_sandbox_channel_request.DeleteApnsVoipSandboxChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_app(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_app_response.DeleteAppResponse":
        """<p>Deletes an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_app_request.DeleteAppRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_app_response.DeleteAppResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_app

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_app.delete_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_app_request.DeleteAppRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_baidu_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_baidu_channel_response.DeleteBaiduChannelResponse":
        """<p>Disables the Baidu channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_baidu_channel_request.DeleteBaiduChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_baidu_channel_response.DeleteBaiduChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_baidu_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_baidu_channel.delete_baidu_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_baidu_channel_request.DeleteBaiduChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_campaign(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        campaign_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_campaign_response.DeleteCampaignResponse":
        """<p>Deletes a campaign from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_campaign_response.DeleteCampaignResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_campaign

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_campaign.delete_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_campaign_request.DeleteCampaignRequest = {
            "application_id": application_id,
            "campaign_id": campaign_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_email_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_email_channel_response.DeleteEmailChannelResponse":
        """<p>Disables the email channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_email_channel_request.DeleteEmailChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_email_channel_response.DeleteEmailChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_email_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_email_channel.delete_email_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_email_channel_request.DeleteEmailChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_email_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> (
        "capo_pinpoint.types.delete_email_template_response.DeleteEmailTemplateResponse"
    ):
        """<p>Deletes a message template for messages that were sent through the email channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_email_template_request.DeleteEmailTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_email_template_response.DeleteEmailTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_email_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_email_template.delete_email_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_email_template_request.DeleteEmailTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_endpoint(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        endpoint_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_endpoint_response.DeleteEndpointResponse":
        """<p>Deletes an endpoint from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_endpoint_request.DeleteEndpointRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_endpoint_response.DeleteEndpointResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_endpoint

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_endpoint.delete_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_endpoint_request.DeleteEndpointRequest = {
            "application_id": application_id,
            "endpoint_id": endpoint_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_stream(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_event_stream_response.DeleteEventStreamResponse":
        """<p>Deletes the event stream for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_event_stream_request.DeleteEventStreamRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_event_stream_response.DeleteEventStreamResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_event_stream

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_event_stream.delete_event_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_event_stream_request.DeleteEventStreamRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gcm_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_gcm_channel_response.DeleteGcmChannelResponse":
        """<p>Disables the GCM channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_gcm_channel_request.DeleteGcmChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_gcm_channel_response.DeleteGcmChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_gcm_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_gcm_channel.delete_gcm_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_gcm_channel_request.DeleteGcmChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_in_app_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.delete_in_app_template_response.DeleteInAppTemplateResponse":
        """<p>Deletes a message template for messages sent using the in-app message channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_in_app_template_request.DeleteInAppTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_in_app_template_response.DeleteInAppTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_in_app_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_in_app_template.delete_in_app_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_in_app_template_request.DeleteInAppTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_journey(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_journey_response.DeleteJourneyResponse":
        """<p>Deletes a journey from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_journey_request.DeleteJourneyRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_journey_response.DeleteJourneyResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_journey

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_journey.delete_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_journey_request.DeleteJourneyRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_push_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.delete_push_template_response.DeletePushTemplateResponse":
        """<p>Deletes a message template for messages that were sent through a push notification channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_push_template_request.DeletePushTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_push_template_response.DeletePushTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_push_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_push_template.delete_push_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_push_template_request.DeletePushTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recommender_configuration(
        self,
        recommender_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_recommender_configuration_response.DeleteRecommenderConfigurationResponse":
        """<p>Deletes an Amazon Pinpoint configuration for a recommender model.</p>

        Args:
            recommender_id: <p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_recommender_configuration_request.DeleteRecommenderConfigurationRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_recommender_configuration_response.DeleteRecommenderConfigurationResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_recommender_configuration

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_recommender_configuration.delete_recommender_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_recommender_configuration_request.DeleteRecommenderConfigurationRequest = {
            "recommender_id": recommender_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_segment(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        segment_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_segment_response.DeleteSegmentResponse":
        """<p>Deletes a segment from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_segment_request.DeleteSegmentRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_segment_response.DeleteSegmentResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_segment

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_segment.delete_segment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_segment_request.DeleteSegmentRequest = {
            "application_id": application_id,
            "segment_id": segment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sms_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_sms_channel_response.DeleteSmsChannelResponse":
        """<p>Disables the SMS channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_sms_channel_request.DeleteSmsChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_sms_channel_response.DeleteSmsChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_sms_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_sms_channel.delete_sms_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_sms_channel_request.DeleteSmsChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sms_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.delete_sms_template_response.DeleteSmsTemplateResponse":
        """<p>Deletes a message template for messages that were sent through the SMS channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_sms_template_request.DeleteSmsTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_sms_template_response.DeleteSmsTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_sms_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_sms_template.delete_sms_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_sms_template_request.DeleteSmsTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_user_endpoints(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        user_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> (
        "capo_pinpoint.types.delete_user_endpoints_response.DeleteUserEndpointsResponse"
    ):
        """<p>Deletes all the endpoints that are associated with a specific user ID.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            user_id: <p>The unique identifier for the user.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_user_endpoints_request.DeleteUserEndpointsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_user_endpoints_response.DeleteUserEndpointsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_user_endpoints

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_user_endpoints.delete_user_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_user_endpoints_request.DeleteUserEndpointsRequest = {
            "application_id": application_id,
            "user_id": user_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.delete_voice_channel_response.DeleteVoiceChannelResponse":
        """<p>Disables the voice channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_voice_channel_request.DeleteVoiceChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_voice_channel_response.DeleteVoiceChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_voice_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_voice_channel.delete_voice_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_voice_channel_request.DeleteVoiceChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> (
        "capo_pinpoint.types.delete_voice_template_response.DeleteVoiceTemplateResponse"
    ):
        """<p>Deletes a message template for messages that were sent through the voice channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.delete_voice_template_request.DeleteVoiceTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.delete_voice_template_response.DeleteVoiceTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.delete_voice_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.delete_voice_template.delete_voice_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.delete_voice_template_request.DeleteVoiceTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_adm_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_adm_channel_response.GetAdmChannelResponse":
        """<p>Retrieves information about the status and settings of the ADM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_adm_channel_request.GetAdmChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_adm_channel_response.GetAdmChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_adm_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_adm_channel.get_adm_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_adm_channel_request.GetAdmChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_apns_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_apns_channel_response.GetApnsChannelResponse":
        """<p>Retrieves information about the status and settings of the APNs channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_apns_channel_request.GetApnsChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_apns_channel_response.GetApnsChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_apns_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_apns_channel.get_apns_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_apns_channel_request.GetApnsChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_apns_sandbox_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_apns_sandbox_channel_response.GetApnsSandboxChannelResponse":
        """<p>Retrieves information about the status and settings of the APNs sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_apns_sandbox_channel_request.GetApnsSandboxChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_apns_sandbox_channel_response.GetApnsSandboxChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_apns_sandbox_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_apns_sandbox_channel.get_apns_sandbox_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_apns_sandbox_channel_request.GetApnsSandboxChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_apns_voip_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> (
        "capo_pinpoint.types.get_apns_voip_channel_response.GetApnsVoipChannelResponse"
    ):
        """<p>Retrieves information about the status and settings of the APNs VoIP channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_apns_voip_channel_request.GetApnsVoipChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_apns_voip_channel_response.GetApnsVoipChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_apns_voip_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_apns_voip_channel.get_apns_voip_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_apns_voip_channel_request.GetApnsVoipChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_apns_voip_sandbox_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_apns_voip_sandbox_channel_response.GetApnsVoipSandboxChannelResponse":
        """<p>Retrieves information about the status and settings of the APNs VoIP sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_apns_voip_sandbox_channel_request.GetApnsVoipSandboxChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_apns_voip_sandbox_channel_response.GetApnsVoipSandboxChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_apns_voip_sandbox_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_apns_voip_sandbox_channel.get_apns_voip_sandbox_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_apns_voip_sandbox_channel_request.GetApnsVoipSandboxChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_app(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_app_response.GetAppResponse":
        """<p>Retrieves information about an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_app_request.GetAppRequest]",
        ) -> OperationResponse["capo_pinpoint.types.get_app_response.GetAppResponse"]:
            import capo_pinpoint._operations.pinpoint.get_app

            output, http_response = capo_pinpoint._operations.pinpoint.get_app.get_app(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_app_request.GetAppRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application_date_range_kpi(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        kpi_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        end_time: Optional[
            "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        start_time: Optional[
            "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
    ) -> "capo_pinpoint.types.get_application_date_range_kpi_response.GetApplicationDateRangeKpiResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard metric that applies to an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            end_time: <p>The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.</p>
            kpi_name: <p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html">Amazon Pinpoint Developer Guide</a>.</p>
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            start_time: <p>The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_application_date_range_kpi_request.GetApplicationDateRangeKpiRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_application_date_range_kpi_response.GetApplicationDateRangeKpiResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_application_date_range_kpi

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_application_date_range_kpi.get_application_date_range_kpi(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_application_date_range_kpi_request.GetApplicationDateRangeKpiRequest = {
            "application_id": application_id,
            "kpi_name": kpi_name,
        }
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if start_time is not None:
            input_["start_time"] = start_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application_settings(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_application_settings_response.GetApplicationSettingsResponse":
        """<p>Retrieves information about the settings for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_application_settings_request.GetApplicationSettingsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_application_settings_response.GetApplicationSettingsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_application_settings

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_application_settings.get_application_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_application_settings_request.GetApplicationSettingsRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_apps(
        self,
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_apps_response.GetAppsResponse":
        """<p>Retrieves information about all the applications that are associated with your Amazon Pinpoint account.</p>

        Args:
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_apps_request.GetAppsRequest]",
        ) -> OperationResponse["capo_pinpoint.types.get_apps_response.GetAppsResponse"]:
            import capo_pinpoint._operations.pinpoint.get_apps

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_apps.get_apps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_apps_request.GetAppsRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_baidu_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_baidu_channel_response.GetBaiduChannelResponse":
        """<p>Retrieves information about the status and settings of the Baidu channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_baidu_channel_request.GetBaiduChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_baidu_channel_response.GetBaiduChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_baidu_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_baidu_channel.get_baidu_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_baidu_channel_request.GetBaiduChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        campaign_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_campaign_response.GetCampaignResponse":
        """<p>Retrieves information about the status, configuration, and other settings for a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_campaign_request.GetCampaignRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_campaign_response.GetCampaignResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_campaign

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_campaign.get_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_campaign_request.GetCampaignRequest = {
            "application_id": application_id,
            "campaign_id": campaign_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign_activities(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        campaign_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_campaign_activities_response.GetCampaignActivitiesResponse":
        """<p>Retrieves information about all the activities for a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_campaign_activities_request.GetCampaignActivitiesRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_campaign_activities_response.GetCampaignActivitiesResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_campaign_activities

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_campaign_activities.get_campaign_activities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_campaign_activities_request.GetCampaignActivitiesRequest = {
            "application_id": application_id,
            "campaign_id": campaign_id,
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign_date_range_kpi(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        campaign_id: "capo_pinpoint.types.__string.__string",
        kpi_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        end_time: Optional[
            "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        start_time: Optional[
            "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
    ) -> "capo_pinpoint.types.get_campaign_date_range_kpi_response.GetCampaignDateRangeKpiResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard metric that applies to a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            end_time: <p>The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.</p>
            kpi_name: <p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html">Amazon Pinpoint Developer Guide</a>.</p>
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            start_time: <p>The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_campaign_date_range_kpi_request.GetCampaignDateRangeKpiRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_campaign_date_range_kpi_response.GetCampaignDateRangeKpiResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_campaign_date_range_kpi

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_campaign_date_range_kpi.get_campaign_date_range_kpi(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_campaign_date_range_kpi_request.GetCampaignDateRangeKpiRequest = {
            "application_id": application_id,
            "campaign_id": campaign_id,
            "kpi_name": kpi_name,
        }
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if start_time is not None:
            input_["start_time"] = start_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaigns(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_campaigns_response.GetCampaignsResponse":
        """<p>Retrieves information about the status, configuration, and other settings for all the campaigns that are associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_campaigns_request.GetCampaignsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_campaigns_response.GetCampaignsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_campaigns

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_campaigns.get_campaigns(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_campaigns_request.GetCampaignsRequest = {
            "application_id": application_id
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign_version(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        campaign_id: "capo_pinpoint.types.__string.__string",
        version: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_campaign_version_response.GetCampaignVersionResponse":
        """<p>Retrieves information about the status, configuration, and other settings for a specific version of a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            version: <p>The unique version number (Version property) for the campaign version.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_campaign_version_request.GetCampaignVersionRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_campaign_version_response.GetCampaignVersionResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_campaign_version

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_campaign_version.get_campaign_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_campaign_version_request.GetCampaignVersionRequest = {
            "application_id": application_id,
            "campaign_id": campaign_id,
            "version": version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign_versions(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        campaign_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> (
        "capo_pinpoint.types.get_campaign_versions_response.GetCampaignVersionsResponse"
    ):
        """<p>Retrieves information about the status, configuration, and other settings for all versions of a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_campaign_versions_request.GetCampaignVersionsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_campaign_versions_response.GetCampaignVersionsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_campaign_versions

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_campaign_versions.get_campaign_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_campaign_versions_request.GetCampaignVersionsRequest = {
            "application_id": application_id,
            "campaign_id": campaign_id,
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channels(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_channels_response.GetChannelsResponse":
        """<p>Retrieves information about the history and status of each channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_channels_request.GetChannelsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_channels_response.GetChannelsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_channels

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_channels.get_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_channels_request.GetChannelsRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_email_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_email_channel_response.GetEmailChannelResponse":
        """<p>Retrieves information about the status and settings of the email channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_email_channel_request.GetEmailChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_email_channel_response.GetEmailChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_email_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_email_channel.get_email_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_email_channel_request.GetEmailChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_email_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_email_template_response.GetEmailTemplateResponse":
        """<p>Retrieves the content and settings of a message template for messages that are sent through the email channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_email_template_request.GetEmailTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_email_template_response.GetEmailTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_email_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_email_template.get_email_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_email_template_request.GetEmailTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_endpoint(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        endpoint_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_endpoint_response.GetEndpointResponse":
        """<p>Retrieves information about the settings and attributes of a specific endpoint for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_endpoint_request.GetEndpointRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_endpoint_response.GetEndpointResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_endpoint

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_endpoint.get_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_endpoint_request.GetEndpointRequest = {
            "application_id": application_id,
            "endpoint_id": endpoint_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_stream(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_event_stream_response.GetEventStreamResponse":
        """<p>Retrieves information about the event stream settings for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_event_stream_request.GetEventStreamRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_event_stream_response.GetEventStreamResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_event_stream

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_event_stream.get_event_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_event_stream_request.GetEventStreamRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_export_job(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        job_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_export_job_response.GetExportJobResponse":
        """<p>Retrieves information about the status and settings of a specific export job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            job_id: <p>The unique identifier for the job.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_export_job_request.GetExportJobRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_export_job_response.GetExportJobResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_export_job

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_export_job.get_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_export_job_request.GetExportJobRequest = {
            "application_id": application_id,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_export_jobs(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_export_jobs_response.GetExportJobsResponse":
        """<p>Retrieves information about the status and settings of all the export jobs for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_export_jobs_request.GetExportJobsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_export_jobs_response.GetExportJobsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_export_jobs

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_export_jobs.get_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_export_jobs_request.GetExportJobsRequest = {
            "application_id": application_id
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gcm_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_gcm_channel_response.GetGcmChannelResponse":
        """<p>Retrieves information about the status and settings of the GCM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_gcm_channel_request.GetGcmChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_gcm_channel_response.GetGcmChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_gcm_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_gcm_channel.get_gcm_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_gcm_channel_request.GetGcmChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_import_job(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        job_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_import_job_response.GetImportJobResponse":
        """<p>Retrieves information about the status and settings of a specific import job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            job_id: <p>The unique identifier for the job.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_import_job_request.GetImportJobRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_import_job_response.GetImportJobResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_import_job

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_import_job.get_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_import_job_request.GetImportJobRequest = {
            "application_id": application_id,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_import_jobs(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_import_jobs_response.GetImportJobsResponse":
        """<p>Retrieves information about the status and settings of all the import jobs for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_import_jobs_request.GetImportJobsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_import_jobs_response.GetImportJobsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_import_jobs

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_import_jobs.get_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_import_jobs_request.GetImportJobsRequest = {
            "application_id": application_id
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_in_app_messages(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        endpoint_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_in_app_messages_response.GetInAppMessagesResponse":
        """<p>Retrieves the in-app messages targeted for the provided endpoint ID.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The unique identifier for the endpoint.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_in_app_messages_request.GetInAppMessagesRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_in_app_messages_response.GetInAppMessagesResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_in_app_messages

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_in_app_messages.get_in_app_messages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_in_app_messages_request.GetInAppMessagesRequest = {
            "application_id": application_id,
            "endpoint_id": endpoint_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_in_app_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_in_app_template_response.GetInAppTemplateResponse":
        """<p>Retrieves the content and settings of a message template for messages sent through the in-app channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_in_app_template_request.GetInAppTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_in_app_template_response.GetInAppTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_in_app_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_in_app_template.get_in_app_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_in_app_template_request.GetInAppTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_journey(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_journey_response.GetJourneyResponse":
        """<p>Retrieves information about the status, configuration, and other settings for a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_journey_request.GetJourneyRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_journey_response.GetJourneyResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_journey

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_journey.get_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_journey_request.GetJourneyRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_journey_date_range_kpi(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        kpi_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        end_time: Optional[
            "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        start_time: Optional[
            "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
    ) -> "capo_pinpoint.types.get_journey_date_range_kpi_response.GetJourneyDateRangeKpiResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard engagement metric that applies to a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            end_time: <p>The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            kpi_name: <p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html">Amazon Pinpoint Developer Guide</a>.</p>
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            start_time: <p>The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_journey_date_range_kpi_request.GetJourneyDateRangeKpiRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_journey_date_range_kpi_response.GetJourneyDateRangeKpiResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_journey_date_range_kpi

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_journey_date_range_kpi.get_journey_date_range_kpi(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_journey_date_range_kpi_request.GetJourneyDateRangeKpiRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
            "kpi_name": kpi_name,
        }
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if start_time is not None:
            input_["start_time"] = start_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_journey_execution_activity_metrics(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_activity_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_journey_execution_activity_metrics_response.GetJourneyExecutionActivityMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey activity.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_activity_id: <p>The unique identifier for the journey activity.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_journey_execution_activity_metrics_request.GetJourneyExecutionActivityMetricsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_journey_execution_activity_metrics_response.GetJourneyExecutionActivityMetricsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_journey_execution_activity_metrics

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_journey_execution_activity_metrics.get_journey_execution_activity_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_journey_execution_activity_metrics_request.GetJourneyExecutionActivityMetricsRequest = {
            "application_id": application_id,
            "journey_activity_id": journey_activity_id,
            "journey_id": journey_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_journey_execution_metrics(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_journey_execution_metrics_response.GetJourneyExecutionMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_journey_execution_metrics_request.GetJourneyExecutionMetricsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_journey_execution_metrics_response.GetJourneyExecutionMetricsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_journey_execution_metrics

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_journey_execution_metrics.get_journey_execution_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_journey_execution_metrics_request.GetJourneyExecutionMetricsRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_journey_run_execution_activity_metrics(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_activity_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        run_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_journey_run_execution_activity_metrics_response.GetJourneyRunExecutionActivityMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey activity.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_activity_id: <p>The unique identifier for the journey activity.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            run_id: <p>The unique identifier for the journey run.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the activity execution metrics for a journey run
            The following example gets activity execution metrics for a single run of a journey.

            >>> client.get_journey_run_execution_activity_metrics(application_id='11111111112222222222333333333344', journey_id='aaaaaaaaaabbbbbbbbbbccccccccccdd', run_id='99999999998888888888777777777766', journey_activity_id='AAAAAAAAAA')
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_journey_run_execution_activity_metrics_request.GetJourneyRunExecutionActivityMetricsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_journey_run_execution_activity_metrics_response.GetJourneyRunExecutionActivityMetricsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_journey_run_execution_activity_metrics

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_journey_run_execution_activity_metrics.get_journey_run_execution_activity_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_journey_run_execution_activity_metrics_request.GetJourneyRunExecutionActivityMetricsRequest = {
            "application_id": application_id,
            "journey_activity_id": journey_activity_id,
            "journey_id": journey_id,
            "run_id": run_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_journey_run_execution_metrics(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        run_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_journey_run_execution_metrics_response.GetJourneyRunExecutionMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            run_id: <p>The unique identifier for the journey run.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the execution metrics for a journey run
            The following example gets execution metrics for a single run of a journey.

            >>> client.get_journey_run_execution_metrics(application_id='11111111112222222222333333333344', journey_id='aaaaaaaaaabbbbbbbbbbccccccccccdd', run_id='99999999998888888888777777777766')
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_journey_run_execution_metrics_request.GetJourneyRunExecutionMetricsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_journey_run_execution_metrics_response.GetJourneyRunExecutionMetricsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_journey_run_execution_metrics

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_journey_run_execution_metrics.get_journey_run_execution_metrics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_journey_run_execution_metrics_request.GetJourneyRunExecutionMetricsRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
            "run_id": run_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_journey_runs(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_journey_runs_response.GetJourneyRunsResponse":
        """<p>Provides information about the runs of a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the runs of a journey
            The following example gets the runs of a journey.

            >>> client.get_journey_runs(application_id='11111111112222222222333333333344', journey_id='aaaaaaaaaabbbbbbbbbbccccccccccdd')
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_journey_runs_request.GetJourneyRunsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_journey_runs_response.GetJourneyRunsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_journey_runs

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_journey_runs.get_journey_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_journey_runs_request.GetJourneyRunsRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_push_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_push_template_response.GetPushTemplateResponse":
        """<p>Retrieves the content and settings of a message template for messages that are sent through a push notification channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_push_template_request.GetPushTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_push_template_response.GetPushTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_push_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_push_template.get_push_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_push_template_request.GetPushTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommender_configuration(
        self,
        recommender_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_recommender_configuration_response.GetRecommenderConfigurationResponse":
        """<p>Retrieves information about an Amazon Pinpoint configuration for a recommender model.</p>

        Args:
            recommender_id: <p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_recommender_configuration_request.GetRecommenderConfigurationRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_recommender_configuration_response.GetRecommenderConfigurationResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_recommender_configuration

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_recommender_configuration.get_recommender_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_recommender_configuration_request.GetRecommenderConfigurationRequest = {
            "recommender_id": recommender_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommender_configurations(
        self,
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_recommender_configurations_response.GetRecommenderConfigurationsResponse":
        """<p>Retrieves information about all the recommender model configurations that are associated with your Amazon Pinpoint account.</p>

        Args:
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_recommender_configurations_request.GetRecommenderConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_recommender_configurations_response.GetRecommenderConfigurationsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_recommender_configurations

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_recommender_configurations.get_recommender_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_recommender_configurations_request.GetRecommenderConfigurationsRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        segment_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_segment_response.GetSegmentResponse":
        """<p>Retrieves information about the configuration, dimension, and other settings for a specific segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_segment_request.GetSegmentRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_segment_response.GetSegmentResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_segment

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_segment.get_segment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_segment_request.GetSegmentRequest = {
            "application_id": application_id,
            "segment_id": segment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_export_jobs(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        segment_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_segment_export_jobs_response.GetSegmentExportJobsResponse":
        """<p>Retrieves information about the status and settings of the export jobs for a segment.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_segment_export_jobs_request.GetSegmentExportJobsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_segment_export_jobs_response.GetSegmentExportJobsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_segment_export_jobs

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_segment_export_jobs.get_segment_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_segment_export_jobs_request.GetSegmentExportJobsRequest = {
            "application_id": application_id,
            "segment_id": segment_id,
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_import_jobs(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        segment_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_segment_import_jobs_response.GetSegmentImportJobsResponse":
        """<p>Retrieves information about the status and settings of the import jobs for a segment.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_segment_import_jobs_request.GetSegmentImportJobsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_segment_import_jobs_response.GetSegmentImportJobsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_segment_import_jobs

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_segment_import_jobs.get_segment_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_segment_import_jobs_request.GetSegmentImportJobsRequest = {
            "application_id": application_id,
            "segment_id": segment_id,
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segments(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_segments_response.GetSegmentsResponse":
        """<p>Retrieves information about the configuration, dimension, and other settings for all the segments that are associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_segments_request.GetSegmentsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_segments_response.GetSegmentsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_segments

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_segments.get_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_segments_request.GetSegmentsRequest = {
            "application_id": application_id
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_version(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        segment_id: "capo_pinpoint.types.__string.__string",
        version: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_segment_version_response.GetSegmentVersionResponse":
        """<p>Retrieves information about the configuration, dimension, and other settings for a specific version of a segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            version: <p>The unique version number (Version property) for the campaign version.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_segment_version_request.GetSegmentVersionRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_segment_version_response.GetSegmentVersionResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_segment_version

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_segment_version.get_segment_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_segment_version_request.GetSegmentVersionRequest = {
            "application_id": application_id,
            "segment_id": segment_id,
            "version": version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_segment_versions(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        segment_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_segment_versions_response.GetSegmentVersionsResponse":
        """<p>Retrieves information about the configuration, dimension, and other settings for all the versions of a specific segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_segment_versions_request.GetSegmentVersionsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_segment_versions_response.GetSegmentVersionsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_segment_versions

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_segment_versions.get_segment_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_segment_versions_request.GetSegmentVersionsRequest = {
            "application_id": application_id,
            "segment_id": segment_id,
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sms_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse":
        """<p>Retrieves information about the status and settings of the SMS channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_sms_channel_request.GetSmsChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_sms_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_sms_channel.get_sms_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_sms_channel_request.GetSmsChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sms_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_sms_template_response.GetSmsTemplateResponse":
        """<p>Retrieves the content and settings of a message template for messages that are sent through the SMS channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_sms_template_request.GetSmsTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_sms_template_response.GetSmsTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_sms_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_sms_template.get_sms_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_sms_template_request.GetSmsTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_user_endpoints(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        user_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_user_endpoints_response.GetUserEndpointsResponse":
        """<p>Retrieves information about all the endpoints that are associated with a specific user ID.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            user_id: <p>The unique identifier for the user.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_user_endpoints_request.GetUserEndpointsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_user_endpoints_response.GetUserEndpointsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_user_endpoints

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_user_endpoints.get_user_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_user_endpoints_request.GetUserEndpointsRequest = {
            "application_id": application_id,
            "user_id": user_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.get_voice_channel_response.GetVoiceChannelResponse":
        """<p>Retrieves information about the status and settings of the voice channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_voice_channel_request.GetVoiceChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_voice_channel_response.GetVoiceChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_voice_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_voice_channel.get_voice_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_voice_channel_request.GetVoiceChannelRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.get_voice_template_response.GetVoiceTemplateResponse":
        """<p>Retrieves the content and settings of a message template for messages that are sent through the voice channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.get_voice_template_request.GetVoiceTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.get_voice_template_response.GetVoiceTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.get_voice_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.get_voice_template.get_voice_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.get_voice_template_request.GetVoiceTemplateRequest = {
            "template_name": template_name
        }
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_journeys(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        token: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.list_journeys_response.ListJourneysResponse":
        """<p>Retrieves information about the status, configuration, and other settings for all the journeys that are associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.list_journeys_request.ListJourneysRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.list_journeys_response.ListJourneysResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.list_journeys

            output, http_response = (
                capo_pinpoint._operations.pinpoint.list_journeys.list_journeys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.list_journeys_request.ListJourneysRequest = {
            "application_id": application_id
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
    ) -> "capo_pinpoint.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves all the tags (keys and values) that are associated with an application, campaign, message template, or segment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.list_tags_for_resource

            output, http_response = (
                capo_pinpoint._operations.pinpoint.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_templates(
        self,
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
        prefix: Optional["capo_pinpoint.types.__string.__string"] = None,
        template_type: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.list_templates_response.ListTemplatesResponse":
        """<p>Retrieves information about all the message templates that are associated with your Amazon Pinpoint account.</p>

        Args:
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            prefix: <p>The substring to match in the names of the message templates to include in the results. If you specify this value, Amazon Pinpoint returns only those templates whose names begin with the value that you specify.</p>
            template_type: <p>The type of message template to include in the results. Valid values are: EMAIL, PUSH, SMS, and VOICE. To include all types of templates in the results, don't include this parameter in your request.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.list_templates_request.ListTemplatesRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.list_templates

            output, http_response = (
                capo_pinpoint._operations.pinpoint.list_templates.list_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.list_templates_request.ListTemplatesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if prefix is not None:
            input_["prefix"] = prefix
        if template_type is not None:
            input_["template_type"] = template_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_template_versions(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        template_type: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        next_token: Optional["capo_pinpoint.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.list_template_versions_response.ListTemplateVersionsResponse":
        """<p>Retrieves information about all the versions of a specific message template.</p>

        Args:
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            template_type: <p>The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.list_template_versions_request.ListTemplateVersionsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.list_template_versions_response.ListTemplateVersionsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.list_template_versions

            output, http_response = (
                capo_pinpoint._operations.pinpoint.list_template_versions.list_template_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.list_template_versions_request.ListTemplateVersionsRequest = {
            "template_name": template_name,
            "template_type": template_type,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def phone_number_validate(
        self,
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        number_validate_request: Optional[
            "capo_pinpoint.types.number_validate_request.NumberValidateRequest"
        ] = None,
    ) -> (
        "capo_pinpoint.types.phone_number_validate_response.PhoneNumberValidateResponse"
    ):
        """<p>Retrieves information about a phone number.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.phone_number_validate_request.PhoneNumberValidateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.phone_number_validate_response.PhoneNumberValidateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.phone_number_validate

            output, http_response = (
                capo_pinpoint._operations.pinpoint.phone_number_validate.phone_number_validate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.phone_number_validate_request.PhoneNumberValidateRequest = {}
        if number_validate_request is not None:
            input_["number_validate_request"] = number_validate_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_events(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        events_request: Optional[
            "capo_pinpoint.types.events_request.EventsRequest"
        ] = None,
    ) -> "capo_pinpoint.types.put_events_response.PutEventsResponse":
        """<p>Creates a new event to record for endpoints, or creates or updates endpoint data that existing events are associated with.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.put_events_request.PutEventsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.put_events_response.PutEventsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.put_events

            output, http_response = (
                capo_pinpoint._operations.pinpoint.put_events.put_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.put_events_request.PutEventsRequest = {
            "application_id": application_id
        }
        if events_request is not None:
            input_["events_request"] = events_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_event_stream(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_event_stream: Optional[
            "capo_pinpoint.types.write_event_stream.WriteEventStream"
        ] = None,
    ) -> "capo_pinpoint.types.put_event_stream_response.PutEventStreamResponse":
        """<p>Creates a new event stream for an application or updates the settings of an existing event stream for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.put_event_stream_request.PutEventStreamRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.put_event_stream_response.PutEventStreamResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.put_event_stream

            output, http_response = (
                capo_pinpoint._operations.pinpoint.put_event_stream.put_event_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.put_event_stream_request.PutEventStreamRequest = {
            "application_id": application_id
        }
        if write_event_stream is not None:
            input_["write_event_stream"] = write_event_stream

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_attributes(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        attribute_type: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        update_attributes_request: Optional[
            "capo_pinpoint.types.update_attributes_request.UpdateAttributesRequest"
        ] = None,
    ) -> "capo_pinpoint.types.remove_attributes_response.RemoveAttributesResponse":
        """<p>Removes one or more custom attributes, of the same attribute type, from the application. Existing endpoints still have the attributes but Amazon Pinpoint will stop capturing new or changed values for these attributes.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            attribute_type: <p>The type of attribute or attributes to remove. Valid values are:</p> <ul><li><p>endpoint-custom-attributes - Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel.</p></li> <li><p>endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart.</p></li> <li><p>endpoint-user-attributes - Custom attributes that describe users, such as first name, last name, and age.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.remove_attributes_request.RemoveAttributesRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.remove_attributes_response.RemoveAttributesResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.remove_attributes

            output, http_response = (
                capo_pinpoint._operations.pinpoint.remove_attributes.remove_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.remove_attributes_request.RemoveAttributesRequest = {
            "application_id": application_id,
            "attribute_type": attribute_type,
        }
        if update_attributes_request is not None:
            input_["update_attributes_request"] = update_attributes_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_messages(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        message_request: Optional[
            "capo_pinpoint.types.message_request.MessageRequest"
        ] = None,
    ) -> "capo_pinpoint.types.send_messages_response.SendMessagesResponse":
        """<p>Creates and sends a direct message.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.send_messages_request.SendMessagesRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.send_messages_response.SendMessagesResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.send_messages

            output, http_response = (
                capo_pinpoint._operations.pinpoint.send_messages.send_messages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.send_messages_request.SendMessagesRequest = {
            "application_id": application_id
        }
        if message_request is not None:
            input_["message_request"] = message_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_otp_message(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        send_otp_message_request_parameters: Optional[
            "capo_pinpoint.types.send_otp_message_request_parameters.SendOTPMessageRequestParameters"
        ] = None,
    ) -> "capo_pinpoint.types.send_otp_message_response.SendOTPMessageResponse":
        """<p>Send an OTP message</p>

        Args:
            application_id: <p>The unique ID of your Amazon Pinpoint application.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.send_otp_message_request.SendOTPMessageRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.send_otp_message_response.SendOTPMessageResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.send_otp_message

            output, http_response = (
                capo_pinpoint._operations.pinpoint.send_otp_message.send_otp_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.send_otp_message_request.SendOTPMessageRequest = {
            "application_id": application_id
        }
        if send_otp_message_request_parameters is not None:
            input_["send_otp_message_request_parameters"] = (
                send_otp_message_request_parameters
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_users_messages(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        send_users_message_request: Optional[
            "capo_pinpoint.types.send_users_message_request.SendUsersMessageRequest"
        ] = None,
    ) -> "capo_pinpoint.types.send_users_messages_response.SendUsersMessagesResponse":
        """<p>Creates and sends a message to a list of users.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.send_users_messages_request.SendUsersMessagesRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.send_users_messages_response.SendUsersMessagesResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.send_users_messages

            output, http_response = (
                capo_pinpoint._operations.pinpoint.send_users_messages.send_users_messages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.send_users_messages_request.SendUsersMessagesRequest = {
            "application_id": application_id
        }
        if send_users_message_request is not None:
            input_["send_users_message_request"] = send_users_message_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        tags_model: Optional["capo_pinpoint.types.tags_model.TagsModel"] = None,
    ) -> None:
        """<p>Adds one or more tags (keys and values) to an application, campaign, message template, or segment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_pinpoint._operations.pinpoint.tag_resource

            output, http_response = (
                capo_pinpoint._operations.pinpoint.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags_model is not None:
            input_["tags_model"] = tags_model

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        tag_keys: Optional["capo_pinpoint.types.list_of__string.ListOf__string"] = None,
    ) -> None:
        """<p>Removes one or more tags (keys and values) from an application, campaign, message template, or segment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The key of the tag to remove from the resource. To remove multiple tags, append the tagKeys parameter and argument for each additional tag to remove, separated by an ampersand (&amp;).</p>

        Raises:
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_pinpoint._operations.pinpoint.untag_resource

            output, http_response = (
                capo_pinpoint._operations.pinpoint.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_adm_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        adm_channel_request: Optional[
            "capo_pinpoint.types.adm_channel_request.ADMChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_adm_channel_response.UpdateAdmChannelResponse":
        """<p>Enables the ADM channel for an application or updates the status and settings of the ADM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_adm_channel_request.UpdateAdmChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_adm_channel_response.UpdateAdmChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_adm_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_adm_channel.update_adm_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_adm_channel_request.UpdateAdmChannelRequest = {
            "application_id": application_id
        }
        if adm_channel_request is not None:
            input_["adm_channel_request"] = adm_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_apns_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        apns_channel_request: Optional[
            "capo_pinpoint.types.apns_channel_request.APNSChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_apns_channel_response.UpdateApnsChannelResponse":
        """<p>Enables the APNs channel for an application or updates the status and settings of the APNs channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_apns_channel_request.UpdateApnsChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_apns_channel_response.UpdateApnsChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_apns_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_apns_channel.update_apns_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_apns_channel_request.UpdateApnsChannelRequest = {
            "application_id": application_id
        }
        if apns_channel_request is not None:
            input_["apns_channel_request"] = apns_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_apns_sandbox_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        apns_sandbox_channel_request: Optional[
            "capo_pinpoint.types.apns_sandbox_channel_request.APNSSandboxChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_apns_sandbox_channel_response.UpdateApnsSandboxChannelResponse":
        """<p>Enables the APNs sandbox channel for an application or updates the status and settings of the APNs sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_apns_sandbox_channel_request.UpdateApnsSandboxChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_apns_sandbox_channel_response.UpdateApnsSandboxChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_apns_sandbox_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_apns_sandbox_channel.update_apns_sandbox_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_apns_sandbox_channel_request.UpdateApnsSandboxChannelRequest = {
            "application_id": application_id
        }
        if apns_sandbox_channel_request is not None:
            input_["apns_sandbox_channel_request"] = apns_sandbox_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_apns_voip_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        apns_voip_channel_request: Optional[
            "capo_pinpoint.types.apns_voip_channel_request.APNSVoipChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_apns_voip_channel_response.UpdateApnsVoipChannelResponse":
        """<p>Enables the APNs VoIP channel for an application or updates the status and settings of the APNs VoIP channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_apns_voip_channel_request.UpdateApnsVoipChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_apns_voip_channel_response.UpdateApnsVoipChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_apns_voip_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_apns_voip_channel.update_apns_voip_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_apns_voip_channel_request.UpdateApnsVoipChannelRequest = {
            "application_id": application_id
        }
        if apns_voip_channel_request is not None:
            input_["apns_voip_channel_request"] = apns_voip_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_apns_voip_sandbox_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        apns_voip_sandbox_channel_request: Optional[
            "capo_pinpoint.types.apns_voip_sandbox_channel_request.APNSVoipSandboxChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_apns_voip_sandbox_channel_response.UpdateApnsVoipSandboxChannelResponse":
        """<p>Enables the APNs VoIP sandbox channel for an application or updates the status and settings of the APNs VoIP sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_apns_voip_sandbox_channel_request.UpdateApnsVoipSandboxChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_apns_voip_sandbox_channel_response.UpdateApnsVoipSandboxChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_apns_voip_sandbox_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_apns_voip_sandbox_channel.update_apns_voip_sandbox_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_apns_voip_sandbox_channel_request.UpdateApnsVoipSandboxChannelRequest = {
            "application_id": application_id
        }
        if apns_voip_sandbox_channel_request is not None:
            input_["apns_voip_sandbox_channel_request"] = (
                apns_voip_sandbox_channel_request
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application_settings(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_application_settings_request: Optional[
            "capo_pinpoint.types.write_application_settings_request.WriteApplicationSettingsRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_application_settings_response.UpdateApplicationSettingsResponse":
        """<p>Updates the settings for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_application_settings_request.UpdateApplicationSettingsRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_application_settings_response.UpdateApplicationSettingsResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_application_settings

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_application_settings.update_application_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_application_settings_request.UpdateApplicationSettingsRequest = {
            "application_id": application_id
        }
        if write_application_settings_request is not None:
            input_["write_application_settings_request"] = (
                write_application_settings_request
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_baidu_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        baidu_channel_request: Optional[
            "capo_pinpoint.types.baidu_channel_request.BaiduChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_baidu_channel_response.UpdateBaiduChannelResponse":
        """<p>Enables the Baidu channel for an application or updates the status and settings of the Baidu channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_baidu_channel_request.UpdateBaiduChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_baidu_channel_response.UpdateBaiduChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_baidu_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_baidu_channel.update_baidu_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_baidu_channel_request.UpdateBaiduChannelRequest = {
            "application_id": application_id
        }
        if baidu_channel_request is not None:
            input_["baidu_channel_request"] = baidu_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_campaign(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        campaign_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_campaign_request: Optional[
            "capo_pinpoint.types.write_campaign_request.WriteCampaignRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_campaign_response.UpdateCampaignResponse":
        """<p>Updates the configuration and other settings for a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_campaign

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_campaign.update_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_campaign_request.UpdateCampaignRequest = {
            "application_id": application_id,
            "campaign_id": campaign_id,
        }
        if write_campaign_request is not None:
            input_["write_campaign_request"] = write_campaign_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_email_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        email_channel_request: Optional[
            "capo_pinpoint.types.email_channel_request.EmailChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_email_channel_response.UpdateEmailChannelResponse":
        """<p>Enables the email channel for an application or updates the status and settings of the email channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_email_channel_request.UpdateEmailChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_email_channel_response.UpdateEmailChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_email_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_email_channel.update_email_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_email_channel_request.UpdateEmailChannelRequest = {
            "application_id": application_id
        }
        if email_channel_request is not None:
            input_["email_channel_request"] = email_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_email_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        create_new_version: Optional["capo_pinpoint.types.__boolean.__boolean"] = None,
        email_template_request: Optional[
            "capo_pinpoint.types.email_template_request.EmailTemplateRequest"
        ] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> (
        "capo_pinpoint.types.update_email_template_response.UpdateEmailTemplateResponse"
    ):
        """<p>Updates an existing message template for messages that are sent through the email channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_email_template_request.UpdateEmailTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_email_template_response.UpdateEmailTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_email_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_email_template.update_email_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_email_template_request.UpdateEmailTemplateRequest = {
            "template_name": template_name
        }
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        if email_template_request is not None:
            input_["email_template_request"] = email_template_request
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_endpoint(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        endpoint_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        endpoint_request: Optional[
            "capo_pinpoint.types.endpoint_request.EndpointRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_endpoint_response.UpdateEndpointResponse":
        """<p>Creates a new endpoint for an application or updates the settings and attributes of an existing endpoint for an application. You can also use this operation to define custom attributes for an endpoint. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_endpoint_request.UpdateEndpointRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_endpoint_response.UpdateEndpointResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_endpoint

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_endpoint.update_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_endpoint_request.UpdateEndpointRequest = {
            "application_id": application_id,
            "endpoint_id": endpoint_id,
        }
        if endpoint_request is not None:
            input_["endpoint_request"] = endpoint_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_endpoints_batch(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        endpoint_batch_request: Optional[
            "capo_pinpoint.types.endpoint_batch_request.EndpointBatchRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_endpoints_batch_response.UpdateEndpointsBatchResponse":
        """<p>Creates a new batch of endpoints for an application or updates the settings and attributes of a batch of existing endpoints for an application. You can also use this operation to define custom attributes for a batch of endpoints. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_endpoints_batch_request.UpdateEndpointsBatchRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_endpoints_batch_response.UpdateEndpointsBatchResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_endpoints_batch

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_endpoints_batch.update_endpoints_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_endpoints_batch_request.UpdateEndpointsBatchRequest = {
            "application_id": application_id
        }
        if endpoint_batch_request is not None:
            input_["endpoint_batch_request"] = endpoint_batch_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gcm_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        gcm_channel_request: Optional[
            "capo_pinpoint.types.gcm_channel_request.GCMChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_gcm_channel_response.UpdateGcmChannelResponse":
        """<p>Enables the GCM channel for an application or updates the status and settings of the GCM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_gcm_channel_request.UpdateGcmChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_gcm_channel_response.UpdateGcmChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_gcm_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_gcm_channel.update_gcm_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_gcm_channel_request.UpdateGcmChannelRequest = {
            "application_id": application_id
        }
        if gcm_channel_request is not None:
            input_["gcm_channel_request"] = gcm_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_in_app_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        create_new_version: Optional["capo_pinpoint.types.__boolean.__boolean"] = None,
        in_app_template_request: Optional[
            "capo_pinpoint.types.in_app_template_request.InAppTemplateRequest"
        ] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.update_in_app_template_response.UpdateInAppTemplateResponse":
        """<p>Updates an existing message template for messages sent through the in-app message channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_in_app_template_request.UpdateInAppTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_in_app_template_response.UpdateInAppTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_in_app_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_in_app_template.update_in_app_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_in_app_template_request.UpdateInAppTemplateRequest = {
            "template_name": template_name
        }
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        if in_app_template_request is not None:
            input_["in_app_template_request"] = in_app_template_request
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_journey(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_journey_request: Optional[
            "capo_pinpoint.types.write_journey_request.WriteJourneyRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_journey_response.UpdateJourneyResponse":
        """<p>Updates the configuration and other settings for a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.conflict_exception.ConflictException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_journey_request.UpdateJourneyRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_journey_response.UpdateJourneyResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_journey

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_journey.update_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_journey_request.UpdateJourneyRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
        }
        if write_journey_request is not None:
            input_["write_journey_request"] = write_journey_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_journey_state(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        journey_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        journey_state_request: Optional[
            "capo_pinpoint.types.journey_state_request.JourneyStateRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_journey_state_response.UpdateJourneyStateResponse":
        """<p>Cancels (stops) an active journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_journey_state_request.UpdateJourneyStateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_journey_state_response.UpdateJourneyStateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_journey_state

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_journey_state.update_journey_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_journey_state_request.UpdateJourneyStateRequest = {
            "application_id": application_id,
            "journey_id": journey_id,
        }
        if journey_state_request is not None:
            input_["journey_state_request"] = journey_state_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_push_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        create_new_version: Optional["capo_pinpoint.types.__boolean.__boolean"] = None,
        push_notification_template_request: Optional[
            "capo_pinpoint.types.push_notification_template_request.PushNotificationTemplateRequest"
        ] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.update_push_template_response.UpdatePushTemplateResponse":
        """<p>Updates an existing message template for messages that are sent through a push notification channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_push_template_request.UpdatePushTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_push_template_response.UpdatePushTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_push_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_push_template.update_push_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_push_template_request.UpdatePushTemplateRequest = {
            "template_name": template_name
        }
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        if push_notification_template_request is not None:
            input_["push_notification_template_request"] = (
                push_notification_template_request
            )
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_recommender_configuration(
        self,
        recommender_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        update_recommender_configuration: Optional[
            "capo_pinpoint.types.update_recommender_configuration_shape.UpdateRecommenderConfigurationShape"
        ] = None,
    ) -> "capo_pinpoint.types.update_recommender_configuration_response.UpdateRecommenderConfigurationResponse":
        """<p>Updates an Amazon Pinpoint configuration for a recommender model.</p>

        Args:
            recommender_id: <p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_recommender_configuration_request.UpdateRecommenderConfigurationRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_recommender_configuration_response.UpdateRecommenderConfigurationResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_recommender_configuration

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_recommender_configuration.update_recommender_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_recommender_configuration_request.UpdateRecommenderConfigurationRequest = {
            "recommender_id": recommender_id
        }
        if update_recommender_configuration is not None:
            input_["update_recommender_configuration"] = (
                update_recommender_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_segment(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        segment_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        write_segment_request: Optional[
            "capo_pinpoint.types.write_segment_request.WriteSegmentRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_segment_response.UpdateSegmentResponse":
        """<p>Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_segment_request.UpdateSegmentRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_segment_response.UpdateSegmentResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_segment

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_segment.update_segment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_segment_request.UpdateSegmentRequest = {
            "application_id": application_id,
            "segment_id": segment_id,
        }
        if write_segment_request is not None:
            input_["write_segment_request"] = write_segment_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sms_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        sms_channel_request: Optional[
            "capo_pinpoint.types.sms_channel_request.SMSChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_sms_channel_response.UpdateSmsChannelResponse":
        """<p>Enables the SMS channel for an application or updates the status and settings of the SMS channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_sms_channel_request.UpdateSmsChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_sms_channel_response.UpdateSmsChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_sms_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_sms_channel.update_sms_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_sms_channel_request.UpdateSmsChannelRequest = {
            "application_id": application_id
        }
        if sms_channel_request is not None:
            input_["sms_channel_request"] = sms_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sms_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        create_new_version: Optional["capo_pinpoint.types.__boolean.__boolean"] = None,
        sms_template_request: Optional[
            "capo_pinpoint.types.sms_template_request.SMSTemplateRequest"
        ] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
    ) -> "capo_pinpoint.types.update_sms_template_response.UpdateSmsTemplateResponse":
        """<p>Updates an existing message template for messages that are sent through the SMS channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_sms_template_request.UpdateSmsTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_sms_template_response.UpdateSmsTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_sms_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_sms_template.update_sms_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_sms_template_request.UpdateSmsTemplateRequest = {
            "template_name": template_name
        }
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        if sms_template_request is not None:
            input_["sms_template_request"] = sms_template_request
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_template_active_version(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        template_type: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        template_active_version_request: Optional[
            "capo_pinpoint.types.template_active_version_request.TemplateActiveVersionRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_template_active_version_response.UpdateTemplateActiveVersionResponse":
        """<p>Changes the status of a specific version of a message template to <i>active</i>.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            template_type: <p>The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_template_active_version_request.UpdateTemplateActiveVersionRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_template_active_version_response.UpdateTemplateActiveVersionResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_template_active_version

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_template_active_version.update_template_active_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_template_active_version_request.UpdateTemplateActiveVersionRequest = {
            "template_name": template_name,
            "template_type": template_type,
        }
        if template_active_version_request is not None:
            input_["template_active_version_request"] = template_active_version_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_voice_channel(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        voice_channel_request: Optional[
            "capo_pinpoint.types.voice_channel_request.VoiceChannelRequest"
        ] = None,
    ) -> "capo_pinpoint.types.update_voice_channel_response.UpdateVoiceChannelResponse":
        """<p>Enables the voice channel for an application or updates the status and settings of the voice channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_voice_channel_request.UpdateVoiceChannelRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_voice_channel_response.UpdateVoiceChannelResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_voice_channel

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_voice_channel.update_voice_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_voice_channel_request.UpdateVoiceChannelRequest = {
            "application_id": application_id
        }
        if voice_channel_request is not None:
            input_["voice_channel_request"] = voice_channel_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_voice_template(
        self,
        template_name: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        create_new_version: Optional["capo_pinpoint.types.__boolean.__boolean"] = None,
        version: Optional["capo_pinpoint.types.__string.__string"] = None,
        voice_template_request: Optional[
            "capo_pinpoint.types.voice_template_request.VoiceTemplateRequest"
        ] = None,
    ) -> (
        "capo_pinpoint.types.update_voice_template_response.UpdateVoiceTemplateResponse"
    ):
        """<p>Updates an existing message template for messages that are sent through the voice channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.update_voice_template_request.UpdateVoiceTemplateRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.update_voice_template_response.UpdateVoiceTemplateResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.update_voice_template

            output, http_response = (
                capo_pinpoint._operations.pinpoint.update_voice_template.update_voice_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.update_voice_template_request.UpdateVoiceTemplateRequest = {
            "template_name": template_name
        }
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        if version is not None:
            input_["version"] = version
        if voice_template_request is not None:
            input_["voice_template_request"] = voice_template_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def verify_otp_message(
        self,
        application_id: "capo_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[PinpointClientConfig] = None,
        verify_otp_message_request_parameters: Optional[
            "capo_pinpoint.types.verify_otp_message_request_parameters.VerifyOTPMessageRequestParameters"
        ] = None,
    ) -> "capo_pinpoint.types.verify_otp_message_response.VerifyOTPMessageResponse":
        """<p>Verify an OTP</p>

        Args:
            application_id: <p>The unique ID of your Amazon Pinpoint application.</p>

        Raises:
            capo_pinpoint.errors.bad_request_exception.BadRequestException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.forbidden_exception.ForbiddenException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.internal_server_error_exception.InternalServerErrorException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.method_not_allowed_exception.MethodNotAllowedException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.not_found_exception.NotFoundException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.payload_too_large_exception.PayloadTooLargeException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.too_many_requests_exception.TooManyRequestsException: <p>Provides information about an API request or response.</p>
            capo_pinpoint.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pinpoint.types.verify_otp_message_request.VerifyOTPMessageRequest]",
        ) -> OperationResponse[
            "capo_pinpoint.types.verify_otp_message_response.VerifyOTPMessageResponse"
        ]:
            import capo_pinpoint._operations.pinpoint.verify_otp_message

            output, http_response = (
                capo_pinpoint._operations.pinpoint.verify_otp_message.verify_otp_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint.types.verify_otp_message_request.VerifyOTPMessageRequest = {
            "application_id": application_id
        }
        if verify_otp_message_request_parameters is not None:
            input_["verify_otp_message_request_parameters"] = (
                verify_otp_message_request_parameters
            )

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
