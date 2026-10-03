from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.encryption_type
    import capo_iot_managed_integrations.types.get_default_encryption_configuration_request
    import capo_iot_managed_integrations.types.get_default_encryption_configuration_response
    import capo_iot_managed_integrations.types.kms_key_arn
    import capo_iot_managed_integrations.types.put_default_encryption_configuration_request
    import capo_iot_managed_integrations.types.put_default_encryption_configuration_response
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class KmsKeyAssociationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def get_default_encryption_configuration(
        self, *, config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None
    ) -> "capo_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse":
        """<p> Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified region. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html">Key management</a> in the <i>AWS IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration.get_default_encryption_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_default_encryption_configuration(
        self,
        encryption_type: "capo_iot_managed_integrations.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        kms_key_arn: Optional[
            "capo_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse":
        """<p>Sets the default encryption configuration for the Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html">Key management</a> in the AWS IoT SiteWise User Guide.</p>

        Args:
            encryption_type: <p>The type of encryption used for the encryption configuration.</p>
            kms_key_arn: <p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration.put_default_encryption_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest = {
            "encryption_type": encryption_type
        }
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncKmsKeyAssociationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def get_default_encryption_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse":
        """<p> Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified region. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html">Key management</a> in the <i>AWS IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration.async_get_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_default_encryption_configuration(
        self,
        encryption_type: "capo_iot_managed_integrations.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        kms_key_arn: Optional[
            "capo_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse":
        """<p>Sets the default encryption configuration for the Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html">Key management</a> in the AWS IoT SiteWise User Guide.</p>

        Args:
            encryption_type: <p>The type of encryption used for the encryption configuration.</p>
            kms_key_arn: <p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration.async_put_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest = {
            "encryption_type": encryption_type
        }
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
