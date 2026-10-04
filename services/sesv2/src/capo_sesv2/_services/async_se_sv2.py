"""Generated from Smithy shape ``com.amazonaws.sesv2#SimpleEmailService_v2``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sesv2._auth._signers
import capo_sesv2._auth._sigv4
from capo_sesv2._auth._identity import Credentials
from capo_sesv2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sesv2._auth._zapros_handler import AuthMiddleware
from capo_sesv2._pagination import resolve_path as _resolve_path
from capo_sesv2._services._aws_config import aaws_config
from capo_sesv2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sesv2.types.additional_contact_email_addresses
    import capo_sesv2.types.amazon_resource_name
    import capo_sesv2.types.archive_arn
    import capo_sesv2.types.archiving_options
    import capo_sesv2.types.associate_email_identity_certificate_request
    import capo_sesv2.types.associate_email_identity_certificate_response
    import capo_sesv2.types.attributes_data
    import capo_sesv2.types.batch_get_metric_data_queries
    import capo_sesv2.types.batch_get_metric_data_request
    import capo_sesv2.types.batch_get_metric_data_response
    import capo_sesv2.types.behavior_on_mx_failure
    import capo_sesv2.types.blacklist_item_names
    import capo_sesv2.types.bulk_email_content
    import capo_sesv2.types.bulk_email_entry_list
    import capo_sesv2.types.campaign_id
    import capo_sesv2.types.cancel_export_job_request
    import capo_sesv2.types.cancel_export_job_response
    import capo_sesv2.types.certificate_arn
    import capo_sesv2.types.configuration_overrides
    import capo_sesv2.types.configuration_set_filter
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.contact_language
    import capo_sesv2.types.contact_list_name
    import capo_sesv2.types.create_configuration_set_event_destination_request
    import capo_sesv2.types.create_configuration_set_event_destination_response
    import capo_sesv2.types.create_configuration_set_request
    import capo_sesv2.types.create_configuration_set_response
    import capo_sesv2.types.create_contact_list_request
    import capo_sesv2.types.create_contact_list_response
    import capo_sesv2.types.create_contact_request
    import capo_sesv2.types.create_contact_response
    import capo_sesv2.types.create_custom_verification_email_template_request
    import capo_sesv2.types.create_custom_verification_email_template_response
    import capo_sesv2.types.create_dedicated_ip_pool_request
    import capo_sesv2.types.create_dedicated_ip_pool_response
    import capo_sesv2.types.create_deliverability_test_report_request
    import capo_sesv2.types.create_deliverability_test_report_response
    import capo_sesv2.types.create_email_identity_policy_request
    import capo_sesv2.types.create_email_identity_policy_response
    import capo_sesv2.types.create_email_identity_request
    import capo_sesv2.types.create_email_identity_response
    import capo_sesv2.types.create_email_template_request
    import capo_sesv2.types.create_email_template_response
    import capo_sesv2.types.create_export_job_request
    import capo_sesv2.types.create_export_job_response
    import capo_sesv2.types.create_import_job_request
    import capo_sesv2.types.create_import_job_response
    import capo_sesv2.types.create_multi_region_endpoint_request
    import capo_sesv2.types.create_multi_region_endpoint_response
    import capo_sesv2.types.create_tenant_request
    import capo_sesv2.types.create_tenant_resource_association_request
    import capo_sesv2.types.create_tenant_resource_association_response
    import capo_sesv2.types.create_tenant_response
    import capo_sesv2.types.custom_redirect_domain
    import capo_sesv2.types.delete_configuration_set_event_destination_request
    import capo_sesv2.types.delete_configuration_set_event_destination_response
    import capo_sesv2.types.delete_configuration_set_request
    import capo_sesv2.types.delete_configuration_set_response
    import capo_sesv2.types.delete_contact_list_request
    import capo_sesv2.types.delete_contact_list_response
    import capo_sesv2.types.delete_contact_request
    import capo_sesv2.types.delete_contact_response
    import capo_sesv2.types.delete_custom_verification_email_template_request
    import capo_sesv2.types.delete_custom_verification_email_template_response
    import capo_sesv2.types.delete_dedicated_ip_pool_request
    import capo_sesv2.types.delete_dedicated_ip_pool_response
    import capo_sesv2.types.delete_email_identity_policy_request
    import capo_sesv2.types.delete_email_identity_policy_response
    import capo_sesv2.types.delete_email_identity_request
    import capo_sesv2.types.delete_email_identity_response
    import capo_sesv2.types.delete_email_template_request
    import capo_sesv2.types.delete_email_template_response
    import capo_sesv2.types.delete_multi_region_endpoint_request
    import capo_sesv2.types.delete_multi_region_endpoint_response
    import capo_sesv2.types.delete_suppressed_destination_request
    import capo_sesv2.types.delete_suppressed_destination_response
    import capo_sesv2.types.delete_tenant_request
    import capo_sesv2.types.delete_tenant_resource_association_request
    import capo_sesv2.types.delete_tenant_resource_association_response
    import capo_sesv2.types.delete_tenant_response
    import capo_sesv2.types.delivery_options
    import capo_sesv2.types.description
    import capo_sesv2.types.destination
    import capo_sesv2.types.details
    import capo_sesv2.types.disassociate_email_identity_certificate_request
    import capo_sesv2.types.disassociate_email_identity_certificate_response
    import capo_sesv2.types.dkim_signing_attributes
    import capo_sesv2.types.dkim_signing_attributes_origin
    import capo_sesv2.types.domain
    import capo_sesv2.types.domain_deliverability_tracking_options
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_address_list
    import capo_sesv2.types.email_content
    import capo_sesv2.types.email_template_content
    import capo_sesv2.types.email_template_data
    import capo_sesv2.types.email_template_name
    import capo_sesv2.types.email_template_subject
    import capo_sesv2.types.enabled
    import capo_sesv2.types.enabled_wrapper
    import capo_sesv2.types.endpoint_id
    import capo_sesv2.types.endpoint_name
    import capo_sesv2.types.event_destination_definition
    import capo_sesv2.types.event_destination_name
    import capo_sesv2.types.export_data_source
    import capo_sesv2.types.export_destination
    import capo_sesv2.types.export_source_type
    import capo_sesv2.types.failure_redirection_url
    import capo_sesv2.types.get_account_request
    import capo_sesv2.types.get_account_response
    import capo_sesv2.types.get_blacklist_reports_request
    import capo_sesv2.types.get_blacklist_reports_response
    import capo_sesv2.types.get_configuration_set_event_destinations_request
    import capo_sesv2.types.get_configuration_set_event_destinations_response
    import capo_sesv2.types.get_configuration_set_request
    import capo_sesv2.types.get_configuration_set_response
    import capo_sesv2.types.get_contact_list_request
    import capo_sesv2.types.get_contact_list_response
    import capo_sesv2.types.get_contact_request
    import capo_sesv2.types.get_contact_response
    import capo_sesv2.types.get_custom_verification_email_template_request
    import capo_sesv2.types.get_custom_verification_email_template_response
    import capo_sesv2.types.get_dedicated_ip_pool_request
    import capo_sesv2.types.get_dedicated_ip_pool_response
    import capo_sesv2.types.get_dedicated_ip_request
    import capo_sesv2.types.get_dedicated_ip_response
    import capo_sesv2.types.get_dedicated_ips_request
    import capo_sesv2.types.get_dedicated_ips_response
    import capo_sesv2.types.get_deliverability_dashboard_options_request
    import capo_sesv2.types.get_deliverability_dashboard_options_response
    import capo_sesv2.types.get_deliverability_test_report_request
    import capo_sesv2.types.get_deliverability_test_report_response
    import capo_sesv2.types.get_domain_deliverability_campaign_request
    import capo_sesv2.types.get_domain_deliverability_campaign_response
    import capo_sesv2.types.get_domain_statistics_report_request
    import capo_sesv2.types.get_domain_statistics_report_response
    import capo_sesv2.types.get_email_address_insights_request
    import capo_sesv2.types.get_email_address_insights_response
    import capo_sesv2.types.get_email_identity_policies_request
    import capo_sesv2.types.get_email_identity_policies_response
    import capo_sesv2.types.get_email_identity_request
    import capo_sesv2.types.get_email_identity_response
    import capo_sesv2.types.get_email_template_request
    import capo_sesv2.types.get_email_template_response
    import capo_sesv2.types.get_export_job_request
    import capo_sesv2.types.get_export_job_response
    import capo_sesv2.types.get_import_job_request
    import capo_sesv2.types.get_import_job_response
    import capo_sesv2.types.get_message_insights_request
    import capo_sesv2.types.get_message_insights_response
    import capo_sesv2.types.get_multi_region_endpoint_request
    import capo_sesv2.types.get_multi_region_endpoint_response
    import capo_sesv2.types.get_reputation_entity_request
    import capo_sesv2.types.get_reputation_entity_response
    import capo_sesv2.types.get_suppressed_destination_request
    import capo_sesv2.types.get_suppressed_destination_response
    import capo_sesv2.types.get_tenant_request
    import capo_sesv2.types.get_tenant_response
    import capo_sesv2.types.https_policy
    import capo_sesv2.types.identity
    import capo_sesv2.types.identity_certificate
    import capo_sesv2.types.identity_filter
    import capo_sesv2.types.import_data_source
    import capo_sesv2.types.import_destination
    import capo_sesv2.types.import_destination_type
    import capo_sesv2.types.ip
    import capo_sesv2.types.job_id
    import capo_sesv2.types.job_status
    import capo_sesv2.types.list_configuration_sets_request
    import capo_sesv2.types.list_configuration_sets_response
    import capo_sesv2.types.list_contact_lists_request
    import capo_sesv2.types.list_contact_lists_response
    import capo_sesv2.types.list_contacts_filter
    import capo_sesv2.types.list_contacts_request
    import capo_sesv2.types.list_contacts_response
    import capo_sesv2.types.list_custom_verification_email_templates_request
    import capo_sesv2.types.list_custom_verification_email_templates_response
    import capo_sesv2.types.list_dedicated_ip_pools_request
    import capo_sesv2.types.list_dedicated_ip_pools_response
    import capo_sesv2.types.list_deliverability_test_reports_request
    import capo_sesv2.types.list_deliverability_test_reports_response
    import capo_sesv2.types.list_domain_deliverability_campaigns_request
    import capo_sesv2.types.list_domain_deliverability_campaigns_response
    import capo_sesv2.types.list_email_identities_request
    import capo_sesv2.types.list_email_identities_response
    import capo_sesv2.types.list_email_identity_certificates_request
    import capo_sesv2.types.list_email_identity_certificates_response
    import capo_sesv2.types.list_email_templates_request
    import capo_sesv2.types.list_email_templates_response
    import capo_sesv2.types.list_export_jobs_request
    import capo_sesv2.types.list_export_jobs_response
    import capo_sesv2.types.list_import_jobs_request
    import capo_sesv2.types.list_import_jobs_response
    import capo_sesv2.types.list_management_options
    import capo_sesv2.types.list_multi_region_endpoints_request
    import capo_sesv2.types.list_multi_region_endpoints_response
    import capo_sesv2.types.list_recommendations_filter
    import capo_sesv2.types.list_recommendations_request
    import capo_sesv2.types.list_recommendations_response
    import capo_sesv2.types.list_reputation_entities_request
    import capo_sesv2.types.list_reputation_entities_response
    import capo_sesv2.types.list_resource_tenants_request
    import capo_sesv2.types.list_resource_tenants_response
    import capo_sesv2.types.list_suppressed_destinations_request
    import capo_sesv2.types.list_suppressed_destinations_response
    import capo_sesv2.types.list_tags_for_resource_request
    import capo_sesv2.types.list_tags_for_resource_response
    import capo_sesv2.types.list_tenant_resources_filter
    import capo_sesv2.types.list_tenant_resources_request
    import capo_sesv2.types.list_tenant_resources_response
    import capo_sesv2.types.list_tenants_filter
    import capo_sesv2.types.list_tenants_request
    import capo_sesv2.types.list_tenants_response
    import capo_sesv2.types.mail_from_domain_name
    import capo_sesv2.types.mail_type
    import capo_sesv2.types.max_delivery_seconds
    import capo_sesv2.types.max_items
    import capo_sesv2.types.message_security_options
    import capo_sesv2.types.message_tag_list
    import capo_sesv2.types.multi_region_endpoint
    import capo_sesv2.types.next_token
    import capo_sesv2.types.next_token_v2
    import capo_sesv2.types.outbound_message_id
    import capo_sesv2.types.page_size_v2
    import capo_sesv2.types.percentage100_wrapper
    import capo_sesv2.types.policy
    import capo_sesv2.types.policy_name
    import capo_sesv2.types.pool_name
    import capo_sesv2.types.pricing_plan
    import capo_sesv2.types.put_account_dedicated_ip_warmup_attributes_request
    import capo_sesv2.types.put_account_dedicated_ip_warmup_attributes_response
    import capo_sesv2.types.put_account_details_request
    import capo_sesv2.types.put_account_details_response
    import capo_sesv2.types.put_account_pricing_attributes_request
    import capo_sesv2.types.put_account_pricing_attributes_response
    import capo_sesv2.types.put_account_sending_attributes_request
    import capo_sesv2.types.put_account_sending_attributes_response
    import capo_sesv2.types.put_account_suppression_attributes_request
    import capo_sesv2.types.put_account_suppression_attributes_response
    import capo_sesv2.types.put_account_vdm_attributes_request
    import capo_sesv2.types.put_account_vdm_attributes_response
    import capo_sesv2.types.put_configuration_set_archiving_options_request
    import capo_sesv2.types.put_configuration_set_archiving_options_response
    import capo_sesv2.types.put_configuration_set_delivery_options_request
    import capo_sesv2.types.put_configuration_set_delivery_options_response
    import capo_sesv2.types.put_configuration_set_reputation_options_request
    import capo_sesv2.types.put_configuration_set_reputation_options_response
    import capo_sesv2.types.put_configuration_set_sending_options_request
    import capo_sesv2.types.put_configuration_set_sending_options_response
    import capo_sesv2.types.put_configuration_set_suppression_options_request
    import capo_sesv2.types.put_configuration_set_suppression_options_response
    import capo_sesv2.types.put_configuration_set_tracking_options_request
    import capo_sesv2.types.put_configuration_set_tracking_options_response
    import capo_sesv2.types.put_configuration_set_vdm_options_request
    import capo_sesv2.types.put_configuration_set_vdm_options_response
    import capo_sesv2.types.put_dedicated_ip_in_pool_request
    import capo_sesv2.types.put_dedicated_ip_in_pool_response
    import capo_sesv2.types.put_dedicated_ip_pool_scaling_attributes_request
    import capo_sesv2.types.put_dedicated_ip_pool_scaling_attributes_response
    import capo_sesv2.types.put_dedicated_ip_warmup_attributes_request
    import capo_sesv2.types.put_dedicated_ip_warmup_attributes_response
    import capo_sesv2.types.put_deliverability_dashboard_option_request
    import capo_sesv2.types.put_deliverability_dashboard_option_response
    import capo_sesv2.types.put_email_identity_configuration_set_attributes_request
    import capo_sesv2.types.put_email_identity_configuration_set_attributes_response
    import capo_sesv2.types.put_email_identity_dkim_attributes_request
    import capo_sesv2.types.put_email_identity_dkim_attributes_response
    import capo_sesv2.types.put_email_identity_dkim_signing_attributes_request
    import capo_sesv2.types.put_email_identity_dkim_signing_attributes_response
    import capo_sesv2.types.put_email_identity_feedback_attributes_request
    import capo_sesv2.types.put_email_identity_feedback_attributes_response
    import capo_sesv2.types.put_email_identity_mail_from_attributes_request
    import capo_sesv2.types.put_email_identity_mail_from_attributes_response
    import capo_sesv2.types.put_suppressed_destination_request
    import capo_sesv2.types.put_suppressed_destination_response
    import capo_sesv2.types.put_tenant_suppression_attributes_request
    import capo_sesv2.types.put_tenant_suppression_attributes_response
    import capo_sesv2.types.report_id
    import capo_sesv2.types.report_name
    import capo_sesv2.types.reputation_entity
    import capo_sesv2.types.reputation_entity_filter
    import capo_sesv2.types.reputation_entity_reference
    import capo_sesv2.types.reputation_entity_type
    import capo_sesv2.types.reputation_options
    import capo_sesv2.types.resource_tenant_metadata
    import capo_sesv2.types.scaling_mode
    import capo_sesv2.types.send_bulk_email_request
    import capo_sesv2.types.send_bulk_email_response
    import capo_sesv2.types.send_custom_verification_email_request
    import capo_sesv2.types.send_custom_verification_email_response
    import capo_sesv2.types.send_email_request
    import capo_sesv2.types.send_email_response
    import capo_sesv2.types.sending_options
    import capo_sesv2.types.sending_pool_name
    import capo_sesv2.types.sending_status
    import capo_sesv2.types.success_redirection_url
    import capo_sesv2.types.suppression_list_reason
    import capo_sesv2.types.suppression_list_reasons
    import capo_sesv2.types.suppression_list_scope
    import capo_sesv2.types.suppression_options
    import capo_sesv2.types.suppression_validation_attributes
    import capo_sesv2.types.suppression_validation_options
    import capo_sesv2.types.tag_key_list
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.tag_resource_request
    import capo_sesv2.types.tag_resource_response
    import capo_sesv2.types.template_content
    import capo_sesv2.types.tenant_info
    import capo_sesv2.types.tenant_name
    import capo_sesv2.types.tenant_resource
    import capo_sesv2.types.tenant_suppression_attributes
    import capo_sesv2.types.test_render_email_template_request
    import capo_sesv2.types.test_render_email_template_response
    import capo_sesv2.types.timestamp
    import capo_sesv2.types.tls_policy
    import capo_sesv2.types.topic_preference_list
    import capo_sesv2.types.topics
    import capo_sesv2.types.tracking_options
    import capo_sesv2.types.unsubscribe_all
    import capo_sesv2.types.untag_resource_request
    import capo_sesv2.types.untag_resource_response
    import capo_sesv2.types.update_configuration_set_event_destination_request
    import capo_sesv2.types.update_configuration_set_event_destination_response
    import capo_sesv2.types.update_configuration_set_request
    import capo_sesv2.types.update_configuration_set_response
    import capo_sesv2.types.update_contact_list_request
    import capo_sesv2.types.update_contact_list_response
    import capo_sesv2.types.update_contact_request
    import capo_sesv2.types.update_contact_response
    import capo_sesv2.types.update_custom_verification_email_template_request
    import capo_sesv2.types.update_custom_verification_email_template_response
    import capo_sesv2.types.update_email_identity_policy_request
    import capo_sesv2.types.update_email_identity_policy_response
    import capo_sesv2.types.update_email_template_request
    import capo_sesv2.types.update_email_template_response
    import capo_sesv2.types.update_reputation_entity_customer_managed_status_request
    import capo_sesv2.types.update_reputation_entity_customer_managed_status_response
    import capo_sesv2.types.update_reputation_entity_policy_request
    import capo_sesv2.types.update_reputation_entity_policy_response
    import capo_sesv2.types.use_case_description
    import capo_sesv2.types.vdm_attributes
    import capo_sesv2.types.vdm_options
    import capo_sesv2.types.website_url


class AsyncSESv2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSESv2Client:
    """A client for the ``SESv2`` service.

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
        self._config = AsyncSESv2ClientConfig(
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
        self, config_overrides: Optional[AsyncSESv2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSESv2ClientConfig = config_overrides or {}
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

    async def associate_email_identity_certificate(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        certificate_arn: "capo_sesv2.types.certificate_arn.CertificateArn",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        from_address: Optional["capo_sesv2.types.email_address.EmailAddress"] = None,
    ) -> "capo_sesv2.types.associate_email_identity_certificate_response.AssociateEmailIdentityCertificateResponse":
        """<p>Associates an S/MIME certificate with an email identity. After the certificate is active, Amazon SES API v2 can add an S/MIME signature to messages that you send from the associated address when signing is enabled on the configuration set used to send the message.</p> <p>The certificate is an X.509 certificate that you manage in Certificate Manager (ACM). You identify it by its Amazon Resource Name (ARN).</p> <ul> <li> <p>If the email identity is a domain, you must specify a <code>FromAddress</code> that belongs to that domain or one of its subdomains. The certificate applies to messages sent from that address.</p> </li> <li> <p>If the email identity is an email address, <code>FromAddress</code> is optional. If you specify it, it must exactly match the email identity.</p> </li> </ul> <p>When the association is created, the certificate begins provisioning and its status is <code>PROVISIONING</code>. The status changes to <code>ACTIVE</code> when the certificate is ready to use for signing. Each email address can have only one certificate association. If an association already exists for the address, this operation returns an error, unless the existing association is in the <code>DEPROVISIONING</code> state.</p>

        Args:
            email_identity: <p>The email identity, either an email address or a domain, to associate the certificate with.</p>
            from_address: <p>The email address that the certificate applies to. This value is required when the email identity is a domain, and the address must belong to that domain or one of its subdomains. When the email identity is an email address, this value is optional. If you specify it, it must exactly match the email identity.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the Certificate Manager (ACM) certificate to associate with the email identity.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.associate_email_identity_certificate_request.AssociateEmailIdentityCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.associate_email_identity_certificate_response.AssociateEmailIdentityCertificateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.associate_email_identity_certificate

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.associate_email_identity_certificate.async_associate_email_identity_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.associate_email_identity_certificate_request.AssociateEmailIdentityCertificateRequest = {
            "email_identity": email_identity,
            "certificate_arn": certificate_arn,
        }
        if from_address is not None:
            input_["from_address"] = from_address

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_metric_data(
        self,
        queries: "capo_sesv2.types.batch_get_metric_data_queries.BatchGetMetricDataQueries",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.batch_get_metric_data_response.BatchGetMetricDataResponse":
        """<p>Retrieves batches of metric data collected based on your sending activity.</p> <p>You can execute this operation no more than 16 times per second, and with at most 160 queries from the batches per second (cumulative).</p>

        Args:
            queries: <p>A list of queries for metrics to be retrieved.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.internal_service_error_exception.InternalServiceErrorException: <p>The request couldn't be processed because an error occurred with the Amazon SES API v2.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.batch_get_metric_data_request.BatchGetMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.batch_get_metric_data_response.BatchGetMetricDataResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.batch_get_metric_data

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.batch_get_metric_data.async_batch_get_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.batch_get_metric_data_request.BatchGetMetricDataRequest = {
            "queries": queries
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_export_job(
        self,
        job_id: "capo_sesv2.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.cancel_export_job_response.CancelExportJobResponse":
        """<p>Cancels an export job.</p>

        Args:
            job_id: <p>The export job ID.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel export job
            Cancels the export job with ID ef28cf62-9d8e-4b60-9283-b09816c99a99

            >>> await client.cancel_export_job(job_id='ef28cf62-9d8e-4b60-9283-b09816c99a99')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.cancel_export_job_request.CancelExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.cancel_export_job_response.CancelExportJobResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.cancel_export_job

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.cancel_export_job.async_cancel_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.cancel_export_job_request.CancelExportJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tracking_options: Optional[
            "capo_sesv2.types.tracking_options.TrackingOptions"
        ] = None,
        delivery_options: Optional[
            "capo_sesv2.types.delivery_options.DeliveryOptions"
        ] = None,
        reputation_options: Optional[
            "capo_sesv2.types.reputation_options.ReputationOptions"
        ] = None,
        sending_options: Optional[
            "capo_sesv2.types.sending_options.SendingOptions"
        ] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
        suppression_options: Optional[
            "capo_sesv2.types.suppression_options.SuppressionOptions"
        ] = None,
        vdm_options: Optional["capo_sesv2.types.vdm_options.VdmOptions"] = None,
        archiving_options: Optional[
            "capo_sesv2.types.archiving_options.ArchivingOptions"
        ] = None,
        message_security_options: Optional[
            "capo_sesv2.types.message_security_options.MessageSecurityOptions"
        ] = None,
    ) -> "capo_sesv2.types.create_configuration_set_response.CreateConfigurationSetResponse":
        """<p>Create a configuration set. <i>Configuration sets</i> are groups of rules that you can apply to the emails that you send. You apply a configuration set to an email by specifying the name of the configuration set when you call the Amazon SES API v2. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email. </p>

        Args:
            configuration_set_name: <p>The name of the configuration set. The name can contain up to 64 alphanumeric characters, including letters, numbers, hyphens (-) and underscores (_) only.</p>
            tracking_options: <p>An object that defines the open and click tracking options for emails that you send using the configuration set.</p>
            delivery_options: <p>An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.</p>
            reputation_options: <p>An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.</p>
            sending_options: <p>An object that defines whether or not Amazon SES can send email that you send using the configuration set.</p>
            tags: <p>An array of objects that define the tags (keys and values) to associate with the configuration set.</p>
            suppression_options: <p>An object that contains information about the suppression list preferences for the configuration set. You can optionally include a <code>SuppressionScope</code> to override the tenant or account suppression scope for emails sent using this configuration set.</p>
            vdm_options: <p>An object that defines the VDM options for emails that you send using the configuration set.</p>
            archiving_options: <p>An object that defines the MailManager archiving options for emails that you send using the configuration set.</p>
            message_security_options: <p>The message security options to apply to the configuration set, such as the signing scheme used for messages that you send with the configuration set.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_configuration_set_request.CreateConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_configuration_set_response.CreateConfigurationSetResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_configuration_set

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_configuration_set.async_create_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_configuration_set_request.CreateConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }
        if tracking_options is not None:
            input_["tracking_options"] = tracking_options
        if delivery_options is not None:
            input_["delivery_options"] = delivery_options
        if reputation_options is not None:
            input_["reputation_options"] = reputation_options
        if sending_options is not None:
            input_["sending_options"] = sending_options
        if tags is not None:
            input_["tags"] = tags
        if suppression_options is not None:
            input_["suppression_options"] = suppression_options
        if vdm_options is not None:
            input_["vdm_options"] = vdm_options
        if archiving_options is not None:
            input_["archiving_options"] = archiving_options
        if message_security_options is not None:
            input_["message_security_options"] = message_security_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        event_destination_name: "capo_sesv2.types.event_destination_name.EventDestinationName",
        event_destination: "capo_sesv2.types.event_destination_definition.EventDestinationDefinition",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse":
        """<p>Create an event destination. <i>Events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon EventBridge and associate a rule to send the event to the specified target.</p> <p>A single configuration set can include more than one event destination.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set .</p>
            event_destination_name: <p>A name that identifies the event destination within the configuration set.</p>
            event_destination: <p>An object that defines the event destination.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_configuration_set_event_destination.async_create_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
            "event_destination": event_destination,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_contact(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        topic_preferences: Optional[
            "capo_sesv2.types.topic_preference_list.TopicPreferenceList"
        ] = None,
        unsubscribe_all: Optional[
            "capo_sesv2.types.unsubscribe_all.UnsubscribeAll"
        ] = None,
        attributes_data: Optional[
            "capo_sesv2.types.attributes_data.AttributesData"
        ] = None,
    ) -> "capo_sesv2.types.create_contact_response.CreateContactResponse":
        """<p>Creates a contact, which is an end-user who is receiving the email, and adds them to a contact list.</p>

        Args:
            contact_list_name: <p>The name of the contact list to which the contact should be added.</p>
            email_address: <p>The contact's email address.</p>
            topic_preferences: <p>The contact's preferences for being opted-in to or opted-out of topics.</p>
            unsubscribe_all: <p>A boolean value status noting if the contact is unsubscribed from all contact list topics.</p>
            attributes_data: <p>The attribute data attached to a contact.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_contact_request.CreateContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_contact_response.CreateContactResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_contact

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_contact.async_create_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_contact_request.CreateContactRequest = {
            "contact_list_name": contact_list_name,
            "email_address": email_address,
        }
        if topic_preferences is not None:
            input_["topic_preferences"] = topic_preferences
        if unsubscribe_all is not None:
            input_["unsubscribe_all"] = unsubscribe_all
        if attributes_data is not None:
            input_["attributes_data"] = attributes_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_contact_list(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        topics: Optional["capo_sesv2.types.topics.Topics"] = None,
        description: Optional["capo_sesv2.types.description.Description"] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
    ) -> "capo_sesv2.types.create_contact_list_response.CreateContactListResponse":
        """<p>Creates a contact list.</p>

        Args:
            contact_list_name: <p>The name of the contact list.</p>
            topics: <p>An interest group, theme, or label within a list. A contact list can have multiple topics.</p>
            description: <p>A description of what the contact list is about.</p>
            tags: <p>The tags associated with a contact list.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_contact_list_request.CreateContactListRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_contact_list_response.CreateContactListResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_contact_list

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_contact_list.async_create_contact_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_contact_list_request.CreateContactListRequest = {
            "contact_list_name": contact_list_name
        }
        if topics is not None:
            input_["topics"] = topics
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_verification_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        from_email_address: "capo_sesv2.types.email_address.EmailAddress",
        template_subject: "capo_sesv2.types.email_template_subject.EmailTemplateSubject",
        template_content: "capo_sesv2.types.template_content.TemplateContent",
        success_redirection_url: "capo_sesv2.types.success_redirection_url.SuccessRedirectionURL",
        failure_redirection_url: "capo_sesv2.types.failure_redirection_url.FailureRedirectionURL",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
    ) -> "capo_sesv2.types.create_custom_verification_email_template_response.CreateCustomVerificationEmailTemplateResponse":
        """<p>Creates a new custom verification email template.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using custom verification email templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template.</p>
            from_email_address: <p>The email address that the custom verification email is sent from.</p>
            template_subject: <p>The subject line of the custom verification email.</p>
            template_content: <p>The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom-faq">Custom verification email frequently asked questions</a> in the <i>Amazon SES Developer Guide</i>.</p>
            tags: <p>An array of objects that define the tags (keys and values) to associate with the custom verification email template.</p>
            success_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>
            failure_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_custom_verification_email_template_request.CreateCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_custom_verification_email_template_response.CreateCustomVerificationEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_custom_verification_email_template.async_create_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_custom_verification_email_template_request.CreateCustomVerificationEmailTemplateRequest = {
            "template_name": template_name,
            "from_email_address": from_email_address,
            "template_subject": template_subject,
            "template_content": template_content,
            "success_redirection_url": success_redirection_url,
            "failure_redirection_url": failure_redirection_url,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dedicated_ip_pool(
        self,
        pool_name: "capo_sesv2.types.pool_name.PoolName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
        scaling_mode: Optional["capo_sesv2.types.scaling_mode.ScalingMode"] = None,
    ) -> "capo_sesv2.types.create_dedicated_ip_pool_response.CreateDedicatedIpPoolResponse":
        """<p>Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Web Services account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, the message is sent from one of the addresses in the associated pool.</p>

        Args:
            pool_name: <p>The name of the dedicated IP pool.</p>
            tags: <p>An object that defines the tags (keys and values) that you want to associate with the pool.</p>
            scaling_mode: <p>The type of scaling mode.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_dedicated_ip_pool_request.CreateDedicatedIpPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_dedicated_ip_pool_response.CreateDedicatedIpPoolResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_dedicated_ip_pool

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_dedicated_ip_pool.async_create_dedicated_ip_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_dedicated_ip_pool_request.CreateDedicatedIpPoolRequest = {
            "pool_name": pool_name
        }
        if tags is not None:
            input_["tags"] = tags
        if scaling_mode is not None:
            input_["scaling_mode"] = scaling_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_deliverability_test_report(
        self,
        from_email_address: "capo_sesv2.types.email_address.EmailAddress",
        content: "capo_sesv2.types.email_content.EmailContent",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        report_name: Optional["capo_sesv2.types.report_name.ReportName"] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
    ) -> "capo_sesv2.types.create_deliverability_test_report_response.CreateDeliverabilityTestReportResponse":
        """<p>Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon SES then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the <code>GetDeliverabilityTestReport</code> operation to view the results of the test.</p>

        Args:
            report_name: <p>A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.</p>
            from_email_address: <p>The email address that the predictive inbox placement test email was sent from.</p>
            content: <p>The HTML body of the message that you sent when you performed the predictive inbox placement test.</p>
            tags: <p>An array of objects that define the tags (keys and values) that you want to associate with the predictive inbox placement test.</p>

        Raises:
            capo_sesv2.errors.account_suspended_exception.AccountSuspendedException: <p>The message can't be sent because the account's ability to send email has been permanently restricted.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p>The message can't be sent because the sending domain isn't verified.</p>
            capo_sesv2.errors.message_rejected.MessageRejected: <p>The message can't be sent because it contains invalid content.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.sending_paused_exception.SendingPausedException: <p>The message can't be sent because the account's ability to send email is currently paused.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_deliverability_test_report_request.CreateDeliverabilityTestReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_deliverability_test_report_response.CreateDeliverabilityTestReportResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_deliverability_test_report

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_deliverability_test_report.async_create_deliverability_test_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_deliverability_test_report_request.CreateDeliverabilityTestReportRequest = {
            "from_email_address": from_email_address,
            "content": content,
        }
        if report_name is not None:
            input_["report_name"] = report_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_email_identity(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
        dkim_signing_attributes: Optional[
            "capo_sesv2.types.dkim_signing_attributes.DkimSigningAttributes"
        ] = None,
        configuration_set_name: Optional[
            "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
        ] = None,
    ) -> "capo_sesv2.types.create_email_identity_response.CreateEmailIdentityResponse":
        """<p>Starts the process of verifying an email identity. An <i>identity</i> is an email address or domain that you use when you send email. Before you can use an identity to send email, you first have to verify it. By verifying an identity, you demonstrate that you're the owner of the identity, and that you've given Amazon SES API v2 permission to send email from the identity.</p> <p>When you verify an email address, Amazon SES sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. </p> <p>When you verify a domain without specifying the <code>DkimSigningAttributes</code> object, this operation provides a set of DKIM tokens. You can convert these tokens into CNAME records, which you then add to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. This verification method is known as <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p> <p>Alternatively, you can perform the verification process by providing your own public-private key pair. This verification method is known as Bring Your Own DKIM (BYODKIM). To use BYODKIM, your call to the <code>CreateEmailIdentity</code> operation has to include the <code>DkimSigningAttributes</code> object. When you specify this object, you provide a selector (a component of the DNS record name that identifies the public key to use for DKIM authentication) and a private key.</p> <p>When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. For some DNS providers, it can take 72 hours or more to complete the domain verification process.</p> <p>Additionally, you can associate an existing configuration set with the email identity that you're verifying.</p>

        Args:
            email_identity: <p>The email address or domain to verify.</p>
            tags: <p>An array of objects that define the tags (keys and values) to associate with the email identity.</p>
            dkim_signing_attributes: <p>If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p> <p>You can only specify this object if the email identity is a domain, as opposed to an address.</p>
            configuration_set_name: <p>The configuration set to use by default when sending from this identity. Note that any configuration set defined in the email sending request takes precedence. </p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_email_identity_request.CreateEmailIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_email_identity_response.CreateEmailIdentityResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_email_identity

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_email_identity.async_create_email_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_email_identity_request.CreateEmailIdentityRequest = {
            "email_identity": email_identity
        }
        if tags is not None:
            input_["tags"] = tags
        if dkim_signing_attributes is not None:
            input_["dkim_signing_attributes"] = dkim_signing_attributes
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_email_identity_policy(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        policy_name: "capo_sesv2.types.policy_name.PolicyName",
        policy: "capo_sesv2.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.create_email_identity_policy_response.CreateEmailIdentityPolicyResponse":
        """<p>Creates the specified sending authorization policy for the given identity (an email address or a domain).</p> <note> <p>This API is for the identity owner only. If you have not verified the identity, this API will return an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            email_identity: <p>The email identity.</p>
            policy_name: <p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>
            policy: <p>The text of the policy in JSON format. The policy cannot exceed 4 KB.</p> <p>For information about the syntax of sending authorization policies, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html">Amazon SES Developer Guide</a>.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_email_identity_policy_request.CreateEmailIdentityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_email_identity_policy_response.CreateEmailIdentityPolicyResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_email_identity_policy

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_email_identity_policy.async_create_email_identity_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_email_identity_policy_request.CreateEmailIdentityPolicyRequest = {
            "email_identity": email_identity,
            "policy_name": policy_name,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        template_content: "capo_sesv2.types.email_template_content.EmailTemplateContent",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
    ) -> "capo_sesv2.types.create_email_template_response.CreateEmailTemplateResponse":
        """<p>Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the template.</p>
            template_content: <p>The content of the email template, composed of a subject line, an HTML part, and a text-only part.</p>
            tags: <p>An array of objects that define the tags (keys and values) to associate with the email template.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_email_template_request.CreateEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_email_template_response.CreateEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_email_template.async_create_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_email_template_request.CreateEmailTemplateRequest = {
            "template_name": template_name,
            "template_content": template_content,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_export_job(
        self,
        export_data_source: "capo_sesv2.types.export_data_source.ExportDataSource",
        export_destination: "capo_sesv2.types.export_destination.ExportDestination",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.create_export_job_response.CreateExportJobResponse":
        """<p>Creates an export job for a data source and destination.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            export_data_source: <p>The data source for the export job.</p>
            export_destination: <p>The destination for the export job.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_export_job_request.CreateExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_export_job_response.CreateExportJobResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_export_job

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_export_job.async_create_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_export_job_request.CreateExportJobRequest = {
            "export_data_source": export_data_source,
            "export_destination": export_destination,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_import_job(
        self,
        import_destination: "capo_sesv2.types.import_destination.ImportDestination",
        import_data_source: "capo_sesv2.types.import_data_source.ImportDataSource",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.create_import_job_response.CreateImportJobResponse":
        """<p>Creates an import job for a data destination.</p>

        Args:
            import_destination: <p>The destination for the import job.</p>
            import_data_source: <p>The data source for the import job.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_import_job_request.CreateImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_import_job_response.CreateImportJobResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_import_job

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_import_job.async_create_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_import_job_request.CreateImportJobRequest = {
            "import_destination": import_destination,
            "import_data_source": import_data_source,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_multi_region_endpoint(
        self,
        endpoint_name: "capo_sesv2.types.endpoint_name.EndpointName",
        details: "capo_sesv2.types.details.Details",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
    ) -> "capo_sesv2.types.create_multi_region_endpoint_response.CreateMultiRegionEndpointResponse":
        """<p>Creates a multi-region endpoint (global-endpoint).</p> <p>The primary region is going to be the AWS-Region where the operation is executed. The secondary region has to be provided in request's parameters. From the data flow standpoint there is no difference between primary and secondary regions - sending traffic is divided between the two. The primary region is the region where the resource has been created and where it can be managed. </p>

        Args:
            endpoint_name: <p>The name of the multi-region endpoint (global-endpoint).</p>
            details: <p>Contains details of a multi-region endpoint (global-endpoint) being created.</p>
            tags: <p>An array of objects that define the tags (keys and values) to associate with the multi-region endpoint (global-endpoint).</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_multi_region_endpoint_request.CreateMultiRegionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_multi_region_endpoint_response.CreateMultiRegionEndpointResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_multi_region_endpoint

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_multi_region_endpoint.async_create_multi_region_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_multi_region_endpoint_request.CreateMultiRegionEndpointRequest = {
            "endpoint_name": endpoint_name,
            "details": details,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_tenant(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tags: Optional["capo_sesv2.types.tag_list.TagList"] = None,
        suppression_attributes: Optional[
            "capo_sesv2.types.tenant_suppression_attributes.TenantSuppressionAttributes"
        ] = None,
    ) -> "capo_sesv2.types.create_tenant_response.CreateTenantResponse":
        """<p>Create a tenant.</p> <p> <i>Tenants</i> are logical containers that group related SES resources together. Each tenant can have its own set of resources like email identities, configuration sets, and templates, along with reputation metrics and sending status. This helps isolate and manage email sending for different customers or business units within your Amazon SES API v2 account.</p> <p>You can optionally specify <code>SuppressionAttributes</code> to configure tenant-level suppression at creation time. When tenant-level suppression is enabled, Amazon SES maintains a separate suppression list for the tenant instead of using the account-level suppression list.</p>

        Args:
            tenant_name: <p>The name of the tenant to create. The name can contain up to 64 alphanumeric characters, including letters, numbers, hyphens (-) and underscores (_) only.</p>
            tags: <p>An array of objects that define the tags (keys and values) to associate with the tenant</p>
            suppression_attributes: <p>An object that contains information about the suppression list preferences for the tenant. Use this to configure tenant-level suppression at creation time.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_tenant_request.CreateTenantRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_tenant_response.CreateTenantResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_tenant

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_tenant.async_create_tenant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_tenant_request.CreateTenantRequest = {
            "tenant_name": tenant_name
        }
        if tags is not None:
            input_["tags"] = tags
        if suppression_attributes is not None:
            input_["suppression_attributes"] = suppression_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_tenant_resource_association(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.create_tenant_resource_association_response.CreateTenantResourceAssociationResponse":
        """<p>Associate a resource with a tenant.</p> <p> <i>Resources</i> can be email identities, configuration sets, or email templates. When you associate a resource with a tenant, you can use that resource when sending emails on behalf of that tenant.</p> <p>A single resource can be associated with multiple tenants, allowing for resource sharing across different tenants while maintaining isolation in email sending operations.</p>

        Args:
            tenant_name: <p>The name of the tenant to associate the resource with.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to associate with the tenant.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.create_tenant_resource_association_request.CreateTenantResourceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.create_tenant_resource_association_response.CreateTenantResourceAssociationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.create_tenant_resource_association

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.create_tenant_resource_association.async_create_tenant_resource_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.create_tenant_resource_association_request.CreateTenantResourceAssociationRequest = {
            "tenant_name": tenant_name,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_configuration_set_response.DeleteConfigurationSetResponse":
        """<p>Delete an existing configuration set.</p> <p> <i>Configuration sets</i> are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_configuration_set_request.DeleteConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_configuration_set_response.DeleteConfigurationSetResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_configuration_set

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_configuration_set.async_delete_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_configuration_set_request.DeleteConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        event_destination_name: "capo_sesv2.types.event_destination_name.EventDestinationName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse":
        """<p>Delete an event destination.</p> <p> <i>Events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon EventBridge and associate a rule to send the event to the specified target.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that contains the event destination to delete.</p>
            event_destination_name: <p>The name of the event destination to delete.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_configuration_set_event_destination.async_delete_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_contact(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_contact_response.DeleteContactResponse":
        """<p>Removes a contact from a contact list.</p>

        Args:
            contact_list_name: <p>The name of the contact list from which the contact should be removed.</p>
            email_address: <p>The contact's email address.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_contact_request.DeleteContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_contact_response.DeleteContactResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_contact

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_contact.async_delete_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_contact_request.DeleteContactRequest = {
            "contact_list_name": contact_list_name,
            "email_address": email_address,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_contact_list(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_contact_list_response.DeleteContactListResponse":
        """<p>Deletes a contact list and all of the contacts on that list.</p>

        Args:
            contact_list_name: <p>The name of the contact list.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_contact_list_request.DeleteContactListRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_contact_list_response.DeleteContactListResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_contact_list

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_contact_list.async_delete_contact_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_contact_list_request.DeleteContactListRequest = {
            "contact_list_name": contact_list_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_verification_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_custom_verification_email_template_response.DeleteCustomVerificationEmailTemplateResponse":
        """<p>Deletes an existing custom verification email template.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using custom verification email templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template that you want to delete.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_custom_verification_email_template_request.DeleteCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_custom_verification_email_template_response.DeleteCustomVerificationEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_custom_verification_email_template.async_delete_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_custom_verification_email_template_request.DeleteCustomVerificationEmailTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dedicated_ip_pool(
        self,
        pool_name: "capo_sesv2.types.pool_name.PoolName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_dedicated_ip_pool_response.DeleteDedicatedIpPoolResponse":
        """<p>Delete a dedicated IP pool.</p>

        Args:
            pool_name: <p>The name of the dedicated IP pool that you want to delete.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_dedicated_ip_pool_request.DeleteDedicatedIpPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_dedicated_ip_pool_response.DeleteDedicatedIpPoolResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_dedicated_ip_pool

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_dedicated_ip_pool.async_delete_dedicated_ip_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_dedicated_ip_pool_request.DeleteDedicatedIpPoolRequest = {
            "pool_name": pool_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_email_identity(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_email_identity_response.DeleteEmailIdentityResponse":
        """<p>Deletes an email identity. An identity can be either an email address or a domain name.</p>

        Args:
            email_identity: <p>The identity (that is, the email address or domain) to delete.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_email_identity_request.DeleteEmailIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_email_identity_response.DeleteEmailIdentityResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_email_identity

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_email_identity.async_delete_email_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_email_identity_request.DeleteEmailIdentityRequest = {
            "email_identity": email_identity
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_email_identity_policy(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        policy_name: "capo_sesv2.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_email_identity_policy_response.DeleteEmailIdentityPolicyResponse":
        """<p>Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.</p> <note> <p>This API is for the identity owner only. If you have not verified the identity, this API will return an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            email_identity: <p>The email identity.</p>
            policy_name: <p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_email_identity_policy_request.DeleteEmailIdentityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_email_identity_policy_response.DeleteEmailIdentityPolicyResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_email_identity_policy

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_email_identity_policy.async_delete_email_identity_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_email_identity_policy_request.DeleteEmailIdentityPolicyRequest = {
            "email_identity": email_identity,
            "policy_name": policy_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_email_template_response.DeleteEmailTemplateResponse":
        """<p>Deletes an email template.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the template to be deleted.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_email_template_request.DeleteEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_email_template_response.DeleteEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_email_template.async_delete_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_email_template_request.DeleteEmailTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_multi_region_endpoint(
        self,
        endpoint_name: "capo_sesv2.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_multi_region_endpoint_response.DeleteMultiRegionEndpointResponse":
        """<p>Deletes a multi-region endpoint (global-endpoint).</p> <p>Only multi-region endpoints (global-endpoints) whose primary region is the AWS-Region where operation is executed can be deleted.</p>

        Args:
            endpoint_name: <p>The name of the multi-region endpoint (global-endpoint) to be deleted.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_multi_region_endpoint_request.DeleteMultiRegionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_multi_region_endpoint_response.DeleteMultiRegionEndpointResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_multi_region_endpoint

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_multi_region_endpoint.async_delete_multi_region_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_multi_region_endpoint_request.DeleteMultiRegionEndpointRequest = {
            "endpoint_name": endpoint_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_suppressed_destination(
        self,
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tenant_name: Optional["capo_sesv2.types.tenant_name.TenantName"] = None,
    ) -> "capo_sesv2.types.delete_suppressed_destination_response.DeleteSuppressedDestinationResponse":
        """<p>Removes an email address from the suppression list for your account or for a specific tenant. To target a tenant's suppression list, specify the <code>TenantName</code> parameter. If you omit <code>TenantName</code>, the address is removed from the account-level suppression list.</p>

        Args:
            email_address: <p>The suppressed email destination to remove from the suppression list for your account or for the specified tenant.</p>
            tenant_name: <p>The name of the tenant whose suppression list you want to remove the address from. If you omit this parameter, the address is removed from the account-level suppression list.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_suppressed_destination_request.DeleteSuppressedDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_suppressed_destination_response.DeleteSuppressedDestinationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_suppressed_destination

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_suppressed_destination.async_delete_suppressed_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_suppressed_destination_request.DeleteSuppressedDestinationRequest = {
            "email_address": email_address
        }
        if tenant_name is not None:
            input_["tenant_name"] = tenant_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tenant(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_tenant_response.DeleteTenantResponse":
        """<p>Delete an existing tenant.</p> <p>When you delete a tenant, its associations with resources are removed, but the resources themselves are not deleted.</p>

        Args:
            tenant_name: <p>The name of the tenant to delete.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_tenant_request.DeleteTenantRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_tenant_response.DeleteTenantResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_tenant

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_tenant.async_delete_tenant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_tenant_request.DeleteTenantRequest = {
            "tenant_name": tenant_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tenant_resource_association(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.delete_tenant_resource_association_response.DeleteTenantResourceAssociationResponse":
        """<p>Delete an association between a tenant and a resource.</p> <p>When you delete a tenant-resource association, the resource itself is not deleted, only its association with the specific tenant is removed. After removal, the resource will no longer be available for use with that tenant's email sending operations.</p>

        Args:
            tenant_name: <p>The name of the tenant to remove the resource association from.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove from the tenant association.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.delete_tenant_resource_association_request.DeleteTenantResourceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.delete_tenant_resource_association_response.DeleteTenantResourceAssociationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.delete_tenant_resource_association

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.delete_tenant_resource_association.async_delete_tenant_resource_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.delete_tenant_resource_association_request.DeleteTenantResourceAssociationRequest = {
            "tenant_name": tenant_name,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_email_identity_certificate(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        from_address: Optional["capo_sesv2.types.email_address.EmailAddress"] = None,
    ) -> "capo_sesv2.types.disassociate_email_identity_certificate_response.DisassociateEmailIdentityCertificateResponse":
        """<p>Removes the association between an S/MIME certificate and an email identity. After the association is removed, Amazon SES API v2 stops adding an S/MIME signature to messages sent from that address.</p> <p>If the email identity is a domain, specify the <code>FromAddress</code> whose certificate association you want to remove.</p> <p>This operation is idempotent. If the specified email identity exists but there's no matching certificate association, the operation succeeds without making any changes. Amazon SES API v2 returns a <code>NotFoundException</code> only when the specified email identity doesn't exist.</p>

        Args:
            email_identity: <p>The email identity whose certificate association you want to remove.</p>
            from_address: <p>The email address whose certificate association you want to remove. This value is required when the email identity is a domain. When the email identity is an email address, this value is optional.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.disassociate_email_identity_certificate_request.DisassociateEmailIdentityCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.disassociate_email_identity_certificate_response.DisassociateEmailIdentityCertificateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.disassociate_email_identity_certificate

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.disassociate_email_identity_certificate.async_disassociate_email_identity_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.disassociate_email_identity_certificate_request.DisassociateEmailIdentityCertificateRequest = {
            "email_identity": email_identity
        }
        if from_address is not None:
            input_["from_address"] = from_address

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account(
        self, *, config_overrides: Optional[AsyncSESv2ClientConfig] = None
    ) -> "capo_sesv2.types.get_account_response.GetAccountResponse":
        """<p>Obtain information about the email-sending status and capabilities of your Amazon SES account in the current Amazon Web Services Region.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_account_request.GetAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_account_response.GetAccountResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_account

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_account.async_get_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_account_request.GetAccountRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_blacklist_reports(
        self,
        blacklist_item_names: "capo_sesv2.types.blacklist_item_names.BlacklistItemNames",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_blacklist_reports_response.GetBlacklistReportsResponse":
        """<p>Retrieve a list of the blacklists that your dedicated IP addresses appear on.</p>

        Args:
            blacklist_item_names: <p>A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon SES or Amazon Pinpoint.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_blacklist_reports_request.GetBlacklistReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_blacklist_reports_response.GetBlacklistReportsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_blacklist_reports

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_blacklist_reports.async_get_blacklist_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_blacklist_reports_request.GetBlacklistReportsRequest = {
            "blacklist_item_names": blacklist_item_names
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_set(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_configuration_set_response.GetConfigurationSetResponse":
        """<p>Get information about an existing configuration set, including the dedicated IP pool that it's associated with, whether or not it's enabled for sending email, and more.</p> <p> <i>Configuration sets</i> are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_configuration_set_request.GetConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_configuration_set_response.GetConfigurationSetResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_configuration_set

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_configuration_set.async_get_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_configuration_set_request.GetConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_set_event_destinations(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_configuration_set_event_destinations_response.GetConfigurationSetEventDestinationsResponse":
        """<p>Retrieve a list of event destinations that are associated with a configuration set.</p> <p> <i>Events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon EventBridge and associate a rule to send the event to the specified target.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that contains the event destination.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_configuration_set_event_destinations_request.GetConfigurationSetEventDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_configuration_set_event_destinations_response.GetConfigurationSetEventDestinationsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_configuration_set_event_destinations

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_configuration_set_event_destinations.async_get_configuration_set_event_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_configuration_set_event_destinations_request.GetConfigurationSetEventDestinationsRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_contact(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_contact_response.GetContactResponse":
        """<p>Returns a contact from a contact list.</p>

        Args:
            contact_list_name: <p>The name of the contact list to which the contact belongs.</p>
            email_address: <p>The contact's email address.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_contact_request.GetContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_contact_response.GetContactResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_contact

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_contact.async_get_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_contact_request.GetContactRequest = {
            "contact_list_name": contact_list_name,
            "email_address": email_address,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_contact_list(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_contact_list_response.GetContactListResponse":
        """<p>Returns contact list metadata. It does not return any information about the contacts present in the list.</p>

        Args:
            contact_list_name: <p>The name of the contact list.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_contact_list_request.GetContactListRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_contact_list_response.GetContactListResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_contact_list

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_contact_list.async_get_contact_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_contact_list_request.GetContactListRequest = {
            "contact_list_name": contact_list_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_custom_verification_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_custom_verification_email_template_response.GetCustomVerificationEmailTemplateResponse":
        """<p>Returns the custom email verification template for the template name you specify.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using custom verification email templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template that you want to retrieve.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_custom_verification_email_template_request.GetCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_custom_verification_email_template_response.GetCustomVerificationEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_custom_verification_email_template.async_get_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_custom_verification_email_template_request.GetCustomVerificationEmailTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dedicated_ip(
        self,
        ip: "capo_sesv2.types.ip.Ip",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_dedicated_ip_response.GetDedicatedIpResponse":
        """<p>Get information about a dedicated IP address, including the name of the dedicated IP pool that it's associated with, as well information about the automatic warm-up process for the address.</p>

        Args:
            ip: <p>The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that's assocaited with your Amazon Web Services account.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_dedicated_ip_request.GetDedicatedIpRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_dedicated_ip_response.GetDedicatedIpResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_dedicated_ip

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_dedicated_ip.async_get_dedicated_ip(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_dedicated_ip_request.GetDedicatedIpRequest = {
            "ip": ip
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dedicated_ip_pool(
        self,
        pool_name: "capo_sesv2.types.pool_name.PoolName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_dedicated_ip_pool_response.GetDedicatedIpPoolResponse":
        """<p>Retrieve information about the dedicated pool.</p>

        Args:
            pool_name: <p>The name of the dedicated IP pool to retrieve.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_dedicated_ip_pool_request.GetDedicatedIpPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_dedicated_ip_pool_response.GetDedicatedIpPoolResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_dedicated_ip_pool

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_dedicated_ip_pool.async_get_dedicated_ip_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_dedicated_ip_pool_request.GetDedicatedIpPoolRequest = {
            "pool_name": pool_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_dedicated_ips(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        pool_name: Optional["capo_sesv2.types.pool_name.PoolName"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.get_dedicated_ips_response.GetDedicatedIpsResponse":
        """<p>List the dedicated IP addresses that are associated with your Amazon Web Services account.</p>

        Args:
            pool_name: <p>The name of the IP pool that the dedicated IP address is associated with.</p>
            next_token: <p>A token returned from a previous call to <code>GetDedicatedIps</code> to indicate the position of the dedicated IP pool in the list of IP pools.</p>
            page_size: <p>The number of results to show in a single call to <code>GetDedicatedIpsRequest</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_dedicated_ips_request.GetDedicatedIpsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_dedicated_ips_response.GetDedicatedIpsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_dedicated_ips

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_dedicated_ips.async_get_dedicated_ips(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_dedicated_ips_request.GetDedicatedIpsRequest = {}
        if pool_name is not None:
            input_["pool_name"] = pool_name
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_dedicated_ips(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        pool_name: Optional["capo_sesv2.types.pool_name.PoolName"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.get_dedicated_ips_response.GetDedicatedIpsResponse]":
        _token = next_token
        while True:
            _response = await self.get_dedicated_ips(
                config_overrides=config_overrides,
                pool_name=pool_name,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_deliverability_dashboard_options(
        self, *, config_overrides: Optional[AsyncSESv2ClientConfig] = None
    ) -> "capo_sesv2.types.get_deliverability_dashboard_options_response.GetDeliverabilityDashboardOptionsResponse":
        """<p>Retrieve information about the status of the Deliverability dashboard for your account. When the Deliverability dashboard is enabled, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.</p> <p>When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other Amazon Web Services services. For more information about the features and cost of a Deliverability dashboard subscription, see <a href="http://aws.amazon.com/ses/pricing/">Amazon SES Pricing</a>.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_deliverability_dashboard_options_request.GetDeliverabilityDashboardOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_deliverability_dashboard_options_response.GetDeliverabilityDashboardOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_deliverability_dashboard_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_deliverability_dashboard_options.async_get_deliverability_dashboard_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_deliverability_dashboard_options_request.GetDeliverabilityDashboardOptionsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_deliverability_test_report(
        self,
        report_id: "capo_sesv2.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_deliverability_test_report_response.GetDeliverabilityTestReportResponse":
        """<p>Retrieve the results of a predictive inbox placement test.</p>

        Args:
            report_id: <p>A unique string that identifies the predictive inbox placement test.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_deliverability_test_report_request.GetDeliverabilityTestReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_deliverability_test_report_response.GetDeliverabilityTestReportResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_deliverability_test_report

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_deliverability_test_report.async_get_deliverability_test_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_deliverability_test_report_request.GetDeliverabilityTestReportRequest = {
            "report_id": report_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_deliverability_campaign(
        self,
        campaign_id: "capo_sesv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_domain_deliverability_campaign_response.GetDomainDeliverabilityCampaignResponse":
        """<p>Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for.</p>

        Args:
            campaign_id: <p>The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_domain_deliverability_campaign_request.GetDomainDeliverabilityCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_domain_deliverability_campaign_response.GetDomainDeliverabilityCampaignResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_domain_deliverability_campaign

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_domain_deliverability_campaign.async_get_domain_deliverability_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_domain_deliverability_campaign_request.GetDomainDeliverabilityCampaignRequest = {
            "campaign_id": campaign_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain_statistics_report(
        self,
        domain: "capo_sesv2.types.identity.Identity",
        start_date: "capo_sesv2.types.timestamp.Timestamp",
        end_date: "capo_sesv2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_domain_statistics_report_response.GetDomainStatisticsReportResponse":
        """<p>Retrieve inbox placement and engagement rates for the domains that you use to send email.</p>

        Args:
            domain: <p>The domain that you want to obtain deliverability metrics for.</p>
            start_date: <p>The first day (in Unix time) that you want to obtain domain deliverability metrics for.</p>
            end_date: <p>The last day (in Unix time) that you want to obtain domain deliverability metrics for. The <code>EndDate</code> that you specify has to be less than or equal to 30 days after the <code>StartDate</code>.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_domain_statistics_report_request.GetDomainStatisticsReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_domain_statistics_report_response.GetDomainStatisticsReportResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_domain_statistics_report

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_domain_statistics_report.async_get_domain_statistics_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_domain_statistics_report_request.GetDomainStatisticsReportRequest = {
            "domain": domain,
            "start_date": start_date,
            "end_date": end_date,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_email_address_insights(
        self,
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_email_address_insights_response.GetEmailAddressInsightsResponse":
        """<p>Provides validation insights about a specific email address, including syntax validation, DNS record checks, mailbox existence, and other deliverability factors.</p>

        Args:
            email_address: <p>The email address to analyze for validation insights.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get Email Address Insights
            Performs email validation against an email address.

            >>> await client.get_email_address_insights(email_address='hello@example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_email_address_insights_request.GetEmailAddressInsightsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_email_address_insights_response.GetEmailAddressInsightsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_email_address_insights

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_email_address_insights.async_get_email_address_insights(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_email_address_insights_request.GetEmailAddressInsightsRequest = {
            "email_address": email_address
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_email_identity(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_email_identity_response.GetEmailIdentityResponse":
        """<p>Provides information about a specific identity, including the identity's verification status, sending authorization policies, its DKIM authentication status, and its custom Mail-From settings.</p>

        Args:
            email_identity: <p>The email identity.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_email_identity_request.GetEmailIdentityRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_email_identity_response.GetEmailIdentityResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_email_identity

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_email_identity.async_get_email_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_email_identity_request.GetEmailIdentityRequest = {
            "email_identity": email_identity
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_email_identity_policies(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_email_identity_policies_response.GetEmailIdentityPoliciesResponse":
        """<p>Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.</p> <note> <p>This API is for the identity owner only. If you have not verified the identity, this API will return an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            email_identity: <p>The email identity.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_email_identity_policies_request.GetEmailIdentityPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_email_identity_policies_response.GetEmailIdentityPoliciesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_email_identity_policies

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_email_identity_policies.async_get_email_identity_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_email_identity_policies_request.GetEmailIdentityPoliciesRequest = {
            "email_identity": email_identity
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_email_template_response.GetEmailTemplateResponse":
        """<p>Displays the template object (which includes the subject line, HTML part and text part) for the template you specify.</p> <p>You can execute this operation no more than 50 times per second.</p>

        Args:
            template_name: <p>The name of the template.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_email_template_request.GetEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_email_template_response.GetEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_email_template.async_get_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_email_template_request.GetEmailTemplateRequest = {
            "template_name": template_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_export_job(
        self,
        job_id: "capo_sesv2.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_export_job_response.GetExportJobResponse":
        """<p>Provides information about an export job.</p>

        Args:
            job_id: <p>The export job ID.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_export_job_request.GetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_export_job_response.GetExportJobResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_export_job

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_export_job.async_get_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_export_job_request.GetExportJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import_job(
        self,
        job_id: "capo_sesv2.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_import_job_response.GetImportJobResponse":
        """<p>Provides information about an import job.</p>

        Args:
            job_id: <p>The ID of the import job.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_import_job_request.GetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_import_job_response.GetImportJobResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_import_job

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_import_job.async_get_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_import_job_request.GetImportJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_message_insights(
        self,
        message_id: "capo_sesv2.types.outbound_message_id.OutboundMessageId",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_message_insights_response.GetMessageInsightsResponse":
        """<p>Provides information about a specific message, including the from address, the subject, the recipient address, email tags, as well as events associated with the message.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            message_id: <p> A <code>MessageId</code> is a unique identifier for a message, and is returned when sending emails through Amazon SES. </p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_message_insights_request.GetMessageInsightsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_message_insights_response.GetMessageInsightsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_message_insights

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_message_insights.async_get_message_insights(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_message_insights_request.GetMessageInsightsRequest = {
            "message_id": message_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_multi_region_endpoint(
        self,
        endpoint_name: "capo_sesv2.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_multi_region_endpoint_response.GetMultiRegionEndpointResponse":
        """<p>Displays the multi-region endpoint (global-endpoint) configuration.</p> <p>Only multi-region endpoints (global-endpoints) whose primary region is the AWS-Region where operation is executed can be displayed.</p>

        Args:
            endpoint_name: <p>The name of the multi-region endpoint (global-endpoint).</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_multi_region_endpoint_request.GetMultiRegionEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_multi_region_endpoint_response.GetMultiRegionEndpointResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_multi_region_endpoint

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_multi_region_endpoint.async_get_multi_region_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_multi_region_endpoint_request.GetMultiRegionEndpointRequest = {
            "endpoint_name": endpoint_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reputation_entity(
        self,
        reputation_entity_reference: "capo_sesv2.types.reputation_entity_reference.ReputationEntityReference",
        reputation_entity_type: "capo_sesv2.types.reputation_entity_type.ReputationEntityType",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_reputation_entity_response.GetReputationEntityResponse":
        """<p>Retrieve information about a specific reputation entity, including its reputation management policy, customer-managed status, Amazon Web Services Amazon SES-managed status, and aggregate sending status.</p> <p> <i>Reputation entities</i> represent resources in your Amazon SES account that have reputation tracking and management capabilities. The reputation impact reflects the highest impact reputation finding for the entity. Reputation findings can be retrieved using the <code>ListRecommendations</code> operation.</p>

        Args:
            reputation_entity_reference: <p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>
            reputation_entity_type: <p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_reputation_entity_request.GetReputationEntityRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_reputation_entity_response.GetReputationEntityResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_reputation_entity

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_reputation_entity.async_get_reputation_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_reputation_entity_request.GetReputationEntityRequest = {
            "reputation_entity_reference": reputation_entity_reference,
            "reputation_entity_type": reputation_entity_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_suppressed_destination(
        self,
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tenant_name: Optional["capo_sesv2.types.tenant_name.TenantName"] = None,
    ) -> "capo_sesv2.types.get_suppressed_destination_response.GetSuppressedDestinationResponse":
        """<p>Retrieves information about a specific email address that's on the suppression list for your account or for a specific tenant. To target a tenant's suppression list, specify the <code>TenantName</code> parameter. If you omit <code>TenantName</code>, the operation targets the account-level suppression list.</p>

        Args:
            email_address: <p>The email address that's on the suppression list for your account or for the specified tenant.</p>
            tenant_name: <p>The name of the tenant whose suppression list you want to query. If you omit this parameter, the operation targets the account-level suppression list.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_suppressed_destination_request.GetSuppressedDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_suppressed_destination_response.GetSuppressedDestinationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_suppressed_destination

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_suppressed_destination.async_get_suppressed_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_suppressed_destination_request.GetSuppressedDestinationRequest = {
            "email_address": email_address
        }
        if tenant_name is not None:
            input_["tenant_name"] = tenant_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_tenant(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.get_tenant_response.GetTenantResponse":
        """<p>Get information about a specific tenant, including the tenant's name, ID, ARN, creation timestamp, tags, sending status, and suppression attributes.</p>

        Args:
            tenant_name: <p>The name of the tenant to retrieve information about.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.get_tenant_request.GetTenantRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.get_tenant_response.GetTenantResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.get_tenant

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.get_tenant.async_get_tenant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.get_tenant_request.GetTenantRequest = {
            "tenant_name": tenant_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configuration_sets(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.configuration_set_filter.ConfigurationSetFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_configuration_sets_response.ListConfigurationSetsResponse":
        """<p>List all of the configuration sets associated with your account in the current region.</p> <p> <i>Configuration sets</i> are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.</p>

        Args:
            filter: <p>An object that contains filters to apply when listing configuration sets. You can filter by configuration set name.</p>
            next_token: <p>A token returned from a previous call to <code>ListConfigurationSets</code> to indicate the position in the list of configuration sets.</p>
            page_size: <p>The number of results to show in a single call to <code>ListConfigurationSets</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_configuration_sets_request.ListConfigurationSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_configuration_sets_response.ListConfigurationSetsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_configuration_sets

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_configuration_sets.async_list_configuration_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_configuration_sets_request.ListConfigurationSetsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configuration_sets(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.configuration_set_filter.ConfigurationSetFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_configuration_sets_response.ListConfigurationSetsResponse]":
        _token = next_token
        while True:
            _response = await self.list_configuration_sets(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_contact_lists(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "capo_sesv2.types.list_contact_lists_response.ListContactListsResponse":
        """<p>Lists all of the contact lists available.</p> <p>If your output includes a "NextToken" field with a string value, this indicates there may be additional contacts on the filtered list - regardless of the number of contacts returned.</p>

        Args:
            page_size: <p>Maximum number of contact lists to return at once. Use this parameter to paginate results. If additional contact lists exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional lists.</p>
            next_token: <p>A string token indicating that there might be additional contact lists available to be listed. Use the token provided in the Response to use in the subsequent call to ListContactLists with the same parameters to retrieve the next page of contact lists.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_contact_lists_request.ListContactListsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_contact_lists_response.ListContactListsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_contact_lists

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_contact_lists.async_list_contact_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_contact_lists_request.ListContactListsRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_contact_lists(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_contact_lists_response.ListContactListsResponse]":
        _token = next_token
        while True:
            _response = await self.list_contact_lists(
                config_overrides=config_overrides,
                page_size=page_size,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_contacts(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_contacts_filter.ListContactsFilter"
        ] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "capo_sesv2.types.list_contacts_response.ListContactsResponse":
        """<p>Lists the contacts present in a specific contact list.</p>

        Args:
            contact_list_name: <p>The name of the contact list.</p>
            filter: <p>A filter that can be applied to a list of contacts.</p>
            page_size: <p>The number of contacts that may be returned at once, which is dependent on if there are more or less contacts than the value of the PageSize. Use this parameter to paginate results. If additional contacts exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional contacts.</p>
            next_token: <p>A string token indicating that there might be additional contacts available to be listed. Use the token provided in the Response to use in the subsequent call to ListContacts with the same parameters to retrieve the next page of contacts.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_contacts_request.ListContactsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_contacts_response.ListContactsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_contacts

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_contacts.async_list_contacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_contacts_request.ListContactsRequest = {
            "contact_list_name": contact_list_name
        }
        if filter is not None:
            input_["filter"] = filter
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_contacts(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_contacts_filter.ListContactsFilter"
        ] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_contacts_response.ListContactsResponse]":
        _token = next_token
        while True:
            _response = await self.list_contacts(
                contact_list_name,
                config_overrides=config_overrides,
                filter=filter,
                page_size=page_size,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_custom_verification_email_templates(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_custom_verification_email_templates_response.ListCustomVerificationEmailTemplatesResponse":
        """<p>Lists the existing custom verification email templates for your account in the current Amazon Web Services Region.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using custom verification email templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListCustomVerificationEmailTemplates</code> to indicate the position in the list of custom verification email templates.</p>
            page_size: <p>The number of results to show in a single call to <code>ListCustomVerificationEmailTemplates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 50.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_custom_verification_email_templates_request.ListCustomVerificationEmailTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_custom_verification_email_templates_response.ListCustomVerificationEmailTemplatesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_custom_verification_email_templates

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_custom_verification_email_templates.async_list_custom_verification_email_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_custom_verification_email_templates_request.ListCustomVerificationEmailTemplatesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_custom_verification_email_templates(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_custom_verification_email_templates_response.ListCustomVerificationEmailTemplatesResponse]":
        _token = next_token
        while True:
            _response = await self.list_custom_verification_email_templates(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dedicated_ip_pools(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> (
        "capo_sesv2.types.list_dedicated_ip_pools_response.ListDedicatedIpPoolsResponse"
    ):
        """<p>List all of the dedicated IP pools that exist in your Amazon Web Services account in the current Region.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListDedicatedIpPools</code> to indicate the position in the list of dedicated IP pools.</p>
            page_size: <p>The number of results to show in a single call to <code>ListDedicatedIpPools</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_dedicated_ip_pools_request.ListDedicatedIpPoolsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_dedicated_ip_pools_response.ListDedicatedIpPoolsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_dedicated_ip_pools

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_dedicated_ip_pools.async_list_dedicated_ip_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_dedicated_ip_pools_request.ListDedicatedIpPoolsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_dedicated_ip_pools(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_dedicated_ip_pools_response.ListDedicatedIpPoolsResponse]":
        _token = next_token
        while True:
            _response = await self.list_dedicated_ip_pools(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_deliverability_test_reports(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_deliverability_test_reports_response.ListDeliverabilityTestReportsResponse":
        """<p>Show a list of the predictive inbox placement tests that you've performed, regardless of their statuses. For predictive inbox placement tests that are complete, you can use the <code>GetDeliverabilityTestReport</code> operation to view the results.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListDeliverabilityTestReports</code> to indicate the position in the list of predictive inbox placement tests.</p>
            page_size: <p>The number of results to show in a single call to <code>ListDeliverabilityTestReports</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_deliverability_test_reports_request.ListDeliverabilityTestReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_deliverability_test_reports_response.ListDeliverabilityTestReportsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_deliverability_test_reports

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_deliverability_test_reports.async_list_deliverability_test_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_deliverability_test_reports_request.ListDeliverabilityTestReportsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_deliverability_test_reports(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_deliverability_test_reports_response.ListDeliverabilityTestReportsResponse]":
        _token = next_token
        while True:
            _response = await self.list_deliverability_test_reports(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_domain_deliverability_campaigns(
        self,
        start_date: "capo_sesv2.types.timestamp.Timestamp",
        end_date: "capo_sesv2.types.timestamp.Timestamp",
        subscribed_domain: "capo_sesv2.types.domain.Domain",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_domain_deliverability_campaigns_response.ListDomainDeliverabilityCampaignsResponse":
        """<p>Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range. This data is available for a domain only if you enabled the Deliverability dashboard for the domain.</p>

        Args:
            start_date: <p>The first day that you want to obtain deliverability data for.</p>
            end_date: <p>The last day that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the <code>StartDate</code> parameter.</p>
            subscribed_domain: <p>The domain to obtain deliverability data for.</p>
            next_token: <p>A token that’s returned from a previous call to the <code>ListDomainDeliverabilityCampaigns</code> operation. This token indicates the position of a campaign in the list of campaigns.</p>
            page_size: <p>The maximum number of results to include in response to a single call to the <code>ListDomainDeliverabilityCampaigns</code> operation. If the number of results is larger than the number that you specify in this parameter, the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_domain_deliverability_campaigns_request.ListDomainDeliverabilityCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_domain_deliverability_campaigns_response.ListDomainDeliverabilityCampaignsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_domain_deliverability_campaigns

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_domain_deliverability_campaigns.async_list_domain_deliverability_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_domain_deliverability_campaigns_request.ListDomainDeliverabilityCampaignsRequest = {
            "start_date": start_date,
            "end_date": end_date,
            "subscribed_domain": subscribed_domain,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_domain_deliverability_campaigns(
        self,
        start_date: "capo_sesv2.types.timestamp.Timestamp",
        end_date: "capo_sesv2.types.timestamp.Timestamp",
        subscribed_domain: "capo_sesv2.types.domain.Domain",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_domain_deliverability_campaigns_response.ListDomainDeliverabilityCampaignsResponse]":
        _token = next_token
        while True:
            _response = await self.list_domain_deliverability_campaigns(
                start_date,
                end_date,
                subscribed_domain,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_email_identities(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional["capo_sesv2.types.identity_filter.IdentityFilter"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_email_identities_response.ListEmailIdentitiesResponse":
        """<p>Returns a list of all of the email identities that are associated with your Amazon Web Services account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren't. This operation returns identities that are associated with Amazon SES and Amazon Pinpoint.</p>

        Args:
            filter: <p>An object that contains filters to apply when listing email identities. You can filter by identity name, identity type, or verification status.</p>
            next_token: <p>A token returned from a previous call to <code>ListEmailIdentities</code> to indicate the position in the list of identities.</p>
            page_size: <p>The number of results to show in a single call to <code>ListEmailIdentities</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_email_identities_request.ListEmailIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_email_identities_response.ListEmailIdentitiesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_email_identities

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_email_identities.async_list_email_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_email_identities_request.ListEmailIdentitiesRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_email_identities(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional["capo_sesv2.types.identity_filter.IdentityFilter"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_email_identities_response.ListEmailIdentitiesResponse]":
        _token = next_token
        while True:
            _response = await self.list_email_identities(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_email_identity_certificates(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_email_identity_certificates_response.ListEmailIdentityCertificatesResponse":
        """<p>Lists the S/MIME certificates that are associated with the specified email identity. The results include certificates in all states, such as <code>PROVISIONING</code>, <code>ACTIVE</code>, <code>INACTIVE</code>, <code>DEPROVISIONING</code>, and <code>FAILED</code>.</p> <p>If a certificate has passed its expiration time, it's returned with a status of <code>FAILED</code>.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully. When there are more results than fit in a single response, the response includes a <code>NextToken</code> value that you use in a subsequent call to retrieve the next set of results.</p>

        Args:
            email_identity: <p>The email identity whose certificate associations you want to list.</p>
            next_token: <p>A token returned from a previous call to <code>ListEmailIdentityCertificates</code> to indicate the position in the list of certificates.</p>
            page_size: <p>The number of results to show in a single call to <code>ListEmailIdentityCertificates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_email_identity_certificates_request.ListEmailIdentityCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_email_identity_certificates_response.ListEmailIdentityCertificatesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_email_identity_certificates

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_email_identity_certificates.async_list_email_identity_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_email_identity_certificates_request.ListEmailIdentityCertificatesRequest = {
            "email_identity": email_identity
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_email_identity_certificates(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.identity_certificate.IdentityCertificate]":
        _token = next_token
        while True:
            _response = await self.list_email_identity_certificates(
                email_identity,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("certificates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_email_templates(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_email_templates_response.ListEmailTemplatesResponse":
        """<p>Lists the email templates present in your Amazon SES account in the current Amazon Web Services Region.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListEmailTemplates</code> to indicate the position in the list of email templates.</p>
            page_size: <p>The number of results to show in a single call to <code>ListEmailTemplates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 100.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_email_templates_request.ListEmailTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_email_templates_response.ListEmailTemplatesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_email_templates

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_email_templates.async_list_email_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_email_templates_request.ListEmailTemplatesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_email_templates(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_email_templates_response.ListEmailTemplatesResponse]":
        _token = next_token
        while True:
            _response = await self.list_email_templates(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        export_source_type: Optional[
            "capo_sesv2.types.export_source_type.ExportSourceType"
        ] = None,
        job_status: Optional["capo_sesv2.types.job_status.JobStatus"] = None,
    ) -> "capo_sesv2.types.list_export_jobs_response.ListExportJobsResponse":
        """<p>Lists all of the export jobs.</p>

        Args:
            next_token: <p>The pagination token returned from a previous call to <code>ListExportJobs</code> to indicate the position in the list of export jobs.</p>
            page_size: <p>Maximum number of export jobs to return at once. Use this parameter to paginate results. If additional export jobs exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent calls to <code>ListExportJobs</code> to retrieve additional export jobs.</p>
            export_source_type: <p>A value used to list export jobs that have a certain <code>ExportSourceType</code>.</p>
            job_status: <p>A value used to list export jobs that have a certain <code>JobStatus</code>.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_export_jobs_request.ListExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_export_jobs_response.ListExportJobsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_export_jobs

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_export_jobs.async_list_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_export_jobs_request.ListExportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if export_source_type is not None:
            input_["export_source_type"] = export_source_type
        if job_status is not None:
            input_["job_status"] = job_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        export_source_type: Optional[
            "capo_sesv2.types.export_source_type.ExportSourceType"
        ] = None,
        job_status: Optional["capo_sesv2.types.job_status.JobStatus"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_export_jobs_response.ListExportJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_export_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
                export_source_type=export_source_type,
                job_status=job_status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        import_destination_type: Optional[
            "capo_sesv2.types.import_destination_type.ImportDestinationType"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_import_jobs_response.ListImportJobsResponse":
        """<p>Lists all of the import jobs.</p>

        Args:
            import_destination_type: <p>The destination of the import job, which can be used to list import jobs that have a certain <code>ImportDestinationType</code>.</p>
            next_token: <p>A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to <code>ListImportJobs</code> with the same parameters to retrieve the next page of import jobs.</p>
            page_size: <p>Maximum number of import jobs to return at once. Use this parameter to paginate results. If additional import jobs exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional addresses.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_import_jobs_request.ListImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_import_jobs_response.ListImportJobsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_import_jobs

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_import_jobs.async_list_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_import_jobs_request.ListImportJobsRequest = {}
        if import_destination_type is not None:
            input_["import_destination_type"] = import_destination_type
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        import_destination_type: Optional[
            "capo_sesv2.types.import_destination_type.ImportDestinationType"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_import_jobs_response.ListImportJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_import_jobs(
                config_overrides=config_overrides,
                import_destination_type=import_destination_type,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_multi_region_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token_v2.NextTokenV2"] = None,
        page_size: Optional["capo_sesv2.types.page_size_v2.PageSizeV2"] = None,
    ) -> "capo_sesv2.types.list_multi_region_endpoints_response.ListMultiRegionEndpointsResponse":
        """<p>List the multi-region endpoints (global-endpoints).</p> <p>Only multi-region endpoints (global-endpoints) whose primary region is the AWS-Region where operation is executed will be listed.</p>

        Args:
            next_token: <p>A token returned from a previous call to <code>ListMultiRegionEndpoints</code> to indicate the position in the list of multi-region endpoints (global-endpoints).</p>
            page_size: <p>The number of results to show in a single call to <code>ListMultiRegionEndpoints</code>. If the number of results is larger than the number you specified in this parameter, the response includes a <code>NextToken</code> element that you can use to retrieve the next page of results. </p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_multi_region_endpoints_request.ListMultiRegionEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_multi_region_endpoints_response.ListMultiRegionEndpointsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_multi_region_endpoints

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_multi_region_endpoints.async_list_multi_region_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_multi_region_endpoints_request.ListMultiRegionEndpointsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_multi_region_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        next_token: Optional["capo_sesv2.types.next_token_v2.NextTokenV2"] = None,
        page_size: Optional["capo_sesv2.types.page_size_v2.PageSizeV2"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.multi_region_endpoint.MultiRegionEndpoint]":
        _token = next_token
        while True:
            _response = await self.list_multi_region_endpoints(
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("multi_region_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_recommendations_filter.ListRecommendationsFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists the recommendations present in your Amazon SES account in the current Amazon Web Services Region.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            filter: <p>Filters applied when retrieving recommendations. Can eiter be an individual filter, or combinations of <code>STATUS</code> and <code>IMPACT</code> or <code>STATUS</code> and <code>TYPE</code> </p>
            next_token: <p>A token returned from a previous call to <code>ListRecommendations</code> to indicate the position in the list of recommendations.</p>
            page_size: <p>The number of results to show in a single call to <code>ListRecommendations</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 100.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_recommendations

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_recommendations.async_list_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_recommendations_request.ListRecommendationsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_recommendations_filter.ListRecommendationsFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_recommendations_response.ListRecommendationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_recommendations(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_reputation_entities(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.reputation_entity_filter.ReputationEntityFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_reputation_entities_response.ListReputationEntitiesResponse":
        """<p>List reputation entities in your Amazon SES account in the current Amazon Web Services Region. You can filter the results by entity type, reputation impact, sending status, or entity reference prefix.</p> <p> <i>Reputation entities</i> represent resources in your account that have reputation tracking and management capabilities. Use this operation to get an overview of all entities and their current reputation status.</p>

        Args:
            filter: <p>An object that contains filters to apply when listing reputation entities. You can filter by entity type, reputation impact, sending status, or entity reference prefix.</p>
            next_token: <p>A token returned from a previous call to <code>ListReputationEntities</code> to indicate the position in the list of reputation entities.</p>
            page_size: <p>The number of results to show in a single call to <code>ListReputationEntities</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_reputation_entities_request.ListReputationEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_reputation_entities_response.ListReputationEntitiesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_reputation_entities

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_reputation_entities.async_list_reputation_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_reputation_entities_request.ListReputationEntitiesRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_reputation_entities(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.reputation_entity_filter.ReputationEntityFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.reputation_entity.ReputationEntity]":
        _token = next_token
        while True:
            _response = await self.list_reputation_entities(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("reputation_entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_tenants(
        self,
        resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "capo_sesv2.types.list_resource_tenants_response.ListResourceTenantsResponse":
        """<p>List all tenants associated with a specific resource.</p> <p>This operation returns a list of tenants that are associated with the specified resource. This is useful for understanding which tenants are currently using a particular resource such as an email identity, configuration set, or email template.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list associated tenants for.</p>
            page_size: <p>The number of results to show in a single call to <code>ListResourceTenants</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            next_token: <p>A token returned from a previous call to <code>ListResourceTenants</code> to indicate the position in the list of resource tenants.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_resource_tenants_request.ListResourceTenantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_resource_tenants_response.ListResourceTenantsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_resource_tenants

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_resource_tenants.async_list_resource_tenants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_resource_tenants_request.ListResourceTenantsRequest = {
            "resource_arn": resource_arn
        }
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resource_tenants(
        self,
        resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.resource_tenant_metadata.ResourceTenantMetadata]":
        _token = next_token
        while True:
            _response = await self.list_resource_tenants(
                resource_arn,
                config_overrides=config_overrides,
                page_size=page_size,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_tenants",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_suppressed_destinations(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tenant_name: Optional["capo_sesv2.types.tenant_name.TenantName"] = None,
        reasons: Optional[
            "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
        ] = None,
        start_date: Optional["capo_sesv2.types.timestamp.Timestamp"] = None,
        end_date: Optional["capo_sesv2.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_suppressed_destinations_response.ListSuppressedDestinationsResponse":
        """<p>Retrieves a list of email addresses that are on the suppression list for your account or for a specific tenant. To target a tenant's suppression list, specify the <code>TenantName</code> parameter. If you omit <code>TenantName</code>, the operation targets the account-level suppression list.</p>

        Args:
            tenant_name: <p>The name of the tenant whose suppression list you want to retrieve. If you omit this parameter, the operation targets the account-level suppression list.</p>
            reasons: <p>The factors that caused the email address to be added to the suppression list for your account or for a specific tenant.</p>
            start_date: <p>Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list after a specific date.</p>
            end_date: <p>Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list before a specific date.</p>
            next_token: <p>A token returned from a previous call to <code>ListSuppressedDestinations</code> to indicate the position in the list of suppressed email addresses.</p>
            page_size: <p>The number of results to show in a single call to <code>ListSuppressedDestinations</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The specified request includes an invalid or expired token.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_suppressed_destinations_request.ListSuppressedDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_suppressed_destinations_response.ListSuppressedDestinationsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_suppressed_destinations

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_suppressed_destinations.async_list_suppressed_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_suppressed_destinations_request.ListSuppressedDestinationsRequest = {}
        if tenant_name is not None:
            input_["tenant_name"] = tenant_name
        if reasons is not None:
            input_["reasons"] = reasons
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_suppressed_destinations(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tenant_name: Optional["capo_sesv2.types.tenant_name.TenantName"] = None,
        reasons: Optional[
            "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
        ] = None,
        start_date: Optional["capo_sesv2.types.timestamp.Timestamp"] = None,
        end_date: Optional["capo_sesv2.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.list_suppressed_destinations_response.ListSuppressedDestinationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_suppressed_destinations(
                config_overrides=config_overrides,
                tenant_name=tenant_name,
                reasons=reasons,
                start_date=start_date,
                end_date=end_date,
                next_token=_token,
                page_size=page_size,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieve a list of the tags (keys and values) that are associated with a specified resource. A <i>tag</i> is a label that you optionally define and associate with a resource. Each tag consists of a required <i>tag key</i> and an optional associated <i>tag value</i>. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to retrieve tag information for.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tenant_resources(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_tenant_resources_filter.ListTenantResourcesFilter"
        ] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "capo_sesv2.types.list_tenant_resources_response.ListTenantResourcesResponse":
        """<p>List all resources associated with a specific tenant.</p> <p>This operation returns a list of resources (email identities, configuration sets, or email templates) that are associated with the specified tenant. You can optionally filter the results by resource type.</p>

        Args:
            tenant_name: <p>The name of the tenant to list resources for.</p>
            filter: <p>A map of filter keys and values for filtering the list of tenant resources. Currently, the only supported filter key is <code>RESOURCE_TYPE</code>.</p>
            page_size: <p>The number of results to show in a single call to <code>ListTenantResources</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            next_token: <p>A token returned from a previous call to <code>ListTenantResources</code> to indicate the position in the list of tenant resources.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_tenant_resources_request.ListTenantResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_tenant_resources_response.ListTenantResourcesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_tenant_resources

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_tenant_resources.async_list_tenant_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_tenant_resources_request.ListTenantResourcesRequest = {
            "tenant_name": tenant_name
        }
        if filter is not None:
            input_["filter"] = filter
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tenant_resources(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_tenant_resources_filter.ListTenantResourcesFilter"
        ] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.tenant_resource.TenantResource]":
        _token = next_token
        while True:
            _response = await self.list_tenant_resources(
                tenant_name,
                config_overrides=config_overrides,
                filter=filter,
                page_size=page_size,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tenant_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tenants(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_tenants_filter.ListTenantsFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "capo_sesv2.types.list_tenants_response.ListTenantsResponse":
        """<p>List all tenants associated with your account in the current Amazon Web Services Region.</p> <p>This operation returns basic information about each tenant, such as tenant name, ID, ARN, and creation timestamp.</p>

        Args:
            filter: <p>An object that contains filters to apply when listing tenants. You can filter by tenant name or sending status.</p>
            next_token: <p>A token returned from a previous call to <code>ListTenants</code> to indicate the position in the list of tenants.</p>
            page_size: <p>The number of results to show in a single call to <code>ListTenants</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.list_tenants_request.ListTenantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.list_tenants_response.ListTenantsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.list_tenants

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.list_tenants.async_list_tenants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.list_tenants_request.ListTenantsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tenants(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        filter: Optional[
            "capo_sesv2.types.list_tenants_filter.ListTenantsFilter"
        ] = None,
        next_token: Optional["capo_sesv2.types.next_token.NextToken"] = None,
        page_size: Optional["capo_sesv2.types.max_items.MaxItems"] = None,
    ) -> "AsyncIterator[capo_sesv2.types.tenant_info.TenantInfo]":
        _token = next_token
        while True:
            _response = await self.list_tenants(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("tenants",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_account_dedicated_ip_warmup_attributes(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        auto_warmup_enabled: Optional["capo_sesv2.types.enabled.Enabled"] = None,
    ) -> "capo_sesv2.types.put_account_dedicated_ip_warmup_attributes_response.PutAccountDedicatedIpWarmupAttributesResponse":
        """<p>Enable or disable the automatic warm-up feature for dedicated IP addresses.</p>

        Args:
            auto_warmup_enabled: <p>Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon SES account in the current Amazon Web Services Region. Set to <code>true</code> to enable the automatic warm-up feature, or set to <code>false</code> to disable it.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_account_dedicated_ip_warmup_attributes_request.PutAccountDedicatedIpWarmupAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_account_dedicated_ip_warmup_attributes_response.PutAccountDedicatedIpWarmupAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_account_dedicated_ip_warmup_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_account_dedicated_ip_warmup_attributes.async_put_account_dedicated_ip_warmup_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_account_dedicated_ip_warmup_attributes_request.PutAccountDedicatedIpWarmupAttributesRequest = {}
        if auto_warmup_enabled is not None:
            input_["auto_warmup_enabled"] = auto_warmup_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_details(
        self,
        mail_type: "capo_sesv2.types.mail_type.MailType",
        website_url: "capo_sesv2.types.website_url.WebsiteURL",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        contact_language: Optional[
            "capo_sesv2.types.contact_language.ContactLanguage"
        ] = None,
        use_case_description: Optional[
            "capo_sesv2.types.use_case_description.UseCaseDescription"
        ] = None,
        additional_contact_email_addresses: Optional[
            "capo_sesv2.types.additional_contact_email_addresses.AdditionalContactEmailAddresses"
        ] = None,
        production_access_enabled: Optional[
            "capo_sesv2.types.enabled_wrapper.EnabledWrapper"
        ] = None,
    ) -> "capo_sesv2.types.put_account_details_response.PutAccountDetailsResponse":
        """<p>Update your Amazon SES account details.</p>

        Args:
            mail_type: <p>The type of email your account will send.</p>
            website_url: <p>The URL of your website. This information helps us better understand the type of content that you plan to send.</p>
            contact_language: <p>The language you would prefer to be contacted with.</p>
            use_case_description: <p>A description of the types of email that you plan to send.</p>
            additional_contact_email_addresses: <p>Additional email addresses that you would like to be notified regarding Amazon SES matters.</p>
            production_access_enabled: <p>Indicates whether or not your account should have production access in the current Amazon Web Services Region.</p> <p>If the value is <code>false</code>, then your account is in the <i>sandbox</i>. When your account is in the sandbox, you can only send email to verified identities. </p> <p>If the value is <code>true</code>, then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.conflict_exception.ConflictException: <p>If there is already an ongoing account details update under review.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_account_details_request.PutAccountDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_account_details_response.PutAccountDetailsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_account_details

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_account_details.async_put_account_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_account_details_request.PutAccountDetailsRequest = {
            "mail_type": mail_type,
            "website_url": website_url,
        }
        if contact_language is not None:
            input_["contact_language"] = contact_language
        if use_case_description is not None:
            input_["use_case_description"] = use_case_description
        if additional_contact_email_addresses is not None:
            input_["additional_contact_email_addresses"] = (
                additional_contact_email_addresses
            )
        if production_access_enabled is not None:
            input_["production_access_enabled"] = production_access_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_pricing_attributes(
        self,
        plan: "capo_sesv2.types.pricing_plan.PricingPlan",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.put_account_pricing_attributes_response.PutAccountPricingAttributesResponse":
        """<p>Set the pricing plan for your Amazon SES account.</p>

        Args:
            plan: <p>The pricing plan to apply to your Amazon SES account. For details about each plan, see <a href="http://aws.amazon.com/ses/pricing/">Amazon SES Pricing</a>. Can be one of the following:</p> <ul> <li> <p> <code>NONE</code> </p> </li> <li> <p> <code>ESSENTIALS</code> </p> </li> <li> <p> <code>PRO</code> </p> </li> <li> <p> <code>ENTERPRISE</code> </p> </li> </ul>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.conflict_exception.ConflictException: <p>If there is already an ongoing account details update under review.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_account_pricing_attributes_request.PutAccountPricingAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_account_pricing_attributes_response.PutAccountPricingAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_account_pricing_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_account_pricing_attributes.async_put_account_pricing_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_account_pricing_attributes_request.PutAccountPricingAttributesRequest = {
            "plan": plan
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_sending_attributes(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        sending_enabled: Optional["capo_sesv2.types.enabled.Enabled"] = None,
    ) -> "capo_sesv2.types.put_account_sending_attributes_response.PutAccountSendingAttributesResponse":
        """<p>Enable or disable the ability of your account to send email.</p>

        Args:
            sending_enabled: <p>Enables or disables your account's ability to send email. Set to <code>true</code> to enable email sending, or set to <code>false</code> to disable email sending.</p> <note> <p>If Amazon Web Services paused your account's ability to send email, you can't use this operation to resume your account's ability to send email.</p> </note>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_account_sending_attributes_request.PutAccountSendingAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_account_sending_attributes_response.PutAccountSendingAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_account_sending_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_account_sending_attributes.async_put_account_sending_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_account_sending_attributes_request.PutAccountSendingAttributesRequest = {}
        if sending_enabled is not None:
            input_["sending_enabled"] = sending_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_suppression_attributes(
        self,
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        suppressed_reasons: Optional[
            "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
        ] = None,
        validation_attributes: Optional[
            "capo_sesv2.types.suppression_validation_attributes.SuppressionValidationAttributes"
        ] = None,
    ) -> "capo_sesv2.types.put_account_suppression_attributes_response.PutAccountSuppressionAttributesResponse":
        """<p>Change the settings for the account-level suppression list.</p>

        Args:
            suppressed_reasons: <p>A list that contains the reasons that email addresses will be automatically added to the suppression list for your account. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.</p> </li> </ul>
            validation_attributes: <p>An object that contains additional suppression attributes for your account.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_account_suppression_attributes_request.PutAccountSuppressionAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_account_suppression_attributes_response.PutAccountSuppressionAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_account_suppression_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_account_suppression_attributes.async_put_account_suppression_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_account_suppression_attributes_request.PutAccountSuppressionAttributesRequest = {}
        if suppressed_reasons is not None:
            input_["suppressed_reasons"] = suppressed_reasons
        if validation_attributes is not None:
            input_["validation_attributes"] = validation_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_vdm_attributes(
        self,
        vdm_attributes: "capo_sesv2.types.vdm_attributes.VdmAttributes",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.put_account_vdm_attributes_response.PutAccountVdmAttributesResponse":
        """<p>Update your Amazon SES account VDM attributes.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            vdm_attributes: <p>The VDM attributes that you wish to apply to your Amazon SES account.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_account_vdm_attributes_request.PutAccountVdmAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_account_vdm_attributes_response.PutAccountVdmAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_account_vdm_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_account_vdm_attributes.async_put_account_vdm_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_account_vdm_attributes_request.PutAccountVdmAttributesRequest = {
            "vdm_attributes": vdm_attributes
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_archiving_options(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        archive_arn: Optional["capo_sesv2.types.archive_arn.ArchiveArn"] = None,
    ) -> "capo_sesv2.types.put_configuration_set_archiving_options_response.PutConfigurationSetArchivingOptionsResponse":
        """<p>Associate the configuration set with a MailManager archive. When you send email using the <code>SendEmail</code> or <code>SendBulkEmail</code> operations the message as it will be given to the receiving SMTP server will be archived, along with the recipient information.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to associate with a MailManager archive.</p>
            archive_arn: <p>The Amazon Resource Name (ARN) of the MailManager archive that the Amazon SES API v2 sends email to.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Used to associate an MailManager archive with a ConfigurationSet.
            This example associates an archive arn with a configuration set.

            >>> await client.put_configuration_set_archiving_options(configuration_set_name='sample-configuration-name', archive_arn='arn:aws:ses:us-west-2:123456789012:mailmanager-archive/a-abcdefghijklmnopqrstuvwxyz')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_configuration_set_archiving_options_request.PutConfigurationSetArchivingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_configuration_set_archiving_options_response.PutConfigurationSetArchivingOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_configuration_set_archiving_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_configuration_set_archiving_options.async_put_configuration_set_archiving_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_configuration_set_archiving_options_request.PutConfigurationSetArchivingOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if archive_arn is not None:
            input_["archive_arn"] = archive_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_delivery_options(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tls_policy: Optional["capo_sesv2.types.tls_policy.TlsPolicy"] = None,
        sending_pool_name: Optional[
            "capo_sesv2.types.sending_pool_name.SendingPoolName"
        ] = None,
        max_delivery_seconds: Optional[
            "capo_sesv2.types.max_delivery_seconds.MaxDeliverySeconds"
        ] = None,
    ) -> "capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse":
        """<p>Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to associate with a dedicated IP pool.</p>
            tls_policy: <p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>Require</code>, messages are only delivered if a TLS connection can be established. If the value is <code>Optional</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>
            sending_pool_name: <p>The name of the dedicated IP pool to associate with the configuration set.</p>
            max_delivery_seconds: <p>The maximum amount of time, in seconds, that Amazon SES API v2 will attempt delivery of email. If specified, the value must greater than or equal to 300 seconds (5 minutes) and less than or equal to 50400 seconds (840 minutes). </p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_configuration_set_delivery_options_response.PutConfigurationSetDeliveryOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_configuration_set_delivery_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_configuration_set_delivery_options.async_put_configuration_set_delivery_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_configuration_set_delivery_options_request.PutConfigurationSetDeliveryOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if tls_policy is not None:
            input_["tls_policy"] = tls_policy
        if sending_pool_name is not None:
            input_["sending_pool_name"] = sending_pool_name
        if max_delivery_seconds is not None:
            input_["max_delivery_seconds"] = max_delivery_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_reputation_options(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        reputation_metrics_enabled: Optional["capo_sesv2.types.enabled.Enabled"] = None,
    ) -> "capo_sesv2.types.put_configuration_set_reputation_options_response.PutConfigurationSetReputationOptionsResponse":
        """<p>Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific Amazon Web Services Region.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>
            reputation_metrics_enabled: <p>If <code>true</code>, tracking of reputation metrics is enabled for the configuration set. If <code>false</code>, tracking of reputation metrics is disabled for the configuration set.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_configuration_set_reputation_options_request.PutConfigurationSetReputationOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_configuration_set_reputation_options_response.PutConfigurationSetReputationOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_configuration_set_reputation_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_configuration_set_reputation_options.async_put_configuration_set_reputation_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_configuration_set_reputation_options_request.PutConfigurationSetReputationOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if reputation_metrics_enabled is not None:
            input_["reputation_metrics_enabled"] = reputation_metrics_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_sending_options(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        sending_enabled: Optional["capo_sesv2.types.enabled.Enabled"] = None,
    ) -> "capo_sesv2.types.put_configuration_set_sending_options_response.PutConfigurationSetSendingOptionsResponse":
        """<p>Enable or disable email sending for messages that use a particular configuration set in a specific Amazon Web Services Region.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to enable or disable email sending for.</p>
            sending_enabled: <p>If <code>true</code>, email sending is enabled for the configuration set. If <code>false</code>, email sending is disabled for the configuration set.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_configuration_set_sending_options_request.PutConfigurationSetSendingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_configuration_set_sending_options_response.PutConfigurationSetSendingOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_configuration_set_sending_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_configuration_set_sending_options.async_put_configuration_set_sending_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_configuration_set_sending_options_request.PutConfigurationSetSendingOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if sending_enabled is not None:
            input_["sending_enabled"] = sending_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_suppression_options(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        suppression_scope: Optional[
            "capo_sesv2.types.suppression_list_scope.SuppressionListScope"
        ] = None,
        suppressed_reasons: Optional[
            "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
        ] = None,
        validation_options: Optional[
            "capo_sesv2.types.suppression_validation_options.SuppressionValidationOptions"
        ] = None,
    ) -> "capo_sesv2.types.put_configuration_set_suppression_options_response.PutConfigurationSetSuppressionOptionsResponse":
        """<p>Specify the suppression list preferences for a configuration set. You can also use this operation to specify a <code>SuppressionScope</code> to override the suppression scope of the tenant or account for emails sent using this configuration set.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to change the suppression list preferences for.</p>
            suppression_scope: <p>The suppression scope for the configuration set. This overrides the tenant or account suppression scope for emails sent using this configuration set. Can be one of the following:</p> <ul> <li> <p> <code>TENANT</code> – Use the tenant's suppression list.</p> </li> <li> <p> <code>ACCOUNT</code> – Use the account-level suppression list.</p> </li> </ul>
            suppressed_reasons: <p>A list that contains the reasons that email addresses are automatically added to the suppression list for your account or for a specific tenant. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a hard bounce.</p> </li> </ul>
            validation_options: <p>An object that contains information about the email address suppression preferences for the configuration set in the current Amazon Web Services Region.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_configuration_set_suppression_options_request.PutConfigurationSetSuppressionOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_configuration_set_suppression_options_response.PutConfigurationSetSuppressionOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_configuration_set_suppression_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_configuration_set_suppression_options.async_put_configuration_set_suppression_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_configuration_set_suppression_options_request.PutConfigurationSetSuppressionOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if suppression_scope is not None:
            input_["suppression_scope"] = suppression_scope
        if suppressed_reasons is not None:
            input_["suppressed_reasons"] = suppressed_reasons
        if validation_options is not None:
            input_["validation_options"] = validation_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_tracking_options(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        custom_redirect_domain: Optional[
            "capo_sesv2.types.custom_redirect_domain.CustomRedirectDomain"
        ] = None,
        https_policy: Optional["capo_sesv2.types.https_policy.HttpsPolicy"] = None,
    ) -> "capo_sesv2.types.put_configuration_set_tracking_options_response.PutConfigurationSetTrackingOptionsResponse":
        """<p>Specify a custom domain to use for open and click tracking elements in email that you send.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>
            custom_redirect_domain: <p>The domain to use to track open and click events.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_configuration_set_tracking_options_request.PutConfigurationSetTrackingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_configuration_set_tracking_options_response.PutConfigurationSetTrackingOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_configuration_set_tracking_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_configuration_set_tracking_options.async_put_configuration_set_tracking_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_configuration_set_tracking_options_request.PutConfigurationSetTrackingOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if custom_redirect_domain is not None:
            input_["custom_redirect_domain"] = custom_redirect_domain
        if https_policy is not None:
            input_["https_policy"] = https_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_configuration_set_vdm_options(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        vdm_options: Optional["capo_sesv2.types.vdm_options.VdmOptions"] = None,
    ) -> "capo_sesv2.types.put_configuration_set_vdm_options_response.PutConfigurationSetVdmOptionsResponse":
        """<p>Specify VDM preferences for email that you send using the configuration set.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set.</p>
            vdm_options: <p>The VDM options to apply to the configuration set.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_configuration_set_vdm_options_request.PutConfigurationSetVdmOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_configuration_set_vdm_options_response.PutConfigurationSetVdmOptionsResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_configuration_set_vdm_options

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_configuration_set_vdm_options.async_put_configuration_set_vdm_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_configuration_set_vdm_options_request.PutConfigurationSetVdmOptionsRequest = {
            "configuration_set_name": configuration_set_name
        }
        if vdm_options is not None:
            input_["vdm_options"] = vdm_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_dedicated_ip_in_pool(
        self,
        ip: "capo_sesv2.types.ip.Ip",
        destination_pool_name: "capo_sesv2.types.pool_name.PoolName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.put_dedicated_ip_in_pool_response.PutDedicatedIpInPoolResponse":
        """<p>Move a dedicated IP address to an existing dedicated IP pool.</p> <note> <p>The dedicated IP address that you specify must already exist, and must be associated with your Amazon Web Services account. </p> <p>The dedicated IP pool you specify must already exist. You can create a new pool by using the <code>CreateDedicatedIpPool</code> operation.</p> </note>

        Args:
            ip: <p>The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that's associated with your Amazon Web Services account.</p>
            destination_pool_name: <p>The name of the IP pool that you want to add the dedicated IP address to. You have to specify an IP pool that already exists.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_dedicated_ip_in_pool_request.PutDedicatedIpInPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_dedicated_ip_in_pool_response.PutDedicatedIpInPoolResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_dedicated_ip_in_pool

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_dedicated_ip_in_pool.async_put_dedicated_ip_in_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_dedicated_ip_in_pool_request.PutDedicatedIpInPoolRequest = {
            "ip": ip,
            "destination_pool_name": destination_pool_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_dedicated_ip_pool_scaling_attributes(
        self,
        pool_name: "capo_sesv2.types.pool_name.PoolName",
        scaling_mode: "capo_sesv2.types.scaling_mode.ScalingMode",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.put_dedicated_ip_pool_scaling_attributes_response.PutDedicatedIpPoolScalingAttributesResponse":
        """<p>Used to convert a dedicated IP pool to a different scaling mode.</p> <note> <p> <code>MANAGED</code> pools cannot be converted to <code>STANDARD</code> scaling mode.</p> </note>

        Args:
            pool_name: <p>The name of the dedicated IP pool.</p>
            scaling_mode: <p>The scaling mode to apply to the dedicated IP pool.</p> <note> <p>Changing the scaling mode from <code>MANAGED</code> to <code>STANDARD</code> is not supported.</p> </note>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Used to convert a dedicated IP pool to a different scaling mode.
            This example converts a dedicated IP pool from STANDARD to MANAGED.

            >>> await client.put_dedicated_ip_pool_scaling_attributes(pool_name='sample-ses-pool', scaling_mode='MANAGED')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_dedicated_ip_pool_scaling_attributes_request.PutDedicatedIpPoolScalingAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_dedicated_ip_pool_scaling_attributes_response.PutDedicatedIpPoolScalingAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_dedicated_ip_pool_scaling_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_dedicated_ip_pool_scaling_attributes.async_put_dedicated_ip_pool_scaling_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_dedicated_ip_pool_scaling_attributes_request.PutDedicatedIpPoolScalingAttributesRequest = {
            "pool_name": pool_name,
            "scaling_mode": scaling_mode,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_dedicated_ip_warmup_attributes(
        self,
        ip: "capo_sesv2.types.ip.Ip",
        warmup_percentage: "capo_sesv2.types.percentage100_wrapper.Percentage100Wrapper",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.put_dedicated_ip_warmup_attributes_response.PutDedicatedIpWarmupAttributesResponse":
        """<p></p>

        Args:
            ip: <p>The dedicated IP address that you want to update the warm-up attributes for.</p>
            warmup_percentage: <p>The warm-up percentage that you want to associate with the dedicated IP address.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_dedicated_ip_warmup_attributes_request.PutDedicatedIpWarmupAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_dedicated_ip_warmup_attributes_response.PutDedicatedIpWarmupAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_dedicated_ip_warmup_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_dedicated_ip_warmup_attributes.async_put_dedicated_ip_warmup_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_dedicated_ip_warmup_attributes_request.PutDedicatedIpWarmupAttributesRequest = {
            "ip": ip,
            "warmup_percentage": warmup_percentage,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_deliverability_dashboard_option(
        self,
        dashboard_enabled: "capo_sesv2.types.enabled.Enabled",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        subscribed_domains: Optional[
            "capo_sesv2.types.domain_deliverability_tracking_options.DomainDeliverabilityTrackingOptions"
        ] = None,
    ) -> "capo_sesv2.types.put_deliverability_dashboard_option_response.PutDeliverabilityDashboardOptionResponse":
        """<p>Enable or disable the Deliverability dashboard. When you enable the Deliverability dashboard, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.</p> <p>When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other Amazon Web Services services. For more information about the features and cost of a Deliverability dashboard subscription, see <a href="http://aws.amazon.com/ses/pricing/">Amazon SES Pricing</a>.</p>

        Args:
            dashboard_enabled: <p>Specifies whether to enable the Deliverability dashboard. To enable the dashboard, set this value to <code>true</code>.</p>
            subscribed_domains: <p>An array of objects, one for each verified domain that you use to send email and enabled the Deliverability dashboard for.</p>

        Raises:
            capo_sesv2.errors.already_exists_exception.AlreadyExistsException: <p>The resource specified in your request already exists.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_deliverability_dashboard_option_request.PutDeliverabilityDashboardOptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_deliverability_dashboard_option_response.PutDeliverabilityDashboardOptionResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_deliverability_dashboard_option

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_deliverability_dashboard_option.async_put_deliverability_dashboard_option(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_deliverability_dashboard_option_request.PutDeliverabilityDashboardOptionRequest = {
            "dashboard_enabled": dashboard_enabled
        }
        if subscribed_domains is not None:
            input_["subscribed_domains"] = subscribed_domains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_configuration_set_attributes(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        configuration_set_name: Optional[
            "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
        ] = None,
    ) -> "capo_sesv2.types.put_email_identity_configuration_set_attributes_response.PutEmailIdentityConfigurationSetAttributesResponse":
        """<p>Used to associate a configuration set with an email identity.</p>

        Args:
            email_identity: <p>The email address or domain to associate with a configuration set.</p>
            configuration_set_name: <p>The configuration set to associate with an email identity.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_email_identity_configuration_set_attributes_request.PutEmailIdentityConfigurationSetAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_email_identity_configuration_set_attributes_response.PutEmailIdentityConfigurationSetAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_email_identity_configuration_set_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_email_identity_configuration_set_attributes.async_put_email_identity_configuration_set_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_email_identity_configuration_set_attributes_request.PutEmailIdentityConfigurationSetAttributesRequest = {
            "email_identity": email_identity
        }
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_dkim_attributes(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        signing_enabled: Optional["capo_sesv2.types.enabled.Enabled"] = None,
    ) -> "capo_sesv2.types.put_email_identity_dkim_attributes_response.PutEmailIdentityDkimAttributesResponse":
        """<p>Used to enable or disable DKIM authentication for an email identity.</p>

        Args:
            email_identity: <p>The email identity.</p>
            signing_enabled: <p>Sets the DKIM signing configuration for the identity.</p> <p>When you set this value <code>true</code>, then the messages that are sent from the identity are signed using DKIM. If you set this value to <code>false</code>, your messages are sent without DKIM signing.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_email_identity_dkim_attributes_request.PutEmailIdentityDkimAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_email_identity_dkim_attributes_response.PutEmailIdentityDkimAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_email_identity_dkim_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_email_identity_dkim_attributes.async_put_email_identity_dkim_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_email_identity_dkim_attributes_request.PutEmailIdentityDkimAttributesRequest = {
            "email_identity": email_identity
        }
        if signing_enabled is not None:
            input_["signing_enabled"] = signing_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_dkim_signing_attributes(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        signing_attributes_origin: "capo_sesv2.types.dkim_signing_attributes_origin.DkimSigningAttributesOrigin",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        signing_attributes: Optional[
            "capo_sesv2.types.dkim_signing_attributes.DkimSigningAttributes"
        ] = None,
    ) -> "capo_sesv2.types.put_email_identity_dkim_signing_attributes_response.PutEmailIdentityDkimSigningAttributesResponse":
        """<p>Used to configure or change the DKIM authentication settings for an email domain identity. You can use this operation to do any of the following:</p> <ul> <li> <p>Update the signing attributes for an identity that uses Bring Your Own DKIM (BYODKIM).</p> </li> <li> <p>Update the key length that should be used for Easy DKIM.</p> </li> <li> <p>Change from using no DKIM authentication to using Easy DKIM.</p> </li> <li> <p>Change from using no DKIM authentication to using BYODKIM.</p> </li> <li> <p>Change from using Easy DKIM to using BYODKIM.</p> </li> <li> <p>Change from using BYODKIM to using Easy DKIM.</p> </li> </ul>

        Args:
            email_identity: <p>The email identity.</p>
            signing_attributes_origin: <p>The method to use to configure DKIM for the identity. There are the following possible values:</p> <ul> <li> <p> <code>AWS_SES</code> – Configure DKIM for the identity by using <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p> </li> <li> <p> <code>EXTERNAL</code> – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).</p> </li> </ul>
            signing_attributes: <p>An object that contains information about the private key and selector that you want to use to configure DKIM for the identity for Bring Your Own DKIM (BYODKIM) for the identity, or, configures the key length to be used for <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html">Easy DKIM</a>.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_email_identity_dkim_signing_attributes_request.PutEmailIdentityDkimSigningAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_email_identity_dkim_signing_attributes_response.PutEmailIdentityDkimSigningAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_email_identity_dkim_signing_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_email_identity_dkim_signing_attributes.async_put_email_identity_dkim_signing_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_email_identity_dkim_signing_attributes_request.PutEmailIdentityDkimSigningAttributesRequest = {
            "email_identity": email_identity,
            "signing_attributes_origin": signing_attributes_origin,
        }
        if signing_attributes is not None:
            input_["signing_attributes"] = signing_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_feedback_attributes(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        email_forwarding_enabled: Optional["capo_sesv2.types.enabled.Enabled"] = None,
    ) -> "capo_sesv2.types.put_email_identity_feedback_attributes_response.PutEmailIdentityFeedbackAttributesResponse":
        """<p>Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.</p> <p>If the value is <code>true</code>, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the <code>Return-Path</code> header of the original email.</p> <p>You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).</p>

        Args:
            email_identity: <p>The email identity.</p>
            email_forwarding_enabled: <p>Sets the feedback forwarding configuration for the identity.</p> <p>If the value is <code>true</code>, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the <code>Return-Path</code> header of the original email.</p> <p>You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_email_identity_feedback_attributes_request.PutEmailIdentityFeedbackAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_email_identity_feedback_attributes_response.PutEmailIdentityFeedbackAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_email_identity_feedback_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_email_identity_feedback_attributes.async_put_email_identity_feedback_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_email_identity_feedback_attributes_request.PutEmailIdentityFeedbackAttributesRequest = {
            "email_identity": email_identity
        }
        if email_forwarding_enabled is not None:
            input_["email_forwarding_enabled"] = email_forwarding_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_email_identity_mail_from_attributes(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        mail_from_domain: Optional[
            "capo_sesv2.types.mail_from_domain_name.MailFromDomainName"
        ] = None,
        behavior_on_mx_failure: Optional[
            "capo_sesv2.types.behavior_on_mx_failure.BehaviorOnMxFailure"
        ] = None,
    ) -> "capo_sesv2.types.put_email_identity_mail_from_attributes_response.PutEmailIdentityMailFromAttributesResponse":
        """<p>Used to enable or disable the custom Mail-From domain configuration for an email identity.</p>

        Args:
            email_identity: <p>The verified email identity.</p>
            mail_from_domain: <p> The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria:</p> <ul> <li> <p>It has to be a subdomain of the verified identity.</p> </li> <li> <p>It can't be used to receive email.</p> </li> <li> <p>It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails.</p> </li> </ul>
            behavior_on_mx_failure: <p>The action to take if the required MX record isn't found when you send an email. When you set this value to <code>UseDefaultValue</code>, the mail is sent using <i>amazonses.com</i> as the MAIL FROM domain. When you set this value to <code>RejectMessage</code>, the Amazon SES API v2 returns a <code>MailFromDomainNotVerified</code> error, and doesn't attempt to deliver the email.</p> <p>These behaviors are taken when the custom MAIL FROM domain configuration is in the <code>Pending</code>, <code>Failed</code>, and <code>TemporaryFailure</code> states.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_email_identity_mail_from_attributes_request.PutEmailIdentityMailFromAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_email_identity_mail_from_attributes_response.PutEmailIdentityMailFromAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_email_identity_mail_from_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_email_identity_mail_from_attributes.async_put_email_identity_mail_from_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_email_identity_mail_from_attributes_request.PutEmailIdentityMailFromAttributesRequest = {
            "email_identity": email_identity
        }
        if mail_from_domain is not None:
            input_["mail_from_domain"] = mail_from_domain
        if behavior_on_mx_failure is not None:
            input_["behavior_on_mx_failure"] = behavior_on_mx_failure

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_suppressed_destination(
        self,
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        reason: "capo_sesv2.types.suppression_list_reason.SuppressionListReason",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        tenant_name: Optional["capo_sesv2.types.tenant_name.TenantName"] = None,
    ) -> "capo_sesv2.types.put_suppressed_destination_response.PutSuppressedDestinationResponse":
        """<p>Adds an email address to the suppression list for your account or for a specific tenant. To target a tenant's suppression list, specify the <code>TenantName</code> parameter. If you omit <code>TenantName</code>, the address is added to the account-level suppression list.</p>

        Args:
            email_address: <p>The email address that should be added to the suppression list for your account or for the specified tenant.</p>
            reason: <p>The factors that should cause the email address to be added to the suppression list for your account or for the specified tenant.</p>
            tenant_name: <p>The name of the tenant whose suppression list you want to add the address to. If you omit this parameter, the address is added to the account-level suppression list.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_suppressed_destination_request.PutSuppressedDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_suppressed_destination_response.PutSuppressedDestinationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_suppressed_destination

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_suppressed_destination.async_put_suppressed_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_suppressed_destination_request.PutSuppressedDestinationRequest = {
            "email_address": email_address,
            "reason": reason,
        }
        if tenant_name is not None:
            input_["tenant_name"] = tenant_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_tenant_suppression_attributes(
        self,
        tenant_name: "capo_sesv2.types.tenant_name.TenantName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        suppressed_reasons: Optional[
            "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
        ] = None,
        suppression_scope: Optional[
            "capo_sesv2.types.suppression_list_scope.SuppressionListScope"
        ] = None,
    ) -> "capo_sesv2.types.put_tenant_suppression_attributes_response.PutTenantSuppressionAttributesResponse":
        """<p>Configure the suppression list preferences for a tenant. Use this operation to enable or disable tenant-level suppression, or to change the suppressed reasons for a tenant.</p> <p>When you set the suppression scope to <code>TENANT</code>, Amazon SES maintains a separate suppression list for the tenant. When you set the scope to <code>ACCOUNT</code>, the tenant uses the account-level suppression list.</p>

        Args:
            tenant_name: <p>The name of the tenant to configure suppression list preferences for.</p>
            suppressed_reasons: <p>A list that contains the reasons that email addresses are automatically added to the suppression list for the tenant. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a hard bounce.</p> </li> </ul>
            suppression_scope: <p>The suppression scope for the tenant. Specify <code>TENANT</code> to use the tenant's own suppression list, or <code>ACCOUNT</code> to use the account-level suppression list.</p> <note> <p>If you don't specify a suppression scope, the tenant defaults to <code>ACCOUNT</code> scope and uses the account-level suppression list.</p> </note>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.put_tenant_suppression_attributes_request.PutTenantSuppressionAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.put_tenant_suppression_attributes_response.PutTenantSuppressionAttributesResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.put_tenant_suppression_attributes

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.put_tenant_suppression_attributes.async_put_tenant_suppression_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.put_tenant_suppression_attributes_request.PutTenantSuppressionAttributesRequest = {
            "tenant_name": tenant_name
        }
        if suppressed_reasons is not None:
            input_["suppressed_reasons"] = suppressed_reasons
        if suppression_scope is not None:
            input_["suppression_scope"] = suppression_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_bulk_email(
        self,
        default_content: "capo_sesv2.types.bulk_email_content.BulkEmailContent",
        bulk_email_entries: "capo_sesv2.types.bulk_email_entry_list.BulkEmailEntryList",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        from_email_address: Optional[
            "capo_sesv2.types.email_address.EmailAddress"
        ] = None,
        from_email_address_identity_arn: Optional[
            "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        reply_to_addresses: Optional[
            "capo_sesv2.types.email_address_list.EmailAddressList"
        ] = None,
        feedback_forwarding_email_address: Optional[
            "capo_sesv2.types.email_address.EmailAddress"
        ] = None,
        feedback_forwarding_email_address_identity_arn: Optional[
            "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        default_email_tags: Optional[
            "capo_sesv2.types.message_tag_list.MessageTagList"
        ] = None,
        configuration_set_name: Optional[
            "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
        ] = None,
        endpoint_id: Optional["capo_sesv2.types.endpoint_id.EndpointId"] = None,
        tenant_name: Optional["capo_sesv2.types.tenant_name.TenantName"] = None,
        configuration_overrides: Optional[
            "capo_sesv2.types.configuration_overrides.ConfigurationOverrides"
        ] = None,
    ) -> "capo_sesv2.types.send_bulk_email_response.SendBulkEmailResponse":
        """<p>Composes an email message to multiple destinations.</p>

        Args:
            from_email_address: <p>The email address to use as the "From" address for the email. The address that you specify has to be verified.</p>
            from_email_address_identity_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>FromEmailAddress</code> parameter.</p> <p>For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use sender@example.com, then you would specify the <code>FromEmailAddressIdentityArn</code> to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the <code>FromEmailAddress</code> to be sender@example.com.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            reply_to_addresses: <p>The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.</p>
            feedback_forwarding_email_address: <p>The address that you want bounce and complaint notifications to be sent to.</p>
            feedback_forwarding_email_address_identity_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>FeedbackForwardingEmailAddress</code> parameter.</p> <p>For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the <code>FeedbackForwardingEmailAddressIdentityArn</code> to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the <code>FeedbackForwardingEmailAddress</code> to be feedback@example.com.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            default_email_tags: <p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.</p>
            default_content: <p>An object that contains the body of the message. You can specify a template message.</p>
            bulk_email_entries: <p>The list of bulk email entry objects.</p>
            configuration_set_name: <p>The name of the configuration set to use when sending the email.</p>
            endpoint_id: <p>The ID of the multi-region endpoint (global-endpoint).</p>
            tenant_name: <p>The name of the tenant through which this bulk email will be sent.</p> <note> <p> The email sending operation will only succeed if all referenced resources (identities, configuration sets, and templates) are associated with this tenant. </p> </note>
            configuration_overrides: <p>An object that overrides, for the messages in this request only, settings that would otherwise apply to them. The overrides apply to every message in the request. Each setting that you don't override keeps the value that already applies.</p>

        Raises:
            capo_sesv2.errors.account_suspended_exception.AccountSuspendedException: <p>The message can't be sent because the account's ability to send email has been permanently restricted.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p>The message can't be sent because the sending domain isn't verified.</p>
            capo_sesv2.errors.message_rejected.MessageRejected: <p>The message can't be sent because it contains invalid content.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.sending_paused_exception.SendingPausedException: <p>The message can't be sent because the account's ability to send email is currently paused.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.send_bulk_email_request.SendBulkEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.send_bulk_email_response.SendBulkEmailResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.send_bulk_email

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.send_bulk_email.async_send_bulk_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.send_bulk_email_request.SendBulkEmailRequest = {
            "default_content": default_content,
            "bulk_email_entries": bulk_email_entries,
        }
        if from_email_address is not None:
            input_["from_email_address"] = from_email_address
        if from_email_address_identity_arn is not None:
            input_["from_email_address_identity_arn"] = from_email_address_identity_arn
        if reply_to_addresses is not None:
            input_["reply_to_addresses"] = reply_to_addresses
        if feedback_forwarding_email_address is not None:
            input_["feedback_forwarding_email_address"] = (
                feedback_forwarding_email_address
            )
        if feedback_forwarding_email_address_identity_arn is not None:
            input_["feedback_forwarding_email_address_identity_arn"] = (
                feedback_forwarding_email_address_identity_arn
            )
        if default_email_tags is not None:
            input_["default_email_tags"] = default_email_tags
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if endpoint_id is not None:
            input_["endpoint_id"] = endpoint_id
        if tenant_name is not None:
            input_["tenant_name"] = tenant_name
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_custom_verification_email(
        self,
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        configuration_set_name: Optional[
            "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
        ] = None,
    ) -> "capo_sesv2.types.send_custom_verification_email_response.SendCustomVerificationEmailResponse":
        """<p>Adds an email address to the list of identities for your Amazon SES account in the current Amazon Web Services Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.</p> <p>To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using custom verification email templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            email_address: <p>The email address to verify.</p>
            template_name: <p>The name of the custom verification email template to use when sending the verification email.</p>
            configuration_set_name: <p>Name of a configuration set to use when sending the verification email.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p>The message can't be sent because the sending domain isn't verified.</p>
            capo_sesv2.errors.message_rejected.MessageRejected: <p>The message can't be sent because it contains invalid content.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.sending_paused_exception.SendingPausedException: <p>The message can't be sent because the account's ability to send email is currently paused.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.send_custom_verification_email_request.SendCustomVerificationEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.send_custom_verification_email_response.SendCustomVerificationEmailResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.send_custom_verification_email

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.send_custom_verification_email.async_send_custom_verification_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.send_custom_verification_email_request.SendCustomVerificationEmailRequest = {
            "email_address": email_address,
            "template_name": template_name,
        }
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_email(
        self,
        content: "capo_sesv2.types.email_content.EmailContent",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        from_email_address: Optional[
            "capo_sesv2.types.email_address.EmailAddress"
        ] = None,
        from_email_address_identity_arn: Optional[
            "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        destination: Optional["capo_sesv2.types.destination.Destination"] = None,
        reply_to_addresses: Optional[
            "capo_sesv2.types.email_address_list.EmailAddressList"
        ] = None,
        feedback_forwarding_email_address: Optional[
            "capo_sesv2.types.email_address.EmailAddress"
        ] = None,
        feedback_forwarding_email_address_identity_arn: Optional[
            "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        email_tags: Optional["capo_sesv2.types.message_tag_list.MessageTagList"] = None,
        configuration_set_name: Optional[
            "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
        ] = None,
        endpoint_id: Optional["capo_sesv2.types.endpoint_id.EndpointId"] = None,
        tenant_name: Optional["capo_sesv2.types.tenant_name.TenantName"] = None,
        list_management_options: Optional[
            "capo_sesv2.types.list_management_options.ListManagementOptions"
        ] = None,
        configuration_overrides: Optional[
            "capo_sesv2.types.configuration_overrides.ConfigurationOverrides"
        ] = None,
    ) -> "capo_sesv2.types.send_email_response.SendEmailResponse":
        """<p>Sends an email message. You can use the Amazon SES API v2 to send the following types of messages:</p> <ul> <li> <p> <b>Simple</b> – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon SES assembles the message for you.</p> </li> <li> <p> <b>Raw</b> – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.</p> </li> <li> <p> <b>Templated</b> – A message that contains personalization tags. When you send this type of email, Amazon SES API v2 automatically replaces the tags with values that you specify.</p> </li> </ul>

        Args:
            from_email_address: <p>The email address to use as the "From" address for the email. The address that you specify has to be verified. </p>
            from_email_address_identity_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>FromEmailAddress</code> parameter.</p> <p>For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use sender@example.com, then you would specify the <code>FromEmailAddressIdentityArn</code> to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the <code>FromEmailAddress</code> to be sender@example.com.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>For Raw emails, the <code>FromEmailAddressIdentityArn</code> value overrides the X-SES-SOURCE-ARN and X-SES-FROM-ARN headers specified in raw email message content.</p>
            destination: <p>An object that contains the recipients of the email message.</p>
            reply_to_addresses: <p>The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.</p>
            feedback_forwarding_email_address: <p>The address that you want bounce and complaint notifications to be sent to.</p>
            feedback_forwarding_email_address_identity_arn: <p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the <code>FeedbackForwardingEmailAddress</code> parameter.</p> <p>For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the <code>FeedbackForwardingEmailAddressIdentityArn</code> to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the <code>FeedbackForwardingEmailAddress</code> to be feedback@example.com.</p> <p>For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p>
            content: <p>An object that contains the body of the message. You can send either a Simple message, Raw message, or a Templated message.</p>
            email_tags: <p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. </p>
            configuration_set_name: <p>The name of the configuration set to use when sending the email.</p>
            endpoint_id: <p>The ID of the multi-region endpoint (global-endpoint).</p>
            tenant_name: <p>The name of the tenant through which this email will be sent.</p> <note> <p>The email sending operation will only succeed if all referenced resources (identities, configuration sets, and templates) are associated with this tenant. </p> </note>
            list_management_options: <p>An object used to specify a list or topic to which an email belongs, which will be used when a contact chooses to unsubscribe.</p>
            configuration_overrides: <p>An object that overrides, for this message only, settings that would otherwise apply to it. Each setting that you don't override keeps the value that already applies.</p>

        Raises:
            capo_sesv2.errors.account_suspended_exception.AccountSuspendedException: <p>The message can't be sent because the account's ability to send email has been permanently restricted.</p>
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.limit_exceeded_exception.LimitExceededException: <p>There are too many instances of the specified resource type.</p>
            capo_sesv2.errors.mail_from_domain_not_verified_exception.MailFromDomainNotVerifiedException: <p>The message can't be sent because the sending domain isn't verified.</p>
            capo_sesv2.errors.message_rejected.MessageRejected: <p>The message can't be sent because it contains invalid content.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.sending_paused_exception.SendingPausedException: <p>The message can't be sent because the account's ability to send email is currently paused.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.send_email_request.SendEmailRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.send_email_response.SendEmailResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.send_email

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.send_email.async_send_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.send_email_request.SendEmailRequest = {
            "content": content
        }
        if from_email_address is not None:
            input_["from_email_address"] = from_email_address
        if from_email_address_identity_arn is not None:
            input_["from_email_address_identity_arn"] = from_email_address_identity_arn
        if destination is not None:
            input_["destination"] = destination
        if reply_to_addresses is not None:
            input_["reply_to_addresses"] = reply_to_addresses
        if feedback_forwarding_email_address is not None:
            input_["feedback_forwarding_email_address"] = (
                feedback_forwarding_email_address
            )
        if feedback_forwarding_email_address_identity_arn is not None:
            input_["feedback_forwarding_email_address_identity_arn"] = (
                feedback_forwarding_email_address_identity_arn
            )
        if email_tags is not None:
            input_["email_tags"] = email_tags
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if endpoint_id is not None:
            input_["endpoint_id"] = endpoint_id
        if tenant_name is not None:
            input_["tenant_name"] = tenant_name
        if list_management_options is not None:
            input_["list_management_options"] = list_management_options
        if configuration_overrides is not None:
            input_["configuration_overrides"] = configuration_overrides

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_sesv2.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.tag_resource_response.TagResourceResponse":
        """<p>Add one or more tags (keys and values) to a specified resource. A <i>tag</i> is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.</p> <p>Each tag consists of a required <i>tag key</i> and an associated <i>tag value</i>, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add one or more tags to.</p>
            tags: <p>A list of the tags that you want to add to the resource. A tag consists of a required tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.tag_resource

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.tag_resource_request.TagResourceRequest = {
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

    async def test_render_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        template_data: "capo_sesv2.types.email_template_data.EmailTemplateData",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.test_render_email_template_response.TestRenderEmailTemplateResponse":
        """<p>Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the template.</p>
            template_data: <p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.test_render_email_template_request.TestRenderEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.test_render_email_template_response.TestRenderEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.test_render_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.test_render_email_template.async_test_render_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.test_render_email_template_request.TestRenderEmailTemplateRequest = {
            "template_name": template_name,
            "template_data": template_data,
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
        resource_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_sesv2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove one or more tags (keys and values) from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.</p>
            tag_keys: <p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the resource, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. For example: <code>/v2/email/tags?ResourceArn=ResourceArn&TagKeys=Key1&TagKeys=Key2</code> </p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.untag_resource

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_set(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        message_security_options: Optional[
            "capo_sesv2.types.message_security_options.MessageSecurityOptions"
        ] = None,
    ) -> "capo_sesv2.types.update_configuration_set_response.UpdateConfigurationSetResponse":
        """<p>Updates an existing configuration set.</p> <p>This operation performs a partial update. Only the attributes that you include in the request are updated; any omitted attribute is left unchanged.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set to update.</p>
            message_security_options: <p>The security options that apply to the MIME message itself for messages sent with the configuration set.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_configuration_set_request.UpdateConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_configuration_set_response.UpdateConfigurationSetResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_configuration_set

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_configuration_set.async_update_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_configuration_set_request.UpdateConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }
        if message_security_options is not None:
            input_["message_security_options"] = message_security_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_sesv2.types.configuration_set_name.ConfigurationSetName",
        event_destination_name: "capo_sesv2.types.event_destination_name.EventDestinationName",
        event_destination: "capo_sesv2.types.event_destination_definition.EventDestinationDefinition",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse":
        """<p>Update the configuration of an event destination for a configuration set.</p> <p> <i>Events</i> include message sends, deliveries, opens, clicks, bounces, and complaints. <i>Event destinations</i> are places that you can send information about these events to. For example, you can send event data to Amazon EventBridge and associate a rule to send the event to the specified target.</p>

        Args:
            configuration_set_name: <p>The name of the configuration set that contains the event destination to modify.</p>
            event_destination_name: <p>The name of the event destination.</p>
            event_destination: <p>An object that defines the event destination.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_configuration_set_event_destination.async_update_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
            "event_destination": event_destination,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_contact(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        email_address: "capo_sesv2.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        topic_preferences: Optional[
            "capo_sesv2.types.topic_preference_list.TopicPreferenceList"
        ] = None,
        unsubscribe_all: Optional[
            "capo_sesv2.types.unsubscribe_all.UnsubscribeAll"
        ] = None,
        attributes_data: Optional[
            "capo_sesv2.types.attributes_data.AttributesData"
        ] = None,
    ) -> "capo_sesv2.types.update_contact_response.UpdateContactResponse":
        """<p>Updates a contact's preferences for a list.</p> <note> <p>You must specify all existing topic preferences in the <code>TopicPreferences</code> object, not just the ones that need updating; otherwise, all your existing preferences will be removed.</p> </note>

        Args:
            contact_list_name: <p>The name of the contact list.</p>
            email_address: <p>The contact's email address.</p>
            topic_preferences: <p>The contact's preference for being opted-in to or opted-out of a topic.</p>
            unsubscribe_all: <p>A boolean value status noting if the contact is unsubscribed from all contact list topics.</p>
            attributes_data: <p>The attribute data attached to a contact.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_contact_request.UpdateContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_contact_response.UpdateContactResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_contact

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_contact.async_update_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_contact_request.UpdateContactRequest = {
            "contact_list_name": contact_list_name,
            "email_address": email_address,
        }
        if topic_preferences is not None:
            input_["topic_preferences"] = topic_preferences
        if unsubscribe_all is not None:
            input_["unsubscribe_all"] = unsubscribe_all
        if attributes_data is not None:
            input_["attributes_data"] = attributes_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_contact_list(
        self,
        contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
        topics: Optional["capo_sesv2.types.topics.Topics"] = None,
        description: Optional["capo_sesv2.types.description.Description"] = None,
    ) -> "capo_sesv2.types.update_contact_list_response.UpdateContactListResponse":
        """<p>Updates contact list metadata. This operation does a complete replacement.</p>

        Args:
            contact_list_name: <p>The name of the contact list.</p>
            topics: <p>An interest group, theme, or label within a list. A contact list can have multiple topics.</p>
            description: <p>A description of what the contact list is about.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is being modified by another operation or thread.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_contact_list_request.UpdateContactListRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_contact_list_response.UpdateContactListResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_contact_list

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_contact_list.async_update_contact_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_contact_list_request.UpdateContactListRequest = {
            "contact_list_name": contact_list_name
        }
        if topics is not None:
            input_["topics"] = topics
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_custom_verification_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        from_email_address: "capo_sesv2.types.email_address.EmailAddress",
        template_subject: "capo_sesv2.types.email_template_subject.EmailTemplateSubject",
        template_content: "capo_sesv2.types.template_content.TemplateContent",
        success_redirection_url: "capo_sesv2.types.success_redirection_url.SuccessRedirectionURL",
        failure_redirection_url: "capo_sesv2.types.failure_redirection_url.FailureRedirectionURL",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.update_custom_verification_email_template_response.UpdateCustomVerificationEmailTemplateResponse":
        """<p>Updates an existing custom verification email template.</p> <p>For more information about custom verification email templates, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom">Using custom verification email templates</a> in the <i>Amazon SES Developer Guide</i>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the custom verification email template that you want to update.</p>
            from_email_address: <p>The email address that the custom verification email is sent from.</p>
            template_subject: <p>The subject line of the custom verification email.</p>
            template_content: <p>The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom-faq">Custom verification email frequently asked questions</a> in the <i>Amazon SES Developer Guide</i>.</p>
            success_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>
            failure_redirection_url: <p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_custom_verification_email_template_request.UpdateCustomVerificationEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_custom_verification_email_template_response.UpdateCustomVerificationEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_custom_verification_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_custom_verification_email_template.async_update_custom_verification_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_custom_verification_email_template_request.UpdateCustomVerificationEmailTemplateRequest = {
            "template_name": template_name,
            "from_email_address": from_email_address,
            "template_subject": template_subject,
            "template_content": template_content,
            "success_redirection_url": success_redirection_url,
            "failure_redirection_url": failure_redirection_url,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_email_identity_policy(
        self,
        email_identity: "capo_sesv2.types.identity.Identity",
        policy_name: "capo_sesv2.types.policy_name.PolicyName",
        policy: "capo_sesv2.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.update_email_identity_policy_response.UpdateEmailIdentityPolicyResponse":
        """<p>Updates the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.</p> <note> <p>This API is for the identity owner only. If you have not verified the identity, this API will return an error.</p> </note> <p>Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            email_identity: <p>The email identity.</p>
            policy_name: <p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>
            policy: <p>The text of the policy in JSON format. The policy cannot exceed 4 KB.</p> <p> For information about the syntax of sending authorization policies, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html">Amazon SES Developer Guide</a>.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_email_identity_policy_request.UpdateEmailIdentityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_email_identity_policy_response.UpdateEmailIdentityPolicyResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_email_identity_policy

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_email_identity_policy.async_update_email_identity_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_email_identity_policy_request.UpdateEmailIdentityPolicyRequest = {
            "email_identity": email_identity,
            "policy_name": policy_name,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_email_template(
        self,
        template_name: "capo_sesv2.types.email_template_name.EmailTemplateName",
        template_content: "capo_sesv2.types.email_template_content.EmailTemplateContent",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.update_email_template_response.UpdateEmailTemplateResponse":
        """<p>Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html">Amazon SES Developer Guide</a>.</p> <p>You can execute this operation no more than once per second.</p>

        Args:
            template_name: <p>The name of the template.</p>
            template_content: <p>The content of the email template, composed of a subject line, an HTML part, and a text-only part.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.not_found_exception.NotFoundException: <p>The resource you attempted to access doesn't exist.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_email_template_request.UpdateEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_email_template_response.UpdateEmailTemplateResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_email_template

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_email_template.async_update_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_email_template_request.UpdateEmailTemplateRequest = {
            "template_name": template_name,
            "template_content": template_content,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_reputation_entity_customer_managed_status(
        self,
        reputation_entity_type: "capo_sesv2.types.reputation_entity_type.ReputationEntityType",
        reputation_entity_reference: "capo_sesv2.types.reputation_entity_reference.ReputationEntityReference",
        sending_status: "capo_sesv2.types.sending_status.SendingStatus",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.update_reputation_entity_customer_managed_status_response.UpdateReputationEntityCustomerManagedStatusResponse":
        """<p>Update the customer-managed sending status for a reputation entity. This allows you to enable, disable, or reinstate sending for the entity.</p> <p>The customer-managed status works in conjunction with the Amazon Web Services Amazon SES-managed status to determine the overall sending capability. When you update the customer-managed status, the Amazon Web Services Amazon SES-managed status remains unchanged. If Amazon Web Services Amazon SES has disabled the entity, it will not be allowed to send regardless of the customer-managed status setting. When you reinstate an entity through the customer-managed status, it can continue sending only if the Amazon Web Services Amazon SES-managed status also permits sending, even if there are active reputation findings, until the findings are resolved or new violations occur.</p>

        Args:
            reputation_entity_type: <p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>
            reputation_entity_reference: <p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>
            sending_status: <p>The new customer-managed sending status for the reputation entity. This can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Allow sending for this entity.</p> </li> <li> <p> <code>DISABLED</code> – Prevent sending for this entity.</p> </li> <li> <p> <code>REINSTATED</code> – Allow sending even if there are active reputation findings.</p> </li> </ul>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.conflict_exception.ConflictException: <p>If there is already an ongoing account details update under review.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_reputation_entity_customer_managed_status_request.UpdateReputationEntityCustomerManagedStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_reputation_entity_customer_managed_status_response.UpdateReputationEntityCustomerManagedStatusResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_reputation_entity_customer_managed_status

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_reputation_entity_customer_managed_status.async_update_reputation_entity_customer_managed_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_reputation_entity_customer_managed_status_request.UpdateReputationEntityCustomerManagedStatusRequest = {
            "reputation_entity_type": reputation_entity_type,
            "reputation_entity_reference": reputation_entity_reference,
            "sending_status": sending_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_reputation_entity_policy(
        self,
        reputation_entity_type: "capo_sesv2.types.reputation_entity_type.ReputationEntityType",
        reputation_entity_reference: "capo_sesv2.types.reputation_entity_reference.ReputationEntityReference",
        reputation_entity_policy: "capo_sesv2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSESv2ClientConfig] = None,
    ) -> "capo_sesv2.types.update_reputation_entity_policy_response.UpdateReputationEntityPolicyResponse":
        """<p>Update the reputation management policy for a reputation entity. The policy determines how the entity responds to reputation findings, such as automatically pausing sending when certain thresholds are exceeded.</p> <p>Reputation management policies are Amazon Web Services Amazon SES-managed (predefined policies). You can select from none, standard, and strict policies.</p>

        Args:
            reputation_entity_type: <p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>
            reputation_entity_reference: <p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>
            reputation_entity_policy: <p>The Amazon Resource Name (ARN) of the reputation management policy to apply to this entity. This is an Amazon Web Services Amazon SES-managed policy.</p>

        Raises:
            capo_sesv2.errors.bad_request_exception.BadRequestException: <p>The input you provided is invalid.</p>
            capo_sesv2.errors.conflict_exception.ConflictException: <p>If there is already an ongoing account details update under review.</p>
            capo_sesv2.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many requests have been made to the operation.</p>
            capo_sesv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sesv2.types.update_reputation_entity_policy_request.UpdateReputationEntityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_sesv2.types.update_reputation_entity_policy_response.UpdateReputationEntityPolicyResponse"
        ]:
            import capo_sesv2._operations.simple_email_service_v2.update_reputation_entity_policy

            (
                output,
                http_response,
            ) = await capo_sesv2._operations.simple_email_service_v2.update_reputation_entity_policy.async_update_reputation_entity_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sesv2.types.update_reputation_entity_policy_request.UpdateReputationEntityPolicyRequest = {
            "reputation_entity_type": reputation_entity_type,
            "reputation_entity_reference": reputation_entity_reference,
            "reputation_entity_policy": reputation_entity_policy,
        }

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
