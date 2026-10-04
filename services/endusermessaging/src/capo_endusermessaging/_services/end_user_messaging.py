"""Generated from Smithy shape ``com.amazonaws.endusermessaging#EndUserMessaging``."""

import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_endusermessaging._auth._signers
import capo_endusermessaging._auth._sigv4
from capo_endusermessaging._auth._identity import Credentials
from capo_endusermessaging._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_endusermessaging._auth._zapros_handler import AuthMiddleware
from capo_endusermessaging._services._aws_config import aws_config
from capo_endusermessaging._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.brand_profile_attribute_category
    import capo_endusermessaging.types.brand_profile_attribute_description
    import capo_endusermessaging.types.brand_profile_attribute_input_list
    import capo_endusermessaging.types.brand_profile_attribute_name
    import capo_endusermessaging.types.brand_profile_attribute_value
    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.brand_profile_name
    import capo_endusermessaging.types.channel_parameters
    import capo_endusermessaging.types.client_token
    import capo_endusermessaging.types.code_configuration_parameters
    import capo_endusermessaging.types.configuration_set_name
    import capo_endusermessaging.types.context_map
    import capo_endusermessaging.types.create_brand_profile_attributes_input
    import capo_endusermessaging.types.create_brand_profile_attributes_output
    import capo_endusermessaging.types.create_brand_profile_from_registration_input
    import capo_endusermessaging.types.create_brand_profile_from_registration_output
    import capo_endusermessaging.types.create_brand_profile_input
    import capo_endusermessaging.types.create_brand_profile_output
    import capo_endusermessaging.types.create_notify_code_configuration_input
    import capo_endusermessaging.types.create_notify_code_configuration_output
    import capo_endusermessaging.types.create_registrations_from_brand_profile_input
    import capo_endusermessaging.types.create_registrations_from_brand_profile_output
    import capo_endusermessaging.types.delete_brand_profile_attribute_input
    import capo_endusermessaging.types.delete_brand_profile_attribute_output
    import capo_endusermessaging.types.delete_brand_profile_input
    import capo_endusermessaging.types.delete_brand_profile_output
    import capo_endusermessaging.types.delete_notify_code_configuration_input
    import capo_endusermessaging.types.delete_notify_code_configuration_output
    import capo_endusermessaging.types.destination_identity
    import capo_endusermessaging.types.get_brand_profile_attribute_input
    import capo_endusermessaging.types.get_brand_profile_attribute_output
    import capo_endusermessaging.types.get_brand_profile_input
    import capo_endusermessaging.types.get_brand_profile_output
    import capo_endusermessaging.types.get_job_input
    import capo_endusermessaging.types.get_notify_code_configuration_input
    import capo_endusermessaging.types.get_notify_code_configuration_output
    import capo_endusermessaging.types.job
    import capo_endusermessaging.types.job_id
    import capo_endusermessaging.types.job_operation_type
    import capo_endusermessaging.types.job_status
    import capo_endusermessaging.types.list_brand_profile_attributes_input
    import capo_endusermessaging.types.list_brand_profile_attributes_output
    import capo_endusermessaging.types.list_brand_profiles_input
    import capo_endusermessaging.types.list_brand_profiles_output
    import capo_endusermessaging.types.list_jobs_input
    import capo_endusermessaging.types.list_jobs_output
    import capo_endusermessaging.types.list_notify_code_configurations_input
    import capo_endusermessaging.types.list_notify_code_configurations_output
    import capo_endusermessaging.types.list_registrations_from_brand_profile_input
    import capo_endusermessaging.types.list_registrations_from_brand_profile_output
    import capo_endusermessaging.types.list_tags_for_resource_input
    import capo_endusermessaging.types.list_tags_for_resource_output
    import capo_endusermessaging.types.max_results
    import capo_endusermessaging.types.next_token
    import capo_endusermessaging.types.notify_channel
    import capo_endusermessaging.types.notify_code_configuration_id_or_arn
    import capo_endusermessaging.types.notify_code_configuration_name
    import capo_endusermessaging.types.on_attribute_conflict
    import capo_endusermessaging.types.origination_identity
    import capo_endusermessaging.types.reference_id
    import capo_endusermessaging.types.registration_id_list
    import capo_endusermessaging.types.registration_id_or_arn
    import capo_endusermessaging.types.registration_type_list
    import capo_endusermessaging.types.send_notify_code_verification_input
    import capo_endusermessaging.types.send_notify_code_verification_output
    import capo_endusermessaging.types.tag_key_list
    import capo_endusermessaging.types.tag_list
    import capo_endusermessaging.types.tag_resource_input
    import capo_endusermessaging.types.tag_resource_output
    import capo_endusermessaging.types.untag_resource_input
    import capo_endusermessaging.types.untag_resource_output
    import capo_endusermessaging.types.update_brand_profile_attribute_input
    import capo_endusermessaging.types.update_brand_profile_attribute_output
    import capo_endusermessaging.types.update_brand_profile_from_registration_input
    import capo_endusermessaging.types.update_brand_profile_from_registration_output
    import capo_endusermessaging.types.update_brand_profile_input
    import capo_endusermessaging.types.update_brand_profile_output
    import capo_endusermessaging.types.update_channel_parameters
    import capo_endusermessaging.types.update_code_configuration_parameters
    import capo_endusermessaging.types.update_notify_code_configuration_input
    import capo_endusermessaging.types.update_notify_code_configuration_output
    import capo_endusermessaging.types.update_registrations_from_brand_profile_input
    import capo_endusermessaging.types.update_registrations_from_brand_profile_output
    import capo_endusermessaging.types.validate_notify_code_verification_input
    import capo_endusermessaging.types.validate_notify_code_verification_output
    import capo_endusermessaging.types.verification_code


class EndUserMessagingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class EndUserMessagingClient:
    """A client for the ``EndUserMessaging`` service.

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
        self._config = EndUserMessagingClientConfig(
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
        self, config_overrides: Optional[EndUserMessagingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EndUserMessagingClientConfig = config_overrides or {}
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

    def create_brand_profile(
        self,
        brand_profile_name: "capo_endusermessaging.types.brand_profile_name.BrandProfileName",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        client_token: Optional[
            "capo_endusermessaging.types.client_token.ClientToken"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
        tags: Optional["capo_endusermessaging.types.tag_list.TagList"] = None,
    ) -> "capo_endusermessaging.types.create_brand_profile_output.CreateBrandProfileOutput":
        """<p>Creates a brand profile. A brand profile is a lightweight container that holds your brand identity information as flexible attributes. After you create a brand profile, use the CreateBrandProfileAttributes operation to add company information, addresses, compliance documents, and logos.</p>

        Args:
            brand_profile_name: <p>The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>
            deletion_protection_enabled: <p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>
            tags: <p>An array of key and value pair tags that are associated with the resource.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a brand profile

            >>> client.create_brand_profile(brand_profile_name='AcmeCorp', deletion_protection_enabled=True)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.create_brand_profile_input.CreateBrandProfileInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.create_brand_profile_output.CreateBrandProfileOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.create_brand_profile

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.create_brand_profile.create_brand_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.create_brand_profile_input.CreateBrandProfileInput = {
            "brand_profile_name": brand_profile_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_brand_profile_attributes(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        attributes: "capo_endusermessaging.types.brand_profile_attribute_input_list.BrandProfileAttributeInputList",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        client_token: Optional[
            "capo_endusermessaging.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_endusermessaging.types.create_brand_profile_attributes_output.CreateBrandProfileAttributesOutput":
        """<p>Creates up to 10 attributes for a brand profile in a single request. For attributes of type IMAGE or DOCUMENT, the response includes a presigned Amazon S3 URL that you use to upload the media. This operation is atomic: either all of the attributes are created, or none of them are.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            attributes: <p>The brand profile attributes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a text attribute on a brand profile

            >>> client.create_brand_profile_attributes(brand_profile_id='bp-abc12345678901234', attributes=[{'attributeName': 'SupportEmail', 'attributeType': 'TEXT', 'attributeValue': 'support@example.com', 'category': 'CONTACT'}])
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.create_brand_profile_attributes_input.CreateBrandProfileAttributesInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.create_brand_profile_attributes_output.CreateBrandProfileAttributesOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.create_brand_profile_attributes

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.create_brand_profile_attributes.create_brand_profile_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.create_brand_profile_attributes_input.CreateBrandProfileAttributesInput = {
            "brand_profile_id": brand_profile_id,
            "attributes": attributes,
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

    def create_brand_profile_from_registration(
        self,
        registration_id: "capo_endusermessaging.types.registration_id_or_arn.RegistrationIdOrArn",
        brand_profile_name: "capo_endusermessaging.types.brand_profile_name.BrandProfileName",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        smart_match: Optional[bool] = None,
        tags: Optional["capo_endusermessaging.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_endusermessaging.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_endusermessaging.types.create_brand_profile_from_registration_output.CreateBrandProfileFromRegistrationOutput":
        """<p>Creates a brand profile and populates its attributes from an existing registration. This operation runs asynchronously. Use the GetJob operation to track its progress.</p>

        Args:
            registration_id: <p>The identifier or Amazon Resource Name (ARN) of the registration to populate the brand profile from.</p>
            brand_profile_name: <p>The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.</p>
            smart_match: <p>Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.</p>
            tags: <p>An array of key and value pair tags that are associated with the resource.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a brand profile from a registration

            >>> client.create_brand_profile_from_registration(registration_id='reg-abc12345678901234', brand_profile_name='AcmeCorp', smart_match=True)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.create_brand_profile_from_registration_input.CreateBrandProfileFromRegistrationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.create_brand_profile_from_registration_output.CreateBrandProfileFromRegistrationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.create_brand_profile_from_registration

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.create_brand_profile_from_registration.create_brand_profile_from_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.create_brand_profile_from_registration_input.CreateBrandProfileFromRegistrationInput = {
            "registration_id": registration_id,
            "brand_profile_name": brand_profile_name,
        }
        if smart_match is not None:
            input_["smart_match"] = smart_match
        if tags is not None:
            input_["tags"] = tags
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

    def create_notify_code_configuration(
        self,
        notify_code_configuration_name: "capo_endusermessaging.types.notify_code_configuration_name.NotifyCodeConfigurationName",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        code_configuration_parameters: Optional[
            "capo_endusermessaging.types.code_configuration_parameters.CodeConfigurationParameters"
        ] = None,
        channel_parameters: Optional[
            "capo_endusermessaging.types.channel_parameters.ChannelParameters"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
        client_token: Optional[
            "capo_endusermessaging.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_endusermessaging.types.tag_list.TagList"] = None,
    ) -> "capo_endusermessaging.types.create_notify_code_configuration_output.CreateNotifyCodeConfigurationOutput":
        """<p>Creates a notify code configuration. A notify code configuration is a reusable policy that defines how one-time passcodes are generated and rendered, including the code type, length, validity period, maximum number of attempts, and channel templates.</p>

        Args:
            notify_code_configuration_name: <p>The name of the notify code configuration.</p>
            code_configuration_parameters: <p>The passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. Each member is optional. When you omit a member, no value is applied at create time and the default is applied when a passcode is sent.</p>
            channel_parameters: <p>The channel-specific parameters used to render and deliver the one-time passcode. Provide parameters for any subset of channels. Each member configures one delivery route, and the route that is selected at send time uses the matching channel.</p>
            deletion_protection_enabled: <p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>
            tags: <p>An array of key and value pair tags that are associated with the resource.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a notify code configuration

            >>> client.create_notify_code_configuration(notify_code_configuration_name='SignupOtp', code_configuration_parameters={'codeType': 'NUMERIC', 'codeLength': 6, 'validityPeriodMinutes': 10, 'maxAttempts': 3}, channel_parameters={'text': {'inlineTemplateBody': 'Your verification code is {{code}}.'}})
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.create_notify_code_configuration_input.CreateNotifyCodeConfigurationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.create_notify_code_configuration_output.CreateNotifyCodeConfigurationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.create_notify_code_configuration

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.create_notify_code_configuration.create_notify_code_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.create_notify_code_configuration_input.CreateNotifyCodeConfigurationInput = {
            "notify_code_configuration_name": notify_code_configuration_name
        }
        if code_configuration_parameters is not None:
            input_["code_configuration_parameters"] = code_configuration_parameters
        if channel_parameters is not None:
            input_["channel_parameters"] = channel_parameters
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
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

    def create_registrations_from_brand_profile(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        registration_types: "capo_endusermessaging.types.registration_type_list.RegistrationTypeList",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        smart_match: Optional[bool] = None,
        client_token: Optional[
            "capo_endusermessaging.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_endusermessaging.types.create_registrations_from_brand_profile_output.CreateRegistrationsFromBrandProfileOutput":
        """<p>Creates one or more registrations in the DRAFT state and prefills their fields from the attributes of a brand profile. This operation runs asynchronously. Use the GetJob operation to track its progress.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            registration_types: <p>The registration types to create, for example US_TOLL_FREE_REGISTRATION or SENDER_ID.</p>
            smart_match: <p>Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create draft registrations from a brand profile

            >>> client.create_registrations_from_brand_profile(brand_profile_id='bp-abc12345678901234', registration_types=['US_TOLL_FREE_REGISTRATION'], smart_match=True)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.create_registrations_from_brand_profile_input.CreateRegistrationsFromBrandProfileInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.create_registrations_from_brand_profile_output.CreateRegistrationsFromBrandProfileOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.create_registrations_from_brand_profile

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.create_registrations_from_brand_profile.create_registrations_from_brand_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.create_registrations_from_brand_profile_input.CreateRegistrationsFromBrandProfileInput = {
            "brand_profile_id": brand_profile_id,
            "registration_types": registration_types,
        }
        if smart_match is not None:
            input_["smart_match"] = smart_match
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

    def delete_brand_profile(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.delete_brand_profile_output.DeleteBrandProfileOutput":
        """<p>Deletes a brand profile. This operation also deletes the attributes of the profile and any associated media. The request fails if deletion protection is enabled for the profile.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a brand profile

            >>> client.delete_brand_profile(brand_profile_id='bp-abc12345678901234')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.delete_brand_profile_input.DeleteBrandProfileInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.delete_brand_profile_output.DeleteBrandProfileOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.delete_brand_profile

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.delete_brand_profile.delete_brand_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.delete_brand_profile_input.DeleteBrandProfileInput = {
            "brand_profile_id": brand_profile_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_brand_profile_attribute(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.delete_brand_profile_attribute_output.DeleteBrandProfileAttributeOutput":
        """<p>Deletes a brand profile attribute. If the attribute stores media, this operation also deletes the associated media.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            attribute_name: <p>The name of the brand profile attribute. The name is unique within a brand profile.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a brand profile attribute

            >>> client.delete_brand_profile_attribute(brand_profile_id='bp-abc12345678901234', attribute_name='SupportEmail')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.delete_brand_profile_attribute_input.DeleteBrandProfileAttributeInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.delete_brand_profile_attribute_output.DeleteBrandProfileAttributeOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.delete_brand_profile_attribute

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.delete_brand_profile_attribute.delete_brand_profile_attribute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.delete_brand_profile_attribute_input.DeleteBrandProfileAttributeInput = {
            "brand_profile_id": brand_profile_id,
            "attribute_name": attribute_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_notify_code_configuration(
        self,
        notify_code_configuration_id: "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.delete_notify_code_configuration_output.DeleteNotifyCodeConfigurationOutput":
        """<p>Deletes a notify code configuration. Verifications that are already in progress are not affected, because they capture the policy at the time that the passcode was sent.</p>

        Args:
            notify_code_configuration_id: <p>The unique identifier of the notify code configuration. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a notify code configuration

            >>> client.delete_notify_code_configuration(notify_code_configuration_id='ncc-abc12345678901234')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.delete_notify_code_configuration_input.DeleteNotifyCodeConfigurationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.delete_notify_code_configuration_output.DeleteNotifyCodeConfigurationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.delete_notify_code_configuration

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.delete_notify_code_configuration.delete_notify_code_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.delete_notify_code_configuration_input.DeleteNotifyCodeConfigurationInput = {
            "notify_code_configuration_id": notify_code_configuration_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_brand_profile(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.get_brand_profile_output.GetBrandProfileOutput":
        """<p>Retrieves the metadata for a brand profile, including its name, status, deletion protection setting, and timestamps. To retrieve the attributes of the profile, use the ListBrandProfileAttributes operation.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a brand profile

            >>> client.get_brand_profile(brand_profile_id='bp-abc12345678901234')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.get_brand_profile_input.GetBrandProfileInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.get_brand_profile_output.GetBrandProfileOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.get_brand_profile

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.get_brand_profile.get_brand_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.get_brand_profile_input.GetBrandProfileInput = {
            "brand_profile_id": brand_profile_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_brand_profile_attribute(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.get_brand_profile_attribute_output.GetBrandProfileAttributeOutput":
        """<p>Retrieves a single brand profile attribute.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            attribute_name: <p>The name of the brand profile attribute. The name is unique within a brand profile.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a brand profile attribute

            >>> client.get_brand_profile_attribute(brand_profile_id='bp-abc12345678901234', attribute_name='SupportEmail')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.get_brand_profile_attribute_input.GetBrandProfileAttributeInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.get_brand_profile_attribute_output.GetBrandProfileAttributeOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.get_brand_profile_attribute

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.get_brand_profile_attribute.get_brand_profile_attribute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.get_brand_profile_attribute_input.GetBrandProfileAttributeInput = {
            "brand_profile_id": brand_profile_id,
            "attribute_name": attribute_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_job(
        self,
        job_id: "capo_endusermessaging.types.job_id.JobId",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.job.Job":
        """<p>Retrieves the current state of an asynchronous job, including its status and any resources that it created or updated.</p>

        Args:
            job_id: <p>The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an async job

            >>> client.get_job(job_id='job-abc12345678901234')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.get_job_input.GetJobInput]",
        ) -> OperationResponse["capo_endusermessaging.types.job.Job"]:
            import capo_endusermessaging._operations.end_user_messaging.get_job

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.get_job.get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.get_job_input.GetJobInput = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_notify_code_configuration(
        self,
        notify_code_configuration_id: "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.get_notify_code_configuration_output.GetNotifyCodeConfigurationOutput":
        """<p>Retrieves a notify code configuration.</p>

        Args:
            notify_code_configuration_id: <p>The unique identifier of the notify code configuration. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a notify code configuration

            >>> client.get_notify_code_configuration(notify_code_configuration_id='ncc-abc12345678901234')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.get_notify_code_configuration_input.GetNotifyCodeConfigurationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.get_notify_code_configuration_output.GetNotifyCodeConfigurationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.get_notify_code_configuration

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.get_notify_code_configuration.get_notify_code_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.get_notify_code_configuration_input.GetNotifyCodeConfigurationInput = {
            "notify_code_configuration_id": notify_code_configuration_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_brand_profile_attributes(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        next_token: Optional["capo_endusermessaging.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_endusermessaging.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_endusermessaging.types.list_brand_profile_attributes_output.ListBrandProfileAttributesOutput":
        """<p>Retrieves a paginated list of the attributes for a brand profile.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            next_token: <p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List brand profile attributes

            >>> client.list_brand_profile_attributes(brand_profile_id='bp-abc12345678901234', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.list_brand_profile_attributes_input.ListBrandProfileAttributesInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.list_brand_profile_attributes_output.ListBrandProfileAttributesOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.list_brand_profile_attributes

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.list_brand_profile_attributes.list_brand_profile_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.list_brand_profile_attributes_input.ListBrandProfileAttributesInput = {
            "brand_profile_id": brand_profile_id
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

    def list_brand_profiles(
        self,
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        next_token: Optional["capo_endusermessaging.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_endusermessaging.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_endusermessaging.types.list_brand_profiles_output.ListBrandProfilesOutput"
    ):
        """<p>Retrieves a paginated list of the brand profiles in your account. Use the nextToken parameter to retrieve additional results.</p>

        Args:
            next_token: <p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List brand profiles

            >>> client.list_brand_profiles(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.list_brand_profiles_input.ListBrandProfilesInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.list_brand_profiles_output.ListBrandProfilesOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.list_brand_profiles

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.list_brand_profiles.list_brand_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.list_brand_profiles_input.ListBrandProfilesInput = {}
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

    def list_jobs(
        self,
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        max_results: Optional[
            "capo_endusermessaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_endusermessaging.types.next_token.NextToken"] = None,
        status: Optional["capo_endusermessaging.types.job_status.JobStatus"] = None,
        brand_profile_id: Optional[
            "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
        ] = None,
        operation_type: Optional[
            "capo_endusermessaging.types.job_operation_type.JobOperationType"
        ] = None,
    ) -> "capo_endusermessaging.types.list_jobs_output.ListJobsOutput":
        """<p>Retrieves a paginated list of the asynchronous jobs in your account. You can filter the results by status, brand profile, or operation type.</p>

        Args:
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>
            status: <p>Filters the results to jobs that have the specified status.</p>
            brand_profile_id: <p>Filters the results to jobs for the specified brand profile.</p>
            operation_type: <p>Filters the results to jobs of the specified operation type.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List async jobs

            >>> client.list_jobs(max_results=10, status='SUCCESS')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.list_jobs_input.ListJobsInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.list_jobs_output.ListJobsOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.list_jobs

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.list_jobs_input.ListJobsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status
        if brand_profile_id is not None:
            input_["brand_profile_id"] = brand_profile_id
        if operation_type is not None:
            input_["operation_type"] = operation_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_notify_code_configurations(
        self,
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        max_results: Optional[
            "capo_endusermessaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_endusermessaging.types.next_token.NextToken"] = None,
    ) -> "capo_endusermessaging.types.list_notify_code_configurations_output.ListNotifyCodeConfigurationsOutput":
        """<p>Retrieves a paginated list of the notify code configurations in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List notify code configurations

            >>> client.list_notify_code_configurations(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.list_notify_code_configurations_input.ListNotifyCodeConfigurationsInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.list_notify_code_configurations_output.ListNotifyCodeConfigurationsOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.list_notify_code_configurations

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.list_notify_code_configurations.list_notify_code_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.list_notify_code_configurations_input.ListNotifyCodeConfigurationsInput = {}
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

    def list_registrations_from_brand_profile(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        max_results: Optional[
            "capo_endusermessaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_endusermessaging.types.next_token.NextToken"] = None,
    ) -> "capo_endusermessaging.types.list_registrations_from_brand_profile_output.ListRegistrationsFromBrandProfileOutput":
        """<p>Retrieves a paginated list of the registrations that were created from a brand profile through the synchronization operations.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List registrations created from a brand profile

            >>> client.list_registrations_from_brand_profile(brand_profile_id='bp-abc12345678901234', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.list_registrations_from_brand_profile_input.ListRegistrationsFromBrandProfileInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.list_registrations_from_brand_profile_output.ListRegistrationsFromBrandProfileOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.list_registrations_from_brand_profile

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.list_registrations_from_brand_profile.list_registrations_from_brand_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.list_registrations_from_brand_profile_input.ListRegistrationsFromBrandProfileInput = {
            "brand_profile_id": brand_profile_id
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Retrieves the tags that are associated with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List tags on a resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:end-user-messaging:us-east-1:123456789012:brand-profile/bp-abc12345678901234')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.list_tags_for_resource

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_notify_code_verification(
        self,
        channel: "capo_endusermessaging.types.notify_channel.NotifyChannel",
        destination_identity: "capo_endusermessaging.types.destination_identity.DestinationIdentity",
        origination_identity: "capo_endusermessaging.types.origination_identity.OriginationIdentity",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        notify_code_configuration: Optional[
            "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn"
        ] = None,
        override_channel_parameters: Optional[
            "capo_endusermessaging.types.channel_parameters.ChannelParameters"
        ] = None,
        override_code_configuration_parameters: Optional[
            "capo_endusermessaging.types.code_configuration_parameters.CodeConfigurationParameters"
        ] = None,
        configuration_set_name: Optional[
            "capo_endusermessaging.types.configuration_set_name.ConfigurationSetName"
        ] = None,
        context: Optional["capo_endusermessaging.types.context_map.ContextMap"] = None,
        reference_id: Optional[
            "capo_endusermessaging.types.reference_id.ReferenceId"
        ] = None,
    ) -> "capo_endusermessaging.types.send_notify_code_verification_output.SendNotifyCodeVerificationOutput":
        """<p>Generates a one-time passcode and delivers it to a recipient over the requested channel. The passcode policy is captured from the referenced notify code configuration at the time of the request, so later updates to the configuration do not affect verifications that are already in progress.</p>

        Args:
            channel: <p>The channel used to deliver the one-time passcode to the recipient.</p>
            destination_identity: <p>The recipient identifier. For the TEXT and VOICE channels, specify an E.164 phone number. For the WhatsApp channel, specify a WhatsApp address.</p>
            origination_identity: <p>The identity used to send the message, such as a phone number, sender ID, or pool that is owned by your account.</p>
            notify_code_configuration: <p>The identifier or Amazon Resource Name (ARN) of the notify code configuration that supplies the passcode policy and template defaults. When you do not specify a configuration, you must supply the template in the request.</p>
            override_channel_parameters: <p>The channel-specific parameters used to render and deliver the one-time passcode for this request. The route that is derived from the channel and the origination identity selects the matching channel. When you do not specify channel parameters, the service uses the parameters from the referenced notify code configuration.</p>
            override_code_configuration_parameters: <p>The per-send overrides for the passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. These values override the values from the referenced notify code configuration. When you do not specify a value, the value from the configuration is used, and if neither is set, the service default applies.</p>
            configuration_set_name: <p>The name of the configuration set used to control how delivery events for the message are handled.</p>
            context: <p>A map of custom key and value pairs that are propagated to the delivery events for this verification.</p>
            reference_id: <p>A caller-supplied reference identifier that binds a send request to a later validate request. Specify the same value in both requests.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Send a one-time passcode over SMS

            >>> client.send_notify_code_verification(channel='TEXT', destination_identity='+14255550100', origination_identity='arn:aws:sms-voice:us-east-1:123456789012:phone-number/pn-abc123', notify_code_configuration='ncc-abc12345678901234', reference_id='signup-flow-42')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.send_notify_code_verification_input.SendNotifyCodeVerificationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.send_notify_code_verification_output.SendNotifyCodeVerificationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.send_notify_code_verification

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.send_notify_code_verification.send_notify_code_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.send_notify_code_verification_input.SendNotifyCodeVerificationInput = {
            "channel": channel,
            "destination_identity": destination_identity,
            "origination_identity": origination_identity,
        }
        if notify_code_configuration is not None:
            input_["notify_code_configuration"] = notify_code_configuration
        if override_channel_parameters is not None:
            input_["override_channel_parameters"] = override_channel_parameters
        if override_code_configuration_parameters is not None:
            input_["override_code_configuration_parameters"] = (
                override_code_configuration_parameters
            )
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if context is not None:
            input_["context"] = context
        if reference_id is not None:
            input_["reference_id"] = reference_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_endusermessaging.types.tag_list.TagList",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.tag_resource_output.TagResourceOutput":
        """<p>Adds or overwrites the tags on a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>An array of key and value pair tags that are associated with the resource.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Tag a resource

            >>> client.tag_resource(resource_arn='arn:aws:end-user-messaging:us-east-1:123456789012:brand-profile/bp-abc12345678901234', tags=[{'key': 'Environment', 'value': 'Production'}])
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.tag_resource

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_endusermessaging.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
    ) -> "capo_endusermessaging.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove tags from a resource

            >>> client.untag_resource(resource_arn='arn:aws:end-user-messaging:us-east-1:123456789012:brand-profile/bp-abc12345678901234', tag_keys=['Environment'])
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.untag_resource

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.untag_resource_input.UntagResourceInput = {
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

    def update_brand_profile(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        brand_profile_name: Optional[
            "capo_endusermessaging.types.brand_profile_name.BrandProfileName"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
    ) -> "capo_endusermessaging.types.update_brand_profile_output.UpdateBrandProfileOutput":
        """<p>Updates the name or the deletion protection setting of a brand profile. To change the information that is stored in the profile, use the brand profile attribute operations.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            brand_profile_name: <p>The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.</p>
            deletion_protection_enabled: <p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a brand profile name

            >>> client.update_brand_profile(brand_profile_id='bp-abc12345678901234', brand_profile_name='AcmeCorpUpdated', deletion_protection_enabled=False)
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.update_brand_profile_input.UpdateBrandProfileInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.update_brand_profile_output.UpdateBrandProfileOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.update_brand_profile

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.update_brand_profile.update_brand_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.update_brand_profile_input.UpdateBrandProfileInput = {
            "brand_profile_id": brand_profile_id
        }
        if brand_profile_name is not None:
            input_["brand_profile_name"] = brand_profile_name
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_brand_profile_attribute(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        attribute_name: "capo_endusermessaging.types.brand_profile_attribute_name.BrandProfileAttributeName",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        attribute_value: Optional[
            "capo_endusermessaging.types.brand_profile_attribute_value.BrandProfileAttributeValue"
        ] = None,
        attachment_body: Optional[bytes] = None,
        description: Optional[
            "capo_endusermessaging.types.brand_profile_attribute_description.BrandProfileAttributeDescription"
        ] = None,
        category: Optional[
            "capo_endusermessaging.types.brand_profile_attribute_category.BrandProfileAttributeCategory"
        ] = None,
    ) -> "capo_endusermessaging.types.update_brand_profile_attribute_output.UpdateBrandProfileAttributeOutput":
        """<p>Updates the value, description, or category of an existing brand profile attribute.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            attribute_name: <p>The name of the brand profile attribute. The name is unique within a brand profile.</p>
            attribute_value: <p>The text value of the attribute. This value applies to attributes of type TEXT.</p>
            attachment_body: <p>The binary content for an attribute of type IMAGE or DOCUMENT. The content is base64-encoded when it is sent over the wire.</p>
            description: <p>A description of the attribute.</p>
            category: <p>The category of the attribute.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a brand profile attribute value

            >>> client.update_brand_profile_attribute(brand_profile_id='bp-abc12345678901234', attribute_name='SupportEmail', attribute_value='help@example.com', category='CONTACT')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.update_brand_profile_attribute_input.UpdateBrandProfileAttributeInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.update_brand_profile_attribute_output.UpdateBrandProfileAttributeOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.update_brand_profile_attribute

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.update_brand_profile_attribute.update_brand_profile_attribute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.update_brand_profile_attribute_input.UpdateBrandProfileAttributeInput = {
            "brand_profile_id": brand_profile_id,
            "attribute_name": attribute_name,
        }
        if attribute_value is not None:
            input_["attribute_value"] = attribute_value
        if attachment_body is not None:
            input_["attachment_body"] = attachment_body
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_brand_profile_from_registration(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        registration_id: "capo_endusermessaging.types.registration_id_or_arn.RegistrationIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        smart_match: Optional[bool] = None,
        on_attribute_conflict: Optional[
            "capo_endusermessaging.types.on_attribute_conflict.OnAttributeConflict"
        ] = None,
        client_token: Optional[
            "capo_endusermessaging.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_endusermessaging.types.update_brand_profile_from_registration_output.UpdateBrandProfileFromRegistrationOutput":
        """<p>Imports or refreshes the attributes of an existing brand profile from an existing registration. This operation runs asynchronously. Use the GetJob operation to track its progress.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            registration_id: <p>The identifier or Amazon Resource Name (ARN) of the registration to import attributes from.</p>
            smart_match: <p>Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.</p>
            on_attribute_conflict: <p>Specifies how the service resolves an attribute that already exists. REPLACE overwrites the existing value with the incoming value. PRESERVE keeps the existing value.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a brand profile from a registration

            >>> client.update_brand_profile_from_registration(brand_profile_id='bp-abc12345678901234', registration_id='reg-abc12345678901234', smart_match=True, on_attribute_conflict='REPLACE')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.update_brand_profile_from_registration_input.UpdateBrandProfileFromRegistrationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.update_brand_profile_from_registration_output.UpdateBrandProfileFromRegistrationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.update_brand_profile_from_registration

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.update_brand_profile_from_registration.update_brand_profile_from_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.update_brand_profile_from_registration_input.UpdateBrandProfileFromRegistrationInput = {
            "brand_profile_id": brand_profile_id,
            "registration_id": registration_id,
        }
        if smart_match is not None:
            input_["smart_match"] = smart_match
        if on_attribute_conflict is not None:
            input_["on_attribute_conflict"] = on_attribute_conflict
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

    def update_notify_code_configuration(
        self,
        notify_code_configuration_id: "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        notify_code_configuration_name: Optional[
            "capo_endusermessaging.types.notify_code_configuration_name.NotifyCodeConfigurationName"
        ] = None,
        code_configuration_parameters: Optional[
            "capo_endusermessaging.types.update_code_configuration_parameters.UpdateCodeConfigurationParameters"
        ] = None,
        channel_parameters: Optional[
            "capo_endusermessaging.types.update_channel_parameters.UpdateChannelParameters"
        ] = None,
        deletion_protection_enabled: Optional[bool] = None,
    ) -> "capo_endusermessaging.types.update_notify_code_configuration_output.UpdateNotifyCodeConfigurationOutput":
        """<p>Updates the mutable fields of a notify code configuration. Only the fields that you supply are changed. For the template and language fields, supplying an empty value clears the currently stored value.</p>

        Args:
            notify_code_configuration_id: <p>The unique identifier of the notify code configuration. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            notify_code_configuration_name: <p>The name of the notify code configuration.</p>
            code_configuration_parameters: <p>The updated passcode policy parameters, including the code type, length, validity period, and maximum number of attempts. When you omit a member, its current value is preserved.</p>
            channel_parameters: <p>The updated channel-specific parameters used to render and deliver the one-time passcode. This is a loose, nested update: when you omit a channel, that channel's parameters remain unchanged. Within a supplied channel, an empty string on a string member, or an empty map on the destination-country parameters, clears the currently stored value, and absent members preserve the current value.</p>
            deletion_protection_enabled: <p>Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a notify code configuration

            >>> client.update_notify_code_configuration(notify_code_configuration_id='ncc-abc12345678901234', code_configuration_parameters={'codeLength': 8, 'validityPeriodMinutes': 15})
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.update_notify_code_configuration_input.UpdateNotifyCodeConfigurationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.update_notify_code_configuration_output.UpdateNotifyCodeConfigurationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.update_notify_code_configuration

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.update_notify_code_configuration.update_notify_code_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.update_notify_code_configuration_input.UpdateNotifyCodeConfigurationInput = {
            "notify_code_configuration_id": notify_code_configuration_id
        }
        if notify_code_configuration_name is not None:
            input_["notify_code_configuration_name"] = notify_code_configuration_name
        if code_configuration_parameters is not None:
            input_["code_configuration_parameters"] = code_configuration_parameters
        if channel_parameters is not None:
            input_["channel_parameters"] = channel_parameters
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registrations_from_brand_profile(
        self,
        brand_profile_id: "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn",
        registration_ids: "capo_endusermessaging.types.registration_id_list.RegistrationIdList",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        smart_match: Optional[bool] = None,
        on_attribute_conflict: Optional[
            "capo_endusermessaging.types.on_attribute_conflict.OnAttributeConflict"
        ] = None,
        client_token: Optional[
            "capo_endusermessaging.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_endusermessaging.types.update_registrations_from_brand_profile_output.UpdateRegistrationsFromBrandProfileOutput":
        """<p>Repushes the attributes of a brand profile into existing DRAFT registrations. This operation runs asynchronously. Use the GetJob operation to track its progress.</p>

        Args:
            brand_profile_id: <p>The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>
            registration_ids: <p>The identifiers of the registrations.</p>
            smart_match: <p>Specifies whether to use semantic field mapping between brand profile attributes and registration fields. The default is true. When false, the service maps fields using a fixed set of standard field types.</p>
            on_attribute_conflict: <p>Specifies how the service resolves an attribute that already exists. REPLACE overwrites the existing value with the incoming value. PRESERVE keeps the existing value.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update registrations from a brand profile

            >>> client.update_registrations_from_brand_profile(brand_profile_id='bp-abc12345678901234', registration_ids=['reg-abc12345678901234'], smart_match=True, on_attribute_conflict='PRESERVE')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.update_registrations_from_brand_profile_input.UpdateRegistrationsFromBrandProfileInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.update_registrations_from_brand_profile_output.UpdateRegistrationsFromBrandProfileOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.update_registrations_from_brand_profile

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.update_registrations_from_brand_profile.update_registrations_from_brand_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.update_registrations_from_brand_profile_input.UpdateRegistrationsFromBrandProfileInput = {
            "brand_profile_id": brand_profile_id,
            "registration_ids": registration_ids,
        }
        if smart_match is not None:
            input_["smart_match"] = smart_match
        if on_attribute_conflict is not None:
            input_["on_attribute_conflict"] = on_attribute_conflict
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

    def validate_notify_code_verification(
        self,
        destination_identity: "capo_endusermessaging.types.destination_identity.DestinationIdentity",
        code: "capo_endusermessaging.types.verification_code.VerificationCode",
        *,
        config_overrides: Optional[EndUserMessagingClientConfig] = None,
        reference_id: Optional[
            "capo_endusermessaging.types.reference_id.ReferenceId"
        ] = None,
    ) -> "capo_endusermessaging.types.validate_notify_code_verification_output.ValidateNotifyCodeVerificationOutput":
        """<p>Validates a one-time passcode that a recipient submitted. Validation succeeds when the passcode matches, the validity period has not elapsed, and the maximum number of attempts has not been exceeded.</p>

        Args:
            destination_identity: <p>The recipient identifier. For the TEXT and VOICE channels, specify an E.164 phone number. For the WhatsApp channel, specify a WhatsApp address.</p>
            reference_id: <p>The caller-supplied reference identifier used to locate the verification. This value must match the value that you supplied to the SendNotifyCodeVerification operation.</p>
            code: <p>The one-time passcode that the recipient submitted for validation.</p>

        Raises:
            capo_endusermessaging.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_endusermessaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_endusermessaging.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed request rate.</p>
            capo_endusermessaging.errors.validation_exception.ValidationException: A standard error for input validation failures. This should be thrown by services when a member of the input structure falls outside of the modeled or documented constraints.
            capo_endusermessaging.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Validate a submitted one-time passcode

            >>> client.validate_notify_code_verification(destination_identity='+14255550100', reference_id='signup-flow-42', code='123456')
        """

        def _handler(
            req: "OperationRequest[capo_endusermessaging.types.validate_notify_code_verification_input.ValidateNotifyCodeVerificationInput]",
        ) -> OperationResponse[
            "capo_endusermessaging.types.validate_notify_code_verification_output.ValidateNotifyCodeVerificationOutput"
        ]:
            import capo_endusermessaging._operations.end_user_messaging.validate_notify_code_verification

            output, http_response = (
                capo_endusermessaging._operations.end_user_messaging.validate_notify_code_verification.validate_notify_code_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_endusermessaging.types.validate_notify_code_verification_input.ValidateNotifyCodeVerificationInput = {
            "destination_identity": destination_identity,
            "code": code,
        }
        if reference_id is not None:
            input_["reference_id"] = reference_id

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
