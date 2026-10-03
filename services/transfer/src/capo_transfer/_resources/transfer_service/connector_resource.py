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
    import capo_transfer.types.as2_connector_config
    import capo_transfer.types.connector_egress_config
    import capo_transfer.types.connector_id
    import capo_transfer.types.connector_security_policy_name
    import capo_transfer.types.connectors_ip_address_type
    import capo_transfer.types.create_connector_request
    import capo_transfer.types.create_connector_response
    import capo_transfer.types.delete_connector_request
    import capo_transfer.types.describe_connector_request
    import capo_transfer.types.describe_connector_response
    import capo_transfer.types.list_connectors_request
    import capo_transfer.types.list_connectors_response
    import capo_transfer.types.listed_connector
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.role
    import capo_transfer.types.sftp_connector_config
    import capo_transfer.types.tags
    import capo_transfer.types.update_connector_egress_config
    import capo_transfer.types.update_connector_request
    import capo_transfer.types.update_connector_response
    import capo_transfer.types.url
    from capo_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from capo_transfer._services.transfer import TransferClient, TransferClientConfig


class ConnectorResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def create(
        self,
        access_role: "capo_transfer.types.role.Role",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        url: Optional["capo_transfer.types.url.Url"] = None,
        as2_config: Optional[
            "capo_transfer.types.as2_connector_config.As2ConnectorConfig"
        ] = None,
        logging_role: Optional["capo_transfer.types.role.Role"] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        sftp_config: Optional[
            "capo_transfer.types.sftp_connector_config.SftpConnectorConfig"
        ] = None,
        security_policy_name: Optional[
            "capo_transfer.types.connector_security_policy_name.ConnectorSecurityPolicyName"
        ] = None,
        egress_config: Optional[
            "capo_transfer.types.connector_egress_config.ConnectorEgressConfig"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.connectors_ip_address_type.ConnectorsIpAddressType"
        ] = None,
    ) -> "capo_transfer.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates the connector, which captures the parameters for a connection for the AS2 or SFTP protocol. For AS2, the connector is required for sending files to an externally hosted AS2 server. For SFTP, the connector is required when sending files to an SFTP server or receiving files from an SFTP server. For more details about connectors, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/configure-as2-connector.html">Configure AS2 connectors</a> and <a href="https://docs.aws.amazon.com/transfer/latest/userguide/configure-sftp-connector.html">Create SFTP connectors</a>.</p> <note> <p>You must specify exactly one configuration object: either for AS2 (<code>As2Config</code>) or SFTP (<code>SftpConfig</code>).</p> </note>

        Args:
            url: <p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>
            as2_config: <p>A structure that contains the parameters for an AS2 connector object.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.</p>
            tags: <p>Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.</p>
            sftp_config: <p>A structure that contains the parameters for an SFTP connector object.</p>
            security_policy_name: <p>Specifies the name of the security policy for the connector.</p>
            egress_config: <p>Specifies the egress configuration for the connector, which determines how traffic is routed from the connector to the SFTP server. When set to VPC, enables routing through customer VPCs using VPC_LATTICE for private connectivity.</p>
            ip_address_type: <p>Specifies the IP address type for the connector's network connections. When set to <code>IPV4</code>, the connector uses IPv4 addresses only. When set to <code>DUALSTACK</code>, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.create_connector_request.CreateConnectorRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.create_connector_response.CreateConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_connector

            output, http_response = (
                capo_transfer._operations.transfer_service.create_connector.create_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_connector_request.CreateConnectorRequest = {
            "access_role": access_role
        }
        if url is not None:
            input_["url"] = url
        if as2_config is not None:
            input_["as2_config"] = as2_config
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if tags is not None:
            input_["tags"] = tags
        if sftp_config is not None:
            input_["sftp_config"] = sftp_config
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if egress_config is not None:
            input_["egress_config"] = egress_config
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_connector_response.DescribeConnectorResponse":
        """<p>Describes the connector that's identified by the <code>ConnectorId.</code> </p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.describe_connector_request.DescribeConnectorRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.describe_connector_response.DescribeConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_connector

            output, http_response = (
                capo_transfer._operations.transfer_service.describe_connector.describe_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_connector_request.DescribeConnectorRequest = {
            "connector_id": connector_id
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
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        url: Optional["capo_transfer.types.url.Url"] = None,
        as2_config: Optional[
            "capo_transfer.types.as2_connector_config.As2ConnectorConfig"
        ] = None,
        access_role: Optional["capo_transfer.types.role.Role"] = None,
        logging_role: Optional["capo_transfer.types.role.Role"] = None,
        sftp_config: Optional[
            "capo_transfer.types.sftp_connector_config.SftpConnectorConfig"
        ] = None,
        security_policy_name: Optional[
            "capo_transfer.types.connector_security_policy_name.ConnectorSecurityPolicyName"
        ] = None,
        egress_config: Optional[
            "capo_transfer.types.update_connector_egress_config.UpdateConnectorEgressConfig"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.connectors_ip_address_type.ConnectorsIpAddressType"
        ] = None,
    ) -> "capo_transfer.types.update_connector_response.UpdateConnectorResponse":
        """<p>Updates some of the parameters for an existing connector. Provide the <code>ConnectorId</code> for the connector that you want to update, along with the new values for the parameters to update.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            url: <p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>
            as2_config: <p>A structure that contains the parameters for an AS2 connector object.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.</p>
            sftp_config: <p>A structure that contains the parameters for an SFTP connector object.</p>
            security_policy_name: <p>Specifies the name of the security policy for the connector.</p>
            egress_config: <p>Updates the egress configuration for the connector, allowing you to modify how traffic is routed from the connector to the SFTP server. Changes to VPC configuration may require connector restart.</p>
            ip_address_type: <p>Specifies the IP address type for the connector's network connections. When set to <code>IPV4</code>, the connector uses IPv4 addresses only. When set to <code>DUALSTACK</code>, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.update_connector_request.UpdateConnectorRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.update_connector_response.UpdateConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_connector

            output, http_response = (
                capo_transfer._operations.transfer_service.update_connector.update_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_connector_request.UpdateConnectorRequest = {
            "connector_id": connector_id
        }
        if url is not None:
            input_["url"] = url
        if as2_config is not None:
            input_["as2_config"] = as2_config
        if access_role is not None:
            input_["access_role"] = access_role
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if sftp_config is not None:
            input_["sftp_config"] = sftp_config
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if egress_config is not None:
            input_["egress_config"] = egress_config
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the connector that's specified in the provided <code>ConnectorId</code>.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> OperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_connector

            output, http_response = (
                capo_transfer._operations.transfer_service.delete_connector.delete_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_id": connector_id
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
    ) -> "capo_transfer.types.list_connectors_response.ListConnectorsResponse":
        """<p>Lists the connectors for the specified Region.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListConnectors</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional connectors.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.list_connectors_request.ListConnectorsRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_connectors

            output, http_response = (
                capo_transfer._operations.transfer_service.list_connectors.list_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_connectors_request.ListConnectorsRequest = {}
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


class AsyncConnectorResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def create(
        self,
        access_role: "capo_transfer.types.role.Role",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        url: Optional["capo_transfer.types.url.Url"] = None,
        as2_config: Optional[
            "capo_transfer.types.as2_connector_config.As2ConnectorConfig"
        ] = None,
        logging_role: Optional["capo_transfer.types.role.Role"] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
        sftp_config: Optional[
            "capo_transfer.types.sftp_connector_config.SftpConnectorConfig"
        ] = None,
        security_policy_name: Optional[
            "capo_transfer.types.connector_security_policy_name.ConnectorSecurityPolicyName"
        ] = None,
        egress_config: Optional[
            "capo_transfer.types.connector_egress_config.ConnectorEgressConfig"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.connectors_ip_address_type.ConnectorsIpAddressType"
        ] = None,
    ) -> "capo_transfer.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates the connector, which captures the parameters for a connection for the AS2 or SFTP protocol. For AS2, the connector is required for sending files to an externally hosted AS2 server. For SFTP, the connector is required when sending files to an SFTP server or receiving files from an SFTP server. For more details about connectors, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/configure-as2-connector.html">Configure AS2 connectors</a> and <a href="https://docs.aws.amazon.com/transfer/latest/userguide/configure-sftp-connector.html">Create SFTP connectors</a>.</p> <note> <p>You must specify exactly one configuration object: either for AS2 (<code>As2Config</code>) or SFTP (<code>SftpConfig</code>).</p> </note>

        Args:
            url: <p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>
            as2_config: <p>A structure that contains the parameters for an AS2 connector object.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.</p>
            tags: <p>Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.</p>
            sftp_config: <p>A structure that contains the parameters for an SFTP connector object.</p>
            security_policy_name: <p>Specifies the name of the security policy for the connector.</p>
            egress_config: <p>Specifies the egress configuration for the connector, which determines how traffic is routed from the connector to the SFTP server. When set to VPC, enables routing through customer VPCs using VPC_LATTICE for private connectivity.</p>
            ip_address_type: <p>Specifies the IP address type for the connector's network connections. When set to <code>IPV4</code>, the connector uses IPv4 addresses only. When set to <code>DUALSTACK</code>, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_connector_response.CreateConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_connector_request.CreateConnectorRequest = {
            "access_role": access_role
        }
        if url is not None:
            input_["url"] = url
        if as2_config is not None:
            input_["as2_config"] = as2_config
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if tags is not None:
            input_["tags"] = tags
        if sftp_config is not None:
            input_["sftp_config"] = sftp_config
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if egress_config is not None:
            input_["egress_config"] = egress_config
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_connector_response.DescribeConnectorResponse":
        """<p>Describes the connector that's identified by the <code>ConnectorId.</code> </p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_connector_request.DescribeConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_connector_response.DescribeConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_connector.async_describe_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_connector_request.DescribeConnectorRequest = {
            "connector_id": connector_id
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
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        url: Optional["capo_transfer.types.url.Url"] = None,
        as2_config: Optional[
            "capo_transfer.types.as2_connector_config.As2ConnectorConfig"
        ] = None,
        access_role: Optional["capo_transfer.types.role.Role"] = None,
        logging_role: Optional["capo_transfer.types.role.Role"] = None,
        sftp_config: Optional[
            "capo_transfer.types.sftp_connector_config.SftpConnectorConfig"
        ] = None,
        security_policy_name: Optional[
            "capo_transfer.types.connector_security_policy_name.ConnectorSecurityPolicyName"
        ] = None,
        egress_config: Optional[
            "capo_transfer.types.update_connector_egress_config.UpdateConnectorEgressConfig"
        ] = None,
        ip_address_type: Optional[
            "capo_transfer.types.connectors_ip_address_type.ConnectorsIpAddressType"
        ] = None,
    ) -> "capo_transfer.types.update_connector_response.UpdateConnectorResponse":
        """<p>Updates some of the parameters for an existing connector. Provide the <code>ConnectorId</code> for the connector that you want to update, along with the new values for the parameters to update.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>
            url: <p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>
            as2_config: <p>A structure that contains the parameters for an AS2 connector object.</p>
            access_role: <p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.</p>
            sftp_config: <p>A structure that contains the parameters for an SFTP connector object.</p>
            security_policy_name: <p>Specifies the name of the security policy for the connector.</p>
            egress_config: <p>Updates the egress configuration for the connector, allowing you to modify how traffic is routed from the connector to the SFTP server. Changes to VPC configuration may require connector restart.</p>
            ip_address_type: <p>Specifies the IP address type for the connector's network connections. When set to <code>IPV4</code>, the connector uses IPv4 addresses only. When set to <code>DUALSTACK</code>, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_exists_exception.ResourceExistsException: <p>The requested resource does not exist, or exists in a region other than the one specified for the command.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_connector_request.UpdateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_connector_response.UpdateConnectorResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_connector.async_update_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_connector_request.UpdateConnectorRequest = {
            "connector_id": connector_id
        }
        if url is not None:
            input_["url"] = url
        if as2_config is not None:
            input_["as2_config"] = as2_config
        if access_role is not None:
            input_["access_role"] = access_role
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if sftp_config is not None:
            input_["sftp_config"] = sftp_config
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if egress_config is not None:
            input_["egress_config"] = egress_config
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        connector_id: "capo_transfer.types.connector_id.ConnectorId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the connector that's specified in the provided <code>ConnectorId</code>.</p>

        Args:
            connector_id: <p>The unique identifier for the connector.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_connector

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_id": connector_id
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
    ) -> "capo_transfer.types.list_connectors_response.ListConnectorsResponse":
        """<p>Lists the connectors for the specified Region.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When you can get additional results from the <code>ListConnectors</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional connectors.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_connectors

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_connectors_request.ListConnectorsRequest = {}
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
