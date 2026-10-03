"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ChimeSDKTelephonyService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_chime_sdk_voice._auth._signers
import capo_chime_sdk_voice._auth._sigv4
from capo_chime_sdk_voice._auth._identity import Credentials
from capo_chime_sdk_voice._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_chime_sdk_voice._auth._zapros_handler import AuthMiddleware
from capo_chime_sdk_voice._pagination import resolve_path as _resolve_path
from capo_chime_sdk_voice._services._aws_config import aws_config
from capo_chime_sdk_voice._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.alpha2_country_code
    import capo_chime_sdk_voice.types.arn
    import capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_group_request
    import capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_group_response
    import capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_request
    import capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_response
    import capo_chime_sdk_voice.types.batch_delete_phone_number_request
    import capo_chime_sdk_voice.types.batch_delete_phone_number_response
    import capo_chime_sdk_voice.types.batch_update_phone_number_request
    import capo_chime_sdk_voice.types.batch_update_phone_number_response
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.call_distribution_type
    import capo_chime_sdk_voice.types.call_leg_type
    import capo_chime_sdk_voice.types.calling_name
    import capo_chime_sdk_voice.types.capability_list
    import capo_chime_sdk_voice.types.client_request_id
    import capo_chime_sdk_voice.types.contact_center_system_type_list
    import capo_chime_sdk_voice.types.country_list
    import capo_chime_sdk_voice.types.create_phone_number_order_request
    import capo_chime_sdk_voice.types.create_phone_number_order_response
    import capo_chime_sdk_voice.types.create_proxy_session_request
    import capo_chime_sdk_voice.types.create_proxy_session_response
    import capo_chime_sdk_voice.types.create_sip_media_application_call_request
    import capo_chime_sdk_voice.types.create_sip_media_application_call_response
    import capo_chime_sdk_voice.types.create_sip_media_application_request
    import capo_chime_sdk_voice.types.create_sip_media_application_response
    import capo_chime_sdk_voice.types.create_sip_rule_request
    import capo_chime_sdk_voice.types.create_sip_rule_response
    import capo_chime_sdk_voice.types.create_voice_connector_group_request
    import capo_chime_sdk_voice.types.create_voice_connector_group_response
    import capo_chime_sdk_voice.types.create_voice_connector_request
    import capo_chime_sdk_voice.types.create_voice_connector_response
    import capo_chime_sdk_voice.types.create_voice_profile_domain_request
    import capo_chime_sdk_voice.types.create_voice_profile_domain_response
    import capo_chime_sdk_voice.types.create_voice_profile_request
    import capo_chime_sdk_voice.types.create_voice_profile_response
    import capo_chime_sdk_voice.types.credential_list
    import capo_chime_sdk_voice.types.delete_phone_number_request
    import capo_chime_sdk_voice.types.delete_proxy_session_request
    import capo_chime_sdk_voice.types.delete_sip_media_application_request
    import capo_chime_sdk_voice.types.delete_sip_rule_request
    import capo_chime_sdk_voice.types.delete_voice_connector_emergency_calling_configuration_request
    import capo_chime_sdk_voice.types.delete_voice_connector_external_systems_configuration_request
    import capo_chime_sdk_voice.types.delete_voice_connector_group_request
    import capo_chime_sdk_voice.types.delete_voice_connector_origination_request
    import capo_chime_sdk_voice.types.delete_voice_connector_proxy_request
    import capo_chime_sdk_voice.types.delete_voice_connector_request
    import capo_chime_sdk_voice.types.delete_voice_connector_streaming_configuration_request
    import capo_chime_sdk_voice.types.delete_voice_connector_termination_credentials_request
    import capo_chime_sdk_voice.types.delete_voice_connector_termination_request
    import capo_chime_sdk_voice.types.delete_voice_profile_domain_request
    import capo_chime_sdk_voice.types.delete_voice_profile_request
    import capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_group_request
    import capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_group_response
    import capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_request
    import capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_response
    import capo_chime_sdk_voice.types.e164_phone_number
    import capo_chime_sdk_voice.types.e164_phone_number_list
    import capo_chime_sdk_voice.types.emergency_calling_configuration
    import capo_chime_sdk_voice.types.geo_match_level
    import capo_chime_sdk_voice.types.geo_match_params
    import capo_chime_sdk_voice.types.get_global_settings_response
    import capo_chime_sdk_voice.types.get_phone_number_order_request
    import capo_chime_sdk_voice.types.get_phone_number_order_response
    import capo_chime_sdk_voice.types.get_phone_number_request
    import capo_chime_sdk_voice.types.get_phone_number_response
    import capo_chime_sdk_voice.types.get_phone_number_settings_response
    import capo_chime_sdk_voice.types.get_proxy_session_request
    import capo_chime_sdk_voice.types.get_proxy_session_response
    import capo_chime_sdk_voice.types.get_sip_media_application_alexa_skill_configuration_request
    import capo_chime_sdk_voice.types.get_sip_media_application_alexa_skill_configuration_response
    import capo_chime_sdk_voice.types.get_sip_media_application_logging_configuration_request
    import capo_chime_sdk_voice.types.get_sip_media_application_logging_configuration_response
    import capo_chime_sdk_voice.types.get_sip_media_application_request
    import capo_chime_sdk_voice.types.get_sip_media_application_response
    import capo_chime_sdk_voice.types.get_sip_rule_request
    import capo_chime_sdk_voice.types.get_sip_rule_response
    import capo_chime_sdk_voice.types.get_speaker_search_task_request
    import capo_chime_sdk_voice.types.get_speaker_search_task_response
    import capo_chime_sdk_voice.types.get_voice_connector_emergency_calling_configuration_request
    import capo_chime_sdk_voice.types.get_voice_connector_emergency_calling_configuration_response
    import capo_chime_sdk_voice.types.get_voice_connector_external_systems_configuration_request
    import capo_chime_sdk_voice.types.get_voice_connector_external_systems_configuration_response
    import capo_chime_sdk_voice.types.get_voice_connector_group_request
    import capo_chime_sdk_voice.types.get_voice_connector_group_response
    import capo_chime_sdk_voice.types.get_voice_connector_logging_configuration_request
    import capo_chime_sdk_voice.types.get_voice_connector_logging_configuration_response
    import capo_chime_sdk_voice.types.get_voice_connector_origination_request
    import capo_chime_sdk_voice.types.get_voice_connector_origination_response
    import capo_chime_sdk_voice.types.get_voice_connector_proxy_request
    import capo_chime_sdk_voice.types.get_voice_connector_proxy_response
    import capo_chime_sdk_voice.types.get_voice_connector_request
    import capo_chime_sdk_voice.types.get_voice_connector_response
    import capo_chime_sdk_voice.types.get_voice_connector_streaming_configuration_request
    import capo_chime_sdk_voice.types.get_voice_connector_streaming_configuration_response
    import capo_chime_sdk_voice.types.get_voice_connector_termination_health_request
    import capo_chime_sdk_voice.types.get_voice_connector_termination_health_response
    import capo_chime_sdk_voice.types.get_voice_connector_termination_request
    import capo_chime_sdk_voice.types.get_voice_connector_termination_response
    import capo_chime_sdk_voice.types.get_voice_profile_domain_request
    import capo_chime_sdk_voice.types.get_voice_profile_domain_response
    import capo_chime_sdk_voice.types.get_voice_profile_request
    import capo_chime_sdk_voice.types.get_voice_profile_response
    import capo_chime_sdk_voice.types.get_voice_tone_analysis_task_request
    import capo_chime_sdk_voice.types.get_voice_tone_analysis_task_response
    import capo_chime_sdk_voice.types.guid_string
    import capo_chime_sdk_voice.types.integer
    import capo_chime_sdk_voice.types.language_code
    import capo_chime_sdk_voice.types.list_available_voice_connector_regions_response
    import capo_chime_sdk_voice.types.list_phone_number_orders_request
    import capo_chime_sdk_voice.types.list_phone_number_orders_response
    import capo_chime_sdk_voice.types.list_phone_numbers_request
    import capo_chime_sdk_voice.types.list_phone_numbers_response
    import capo_chime_sdk_voice.types.list_proxy_sessions_request
    import capo_chime_sdk_voice.types.list_proxy_sessions_response
    import capo_chime_sdk_voice.types.list_sip_media_applications_request
    import capo_chime_sdk_voice.types.list_sip_media_applications_response
    import capo_chime_sdk_voice.types.list_sip_rules_request
    import capo_chime_sdk_voice.types.list_sip_rules_response
    import capo_chime_sdk_voice.types.list_supported_phone_number_countries_request
    import capo_chime_sdk_voice.types.list_supported_phone_number_countries_response
    import capo_chime_sdk_voice.types.list_tags_for_resource_request
    import capo_chime_sdk_voice.types.list_tags_for_resource_response
    import capo_chime_sdk_voice.types.list_voice_connector_groups_request
    import capo_chime_sdk_voice.types.list_voice_connector_groups_response
    import capo_chime_sdk_voice.types.list_voice_connector_termination_credentials_request
    import capo_chime_sdk_voice.types.list_voice_connector_termination_credentials_response
    import capo_chime_sdk_voice.types.list_voice_connectors_request
    import capo_chime_sdk_voice.types.list_voice_connectors_response
    import capo_chime_sdk_voice.types.list_voice_profile_domains_request
    import capo_chime_sdk_voice.types.list_voice_profile_domains_response
    import capo_chime_sdk_voice.types.list_voice_profiles_request
    import capo_chime_sdk_voice.types.list_voice_profiles_response
    import capo_chime_sdk_voice.types.logging_configuration
    import capo_chime_sdk_voice.types.network_type
    import capo_chime_sdk_voice.types.next_token_string
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.non_empty_string128
    import capo_chime_sdk_voice.types.non_empty_string256
    import capo_chime_sdk_voice.types.non_empty_string_list
    import capo_chime_sdk_voice.types.nullable_boolean
    import capo_chime_sdk_voice.types.number_selection_behavior
    import capo_chime_sdk_voice.types.origination
    import capo_chime_sdk_voice.types.participant_phone_number_list
    import capo_chime_sdk_voice.types.phone_number_association_name
    import capo_chime_sdk_voice.types.phone_number_max_results
    import capo_chime_sdk_voice.types.phone_number_name
    import capo_chime_sdk_voice.types.phone_number_product_type
    import capo_chime_sdk_voice.types.phone_number_type
    import capo_chime_sdk_voice.types.positive_integer
    import capo_chime_sdk_voice.types.proxy_session_name_string
    import capo_chime_sdk_voice.types.proxy_session_status
    import capo_chime_sdk_voice.types.put_sip_media_application_alexa_skill_configuration_request
    import capo_chime_sdk_voice.types.put_sip_media_application_alexa_skill_configuration_response
    import capo_chime_sdk_voice.types.put_sip_media_application_logging_configuration_request
    import capo_chime_sdk_voice.types.put_sip_media_application_logging_configuration_response
    import capo_chime_sdk_voice.types.put_voice_connector_emergency_calling_configuration_request
    import capo_chime_sdk_voice.types.put_voice_connector_emergency_calling_configuration_response
    import capo_chime_sdk_voice.types.put_voice_connector_external_systems_configuration_request
    import capo_chime_sdk_voice.types.put_voice_connector_external_systems_configuration_response
    import capo_chime_sdk_voice.types.put_voice_connector_logging_configuration_request
    import capo_chime_sdk_voice.types.put_voice_connector_logging_configuration_response
    import capo_chime_sdk_voice.types.put_voice_connector_origination_request
    import capo_chime_sdk_voice.types.put_voice_connector_origination_response
    import capo_chime_sdk_voice.types.put_voice_connector_proxy_request
    import capo_chime_sdk_voice.types.put_voice_connector_proxy_response
    import capo_chime_sdk_voice.types.put_voice_connector_streaming_configuration_request
    import capo_chime_sdk_voice.types.put_voice_connector_streaming_configuration_response
    import capo_chime_sdk_voice.types.put_voice_connector_termination_credentials_request
    import capo_chime_sdk_voice.types.put_voice_connector_termination_request
    import capo_chime_sdk_voice.types.put_voice_connector_termination_response
    import capo_chime_sdk_voice.types.restore_phone_number_request
    import capo_chime_sdk_voice.types.restore_phone_number_response
    import capo_chime_sdk_voice.types.result_max
    import capo_chime_sdk_voice.types.search_available_phone_numbers_request
    import capo_chime_sdk_voice.types.search_available_phone_numbers_response
    import capo_chime_sdk_voice.types.sensitive_non_empty_string
    import capo_chime_sdk_voice.types.sensitive_string_list
    import capo_chime_sdk_voice.types.server_side_encryption_configuration
    import capo_chime_sdk_voice.types.session_border_controller_type_list
    import capo_chime_sdk_voice.types.sip_headers_map
    import capo_chime_sdk_voice.types.sip_media_application
    import capo_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration
    import capo_chime_sdk_voice.types.sip_media_application_endpoint_list
    import capo_chime_sdk_voice.types.sip_media_application_logging_configuration
    import capo_chime_sdk_voice.types.sip_media_application_name
    import capo_chime_sdk_voice.types.sip_rule
    import capo_chime_sdk_voice.types.sip_rule_name
    import capo_chime_sdk_voice.types.sip_rule_target_application_list
    import capo_chime_sdk_voice.types.sip_rule_trigger_type
    import capo_chime_sdk_voice.types.sma_create_call_arguments_map
    import capo_chime_sdk_voice.types.sma_update_call_arguments_map
    import capo_chime_sdk_voice.types.start_speaker_search_task_request
    import capo_chime_sdk_voice.types.start_speaker_search_task_response
    import capo_chime_sdk_voice.types.start_voice_tone_analysis_task_request
    import capo_chime_sdk_voice.types.start_voice_tone_analysis_task_response
    import capo_chime_sdk_voice.types.stop_speaker_search_task_request
    import capo_chime_sdk_voice.types.stop_voice_tone_analysis_task_request
    import capo_chime_sdk_voice.types.streaming_configuration
    import capo_chime_sdk_voice.types.string
    import capo_chime_sdk_voice.types.tag_key_list
    import capo_chime_sdk_voice.types.tag_list
    import capo_chime_sdk_voice.types.tag_resource_request
    import capo_chime_sdk_voice.types.termination
    import capo_chime_sdk_voice.types.toll_free_prefix
    import capo_chime_sdk_voice.types.untag_resource_request
    import capo_chime_sdk_voice.types.update_global_settings_request
    import capo_chime_sdk_voice.types.update_phone_number_request
    import capo_chime_sdk_voice.types.update_phone_number_request_item_list
    import capo_chime_sdk_voice.types.update_phone_number_response
    import capo_chime_sdk_voice.types.update_phone_number_settings_request
    import capo_chime_sdk_voice.types.update_proxy_session_request
    import capo_chime_sdk_voice.types.update_proxy_session_response
    import capo_chime_sdk_voice.types.update_sip_media_application_call_request
    import capo_chime_sdk_voice.types.update_sip_media_application_call_response
    import capo_chime_sdk_voice.types.update_sip_media_application_request
    import capo_chime_sdk_voice.types.update_sip_media_application_response
    import capo_chime_sdk_voice.types.update_sip_rule_request
    import capo_chime_sdk_voice.types.update_sip_rule_response
    import capo_chime_sdk_voice.types.update_voice_connector_group_request
    import capo_chime_sdk_voice.types.update_voice_connector_group_response
    import capo_chime_sdk_voice.types.update_voice_connector_request
    import capo_chime_sdk_voice.types.update_voice_connector_response
    import capo_chime_sdk_voice.types.update_voice_profile_domain_request
    import capo_chime_sdk_voice.types.update_voice_profile_domain_response
    import capo_chime_sdk_voice.types.update_voice_profile_request
    import capo_chime_sdk_voice.types.update_voice_profile_response
    import capo_chime_sdk_voice.types.validate_e911_address_request
    import capo_chime_sdk_voice.types.validate_e911_address_response
    import capo_chime_sdk_voice.types.voice_connector_aws_region
    import capo_chime_sdk_voice.types.voice_connector_group_name
    import capo_chime_sdk_voice.types.voice_connector_id
    import capo_chime_sdk_voice.types.voice_connector_integration_type
    import capo_chime_sdk_voice.types.voice_connector_item_list
    import capo_chime_sdk_voice.types.voice_connector_name
    import capo_chime_sdk_voice.types.voice_connector_settings
    import capo_chime_sdk_voice.types.voice_profile_domain_description
    import capo_chime_sdk_voice.types.voice_profile_domain_name


class ChimeSDKVoiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ChimeSDKVoiceClient:
    """A client for the ``ChimeSDKVoice`` service.

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
        self._config = ChimeSDKVoiceClientConfig(
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
        self, config_overrides: Optional[ChimeSDKVoiceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ChimeSDKVoiceClientConfig = config_overrides or {}
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

    def associate_phone_numbers_with_voice_connector(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        e164_phone_numbers: "capo_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        force_associate: Optional[
            "capo_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_response.AssociatePhoneNumbersWithVoiceConnectorResponse":
        """<p>Associates phone numbers with the specified Amazon Chime SDK Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            e164_phone_numbers: <p>List of phone numbers, in E.164 format.</p>
            force_associate: <p>If true, associates the provided phone numbers with the provided Amazon Chime SDK Voice Connector and removes any previously existing associations. If false, does not associate any phone numbers that have previously existing associations.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_request.AssociatePhoneNumbersWithVoiceConnectorRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_response.AssociatePhoneNumbersWithVoiceConnectorResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.associate_phone_numbers_with_voice_connector

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.associate_phone_numbers_with_voice_connector.associate_phone_numbers_with_voice_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_request.AssociatePhoneNumbersWithVoiceConnectorRequest = {
            "voice_connector_id": voice_connector_id,
            "e164_phone_numbers": e164_phone_numbers,
        }
        if force_associate is not None:
            input_["force_associate"] = force_associate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_phone_numbers_with_voice_connector_group(
        self,
        voice_connector_group_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        e164_phone_numbers: "capo_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        force_associate: Optional[
            "capo_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_group_response.AssociatePhoneNumbersWithVoiceConnectorGroupResponse":
        """<p>Associates phone numbers with the specified Amazon Chime SDK Voice Connector group.</p>

        Args:
            voice_connector_group_id: <p>The Amazon Chime SDK Voice Connector group ID.</p>
            e164_phone_numbers: <p>List of phone numbers, in E.164 format.</p>
            force_associate: <p>If true, associates the provided phone numbers with the provided Amazon Chime SDK Voice Connector Group and removes any previously existing associations. If false, does not associate any phone numbers that have previously existing associations.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_group_request.AssociatePhoneNumbersWithVoiceConnectorGroupRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_group_response.AssociatePhoneNumbersWithVoiceConnectorGroupResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.associate_phone_numbers_with_voice_connector_group

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.associate_phone_numbers_with_voice_connector_group.associate_phone_numbers_with_voice_connector_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.associate_phone_numbers_with_voice_connector_group_request.AssociatePhoneNumbersWithVoiceConnectorGroupRequest = {
            "voice_connector_group_id": voice_connector_group_id,
            "e164_phone_numbers": e164_phone_numbers,
        }
        if force_associate is not None:
            input_["force_associate"] = force_associate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_phone_number(
        self,
        phone_number_ids: "capo_chime_sdk_voice.types.non_empty_string_list.NonEmptyStringList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.batch_delete_phone_number_response.BatchDeletePhoneNumberResponse":
        """<p> Moves phone numbers into the <b>Deletion queue</b>. Phone numbers must be disassociated from any users or Amazon Chime SDK Voice Connectors before they can be deleted. </p> <p> Phone numbers remain in the <b>Deletion queue</b> for 7 days before they are deleted permanently. </p>

        Args:
            phone_number_ids: <p>List of phone number IDs.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.batch_delete_phone_number_request.BatchDeletePhoneNumberRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.batch_delete_phone_number_response.BatchDeletePhoneNumberResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.batch_delete_phone_number

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.batch_delete_phone_number.batch_delete_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.batch_delete_phone_number_request.BatchDeletePhoneNumberRequest = {
            "phone_number_ids": phone_number_ids
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_phone_number(
        self,
        update_phone_number_request_items: "capo_chime_sdk_voice.types.update_phone_number_request_item_list.UpdatePhoneNumberRequestItemList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse":
        """<p>Updates phone number product types, calling names, or phone number names. You can update one attribute at a time for each <code>UpdatePhoneNumberRequestItem</code>. For example, you can update the product type, the calling name, or phone name. </p> <note> <p>You cannot have a duplicate <code>phoneNumberId</code> in a request.</p> </note>

        Args:
            update_phone_number_request_items: <p>Lists the phone numbers in the update request.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.batch_update_phone_number_request.BatchUpdatePhoneNumberRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.batch_update_phone_number_response.BatchUpdatePhoneNumberResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.batch_update_phone_number

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.batch_update_phone_number.batch_update_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.batch_update_phone_number_request.BatchUpdatePhoneNumberRequest = {
            "update_phone_number_request_items": update_phone_number_request_items
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_phone_number_order(
        self,
        product_type: "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType",
        e164_phone_numbers: "capo_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_voice.types.phone_number_name.PhoneNumberName"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.create_phone_number_order_response.CreatePhoneNumberOrderResponse":
        """<p>Creates an order for phone numbers to be provisioned. For numbers outside the U.S., you must use the Amazon Chime SDK SIP media application dial-in product type.</p>

        Args:
            product_type: <p>The phone number product type.</p>
            e164_phone_numbers: <p>List of phone numbers, in E.164 format.</p>
            name: <p>Specifies the name assigned to one or more phone numbers.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_phone_number_order_request.CreatePhoneNumberOrderRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_phone_number_order_response.CreatePhoneNumberOrderResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_phone_number_order

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_phone_number_order.create_phone_number_order(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_phone_number_order_request.CreatePhoneNumberOrderRequest = {
            "product_type": product_type,
            "e164_phone_numbers": e164_phone_numbers,
        }
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_proxy_session(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        participant_phone_numbers: "capo_chime_sdk_voice.types.participant_phone_number_list.ParticipantPhoneNumberList",
        capabilities: "capo_chime_sdk_voice.types.capability_list.CapabilityList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_voice.types.proxy_session_name_string.ProxySessionNameString"
        ] = None,
        expiry_minutes: Optional[
            "capo_chime_sdk_voice.types.positive_integer.PositiveInteger"
        ] = None,
        number_selection_behavior: Optional[
            "capo_chime_sdk_voice.types.number_selection_behavior.NumberSelectionBehavior"
        ] = None,
        geo_match_level: Optional[
            "capo_chime_sdk_voice.types.geo_match_level.GeoMatchLevel"
        ] = None,
        geo_match_params: Optional[
            "capo_chime_sdk_voice.types.geo_match_params.GeoMatchParams"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.create_proxy_session_response.CreateProxySessionResponse":
        """<p>Creates a proxy session for the specified Amazon Chime SDK Voice Connector for the specified participant phone numbers.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            participant_phone_numbers: <p>The participant phone numbers.</p>
            name: <p>The name of the proxy session.</p>
            expiry_minutes: <p>The number of minutes allowed for the proxy session.</p>
            capabilities: <p>The proxy session's capabilities.</p>
            number_selection_behavior: <p>The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.</p>
            geo_match_level: <p>The preference for matching the country or area code of the proxy phone number with that of the first participant.</p>
            geo_match_params: <p>The country and area code for the proxy phone number.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_proxy_session_request.CreateProxySessionRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_proxy_session_response.CreateProxySessionResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_proxy_session

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_proxy_session.create_proxy_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_proxy_session_request.CreateProxySessionRequest = {
            "voice_connector_id": voice_connector_id,
            "participant_phone_numbers": participant_phone_numbers,
            "capabilities": capabilities,
        }
        if name is not None:
            input_["name"] = name
        if expiry_minutes is not None:
            input_["expiry_minutes"] = expiry_minutes
        if number_selection_behavior is not None:
            input_["number_selection_behavior"] = number_selection_behavior
        if geo_match_level is not None:
            input_["geo_match_level"] = geo_match_level
        if geo_match_params is not None:
            input_["geo_match_params"] = geo_match_params

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sip_media_application(
        self,
        aws_region: "capo_chime_sdk_voice.types.string.String",
        name: "capo_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName",
        endpoints: "capo_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        tags: Optional["capo_chime_sdk_voice.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_voice.types.create_sip_media_application_response.CreateSipMediaApplicationResponse":
        """<p>Creates a SIP media application. For more information about SIP media applications, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html">Managing SIP media applications and rules</a> in the <i>Amazon Chime SDK Administrator Guide</i>.</p>

        Args:
            aws_region: <p>The AWS Region assigned to the SIP media application.</p>
            name: <p>The SIP media application's name.</p>
            endpoints: <p>List of endpoints (Lambda ARNs) specified for the SIP media application.</p>
            tags: <p>The tags assigned to the SIP media application.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_sip_media_application_request.CreateSipMediaApplicationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_sip_media_application_response.CreateSipMediaApplicationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_sip_media_application

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_sip_media_application.create_sip_media_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_sip_media_application_request.CreateSipMediaApplicationRequest = {
            "aws_region": aws_region,
            "name": name,
            "endpoints": endpoints,
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

    def create_sip_media_application_call(
        self,
        from_phone_number: "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber",
        to_phone_number: "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber",
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        sip_headers: Optional[
            "capo_chime_sdk_voice.types.sip_headers_map.SipHeadersMap"
        ] = None,
        arguments_map: Optional[
            "capo_chime_sdk_voice.types.sma_create_call_arguments_map.SMACreateCallArgumentsMap"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.create_sip_media_application_call_response.CreateSipMediaApplicationCallResponse":
        """<p>Creates an outbound call to a phone number from the phone number specified in the request, and it invokes the endpoint of the specified <code>sipMediaApplicationId</code>.</p>

        Args:
            from_phone_number: <p>The phone number that a user calls from. This is a phone number in your Amazon Chime SDK phone number inventory.</p>
            to_phone_number: <p>The phone number that the service should call.</p>
            sip_media_application_id: <p>The ID of the SIP media application.</p>
            sip_headers: <p>The SIP headers added to an outbound call leg.</p>
            arguments_map: <p>Context passed to a CreateSipMediaApplication API call. For example, you could pass key-value pairs such as: <code>"FirstName": "John", "LastName": "Doe"</code> </p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_sip_media_application_call_request.CreateSipMediaApplicationCallRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_sip_media_application_call_response.CreateSipMediaApplicationCallResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_sip_media_application_call

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_sip_media_application_call.create_sip_media_application_call(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_sip_media_application_call_request.CreateSipMediaApplicationCallRequest = {
            "from_phone_number": from_phone_number,
            "to_phone_number": to_phone_number,
            "sip_media_application_id": sip_media_application_id,
        }
        if sip_headers is not None:
            input_["sip_headers"] = sip_headers
        if arguments_map is not None:
            input_["arguments_map"] = arguments_map

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sip_rule(
        self,
        name: "capo_chime_sdk_voice.types.sip_rule_name.SipRuleName",
        trigger_type: "capo_chime_sdk_voice.types.sip_rule_trigger_type.SipRuleTriggerType",
        trigger_value: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        target_applications: "capo_chime_sdk_voice.types.sip_rule_target_application_list.SipRuleTargetApplicationList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        disabled: Optional[
            "capo_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.create_sip_rule_response.CreateSipRuleResponse":
        """<p>Creates a SIP rule, which can be used to run a SIP media application as a target for a specific trigger type. For more information about SIP rules, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html">Managing SIP media applications and rules</a> in the <i>Amazon Chime SDK Administrator Guide</i>.</p>

        Args:
            name: <p>The name of the SIP rule.</p>
            trigger_type: <p>The type of trigger assigned to the SIP rule in <code>TriggerValue</code>, currently <code>RequestUriHostname</code> or <code>ToPhoneNumber</code>.</p>
            trigger_value: <p>If <code>TriggerType</code> is <code>RequestUriHostname</code>, the value can be the outbound host name of a Voice Connector. If <code>TriggerType</code> is <code>ToPhoneNumber</code>, the value can be a customer-owned phone number in the E164 format. The <code>SipMediaApplication</code> specified in the <code>SipRule</code> is triggered if the request URI in an incoming SIP request matches the <code>RequestUriHostname</code>, or if the <code>To</code> header in the incoming SIP request matches the <code>ToPhoneNumber</code> value.</p>
            disabled: <p>Disables or enables a SIP rule. You must disable SIP rules before you can delete them.</p>
            target_applications: <p>List of SIP media applications, with priority and AWS Region. Only one SIP application per AWS Region can be used.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_sip_rule_request.CreateSipRuleRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_sip_rule_response.CreateSipRuleResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_sip_rule

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_sip_rule.create_sip_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_sip_rule_request.CreateSipRuleRequest = {
            "name": name,
            "trigger_type": trigger_type,
            "trigger_value": trigger_value,
            "target_applications": target_applications,
        }
        if disabled is not None:
            input_["disabled"] = disabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_voice_connector(
        self,
        name: "capo_chime_sdk_voice.types.voice_connector_name.VoiceConnectorName",
        require_encryption: "capo_chime_sdk_voice.types.boolean.Boolean",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        aws_region: Optional[
            "capo_chime_sdk_voice.types.voice_connector_aws_region.VoiceConnectorAwsRegion"
        ] = None,
        tags: Optional["capo_chime_sdk_voice.types.tag_list.TagList"] = None,
        integration_type: Optional[
            "capo_chime_sdk_voice.types.voice_connector_integration_type.VoiceConnectorIntegrationType"
        ] = None,
        network_type: Optional[
            "capo_chime_sdk_voice.types.network_type.NetworkType"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.create_voice_connector_response.CreateVoiceConnectorResponse":
        """<p>Creates an Amazon Chime SDK Voice Connector. For more information about Voice Connectors, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connector-groups.html">Managing Amazon Chime SDK Voice Connector groups</a> in the <i>Amazon Chime SDK Administrator Guide</i>.</p>

        Args:
            name: <p>The name of the Voice Connector.</p>
            aws_region: <p>The AWS Region in which the Amazon Chime SDK Voice Connector is created. Default value: <code>us-east-1</code> .</p>
            require_encryption: <p>Enables or disables encryption for the Voice Connector.</p>
            tags: <p>The tags assigned to the Voice Connector.</p>
            integration_type: <p>The connectors for use with Connect Customer.</p> <p>The following options are available:</p> <ul> <li> <p> <code>CONNECT_CALL_TRANSFER_CONNECTOR</code> - Enables enterprises to integrate Connect Customer with other voice systems to directly transfer voice calls and metadata without using the public telephone network. They can use Connect Customer telephony and Interactive Voice Response (IVR) with their existing voice systems to modernize the IVR experience of their existing contact center and their enterprise and branch voice systems. Additionally, enterprises migrating their contact center to Connect Customer can start with Connect telephony and IVR for immediate modernization ahead of agent migration.</p> <note> <p>This integration is a gated feature. Please reach out to your account team to discuss this feature with a Connect Specialist.</p> </note> </li> <li> <p> <code>CONNECT_ANALYTICS_CONNECTOR</code> - Enables enterprises to integrate Connect Customer with other voice systems for real-time and post-call analytics. They can use Connect Customer Contact Lens with their existing voice systems to provides call recordings, conversational analytics (including contact transcript, sensitive data redaction, content categorization, theme detection, sentiment analysis, real-time alerts, and post-contact summary), and agent performance evaluations (including evaluation forms, automated evaluation, supervisor review) with a rich user experience to display, search and filter customer interactions, and programmatic access to data streams and the data lake. Additionally, enterprises migrating their contact center to Connect Customer can start with Contact Lens analytics and performance insights ahead of agent migration.</p> </li> </ul>
            network_type: <p>The type of network for the Voice Connector.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_voice_connector_request.CreateVoiceConnectorRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_voice_connector_response.CreateVoiceConnectorResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_connector

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_connector.create_voice_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_voice_connector_request.CreateVoiceConnectorRequest = {
            "name": name,
            "require_encryption": require_encryption,
        }
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if tags is not None:
            input_["tags"] = tags
        if integration_type is not None:
            input_["integration_type"] = integration_type
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_voice_connector_group(
        self,
        name: "capo_chime_sdk_voice.types.voice_connector_group_name.VoiceConnectorGroupName",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        voice_connector_items: Optional[
            "capo_chime_sdk_voice.types.voice_connector_item_list.VoiceConnectorItemList"
        ] = None,
        call_distribution_type: Optional[
            "capo_chime_sdk_voice.types.call_distribution_type.CallDistributionType"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.create_voice_connector_group_response.CreateVoiceConnectorGroupResponse":
        """<p>Creates an Amazon Chime SDK Voice Connector group under the administrator's AWS account. You can associate Amazon Chime SDK Voice Connectors with the Voice Connector group by including <code>VoiceConnectorItems</code> in the request. </p> <p>You can include Voice Connectors from different AWS Regions in your group. This creates a fault tolerant mechanism for fallback in case of availability events.</p>

        Args:
            name: <p>The name of the Voice Connector group.</p>
            voice_connector_items: <p>Lists the Voice Connectors that inbound calls are routed to.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_voice_connector_group_request.CreateVoiceConnectorGroupRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_voice_connector_group_response.CreateVoiceConnectorGroupResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_connector_group

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_connector_group.create_voice_connector_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_voice_connector_group_request.CreateVoiceConnectorGroupRequest = {
            "name": name
        }
        if voice_connector_items is not None:
            input_["voice_connector_items"] = voice_connector_items
        if call_distribution_type is not None:
            input_["call_distribution_type"] = call_distribution_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_voice_profile(
        self,
        speaker_search_task_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.create_voice_profile_response.CreateVoiceProfileResponse":
        """<p>Creates a voice profile, which consists of an enrolled user and their latest voice print.</p> <important> <p>Before creating any voice profiles, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the <a href="https://aws.amazon.com/service-terms/">AWS service terms</a> for the Amazon Chime SDK.</p> </important> <p>For more information about voice profiles and voice analytics, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-voice-analytics.html">Using Amazon Chime SDK Voice Analytics</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            speaker_search_task_id: <p>The ID of the speaker search task.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.gone_exception.GoneException: <p>Access to the target resource is no longer available at the origin server. This condition is likely to be permanent.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_voice_profile_request.CreateVoiceProfileRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_voice_profile_response.CreateVoiceProfileResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_profile

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_profile.create_voice_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_voice_profile_request.CreateVoiceProfileRequest = {
            "speaker_search_task_id": speaker_search_task_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_voice_profile_domain(
        self,
        name: "capo_chime_sdk_voice.types.voice_profile_domain_name.VoiceProfileDomainName",
        server_side_encryption_configuration: "capo_chime_sdk_voice.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        description: Optional[
            "capo_chime_sdk_voice.types.voice_profile_domain_description.VoiceProfileDomainDescription"
        ] = None,
        client_request_token: Optional[
            "capo_chime_sdk_voice.types.client_request_id.ClientRequestId"
        ] = None,
        tags: Optional["capo_chime_sdk_voice.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_voice.types.create_voice_profile_domain_response.CreateVoiceProfileDomainResponse":
        """<p>Creates a voice profile domain, a collection of voice profiles, their voice prints, and encrypted enrollment audio.</p> <important> <p>Before creating any voice profiles, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the <a href="https://aws.amazon.com/service-terms/">AWS service terms</a> for the Amazon Chime SDK.</p> </important> <p>For more information about voice profile domains, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-voice-analytics.html">Using Amazon Chime SDK Voice Analytics</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            name: <p>The name of the voice profile domain.</p>
            description: <p>A description of the voice profile domain.</p>
            server_side_encryption_configuration: <p>The server-side encryption configuration for the request.</p>
            client_request_token: <p>The unique identifier for the client request. Use a different token for different domain creation requests.</p>
            tags: <p>The tags assigned to the domain.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.create_voice_profile_domain_request.CreateVoiceProfileDomainRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.create_voice_profile_domain_response.CreateVoiceProfileDomainResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_profile_domain

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.create_voice_profile_domain.create_voice_profile_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.create_voice_profile_domain_request.CreateVoiceProfileDomainRequest = {
            "name": name,
            "server_side_encryption_configuration": server_side_encryption_configuration,
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_phone_number(
        self,
        phone_number_id: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Moves the specified phone number into the <b>Deletion queue</b>. A phone number must be disassociated from any users or Amazon Chime SDK Voice Connectors before it can be deleted.</p> <p>Deleted phone numbers remain in the <b>Deletion queue</b> queue for 7 days before they are deleted permanently.</p>

        Args:
            phone_number_id: <p>The phone number ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_phone_number_request.DeletePhoneNumberRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_phone_number

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_phone_number.delete_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_phone_number_request.DeletePhoneNumberRequest = {
            "phone_number_id": phone_number_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_proxy_session(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        proxy_session_id: "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified proxy session from the specified Amazon Chime SDK Voice Connector.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            proxy_session_id: <p>The proxy session ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_proxy_session_request.DeleteProxySessionRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_proxy_session

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_proxy_session.delete_proxy_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_proxy_session_request.DeleteProxySessionRequest = {
            "voice_connector_id": voice_connector_id,
            "proxy_session_id": proxy_session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sip_media_application(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes a SIP media application.</p>

        Args:
            sip_media_application_id: <p>The SIP media application ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_sip_media_application_request.DeleteSipMediaApplicationRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_sip_media_application

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_sip_media_application.delete_sip_media_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_sip_media_application_request.DeleteSipMediaApplicationRequest = {
            "sip_media_application_id": sip_media_application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sip_rule(
        self,
        sip_rule_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes a SIP rule.</p>

        Args:
            sip_rule_id: <p>The SIP rule ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_sip_rule_request.DeleteSipRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_sip_rule

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_sip_rule.delete_sip_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_sip_rule_request.DeleteSipRuleRequest = {
            "sip_rule_id": sip_rule_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Chime SDK Voice Connector. Any phone numbers associated with the Amazon Chime SDK Voice Connector must be disassociated from it before it can be deleted.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_request.DeleteVoiceConnectorRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector.delete_voice_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_request.DeleteVoiceConnectorRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_emergency_calling_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the emergency calling details from the specified Amazon Chime SDK Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_emergency_calling_configuration_request.DeleteVoiceConnectorEmergencyCallingConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_emergency_calling_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_emergency_calling_configuration.delete_voice_connector_emergency_calling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_emergency_calling_configuration_request.DeleteVoiceConnectorEmergencyCallingConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_external_systems_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the external systems configuration for a Voice Connector.</p>

        Args:
            voice_connector_id: <p>The ID of the Voice Connector for which to delete the external system configuration.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_external_systems_configuration_request.DeleteVoiceConnectorExternalSystemsConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_external_systems_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_external_systems_configuration.delete_voice_connector_external_systems_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_external_systems_configuration_request.DeleteVoiceConnectorExternalSystemsConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_group(
        self,
        voice_connector_group_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Chime SDK Voice Connector group. Any <code>VoiceConnectorItems</code> and phone numbers associated with the group must be removed before it can be deleted.</p>

        Args:
            voice_connector_group_id: <p>The Voice Connector Group ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_group_request.DeleteVoiceConnectorGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_group

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_group.delete_voice_connector_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_group_request.DeleteVoiceConnectorGroupRequest = {
            "voice_connector_group_id": voice_connector_group_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_origination(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the origination settings for the specified Amazon Chime SDK Voice Connector. </p> <note> <p>If emergency calling is configured for the Voice Connector, it must be deleted prior to deleting the origination settings.</p> </note>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_origination_request.DeleteVoiceConnectorOriginationRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_origination

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_origination.delete_voice_connector_origination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_origination_request.DeleteVoiceConnectorOriginationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_proxy(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the proxy configuration from the specified Amazon Chime SDK Voice Connector.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_proxy_request.DeleteVoiceConnectorProxyRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_proxy

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_proxy.delete_voice_connector_proxy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_proxy_request.DeleteVoiceConnectorProxyRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_streaming_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes a Voice Connector's streaming configuration.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_streaming_configuration_request.DeleteVoiceConnectorStreamingConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_streaming_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_streaming_configuration.delete_voice_connector_streaming_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_streaming_configuration_request.DeleteVoiceConnectorStreamingConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_termination(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the termination settings for the specified Amazon Chime SDK Voice Connector.</p> <note> <p>If emergency calling is configured for the Voice Connector, it must be deleted prior to deleting the termination settings.</p> </note>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_termination_request.DeleteVoiceConnectorTerminationRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_termination

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_termination.delete_voice_connector_termination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_termination_request.DeleteVoiceConnectorTerminationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_connector_termination_credentials(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        usernames: "capo_chime_sdk_voice.types.sensitive_string_list.SensitiveStringList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified SIP credentials used by your equipment to authenticate during call termination.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            usernames: <p>The RFC2617 compliant username associated with the SIP credentials, in US-ASCII format.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_connector_termination_credentials_request.DeleteVoiceConnectorTerminationCredentialsRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_termination_credentials

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_connector_termination_credentials.delete_voice_connector_termination_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_connector_termination_credentials_request.DeleteVoiceConnectorTerminationCredentialsRequest = {
            "voice_connector_id": voice_connector_id,
            "usernames": usernames,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_profile(
        self,
        voice_profile_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes a voice profile, including its voice print and enrollment data. WARNING: This action is not reversible.</p>

        Args:
            voice_profile_id: <p>The voice profile ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_profile_request.DeleteVoiceProfileRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_profile

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_profile.delete_voice_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_profile_request.DeleteVoiceProfileRequest = {
            "voice_profile_id": voice_profile_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_voice_profile_domain(
        self,
        voice_profile_domain_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Deletes all voice profiles in the domain. WARNING: This action is not reversible.</p>

        Args:
            voice_profile_domain_id: <p>The voice profile domain ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.delete_voice_profile_domain_request.DeleteVoiceProfileDomainRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_profile_domain

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.delete_voice_profile_domain.delete_voice_profile_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.delete_voice_profile_domain_request.DeleteVoiceProfileDomainRequest = {
            "voice_profile_domain_id": voice_profile_domain_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_phone_numbers_from_voice_connector(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        e164_phone_numbers: "capo_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_response.DisassociatePhoneNumbersFromVoiceConnectorResponse":
        """<p>Disassociates the specified phone numbers from the specified Amazon Chime SDK Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            e164_phone_numbers: <p>List of phone numbers, in E.164 format.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_request.DisassociatePhoneNumbersFromVoiceConnectorRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_response.DisassociatePhoneNumbersFromVoiceConnectorResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.disassociate_phone_numbers_from_voice_connector

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.disassociate_phone_numbers_from_voice_connector.disassociate_phone_numbers_from_voice_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_request.DisassociatePhoneNumbersFromVoiceConnectorRequest = {
            "voice_connector_id": voice_connector_id,
            "e164_phone_numbers": e164_phone_numbers,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_phone_numbers_from_voice_connector_group(
        self,
        voice_connector_group_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        e164_phone_numbers: "capo_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_group_response.DisassociatePhoneNumbersFromVoiceConnectorGroupResponse":
        """<p>Disassociates the specified phone numbers from the specified Amazon Chime SDK Voice Connector group.</p>

        Args:
            voice_connector_group_id: <p>The Voice Connector group ID.</p>
            e164_phone_numbers: <p>The list of phone numbers, in E.164 format.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_group_request.DisassociatePhoneNumbersFromVoiceConnectorGroupRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_group_response.DisassociatePhoneNumbersFromVoiceConnectorGroupResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.disassociate_phone_numbers_from_voice_connector_group

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.disassociate_phone_numbers_from_voice_connector_group.disassociate_phone_numbers_from_voice_connector_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.disassociate_phone_numbers_from_voice_connector_group_request.DisassociatePhoneNumbersFromVoiceConnectorGroupRequest = {
            "voice_connector_group_id": voice_connector_group_id,
            "e164_phone_numbers": e164_phone_numbers,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_global_settings(
        self, *, config_overrides: Optional[ChimeSDKVoiceClientConfig] = None
    ) -> "capo_chime_sdk_voice.types.get_global_settings_response.GetGlobalSettingsResponse":
        """<p>Retrieves the global settings for the Amazon Chime SDK Voice Connectors in an AWS account.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_global_settings_response.GetGlobalSettingsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_global_settings

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_global_settings.get_global_settings(
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

    def get_phone_number(
        self,
        phone_number_id: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_phone_number_response.GetPhoneNumberResponse":
        """<p>Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.</p>

        Args:
            phone_number_id: <p>The phone number ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_phone_number_request.GetPhoneNumberRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_phone_number_response.GetPhoneNumberResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_phone_number

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_phone_number.get_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_phone_number_request.GetPhoneNumberRequest = {
            "phone_number_id": phone_number_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_phone_number_order(
        self,
        phone_number_order_id: "capo_chime_sdk_voice.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_phone_number_order_response.GetPhoneNumberOrderResponse":
        """<p>Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.</p>

        Args:
            phone_number_order_id: <p>The ID of the phone number order .</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_phone_number_order_request.GetPhoneNumberOrderRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_phone_number_order_response.GetPhoneNumberOrderResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_phone_number_order

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_phone_number_order.get_phone_number_order(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_phone_number_order_request.GetPhoneNumberOrderRequest = {
            "phone_number_order_id": phone_number_order_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_phone_number_settings(
        self, *, config_overrides: Optional[ChimeSDKVoiceClientConfig] = None
    ) -> "capo_chime_sdk_voice.types.get_phone_number_settings_response.GetPhoneNumberSettingsResponse":
        """<p>Retrieves the phone number settings for the administrator's AWS account, such as the default outbound calling name.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_phone_number_settings_response.GetPhoneNumberSettingsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_phone_number_settings

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_phone_number_settings.get_phone_number_settings(
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

    def get_proxy_session(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        proxy_session_id: "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> (
        "capo_chime_sdk_voice.types.get_proxy_session_response.GetProxySessionResponse"
    ):
        """<p>Retrieves the specified proxy session details for the specified Amazon Chime SDK Voice Connector.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            proxy_session_id: <p>The proxy session ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_proxy_session_request.GetProxySessionRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_proxy_session_response.GetProxySessionResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_proxy_session

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_proxy_session.get_proxy_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_proxy_session_request.GetProxySessionRequest = {
            "voice_connector_id": voice_connector_id,
            "proxy_session_id": proxy_session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sip_media_application(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_sip_media_application_response.GetSipMediaApplicationResponse":
        """<p>Retrieves the information for a SIP media application, including name, AWS Region, and endpoints.</p>

        Args:
            sip_media_application_id: <p>The SIP media application ID .</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_sip_media_application_request.GetSipMediaApplicationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_sip_media_application_response.GetSipMediaApplicationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_media_application

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_media_application.get_sip_media_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_sip_media_application_request.GetSipMediaApplicationRequest = {
            "sip_media_application_id": sip_media_application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sip_media_application_alexa_skill_configuration(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_sip_media_application_alexa_skill_configuration_response.GetSipMediaApplicationAlexaSkillConfigurationResponse":
        """<p>Gets the Alexa Skill configuration for the SIP media application.</p> <important> <p>Due to changes made by the Amazon Alexa service, this API is no longer available for use. For more information, refer to the <a href="https://developer.amazon.com/en-US/alexa/alexasmartproperties">Alexa Smart Properties</a> page.</p> </important>

        Args:
            sip_media_application_id: <p>The SIP media application ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.gone_exception.GoneException: <p>Access to the target resource is no longer available at the origin server. This condition is likely to be permanent.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_sip_media_application_alexa_skill_configuration_request.GetSipMediaApplicationAlexaSkillConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_sip_media_application_alexa_skill_configuration_response.GetSipMediaApplicationAlexaSkillConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_media_application_alexa_skill_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_media_application_alexa_skill_configuration.get_sip_media_application_alexa_skill_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_sip_media_application_alexa_skill_configuration_request.GetSipMediaApplicationAlexaSkillConfigurationRequest = {
            "sip_media_application_id": sip_media_application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sip_media_application_logging_configuration(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_sip_media_application_logging_configuration_response.GetSipMediaApplicationLoggingConfigurationResponse":
        """<p>Retrieves the logging configuration for the specified SIP media application.</p>

        Args:
            sip_media_application_id: <p>The SIP media application ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_sip_media_application_logging_configuration_request.GetSipMediaApplicationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_sip_media_application_logging_configuration_response.GetSipMediaApplicationLoggingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_media_application_logging_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_media_application_logging_configuration.get_sip_media_application_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_sip_media_application_logging_configuration_request.GetSipMediaApplicationLoggingConfigurationRequest = {
            "sip_media_application_id": sip_media_application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sip_rule(
        self,
        sip_rule_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_sip_rule_response.GetSipRuleResponse":
        """<p>Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and target endpoints.</p>

        Args:
            sip_rule_id: <p>The SIP rule ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_sip_rule_request.GetSipRuleRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_sip_rule_response.GetSipRuleResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_rule

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_sip_rule.get_sip_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_sip_rule_request.GetSipRuleRequest = {
            "sip_rule_id": sip_rule_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_speaker_search_task(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        speaker_search_task_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_speaker_search_task_response.GetSpeakerSearchTaskResponse":
        """<p>Retrieves the details of the specified speaker search task.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            speaker_search_task_id: <p>The ID of the speaker search task.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_speaker_search_task_request.GetSpeakerSearchTaskRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_speaker_search_task_response.GetSpeakerSearchTaskResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_speaker_search_task

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_speaker_search_task.get_speaker_search_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_speaker_search_task_request.GetSpeakerSearchTaskRequest = {
            "voice_connector_id": voice_connector_id,
            "speaker_search_task_id": speaker_search_task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_response.GetVoiceConnectorResponse":
        """<p>Retrieves details for the specified Amazon Chime SDK Voice Connector, such as timestamps,name, outbound host, and encryption requirements.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_request.GetVoiceConnectorRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_response.GetVoiceConnectorResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector.get_voice_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_request.GetVoiceConnectorRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_emergency_calling_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_emergency_calling_configuration_response.GetVoiceConnectorEmergencyCallingConfigurationResponse":
        """<p>Retrieves the emergency calling configuration details for the specified Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_emergency_calling_configuration_request.GetVoiceConnectorEmergencyCallingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_emergency_calling_configuration_response.GetVoiceConnectorEmergencyCallingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_emergency_calling_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_emergency_calling_configuration.get_voice_connector_emergency_calling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_emergency_calling_configuration_request.GetVoiceConnectorEmergencyCallingConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_external_systems_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_external_systems_configuration_response.GetVoiceConnectorExternalSystemsConfigurationResponse":
        """<p>Gets information about an external systems configuration for a Voice Connector.</p>

        Args:
            voice_connector_id: <p>The ID of the Voice Connector for which to return information about the external system configuration.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_external_systems_configuration_request.GetVoiceConnectorExternalSystemsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_external_systems_configuration_response.GetVoiceConnectorExternalSystemsConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_external_systems_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_external_systems_configuration.get_voice_connector_external_systems_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_external_systems_configuration_request.GetVoiceConnectorExternalSystemsConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_group(
        self,
        voice_connector_group_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_group_response.GetVoiceConnectorGroupResponse":
        """<p>Retrieves details for the specified Amazon Chime SDK Voice Connector group, such as timestamps,name, and associated <code>VoiceConnectorItems</code>.</p>

        Args:
            voice_connector_group_id: <p>The Voice Connector group ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_group_request.GetVoiceConnectorGroupRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_group_response.GetVoiceConnectorGroupResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_group

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_group.get_voice_connector_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_group_request.GetVoiceConnectorGroupRequest = {
            "voice_connector_group_id": voice_connector_group_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_logging_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_logging_configuration_response.GetVoiceConnectorLoggingConfigurationResponse":
        """<p>Retrieves the logging configuration settings for the specified Voice Connector. Shows whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_logging_configuration_request.GetVoiceConnectorLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_logging_configuration_response.GetVoiceConnectorLoggingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_logging_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_logging_configuration.get_voice_connector_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_logging_configuration_request.GetVoiceConnectorLoggingConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_origination(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_origination_response.GetVoiceConnectorOriginationResponse":
        """<p>Retrieves the origination settings for the specified Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_origination_request.GetVoiceConnectorOriginationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_origination_response.GetVoiceConnectorOriginationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_origination

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_origination.get_voice_connector_origination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_origination_request.GetVoiceConnectorOriginationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_proxy(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_proxy_response.GetVoiceConnectorProxyResponse":
        """<p>Retrieves the proxy configuration details for the specified Amazon Chime SDK Voice Connector.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_proxy_request.GetVoiceConnectorProxyRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_proxy_response.GetVoiceConnectorProxyResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_proxy

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_proxy.get_voice_connector_proxy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_proxy_request.GetVoiceConnectorProxyRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_streaming_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_streaming_configuration_response.GetVoiceConnectorStreamingConfigurationResponse":
        """<p>Retrieves the streaming configuration details for the specified Amazon Chime SDK Voice Connector. Shows whether media streaming is enabled for sending to Amazon Kinesis. It also shows the retention period, in hours, for the Amazon Kinesis data.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_streaming_configuration_request.GetVoiceConnectorStreamingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_streaming_configuration_response.GetVoiceConnectorStreamingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_streaming_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_streaming_configuration.get_voice_connector_streaming_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_streaming_configuration_request.GetVoiceConnectorStreamingConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_termination(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_termination_response.GetVoiceConnectorTerminationResponse":
        """<p>Retrieves the termination setting details for the specified Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_termination_request.GetVoiceConnectorTerminationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_termination_response.GetVoiceConnectorTerminationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_termination

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_termination.get_voice_connector_termination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_termination_request.GetVoiceConnectorTerminationRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_connector_termination_health(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_connector_termination_health_response.GetVoiceConnectorTerminationHealthResponse":
        """<p>Retrieves information about the last time a <code>SIP OPTIONS</code> ping was received from your SIP infrastructure for the specified Amazon Chime SDK Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_connector_termination_health_request.GetVoiceConnectorTerminationHealthRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_connector_termination_health_response.GetVoiceConnectorTerminationHealthResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_termination_health

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_connector_termination_health.get_voice_connector_termination_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_connector_termination_health_request.GetVoiceConnectorTerminationHealthRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_profile(
        self,
        voice_profile_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> (
        "capo_chime_sdk_voice.types.get_voice_profile_response.GetVoiceProfileResponse"
    ):
        """<p>Retrieves the details of the specified voice profile.</p>

        Args:
            voice_profile_id: <p>The voice profile ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_profile_request.GetVoiceProfileRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_profile_response.GetVoiceProfileResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_profile

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_profile.get_voice_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_profile_request.GetVoiceProfileRequest = {
            "voice_profile_id": voice_profile_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_profile_domain(
        self,
        voice_profile_domain_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_profile_domain_response.GetVoiceProfileDomainResponse":
        """<p>Retrieves the details of the specified voice profile domain.</p>

        Args:
            voice_profile_domain_id: <p>The voice profile domain ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_profile_domain_request.GetVoiceProfileDomainRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_profile_domain_response.GetVoiceProfileDomainResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_profile_domain

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_profile_domain.get_voice_profile_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_profile_domain_request.GetVoiceProfileDomainRequest = {
            "voice_profile_domain_id": voice_profile_domain_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_voice_tone_analysis_task(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        voice_tone_analysis_task_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        is_caller: "capo_chime_sdk_voice.types.boolean.Boolean",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.get_voice_tone_analysis_task_response.GetVoiceToneAnalysisTaskResponse":
        """<p>Retrieves the details of a voice tone analysis task.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            voice_tone_analysis_task_id: <p>The ID of the voice tone analysis task.</p>
            is_caller: <p>Specifies whether the voice being analyzed is the caller (originator) or the callee (responder).</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.get_voice_tone_analysis_task_request.GetVoiceToneAnalysisTaskRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.get_voice_tone_analysis_task_response.GetVoiceToneAnalysisTaskResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_tone_analysis_task

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.get_voice_tone_analysis_task.get_voice_tone_analysis_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.get_voice_tone_analysis_task_request.GetVoiceToneAnalysisTaskRequest = {
            "voice_connector_id": voice_connector_id,
            "voice_tone_analysis_task_id": voice_tone_analysis_task_id,
            "is_caller": is_caller,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_available_voice_connector_regions(
        self, *, config_overrides: Optional[ChimeSDKVoiceClientConfig] = None
    ) -> "capo_chime_sdk_voice.types.list_available_voice_connector_regions_response.ListAvailableVoiceConnectorRegionsResponse":
        """<p>Lists the available AWS Regions in which you can create an Amazon Chime SDK Voice Connector.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_available_voice_connector_regions_response.ListAvailableVoiceConnectorRegionsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_available_voice_connector_regions

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_available_voice_connector_regions.list_available_voice_connector_regions(
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

    def list_phone_number_orders(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "capo_chime_sdk_voice.types.list_phone_number_orders_response.ListPhoneNumberOrdersResponse":
        """<p>Lists the phone numbers for an administrator's Amazon Chime SDK account.</p>

        Args:
            next_token: <p>The token used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_phone_number_orders_request.ListPhoneNumberOrdersRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_phone_number_orders_response.ListPhoneNumberOrdersResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_phone_number_orders

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_phone_number_orders.list_phone_number_orders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_phone_number_orders_request.ListPhoneNumberOrdersRequest = {}
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

    def iter_list_phone_number_orders(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.list_phone_number_orders_response.ListPhoneNumberOrdersResponse]":
        _token = next_token
        while True:
            _response = self.list_phone_number_orders(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_phone_numbers(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        status: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        product_type: Optional[
            "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
        ] = None,
        filter_name: Optional[
            "capo_chime_sdk_voice.types.phone_number_association_name.PhoneNumberAssociationName"
        ] = None,
        filter_value: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
    ) -> "capo_chime_sdk_voice.types.list_phone_numbers_response.ListPhoneNumbersResponse":
        """<p>Lists the phone numbers for the specified Amazon Chime SDK account, Amazon Chime SDK user, Amazon Chime SDK Voice Connector, or Amazon Chime SDK Voice Connector group.</p>

        Args:
            status: <p>The status of your organization's phone numbers.</p>
            product_type: <p>The phone number product types.</p>
            filter_name: <p>The filter to limit the number of results.</p>
            filter_value: <p>The filter value.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token used to return the next page of results.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_phone_numbers_request.ListPhoneNumbersRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_phone_numbers_response.ListPhoneNumbersResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_phone_numbers

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_phone_numbers.list_phone_numbers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_phone_numbers_request.ListPhoneNumbersRequest = {}
        if status is not None:
            input_["status"] = status
        if product_type is not None:
            input_["product_type"] = product_type
        if filter_name is not None:
            input_["filter_name"] = filter_name
        if filter_value is not None:
            input_["filter_value"] = filter_value
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

    def iter_list_phone_numbers(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        status: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        product_type: Optional[
            "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
        ] = None,
        filter_name: Optional[
            "capo_chime_sdk_voice.types.phone_number_association_name.PhoneNumberAssociationName"
        ] = None,
        filter_value: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.list_phone_numbers_response.ListPhoneNumbersResponse]":
        _token = next_token
        while True:
            _response = self.list_phone_numbers(
                config_overrides=config_overrides,
                status=status,
                product_type=product_type,
                filter_name=filter_name,
                filter_value=filter_value,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_proxy_sessions(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        status: Optional[
            "capo_chime_sdk_voice.types.proxy_session_status.ProxySessionStatus"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "capo_chime_sdk_voice.types.list_proxy_sessions_response.ListProxySessionsResponse":
        """<p>Lists the proxy sessions for the specified Amazon Chime SDK Voice Connector.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            status: <p>The proxy session status.</p>
            next_token: <p>The token used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_proxy_sessions_request.ListProxySessionsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_proxy_sessions_response.ListProxySessionsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_proxy_sessions

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_proxy_sessions.list_proxy_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_proxy_sessions_request.ListProxySessionsRequest = {
            "voice_connector_id": voice_connector_id
        }
        if status is not None:
            input_["status"] = status
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

    def iter_list_proxy_sessions(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        status: Optional[
            "capo_chime_sdk_voice.types.proxy_session_status.ProxySessionStatus"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.list_proxy_sessions_response.ListProxySessionsResponse]":
        _token = next_token
        while True:
            _response = self.list_proxy_sessions(
                voice_connector_id,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sip_media_applications(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.list_sip_media_applications_response.ListSipMediaApplicationsResponse":
        """<p>Lists the SIP media applications under the administrator's AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Defaults to 100.</p>
            next_token: <p>The token used to return the next page of results.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_sip_media_applications_request.ListSipMediaApplicationsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_sip_media_applications_response.ListSipMediaApplicationsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_sip_media_applications

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_sip_media_applications.list_sip_media_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_sip_media_applications_request.ListSipMediaApplicationsRequest = {}
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

    def iter_list_sip_media_applications(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
    ) -> (
        "Iterator[capo_chime_sdk_voice.types.sip_media_application.SipMediaApplication]"
    ):
        _token = next_token
        while True:
            _response = self.list_sip_media_applications(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sip_media_applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sip_rules(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        sip_media_application_id: Optional[
            "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.list_sip_rules_response.ListSipRulesResponse":
        """<p>Lists the SIP rules under the administrator's AWS account.</p>

        Args:
            sip_media_application_id: <p>The SIP media application ID.</p>
            max_results: <p>The maximum number of results to return in a single call. Defaults to 100.</p>
            next_token: <p>The token used to return the next page of results.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_sip_rules_request.ListSipRulesRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_sip_rules_response.ListSipRulesResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_sip_rules

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_sip_rules.list_sip_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_sip_rules_request.ListSipRulesRequest = {}
        if sip_media_application_id is not None:
            input_["sip_media_application_id"] = sip_media_application_id
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

    def iter_list_sip_rules(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        sip_media_application_id: Optional[
            "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
        next_token: Optional[
            "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.sip_rule.SipRule]":
        _token = next_token
        while True:
            _response = self.list_sip_rules(
                config_overrides=config_overrides,
                sip_media_application_id=sip_media_application_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sip_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_supported_phone_number_countries(
        self,
        product_type: "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.list_supported_phone_number_countries_response.ListSupportedPhoneNumberCountriesResponse":
        """<p>Lists the countries that you can order phone numbers from.</p>

        Args:
            product_type: <p>The phone number product type.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_supported_phone_number_countries_request.ListSupportedPhoneNumberCountriesRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_supported_phone_number_countries_response.ListSupportedPhoneNumberCountriesResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_supported_phone_number_countries

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_supported_phone_number_countries.list_supported_phone_number_countries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_supported_phone_number_countries_request.ListSupportedPhoneNumberCountriesRequest = {
            "product_type": product_type
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_chime_sdk_voice.types.arn.Arn",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of the tags in a given resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_tags_for_resource

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_voice_connector_groups(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "capo_chime_sdk_voice.types.list_voice_connector_groups_response.ListVoiceConnectorGroupsResponse":
        """<p>Lists the Amazon Chime SDK Voice Connector groups in the administrator's AWS account.</p>

        Args:
            next_token: <p>The token used to return the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call. </p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_voice_connector_groups_request.ListVoiceConnectorGroupsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_voice_connector_groups_response.ListVoiceConnectorGroupsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_connector_groups

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_connector_groups.list_voice_connector_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_voice_connector_groups_request.ListVoiceConnectorGroupsRequest = {}
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

    def iter_list_voice_connector_groups(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.list_voice_connector_groups_response.ListVoiceConnectorGroupsResponse]":
        _token = next_token
        while True:
            _response = self.list_voice_connector_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_voice_connectors(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "capo_chime_sdk_voice.types.list_voice_connectors_response.ListVoiceConnectorsResponse":
        """<p>Lists the Amazon Chime SDK Voice Connectors in the administrators AWS account.</p>

        Args:
            next_token: <p>The token used to return the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_voice_connectors_request.ListVoiceConnectorsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_voice_connectors_response.ListVoiceConnectorsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_connectors

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_connectors.list_voice_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_voice_connectors_request.ListVoiceConnectorsRequest = {}
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

    def iter_list_voice_connectors(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.list_voice_connectors_response.ListVoiceConnectorsResponse]":
        _token = next_token
        while True:
            _response = self.list_voice_connectors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_voice_connector_termination_credentials(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.list_voice_connector_termination_credentials_response.ListVoiceConnectorTerminationCredentialsResponse":
        """<p>Lists the SIP credentials for the specified Amazon Chime SDK Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_voice_connector_termination_credentials_request.ListVoiceConnectorTerminationCredentialsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_voice_connector_termination_credentials_response.ListVoiceConnectorTerminationCredentialsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_connector_termination_credentials

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_connector_termination_credentials.list_voice_connector_termination_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_voice_connector_termination_credentials_request.ListVoiceConnectorTerminationCredentialsRequest = {
            "voice_connector_id": voice_connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_voice_profile_domains(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "capo_chime_sdk_voice.types.list_voice_profile_domains_response.ListVoiceProfileDomainsResponse":
        """<p>Lists the specified voice profile domains in the administrator's AWS account. </p>

        Args:
            next_token: <p>The token used to return the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_voice_profile_domains_request.ListVoiceProfileDomainsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_voice_profile_domains_response.ListVoiceProfileDomainsResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_profile_domains

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_profile_domains.list_voice_profile_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_voice_profile_domains_request.ListVoiceProfileDomainsRequest = {}
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

    def iter_list_voice_profile_domains(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.list_voice_profile_domains_response.ListVoiceProfileDomainsResponse]":
        _token = next_token
        while True:
            _response = self.list_voice_profile_domains(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_voice_profiles(
        self,
        voice_profile_domain_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "capo_chime_sdk_voice.types.list_voice_profiles_response.ListVoiceProfilesResponse":
        """<p>Lists the voice profiles in a voice profile domain.</p>

        Args:
            voice_profile_domain_id: <p>The ID of the voice profile domain.</p>
            next_token: <p>The token used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results in the request.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.list_voice_profiles_request.ListVoiceProfilesRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.list_voice_profiles_response.ListVoiceProfilesResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_profiles

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.list_voice_profiles.list_voice_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.list_voice_profiles_request.ListVoiceProfilesRequest = {
            "voice_profile_domain_id": voice_profile_domain_id
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

    def iter_list_voice_profiles(
        self,
        voice_profile_domain_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        max_results: Optional["capo_chime_sdk_voice.types.result_max.ResultMax"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.list_voice_profiles_response.ListVoiceProfilesResponse]":
        _token = next_token
        while True:
            _response = self.list_voice_profiles(
                voice_profile_domain_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_sip_media_application_alexa_skill_configuration(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        sip_media_application_alexa_skill_configuration: Optional[
            "capo_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration.SipMediaApplicationAlexaSkillConfiguration"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.put_sip_media_application_alexa_skill_configuration_response.PutSipMediaApplicationAlexaSkillConfigurationResponse":
        """<p>Updates the Alexa Skill configuration for the SIP media application.</p> <important> <p>Due to changes made by the Amazon Alexa service, this API is no longer available for use. For more information, refer to the <a href="https://developer.amazon.com/en-US/alexa/alexasmartproperties">Alexa Smart Properties</a> page.</p> </important>

        Args:
            sip_media_application_id: <p>The SIP media application ID.</p>
            sip_media_application_alexa_skill_configuration: <p>The Alexa Skill configuration.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.gone_exception.GoneException: <p>Access to the target resource is no longer available at the origin server. This condition is likely to be permanent.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_sip_media_application_alexa_skill_configuration_request.PutSipMediaApplicationAlexaSkillConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_sip_media_application_alexa_skill_configuration_response.PutSipMediaApplicationAlexaSkillConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_sip_media_application_alexa_skill_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_sip_media_application_alexa_skill_configuration.put_sip_media_application_alexa_skill_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_sip_media_application_alexa_skill_configuration_request.PutSipMediaApplicationAlexaSkillConfigurationRequest = {
            "sip_media_application_id": sip_media_application_id
        }
        if sip_media_application_alexa_skill_configuration is not None:
            input_["sip_media_application_alexa_skill_configuration"] = (
                sip_media_application_alexa_skill_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_sip_media_application_logging_configuration(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        sip_media_application_logging_configuration: Optional[
            "capo_chime_sdk_voice.types.sip_media_application_logging_configuration.SipMediaApplicationLoggingConfiguration"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.put_sip_media_application_logging_configuration_response.PutSipMediaApplicationLoggingConfigurationResponse":
        """<p>Updates the logging configuration for the specified SIP media application.</p>

        Args:
            sip_media_application_id: <p>The SIP media application ID.</p>
            sip_media_application_logging_configuration: <p>The logging configuration for the specified SIP media application.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_sip_media_application_logging_configuration_request.PutSipMediaApplicationLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_sip_media_application_logging_configuration_response.PutSipMediaApplicationLoggingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_sip_media_application_logging_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_sip_media_application_logging_configuration.put_sip_media_application_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_sip_media_application_logging_configuration_request.PutSipMediaApplicationLoggingConfigurationRequest = {
            "sip_media_application_id": sip_media_application_id
        }
        if sip_media_application_logging_configuration is not None:
            input_["sip_media_application_logging_configuration"] = (
                sip_media_application_logging_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_emergency_calling_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        emergency_calling_configuration: "capo_chime_sdk_voice.types.emergency_calling_configuration.EmergencyCallingConfiguration",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.put_voice_connector_emergency_calling_configuration_response.PutVoiceConnectorEmergencyCallingConfigurationResponse":
        """<p>Updates a Voice Connector's emergency calling configuration.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            emergency_calling_configuration: <p>The configuration being updated.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_emergency_calling_configuration_request.PutVoiceConnectorEmergencyCallingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_voice_connector_emergency_calling_configuration_response.PutVoiceConnectorEmergencyCallingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_emergency_calling_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_emergency_calling_configuration.put_voice_connector_emergency_calling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_emergency_calling_configuration_request.PutVoiceConnectorEmergencyCallingConfigurationRequest = {
            "voice_connector_id": voice_connector_id,
            "emergency_calling_configuration": emergency_calling_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_external_systems_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        session_border_controller_types: Optional[
            "capo_chime_sdk_voice.types.session_border_controller_type_list.SessionBorderControllerTypeList"
        ] = None,
        contact_center_system_types: Optional[
            "capo_chime_sdk_voice.types.contact_center_system_type_list.ContactCenterSystemTypeList"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.put_voice_connector_external_systems_configuration_response.PutVoiceConnectorExternalSystemsConfigurationResponse":
        """<p>Adds an external systems configuration to a Voice Connector.</p>

        Args:
            voice_connector_id: <p>The ID of the Voice Connector for which to add the external system configuration.</p>
            session_border_controller_types: <p>The session border controllers to use.</p>
            contact_center_system_types: <p>The contact center system to use.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_external_systems_configuration_request.PutVoiceConnectorExternalSystemsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_voice_connector_external_systems_configuration_response.PutVoiceConnectorExternalSystemsConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_external_systems_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_external_systems_configuration.put_voice_connector_external_systems_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_external_systems_configuration_request.PutVoiceConnectorExternalSystemsConfigurationRequest = {
            "voice_connector_id": voice_connector_id
        }
        if session_border_controller_types is not None:
            input_["session_border_controller_types"] = session_border_controller_types
        if contact_center_system_types is not None:
            input_["contact_center_system_types"] = contact_center_system_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_logging_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        logging_configuration: "capo_chime_sdk_voice.types.logging_configuration.LoggingConfiguration",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.put_voice_connector_logging_configuration_response.PutVoiceConnectorLoggingConfigurationResponse":
        """<p>Updates a Voice Connector's logging configuration.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            logging_configuration: <p>The logging configuration being updated.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_logging_configuration_request.PutVoiceConnectorLoggingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_voice_connector_logging_configuration_response.PutVoiceConnectorLoggingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_logging_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_logging_configuration.put_voice_connector_logging_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_logging_configuration_request.PutVoiceConnectorLoggingConfigurationRequest = {
            "voice_connector_id": voice_connector_id,
            "logging_configuration": logging_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_origination(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        origination: "capo_chime_sdk_voice.types.origination.Origination",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.put_voice_connector_origination_response.PutVoiceConnectorOriginationResponse":
        """<p>Updates a Voice Connector's origination settings.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            origination: <p>The origination settings being updated.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_origination_request.PutVoiceConnectorOriginationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_voice_connector_origination_response.PutVoiceConnectorOriginationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_origination

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_origination.put_voice_connector_origination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_origination_request.PutVoiceConnectorOriginationRequest = {
            "voice_connector_id": voice_connector_id,
            "origination": origination,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_proxy(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        default_session_expiry_minutes: "capo_chime_sdk_voice.types.integer.Integer",
        phone_number_pool_countries: "capo_chime_sdk_voice.types.country_list.CountryList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        fall_back_phone_number: Optional[
            "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
        ] = None,
        disabled: Optional["capo_chime_sdk_voice.types.boolean.Boolean"] = None,
    ) -> "capo_chime_sdk_voice.types.put_voice_connector_proxy_response.PutVoiceConnectorProxyResponse":
        """<p>Puts the specified proxy configuration to the specified Amazon Chime SDK Voice Connector.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            default_session_expiry_minutes: <p>The default number of minutes allowed for proxy session.</p>
            phone_number_pool_countries: <p>The countries for proxy phone numbers to be selected from.</p>
            fall_back_phone_number: <p>The phone number to route calls to after a proxy session expires.</p>
            disabled: <p>When true, stops proxy sessions from being created on the specified Amazon Chime SDK Voice Connector.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_proxy_request.PutVoiceConnectorProxyRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_voice_connector_proxy_response.PutVoiceConnectorProxyResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_proxy

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_proxy.put_voice_connector_proxy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_proxy_request.PutVoiceConnectorProxyRequest = {
            "voice_connector_id": voice_connector_id,
            "default_session_expiry_minutes": default_session_expiry_minutes,
            "phone_number_pool_countries": phone_number_pool_countries,
        }
        if fall_back_phone_number is not None:
            input_["fall_back_phone_number"] = fall_back_phone_number
        if disabled is not None:
            input_["disabled"] = disabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_streaming_configuration(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        streaming_configuration: "capo_chime_sdk_voice.types.streaming_configuration.StreamingConfiguration",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.put_voice_connector_streaming_configuration_response.PutVoiceConnectorStreamingConfigurationResponse":
        """<p>Updates a Voice Connector's streaming configuration settings.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            streaming_configuration: <p>The streaming settings being updated.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_streaming_configuration_request.PutVoiceConnectorStreamingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_voice_connector_streaming_configuration_response.PutVoiceConnectorStreamingConfigurationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_streaming_configuration

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_streaming_configuration.put_voice_connector_streaming_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_streaming_configuration_request.PutVoiceConnectorStreamingConfigurationRequest = {
            "voice_connector_id": voice_connector_id,
            "streaming_configuration": streaming_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_termination(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        termination: "capo_chime_sdk_voice.types.termination.Termination",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.put_voice_connector_termination_response.PutVoiceConnectorTerminationResponse":
        """<p>Updates a Voice Connector's termination settings.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            termination: <p>The termination settings to be updated.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_termination_request.PutVoiceConnectorTerminationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.put_voice_connector_termination_response.PutVoiceConnectorTerminationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_termination

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_termination.put_voice_connector_termination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_termination_request.PutVoiceConnectorTerminationRequest = {
            "voice_connector_id": voice_connector_id,
            "termination": termination,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_voice_connector_termination_credentials(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        credentials: Optional[
            "capo_chime_sdk_voice.types.credential_list.CredentialList"
        ] = None,
    ) -> None:
        """<p>Updates a Voice Connector's termination credentials.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            credentials: <p>The termination credentials being updated.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.put_voice_connector_termination_credentials_request.PutVoiceConnectorTerminationCredentialsRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_termination_credentials

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.put_voice_connector_termination_credentials.put_voice_connector_termination_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.put_voice_connector_termination_credentials_request.PutVoiceConnectorTerminationCredentialsRequest = {
            "voice_connector_id": voice_connector_id
        }
        if credentials is not None:
            input_["credentials"] = credentials

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_phone_number(
        self,
        phone_number_id: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.restore_phone_number_response.RestorePhoneNumberResponse":
        """<p>Restores a deleted phone number.</p>

        Args:
            phone_number_id: <p>The ID of the phone number being restored.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.restore_phone_number_request.RestorePhoneNumberRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.restore_phone_number_response.RestorePhoneNumberResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.restore_phone_number

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.restore_phone_number.restore_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.restore_phone_number_request.RestorePhoneNumberRequest = {
            "phone_number_id": phone_number_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_available_phone_numbers(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        area_code: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        city: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        country: Optional[
            "capo_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
        ] = None,
        state: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        toll_free_prefix: Optional[
            "capo_chime_sdk_voice.types.toll_free_prefix.TollFreePrefix"
        ] = None,
        phone_number_type: Optional[
            "capo_chime_sdk_voice.types.phone_number_type.PhoneNumberType"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_voice.types.phone_number_max_results.PhoneNumberMaxResults"
        ] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
    ) -> "capo_chime_sdk_voice.types.search_available_phone_numbers_response.SearchAvailablePhoneNumbersResponse":
        """<p>Searches the provisioned phone numbers in an organization.</p>

        Args:
            area_code: <p>Confines a search to just the phone numbers associated with the specified area code.</p>
            city: <p>Confines a search to just the phone numbers associated with the specified city.</p>
            country: <p>Confines a search to just the phone numbers associated with the specified country.</p>
            state: <p>Confines a search to just the phone numbers associated with the specified state.</p>
            toll_free_prefix: <p>Confines a search to just the phone numbers associated with the specified toll-free prefix.</p>
            phone_number_type: <p>Confines a search to just the phone numbers associated with the specified phone number type, either <b>local</b> or <b>toll-free</b>.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token used to return the next page of results.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.search_available_phone_numbers_request.SearchAvailablePhoneNumbersRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.search_available_phone_numbers_response.SearchAvailablePhoneNumbersResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.search_available_phone_numbers

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.search_available_phone_numbers.search_available_phone_numbers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.search_available_phone_numbers_request.SearchAvailablePhoneNumbersRequest = {}
        if area_code is not None:
            input_["area_code"] = area_code
        if city is not None:
            input_["city"] = city
        if country is not None:
            input_["country"] = country
        if state is not None:
            input_["state"] = state
        if toll_free_prefix is not None:
            input_["toll_free_prefix"] = toll_free_prefix
        if phone_number_type is not None:
            input_["phone_number_type"] = phone_number_type
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

    def iter_search_available_phone_numbers(
        self,
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        area_code: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        city: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        country: Optional[
            "capo_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
        ] = None,
        state: Optional["capo_chime_sdk_voice.types.string.String"] = None,
        toll_free_prefix: Optional[
            "capo_chime_sdk_voice.types.toll_free_prefix.TollFreePrefix"
        ] = None,
        phone_number_type: Optional[
            "capo_chime_sdk_voice.types.phone_number_type.PhoneNumberType"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_voice.types.phone_number_max_results.PhoneNumberMaxResults"
        ] = None,
        next_token: Optional["capo_chime_sdk_voice.types.string.String"] = None,
    ) -> "Iterator[capo_chime_sdk_voice.types.search_available_phone_numbers_response.SearchAvailablePhoneNumbersResponse]":
        _token = next_token
        while True:
            _response = self.search_available_phone_numbers(
                config_overrides=config_overrides,
                area_code=area_code,
                city=city,
                country=country,
                state=state,
                toll_free_prefix=toll_free_prefix,
                phone_number_type=phone_number_type,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_speaker_search_task(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        transaction_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        voice_profile_domain_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        client_request_token: Optional[
            "capo_chime_sdk_voice.types.client_request_id.ClientRequestId"
        ] = None,
        call_leg: Optional[
            "capo_chime_sdk_voice.types.call_leg_type.CallLegType"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.start_speaker_search_task_response.StartSpeakerSearchTaskResponse":
        """<p>Starts a speaker search task.</p> <important> <p>Before starting any speaker search tasks, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the <a href="https://aws.amazon.com/service-terms/">AWS service terms</a> for the Amazon Chime SDK.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            transaction_id: <p>The transaction ID of the call being analyzed.</p>
            voice_profile_domain_id: <p>The ID of the voice profile domain that will store the voice profile.</p>
            client_request_token: <p>The unique identifier for the client request. Use a different token for different speaker search tasks.</p>
            call_leg: <p>Specifies which call leg to stream for speaker search.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.gone_exception.GoneException: <p>Access to the target resource is no longer available at the origin server. This condition is likely to be permanent.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.unprocessable_entity_exception.UnprocessableEntityException: <p>A well-formed request couldn't be followed due to semantic errors.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.start_speaker_search_task_request.StartSpeakerSearchTaskRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.start_speaker_search_task_response.StartSpeakerSearchTaskResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.start_speaker_search_task

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.start_speaker_search_task.start_speaker_search_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.start_speaker_search_task_request.StartSpeakerSearchTaskRequest = {
            "voice_connector_id": voice_connector_id,
            "transaction_id": transaction_id,
            "voice_profile_domain_id": voice_profile_domain_id,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if call_leg is not None:
            input_["call_leg"] = call_leg

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_voice_tone_analysis_task(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        transaction_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        language_code: "capo_chime_sdk_voice.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        client_request_token: Optional[
            "capo_chime_sdk_voice.types.client_request_id.ClientRequestId"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.start_voice_tone_analysis_task_response.StartVoiceToneAnalysisTaskResponse":
        """<p>Starts a voice tone analysis task. For more information about voice tone analysis, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/pstn-voice-analytics.html">Using Amazon Chime SDK voice analytics</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p> <important> <p>Before starting any voice tone analysis tasks, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the <a href="https://aws.amazon.com/service-terms/">AWS service terms</a> for the Amazon Chime SDK.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            transaction_id: <p>The transaction ID.</p>
            language_code: <p>The language code.</p>
            client_request_token: <p>The unique identifier for the client request. Use a different token for different voice tone analysis tasks.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.gone_exception.GoneException: <p>Access to the target resource is no longer available at the origin server. This condition is likely to be permanent.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.unprocessable_entity_exception.UnprocessableEntityException: <p>A well-formed request couldn't be followed due to semantic errors.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.start_voice_tone_analysis_task_request.StartVoiceToneAnalysisTaskRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.start_voice_tone_analysis_task_response.StartVoiceToneAnalysisTaskResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.start_voice_tone_analysis_task

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.start_voice_tone_analysis_task.start_voice_tone_analysis_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.start_voice_tone_analysis_task_request.StartVoiceToneAnalysisTaskRequest = {
            "voice_connector_id": voice_connector_id,
            "transaction_id": transaction_id,
            "language_code": language_code,
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_speaker_search_task(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        speaker_search_task_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Stops a speaker search task.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            speaker_search_task_id: <p>The speaker search task ID.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.unprocessable_entity_exception.UnprocessableEntityException: <p>A well-formed request couldn't be followed due to semantic errors.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.stop_speaker_search_task_request.StopSpeakerSearchTaskRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.stop_speaker_search_task

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.stop_speaker_search_task.stop_speaker_search_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.stop_speaker_search_task_request.StopSpeakerSearchTaskRequest = {
            "voice_connector_id": voice_connector_id,
            "speaker_search_task_id": speaker_search_task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_voice_tone_analysis_task(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        voice_tone_analysis_task_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Stops a voice tone analysis task.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            voice_tone_analysis_task_id: <p>The ID of the voice tone analysis task.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.unprocessable_entity_exception.UnprocessableEntityException: <p>A well-formed request couldn't be followed due to semantic errors.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.stop_voice_tone_analysis_task_request.StopVoiceToneAnalysisTaskRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.stop_voice_tone_analysis_task

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.stop_voice_tone_analysis_task.stop_voice_tone_analysis_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.stop_voice_tone_analysis_task_request.StopVoiceToneAnalysisTaskRequest = {
            "voice_connector_id": voice_connector_id,
            "voice_tone_analysis_task_id": voice_tone_analysis_task_id,
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
        resource_arn: "capo_chime_sdk_voice.types.arn.Arn",
        tags: "capo_chime_sdk_voice.types.tag_list.TagList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Adds a tag to the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource being tagged. </p>
            tags: <p>A list of the tags being added to the resource.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.tag_resource

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_chime_sdk_voice.types.arn.Arn",
        tag_keys: "capo_chime_sdk_voice.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource having its tags removed.</p>
            tag_keys: <p>The keys of the tags being removed from the resource.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.untag_resource

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.untag_resource_request.UntagResourceRequest = {
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

    def update_global_settings(
        self,
        voice_connector: "capo_chime_sdk_voice.types.voice_connector_settings.VoiceConnectorSettings",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Updates global settings for the Amazon Chime SDK Voice Connectors in an AWS account.</p>

        Args:
            voice_connector: <p>The Voice Connector settings.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_global_settings_request.UpdateGlobalSettingsRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_global_settings

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_global_settings.update_global_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_global_settings_request.UpdateGlobalSettingsRequest = {
            "voice_connector": voice_connector
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_phone_number(
        self,
        phone_number_id: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        product_type: Optional[
            "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
        ] = None,
        calling_name: Optional[
            "capo_chime_sdk_voice.types.calling_name.CallingName"
        ] = None,
        name: Optional[
            "capo_chime_sdk_voice.types.phone_number_name.PhoneNumberName"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.update_phone_number_response.UpdatePhoneNumberResponse":
        """<p>Updates phone number details, such as product type, calling name, or phone number name for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type, calling name, or phone number name in one action.</p> <p>For numbers outside the U.S., you must use the Amazon Chime SDK SIP Media Application Dial-In product type.</p> <p>Updates to outbound calling names can take 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.</p>

        Args:
            phone_number_id: <p>The phone number ID.</p>
            product_type: <p>The product type.</p>
            calling_name: <p>The outbound calling name associated with the phone number.</p>
            name: <p>Specifies the updated name assigned to one or more phone numbers.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_phone_number_request.UpdatePhoneNumberRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_phone_number_response.UpdatePhoneNumberResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_phone_number

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_phone_number.update_phone_number(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_phone_number_request.UpdatePhoneNumberRequest = {
            "phone_number_id": phone_number_id
        }
        if product_type is not None:
            input_["product_type"] = product_type
        if calling_name is not None:
            input_["calling_name"] = calling_name
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_phone_number_settings(
        self,
        calling_name: "capo_chime_sdk_voice.types.calling_name.CallingName",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> None:
        """<p>Updates the phone number settings for the administrator's AWS account, such as the default outbound calling name. You can update the default outbound calling name once every seven days. Outbound calling names can take up to 72 hours to update.</p>

        Args:
            calling_name: <p>The default outbound calling name for the account.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_phone_number_settings_request.UpdatePhoneNumberSettingsRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_phone_number_settings

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_phone_number_settings.update_phone_number_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_phone_number_settings_request.UpdatePhoneNumberSettingsRequest = {
            "calling_name": calling_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_proxy_session(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        proxy_session_id: "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128",
        capabilities: "capo_chime_sdk_voice.types.capability_list.CapabilityList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        expiry_minutes: Optional[
            "capo_chime_sdk_voice.types.positive_integer.PositiveInteger"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.update_proxy_session_response.UpdateProxySessionResponse":
        """<p>Updates the specified proxy session details, such as voice or SMS capabilities.</p> <important> <p>End of support notice: On April 7, 2026, AWS will end support for Amazon Chime SDK proxy sessions.</p> </important>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            proxy_session_id: <p>The proxy session ID.</p>
            capabilities: <p>The proxy session capabilities.</p>
            expiry_minutes: <p>The number of minutes allowed for the proxy session.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_proxy_session_request.UpdateProxySessionRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_proxy_session_response.UpdateProxySessionResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_proxy_session

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_proxy_session.update_proxy_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_proxy_session_request.UpdateProxySessionRequest = {
            "voice_connector_id": voice_connector_id,
            "proxy_session_id": proxy_session_id,
            "capabilities": capabilities,
        }
        if expiry_minutes is not None:
            input_["expiry_minutes"] = expiry_minutes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sip_media_application(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName"
        ] = None,
        endpoints: Optional[
            "capo_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.update_sip_media_application_response.UpdateSipMediaApplicationResponse":
        """<p>Updates the details of the specified SIP media application.</p>

        Args:
            sip_media_application_id: <p>The SIP media application ID.</p>
            name: <p>The new name for the specified SIP media application.</p>
            endpoints: <p>The new set of endpoints for the specified SIP media application.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_sip_media_application_request.UpdateSipMediaApplicationRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_sip_media_application_response.UpdateSipMediaApplicationResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_sip_media_application

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_sip_media_application.update_sip_media_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_sip_media_application_request.UpdateSipMediaApplicationRequest = {
            "sip_media_application_id": sip_media_application_id
        }
        if name is not None:
            input_["name"] = name
        if endpoints is not None:
            input_["endpoints"] = endpoints

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sip_media_application_call(
        self,
        sip_media_application_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        transaction_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        arguments: "capo_chime_sdk_voice.types.sma_update_call_arguments_map.SMAUpdateCallArgumentsMap",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.update_sip_media_application_call_response.UpdateSipMediaApplicationCallResponse":
        """<p>Invokes the AWS Lambda function associated with the SIP media application and transaction ID in an update request. The Lambda function can then return a new set of actions.</p>

        Args:
            sip_media_application_id: <p>The ID of the SIP media application handling the call.</p>
            transaction_id: <p>The ID of the call transaction.</p>
            arguments: <p>Arguments made available to the Lambda function as part of the <code>CALL_UPDATE_REQUESTED</code> event. Can contain 0-20 key-value pairs.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_sip_media_application_call_request.UpdateSipMediaApplicationCallRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_sip_media_application_call_response.UpdateSipMediaApplicationCallResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_sip_media_application_call

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_sip_media_application_call.update_sip_media_application_call(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_sip_media_application_call_request.UpdateSipMediaApplicationCallRequest = {
            "sip_media_application_id": sip_media_application_id,
            "transaction_id": transaction_id,
            "arguments": arguments,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sip_rule(
        self,
        sip_rule_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        name: "capo_chime_sdk_voice.types.sip_rule_name.SipRuleName",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        disabled: Optional[
            "capo_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
        ] = None,
        target_applications: Optional[
            "capo_chime_sdk_voice.types.sip_rule_target_application_list.SipRuleTargetApplicationList"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.update_sip_rule_response.UpdateSipRuleResponse":
        """<p>Updates the details of the specified SIP rule.</p>

        Args:
            sip_rule_id: <p>The SIP rule ID.</p>
            name: <p>The new name for the specified SIP rule.</p>
            disabled: <p>The new value that indicates whether the rule is disabled.</p>
            target_applications: <p>The new list of target applications.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_sip_rule_request.UpdateSipRuleRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_sip_rule_response.UpdateSipRuleResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_sip_rule

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_sip_rule.update_sip_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_sip_rule_request.UpdateSipRuleRequest = {
            "sip_rule_id": sip_rule_id,
            "name": name,
        }
        if disabled is not None:
            input_["disabled"] = disabled
        if target_applications is not None:
            input_["target_applications"] = target_applications

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_voice_connector(
        self,
        voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId",
        name: "capo_chime_sdk_voice.types.voice_connector_name.VoiceConnectorName",
        require_encryption: "capo_chime_sdk_voice.types.boolean.Boolean",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.update_voice_connector_response.UpdateVoiceConnectorResponse":
        """<p>Updates the details for the specified Amazon Chime SDK Voice Connector.</p>

        Args:
            voice_connector_id: <p>The Voice Connector ID.</p>
            name: <p>The name of the Voice Connector.</p>
            require_encryption: <p>When enabled, requires encryption for the Voice Connector.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_voice_connector_request.UpdateVoiceConnectorRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_voice_connector_response.UpdateVoiceConnectorResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_connector

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_connector.update_voice_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_voice_connector_request.UpdateVoiceConnectorRequest = {
            "voice_connector_id": voice_connector_id,
            "name": name,
            "require_encryption": require_encryption,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_voice_connector_group(
        self,
        voice_connector_group_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        name: "capo_chime_sdk_voice.types.voice_connector_group_name.VoiceConnectorGroupName",
        voice_connector_items: "capo_chime_sdk_voice.types.voice_connector_item_list.VoiceConnectorItemList",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        call_distribution_type: Optional[
            "capo_chime_sdk_voice.types.call_distribution_type.CallDistributionType"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.update_voice_connector_group_response.UpdateVoiceConnectorGroupResponse":
        """<p>Updates the settings for the specified Amazon Chime SDK Voice Connector group.</p>

        Args:
            voice_connector_group_id: <p>The Voice Connector ID.</p>
            name: <p>The name of the Voice Connector group.</p>
            voice_connector_items: <p>The <code>VoiceConnectorItems</code> to associate with the Voice Connector group.</p>

        Raises:
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_voice_connector_group_request.UpdateVoiceConnectorGroupRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_voice_connector_group_response.UpdateVoiceConnectorGroupResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_connector_group

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_connector_group.update_voice_connector_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_voice_connector_group_request.UpdateVoiceConnectorGroupRequest = {
            "voice_connector_group_id": voice_connector_group_id,
            "name": name,
            "voice_connector_items": voice_connector_items,
        }
        if call_distribution_type is not None:
            input_["call_distribution_type"] = call_distribution_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_voice_profile(
        self,
        voice_profile_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        speaker_search_task_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.update_voice_profile_response.UpdateVoiceProfileResponse":
        """<p>Updates the specified voice profile’s voice print and refreshes its expiration timestamp.</p> <important> <p>As a condition of using this feature, you acknowledge that the collection, use, storage, and retention of your caller’s biometric identifiers and biometric information (“biometric data”) in the form of a digital voiceprint requires the caller’s informed consent via a written release. Such consent is required under various state laws, including biometrics laws in Illinois, Texas, Washington and other state privacy laws.</p> <p>You must provide a written release to each caller through a process that clearly reflects each caller’s informed consent before using Amazon Chime SDK Voice Insights service, as required under the terms of your agreement with AWS governing your use of the service.</p> </important>

        Args:
            voice_profile_id: <p>The profile ID.</p>
            speaker_search_task_id: <p>The ID of the speaker search task.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.conflict_exception.ConflictException: <p>Multiple instances of the same request were made simultaneously.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.gone_exception.GoneException: <p>Access to the target resource is no longer available at the origin server. This condition is likely to be permanent.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_voice_profile_request.UpdateVoiceProfileRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_voice_profile_response.UpdateVoiceProfileResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_profile

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_profile.update_voice_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_voice_profile_request.UpdateVoiceProfileRequest = {
            "voice_profile_id": voice_profile_id,
            "speaker_search_task_id": speaker_search_task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_voice_profile_domain(
        self,
        voice_profile_domain_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_voice.types.voice_profile_domain_name.VoiceProfileDomainName"
        ] = None,
        description: Optional[
            "capo_chime_sdk_voice.types.voice_profile_domain_description.VoiceProfileDomainDescription"
        ] = None,
    ) -> "capo_chime_sdk_voice.types.update_voice_profile_domain_response.UpdateVoiceProfileDomainResponse":
        """<p>Updates the settings for the specified voice profile domain.</p>

        Args:
            voice_profile_domain_id: <p>The domain ID.</p>
            name: <p>The name of the voice profile domain.</p>
            description: <p>The description of the voice profile domain.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.update_voice_profile_domain_request.UpdateVoiceProfileDomainRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.update_voice_profile_domain_response.UpdateVoiceProfileDomainResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_profile_domain

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.update_voice_profile_domain.update_voice_profile_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.update_voice_profile_domain_request.UpdateVoiceProfileDomainRequest = {
            "voice_profile_domain_id": voice_profile_domain_id
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

    def validate_e911_address(
        self,
        aws_account_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString",
        street_number: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        street_info: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        city: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        state: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        country: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        postal_code: "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        *,
        config_overrides: Optional[ChimeSDKVoiceClientConfig] = None,
    ) -> "capo_chime_sdk_voice.types.validate_e911_address_response.ValidateE911AddressResponse":
        """<p>Validates an address to be used for 911 calls made with Amazon Chime SDK Voice Connectors. You can use validated addresses in a Presence Information Data Format Location Object file that you include in SIP requests. That helps ensure that addresses are routed to the appropriate Public Safety Answering Point.</p>

        Args:
            aws_account_id: <p>The AWS account ID.</p>
            street_number: <p>The address street number, such as <code>200</code> or <code>2121</code>.</p>
            street_info: <p>The address street information, such as <code>8th Avenue</code>.</p>
            city: <p>The address city, such as <code>Portland</code>.</p>
            state: <p>The address state, such as <code>ME</code>.</p>
            country: <p>The country in the address being validated as two-letter country code in ISO 3166-1 alpha-2 format, such as <code>US</code>. For more information, see <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> in Wikipedia.</p>
            postal_code: <p>The dress postal code, such <code>04352</code>.</p>

        Raises:
            capo_chime_sdk_voice.errors.access_denied_exception.AccessDeniedException: <p>You don't have the permissions needed to run this action.</p>
            capo_chime_sdk_voice.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_voice.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_voice.errors.not_found_exception.NotFoundException: <p>The requested resource couldn't be found.</p>
            capo_chime_sdk_voice.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_voice.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_voice.errors.throttled_client_exception.ThrottledClientException: <p>The number of customer requests exceeds the request rate limit.</p>
            capo_chime_sdk_voice.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client isn't authorized to request a resource.</p>
            capo_chime_sdk_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_voice.types.validate_e911_address_request.ValidateE911AddressRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_voice.types.validate_e911_address_response.ValidateE911AddressResponse"
        ]:
            import capo_chime_sdk_voice._operations.chime_sdk_telephony_service.validate_e911_address

            output, http_response = (
                capo_chime_sdk_voice._operations.chime_sdk_telephony_service.validate_e911_address.validate_e911_address(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_voice.types.validate_e911_address_request.ValidateE911AddressRequest = {
            "aws_account_id": aws_account_id,
            "street_number": street_number,
            "street_info": street_info,
            "city": city,
            "state": state,
            "country": country,
            "postal_code": postal_code,
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
