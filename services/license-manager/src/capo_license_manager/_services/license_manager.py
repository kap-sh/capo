"""Generated from Smithy shape ``com.amazonaws.licensemanager#AWSLicenseManager``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_license_manager._auth._signers
import capo_license_manager._auth._sigv4
from capo_license_manager._auth._identity import Credentials
from capo_license_manager._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_license_manager._auth._zapros_handler import AuthMiddleware
from capo_license_manager._services._aws_config import aws_config
from capo_license_manager._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_license_manager.types.accept_grant_request
    import capo_license_manager.types.accept_grant_response
    import capo_license_manager.types.allowed_operation_list
    import capo_license_manager.types.arn
    import capo_license_manager.types.arn_list
    import capo_license_manager.types.boolean
    import capo_license_manager.types.box_boolean
    import capo_license_manager.types.box_integer
    import capo_license_manager.types.box_long
    import capo_license_manager.types.check_in_license_request
    import capo_license_manager.types.check_in_license_response
    import capo_license_manager.types.checkout_borrow_license_request
    import capo_license_manager.types.checkout_borrow_license_response
    import capo_license_manager.types.checkout_license_request
    import capo_license_manager.types.checkout_license_response
    import capo_license_manager.types.checkout_type
    import capo_license_manager.types.client_request_token
    import capo_license_manager.types.client_token
    import capo_license_manager.types.consumption_configuration
    import capo_license_manager.types.create_grant_request
    import capo_license_manager.types.create_grant_response
    import capo_license_manager.types.create_grant_version_request
    import capo_license_manager.types.create_grant_version_response
    import capo_license_manager.types.create_license_asset_group_request
    import capo_license_manager.types.create_license_asset_group_response
    import capo_license_manager.types.create_license_asset_ruleset_request
    import capo_license_manager.types.create_license_asset_ruleset_response
    import capo_license_manager.types.create_license_configuration_request
    import capo_license_manager.types.create_license_configuration_response
    import capo_license_manager.types.create_license_conversion_task_for_resource_request
    import capo_license_manager.types.create_license_conversion_task_for_resource_response
    import capo_license_manager.types.create_license_manager_report_generator_request
    import capo_license_manager.types.create_license_manager_report_generator_response
    import capo_license_manager.types.create_license_request
    import capo_license_manager.types.create_license_response
    import capo_license_manager.types.create_license_version_request
    import capo_license_manager.types.create_license_version_response
    import capo_license_manager.types.create_token_request
    import capo_license_manager.types.create_token_response
    import capo_license_manager.types.datetime_range
    import capo_license_manager.types.delete_grant_request
    import capo_license_manager.types.delete_grant_response
    import capo_license_manager.types.delete_license_asset_group_request
    import capo_license_manager.types.delete_license_asset_group_response
    import capo_license_manager.types.delete_license_asset_ruleset_request
    import capo_license_manager.types.delete_license_asset_ruleset_response
    import capo_license_manager.types.delete_license_configuration_request
    import capo_license_manager.types.delete_license_configuration_response
    import capo_license_manager.types.delete_license_manager_report_generator_request
    import capo_license_manager.types.delete_license_manager_report_generator_response
    import capo_license_manager.types.delete_license_request
    import capo_license_manager.types.delete_license_response
    import capo_license_manager.types.delete_token_request
    import capo_license_manager.types.delete_token_response
    import capo_license_manager.types.digital_signature_method
    import capo_license_manager.types.entitlement_data_list
    import capo_license_manager.types.entitlement_list
    import capo_license_manager.types.extend_license_consumption_request
    import capo_license_manager.types.extend_license_consumption_response
    import capo_license_manager.types.filter_list
    import capo_license_manager.types.filters
    import capo_license_manager.types.get_access_token_request
    import capo_license_manager.types.get_access_token_response
    import capo_license_manager.types.get_grant_request
    import capo_license_manager.types.get_grant_response
    import capo_license_manager.types.get_license_asset_group_request
    import capo_license_manager.types.get_license_asset_group_response
    import capo_license_manager.types.get_license_asset_ruleset_request
    import capo_license_manager.types.get_license_asset_ruleset_response
    import capo_license_manager.types.get_license_configuration_request
    import capo_license_manager.types.get_license_configuration_response
    import capo_license_manager.types.get_license_conversion_task_request
    import capo_license_manager.types.get_license_conversion_task_response
    import capo_license_manager.types.get_license_manager_report_generator_request
    import capo_license_manager.types.get_license_manager_report_generator_response
    import capo_license_manager.types.get_license_request
    import capo_license_manager.types.get_license_response
    import capo_license_manager.types.get_license_usage_request
    import capo_license_manager.types.get_license_usage_response
    import capo_license_manager.types.get_service_settings_request
    import capo_license_manager.types.get_service_settings_response
    import capo_license_manager.types.grant_status
    import capo_license_manager.types.integer
    import capo_license_manager.types.inventory_filter_list
    import capo_license_manager.types.issuer
    import capo_license_manager.types.license_asset_group_configuration_list
    import capo_license_manager.types.license_asset_group_property_list
    import capo_license_manager.types.license_asset_group_status
    import capo_license_manager.types.license_asset_resource_description
    import capo_license_manager.types.license_asset_resource_name
    import capo_license_manager.types.license_asset_rule_list
    import capo_license_manager.types.license_asset_ruleset_arn_list
    import capo_license_manager.types.license_configuration_status
    import capo_license_manager.types.license_conversion_context
    import capo_license_manager.types.license_conversion_task_id
    import capo_license_manager.types.license_counting_type
    import capo_license_manager.types.license_specifications
    import capo_license_manager.types.license_status
    import capo_license_manager.types.list_assets_for_license_asset_group_request
    import capo_license_manager.types.list_assets_for_license_asset_group_response
    import capo_license_manager.types.list_associations_for_license_configuration_request
    import capo_license_manager.types.list_associations_for_license_configuration_response
    import capo_license_manager.types.list_distributed_grants_request
    import capo_license_manager.types.list_distributed_grants_response
    import capo_license_manager.types.list_failures_for_license_configuration_operations_request
    import capo_license_manager.types.list_failures_for_license_configuration_operations_response
    import capo_license_manager.types.list_license_asset_groups_request
    import capo_license_manager.types.list_license_asset_groups_response
    import capo_license_manager.types.list_license_asset_rulesets_request
    import capo_license_manager.types.list_license_asset_rulesets_response
    import capo_license_manager.types.list_license_configurations_for_organization_request
    import capo_license_manager.types.list_license_configurations_for_organization_response
    import capo_license_manager.types.list_license_configurations_request
    import capo_license_manager.types.list_license_configurations_response
    import capo_license_manager.types.list_license_conversion_tasks_request
    import capo_license_manager.types.list_license_conversion_tasks_response
    import capo_license_manager.types.list_license_manager_report_generators_request
    import capo_license_manager.types.list_license_manager_report_generators_response
    import capo_license_manager.types.list_license_specifications_for_resource_request
    import capo_license_manager.types.list_license_specifications_for_resource_response
    import capo_license_manager.types.list_license_versions_request
    import capo_license_manager.types.list_license_versions_response
    import capo_license_manager.types.list_licenses_request
    import capo_license_manager.types.list_licenses_response
    import capo_license_manager.types.list_received_grants_for_organization_request
    import capo_license_manager.types.list_received_grants_for_organization_response
    import capo_license_manager.types.list_received_grants_request
    import capo_license_manager.types.list_received_grants_response
    import capo_license_manager.types.list_received_licenses_for_organization_request
    import capo_license_manager.types.list_received_licenses_for_organization_response
    import capo_license_manager.types.list_received_licenses_request
    import capo_license_manager.types.list_received_licenses_response
    import capo_license_manager.types.list_resource_inventory_request
    import capo_license_manager.types.list_resource_inventory_response
    import capo_license_manager.types.list_tags_for_resource_request
    import capo_license_manager.types.list_tags_for_resource_response
    import capo_license_manager.types.list_tokens_request
    import capo_license_manager.types.list_tokens_response
    import capo_license_manager.types.list_usage_for_license_configuration_request
    import capo_license_manager.types.list_usage_for_license_configuration_response
    import capo_license_manager.types.max_size3_string_list
    import capo_license_manager.types.max_size100
    import capo_license_manager.types.metadata_list
    import capo_license_manager.types.options
    import capo_license_manager.types.organization_configuration
    import capo_license_manager.types.principal_arn_list
    import capo_license_manager.types.product_information_list
    import capo_license_manager.types.reject_grant_request
    import capo_license_manager.types.reject_grant_response
    import capo_license_manager.types.report_context
    import capo_license_manager.types.report_frequency
    import capo_license_manager.types.report_generator_name
    import capo_license_manager.types.report_type_list
    import capo_license_manager.types.status_reason_message
    import capo_license_manager.types.string
    import capo_license_manager.types.string_list
    import capo_license_manager.types.tag_key_list
    import capo_license_manager.types.tag_list
    import capo_license_manager.types.tag_resource_request
    import capo_license_manager.types.tag_resource_response
    import capo_license_manager.types.token_string
    import capo_license_manager.types.untag_resource_request
    import capo_license_manager.types.untag_resource_response
    import capo_license_manager.types.update_license_asset_group_request
    import capo_license_manager.types.update_license_asset_group_response
    import capo_license_manager.types.update_license_asset_ruleset_request
    import capo_license_manager.types.update_license_asset_ruleset_response
    import capo_license_manager.types.update_license_configuration_request
    import capo_license_manager.types.update_license_configuration_response
    import capo_license_manager.types.update_license_manager_report_generator_request
    import capo_license_manager.types.update_license_manager_report_generator_response
    import capo_license_manager.types.update_license_specifications_for_resource_request
    import capo_license_manager.types.update_license_specifications_for_resource_response
    import capo_license_manager.types.update_service_settings_request
    import capo_license_manager.types.update_service_settings_response


class LicenseManagerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class LicenseManagerClient:
    """A client for the ``LicenseManager`` service.

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
        self._config = LicenseManagerClientConfig(
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
        self, config_overrides: Optional[LicenseManagerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LicenseManagerClientConfig = config_overrides or {}
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

    def accept_grant(
        self,
        grant_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.accept_grant_response.AcceptGrantResponse":
        """<p>Accepts the specified grant.</p>

        Args:
            grant_arn: <p>Amazon Resource Name (ARN) of the grant.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.accept_grant_request.AcceptGrantRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.accept_grant_response.AcceptGrantResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.accept_grant

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.accept_grant.accept_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.accept_grant_request.AcceptGrantRequest = {
            "grant_arn": grant_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def check_in_license(
        self,
        license_consumption_token: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        beneficiary: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.check_in_license_response.CheckInLicenseResponse":
        """<p>Checks in the specified license. Check in a license when it is no longer in use.</p>

        Args:
            license_consumption_token: <p>License consumption token.</p>
            beneficiary: <p>License beneficiary.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Try your request again.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.check_in_license_request.CheckInLicenseRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.check_in_license_response.CheckInLicenseResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.check_in_license

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.check_in_license.check_in_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.check_in_license_request.CheckInLicenseRequest = {
            "license_consumption_token": license_consumption_token
        }
        if beneficiary is not None:
            input_["beneficiary"] = beneficiary

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def checkout_borrow_license(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        entitlements: "capo_license_manager.types.entitlement_data_list.EntitlementDataList",
        digital_signature_method: "capo_license_manager.types.digital_signature_method.DigitalSignatureMethod",
        client_token: "capo_license_manager.types.client_token.ClientToken",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        node_id: Optional["capo_license_manager.types.string.String"] = None,
        checkout_metadata: Optional[
            "capo_license_manager.types.metadata_list.MetadataList"
        ] = None,
    ) -> "capo_license_manager.types.checkout_borrow_license_response.CheckoutBorrowLicenseResponse":
        """<p>Checks out the specified license for offline use.</p>

        Args:
            license_arn: <p>Amazon Resource Name (ARN) of the license. The license must use the borrow consumption configuration.</p>
            entitlements: <p>License entitlements. Partial checkouts are not supported.</p>
            digital_signature_method: <p>Digital signature method. The possible value is JSON Web Signature (JWS) algorithm PS384. For more information, see <a href="https://tools.ietf.org/html/rfc7518#section-3.5">RFC 7518 Digital Signature with RSASSA-PSS</a>.</p>
            node_id: <p>Node ID.</p>
            checkout_metadata: <p>Information about constraints.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.entitlement_not_allowed_exception.EntitlementNotAllowedException: <p>The entitlement is not allowed.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.no_entitlements_allowed_exception.NoEntitlementsAllowedException: <p>There are no entitlements found for this license, or the entitlement maximum count is reached.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.redirect_exception.RedirectException: <p>This is not the correct Region for the resource. Try again.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.unsupported_digital_signature_method_exception.UnsupportedDigitalSignatureMethodException: <p>The digital signature method is unsupported. Try your request again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.checkout_borrow_license_request.CheckoutBorrowLicenseRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.checkout_borrow_license_response.CheckoutBorrowLicenseResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.checkout_borrow_license

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.checkout_borrow_license.checkout_borrow_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.checkout_borrow_license_request.CheckoutBorrowLicenseRequest = {
            "license_arn": license_arn,
            "entitlements": entitlements,
            "digital_signature_method": digital_signature_method,
            "client_token": client_token,
        }
        if node_id is not None:
            input_["node_id"] = node_id
        if checkout_metadata is not None:
            input_["checkout_metadata"] = checkout_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def checkout_license(
        self,
        product_sku: "capo_license_manager.types.string.String",
        checkout_type: "capo_license_manager.types.checkout_type.CheckoutType",
        key_fingerprint: "capo_license_manager.types.string.String",
        entitlements: "capo_license_manager.types.entitlement_data_list.EntitlementDataList",
        client_token: "capo_license_manager.types.client_token.ClientToken",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        beneficiary: Optional["capo_license_manager.types.string.String"] = None,
        node_id: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.checkout_license_response.CheckoutLicenseResponse":
        """<p>Checks out the specified license.</p> <note> <p>If the account that created the license is the same that is performing the check out, you must specify the account as the beneficiary.</p> </note>

        Args:
            product_sku: <p>Product SKU.</p>
            checkout_type: <p>Checkout type.</p>
            key_fingerprint: <p>Key fingerprint identifying the license.</p>
            entitlements: <p>License entitlements.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            beneficiary: <p>License beneficiary.</p>
            node_id: <p>Node ID.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.no_entitlements_allowed_exception.NoEntitlementsAllowedException: <p>There are no entitlements found for this license, or the entitlement maximum count is reached.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.redirect_exception.RedirectException: <p>This is not the correct Region for the resource. Try again.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.unsupported_digital_signature_method_exception.UnsupportedDigitalSignatureMethodException: <p>The digital signature method is unsupported. Try your request again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.checkout_license_request.CheckoutLicenseRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.checkout_license_response.CheckoutLicenseResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.checkout_license

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.checkout_license.checkout_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.checkout_license_request.CheckoutLicenseRequest = {
            "product_sku": product_sku,
            "checkout_type": checkout_type,
            "key_fingerprint": key_fingerprint,
            "entitlements": entitlements,
            "client_token": client_token,
        }
        if beneficiary is not None:
            input_["beneficiary"] = beneficiary
        if node_id is not None:
            input_["node_id"] = node_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_grant(
        self,
        client_token: "capo_license_manager.types.client_token.ClientToken",
        grant_name: "capo_license_manager.types.string.String",
        license_arn: "capo_license_manager.types.arn.Arn",
        principals: "capo_license_manager.types.principal_arn_list.PrincipalArnList",
        home_region: "capo_license_manager.types.string.String",
        allowed_operations: "capo_license_manager.types.allowed_operation_list.AllowedOperationList",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        tags: Optional["capo_license_manager.types.tag_list.TagList"] = None,
    ) -> "capo_license_manager.types.create_grant_response.CreateGrantResponse":
        """<p>Creates a grant for the specified license. A grant shares the use of license entitlements with a specific Amazon Web Services account, an organization, or an organizational unit (OU). For more information, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html">Granted licenses in License Manager</a> in the <i>License Manager User Guide</i>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            grant_name: <p>Grant name.</p>
            license_arn: <p>Amazon Resource Name (ARN) of the license.</p>
            principals: <p>The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):</p> <ul> <li> <p>An Amazon Web Services account, which includes only the account specified.</p> </li> </ul> <ul> <li> <p>An organizational unit (OU), which includes all accounts in the OU.</p> </li> </ul> <ul> <li> <p>An organization, which will include all accounts across your organization.</p> </li> </ul>
            home_region: <p>Home Region of the grant.</p>
            allowed_operations: <p>Allowed operations for the grant.</p>
            tags: <p>Tags to add to the grant. For more information about tagging support in License Manager, see the <a href="https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_grant_request.CreateGrantRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_grant_response.CreateGrantResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_grant

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_grant.create_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_grant_request.CreateGrantRequest = {
            "client_token": client_token,
            "grant_name": grant_name,
            "license_arn": license_arn,
            "principals": principals,
            "home_region": home_region,
            "allowed_operations": allowed_operations,
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

    def create_grant_version(
        self,
        client_token: "capo_license_manager.types.client_token.ClientToken",
        grant_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        grant_name: Optional["capo_license_manager.types.string.String"] = None,
        allowed_operations: Optional[
            "capo_license_manager.types.allowed_operation_list.AllowedOperationList"
        ] = None,
        status: Optional["capo_license_manager.types.grant_status.GrantStatus"] = None,
        status_reason: Optional[
            "capo_license_manager.types.status_reason_message.StatusReasonMessage"
        ] = None,
        source_version: Optional["capo_license_manager.types.string.String"] = None,
        options: Optional["capo_license_manager.types.options.Options"] = None,
    ) -> "capo_license_manager.types.create_grant_version_response.CreateGrantVersionResponse":
        """<p>Creates a new version of the specified grant. For more information, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html">Granted licenses in License Manager</a> in the <i>License Manager User Guide</i>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            grant_arn: <p>Amazon Resource Name (ARN) of the grant.</p>
            grant_name: <p>Grant name.</p>
            allowed_operations: <p>Allowed operations for the grant.</p>
            status: <p>Grant status.</p>
            status_reason: <p>Grant status reason.</p>
            source_version: <p>Current version of the grant.</p>
            options: <p>The options specified for the grant.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_grant_version_request.CreateGrantVersionRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_grant_version_response.CreateGrantVersionResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_grant_version

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_grant_version.create_grant_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_grant_version_request.CreateGrantVersionRequest = {
            "client_token": client_token,
            "grant_arn": grant_arn,
        }
        if grant_name is not None:
            input_["grant_name"] = grant_name
        if allowed_operations is not None:
            input_["allowed_operations"] = allowed_operations
        if status is not None:
            input_["status"] = status
        if status_reason is not None:
            input_["status_reason"] = status_reason
        if source_version is not None:
            input_["source_version"] = source_version
        if options is not None:
            input_["options"] = options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_license(
        self,
        license_name: "capo_license_manager.types.string.String",
        product_name: "capo_license_manager.types.string.String",
        product_sku: "capo_license_manager.types.string.String",
        issuer: "capo_license_manager.types.issuer.Issuer",
        home_region: "capo_license_manager.types.string.String",
        validity: "capo_license_manager.types.datetime_range.DatetimeRange",
        entitlements: "capo_license_manager.types.entitlement_list.EntitlementList",
        beneficiary: "capo_license_manager.types.string.String",
        consumption_configuration: "capo_license_manager.types.consumption_configuration.ConsumptionConfiguration",
        client_token: "capo_license_manager.types.client_token.ClientToken",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        license_metadata: Optional[
            "capo_license_manager.types.metadata_list.MetadataList"
        ] = None,
        tags: Optional["capo_license_manager.types.tag_list.TagList"] = None,
    ) -> "capo_license_manager.types.create_license_response.CreateLicenseResponse":
        """<p>Creates a license.</p>

        Args:
            license_name: <p>License name.</p>
            product_name: <p>Product name.</p>
            product_sku: <p>Product SKU.</p>
            issuer: <p>License issuer.</p>
            home_region: <p>Home Region for the license.</p>
            validity: <p>Date and time range during which the license is valid, in ISO8601-UTC format.</p>
            entitlements: <p>License entitlements.</p>
            beneficiary: <p>License beneficiary.</p>
            consumption_configuration: <p>Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.</p>
            license_metadata: <p>Information about the license.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Tags to add to the license. For more information about tagging support in License Manager, see the <a href="https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.redirect_exception.RedirectException: <p>This is not the correct Region for the resource. Try again.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_license_request.CreateLicenseRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_license_response.CreateLicenseResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_license

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_license.create_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_license_request.CreateLicenseRequest = {
            "license_name": license_name,
            "product_name": product_name,
            "product_sku": product_sku,
            "issuer": issuer,
            "home_region": home_region,
            "validity": validity,
            "entitlements": entitlements,
            "beneficiary": beneficiary,
            "consumption_configuration": consumption_configuration,
            "client_token": client_token,
        }
        if license_metadata is not None:
            input_["license_metadata"] = license_metadata
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_license_asset_group(
        self,
        name: "capo_license_manager.types.license_asset_resource_name.LicenseAssetResourceName",
        license_asset_group_configurations: "capo_license_manager.types.license_asset_group_configuration_list.LicenseAssetGroupConfigurationList",
        associated_license_asset_ruleset_ar_ns: "capo_license_manager.types.license_asset_ruleset_arn_list.LicenseAssetRulesetArnList",
        client_token: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        description: Optional[
            "capo_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
        ] = None,
        properties: Optional[
            "capo_license_manager.types.license_asset_group_property_list.LicenseAssetGroupPropertyList"
        ] = None,
        tags: Optional["capo_license_manager.types.tag_list.TagList"] = None,
    ) -> "capo_license_manager.types.create_license_asset_group_response.CreateLicenseAssetGroupResponse":
        """<p>Creates a license asset group.</p>

        Args:
            name: <p>License asset group name.</p>
            description: <p>License asset group description.</p>
            license_asset_group_configurations: <p>License asset group configurations.</p>
            associated_license_asset_ruleset_ar_ns: <p>ARNs of associated license asset rulesets.</p>
            properties: <p>License asset group properties.</p>
            tags: <p>Tags to add to the license asset group.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_license_asset_group_request.CreateLicenseAssetGroupRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_license_asset_group_response.CreateLicenseAssetGroupResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_license_asset_group

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_license_asset_group.create_license_asset_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_license_asset_group_request.CreateLicenseAssetGroupRequest = {
            "name": name,
            "license_asset_group_configurations": license_asset_group_configurations,
            "associated_license_asset_ruleset_ar_ns": associated_license_asset_ruleset_ar_ns,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if properties is not None:
            input_["properties"] = properties
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_license_asset_ruleset(
        self,
        name: "capo_license_manager.types.license_asset_resource_name.LicenseAssetResourceName",
        rules: "capo_license_manager.types.license_asset_rule_list.LicenseAssetRuleList",
        client_token: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        description: Optional[
            "capo_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
        ] = None,
        tags: Optional["capo_license_manager.types.tag_list.TagList"] = None,
    ) -> "capo_license_manager.types.create_license_asset_ruleset_response.CreateLicenseAssetRulesetResponse":
        """<p>Creates a license asset ruleset.</p>

        Args:
            name: <p>License asset ruleset name.</p>
            description: <p>License asset ruleset description.</p>
            rules: <p>License asset rules.</p>
            tags: <p>Tags to add to the license asset ruleset.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_license_asset_ruleset_request.CreateLicenseAssetRulesetRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_license_asset_ruleset_response.CreateLicenseAssetRulesetResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_license_asset_ruleset

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_license_asset_ruleset.create_license_asset_ruleset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_license_asset_ruleset_request.CreateLicenseAssetRulesetRequest = {
            "name": name,
            "rules": rules,
            "client_token": client_token,
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

    def create_license_configuration(
        self,
        name: "capo_license_manager.types.string.String",
        license_counting_type: "capo_license_manager.types.license_counting_type.LicenseCountingType",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        description: Optional["capo_license_manager.types.string.String"] = None,
        license_count: Optional["capo_license_manager.types.box_long.BoxLong"] = None,
        license_count_hard_limit: Optional[
            "capo_license_manager.types.box_boolean.BoxBoolean"
        ] = None,
        license_rules: Optional[
            "capo_license_manager.types.string_list.StringList"
        ] = None,
        tags: Optional["capo_license_manager.types.tag_list.TagList"] = None,
        disassociate_when_not_found: Optional[
            "capo_license_manager.types.box_boolean.BoxBoolean"
        ] = None,
        product_information_list: Optional[
            "capo_license_manager.types.product_information_list.ProductInformationList"
        ] = None,
        license_expiry: Optional["capo_license_manager.types.box_long.BoxLong"] = None,
    ) -> "capo_license_manager.types.create_license_configuration_response.CreateLicenseConfigurationResponse":
        """<p>Creates a license configuration.</p> <p>A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), license affinity to host (how long a license must be associated with a host), and the number of licenses purchased and used.</p>

        Args:
            name: <p>Name of the license configuration.</p>
            description: <p>Description of the license configuration.</p>
            license_counting_type: <p>Dimension used to track the license inventory.</p>
            license_count: <p>Number of licenses managed by the license configuration.</p>
            license_count_hard_limit: <p>Indicates whether hard or soft license enforcement is used. Exceeding a hard limit blocks the launch of new instances.</p>
            license_rules: <p>License rules. The syntax is #name=value (for example, #allowedTenancy=EC2-DedicatedHost). The available rules vary by dimension, as follows.</p> <ul> <li> <p> <code>Cores</code> dimension: <code>allowedTenancy</code> | <code>licenseAffinityToHost</code> | <code>maximumCores</code> | <code>minimumCores</code> </p> </li> <li> <p> <code>Instances</code> dimension: <code>allowedTenancy</code> | <code>maximumVcpus</code> | <code>minimumVcpus</code> </p> </li> <li> <p> <code>Sockets</code> dimension: <code>allowedTenancy</code> | <code>licenseAffinityToHost</code> | <code>maximumSockets</code> | <code>minimumSockets</code> </p> </li> <li> <p> <code>vCPUs</code> dimension: <code>allowedTenancy</code> | <code>honorVcpuOptimization</code> | <code>maximumVcpus</code> | <code>minimumVcpus</code> </p> </li> </ul> <p>The unit for <code>licenseAffinityToHost</code> is days and the range is 1 to 180. The possible values for <code>allowedTenancy</code> are <code>EC2-Default</code>, <code>EC2-DedicatedHost</code>, and <code>EC2-DedicatedInstance</code>. The possible values for <code>honorVcpuOptimization</code> are <code>True</code> and <code>False</code>.</p>
            tags: <p>Tags to add to the license configuration.</p>
            disassociate_when_not_found: <p>When true, disassociates a resource when software is uninstalled.</p>
            product_information_list: <p>Product information.</p>
            license_expiry: <p>License configuration expiry.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_license_configuration_request.CreateLicenseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_license_configuration_response.CreateLicenseConfigurationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_license_configuration

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_license_configuration.create_license_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_license_configuration_request.CreateLicenseConfigurationRequest = {
            "name": name,
            "license_counting_type": license_counting_type,
        }
        if description is not None:
            input_["description"] = description
        if license_count is not None:
            input_["license_count"] = license_count
        if license_count_hard_limit is not None:
            input_["license_count_hard_limit"] = license_count_hard_limit
        if license_rules is not None:
            input_["license_rules"] = license_rules
        if tags is not None:
            input_["tags"] = tags
        if disassociate_when_not_found is not None:
            input_["disassociate_when_not_found"] = disassociate_when_not_found
        if product_information_list is not None:
            input_["product_information_list"] = product_information_list
        if license_expiry is not None:
            input_["license_expiry"] = license_expiry

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_license_conversion_task_for_resource(
        self,
        resource_arn: "capo_license_manager.types.arn.Arn",
        source_license_context: "capo_license_manager.types.license_conversion_context.LicenseConversionContext",
        destination_license_context: "capo_license_manager.types.license_conversion_context.LicenseConversionContext",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.create_license_conversion_task_for_resource_response.CreateLicenseConversionTaskForResourceResponse":
        """<p>Creates a new license conversion task.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource you are converting the license type for.</p>
            source_license_context: <p>Information that identifies the license type you are converting from. For the structure of the source license, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli">Convert a license type using the CLI </a> in the <i>License Manager User Guide</i>.</p>
            destination_license_context: <p>Information that identifies the license type you are converting to. For the structure of the destination license, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli">Convert a license type using the CLI </a> in the <i>License Manager User Guide</i>.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_license_conversion_task_for_resource_request.CreateLicenseConversionTaskForResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_license_conversion_task_for_resource_response.CreateLicenseConversionTaskForResourceResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_license_conversion_task_for_resource

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_license_conversion_task_for_resource.create_license_conversion_task_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_license_conversion_task_for_resource_request.CreateLicenseConversionTaskForResourceRequest = {
            "resource_arn": resource_arn,
            "source_license_context": source_license_context,
            "destination_license_context": destination_license_context,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_license_manager_report_generator(
        self,
        report_generator_name: "capo_license_manager.types.report_generator_name.ReportGeneratorName",
        type: "capo_license_manager.types.report_type_list.ReportTypeList",
        report_context: "capo_license_manager.types.report_context.ReportContext",
        report_frequency: "capo_license_manager.types.report_frequency.ReportFrequency",
        client_token: "capo_license_manager.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        description: Optional["capo_license_manager.types.string.String"] = None,
        tags: Optional["capo_license_manager.types.tag_list.TagList"] = None,
    ) -> "capo_license_manager.types.create_license_manager_report_generator_response.CreateLicenseManagerReportGeneratorResponse":
        """<p>Creates a report generator.</p>

        Args:
            report_generator_name: <p>Name of the report generator.</p>
            type: <p>Type of reports to generate. The following report types an be generated:</p> <ul> <li> <p>License configuration report - Reports the number and details of consumed licenses for a license configuration.</p> </li> <li> <p>Resource report - Reports the tracked licenses and resource consumption for a license configuration.</p> </li> </ul>
            report_context: <p>Defines the type of license configuration the report generator tracks.</p>
            report_frequency: <p>Frequency by which reports are generated. Reports can be generated daily, monthly, or weekly.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            description: <p>Description of the report generator.</p>
            tags: <p>Tags to add to the report generator.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_license_manager_report_generator_request.CreateLicenseManagerReportGeneratorRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_license_manager_report_generator_response.CreateLicenseManagerReportGeneratorResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_license_manager_report_generator

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_license_manager_report_generator.create_license_manager_report_generator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_license_manager_report_generator_request.CreateLicenseManagerReportGeneratorRequest = {
            "report_generator_name": report_generator_name,
            "type": type,
            "report_context": report_context,
            "report_frequency": report_frequency,
            "client_token": client_token,
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

    def create_license_version(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        license_name: "capo_license_manager.types.string.String",
        product_name: "capo_license_manager.types.string.String",
        issuer: "capo_license_manager.types.issuer.Issuer",
        home_region: "capo_license_manager.types.string.String",
        validity: "capo_license_manager.types.datetime_range.DatetimeRange",
        entitlements: "capo_license_manager.types.entitlement_list.EntitlementList",
        consumption_configuration: "capo_license_manager.types.consumption_configuration.ConsumptionConfiguration",
        status: "capo_license_manager.types.license_status.LicenseStatus",
        client_token: "capo_license_manager.types.client_token.ClientToken",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        license_metadata: Optional[
            "capo_license_manager.types.metadata_list.MetadataList"
        ] = None,
        source_version: Optional["capo_license_manager.types.string.String"] = None,
        reset_usage: Optional["capo_license_manager.types.boolean.Boolean"] = None,
    ) -> "capo_license_manager.types.create_license_version_response.CreateLicenseVersionResponse":
        """<p>Creates a new version of the specified license.</p>

        Args:
            license_arn: <p>Amazon Resource Name (ARN) of the license.</p>
            license_name: <p>License name.</p>
            product_name: <p>Product name.</p>
            issuer: <p>License issuer.</p>
            home_region: <p>Home Region of the license.</p>
            validity: <p>Date and time range during which the license is valid, in ISO8601-UTC format.</p>
            license_metadata: <p>Information about the license.</p>
            entitlements: <p>License entitlements.</p>
            consumption_configuration: <p>Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.</p>
            status: <p>License status.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            source_version: <p>Current version of the license.</p>
            reset_usage: <p>Specifies whether to reset the license usage for the new license version. If you don't specify a value, the license usage is not reset.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Try your request again.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.redirect_exception.RedirectException: <p>This is not the correct Region for the resource. Try again.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_license_version_request.CreateLicenseVersionRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_license_version_response.CreateLicenseVersionResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_license_version

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_license_version.create_license_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_license_version_request.CreateLicenseVersionRequest = {
            "license_arn": license_arn,
            "license_name": license_name,
            "product_name": product_name,
            "issuer": issuer,
            "home_region": home_region,
            "validity": validity,
            "entitlements": entitlements,
            "consumption_configuration": consumption_configuration,
            "status": status,
            "client_token": client_token,
        }
        if license_metadata is not None:
            input_["license_metadata"] = license_metadata
        if source_version is not None:
            input_["source_version"] = source_version
        if reset_usage is not None:
            input_["reset_usage"] = reset_usage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_token(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        client_token: "capo_license_manager.types.client_token.ClientToken",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        role_arns: Optional["capo_license_manager.types.arn_list.ArnList"] = None,
        expiration_in_days: Optional[
            "capo_license_manager.types.integer.Integer"
        ] = None,
        token_properties: Optional[
            "capo_license_manager.types.max_size3_string_list.MaxSize3StringList"
        ] = None,
    ) -> "capo_license_manager.types.create_token_response.CreateTokenResponse":
        """<p>Creates a long-lived token.</p> <p>A refresh token is a JWT token used to get an access token. With an access token, you can call AssumeRoleWithWebIdentity to get role credentials that you can use to call License Manager to manage the specified license.</p>

        Args:
            license_arn: <p>Amazon Resource Name (ARN) of the license. The ARN is mapped to the aud claim of the JWT token.</p>
            role_arns: <p>Amazon Resource Name (ARN) of the IAM roles to embed in the token. License Manager does not check whether the roles are in use.</p>
            expiration_in_days: <p>Token expiration, in days, counted from token creation. The default is 365 days.</p>
            token_properties: <p>Data specified by the caller to be included in the JWT token. The data is mapped to the amr claim of the JWT token.</p>
            client_token: <p>Idempotency token, valid for 10 minutes.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.redirect_exception.RedirectException: <p>This is not the correct Region for the resource. Try again.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.create_token_request.CreateTokenRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.create_token_response.CreateTokenResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.create_token

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.create_token.create_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.create_token_request.CreateTokenRequest = {
            "license_arn": license_arn,
            "client_token": client_token,
        }
        if role_arns is not None:
            input_["role_arns"] = role_arns
        if expiration_in_days is not None:
            input_["expiration_in_days"] = expiration_in_days
        if token_properties is not None:
            input_["token_properties"] = token_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_grant(
        self,
        grant_arn: "capo_license_manager.types.arn.Arn",
        version: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        status_reason: Optional[
            "capo_license_manager.types.status_reason_message.StatusReasonMessage"
        ] = None,
    ) -> "capo_license_manager.types.delete_grant_response.DeleteGrantResponse":
        """<p>Deletes the specified grant.</p>

        Args:
            grant_arn: <p>Amazon Resource Name (ARN) of the grant.</p>
            status_reason: <p>The Status reason for the delete request.</p>
            version: <p>Current version of the grant.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.delete_grant_request.DeleteGrantRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.delete_grant_response.DeleteGrantResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.delete_grant

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.delete_grant.delete_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.delete_grant_request.DeleteGrantRequest = {
            "grant_arn": grant_arn,
            "version": version,
        }
        if status_reason is not None:
            input_["status_reason"] = status_reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_license(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        source_version: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.delete_license_response.DeleteLicenseResponse":
        """<p>Deletes the specified license.</p>

        Args:
            license_arn: <p>Amazon Resource Name (ARN) of the license.</p>
            source_version: <p>Current version of the license.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Try your request again.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.redirect_exception.RedirectException: <p>This is not the correct Region for the resource. Try again.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.delete_license_request.DeleteLicenseRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.delete_license_response.DeleteLicenseResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.delete_license

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.delete_license.delete_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.delete_license_request.DeleteLicenseRequest = {
            "license_arn": license_arn,
            "source_version": source_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_license_asset_group(
        self,
        license_asset_group_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.delete_license_asset_group_response.DeleteLicenseAssetGroupResponse":
        """<p>Deletes a license asset group.</p>

        Args:
            license_asset_group_arn: <p>Amazon Resource Name (ARN) of the license asset group.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.delete_license_asset_group_request.DeleteLicenseAssetGroupRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.delete_license_asset_group_response.DeleteLicenseAssetGroupResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.delete_license_asset_group

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.delete_license_asset_group.delete_license_asset_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.delete_license_asset_group_request.DeleteLicenseAssetGroupRequest = {
            "license_asset_group_arn": license_asset_group_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_license_asset_ruleset(
        self,
        license_asset_ruleset_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.delete_license_asset_ruleset_response.DeleteLicenseAssetRulesetResponse":
        """<p>Deletes a license asset ruleset.</p>

        Args:
            license_asset_ruleset_arn: <p>Amazon Resource Name (ARN) of the license asset ruleset.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.delete_license_asset_ruleset_request.DeleteLicenseAssetRulesetRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.delete_license_asset_ruleset_response.DeleteLicenseAssetRulesetResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.delete_license_asset_ruleset

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.delete_license_asset_ruleset.delete_license_asset_ruleset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.delete_license_asset_ruleset_request.DeleteLicenseAssetRulesetRequest = {
            "license_asset_ruleset_arn": license_asset_ruleset_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_license_configuration(
        self,
        license_configuration_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.delete_license_configuration_response.DeleteLicenseConfigurationResponse":
        """<p>Deletes the specified license configuration.</p> <p>You cannot delete a license configuration that is in use.</p>

        Args:
            license_configuration_arn: <p>ID of the license configuration.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.delete_license_configuration_request.DeleteLicenseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.delete_license_configuration_response.DeleteLicenseConfigurationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.delete_license_configuration

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.delete_license_configuration.delete_license_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.delete_license_configuration_request.DeleteLicenseConfigurationRequest = {
            "license_configuration_arn": license_configuration_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_license_manager_report_generator(
        self,
        license_manager_report_generator_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.delete_license_manager_report_generator_response.DeleteLicenseManagerReportGeneratorResponse":
        """<p>Deletes the specified report generator.</p> <p>This action deletes the report generator, which stops it from generating future reports. The action cannot be reversed. It has no effect on the previous reports from this generator.</p>

        Args:
            license_manager_report_generator_arn: <p>Amazon Resource Name (ARN) of the report generator to be deleted.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.delete_license_manager_report_generator_request.DeleteLicenseManagerReportGeneratorRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.delete_license_manager_report_generator_response.DeleteLicenseManagerReportGeneratorResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.delete_license_manager_report_generator

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.delete_license_manager_report_generator.delete_license_manager_report_generator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.delete_license_manager_report_generator_request.DeleteLicenseManagerReportGeneratorRequest = {
            "license_manager_report_generator_arn": license_manager_report_generator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_token(
        self,
        token_id: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.delete_token_response.DeleteTokenResponse":
        """<p>Deletes the specified token. Must be called in the license home Region.</p>

        Args:
            token_id: <p>Token ID.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.redirect_exception.RedirectException: <p>This is not the correct Region for the resource. Try again.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.delete_token_request.DeleteTokenRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.delete_token_response.DeleteTokenResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.delete_token

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.delete_token.delete_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.delete_token_request.DeleteTokenRequest = {
            "token_id": token_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def extend_license_consumption(
        self,
        license_consumption_token: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        dry_run: Optional["capo_license_manager.types.boolean.Boolean"] = None,
    ) -> "capo_license_manager.types.extend_license_consumption_response.ExtendLicenseConsumptionResponse":
        """<p>Extends the expiration date for license consumption.</p>

        Args:
            license_consumption_token: <p>License consumption token.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request. Provides an error response if you do not have the required permissions.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.extend_license_consumption_request.ExtendLicenseConsumptionRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.extend_license_consumption_response.ExtendLicenseConsumptionResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.extend_license_consumption

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.extend_license_consumption.extend_license_consumption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.extend_license_consumption_request.ExtendLicenseConsumptionRequest = {
            "license_consumption_token": license_consumption_token
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_access_token(
        self,
        token: "capo_license_manager.types.token_string.TokenString",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        token_properties: Optional[
            "capo_license_manager.types.max_size3_string_list.MaxSize3StringList"
        ] = None,
    ) -> "capo_license_manager.types.get_access_token_response.GetAccessTokenResponse":
        """<p>Gets a temporary access token to use with AssumeRoleWithWebIdentity. Access tokens are valid for one hour.</p>

        Args:
            token: <p>Refresh token, encoded as a JWT token.</p>
            token_properties: <p>Token properties to validate against those present in the JWT token.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_access_token_request.GetAccessTokenRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_access_token_response.GetAccessTokenResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_access_token

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_access_token.get_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_access_token_request.GetAccessTokenRequest = {
            "token": token
        }
        if token_properties is not None:
            input_["token_properties"] = token_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_grant(
        self,
        grant_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        version: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.get_grant_response.GetGrantResponse":
        """<p>Gets detailed information about the specified grant.</p>

        Args:
            grant_arn: <p>Amazon Resource Name (ARN) of the grant.</p>
            version: <p>Grant version.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_grant_request.GetGrantRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_grant_response.GetGrantResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_grant

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_grant.get_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_grant_request.GetGrantRequest = {
            "grant_arn": grant_arn
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

    def get_license(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        version: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.get_license_response.GetLicenseResponse":
        """<p>Gets detailed information about the specified license.</p>

        Args:
            license_arn: <p>Amazon Resource Name (ARN) of the license.</p>
            version: <p>License version.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_license_request.GetLicenseRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_license_response.GetLicenseResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_license

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_license.get_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_license_request.GetLicenseRequest = {
            "license_arn": license_arn
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

    def get_license_asset_group(
        self,
        license_asset_group_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.get_license_asset_group_response.GetLicenseAssetGroupResponse":
        """<p>Gets a license asset group.</p>

        Args:
            license_asset_group_arn: <p>Amazon Resource Name (ARN) of the license asset group.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_license_asset_group_request.GetLicenseAssetGroupRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_license_asset_group_response.GetLicenseAssetGroupResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_license_asset_group

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_license_asset_group.get_license_asset_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_license_asset_group_request.GetLicenseAssetGroupRequest = {
            "license_asset_group_arn": license_asset_group_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_license_asset_ruleset(
        self,
        license_asset_ruleset_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.get_license_asset_ruleset_response.GetLicenseAssetRulesetResponse":
        """<p>Gets a license asset ruleset.</p>

        Args:
            license_asset_ruleset_arn: <p>Amazon Resource Name (ARN) of the license asset ruleset.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_license_asset_ruleset_request.GetLicenseAssetRulesetRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_license_asset_ruleset_response.GetLicenseAssetRulesetResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_license_asset_ruleset

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_license_asset_ruleset.get_license_asset_ruleset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_license_asset_ruleset_request.GetLicenseAssetRulesetRequest = {
            "license_asset_ruleset_arn": license_asset_ruleset_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_license_configuration(
        self,
        license_configuration_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.get_license_configuration_response.GetLicenseConfigurationResponse":
        """<p>Gets detailed information about the specified license configuration.</p>

        Args:
            license_configuration_arn: <p>Amazon Resource Name (ARN) of the license configuration.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_license_configuration_request.GetLicenseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_license_configuration_response.GetLicenseConfigurationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_license_configuration

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_license_configuration.get_license_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_license_configuration_request.GetLicenseConfigurationRequest = {
            "license_configuration_arn": license_configuration_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_license_conversion_task(
        self,
        license_conversion_task_id: "capo_license_manager.types.license_conversion_task_id.LicenseConversionTaskId",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.get_license_conversion_task_response.GetLicenseConversionTaskResponse":
        """<p>Gets information about the specified license type conversion task.</p>

        Args:
            license_conversion_task_id: <p>ID of the license type conversion task to retrieve information on.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_license_conversion_task_request.GetLicenseConversionTaskRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_license_conversion_task_response.GetLicenseConversionTaskResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_license_conversion_task

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_license_conversion_task.get_license_conversion_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_license_conversion_task_request.GetLicenseConversionTaskRequest = {
            "license_conversion_task_id": license_conversion_task_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_license_manager_report_generator(
        self,
        license_manager_report_generator_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.get_license_manager_report_generator_response.GetLicenseManagerReportGeneratorResponse":
        """<p>Gets information about the specified report generator.</p>

        Args:
            license_manager_report_generator_arn: <p>Amazon Resource Name (ARN) of the report generator.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_license_manager_report_generator_request.GetLicenseManagerReportGeneratorRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_license_manager_report_generator_response.GetLicenseManagerReportGeneratorResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_license_manager_report_generator

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_license_manager_report_generator.get_license_manager_report_generator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_license_manager_report_generator_request.GetLicenseManagerReportGeneratorRequest = {
            "license_manager_report_generator_arn": license_manager_report_generator_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_license_usage(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> (
        "capo_license_manager.types.get_license_usage_response.GetLicenseUsageResponse"
    ):
        """<p>Gets detailed information about the usage of the specified license.</p>

        Args:
            license_arn: <p>Amazon Resource Name (ARN) of the license.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_license_usage_request.GetLicenseUsageRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_license_usage_response.GetLicenseUsageResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_license_usage

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_license_usage.get_license_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_license_usage_request.GetLicenseUsageRequest = {
            "license_arn": license_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service_settings(
        self, *, config_overrides: Optional[LicenseManagerClientConfig] = None
    ) -> "capo_license_manager.types.get_service_settings_response.GetServiceSettingsResponse":
        """<p>Gets the License Manager settings for the current Region.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.get_service_settings_request.GetServiceSettingsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.get_service_settings_response.GetServiceSettingsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.get_service_settings

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.get_service_settings.get_service_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.get_service_settings_request.GetServiceSettingsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_assets_for_license_asset_group(
        self,
        license_asset_group_arn: "capo_license_manager.types.string.String",
        asset_type: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.list_assets_for_license_asset_group_response.ListAssetsForLicenseAssetGroupResponse":
        """<p>Lists assets for a license asset group.</p>

        Args:
            license_asset_group_arn: <p>Amazon Resource Name (ARN) of the license asset group.</p>
            asset_type: <p>Asset type. The possible values are <code>Instance</code> | <code>License</code> | <code>LicenseConfiguration</code>.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_assets_for_license_asset_group_request.ListAssetsForLicenseAssetGroupRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_assets_for_license_asset_group_response.ListAssetsForLicenseAssetGroupResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_assets_for_license_asset_group

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_assets_for_license_asset_group.list_assets_for_license_asset_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_assets_for_license_asset_group_request.ListAssetsForLicenseAssetGroupRequest = {
            "license_asset_group_arn": license_asset_group_arn,
            "asset_type": asset_type,
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

    def list_associations_for_license_configuration(
        self,
        license_configuration_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.list_associations_for_license_configuration_response.ListAssociationsForLicenseConfigurationResponse":
        """<p>Lists the resource associations for the specified license configuration.</p> <p>Resource associations need not consume licenses from a license configuration. For example, an AMI or a stopped instance might not consume a license (depending on the license rules).</p>

        Args:
            license_configuration_arn: <p>Amazon Resource Name (ARN) of a license configuration.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.filter_limit_exceeded_exception.FilterLimitExceededException: <p>The request uses too many filters or too many filter values.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_associations_for_license_configuration_request.ListAssociationsForLicenseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_associations_for_license_configuration_response.ListAssociationsForLicenseConfigurationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_associations_for_license_configuration

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_associations_for_license_configuration.list_associations_for_license_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_associations_for_license_configuration_request.ListAssociationsForLicenseConfigurationRequest = {
            "license_configuration_arn": license_configuration_arn
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

    def list_distributed_grants(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        grant_arns: Optional["capo_license_manager.types.arn_list.ArnList"] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_distributed_grants_response.ListDistributedGrantsResponse":
        """<p>Lists the grants distributed for the specified license.</p>

        Args:
            grant_arns: <p>Amazon Resource Names (ARNs) of the grants.</p>
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>LicenseArn</code> </p> </li> <li> <p> <code>GrantStatus</code> </p> </li> <li> <p> <code>GranteePrincipalARN</code> </p> </li> <li> <p> <code>ProductSKU</code> </p> </li> <li> <p> <code>LicenseIssuerName</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_distributed_grants_request.ListDistributedGrantsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_distributed_grants_response.ListDistributedGrantsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_distributed_grants

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_distributed_grants.list_distributed_grants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_distributed_grants_request.ListDistributedGrantsRequest = {}
        if grant_arns is not None:
            input_["grant_arns"] = grant_arns
        if filters is not None:
            input_["filters"] = filters
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

    def list_failures_for_license_configuration_operations(
        self,
        license_configuration_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.list_failures_for_license_configuration_operations_response.ListFailuresForLicenseConfigurationOperationsResponse":
        """<p>Lists the license configuration operations that failed.</p>

        Args:
            license_configuration_arn: <p>Amazon Resource Name of the license configuration.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_failures_for_license_configuration_operations_request.ListFailuresForLicenseConfigurationOperationsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_failures_for_license_configuration_operations_response.ListFailuresForLicenseConfigurationOperationsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_failures_for_license_configuration_operations

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_failures_for_license_configuration_operations.list_failures_for_license_configuration_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_failures_for_license_configuration_operations_request.ListFailuresForLicenseConfigurationOperationsRequest = {
            "license_configuration_arn": license_configuration_arn
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

    def list_license_asset_groups(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        filters: Optional["capo_license_manager.types.filters.Filters"] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.list_license_asset_groups_response.ListLicenseAssetGroupsResponse":
        """<p>Lists license asset groups.</p>

        Args:
            filters: <p>Filters to scope the results. Following filters are supported</p> <ul> <li> <p> <code>LicenseAssetRulesetArn</code> </p> </li> </ul>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_asset_groups_request.ListLicenseAssetGroupsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_asset_groups_response.ListLicenseAssetGroupsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_asset_groups

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_asset_groups.list_license_asset_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_asset_groups_request.ListLicenseAssetGroupsRequest = {}
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

    def list_license_asset_rulesets(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        filters: Optional["capo_license_manager.types.filters.Filters"] = None,
        show_aws_managed_license_asset_rulesets: Optional[
            "capo_license_manager.types.boolean.Boolean"
        ] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.list_license_asset_rulesets_response.ListLicenseAssetRulesetsResponse":
        """<p>Lists license asset rulesets.</p>

        Args:
            filters: <p>Filters to scope the results. Following filters are supported</p> <ul> <li> <p> <code>Name</code> </p> </li> </ul>
            show_aws_managed_license_asset_rulesets: <p>Specifies whether to show License Manager managed license asset rulesets.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_asset_rulesets_request.ListLicenseAssetRulesetsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_asset_rulesets_response.ListLicenseAssetRulesetsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_asset_rulesets

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_asset_rulesets.list_license_asset_rulesets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_asset_rulesets_request.ListLicenseAssetRulesetsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if show_aws_managed_license_asset_rulesets is not None:
            input_["show_aws_managed_license_asset_rulesets"] = (
                show_aws_managed_license_asset_rulesets
            )
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

    def list_license_configurations(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        license_configuration_arns: Optional[
            "capo_license_manager.types.string_list.StringList"
        ] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        filters: Optional["capo_license_manager.types.filters.Filters"] = None,
    ) -> "capo_license_manager.types.list_license_configurations_response.ListLicenseConfigurationsResponse":
        """<p>Lists the license configurations for your account.</p>

        Args:
            license_configuration_arns: <p>Amazon Resource Names (ARN) of the license configurations.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>
            filters: <p>Filters to scope the results. The following filters and logical operators are supported:</p> <ul> <li> <p> <code>licenseCountingType</code> - The dimension for which licenses are counted. Possible values are <code>vCPU</code> | <code>Instance</code> | <code>Core</code> | <code>Socket</code>.</p> </li> <li> <p> <code>enforceLicenseCount</code> - A Boolean value that indicates whether hard license enforcement is used.</p> </li> <li> <p> <code>usagelimitExceeded</code> - A Boolean value that indicates whether the available licenses have been exceeded.</p> </li> </ul>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.filter_limit_exceeded_exception.FilterLimitExceededException: <p>The request uses too many filters or too many filter values.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_configurations_request.ListLicenseConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_configurations_response.ListLicenseConfigurationsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_configurations

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_configurations.list_license_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_configurations_request.ListLicenseConfigurationsRequest = {}
        if license_configuration_arns is not None:
            input_["license_configuration_arns"] = license_configuration_arns
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_license_configurations_for_organization(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        license_configuration_arns: Optional[
            "capo_license_manager.types.string_list.StringList"
        ] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        filters: Optional["capo_license_manager.types.filters.Filters"] = None,
    ) -> "capo_license_manager.types.list_license_configurations_for_organization_response.ListLicenseConfigurationsForOrganizationResponse":
        """<p>Lists license configurations for an organization.</p>

        Args:
            license_configuration_arns: <p>License configuration ARNs.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>
            filters: <p>Filters to scope the results.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.filter_limit_exceeded_exception.FilterLimitExceededException: <p>The request uses too many filters or too many filter values.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_configurations_for_organization_request.ListLicenseConfigurationsForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_configurations_for_organization_response.ListLicenseConfigurationsForOrganizationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_configurations_for_organization

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_configurations_for_organization.list_license_configurations_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_configurations_for_organization_request.ListLicenseConfigurationsForOrganizationRequest = {}
        if license_configuration_arns is not None:
            input_["license_configuration_arns"] = license_configuration_arns
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_license_conversion_tasks(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        filters: Optional["capo_license_manager.types.filters.Filters"] = None,
    ) -> "capo_license_manager.types.list_license_conversion_tasks_response.ListLicenseConversionTasksResponse":
        """<p>Lists the license type conversion tasks for your account.</p>

        Args:
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            filters: <p> Filters to scope the results. Valid filters are <code>ResourceArns</code> and <code>Status</code>. </p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_conversion_tasks_request.ListLicenseConversionTasksRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_conversion_tasks_response.ListLicenseConversionTasksResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_conversion_tasks

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_conversion_tasks.list_license_conversion_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_conversion_tasks_request.ListLicenseConversionTasksRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_license_manager_report_generators(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_license_manager_report_generators_response.ListLicenseManagerReportGeneratorsResponse":
        """<p>Lists the report generators for your account.</p>

        Args:
            filters: <p>Filters to scope the results. The following filters are supported: </p> <ul> <li> <p> <code>LicenseConfigurationArn</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_manager_report_generators_request.ListLicenseManagerReportGeneratorsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_manager_report_generators_response.ListLicenseManagerReportGeneratorsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_manager_report_generators

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_manager_report_generators.list_license_manager_report_generators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_manager_report_generators_request.ListLicenseManagerReportGeneratorsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def list_licenses(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        license_arns: Optional["capo_license_manager.types.arn_list.ArnList"] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_licenses_response.ListLicensesResponse":
        """<p>Lists the licenses for your account.</p>

        Args:
            license_arns: <p>Amazon Resource Names (ARNs) of the licenses.</p>
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>Beneficiary</code> </p> </li> <li> <p> <code>ProductSKU</code> </p> </li> <li> <p> <code>Fingerprint</code> </p> </li> <li> <p> <code>Status</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_licenses_request.ListLicensesRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_licenses_response.ListLicensesResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_licenses

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_licenses.list_licenses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_licenses_request.ListLicensesRequest = {}
        if license_arns is not None:
            input_["license_arns"] = license_arns
        if filters is not None:
            input_["filters"] = filters
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

    def list_license_specifications_for_resource(
        self,
        resource_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.list_license_specifications_for_resource_response.ListLicenseSpecificationsForResourceResponse":
        """<p>Describes the license configurations for the specified resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of a resource that has an associated license configuration.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_specifications_for_resource_request.ListLicenseSpecificationsForResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_specifications_for_resource_response.ListLicenseSpecificationsForResourceResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_specifications_for_resource

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_specifications_for_resource.list_license_specifications_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_specifications_for_resource_request.ListLicenseSpecificationsForResourceRequest = {
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

    def list_license_versions(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_license_versions_response.ListLicenseVersionsResponse":
        """<p>Lists all versions of the specified license.</p>

        Args:
            license_arn: <p>Amazon Resource Name (ARN) of the license.</p>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_license_versions_request.ListLicenseVersionsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_license_versions_response.ListLicenseVersionsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_license_versions

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_license_versions.list_license_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_license_versions_request.ListLicenseVersionsRequest = {
            "license_arn": license_arn
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

    def list_received_grants(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        grant_arns: Optional["capo_license_manager.types.arn_list.ArnList"] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_received_grants_response.ListReceivedGrantsResponse":
        """<p>Lists grants that are received. Received grants are grants created while specifying the recipient as this Amazon Web Services account, your organization, or an organizational unit (OU) to which this member account belongs.</p>

        Args:
            grant_arns: <p>Amazon Resource Names (ARNs) of the grants.</p>
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>ProductSKU</code> </p> </li> <li> <p> <code>LicenseIssuerName</code> </p> </li> <li> <p> <code>LicenseArn</code> </p> </li> <li> <p> <code>GrantStatus</code> </p> </li> <li> <p> <code>GranterAccountId</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_received_grants_request.ListReceivedGrantsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_received_grants_response.ListReceivedGrantsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_received_grants

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_received_grants.list_received_grants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_received_grants_request.ListReceivedGrantsRequest = {}
        if grant_arns is not None:
            input_["grant_arns"] = grant_arns
        if filters is not None:
            input_["filters"] = filters
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

    def list_received_grants_for_organization(
        self,
        license_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_received_grants_for_organization_response.ListReceivedGrantsForOrganizationResponse":
        """<p>Lists the grants received for all accounts in the organization.</p>

        Args:
            license_arn: <p>The Amazon Resource Name (ARN) of the received license.</p>
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>ParentArn</code> </p> </li> <li> <p> <code>GranteePrincipalArn</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_received_grants_for_organization_request.ListReceivedGrantsForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_received_grants_for_organization_response.ListReceivedGrantsForOrganizationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_received_grants_for_organization

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_received_grants_for_organization.list_received_grants_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_received_grants_for_organization_request.ListReceivedGrantsForOrganizationRequest = {
            "license_arn": license_arn
        }
        if filters is not None:
            input_["filters"] = filters
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

    def list_received_licenses(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        license_arns: Optional["capo_license_manager.types.arn_list.ArnList"] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_received_licenses_response.ListReceivedLicensesResponse":
        """<p>Lists received licenses.</p>

        Args:
            license_arns: <p>Amazon Resource Names (ARNs) of the licenses.</p>
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>ProductSKU</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>Fingerprint</code> </p> </li> <li> <p> <code>IssuerName</code> </p> </li> <li> <p> <code>Beneficiary</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_received_licenses_request.ListReceivedLicensesRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_received_licenses_response.ListReceivedLicensesResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_received_licenses

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_received_licenses.list_received_licenses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_received_licenses_request.ListReceivedLicensesRequest = {}
        if license_arns is not None:
            input_["license_arns"] = license_arns
        if filters is not None:
            input_["filters"] = filters
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

    def list_received_licenses_for_organization(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_received_licenses_for_organization_response.ListReceivedLicensesForOrganizationResponse":
        """<p>Lists the licenses received for all accounts in the organization.</p>

        Args:
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>Beneficiary</code> </p> </li> <li> <p> <code>ProductSKU</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_received_licenses_for_organization_request.ListReceivedLicensesForOrganizationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_received_licenses_for_organization_response.ListReceivedLicensesForOrganizationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_received_licenses_for_organization

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_received_licenses_for_organization.list_received_licenses_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_received_licenses_for_organization_request.ListReceivedLicensesForOrganizationRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def list_resource_inventory(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        filters: Optional[
            "capo_license_manager.types.inventory_filter_list.InventoryFilterList"
        ] = None,
    ) -> "capo_license_manager.types.list_resource_inventory_response.ListResourceInventoryResponse":
        """<p>Lists resources managed using Systems Manager inventory.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>
            filters: <p>Filters to scope the results. The following filters and logical operators are supported:</p> <ul> <li> <p> <code>account_id</code> - The ID of the Amazon Web Services account that owns the resource. Logical operators are <code>EQUALS</code> | <code>NOT_EQUALS</code>.</p> </li> <li> <p> <code>application_name</code> - The name of the application. Logical operators are <code>EQUALS</code> | <code>BEGINS_WITH</code>.</p> </li> <li> <p> <code>license_included</code> - The type of license included. Logical operators are <code>EQUALS</code> | <code>NOT_EQUALS</code>. Possible values are <code>sql-server-enterprise</code> | <code>sql-server-standard</code> | <code>sql-server-web</code> | <code>windows-server-datacenter</code>.</p> </li> <li> <p> <code>platform</code> - The platform of the resource. Logical operators are <code>EQUALS</code> | <code>BEGINS_WITH</code>.</p> </li> <li> <p> <code>resource_id</code> - The ID of the resource. Logical operators are <code>EQUALS</code> | <code>NOT_EQUALS</code>.</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Logical operators are <code>EQUALS</code> (single account) or <code>EQUALS</code> | <code>NOT_EQUALS</code> (cross account).</p> </li> </ul>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.failed_dependency_exception.FailedDependencyException: <p>A dependency required to run the API is missing.</p>
            capo_license_manager.errors.filter_limit_exceeded_exception.FilterLimitExceededException: <p>The request uses too many filters or too many filter values.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_resource_inventory_request.ListResourceInventoryRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_resource_inventory_response.ListResourceInventoryResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_resource_inventory

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_resource_inventory.list_resource_inventory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_resource_inventory_request.ListResourceInventoryRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource. For more information about tagging support in License Manager, see the <a href="https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_tags_for_resource

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tokens(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        token_ids: Optional["capo_license_manager.types.string_list.StringList"] = None,
        filters: Optional["capo_license_manager.types.filter_list.FilterList"] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        max_results: Optional[
            "capo_license_manager.types.max_size100.MaxSize100"
        ] = None,
    ) -> "capo_license_manager.types.list_tokens_response.ListTokensResponse":
        """<p>Lists your tokens.</p>

        Args:
            token_ids: <p>Token IDs.</p>
            filters: <p>Filters to scope the results. The following filter is supported:</p> <ul> <li> <p> <code>LicenseArns</code> </p> </li> </ul>
            next_token: <p>Token for the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_tokens_request.ListTokensRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_tokens_response.ListTokensResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_tokens

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_tokens.list_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_tokens_request.ListTokensRequest = {}
        if token_ids is not None:
            input_["token_ids"] = token_ids
        if filters is not None:
            input_["filters"] = filters
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

    def list_usage_for_license_configuration(
        self,
        license_configuration_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        max_results: Optional[
            "capo_license_manager.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional["capo_license_manager.types.string.String"] = None,
        filters: Optional["capo_license_manager.types.filters.Filters"] = None,
    ) -> "capo_license_manager.types.list_usage_for_license_configuration_response.ListUsageForLicenseConfigurationResponse":
        """<p>Lists all license usage records for a license configuration, displaying license consumption details by resource at a selected point in time. Use this action to audit the current license consumption for any license inventory and configuration.</p>

        Args:
            license_configuration_arn: <p>Amazon Resource Name (ARN) of the license configuration.</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next set of results.</p>
            filters: <p>Filters to scope the results. The following filters and logical operators are supported:</p> <ul> <li> <p> <code>resourceArn</code> - The ARN of the license configuration resource.</p> </li> <li> <p> <code>resourceType</code> - The resource type (<code>EC2_INSTANCE</code> | <code>EC2_HOST</code> | <code>EC2_AMI</code> | <code>SYSTEMS_MANAGER_MANAGED_INSTANCE</code>).</p> </li> <li> <p> <code>resourceAccount</code> - The ID of the account that owns the resource.</p> </li> </ul>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.filter_limit_exceeded_exception.FilterLimitExceededException: <p>The request uses too many filters or too many filter values.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.list_usage_for_license_configuration_request.ListUsageForLicenseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.list_usage_for_license_configuration_response.ListUsageForLicenseConfigurationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.list_usage_for_license_configuration

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.list_usage_for_license_configuration.list_usage_for_license_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.list_usage_for_license_configuration_request.ListUsageForLicenseConfigurationRequest = {
            "license_configuration_arn": license_configuration_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_grant(
        self,
        grant_arn: "capo_license_manager.types.arn.Arn",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.reject_grant_response.RejectGrantResponse":
        """<p>Rejects the specified grant.</p>

        Args:
            grant_arn: <p>Amazon Resource Name (ARN) of the grant.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.reject_grant_request.RejectGrantRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.reject_grant_response.RejectGrantResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.reject_grant

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.reject_grant.reject_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.reject_grant_request.RejectGrantRequest = {
            "grant_arn": grant_arn
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
        resource_arn: "capo_license_manager.types.string.String",
        tags: "capo_license_manager.types.tag_list.TagList",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource. The following resources support tagging in License Manager:</p> <ul> <li> <p>Licenses</p> </li> <li> <p>Grants</p> </li> <li> <p>License configurations</p> </li> <li> <p>Report generators</p> </li> </ul>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource. The following examples provide an example ARN for each supported resource in License Manager:</p> <ul> <li> <p>Licenses - <code>arn:aws:license-manager::111122223333:license:l-EXAMPLE2da7646d6861033667f20e895</code> </p> </li> <li> <p>Grants - <code>arn:aws:license-manager::111122223333:grant:g-EXAMPLE7b19f4a0ab73679b0beb52707</code> </p> </li> <li> <p>License configurations - <code>arn:aws:license-manager:us-east-1:111122223333:license-configuration:lic-EXAMPLE6a788d4c8acd4264ff0ecf2ed2d</code> </p> </li> <li> <p>Report generators - <code>arn:aws:license-manager:us-east-1:111122223333:report-generator:r-EXAMPLE825b4a4f8fe5a3e0c88824e5fc6</code> </p> </li> </ul>
            tags: <p>One or more tags.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.tag_resource

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_license_manager.types.string.String",
        tag_keys: "capo_license_manager.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
    ) -> "capo_license_manager.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Keys identifying the tags to remove.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.untag_resource

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.untag_resource_request.UntagResourceRequest = {
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

    def update_license_asset_group(
        self,
        associated_license_asset_ruleset_ar_ns: "capo_license_manager.types.license_asset_ruleset_arn_list.LicenseAssetRulesetArnList",
        license_asset_group_arn: "capo_license_manager.types.arn.Arn",
        client_token: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        name: Optional[
            "capo_license_manager.types.license_asset_resource_name.LicenseAssetResourceName"
        ] = None,
        description: Optional[
            "capo_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
        ] = None,
        license_asset_group_configurations: Optional[
            "capo_license_manager.types.license_asset_group_configuration_list.LicenseAssetGroupConfigurationList"
        ] = None,
        properties: Optional[
            "capo_license_manager.types.license_asset_group_property_list.LicenseAssetGroupPropertyList"
        ] = None,
        status: Optional[
            "capo_license_manager.types.license_asset_group_status.LicenseAssetGroupStatus"
        ] = None,
    ) -> "capo_license_manager.types.update_license_asset_group_response.UpdateLicenseAssetGroupResponse":
        """<p>Updates a license asset group.</p>

        Args:
            name: <p>License asset group name.</p>
            description: <p>License asset group description.</p>
            license_asset_group_configurations: <p>License asset group configurations.</p>
            associated_license_asset_ruleset_ar_ns: <p>ARNs of associated license asset rulesets.</p>
            properties: <p>License asset group properties.</p>
            license_asset_group_arn: <p>Amazon Resource Name (ARN) of the license asset group.</p>
            status: <p>License asset group status. The possible values are <code>ACTIVE</code> | <code>DISABLED</code>.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.update_license_asset_group_request.UpdateLicenseAssetGroupRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.update_license_asset_group_response.UpdateLicenseAssetGroupResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.update_license_asset_group

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.update_license_asset_group.update_license_asset_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.update_license_asset_group_request.UpdateLicenseAssetGroupRequest = {
            "associated_license_asset_ruleset_ar_ns": associated_license_asset_ruleset_ar_ns,
            "license_asset_group_arn": license_asset_group_arn,
            "client_token": client_token,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if license_asset_group_configurations is not None:
            input_["license_asset_group_configurations"] = (
                license_asset_group_configurations
            )
        if properties is not None:
            input_["properties"] = properties
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_license_asset_ruleset(
        self,
        rules: "capo_license_manager.types.license_asset_rule_list.LicenseAssetRuleList",
        license_asset_ruleset_arn: "capo_license_manager.types.arn.Arn",
        client_token: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        name: Optional[
            "capo_license_manager.types.license_asset_resource_name.LicenseAssetResourceName"
        ] = None,
        description: Optional[
            "capo_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
        ] = None,
    ) -> "capo_license_manager.types.update_license_asset_ruleset_response.UpdateLicenseAssetRulesetResponse":
        """<p>Updates a license asset ruleset.</p>

        Args:
            name: <p>License asset ruleset name.</p>
            description: <p>License asset ruleset description.</p>
            rules: <p>License asset rules.</p>
            license_asset_ruleset_arn: <p>Amazon Resource Name (ARN) of the license asset ruleset.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.update_license_asset_ruleset_request.UpdateLicenseAssetRulesetRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.update_license_asset_ruleset_response.UpdateLicenseAssetRulesetResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.update_license_asset_ruleset

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.update_license_asset_ruleset.update_license_asset_ruleset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.update_license_asset_ruleset_request.UpdateLicenseAssetRulesetRequest = {
            "rules": rules,
            "license_asset_ruleset_arn": license_asset_ruleset_arn,
            "client_token": client_token,
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

    def update_license_configuration(
        self,
        license_configuration_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        license_configuration_status: Optional[
            "capo_license_manager.types.license_configuration_status.LicenseConfigurationStatus"
        ] = None,
        license_rules: Optional[
            "capo_license_manager.types.string_list.StringList"
        ] = None,
        license_count: Optional["capo_license_manager.types.box_long.BoxLong"] = None,
        license_count_hard_limit: Optional[
            "capo_license_manager.types.box_boolean.BoxBoolean"
        ] = None,
        name: Optional["capo_license_manager.types.string.String"] = None,
        description: Optional["capo_license_manager.types.string.String"] = None,
        product_information_list: Optional[
            "capo_license_manager.types.product_information_list.ProductInformationList"
        ] = None,
        disassociate_when_not_found: Optional[
            "capo_license_manager.types.box_boolean.BoxBoolean"
        ] = None,
        license_expiry: Optional["capo_license_manager.types.box_long.BoxLong"] = None,
    ) -> "capo_license_manager.types.update_license_configuration_response.UpdateLicenseConfigurationResponse":
        """<p>Modifies the attributes of an existing license configuration.</p>

        Args:
            license_configuration_arn: <p>Amazon Resource Name (ARN) of the license configuration.</p>
            license_configuration_status: <p>New status of the license configuration.</p>
            license_rules: <p>New license rule. The only rule that you can add after you create a license configuration is licenseAffinityToHost.</p>
            license_count: <p>New number of licenses managed by the license configuration.</p>
            license_count_hard_limit: <p>New hard limit of the number of available licenses.</p>
            name: <p>New name of the license configuration.</p>
            description: <p>New description of the license configuration.</p>
            product_information_list: <p>New product information.</p>
            disassociate_when_not_found: <p>When true, disassociates a resource when software is uninstalled.</p>
            license_expiry: <p>License configuration expiry time.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Try your request again.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.update_license_configuration_request.UpdateLicenseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.update_license_configuration_response.UpdateLicenseConfigurationResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.update_license_configuration

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.update_license_configuration.update_license_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.update_license_configuration_request.UpdateLicenseConfigurationRequest = {
            "license_configuration_arn": license_configuration_arn
        }
        if license_configuration_status is not None:
            input_["license_configuration_status"] = license_configuration_status
        if license_rules is not None:
            input_["license_rules"] = license_rules
        if license_count is not None:
            input_["license_count"] = license_count
        if license_count_hard_limit is not None:
            input_["license_count_hard_limit"] = license_count_hard_limit
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if product_information_list is not None:
            input_["product_information_list"] = product_information_list
        if disassociate_when_not_found is not None:
            input_["disassociate_when_not_found"] = disassociate_when_not_found
        if license_expiry is not None:
            input_["license_expiry"] = license_expiry

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_license_manager_report_generator(
        self,
        license_manager_report_generator_arn: "capo_license_manager.types.string.String",
        report_generator_name: "capo_license_manager.types.report_generator_name.ReportGeneratorName",
        type: "capo_license_manager.types.report_type_list.ReportTypeList",
        report_context: "capo_license_manager.types.report_context.ReportContext",
        report_frequency: "capo_license_manager.types.report_frequency.ReportFrequency",
        client_token: "capo_license_manager.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        description: Optional["capo_license_manager.types.string.String"] = None,
    ) -> "capo_license_manager.types.update_license_manager_report_generator_response.UpdateLicenseManagerReportGeneratorResponse":
        """<p>Updates a report generator.</p> <p>After you make changes to a report generator, it starts generating new reports within 60 minutes of being updated.</p>

        Args:
            license_manager_report_generator_arn: <p>Amazon Resource Name (ARN) of the report generator to update.</p>
            report_generator_name: <p>Name of the report generator.</p>
            type: <p>Type of reports to generate. The following report types are supported:</p> <ul> <li> <p>License configuration report - Reports the number and details of consumed licenses for a license configuration.</p> </li> <li> <p>Resource report - Reports the tracked licenses and resource consumption for a license configuration.</p> </li> </ul>
            report_context: <p>The report context.</p>
            report_frequency: <p>Frequency by which reports are generated.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            description: <p>Description of the report generator.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_license_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.update_license_manager_report_generator_request.UpdateLicenseManagerReportGeneratorRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.update_license_manager_report_generator_response.UpdateLicenseManagerReportGeneratorResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.update_license_manager_report_generator

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.update_license_manager_report_generator.update_license_manager_report_generator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.update_license_manager_report_generator_request.UpdateLicenseManagerReportGeneratorRequest = {
            "license_manager_report_generator_arn": license_manager_report_generator_arn,
            "report_generator_name": report_generator_name,
            "type": type,
            "report_context": report_context,
            "report_frequency": report_frequency,
            "client_token": client_token,
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

    def update_license_specifications_for_resource(
        self,
        resource_arn: "capo_license_manager.types.string.String",
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        add_license_specifications: Optional[
            "capo_license_manager.types.license_specifications.LicenseSpecifications"
        ] = None,
        remove_license_specifications: Optional[
            "capo_license_manager.types.license_specifications.LicenseSpecifications"
        ] = None,
    ) -> "capo_license_manager.types.update_license_specifications_for_resource_response.UpdateLicenseSpecificationsForResourceResponse":
        """<p>Adds or removes the specified license configurations for the specified Amazon Web Services resource.</p> <p>You can update the license specifications of AMIs, instances, and hosts. You cannot update the license specifications for launch templates and CloudFormation templates, as they send license configurations to the operation that creates the resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the Amazon Web Services resource.</p>
            add_license_specifications: <p>ARNs of the license configurations to add.</p>
            remove_license_specifications: <p>ARNs of the license configurations to remove.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Try your request again.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>License Manager cannot allocate a license to a resource because of its state. </p> <p>For example, you cannot allocate a license to an instance in the process of shutting down.</p>
            capo_license_manager.errors.license_usage_exception.LicenseUsageException: <p>You do not have enough licenses available to support a new resource launch.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.update_license_specifications_for_resource_request.UpdateLicenseSpecificationsForResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.update_license_specifications_for_resource_response.UpdateLicenseSpecificationsForResourceResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.update_license_specifications_for_resource

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.update_license_specifications_for_resource.update_license_specifications_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.update_license_specifications_for_resource_request.UpdateLicenseSpecificationsForResourceRequest = {
            "resource_arn": resource_arn
        }
        if add_license_specifications is not None:
            input_["add_license_specifications"] = add_license_specifications
        if remove_license_specifications is not None:
            input_["remove_license_specifications"] = remove_license_specifications

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_settings(
        self,
        *,
        config_overrides: Optional[LicenseManagerClientConfig] = None,
        s3_bucket_arn: Optional["capo_license_manager.types.string.String"] = None,
        sns_topic_arn: Optional["capo_license_manager.types.string.String"] = None,
        organization_configuration: Optional[
            "capo_license_manager.types.organization_configuration.OrganizationConfiguration"
        ] = None,
        enable_cross_accounts_discovery: Optional[
            "capo_license_manager.types.box_boolean.BoxBoolean"
        ] = None,
        enabled_discovery_source_regions: Optional[
            "capo_license_manager.types.string_list.StringList"
        ] = None,
    ) -> "capo_license_manager.types.update_service_settings_response.UpdateServiceSettingsResponse":
        """<p>Updates License Manager settings for the current Region.</p>

        Args:
            s3_bucket_arn: <p>Amazon Resource Name (ARN) of the Amazon S3 bucket where the License Manager information is stored.</p>
            sns_topic_arn: <p>Amazon Resource Name (ARN) of the Amazon SNS topic used for License Manager alerts.</p>
            organization_configuration: <p>Enables integration with Organizations for cross-account discovery.</p>
            enable_cross_accounts_discovery: <p>Activates cross-account discovery.</p>
            enabled_discovery_source_regions: <p>Cross region discovery enabled source regions.</p>

        Raises:
            capo_license_manager.errors.access_denied_exception.AccessDeniedException: <p>Access to resource denied.</p>
            capo_license_manager.errors.authorization_exception.AuthorizationException: <p>The Amazon Web Services user account does not have permission to perform the action. Check the IAM policy associated with this account.</p>
            capo_license_manager.errors.conflict_exception.ConflictException: <p>There was a conflict processing the request. Try your request again.</p>
            capo_license_manager.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One or more parameter values are not valid.</p>
            capo_license_manager.errors.rate_limit_exceeded_exception.RateLimitExceededException: <p>Too many requests have been submitted. Try again after a brief wait.</p>
            capo_license_manager.errors.server_internal_exception.ServerInternalException: <p>The server experienced an internal error. Try again.</p>
            capo_license_manager.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager.types.update_service_settings_request.UpdateServiceSettingsRequest]",
        ) -> OperationResponse[
            "capo_license_manager.types.update_service_settings_response.UpdateServiceSettingsResponse"
        ]:
            import capo_license_manager._operations.aws_license_manager.update_service_settings

            output, http_response = (
                capo_license_manager._operations.aws_license_manager.update_service_settings.update_service_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager.types.update_service_settings_request.UpdateServiceSettingsRequest = {}
        if s3_bucket_arn is not None:
            input_["s3_bucket_arn"] = s3_bucket_arn
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if organization_configuration is not None:
            input_["organization_configuration"] = organization_configuration
        if enable_cross_accounts_discovery is not None:
            input_["enable_cross_accounts_discovery"] = enable_cross_accounts_discovery
        if enabled_discovery_source_regions is not None:
            input_["enabled_discovery_source_regions"] = (
                enabled_discovery_source_regions
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
