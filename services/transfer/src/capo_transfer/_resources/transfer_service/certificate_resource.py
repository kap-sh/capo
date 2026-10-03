from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_transfer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_transfer.types.cert_date
    import capo_transfer.types.certificate_body_type
    import capo_transfer.types.certificate_chain_type
    import capo_transfer.types.certificate_id
    import capo_transfer.types.certificate_usage_type
    import capo_transfer.types.delete_certificate_request
    import capo_transfer.types.describe_certificate_request
    import capo_transfer.types.describe_certificate_response
    import capo_transfer.types.description
    import capo_transfer.types.import_certificate_request
    import capo_transfer.types.import_certificate_response
    import capo_transfer.types.list_certificates_request
    import capo_transfer.types.list_certificates_response
    import capo_transfer.types.listed_certificate
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.private_key_type
    import capo_transfer.types.tags
    import capo_transfer.types.update_certificate_request
    import capo_transfer.types.update_certificate_response
    from capo_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from capo_transfer._services.transfer import TransferClient, TransferClientConfig


class CertificateResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def create(
        self,
        usage: "capo_transfer.types.certificate_usage_type.CertificateUsageType",
        certificate: "capo_transfer.types.certificate_body_type.CertificateBodyType",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        certificate_chain: Optional[
            "capo_transfer.types.certificate_chain_type.CertificateChainType"
        ] = None,
        private_key: Optional[
            "capo_transfer.types.private_key_type.PrivateKeyType"
        ] = None,
        active_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        inactive_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.import_certificate_response.ImportCertificateResponse":
        """<p>Imports the signing and encryption certificates that you need to create local (AS2) profiles and partner profiles.</p> <p>You can import both the certificate and its chain in the <code>Certificate</code> parameter.</p> <p>After importing a certificate, Transfer Family automatically creates a Amazon CloudWatch metric called <code>DaysUntilExpiry</code> that tracks the number of days until the certificate expires. The metric is based on the <code>InactiveDate</code> parameter and is published daily in the <code>AWS/Transfer</code> namespace.</p> <important> <p>It can take up to a full day after importing a certificate for Transfer Family to emit the <code>DaysUntilExpiry</code> metric to your account.</p> </important> <note> <p>If you use the <code>Certificate</code> parameter to upload both the certificate and its chain, don't use the <code>CertificateChain</code> parameter.</p> </note> <p> <b>CloudWatch monitoring</b> </p> <p>The <code>DaysUntilExpiry</code> metric includes the following specifications:</p> <ul> <li> <p> <b>Units:</b> Count (days)</p> </li> <li> <p> <b>Dimensions:</b> <code>CertificateId</code> (always present), <code>Description</code> (if provided during certificate import)</p> </li> <li> <p> <b>Statistics:</b> Minimum, Maximum, Average</p> </li> <li> <p> <b>Frequency:</b> Published daily</p> </li> </ul>

        Args:
            usage: <p>Specifies how this certificate is used. It can be used in the following ways:</p> <ul> <li> <p> <code>SIGNING</code>: For signing AS2 messages</p> </li> <li> <p> <code>ENCRYPTION</code>: For encrypting AS2 messages</p> </li> <li> <p> <code>TLS</code>: For securing AS2 communications sent over HTTPS</p> </li> </ul>
            certificate: <ul> <li> <p>For the CLI, provide a file path for a certificate in URI format. For example, <code>--certificate file://encryption-cert.pem</code>. Alternatively, you can provide the raw content.</p> </li> <li> <p>For the SDK, specify the raw content of a certificate file. For example, <code>--certificate "`cat encryption-cert.pem`"</code>.</p> </li> </ul> <note> <p>You can provide both the certificate and its chain in this parameter, without needing to use the <code>CertificateChain</code> parameter. If you use this parameter for both the certificate and its chain, do not use the <code>CertificateChain</code> parameter.</p> </note>
            certificate_chain: <p>An optional list of certificates that make up the chain for the certificate that's being imported.</p>
            private_key: <ul> <li> <p>For the CLI, provide a file path for a private key in URI format. For example, <code>--private-key file://encryption-key.pem</code>. Alternatively, you can provide the raw content of the private key file.</p> </li> <li> <p>For the SDK, specify the raw content of a private key file. For example, <code>--private-key "`cat encryption-key.pem`"</code> </p> </li> </ul>
            active_date: <p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>
            inactive_date: <p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>
            description: <p>A short description that helps identify the certificate. </p>
            tags: <p>Key-value pairs that can be used to group and search for certificates.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.import_certificate_request.ImportCertificateRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.import_certificate_response.ImportCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.import_certificate

            output, http_response = (
                capo_transfer._operations.transfer_service.import_certificate.import_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.import_certificate_request.ImportCertificateRequest = {
            "usage": usage,
            "certificate": certificate,
        }
        if certificate_chain is not None:
            input_["certificate_chain"] = certificate_chain
        if private_key is not None:
            input_["private_key"] = private_key
        if active_date is not None:
            input_["active_date"] = active_date
        if inactive_date is not None:
            input_["inactive_date"] = inactive_date
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

    def read(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> (
        "capo_transfer.types.describe_certificate_response.DescribeCertificateResponse"
    ):
        """<p>Describes the certificate that's identified by the <code>CertificateId</code>.</p> <note> <p>Transfer Family automatically publishes a Amazon CloudWatch metric called <code>DaysUntilExpiry</code> for imported certificates. This metric tracks the number of days until the certificate expires based on the <code>InactiveDate</code>. The metric is available in the <code>AWS/Transfer</code> namespace and includes the <code>CertificateId</code> as a dimension.</p> </note>

        Args:
            certificate_id: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.describe_certificate_request.DescribeCertificateRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.describe_certificate_response.DescribeCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_certificate

            output, http_response = (
                capo_transfer._operations.transfer_service.describe_certificate.describe_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_certificate_request.DescribeCertificateRequest = {
            "certificate_id": certificate_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        active_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        inactive_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
    ) -> "capo_transfer.types.update_certificate_response.UpdateCertificateResponse":
        """<p>Updates the active and inactive dates for a certificate.</p>

        Args:
            certificate_id: <p>The identifier of the certificate object that you are updating.</p>
            active_date: <p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>
            inactive_date: <p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>
            description: <p>A short description to help identify the certificate.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.update_certificate_request.UpdateCertificateRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.update_certificate_response.UpdateCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_certificate

            output, http_response = (
                capo_transfer._operations.transfer_service.update_certificate.update_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_certificate_request.UpdateCertificateRequest = {
            "certificate_id": certificate_id
        }
        if active_date is not None:
            input_["active_date"] = active_date
        if inactive_date is not None:
            input_["inactive_date"] = inactive_date
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the certificate that's specified in the <code>CertificateId</code> parameter.</p>

        Args:
            certificate_id: <p>The identifier of the certificate object that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.delete_certificate_request.DeleteCertificateRequest]",
        ) -> OperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_certificate

            output, http_response = (
                capo_transfer._operations.transfer_service.delete_certificate.delete_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_certificate_request.DeleteCertificateRequest = {
            "certificate_id": certificate_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_certificates_response.ListCertificatesResponse":
        """<p>Returns a list of the current certificates that have been imported into Transfer Family. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for the <code>NextToken</code> parameter, you can supply that value to continue listing certificates from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListCertificates</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional certificates.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.list_certificates_request.ListCertificatesRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.list_certificates_response.ListCertificatesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_certificates

            output, http_response = (
                capo_transfer._operations.transfer_service.list_certificates.list_certificates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_certificates_request.ListCertificatesRequest = {}
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


class AsyncCertificateResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def create(
        self,
        usage: "capo_transfer.types.certificate_usage_type.CertificateUsageType",
        certificate: "capo_transfer.types.certificate_body_type.CertificateBodyType",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate_chain: Optional[
            "capo_transfer.types.certificate_chain_type.CertificateChainType"
        ] = None,
        private_key: Optional[
            "capo_transfer.types.private_key_type.PrivateKeyType"
        ] = None,
        active_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        inactive_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.import_certificate_response.ImportCertificateResponse":
        """<p>Imports the signing and encryption certificates that you need to create local (AS2) profiles and partner profiles.</p> <p>You can import both the certificate and its chain in the <code>Certificate</code> parameter.</p> <p>After importing a certificate, Transfer Family automatically creates a Amazon CloudWatch metric called <code>DaysUntilExpiry</code> that tracks the number of days until the certificate expires. The metric is based on the <code>InactiveDate</code> parameter and is published daily in the <code>AWS/Transfer</code> namespace.</p> <important> <p>It can take up to a full day after importing a certificate for Transfer Family to emit the <code>DaysUntilExpiry</code> metric to your account.</p> </important> <note> <p>If you use the <code>Certificate</code> parameter to upload both the certificate and its chain, don't use the <code>CertificateChain</code> parameter.</p> </note> <p> <b>CloudWatch monitoring</b> </p> <p>The <code>DaysUntilExpiry</code> metric includes the following specifications:</p> <ul> <li> <p> <b>Units:</b> Count (days)</p> </li> <li> <p> <b>Dimensions:</b> <code>CertificateId</code> (always present), <code>Description</code> (if provided during certificate import)</p> </li> <li> <p> <b>Statistics:</b> Minimum, Maximum, Average</p> </li> <li> <p> <b>Frequency:</b> Published daily</p> </li> </ul>

        Args:
            usage: <p>Specifies how this certificate is used. It can be used in the following ways:</p> <ul> <li> <p> <code>SIGNING</code>: For signing AS2 messages</p> </li> <li> <p> <code>ENCRYPTION</code>: For encrypting AS2 messages</p> </li> <li> <p> <code>TLS</code>: For securing AS2 communications sent over HTTPS</p> </li> </ul>
            certificate: <ul> <li> <p>For the CLI, provide a file path for a certificate in URI format. For example, <code>--certificate file://encryption-cert.pem</code>. Alternatively, you can provide the raw content.</p> </li> <li> <p>For the SDK, specify the raw content of a certificate file. For example, <code>--certificate "`cat encryption-cert.pem`"</code>.</p> </li> </ul> <note> <p>You can provide both the certificate and its chain in this parameter, without needing to use the <code>CertificateChain</code> parameter. If you use this parameter for both the certificate and its chain, do not use the <code>CertificateChain</code> parameter.</p> </note>
            certificate_chain: <p>An optional list of certificates that make up the chain for the certificate that's being imported.</p>
            private_key: <ul> <li> <p>For the CLI, provide a file path for a private key in URI format. For example, <code>--private-key file://encryption-key.pem</code>. Alternatively, you can provide the raw content of the private key file.</p> </li> <li> <p>For the SDK, specify the raw content of a private key file. For example, <code>--private-key "`cat encryption-key.pem`"</code> </p> </li> </ul>
            active_date: <p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>
            inactive_date: <p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>
            description: <p>A short description that helps identify the certificate. </p>
            tags: <p>Key-value pairs that can be used to group and search for certificates.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.import_certificate_request.ImportCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.import_certificate_response.ImportCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.import_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.import_certificate.async_import_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.import_certificate_request.ImportCertificateRequest = {
            "usage": usage,
            "certificate": certificate,
        }
        if certificate_chain is not None:
            input_["certificate_chain"] = certificate_chain
        if private_key is not None:
            input_["private_key"] = private_key
        if active_date is not None:
            input_["active_date"] = active_date
        if inactive_date is not None:
            input_["inactive_date"] = inactive_date
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

    async def read(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> (
        "capo_transfer.types.describe_certificate_response.DescribeCertificateResponse"
    ):
        """<p>Describes the certificate that's identified by the <code>CertificateId</code>.</p> <note> <p>Transfer Family automatically publishes a Amazon CloudWatch metric called <code>DaysUntilExpiry</code> for imported certificates. This metric tracks the number of days until the certificate expires based on the <code>InactiveDate</code>. The metric is available in the <code>AWS/Transfer</code> namespace and includes the <code>CertificateId</code> as a dimension.</p> </note>

        Args:
            certificate_id: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_certificate_request.DescribeCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_certificate_response.DescribeCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_certificate.async_describe_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_certificate_request.DescribeCertificateRequest = {
            "certificate_id": certificate_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        active_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        inactive_date: Optional["capo_transfer.types.cert_date.CertDate"] = None,
        description: Optional["capo_transfer.types.description.Description"] = None,
    ) -> "capo_transfer.types.update_certificate_response.UpdateCertificateResponse":
        """<p>Updates the active and inactive dates for a certificate.</p>

        Args:
            certificate_id: <p>The identifier of the certificate object that you are updating.</p>
            active_date: <p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>
            inactive_date: <p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>
            description: <p>A short description to help identify the certificate.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_certificate_request.UpdateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_certificate_response.UpdateCertificateResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_certificate.async_update_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_certificate_request.UpdateCertificateRequest = {
            "certificate_id": certificate_id
        }
        if active_date is not None:
            input_["active_date"] = active_date
        if inactive_date is not None:
            input_["inactive_date"] = inactive_date
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        certificate_id: "capo_transfer.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the certificate that's specified in the <code>CertificateId</code> parameter.</p>

        Args:
            certificate_id: <p>The identifier of the certificate object that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_certificate_request.DeleteCertificateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_certificate

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_certificate.async_delete_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_certificate_request.DeleteCertificateRequest = {
            "certificate_id": certificate_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
    ) -> "capo_transfer.types.list_certificates_response.ListCertificatesResponse":
        """<p>Returns a list of the current certificates that have been imported into Transfer Family. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for the <code>NextToken</code> parameter, you can supply that value to continue listing certificates from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListCertificates</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional certificates.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_certificates_request.ListCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_certificates_response.ListCertificatesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_certificates

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_certificates.async_list_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_certificates_request.ListCertificatesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
